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
            z = re.match("(.*),(.*)",line)
            if z:
                word = z.group(1)
                desc = z.group(2)
                get_alt_words(word,desc,file_name)

def get_alt_words(word,desc,file_name):
    alt_sign = "དང་འདྲ"
    if alt_sign not in desc:
        return
    alt_words = []
    alt_words.append(word)
    for match in re.finditer(f"{alt_sign}",desc):
        alt_words.append(get_word(desc,match))

    with open("./alt_words/monlam","a") as f:
        f.write(str(alt_words)+"\n")
    

def get_word(desc,match):
    start = match.start()-1
    word =""
    while start >= 0:
        if desc[start] == " ":
            break
        word = desc[start]+word
        start-=1
    return word



def main(dic_name):
    text = Path(f"./uni_dic/monlam").read_text()
    convert_file_to_uni(text,dic_name)


if __name__ == "__main__":
    dic_name = "monlam"
    main(dic_name)