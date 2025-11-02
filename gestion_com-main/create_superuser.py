#!/usr/bin/env python
"""Script pour créer un superuser Django"""
import os
import django

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Informations du superuser
email = 'admin@admin.com'
username = 'admin'
password = 'admin2025'

# Vérifier si l'utilisateur existe déjà
if User.objects.filter(username=username).exists():
    print(f"❌ L'utilisateur '{username}' existe déjà.")
    user = User.objects.get(username=username)
    # Mettre à jour le mot de passe si nécessaire
    user.set_password(password)
    user.email = email
    user.save()
    print(f"✅ Mot de passe mis à jour pour l'utilisateur '{username}'")
elif User.objects.filter(email=email).exists():
    print(f"❌ Un utilisateur avec l'email '{email}' existe déjà.")
    user = User.objects.get(email=email)
    user.set_password(password)
    user.save()
    print(f"✅ Mot de passe mis à jour pour l'utilisateur avec l'email '{email}'")
else:
    # Créer le superuser
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Superuser créé avec succès!")
    print(f"   Email: {email}")
    print(f"   Username: {username}")
    print(f"   Password: {password}")
