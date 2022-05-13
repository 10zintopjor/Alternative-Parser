from distutils.command.clean import clean
from importlib.resources import path
from mailbox import linesep
from socket import inet_aton
from numpy import append
from pyewts import pyewts
from pathlib import Path
import re


def convert_willie_to_uni(word):
    converter = pyewts()
    poti_title = converter.toUnicode(word)
    return poti_title

def get_word(desc,match):
    start = match.start()-1
    word =""
    while start >= 0:
        if desc[start] == " ":
            break
        word = desc[start]+word
        start-=1
    return word

def convert_file_to_uni(text,file_name):
    lines = re.split("\n",text)
    with open(f"./uni_dic/{file_name}","a") as f:
        for line in lines:
            z = re.match("(.*),(.*)",line)
            if z:
                word = z.group(1)
                desc = z.group(2)
                #get_monlam_alt_words(word,desc,file_name)


def get_monlam_alt_words():
    alt_signs = ["དང་འདྲ","འབྲི་ཚུལ་གཞན"]
    alt_sign = "འབྲི་ཚུལ་གཞན"
    alt_words = []
    with open("./uni_dic/monlam") as file:
        for line in file:
            if alt_sign in line:
                alt_word = extract_alt_words(line,alt_sign)
                alt_words.append(alt_word)

    return alt_words


def clean_word(raw):
    li = ["ཀྱི་","གི་","གྱི་","ཡི་"]

    if "འི་" in raw[-3:]:
        return raw[:-3]+"་"

    for elm in li:
        if elm in raw[-4:]:
            return raw[:-len(elm)]

    return raw        


def extract_alt_words(line,alt_sign):
    z = re.match("^(.*),(.*)",line)
    main_word = z.group(1)
    desc = z.group(2)
    alt_words=[main_word]
    for match in re.finditer(f"{alt_sign}",desc):
        alt_word = get_word(desc,match)
        alt_words.append(alt_word)

    return alt_words    


def convert_to_csv(li):
    line = ""
    for index,elem in enumerate(li):
        line += clean_word(elem)
        if index < len(li)-1:
            line+=","
    return line


if __name__ == "__main__":
    alt_words = get_monlam_alt_words()
    with open("./alt_word.txt","a") as file:
        file.write("\n".join(convert_to_csv(word) for word in alt_words))
    #Path("./alt_word.txt").write_text(str(alt_words))