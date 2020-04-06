import os
import shutil


def main(fileFormat, folder):
    moved = 0
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    for file in os.listdir(os.getcwd()):
        if file.endswith(tuple(fileFormat)):
            shutil.move(file, folder)
            moved += 1
    if len(os.listdir(folder)) == 0:
        os.rmdir(folder)
    elif moved == 0:
        pass
    else:
        print("Moved in total {} file(s) to {}.".format(moved, folder))


# Getting into the Downloads folder
os.chdir(os.path.expanduser("~") + os.sep + "Downloads")


# Creating lists for the file formats and folders
vids = ['.mp4', '.mkv', '.avi', '.mpg', '.mov', '.wmv', '.webm', '.mp2', '.mpeg', '.mpe', '.mpv', '.m4p', '.m4v', '.mov']
pics = ['.gif', '.jpg', '.png', '.tif', '.tiff', '.webp', '.psd', '.raw', '.arw', '.cr2', '.nrw', '.k25', '.svg']
audio = ['.mp3', '.aac', '.wav', '.flac', '.alac', '.dsd', '.aif', '.cda', '.mid', '.midi', '.mpa', '.wpl' ]
compressed = ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', 'zip']
discMedia = ['.dmg', '.iso', '.toast', '.vcd']
email = ['.email', '.eml', 'emlx', '.msg', '.oft', '.ost', '.pst', '.vcf']
executable = ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.py', '.wsf']
wordProcessor = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd']

folderConjunction = {
    'Vids': vids, 'Pics': pics, 'Audio': audio, 'Compressed': compressed, 'DiscMedia': discMedia,
    'Email': email, 'Executables': executable, 'wordProcessor': wordProcessor
}

# loop
for i in folderConjunction:
    main(folderConjunction[i], i)
