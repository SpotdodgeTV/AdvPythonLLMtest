import re

def analyze_text(text):
    # Split text into individual words
    words = re.findall(r'\b\w+\b', text)

    # Filter out words with less than or equal to 3 letters
    filtered_words = [word for word in words if len(word) > 3]

    # Sort the filtered words alphabetically
    sorted_words = sorted(filtered_words, key=lambda x: x.lower())

    # Count occurrences of "and"
    and_count = text.count('and')

    print("Words with more than 3 letters:")
    for word in sorted_words:
        print(word)

    print(f"'and' appears {and_count} times.")

if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    analyze_text(paragraph)