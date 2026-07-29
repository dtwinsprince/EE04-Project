import requests
import os
import random
import sys

apiurl = "https://api.github.com/repos/spMohanty/PlantVillage-Dataset/contents/raw/color/{folder}"

folders = {
    "early_blight": "Potato___Early_blight",
    "healthy": "Potato___healthy"
}

maxbytesperclass = 5 * 1024 * 1024

def downloadclass(localfolder, repofolder):
    print(f"Listing files in {repofolder}...")
    response = requests.get(apiurl.format(folder=repofolder))
    response.raise_for_status()
    itemslist = response.json()

    filesonly = [currentitem for currentitem in itemslist if currentitem["type"] == "file"]
    random.shuffle(filesonly)

    destinationfolder = os.path.join("dataset", localfolder)
    os.makedirs(destinationfolder, exist_ok=True)

    totalbytes = 0
    imagecount = 0
    for currentitem in filesonly:
        if totalbytes >= maxbytesperclass:
            break
        imageresponse = requests.get(currentitem["download_url"])
        imageresponse.raise_for_status()
        filepath = os.path.join(destinationfolder, currentitem["name"])
        with open(filepath, "wb") as outfile:
            outfile.write(imageresponse.content)
        totalbytes += len(imageresponse.content)
        imagecount += 1

    print(f"{localfolder}: {imagecount} images, {totalbytes / 1024 / 1024:.2f} MB")

def main():
    if len(sys.argv) > 1:
        selectedclass = sys.argv[1]
        if selectedclass not in folders:
            print(f"Unknown class '{selectedclass}'. Use 'early_blight' or 'healthy'.")
            return
        downloadclass(selectedclass, folders[selectedclass])
    else:
        for localfolder, repofolder in folders.items():
            downloadclass(localfolder, repofolder)

if __name__ == "__main__":
    main()
