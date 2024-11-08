import os
import shutil
from PIL import Image

def extract_music(album_folder, artist_name, album_name, ipod_path="d:\\"):
    # Check if album folder exists
    if not os.path.exists(album_folder):
        print(f"Album folder '{album_folder}' not found.")
        return

    # Create artist and album folder on the iPod (Rockbox path)
    target_path = os.path.join(ipod_path, 'Music', artist_name, album_name)
    os.makedirs(target_path, exist_ok=True)

    # Process cover.jpg if it exists and make it non-progressive
    cover_path = os.path.join(album_folder, 'cover.jpg')
    if os.path.exists(cover_path):
        try:
            with Image.open(cover_path) as img:
                img.save(os.path.join(target_path, 'cover.jpg'), "JPEG", progressive=False)
            print("Processed cover.jpg to make it non-progressive.")
        except Exception as e:
            print(f"Error processing cover.jpg: {e}")
    else:
        print("No cover.jpg found in the album folder.")

    # Copy remaining files from album folder to target path
    for file_name in os.listdir(album_folder):
        file_path = os.path.join(album_folder, file_name)
        if os.path.isfile(file_path) and file_name != 'cover.jpg':  # Skip cover.jpg as it’s already processed
            shutil.copy(file_path, target_path)

    print(f"Music from '{album_folder}' has been copied to '{target_path}'.")

# Prompt user for inputs
album_folder = input("Enter the path to your album folder: ")
artist_name = input("Enter the artist's name: ")
album_name = input("Enter the album's name: ")

# Run the function with the hardcoded iPod path
extract_music(album_folder, artist_name, album_name)
