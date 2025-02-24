[]

import json

# Fichier JSON pour stocker les tâches
TASKS_FILE = "tasks.json"

# Charger les tâches existantes
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Sauvegarder les tâches
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Ajouter une tâche
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Tâche ajoutée : {task}")

# Afficher les tâches
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Aucune tâche enregistrée.")
    else:
        for i, t in enumerate(tasks, 1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {status} {t['task']}")

# Supprimer une tâche
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tâche supprimée : {removed_task['task']}")
    else:
        print("Index invalide.")

# Marquer une tâche comme terminée
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Tâche terminée : {tasks[index]['task']}")
    else:
        print("Index invalide.")

# Interface utilisateur (ligne de commande)
def main():
    while True:
        print("\n1. Ajouter une tâche")
        print("2. Voir les tâches")
        print("3. Supprimer une tâche")
        print("4. Marquer une tâche comme faite")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            task = input("Entrez la tâche : ")
            add_task(task)
        elif choix == "2":
            list_tasks()
        elif choix == "3":
            list_tasks()
            index = int(input("Numéro de la tâche à supprimer : ")) - 1
            delete_task(index)
        elif choix == "4":
            list_tasks()
            index = int(input("Numéro de la tâche terminée : ")) - 1
            complete_task(index)
        elif choix == "5":
            print("Bye ! 👋")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
