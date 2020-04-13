# backupToZip.py
# Copies entire folder into a zip file
# Increments the filename of the zip

import zipfile, os

def backupToZip(folder):
    # Backup the contents of folder to zip file

    folder = os.path.abspath(folder)

    # Increment the output filename if needed
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Compress each file within each subfolder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s' % (foldername))
        # Add the current folder to the zip
        backupZip.write(foldername)

        # Add the files in current folder to the zip
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Finished')

# Windows
# backupToZip('C:\\myfolder')

# Mac (in current working directory)
backupToZip('myfolder')

