import cv2
import imageio
import os

# Base directory containing sets of images
base_image_dir = '../images/'  # Adjust relative path as per your directory structure

# Output directory
output_dir = '../output/'  # Adjust relative path as per your directory structure

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process images and create a GIF
def create_gif(image_dir, output_gif_path):
    # List to store processed images
    images = []

    # Check if the image directory exists
    if not os.path.exists(image_dir):
        print(f"Error: The directory {image_dir} does not exist.")
        return

    # Iterate through images in the directory
    for filename in sorted(os.listdir(image_dir)):
        if filename.lower().endswith(('.jpeg', '.png', '.gif')):
            img_path = os.path.join(image_dir, filename)
            print(f"Processing image: {img_path}")
            image = cv2.imread(img_path)
            
            # Check if image loading is successful
            if image is None:
                print(f"Error: Unable to load image {img_path}")
                continue
            
            # Perform image processing here if needed (e.g., resizing)
            resized_image = cv2.resize(image, (400, 300))
            
            # Convert to RGB (imageio expects RGB format)
            rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            
            # Append processed image to the list
            images.append(rgb_image)

    # Check if we have images to process
    if not images:
        print(f"No images found in {image_dir}. Skipping GIF creation.")
        return

    # Ensure images repeat infinitely by appending the list to itself
    images *= 2  # Double the list to ensure it loops through all images

    # Save images as GIF with looping (indefinitely by default)
    imageio.mimsave(output_gif_path, images, duration=0.5, loop=0)

    print(f"GIF saved successfully as {output_gif_path}")

# Iterate over each subdirectory in the base image directory
for subdir in sorted(os.listdir(base_image_dir)):
    subdir_path = os.path.join(base_image_dir, subdir)
    if os.path.isdir(subdir_path):
        output_gif_path = os.path.join(output_dir, f"{subdir}.gif")
        print(f"Creating GIF for images in {subdir_path}...")
        create_gif(subdir_path, output_gif_path)
