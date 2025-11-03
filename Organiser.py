import os
import shutil

path_to_scan = r"C:\Users\dchan\OneDrive\Documents\Programming\Data\Python\File organiser\Test folder"

files = os.listdir(path_to_scan)

print("--- Starting Scan ---")

for filename in files:
    print("found files")

    if filename.endswith(".pdf"):
        destination = os.path.join(path_to_scan, "PDFs")
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"created {destination} folder.")
        shutil.move(os.path.join(path_to_scan, filename), destination)
        print(f"{filename} moved to PDfs folder.")

    elif filename.endswith(".mp4"):
        destination = os.path.join(path_to_scan, "Videos")
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"created {destination} folder.")
        shutil.move(os.path.join(path_to_scan, filename), destination)
        print(f"{filename} moved to Videos folder.")

    elif filename.endswith(".jpg") or filename.endswith(".png"):
        destination = os.path.join(path_to_scan, "Images")
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"created {destination} folder.")
        shutil.move(os.path.join(path_to_scan, filename), destination)
        print(f"{filename} moved to Images folder.")

    elif filename.endswith(".txt"):
        destination = os.path.join(path_to_scan, "Text files")
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"created {destination} folder.")
        shutil.move(os.path.join(path_to_scan, filename), destination)
        print(f"{filename} moved to the Text files folder.")

    elif filename.endswith(".docx"):
        destination = os.path.join(path_to_scan, "Word Documents")
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"created {destination} folder.")
        shutil.move(os.path.join(path_to_scan, filename), destination)
        print(f"{filename} moved to the Word Documents folder. ")

    else:
        print(f"Don't know what {filename} is")

print("--- Scan Complete ---")