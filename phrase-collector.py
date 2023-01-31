open_letter = ("Pictures on the floor, ")

for letter in open_letter:
    letter = letter.split()
phrase = input(str("Type the next phrase: "))
letter += phrase
open_letter += (" " + phrase + " ")

print(open_letter + "Your phrase has ", len(letter), "letters.")