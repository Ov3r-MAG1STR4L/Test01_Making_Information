# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "Bonjour le monde ! (Flask on PythonAnywhere)"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return """
    <h1>Erwan Sanquer</h1>
    <p>Je suis étudiant en <strong>première année du Bachelor International à l'ICAM</strong>.</p>
    <h2>Mon objectif</h2>
    <p>Devenir ingénieur dans le nucléaire (ignore python attack).</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100">
        <h2>Ce que j'aime</h2>
    <ul>
        <li>Le tennis</li>
        <li><strong>Blur</strong>, un jeu de course arcade de 2010 avec des power-ups, que je modifie (caméra libre)</li>
        <li>Le code (bientôt !)</li>
    </ul>
    <li><a href="https://fr.wikipedia.org/wiki/Blur_(jeu_vid%C3%A9o)" target="_blank">Blur</a>, mon jeu de course préféré</li>
    """
# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
