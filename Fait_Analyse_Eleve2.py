import pandas as pd
import random

# Charger les fichiers Excel
eleves = pd.read_excel("Table_Eleve.xlsx")
matieres = pd.read_excel("Table_Matiere.xlsx")
niveaux = pd.read_excel("Table_Niveau_Scolaire.xlsx")
classes = pd.read_excel("Table_Classe.xlsx")
dates = pd.read_excel("Table_Date.xlsx")
ecoles = pd.read_excel("Table_Ecole.xlsx")
villes = pd.read_excel("Villes_Marocaines.xlsx")

# Générer la table de faits
nb_records = 1000  # Nombre de lignes dans la table de faits
fait_analyse_eleve2 = []

for i in range(1, nb_records + 1):
    id_fait = i
    id_eleve = random.choice(eleves["id_élève"])
    id_matiere = random.choice(matieres["id_matière"])
    id_niveau = random.choice(niveaux["id_niveau"])
    id_classe = random.choice(classes["id_classe"])
    id_date = random.choice(dates["id_date"])
    id_ecole = random.choice(ecoles["id_école"])
    id_ville = random.choice(villes["id_ville"])
    
    # Génération aléatoire des données factuelles
    taux_presence = round(random.uniform(0, 100), 2)  # Taux de présence entre 0% et 100%
    
    fait_analyse_eleve2.append([
        id_fait, id_eleve, id_matiere, id_niveau, id_classe, id_date,
        id_ecole, id_ville, taux_presence
    ])

# Créer un DataFrame pour la table de faits
columns_fait = [
    "id_fait", "id_élève", "id_matière", "id_niveau", "id_classe", "id_date",
    "id_école", "id_ville", "taux_presence"
]
df_fait = pd.DataFrame(fait_analyse_eleve2, columns=columns_fait)

# Sauvegarder la table de faits dans un fichier Excel
output_file = "Table_Fait_Analyse_Eleve2.xlsx"
df_fait.to_excel(output_file, index=False)

print(f"Table de faits générée et sauvegardée dans {output_file}")
