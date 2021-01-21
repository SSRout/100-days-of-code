import pandas
data=pandas.read_csv("Day26/NATO_alphabet/nato_phonetic_alphabet.csv")
#create Dictionary
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

#print(phonetic_dict)

#create phonetic code
def gen():
    try:
        word=input("enter word\n").upper()
        op=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("only alphabet please")
        gen()
    else:
        print(op)

gen()