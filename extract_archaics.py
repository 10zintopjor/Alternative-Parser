import requests
import yaml

url = "https://raw.githubusercontent.com/Esukhia/Tibetan-archaic2modern-word/main/arch_modern.yml"

def extract():
    alt_words =[]
    res = requests.get(url)
    parsed_yml = yaml.load(res.text,Loader=yaml.FullLoader)
    for id in parsed_yml:
        moderns = parsed_yml[id]["modern"]
        archaic = parsed_yml[id]["archaic"]
        moderns.append(archaic)
        alt_words.append(moderns)        
    return alt_words

def convert_to_csv(li):
    line = ""
    for index,elem in enumerate(li):
        line += elem
        if index < len(li)-1:
            line+=","
    return line

if __name__ == "__main__":
    alt_words = extract()  
    with open("./alt_word_archaic.txt","a") as file:
        file.write("\n".join(convert_to_csv(word) for word in alt_words))  