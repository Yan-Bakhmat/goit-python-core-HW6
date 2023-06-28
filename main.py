from pathlib import Path
import shutil
import sys
import os
import re


def category(extension):
    if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
        return 'images'
    elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
        return 'video'
    elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
        return 'documents'
    elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
        return 'audio'
    elif extension in ['ZIP', 'GZ', 'TAR']:
        return 'archives'
    else:
        return 'Unknown extensions'


def normalize(name):
    translate_to_latin = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'h', ord('ґ'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y', ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu', ord('я'): 'ya',
                          ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'H', ord('Ґ'): 'G', ord('Д'): 'D', ord('Е'): 'E', ord('Є'): 'YE', ord('Ж'): 'ZH', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'YI', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'KH', ord('Ц'): 'TS', ord('Ч'): 'CH', ord('Ш'): 'SH', ord('Щ'): 'SHCH', ord('Ю'): 'YU', ord('Я'): 'YA'}
    name.translate(translate_to_latin)
    re.sub(r"\W", "_", name)


def sort_files(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            sort_files(item_path)
            if not os.listdir(item_path):
                os.rmdir(item_path)
        elif os.path.isfile(item_path):
            extension = item.split('.')[-1].upper()
            if extension in ['JPEG', 'PNG', 'JPG', 'SVG', 'AVI', 'MP4', 'MOV', 'MKV', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'MP3', 'OGG', 'WAV', 'AMR']:
                category_folder = category(extension)
                category_path = os.path.join(path, category_folder)
                if not os.path.exists(category_path):
                    os.mkdir(category_path)
                src_path = os.path.join(path, item)
                dst_path = os.path.join(category_path, item)
                shutil.move(src_path, dst_path)
            else:
                pass


if __name__ == '__main__':
    sort_files(Path(sys.argv[1]))
