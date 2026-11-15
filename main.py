LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def writer(Filename: str, Content: str) -> None:
    """Saves the text to a file with the given filename."""
    file = open(Filename, 'w', encoding="UTF-8")
    file.write(Content)
    file.close()

def rowmaker() -> str:
    """Asks rows from the user until an empty row. Returns all rows joined with newlines."""
    print("Collecting plain text rows for ciphering.")
    Content: str = ""
    while True:
        Row = input("Insert row(empty stops): ")
        if len(Row) == 0:
            break
        Content += Row + "\n"
    return Content

def swift(Character: str, Alphabets: str, Shift: int = 13) -> str:
    """Shifts one character by Shift positions in the given alphabets."""
    Index = Alphabets.find(Character)
    return Alphabets[(Index + Shift) % len(Alphabets)]

def forest(Content: str) -> str:
    """Applies ROT13 to letters, other characters remain the same."""
    Result: str = ""
    for Character in Content:
        if Character in LOWER_ALPHABETS:
            Result += swift(Character, LOWER_ALPHABETS)
        elif Character in UPPER_ALPHABETS:
            Result += swift(Character, UPPER_ALPHABETS)
        else:
            Result += Character
    return Result

def main() -> None:
    print("Program starting.")
    print()
    PlainText: str = rowmaker()
    CipheredText: str = forest(PlainText)

    print()
    print("#### Ciphered text ####")
    print(CipheredText)
    print("#### Ciphered text ####")

    Filename: str = input("Insert filename to save: ")
    if len(Filename.strip()) == 0:
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writer(Filename, CipheredText)
        print("Ciphered text saved!")
    print("Program ending.")


if __name__ == "__main__":
    main()
