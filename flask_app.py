# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Erwan", nom="Sanquer",
                           loisirs=["Le tennis", "Blur, un jeu de course arcade que je modifie", "Le code (bientôt !)"])


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return "Erreur : a et b doivent être des nombres.", 400

    op = request.args.get("op", "plus")
    if op == "plus":
        return f"{a} + {b} = {a + b}"
    elif op == "moins":
        return f"{a} - {b} = {a - b}"
    elif op == "fois":
        return f"{a} × {b} = {a * b}"
    elif op == "divise":
        if b == 0:
            return "Erreur : division par zéro.", 400
        return f"{a} ÷ {b} = {a / b}"
    else:
        return "Opération inconnue (plus, moins, fois, divise).", 400

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    donnees = request.form if request.method == "POST" else request.args
    prenom = donnees.get("prenom", "inconnu")
    ville = donnees.get("ville", "nulle part")
    couleur = donnees.get("couleur", "black")
    if couleur not in ["tomato", "teal", "royalblue"]:
        couleur = "black"
    return render_template("salut.html", prenom=prenom, ville=ville,
                           couleur=couleur, methode=request.method)

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
