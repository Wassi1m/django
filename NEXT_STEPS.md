# 🎯 Prochaines Étapes - Déploiement Kubernetes

## ✅ Ce qui a été fait

Votre projet Django Hotel Management a été configuré avec une architecture Kubernetes complète :

- ✅ **Dockerfile** optimisé pour la production
- ✅ **Configuration Kubernetes** avec Kustomize (base + environnements)
- ✅ **Pipeline CI/CD** avec GitHub Actions
- ✅ **Scripts d'automatisation** pour AWS
- ✅ **Settings Django** adaptés pour la production
- ✅ **Documentation complète**

## 🚀 Ce que vous devez faire maintenant

### 1. Préparer AWS (30-45 minutes)

```bash
# 1. Installer AWS CLI si pas déjà fait
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# 2. Configurer AWS CLI
aws configure
# Entrez vos AWS Access Key ID, Secret Access Key, région (eu-west-1), format (json)

# 3. Exécuter le script d'infrastructure
chmod +x scripts/setup-aws-infrastructure.sh
./scripts/setup-aws-infrastructure.sh
```

### 2. Configurer GitHub (10 minutes)

1. **Pousser votre code sur GitHub** :
   ```bash
   git add .
   git commit -m "Add Kubernetes configuration"
   git push origin main
   ```

2. **Configurer les secrets GitHub** :
   - Allez sur votre repo GitHub
   - Settings > Secrets and variables > Actions
   - Ajoutez :
     - `AWS_ACCESS_KEY_ID` : Votre clé d'accès AWS
     - `AWS_SECRET_ACCESS_KEY` : Votre clé secrète AWS

### 3. Configurer les domaines (15 minutes)

1. **Modifiez les domaines** dans ces fichiers :
   - `k8s/environments/test/ingress-patch.yaml` (ligne 9 et 12)
   - `k8s/environments/prod/ingress-patch.yaml` (ligne 13 et 16)
   
   Remplacez `yourdomain.com` par votre vrai domaine.

2. **Configurez vos DNS** pour pointer vers les Load Balancers AWS qui seront créés.

### 4. Configurer les secrets de production (10 minutes)

1. **Générez une clé secrète Django** :
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Éditez** `k8s/environments/prod/secrets.env` :
   ```bash
   DJANGO_SECRET_KEY=votre-clé-générée-ici
   DB_PASSWORD=mot-de-passe-postgresql-sécurisé
   AWS_ACCESS_KEY_ID=votre-access-key
   AWS_SECRET_ACCESS_KEY=votre-secret-key
   ```

### 5. Créer la branche develop (5 minutes)

```bash
# Créer et pousser la branche develop pour les tests
git checkout -b develop
git push origin develop
```

## 🎉 Déploiement Automatique

Une fois ces étapes terminées :

- **Push sur `develop`** → Déploie automatiquement sur l'environnement de test
- **Push sur `main`** → Déploie automatiquement sur l'environnement de production

## 🔍 Vérification du Déploiement

### Commandes utiles :

```bash
# Voir les pods en cours d'exécution
kubectl get pods -A

# Voir les services
kubectl get services -A

# Voir les ingress et leurs URLs
kubectl get ingress -A

# Logs de l'application
kubectl logs -f deployment/prod-hotel-management-app -n hotel-management-prod
```

### URLs d'accès :

- **Test** : `https://test-hotel.yourdomain.com`
- **Production** : `https://hotel.yourdomain.com`

## 🆘 En cas de problème

1. **Consultez la documentation** : `KUBERNETES_DEPLOYMENT.md`
2. **Vérifiez les logs** des pods Kubernetes
3. **Consultez les Actions GitHub** pour voir les erreurs de déploiement
4. **Utilisez les scripts de dépannage** fournis dans la documentation

## 📊 Monitoring

Une fois déployé, vous pouvez :

- Voir les métriques dans AWS CloudWatch
- Configurer des alertes
- Utiliser `kubectl top` pour voir l'utilisation des ressources
- Configurer Sentry pour le monitoring des erreurs (optionnel)

---

**🎯 Objectif** : Avoir votre application Django déployée sur AWS EKS avec deux environnements fonctionnels en moins de 2 heures !

**📞 Support** : Consultez `KUBERNETES_DEPLOYMENT.md` pour plus de détails et de dépannage. 