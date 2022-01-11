import zipfile, os

def backupToZip(folder):
    folder1 = os.path.abspath(folder)
    number = 1

    while True:
        zipFilename = os.path.basename(folder1) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder1):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)
        for file in filenames:
            newBase = os.path.basename(folder1) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, file))
    backupZip.close()
    print('Done')