from json import load, dump
from typing import List, Dict

def nicer_formatting() -> None:
    with open("filtered.json", encoding="utf-8") as file:
        txt: str = file.read()

    with open("filtered.json", "w", encoding="utf-8") as file:
        file.write("{\n")
        for line in txt.split("]"):
            if line[0] == ",":
                file.write(f"   {line[1:]}],\n")

        file.write("}")

def main() -> None:
    filtered_dictionary: Dict[str, List[str]] = {}
    try:
        with open("words.json", encoding="utf-8") as input_file:
            unfiltered_dictionary: List[Dict[str, str]] = load(input_file)
    except FileNotFoundError:
        print("Please make sure that you have the 'words.json' file inside this directory")
        return

    for data in unfiltered_dictionary:
        word: str = data["text"]
        sounds: List[str] = word.split()
        if len(sounds) != 2:
            continue

        head: str = sounds[0].lower()
        tail: str = sounds[1].lower()
        if head in filtered_dictionary:
            filtered_dictionary[head] += [tail]
        else:
            filtered_dictionary[head] = [tail]

    with open("filtered.json", "w", encoding="utf-8") as output_file:
        dump(filtered_dictionary, output_file, ensure_ascii=False)

    nicer_formatting()

if __name__ == "__main__":
    main()