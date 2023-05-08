# This program consist of two functions which encodes the user input by moving each letter by 15 character.

# below function changes the letter
def change_letter(letter):
    """This function takes a letter as input and return a new encoded letter"""
    # All characters apart from alphabet, stays as it is
    if ord(letter) < 65 or ord(letter) > 122:
        new_letter = letter
        # Checks if it is a capital letter and changes it
    elif ord(letter) < 91:
        if ord(letter) + 15 > 90:
            new_letter = chr(ord(letter) - 11)
        else:
            new_letter = chr(ord(letter) + 15)
    # Checks if it's lowercase letter and changes it
    elif ord(letter) < 123:
        if ord(letter) + 15 > 122:
            new_letter = chr(ord(letter) - 11)
        else:
            new_letter = chr(ord(letter) + 15)
    return new_letter


# function below makes a new sentence
def change_sentence():
    """This function takes user input and prints encoded sentence by using change_letter() function"""
    new_sentence = ""
    for letter in text:
        new_letter = change_letter(letter)
        new_sentence += new_letter
    print(f"Your encoded text is: {new_sentence}\n")

# Program will ask if the user wish to continue creating sentences


run_again = True
while run_again:

    text = input("Please input the text you wish to encode:  ")
    change_sentence()
    choice = input("Would you like to encode another word/sentence? Type (Y/N)?: ").lower()

    if choice == "n":
        print("Thank you. Goodbye.")
        run_again = False
