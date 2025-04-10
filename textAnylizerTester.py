import nltk
import string
from collections import Counter

# Function to count number of occurrences of a word in a text
def count_occurrences(text, word):
    # Converting word to lowercase for case insensitivity
    word = word.lower()
    return Counter(text).get(word)
    
def sort_words(words):
    # Sorting words alphabetically by their counts in descending order
    sorted_words = sorted(list(Counter(w.split())).items(), key=lambda x: -x[1])
    return sorted_words

def find_greater_than_three(text, word):
    # Checking if word is greater than three letters long in alphabetical order
    count = count_occurrences(text, word)
    if count > 3:
        return True
    else:
        return False

def main():
    text = input("Enter a paragraph of text to find and count the longer words: ").strip()
    # Removing punctuation and converting to lowercase
    text = ' '.join(text.split())
    text = text.lower()
    
    words_list = nltk.word_tokenize(text)
    words = []
    for word in words_list:
        if word[0] != 'a':
            continue
        try:
            count = count_occurrences(words, word)
            # Checking if the word is longer than three letters long in alphabetical order
            if count > 3:
                # Sorting the words alphabetically by their counts in descending order
                sorted_words = sort_words(sorted(list(Counter(w.split())).items(), key=lambda x: -x[1]))
                # Printing all longer and shorter words
                print("Longer Word (count > 3): ", word)
                print("Shortest Word (count < 3): ", sorted_words[0][1])
            else:
                # If the word is not greater than three letters long in alphabetical order, no need to sort it.
                pass
        except Exception as e:
            print(f"Error: {e}")
    
    main()

if __name__ == '__main__':
    main()