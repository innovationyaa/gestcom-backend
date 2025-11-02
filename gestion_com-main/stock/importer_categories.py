from stock.models import Categorie, SousCategorie

def importer_categories():
    data = {
        "الخضر": ["بدنجان", "طماطم", "افوكا", "كرومب", "فلفل"],
        "فواكه": ["منكو", "أفوكادو", "تفاح أحمر", "تفاح أخضر", "تفاح أصفر"],
        "الخزين": ["روز أصفر", "روز بسمتي", "روز سيكالا", "مايس", "تون ثومة"],
        "الماء": ["AQUA SIERRA 0.33", "AQUA SIERRA 0.5", "AQUA SIERRA 1.5", "Sidi Ali 0.5", "Sidi Ali 1.5"],
        "السمك": ["سلمون", "مراخو", "سيبادا", "تون", "تربو"],
        "سمك مجمد": ["كالامار بوطا", "لانغوستينوس", "صول 40/50", "كروكيت", "ميتينوينس"],
        "فحم": ["فحم"],
        "ثلج": ["ثلج"],
        "زيتون": ["زيتون أبيض", "زيتون أسود", "زيتون حامض"],
        "زيت": ["زيت بلديّة"],
        "مشروبات": ["كانص", "0.5 ل", "1 ل"],
        "البيض": ["بيض"],
        "امبورطي": [],
        "مواد التنظيف": [],
    }

    for cat, sous_cats in data.items():
        categorie, _ = Categorie.objects.get_or_create(nom=cat)
        for sous in sous_cats:
            SousCategorie.objects.get_or_create(categorie=categorie, nom=sous)

    print("   Catégories et sous-catégories importées avec succès.")
