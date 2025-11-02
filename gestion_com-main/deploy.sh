#!/bin/bash

# Script de déploiement Gestion Com Backend sur Google Cloud Run
set -e

echo "🚀 Déploiement Gestion Com Backend sur Google Cloud Run"
echo "========================================================"

# Configuration
PROJECT_ID="yaaprojects"
REGION="europe-west1"
SERVICE_NAME="gestion-com-backend"
REPOSITORY="cloud-run-source-deploy"
IMAGE_NAME="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${SERVICE_NAME}"
CLOUD_SQL_INSTANCE="yaaprojects:europe-west1:gestion-com-postgres"

echo "📋 Configuration:"
echo "   Projet: ${PROJECT_ID}"
echo "   Région: ${REGION}"
echo "   Service: ${SERVICE_NAME}"
echo ""

# 1. Configuration du projet
echo "📋 Configuration du projet Google Cloud..."
gcloud config set project ${PROJECT_ID}

# 2. Activation des APIs nécessaires
echo "🔧 Activation des APIs..."
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com

# 3. Création du repository Artifact Registry (si nécessaire)
echo "📦 Configuration Artifact Registry..."
gcloud artifacts repositories create ${REPOSITORY} \
    --repository-format=docker \
    --location=${REGION} \
    --description="Repository pour Gestion Com Backend Cloud Run" 2>/dev/null || echo "✓ Repository déjà existant"

# 4. Build de l'image Docker
echo "🐳 Build de l'image Docker..."
gcloud builds submit --tag ${IMAGE_NAME}:latest .

# 5. Déploiement sur Cloud Run
echo "☁️  Déploiement sur Cloud Run..."
gcloud run deploy ${SERVICE_NAME} \
    --image=${IMAGE_NAME}:latest \
    --region=${REGION} \
    --platform=managed \
    --add-cloudsql-instances=${CLOUD_SQL_INSTANCE} \
    --memory=512Mi \
    --cpu=1 \
    --timeout=900 \
    --max-instances=10 \
    --allow-unauthenticated \
    --set-env-vars="ENVIRONMENT=production,PYTHONPATH=/app,DB_HOST=/cloudsql/${CLOUD_SQL_INSTANCE},DB_PORT=5432,DB_NAME=gestioncom_db,DB_USER=postgres,DB_PASSWORD=WECAN2025@@,SECRET_KEY=django-insecure-prod-change-this-key-in-production,DJANGO_SETTINGS_MODULE=backend.settings"

# 6. Récupération de l'URL du service
echo "🌐 Récupération de l'URL du service..."
SERVICE_URL=$(gcloud run services describe ${SERVICE_NAME} --region=${REGION} --format='value(status.url)')

echo ""
echo "✅ Déploiement terminé avec succès!"
echo "======================================"
echo "🌐 URL du service: ${SERVICE_URL}"
echo "📊 Logs: gcloud run logs read ${SERVICE_NAME} --region=${REGION}"
echo "🔍 Status: gcloud run services describe ${SERVICE_NAME} --region=${REGION}"
echo ""
echo "📋 Informations Cloud SQL:"
echo "   Instance: gestion-com-postgres"
echo "   Database: gestioncom_db"
echo "   Connection: yaaprojects:europe-west1:gestion-com-postgres"
echo ""
