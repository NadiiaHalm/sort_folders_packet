from pathlib import Path
import sys

images = []
videos = []
documents = []
musics = []
archives = []
folders = []
others = []
unknown = set()
extensions = set()

registered_extentions = {
    'JPEG' : images, 'PNG' : images, 'JPG' : images,
    'AVI' : videos, 'MP4' : videos,
    'DOC' : documents, 'DOCX' : documents, 'TXT' : documents,
    'MP3' : musics, 'OGG' : musics,
    'ZIP' : archives, 'GZ' : archives, 'TAR' : archives,
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('JPEG', 'PNG', 'JPG', 'AVI', 'TXT', 'MP3', 'MP4', 'DOCX', 'DOC', 'OGG', 'ARCHIVE', 'OTHER'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extentions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    folder = Path(path)

    scan(folder)

