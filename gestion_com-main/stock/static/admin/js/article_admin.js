document.addEventListener('DOMContentLoaded', function() {
    const categorieSelect = document.getElementById('id_categorie');
    const sousCategorieSelect = document.getElementById('id_sous_categorie');

    if (!categorieSelect || !sousCategorieSelect) return;

    // Fonction pour recharger les sous-catégories selon la catégorie choisie
    categorieSelect.addEventListener('change', function() {
        const categorieId = this.value;

        // Effacer les anciennes options
        sousCategorieSelect.innerHTML = '<option value="">---------</option>';

        if (!categorieId) return;

        // Charger les sous-catégories via l’API
        fetch(`/api/stock/sous-categories/?categorie=${categorieId}`)
            .then(response => response.json())
            .then(data => {
                data.forEach(sousCat => {
                    const option = document.createElement('option');
                    option.value = sousCat.id;
                    option.textContent = sousCat.nom;
                    sousCategorieSelect.appendChild(option);
                });
            })
            .catch(err => console.error('Erreur chargement sous-catégories:', err));
    });
});
