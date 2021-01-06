PLACEHOLDER="[name]"

with open("Day24/input/names/invited_name.txt") as names_file:
    names=names_file.readlines()
    print(names)


with open("Day24/input/letters/starting_letter.docx") as letter_file:
    letters=letter_file.read()
    for name in names:
        new_letter=letters.replace(PLACEHOLDER,name.strip())
        print(new_letter)
        with open(f"Day24/output/RedyToSend/Letter_for_{name.strip()}.docx",mode="w") as file:
            file.write(new_letter)
