# Homework 7
# Name: Javon Salazar
# Date: 4/17/26
#Description: This homework covers over lecture 12 unit 3.

#Exercise 1
import pickle
import os

def practice_3_beginner():
    print("\n" + "=" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("=" * 50)

    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]

    with open("shopping.pkl", "wb") as f:
        pickle.dump(shopping_list, f)

    print("Shopping list pickled!")

    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f)

    print(f"Loaded list: {loaded_list}")

    loaded_list.append("Eggs")
    loaded_list.append("Cheese")

    with open("shopping.pkl", "wb") as f:
        pickle.dump(loaded_list, f)

    print("Updated list saved")

    project_name = "my_project"

    if not os.path.exists(project_name):
        os.mkdir(project_name)

    subdirs = ["src", "docs", "tests", "data"]

    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        os.makedirs(path, exist_ok=True)

    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write("# My Project\n")

    with open(os.path.join(project_name, "src", "main.py"), "w") as f:
        f.write("print('Hello World')\n")

    print("\nProject structure:")
    for root, dirs, files in os.walk(project_name):
        level = root.replace(project_name, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = "  " * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

practice_3_beginner()


#Exercise 2
import os
import shutil

def practice_3_intermediate():
    print("\n" + "=" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("=" * 50)

    messy_folder = "messy_files"

    os.makedirs(messy_folder, exist_ok=True)

    test_files = [
        "document.txt", "image.jpg", "photo.png",
        "report.pdf", "script.py", "data.csv",
        "music.mp3", "video.mp4", "archive.zip"
    ]

    for file in test_files:
        path = os.path.join(messy_folder, file)
        with open(path, "w") as f:
            f.write(f"Test file: {file}")

    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images": [".jpg", ".png", ".gif"],
        "code": [".py", ".js", ".html"],
        "data": [".csv", ".json", ".xml"],
        "media": [".mp3", ".mp4", ".avi"],
        "archives": [".zip", ".tar", ".rar"]
    }

    for folder in organized:
        os.makedirs(os.path.join(messy_folder, folder), exist_ok=True)

    for file in os.listdir(messy_folder):
        file_path = os.path.join(messy_folder, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1]

            for category, extensions in organized.items():
                if ext in extensions:
                    dest = os.path.join(messy_folder, category, file)
                    shutil.move(file_path, dest)
                    break

    print("\nOrganized structure:")
    for root, dirs, files in os.walk(messy_folder):
        level = root.replace(messy_folder, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = "  " * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

practice_3_intermediate()


#Exercise 3
import pickle
import os
import shutil
from datetime import datetime
from pathlib import Path

def practice_3_advanced():
    print("\n" + "=" * 50)
    print("EXERCISE 3.3: Game Save System")
    print("=" * 50)

    class GameState:
        def __init__(self):
            self.player_name = ""
            self.level = 1
            self.score = 0
            self.inventory = []
            self.position = (0, 0)

        def __str__(self):
            return f"{self.player_name} - Level {self.level}, Score: {self.score}"

    game = GameState()
    game.player_name = "Hero"
    game.level = 5
    game.score = 1250
    game.inventory = ["Sword", "Shield", "Potion"]
    game.position = (10, 25)

    save_dir = "saves"
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "save1.pkl")

    with open(save_path, "wb") as f:
        pickle.dump(game, f)

    with open(save_path, "rb") as f:
        loaded_game = pickle.load(f)

    print(loaded_game.player_name, loaded_game.level, loaded_game.score, loaded_game.inventory, loaded_game.position)

    def save_game(game_state, slot_number):
        path = os.path.join(save_dir, f"save{slot_number}.pkl")
        with open(path, "wb") as f:
            pickle.dump(game_state, f)

    save_game(game, 2)

    print("\nSave files:")
    for file in os.listdir(save_dir):
        print(file)

    def create_backup(source_dir, backup_dir="backups"):
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = os.path.join(backup_dir, f"backup_{timestamp}")
        shutil.copytree(source_dir, dest)
        return dest

    backup_path = create_backup(save_dir)

    def verify_backup(source, backup):
        for root, dirs, files in os.walk(source):
            for file in files:
                src_file = os.path.join(root, file)
                rel = os.path.relpath(src_file, source)
                backup_file = os.path.join(backup, rel)
                if not os.path.exists(backup_file):
                    return False
        return True

    print("Backup valid:", verify_backup(save_dir, backup_path))

    def cleanup_old_backups(backup_dir, keep_count=3):
        backups = sorted(
            [os.path.join(backup_dir, d) for d in os.listdir(backup_dir)],
            key=os.path.getmtime,
            reverse=True
        )

        for old in backups[keep_count:]:
            shutil.rmtree(old)

    cleanup_old_backups("backups")

practice_3_advanced()