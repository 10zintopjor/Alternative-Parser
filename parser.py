from importlib.resources import path
from mailbox import linesep
from pyewts import pyewts
from pathlib import Path
import re

def convert_willie_to_uni(word):
    converter = pyewts()
    poti_title = converter.toUnicode(word)
    return poti_title

def split_word_and_desc(line):
    pass

def convert_file_to_uni(text,file_name):
    lines = re.split("\n",text)
    with open(f"./uni_dic/{file_name}","a") as f:
        for line in lines:
            z = re.match("(.*)\|(.*)",line)
            if z:
                word =convert_willie_to_uni(z.group(1))
                desc = convert_willie_to_uni(z.group(2))
                f.write(f"{word},{desc}\n")


if __name__ == "__main__":
    text = Path("./willie_dic/34-dung-dkar-tshig-mdzod-chen-mo-Tib").read_text()
    file_name = Path("./willie_dic/34-dung-dkar-tshig-mdzod-chen-mo-Tib").stem
    convert_file_to_uni(text,file_name)
