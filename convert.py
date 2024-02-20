import subprocess
import os

def convert_heic_to_png(heic_path, png_path):
    command = ['heif-convert', heic_path, png_path]
    subprocess.run(command, check=True)

def convert_all_heic_to_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            png_path = os.path.splitext(heic_path)[0] + ".png"
            try:
                convert_heic_to_png(heic_path, png_path)
                print(f"Converted {heic_path} to {png_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {heic_path}: {e}")

current_directory = os.getcwd()
convert_all_heic_to_png(current_directory)

