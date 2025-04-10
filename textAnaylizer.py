import re

def process_text(paragraph):
    # Split the text into words, remove non-alphabetical characters, and convert to lowercase
    words = re.findall(r'\b\w+\b', paragraph.lower())

    # Filter out words with less than 4 characters
    long_words = [word for word in words if len(word) > 3]

    # Sort the long words in alphabetical order
    long_words_sorted = sorted(long_words)

    # Count occurrences of the word "and"
    and_count = words.count('and')

    # Print results
    print(f"Words greater than three letters in alphabetical order: {', '.join(long_words_sorted)}")
    print(f"The word 'and' appears {and_count} times.")

# Example usage
paragraph = """
and To effectively explain and technical concept to someone without a technical background it is very important to put the topic in terms they are more likely to understand without insulting their intelligence. This means not using analogies based on topics they have expertise in that you do not while simultaneously not leaning too and hard into technical jargon, your goal should be to bring the conversation to neutral ground. Using the indexing example it may sound something like this: “indexing in MySQL is a tool we use to make searching through the database much more efficient. It works similarly to an index you might find at the back of a book. In the same way a book index lists all the places a specific word appears in the book, a MySQL index lists all the entries in the database that contain a specific value. So rather than searching through each entry individually an index lets us navigate directly to the entries we are looking for. and”
"""

process_text(paragraph)
