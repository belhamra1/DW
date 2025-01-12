import pandas as pd
import random

# Charger les fichiers Excel
niveaux = pd.read_excel("Table_Niveau_Scolaire.xlsx")
classes = pd.read_excel("Table_Classe.xlsx")
dates = pd.read_excel("Table_Date.xlsx")
ecoles = pd.read_excel("Table_Ecole.xlsx")
examens = pd.read_excel("Types_Examens.xlsx")
villes = pd.read_excel("Villes_Marocaines.xlsx")

# Générer la table de faits
nb_records = 1000  # Nombre de lignes dans la table de faits
fait_analyse_ecole1 = []

for i in range(1, nb_records + 1):
    id_fait = i
    id_niveau = random.choice(niveaux["id_niveau"])
    id_classe = random.choice(classes["id_classe"])
    id_date = random.choice(dates["id_date"])
    id_ecole = random.choice(ecoles["id_école"])
    id_type_examen = random.choice(examens["id_type_examen"])
    id_ville = random.choice(villes["id_ville"])
    
    # Génération aléatoire des données factuelles
    taux_reussite_examen = round(random.uniform(0, 100), 2)  # Entre 0% et 100%
    taux_redoublement = round(random.uniform(0, 100), 2)  # Entre 0% et 100%
    
    fait_analyse_ecole1.append([
        id_fait, id_niveau, id_classe, id_date, id_ecole, id_type_examen, id_ville,
        taux_reussite_examen, taux_redoublement
    ])

# Créer un DataFrame pour la table de faits
columns_fait = [
    "id_fait", "id_niveau", "id_classe", "id_date", "id_école", "id_type_examen", "id_ville",
    "taux_reussite_examen", "taux_redoublement"
]
df_fait = pd.DataFrame(fait_analyse_ecole1, columns=columns_fait)

# Sauvegarder la table de faits dans un fichier Excel
output_file = "Table_Fait_Analyse_Ecole1.xlsx"
df_fait.to_excel(output_file, index=False)

print(f"Table de faits générée et sauvegardée dans {output_file}")
