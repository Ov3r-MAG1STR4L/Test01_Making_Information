# 📒 Mon carnet de bord

**Nom :** SANQUER

**Prénom :** Erwan

**Adresse de mon site :** [https://ov3rmag1str4l.pythonanywhere.com](https://ov3rmag1str4l.pythonanywhere.com)

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code est stocké sur GitHub, mais celui qui fabrique la page tourne sur le serveur de PythonAnywhere. GitHub Actions copie le code de GitHub vers PythonAnywhere à chaque commit. Rien ne tourne sur mon ordinateur.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Le site tourne sur un serveur connecté à Internet en permanence. Son navigateur envoie une demande à l’adresse du site, le serveur lui renvoie la page, et le navigateur sait déjà l’afficher.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est www.google.com : il désigne le serveur à contacter. Le chemin est /maps : il indique la page demandée sur ce serveur.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ « Not Found » veut dire que la page demandée n’existe pas. C’est le serveur qui l’envoie : il a bien reçu la demande, mais aucune route ne correspond à ce chemin.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Le site plante avec « Something went wrong ». L’Error log indique AssertionError: View function mapping is overwriting an existing endpoint function: accueil à la ligne 27 de flask_app.py. Flask identifie chaque route par le nom de sa fonction : deux fonctions avec le même nom créent un conflit et le serveur refuse de démarrer.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie seulement du texte avec des balises (visible avec Ctrl + U). Le navigateur lit ces balises et les transforme en page mise en forme : titres, gras, listes, image. De plus, le HTML est tolérant : une balise mal fermée ne provoque pas d’erreur, le navigateur devine la suite.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ h1 = titre principal, p = paragraphe, ul = liste à puces, li = un élément de la liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ La balise <img> contient seulement l’adresse de l’image. C’est le navigateur qui va la télécharger directement sur le serveur de Wikimedia, pas sur le mien.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Chacun travaille sur son fichier sans gêner l’autre : le développeur modifie le Python (les données), le graphiste modifie le HTML (l’apparence). Le code est aussi plus lisible qu’avec du HTML entre guillemets dans le Python.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Par le serveur. Avec Ctrl + U, le code source reçu affiche directement « Erwan Sanquer » : les {{ prenom }} n’existent plus. Le navigateur ne voit jamais le template original.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit la structure et le contenu (titre, paragraphe, liste). Le CSS décrit l’apparence (couleurs, police, marges). On peut changer tout le style sans toucher au contenu.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Au moins 3 : la page HTML, le fichier style.css et l’image du logo Python. Le navigateur demande aussi souvent une favicon (l’icône de l’onglet).

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur garde le CSS en mémoire (le cache) pour ne pas le retélécharger à chaque visite. Ctrl + F5 force le rechargement de tous les fichiers depuis le serveur.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP = HyperText Transfer Protocol, le protocole de communication du Web. Le navigateur envoie la requête, le serveur renvoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ 4 requêtes : la page presentation (HTML), style.css, l’image du logo Python (chez Wikimedia) et favicon.ico.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 200 = « OK », le serveur a trouvé le fichier et l’envoie. 404 = « Not Found » : le navigateur demande tout seul une icône d’onglet (favicon.ico), mais mon site n’en a pas.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ L’onglet Éléments modifie seulement la copie de la page dans mon navigateur. Le fichier sur le serveur ne change pas : au rechargement, ou pour un autre visiteur, le serveur renvoie la page d’origine.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre s’appelle search_query, sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ int() essaie de convertir « bonjour » en nombre, c’est impossible : Python lève une ValueError et le serveur renvoie une erreur 500. Il faudrait vérifier ce que l’utilisateur envoie avant de le convertir (avec un try/except) et renvoyer un message d’erreur clair.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ L’utilisateur peut glisser du HTML, voire un script, qui s’exécute dans la page comme s’il venait du site. Un pirate pourrait envoyer ce lien piégé à quelqu’un pour voler ses données (faille XSS). Il ne faut jamais faire confiance à ce que l’utilisateur envoie.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données apparaissent dans l’URL (/salut?prenom=Erwan&ville=...). En POST, l’URL reste /salut : les données voyagent dans le corps de la requête.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ GET pour une recherche : on peut copier le lien, le partager ou le mettre en favori. POST pour une connexion : le mot de passe n’apparaît pas dans l’URL, donc ni dans l’historique, ni dans les journaux du serveur, ni par-dessus l’épaule.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. Elles sont seulement cachées de l’URL : on les voit en clair dans l’onglet Réseau (Charge utile). Pour les protéger pendant le trajet, il faut HTTPS, qui chiffre la requête.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ erreur du client : il demande une page qui n’existe pas (404) ou à laquelle il n’a pas accès (403). 5xx = erreur du serveur : la demande est correcte mais le serveur plante (bug dans le code, panne), comme l’erreur 500 de l’exercice 7.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond avec un code 3xx et un en-tête Location qui contient la nouvelle adresse. C’est le navigateur qui fait la deuxième requête vers cette adresse, tout seul.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Taper http:// au lieu de https:// : le site redirige vers la version sécurisée. Autre exemple : une page qui a changé d’adresse redirige (301) vers la nouvelle, pour ne pas casser les anciens liens.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
