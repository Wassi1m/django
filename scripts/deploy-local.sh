#!/bin/bash

# Script pour déployer localement avec Kubernetes (minikube ou kind)
# Utile pour tester avant de déployer sur AWS

set -e

ENVIRONMENT=${1:-test}  # test ou prod
PROJECT_NAME="hotel-management"

echo "🚀 Déploiement local de $PROJECT_NAME en environnement $ENVIRONMENT"

# Vérifier que kubectl est disponible
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl n'est pas installé"
    exit 1
fi

# Vérifier que kustomize est disponible
if ! command -v kustomize &> /dev/null; then
    echo "📦 Installation de Kustomize..."
    curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash
    sudo mv kustomize /usr/local/bin/
fi

# Construire l'image Docker localement
echo "🔨 Construction de l'image Docker..."
docker build -t hotel-management:local .

# Si on utilise minikube, charger l'image
if command -v minikube &> /dev/null && minikube status &> /dev/null; then
    echo "📤 Chargement de l'image dans minikube..."
    minikube image load hotel-management:local
fi

# Déployer avec Kustomize
echo "🚀 Déploiement avec Kustomize..."
cd k8s/environments/$ENVIRONMENT

# Modifier l'image pour utiliser la version locale
kustomize edit set image hotel-management=hotel-management:local

# Appliquer la configuration
kustomize build . | kubectl apply -f -

echo "⏳ Attente du déploiement..."
kubectl rollout status deployment/${ENVIRONMENT}-hotel-management-app -n hotel-management-${ENVIRONMENT} --timeout=300s

echo "✅ Déploiement terminé!"

# Afficher les informations de connexion
echo ""
echo "📋 Informations de connexion:"
echo "Namespace: hotel-management-${ENVIRONMENT}"
echo "Service: ${ENVIRONMENT}-hotel-management-service"

# Si on utilise minikube, afficher l'URL
if command -v minikube &> /dev/null && minikube status &> /dev/null; then
    echo "🌐 URL locale:"
    minikube service ${ENVIRONMENT}-hotel-management-service -n hotel-management-${ENVIRONMENT} --url
fi

echo ""
echo "🔍 Commandes utiles:"
echo "kubectl get pods -n hotel-management-${ENVIRONMENT}"
echo "kubectl logs -f deployment/${ENVIRONMENT}-hotel-management-app -n hotel-management-${ENVIRONMENT}"
echo "kubectl port-forward service/${ENVIRONMENT}-hotel-management-service 8080:80 -n hotel-management-${ENVIRONMENT}" 