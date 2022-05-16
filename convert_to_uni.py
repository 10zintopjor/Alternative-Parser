from pyewts import pyewts
from pathlib import Path
import re

def convert_willie_to_uni(word):
    converter = pyewts()
    poti_title = converter.toUnicode(word)
    return poti_title


def convert_file_to_uni(file_name):
    with open(f"./willie_dic/{file_name}") as file:
        for line in file:
            z = re.match("(.*)\|(.*)",line)
            if z:
                word = z.group(1)
                desc = z.group(2)
                write_file(word,desc,file_name)

def write_file(word,desc,file_name):
    word_uni = convert_willie_to_uni(word)
    desc_uni = convert_willie_to_uni(desc)

    with open(f"./uni_dic/{file_name}","a") as file:
        file.write(word_uni+","+desc_uni+"\n")


if __name__ == "__main__":
    file_name = "09-DanMartin"
    convert_file_to_uni(file_name)
