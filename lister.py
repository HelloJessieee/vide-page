import os
import json
try:
    from PIL import Image
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError as e:
    print("Got import error", e)
    print("You need to install pillow and pillow-heif: `pip3 install pillow pillow-heif`")
    import sys; sys.exit(1);

print("Scanning directory for images...")
files = []
supported_extensions = ['.jpg', '.jpeg', '.png', '.heic', '.webp']  # 添加更多支持的格式
for file in os.listdir("."):
    ext = os.path.splitext(file)[1].lower()
    if ext in supported_extensions:
        try:
            im = Image.open(file)
            print(f"Successfully processed: {file} ({im.width}x{im.height})")
            files.append([file, [im.width, im.height]])
        except Exception as e:
            print(f"Failed to process {file}: {str(e)}")
    else:
        print(f"Skipping non-image file: {file}")

json.dump(files, open("image_widths_heights.json", 'w'))
print(f"Successfully created image_widths_heights.json with {len(files)} files.")