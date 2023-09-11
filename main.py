import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(file):
    words = file.split()
    counter = 0
    for word in words:
        counter += 1
    print(counter)

def count_letters(str):
    new_str = str.lower()
    alphabet = list(string.ascii_lowercase)
    letter_counter = {}
    
    
    for letter in alphabet:
        letter_counter.update({letter:0})
    
    for letter in new_str:
        if letter in letter_counter:
            letter_counter[letter] += 1

    list_of_pairs = letter_counter.items()
    list_of_pairs = sorted(list_of_pairs)

    print(list_of_pairs)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(letter_counter.values())} words were found in the document.")
   
    for pair in list_of_pairs:
        print(f"The character {pair[0]} was found {pair[1]} times.")


    

    

    #for pair in list_of_counter:
     #   print(f"The {pair.key()} character was found {pair.value()} times")





count_letters(file_contents)

