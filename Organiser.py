import os
import shutil
import csv
import datetime

path_to_scan = r"C:\Users\dchan\OneDrive\Documents\Programming\Data\Python\File organiser\Test folder"
log_file_path = os.path.join(path_to_scan, "activity_log.csv")
with open(log_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Filename", "Original_Path", ])

print("--- Starting Scan & logging---")
files = os.listdir(path_to_scan)

for filename in files:
    if filename == "activity_log.csv":
        continue
    file_path = os.path.join(path_to_scan, filename)
    if os.path.isfile(file_path):

        if filename.endswith(".pdf"):
            destination = os.path.join(path_to_scan, "PDFs")
            if not os.path.exists(destination):
                os.makedirs(destination)
                print(f"created {destination} folder.")
            shutil.move(os.path.join(path_to_scan, filename), destination)
            with open(log_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
                writer.writerow([timestamp, filename, file_path, destination])

            print(f"{filename} moved to PDfs folder and has been logged.")

        elif filename.endswith(".mp4"):
            destination = os.path.join(path_to_scan, "Videos")
            if not os.path.exists(destination):
                os.makedirs(destination)
                print(f"created {destination} folder.")
            shutil.move(os.path.join(path_to_scan, filename), destination)
            with open(log_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
                writer.writerow([timestamp, filename, file_path, destination])
            print(f"{filename} moved to Videos folder and has been logged.")

        elif filename.endswith(".jpg") or filename.endswith(".png"):
            destination = os.path.join(path_to_scan, "Images")
            if not os.path.exists(destination):
                os.makedirs(destination)
            print(f"created {destination} folder.")
            shutil.move(os.path.join(path_to_scan, filename), destination)
            with open(log_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
                writer.writerow([timestamp, filename, file_path, destination])
            print(f"{filename} moved to Images folder and has been logged.")

        elif filename.endswith(".txt"):
            destination = os.path.join(path_to_scan, "Text files")
            if not os.path.exists(destination):
                os.makedirs(destination)
            print(f"created {destination} folder.")
            shutil.move(os.path.join(path_to_scan, filename), destination)
            with open(log_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
                writer.writerow([timestamp, filename, file_path, destination])
            print(f"{filename} moved to the Text files folder and has been logged.")

        elif filename.endswith(".docx"):
            destination = os.path.join(path_to_scan, "Word Documents")
            if not os.path.exists(destination):
                os.makedirs(destination)
            print(f"created {destination} folder.")
            shutil.move(os.path.join(path_to_scan, filename), destination)
            with open(log_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
                writer.writerow([timestamp, filename, file_path, destination])
            print(f"{filename} moved to the Word Documents folder and has been logged. ")

        else:
            print(f"Don't know what {filename} is")

print("--- Scan Complete ---")
