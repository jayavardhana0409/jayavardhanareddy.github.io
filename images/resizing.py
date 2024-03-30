from PIL import Image
import os

def resize_images_in_folder(folder_path, output_folder, target_size=(4000, 2250)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Open the image
            with Image.open(os.path.join(folder_path, filename)) as img:
                # Resize the image
                resized_img = img.resize(target_size, Image.ANTIALIAS)
                # Save the resized image to the output folder
                resized_img.save(os.path.join(output_folder, filename))

# Usage
folder_path = 'C:\\Users\\jaire\\Downloads\\project portfolio\\images'
output_folder = 'C:\\Users\\jaire\\Downloads\\project portfolio\\img'
resize_images_in_folder(folder_path, output_folder)
