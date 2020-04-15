# resize_add_logo.py

# Resize all images in cwd to 300x300,
# adds preset logo to lower-right corner

import os
from PIL import image

square_fit_size = 300
logo_file = 'catlogo.png'

logo_img = Image.open(logo_file)
logo_width, logo_height = logo_img.size

os.makedirs('withLogo', exist_ok=True)
# Loop over the files in the directory
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == logo_file:
            continue
    im = Image.open(filename)
    width, height = im.size

    # Resize if needed
    if width > square_fit_size and height > square_fit_size:
        # Calculate the new dimensions
        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        # resize
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo
    print('Adding logo to %s...' % (filename))
    im.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    # Save
    im.save(os.path.join('withLogo', filename))
