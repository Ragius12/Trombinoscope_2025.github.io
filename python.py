import os

# --- Données de test (10 personnes sans photos) ---
personnes = [
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
    {"nom": "Bourdon", "prenom": "Thomas", "surnom": "Vespula", "famille": "84", "tel": "0631495722", "photo": "trombinoscope/Thomas_Bourdon.png"},
]

# --- Création du HTML ---
html = """
<html>
<head>
<meta charset="utf-8">
<title>Trombinoscope</title>
<style>
body {
    font-family: Arial, sans-serif;
    margin: 2cm;
}
.personne {
    display: flex;
    align-items: center;
    margin: 1.5em 0;
    border: 1px solid #aaa;
    border-radius: 8px;
    padding: 10px;
}
.personne img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border: 2px solid #ccc;
    border-radius: 6px;
}
.infos {
    flex: 1;
    margin-left: 20px;
}
.page {
    page-break-after: always;
}
</style>
</head>
<body>
<h1>Trombinoscope</h1>
"""

# --- Génération des blocs ---
for i, p in enumerate(personnes):
    # Vérifie si la photo existe
    if os.path.exists(p["photo"]):
        photo = p["photo"]
    else:
        # Génère un cadre gris vide (base64 d’un carré gris)
        photo = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><rect width='120' height='120' fill='%23cccccc'/><text x='15' y='65' font-size='14' fill='black'>Aucune photo</text></svg>"

    # Quinconce : alterner image droite/gauche
    if i % 2 == 0:
        bloc = f"""
        <div class="personne">
            <div class="infos">
                <b>Nom :</b> {p['nom']}<br>
                <b>Prénom :</b> {p['prenom']}<br>
                <b>Surnom :</b> {p['surnom']}<br>
                <b>Famille :</b> {p['famille']}<br>
                <b>Téléphone :</b> {p['tel']}
            </div>
            <img src="{photo}">
        </div>
        """
    else:
        bloc = f"""
        <div class="personne">
            <img src="{photo}">
            <div class="infos">
                <b>Nom :</b> {p['nom']}<br>
                <b>Prénom :</b> {p['prenom']}<br>
                <b>Surnom :</b> {p['surnom']}<br>
                <b>Famille :</b> {p['famille']}<br>
                <b>Téléphone :</b> {p['tel']}
            </div>
        </div>
        """

    # Ajout du saut de page tous les 5
    if (i + 1) % 5 == 0 and i != len(personnes) - 1:
        bloc += '<div class="page"></div>'

    html += bloc

html += "</body></html>"

# --- Sauvegarde ---
with open("trombinoscope_nouveau.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Fichier 'trombinoscope.html' généré avec succès !")
print("➡️ Ouvre-le dans ton navigateur, puis fais : Ctrl+P → Enregistrer en PDF")
