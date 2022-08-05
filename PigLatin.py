"""To form Pig Latin, you take an English word that begins with a consonant, move that
consonant to the end, and then add “ay” to the end of the word. If the word begins with
a vowel, you simply add “way” to the end of the word. One of the most famous Pig Latin
phrases of all time is “ixnay on the ottenray,” uttered by Marty Feldman in Mel Brooks’s
comedic masterpiece Young Frankenstein."""


#Setting consonants and vowels:
consonants = ('B', 'C', 'D', 'F', 'G', 'H', 'N', 'P', 'Q', 'R', 'S', 'T')
vowels = ('A', 'E', 'I', 'O', 'U')


def main():
    while True:
    #getting the word from user
        user_word = input("Enter a word or L to leave: ").upper()

    #if word starts with consonant do:
        if user_word[0] in consonants:
            print(user_word[1:] + user_word[0] + 'AY')
    #if word starts with vowel do:
        elif user_word[0] in vowels:
            print(user_word + "WAY")
    #Giving him the option to leave:
        elif user_word == 'L':
            print("Have a great time! ")
            break
    #for invalid input
        else:
            print("Invalid input :/")
            continue



if __name__ == '__main__':
    main()


