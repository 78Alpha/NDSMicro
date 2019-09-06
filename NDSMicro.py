import os
import glob
import secrets
import shutil
import time
from subprocess import call
import zipfile
import pathlib
import zlib


def title_gen():
    title_return = []
    for i in range(9999):
        title_code = i
        if i < 10:
            title_return.append("000{}".format(i))
        elif i >= 10 and i <= 99:
            title_return.append("00{}".format(i))
        elif i >= 100 and i <= 999:
            title_return.append("0{}".format(i))
        else:
            title_return.append(str(i))
    return title_return

def game_name_list():
    cwd = os.getcwd()
    dir_list = []
    for name in glob.glob("{}\\*.nds".format(cwd)):
        dir_list.append(name)
    return dir_list

def make_wd():
    cwd = os.getcwd()
    try:
        if not os.path.exists("{}\\WORKDIR\\".format(cwd)):
            shutil.copytree(f'{cwd}\\Input\\Modded_Base', f'{cwd}\\WORKDIR\\')
    except:
        print("Cannot Create working directory! Process Halted!")
        input()
        exit()

def clean_cwd():
    cwd = os.getcwd()
    try:
        if os.path.exists("{}\\WORKDIR\\".format(cwd)):
            shutil.rmtree("{}\\WORKDIR\\".format(cwd))
    except:
        print("Could not remove WORKDIR!")
        input()
        exit()
    try:
        os.remove("{}\\rom.zip".format(cwd))
    except:
        pass

def copy_data_to_cwd():
    cwd = os.getcwd()
    try:
        os.remove("{}\\WORKDIR\\meta\\iconTex.tga".format(cwd))
        os.remove("{}\\WORKDIR\\meta\\bootTvTex.tga".format(cwd))
        os.remove("{}\\WORKDIR\\meta\\bootDrcTex.tga".format(cwd))
    except:
        print("No TGA Files Found In WORKDIR, Copying TGA!")
    shutil.copy("{}\\Input\\iconTex.tga".format(cwd), "{}\\WORKDIR\\meta".format(cwd))
    shutil.copy("{}\\Input\\bootTvTex.tga".format(cwd), "{}\\WORKDIR\\meta".format(cwd))
    shutil.copy("{}\\Input\\bootDrcTex.tga".format(cwd), "{}\\WORKDIR\\meta".format(cwd))


def gen_xml_steal(current, title_return, name):
    cwd = os.getcwd()
    pack_name = name.split("\\")
    pack_name2 = pack_name[-1].split("(")
    blacklist = "!@#$%^&*()~`,./<>?;\':\"[]{}-=_+\\"
    new_name = ""
    for letter in pack_name2[0]:
        if letter not in blacklist:
            new_name += letter
    with open(f"{cwd}\\Input\\app.xml", 'r') as app:
        data = app.readlines()
        app.close()
    app = []
    for line in data:
        if "3C00" in line:
            new_line = str(line.replace("3C00", f"{title_return[current]}"))
            app.append(new_line)
        else:
            app.append(line)
    with open(f"{cwd}\\WORKDIR\\code\\app.xml", 'w+') as out_xml:
        for line in app:
            out_xml.write(line)
        out_xml.close()
    with open(f"{cwd}\\Input\\meta.xml", 'r') as meta:
        data2 = meta.readlines()
        meta.close()
    meta = []
    for line in data2:
        if "WUP-N-DAPP" in line:
            new_line = str(line.replace("WUP-N-DAPP", f"WUP-N-{title_return[current]}"))
            meta.append(new_line)
        elif "00050000101B3C00" in line:
            new_line = str(line.replace("00050000101B3C00", f"00050000101B{title_return[current]}"))
            meta.append(new_line)
        elif "Metroid Prime Hunters" in line:
            new_line = str(line.replace("Metroid Prime Hunters", f"{new_name}"))
            meta.append(new_line)
        else:
            meta.append(line)
    with open(f"{cwd}\\WORKDIR\\meta\\meta.xml", 'w+') as new_meta:
        for line in meta:
            new_meta.write(line)
        new_meta.close()



def Nus_Pack(name, title_return, current):
    cwd = os.getcwd()
    pack_name = name.split("\\")
    pack_name2 = pack_name[-1].split("(")
    blacklist = "!@#$%^&*()~`,./<>?;\':\"[]{}-=_+\\"
    new_name = ""
    for letter in pack_name2[0]:
        if letter not in blacklist:
            new_name += letter
    call(args=['java', '-jar', 'NUSPacker.jar', '-in', f'{cwd}\\WORKDIR\\', '-out', f'{cwd}\\Output\\[NDS] {new_name} (00050000101B{title_return[current]})'])


def injectiine_Start():
    print("Process Start!\n")
    cwd = os.getcwd()
    name_list = game_name_list()
    print(name_list)
    title_return = title_gen()
    print("Starting File Gen...")
    current = 0
    for name in name_list:
        pack_name = name.split("\\")
        print(f"PROCESSING: {pack_name[-1]}\n")
        print(f"PATH: {name_list[current]}\n")

        print("Cleaning...")

        clean_cwd()

        print("Creating...")
        make_wd()

        print("Copying...")

        copy_data_to_cwd()

        print("Compressing...")

        zipfile.ZipFile('{}\\rom.zip'.format(cwd), mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=True, compresslevel=9).write("{}".format(pack_name[-1]))
        try:
            os.remove("{}\\WORKDIR\\content\\0010\\rom.zip".format(cwd))
        except:
            print("rom.zip not found! Transferring...")
        shutil.move("{}\\rom.zip".format(cwd), "{}\\WORKDIR\\content\\0010\\".format(cwd))
        print("Generating...")
        # gen_app_xml(current, title_return, name=pack_name[-1])
        gen_xml_steal(current, title_return, name=pack_name[-1])
        print("Packing...")
        Nus_Pack(name, title_return, current)
        current += 1

injectiine_Start()
