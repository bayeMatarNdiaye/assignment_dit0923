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
    # Fonction récursive pour parcourir l'arborescence
    def parcourir_arborescence(arbo, chemin_actuel):
        for element, contenu in arbo.items():
            chemin_element = os.path.join(chemin_actuel, element)

            if isinstance(contenu, dict):  # Si c'est un dossier
                os.makedirs(chemin_element, exist_ok=True)
                parcourir_arborescence(contenu, chemin_element)
            elif contenu:  # Si c'est un fichier avec du contenu
                os.makedirs(os.path.dirname(chemin_element), exist_ok=True)
                with open(chemin_element, "w") as fichier:
                    fichier.write(contenu)

    # Créer l'arborescence locale
    parcourir_arborescence(arborescence, chemin_repo)

# Structure d'arborescence
arborescence_a_creer = {
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
        "main.ipynb": "mycode"
    },
    "README.md": "Ce programme Python a pour objectif de créer une structure d'arborescence de fichiers et de dossiers spécifique dans un dépôt Git",
    "reports": {},
    "requirements.txt": "os\nsubprocess",
    "src": {
        "utils.py": "",
        "process.py": "",
        "train.py": ""
    }
}

chemin_repo_git = r"C:\Users\baaymatar\Desktop\COURS\assignment_dit0923"  # Remplacez par le chemin de votre dépôt local

subprocess.run(["git", "init"], cwd=chemin_repo_git, check=True)

create_arborescence(arborescence_a_creer, chemin_repo_git)

git_commit("Création de l'arborescence", chemin_repo_git)

