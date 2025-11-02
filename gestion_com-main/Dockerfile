FROM python:3.12-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

WORKDIR /app

# Installer les dépendances système nécessaires pour PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Cache buster - change this value to force rebuild
ENV CACHE_BUST=202410251600

# Copier le code de l'application
COPY manage.py .
COPY create_superuser.py .
COPY backend/ ./backend/
COPY clients/ ./clients/
COPY commandes/ ./commandes/
COPY devis/ ./devis/
COPY depots/ ./depots/
COPY facturation/ ./facturation/
COPY fournisseurs/ ./fournisseurs/
COPY livraisons/ ./livraisons/
COPY stock/ ./stock/

# Créer les répertoires nécessaires
RUN mkdir -p static media logs

# Exposer le port (Cloud Run utilise la variable PORT)
EXPOSE $PORT

# Commande de démarrage
CMD ["/bin/bash", "-c", "echo '🚀 Démarrage de Gestion Com Backend' && echo '====================================' && echo '📊 Exécution des migrations...' && python manage.py migrate --noinput && echo '👤 Création du superuser...' && python create_superuser.py && echo '📦 Collection des fichiers statiques...' && python manage.py collectstatic --noinput --clear && echo '✅ Initialisation terminée!' && echo '====================================' && echo '🌐 Démarrage du serveur...' && exec gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 0 --keep-alive 80 --log-level info --access-logfile - --error-logfile -"]
