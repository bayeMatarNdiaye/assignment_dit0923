#EL HADJI MATAR NDIAYE
import os
import subprocess

def git_commit(message, chemin_repo):
    """
    Effectue un commit avec un message donné dans un dépôt Git.

    Args:
        message (str): Le message de commit.
        chemin_repo (str): Le chemin local du dépôt Git.
    """
    try:
        subprocess.run(["git", "add", "."], cwd=chemin_repo, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=chemin_repo, check=True)
        print(f"Commit effectué avec le message : {message}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'ajout et du commit : {e}")

def create_arborescence(arborescence, chemin_repo):
    """
    Crée une arborescence de fichiers et de dossiers dans le dépôt Git.

    Args:
        arborescence (dict): Une structure d'arborescence spécifiée comme un dictionnaire.
        chemin_repo (str): Le chemin local du dépôt Git.
    """
    
    def parcourir_arborescence(arbo, chemin_actuel):
        for element, contenu in arbo.items():
            chemin_element = os.path.join(chemin_actuel, element)

            if isinstance(contenu, dict): 
                os.makedirs(chemin_element, exist_ok=True)
                parcourir_arborescence(contenu, chemin_element)
            elif contenu:  
                os.makedirs(os.path.dirname(chemin_element), exist_ok=True)
                with open(chemin_element, "w") as fichier:
                    fichier.write(contenu)

    # Création arborescence locale
    parcourir_arborescence(arborescence, chemin_repo)


if __name__ == '__main__' :
#arborescence
    arborescence = {
        "data": {
            "cleaned": {},
            "processed": {},
            "raw": {}
            
        },
        "docs": {},
        "LICENCE" : "",
        "Makefile": "",
        "models": {},
        "notebooks": {
            "main.ipynb": 'my code python'
        },
        "README.md": """Ce programme Python a pour objectif de créer une structure d'arborescence de fichiers et de dossiers spécifique dans un dépôt Git\nPour exécuter l'application, suivez ces étapes :
    1. [Étape 1 : Prérequis, par exemple, installer Python 3.7+]
    2. [Étape 2 : Cloner le dépôt Git : `git clone https://github.com/votre-utilisateur/mon-projet.git`]
    3. [Étape 3 : Naviguer vers le répertoire du projet : `cd mon-projet`]
    4. [Étape 4 : Installer les dépendances : `pip install -r requirements.txt`]
    5. [Étape 5 : Lancer l'application : `python main.py`]
    """,
        "reports": {},
        "requirements.txt": "os\nsubprocess",
        "src": {
            "utils.py": "",
            "process.py": "",
            "train.py": ""
        }
    }

    chemin_repo_git = r"C:\Users\baaymatar\Desktop\COURS\assignment_dit0923"
    subprocess.run(["git", "init"], cwd=chemin_repo_git, check=True)

    create_arborescence(arborescence, chemin_repo_git)

    git_commit("Création de l'arborescence", chemin_repo_git)

    subprocess.run(["git", "init"], cwd=chemin_repo_git, check=True)

    # Vérifier si le référentiel distant "origin" existe déjà
    try:
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/bayeMatarNdiaye/assignment_dit0923.git"], cwd=chemin_repo_git, check=True)
    except subprocess.CalledProcessError:
        # "origin" existe déjà, vous pouvez ignorer cette erreur
        pass

    # Ajouter tous les fichiers et effectuer un commit initial
    subprocess.run(["git", "add", "."], cwd=chemin_repo_git, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=chemin_repo_git, check=True)



