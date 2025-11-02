#!/bin/bash
set -e

echo "🚀 Démarrage de Gestion Com Backend"
echo "===================================="

# 1. Exécuter les migrations
echo "📊 Exécution des migrations..."
python manage.py migrate --noinput

# 2. Créer le superuser s'il n'existe pas
echo "👤 Création du superuser..."
python create_superuser.py

# 3. Collecter les fichiers statiques
echo "📦 Collection des fichiers statiques..."
python manage.py collectstatic --noinput --clear

echo "✅ Initialisation terminée!"
echo "===================================="

# 4. Démarrer l'application avec gunicorn
echo "🌐 Démarrage du serveur..."
exec gunicorn backend.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads 4 \
    --timeout 0 \
    --keep-alive 80 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
