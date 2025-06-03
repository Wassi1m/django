#!/bin/bash

# Script pour configurer l'infrastructure AWS pour le projet Hotel Management
# Ce script crée les clusters EKS, ECR, et autres ressources nécessaires

set -e

# Variables de configuration
AWS_REGION="eu-west-1"
PROJECT_NAME="hotel-management"
CLUSTER_VERSION="1.28"

echo "🚀 Configuration de l'infrastructure AWS pour $PROJECT_NAME"

# Vérifier que AWS CLI est installé et configuré
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier que eksctl est installé
if ! command -v eksctl &> /dev/null; then
    echo "❌ eksctl n'est pas installé. Installation en cours..."
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
    sudo mv /tmp/eksctl /usr/local/bin
fi

# Vérifier que kubectl est installé
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl n'est pas installé. Installation en cours..."
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/
fi

echo "✅ Outils vérifiés"

# 1. Créer le repository ECR
echo "📦 Création du repository ECR..."
aws ecr describe-repositories --repository-names $PROJECT_NAME --region $AWS_REGION 2>/dev/null || \
aws ecr create-repository --repository-name $PROJECT_NAME --region $AWS_REGION

echo "✅ Repository ECR créé"

# 2. Créer le cluster EKS de test
echo "🧪 Création du cluster EKS de test..."
eksctl create cluster \
  --name ${PROJECT_NAME}-test-cluster \
  --region $AWS_REGION \
  --version $CLUSTER_VERSION \
  --nodegroup-name test-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 4 \
  --managed \
  --with-oidc \
  --ssh-access \
  --ssh-public-key ~/.ssh/id_rsa.pub \
  --tags Environment=test,Project=$PROJECT_NAME

echo "✅ Cluster EKS de test créé"

# 3. Créer le cluster EKS de production
echo "🏭 Création du cluster EKS de production..."
eksctl create cluster \
  --name ${PROJECT_NAME}-prod-cluster \
  --region $AWS_REGION \
  --version $CLUSTER_VERSION \
  --nodegroup-name prod-nodes \
  --node-type t3.large \
  --nodes 3 \
  --nodes-min 2 \
  --nodes-max 10 \
  --managed \
  --with-oidc \
  --ssh-access \
  --ssh-public-key ~/.ssh/id_rsa.pub \
  --tags Environment=production,Project=$PROJECT_NAME

echo "✅ Cluster EKS de production créé"

# 4. Installer NGINX Ingress Controller
echo "🌐 Installation de NGINX Ingress Controller..."

# Pour le cluster de test
kubectl config use-context arn:aws:eks:$AWS_REGION:$(aws sts get-caller-identity --query Account --output text):cluster/${PROJECT_NAME}-test-cluster
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/aws/deploy.yaml

# Pour le cluster de production
kubectl config use-context arn:aws:eks:$AWS_REGION:$(aws sts get-caller-identity --query Account --output text):cluster/${PROJECT_NAME}-prod-cluster
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/aws/deploy.yaml

echo "✅ NGINX Ingress Controller installé"

# 5. Installer cert-manager pour les certificats SSL
echo "🔒 Installation de cert-manager..."

# Pour le cluster de test
kubectl config use-context arn:aws:eks:$AWS_REGION:$(aws sts get-caller-identity --query Account --output text):cluster/${PROJECT_NAME}-test-cluster
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml

# Pour le cluster de production
kubectl config use-context arn:aws:eks:$AWS_REGION:$(aws sts get-caller-identity --query Account --output text):cluster/${PROJECT_NAME}-prod-cluster
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml

echo "✅ cert-manager installé"

# 6. Créer les ClusterIssuer pour Let's Encrypt
echo "📜 Configuration des certificats SSL..."

cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com  # Remplacez par votre email
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
EOF

echo "✅ Configuration SSL terminée"

echo "🎉 Infrastructure AWS configurée avec succès!"
echo ""
echo "📋 Prochaines étapes:"
echo "1. Configurez vos secrets GitHub Actions:"
echo "   - AWS_ACCESS_KEY_ID"
echo "   - AWS_SECRET_ACCESS_KEY"
echo "2. Modifiez les domaines dans les fichiers ingress-patch.yaml"
echo "3. Configurez vos secrets de production dans k8s/environments/prod/secrets.env"
echo "4. Poussez votre code sur GitHub pour déclencher le déploiement"
echo ""
echo "🔗 URLs des clusters:"
echo "Test: https://test-hotel.yourdomain.com"
echo "Production: https://hotel.yourdomain.com" 