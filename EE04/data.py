import requests
import os
import random
import sys

API_URL = "https://api.github.com/repos/spMohanty/PlantVillage-Dataset/contents/raw/color/{folder}"

FOLDERS = {
    "early_blight": "Potato___Early_blight",
    "healthy": "Potato___healthy"
}

MAX_BYTES_PER_CLASS = 5 * 1024 * 1024

def download_class(local_folder, repo_folder):
    print(f"Listing files in {repo_folder}...")
    resp = requests.get(API_URL.format(folder=repo_folder))
    resp.raise_for_status()
    items = resp.json()

    files = [item for item in items if item["type"] == "file"]
    random.shuffle(files)

    dest_dir = os.path.join("dataset", local_folder)
    os.makedirs(dest_dir, exist_ok=True)

    total_bytes = 0
    count = 0
    for item in files:
        if total_bytes >= MAX_BYTES_PER_CLASS:
            break
        img_resp = requests.get(item["download_url"])
        img_resp.raise_for_status()
        filepath = os.path.join(dest_dir, item["name"])
        with open(filepath, "wb") as f:
            f.write(img_resp.content)
        total_bytes += len(img_resp.content)
        count += 1

    print(f"{local_folder}: {count} images, {total_bytes / 1024 / 1024:.2f} MB")

def main():
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice not in FOLDERS:
            print(f"Unknown class '{choice}'. Use 'early_blight' or 'healthy'.")
            return
        download_class(choice, FOLDERS[choice])
    else:
        for local_folder, repo_folder in FOLDERS.items():
            download_class(local_folder, repo_folder)

if __name__ == "__main__":
    main()