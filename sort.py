from pathlib import Path
import sys
import os
import shutil
import re

images_types = {'JPEG', 'PNG', 'JPG', 'SVG'}
videos_types = {'AVI', 'MP4', 'MOV', 'MKV'}
docs_types = {'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'}
musics_types = {'MP3', 'OGG', 'WAV', 'AMR'}
archives_types = {'ZIP', 'GZ', 'TAR'}
finding_types = images_types | videos_types | docs_types | musics_types | archives_types

known_types = set()
unknown_types = set()

list_images = []
list_videos = []
list_docs = []
list_musics = []
list_archives = []


def normalize(name):
    translate_to_latin = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'h', ord('ґ'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y', ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu', ord('я'): 'ya',
                          ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'H', ord('Ґ'): 'G', ord('Д'): 'D', ord('Е'): 'E', ord('Є'): 'YE', ord('Ж'): 'ZH', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'YI', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'KH', ord('Ц'): 'TS', ord('Ч'): 'CH', ord('Ш'): 'SH', ord('Щ'): 'SHCH', ord('Ю'): 'YU', ord('Я'): 'YA'}
    name.translate(translate_to_latin)
    re.sub(r"\W", "_", name)


def sort_folder(folder):
    for object in os.listdir(folder):
        object_folder = os.path.join(folder, object)
        if os.path.isfile(object_folder):
            if object.split('.')[-1].upper().removeprefix(".") in finding_types:
                known_types.add(object.split(
                    '.')[-1].upper().removeprefix("."))
                if object.split('.')[-1].upper().removeprefix(".") in images_types:
                    list_images.append(object)
                    type_folder = os.path.join(folder, "images")
                    if not os.path.exists(type_folder):
                        os.mkdir(type_folder)
                elif object.split('.')[-1].upper().removeprefix(".") in videos_types:
                    list_videos.append(object)
                    type_folder = os.path.join(folder, "video")
                    if not os.path.exists(type_folder):
                        os.mkdir(type_folder)
                elif object.split('.')[-1].upper().removeprefix(".") in docs_types:
                    list_docs.append(object)
                    type_folder = os.path.join(folder, "documents")
                    if not os.path.exists(type_folder):
                        os.mkdir(type_folder)
                elif object.split('.')[-1].upper().removeprefix(".") in musics_types:
                    list_musics.append(object)
                    type_folder = os.path.join(folder, "audio")
                    if not os.path.exists(type_folder):
                        os.mkdir(type_folder)
                elif object.split('.')[-1].upper().removeprefix(".") in archives_types:
                    list_archives.append(object)
                    type_folder = os.path.join(folder, "archives")
                    if not os.path.exists(type_folder):
                        os.mkdir(type_folder)
            else:
                unknown_types.add(object.split(
                    '.')[-1].upper().removeprefix("."))
        elif os.path.isdir(object_folder):
            sort_folder(object_folder)
            if not os.listdir(object_folder):
                os.rmdir(object_folder)


"""
def scan_folder(folder):
    for object in folder.iterdir():
        if object.is_file():
            if object.suffix.upper().removeprefix(".") in finding_types:
                known_types.add(object.suffix.upper().removeprefix("."))
                if object.suffix.upper().removeprefix(".") in images_types:
                    list_images.append(object.name)
                elif object.suffix.upper().removeprefix(".") in videos_types:
                    list_videos.append(object.name)
                elif object.suffix.upper().removeprefix(".") in docs_types:
                    list_docs.append(object.name)
                elif object.suffix.upper().removeprefix(".") in musics_types:
                    list_musics.append(object.name)
                elif object.suffix.upper().removeprefix(".") in archives_types:
                    list_archives.append(object.name)
            else:
                unknown_types.add(object.suffix.upper().removeprefix("."))
        elif object.is_dir():
            scan_folder(object)
"""

sort_folder(Path(sys.argv[1]))

print(f"Images: {list_images}")
print(f"Videos: {list_videos}")
print(f"Docs: {list_docs}")
print(f"Musics: {list_musics}")
print(f"Archives: {list_archives}")

print(f"Known types: {known_types}")
print(f"Unknown types: {unknown_types}")
