def main() -> None:
    try:
        with open("words.json", encoding="utf-8") as file:
            txt: str = file.read()
    except FileNotFoundError:
        print("Please make sure that you have the 'words.json' file inside this directory")
        return

    with open("words.json", "w", encoding="utf-8") as file:
        file.write("[\n")
        for line in txt.split("\n"):
            file.write(f"    {line},\n")

        file.write("]")

if __name__ == "__main__":
    main()