import os
from PIL import Image

def resize_image_to_longest_side(input_path, output_path, max_length=1500):
    """
    Resize the image so its longest side is max_length pixels, maintaining aspect ratio.
    """
    with Image.open(input_path) as img:
        original_width, original_height = img.size

        # Determine the scaling factor, ensuring the longest dimension is max_length
        scaling_factor = max_length / max(original_width, original_height)

        # Calculate new dimensions
        new_width = int(original_width * scaling_factor)
        new_height = int(original_height * scaling_factor)
        
        # Resize the image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the resized image
        img.save(output_path)

def convert_images_to_max_dimension(folder_path='.'):
    """
    Resize all .png files so their longest dimension is 1500 pixels,
    maintaining aspect ratio, and save them in a /compressed subfolder.
    """
    compressed_folder_path = os.path.join(folder_path, 'compressed')
    # Check if the /compressed folder exists, if not, create it
    if not os.path.exists(compressed_folder_path):
        os.makedirs(compressed_folder_path)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            full_path = os.path.join(folder_path, filename)
            new_full_path = os.path.join(compressed_folder_path, filename)
            resize_image_to_longest_side(full_path, new_full_path)
            print(f"Resized and saved: {filename}")

# Example usage, assuming the script is in the same directory as the images
convert_images_to_max_dimension()
