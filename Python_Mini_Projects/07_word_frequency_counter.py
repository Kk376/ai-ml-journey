"""
Word Frequency Counter
Counts how often each word appears in entered text.
"""


def clean_text(raw_text):
    # punctuation characters won't be checked for frequency
    punctuation = ".,!?;:\"'()[]{}--_/"

    # replace punctuation with space
    cleaned = ""
    for char in raw_text.lower():
        if char in punctuation:
            cleaned += " "
        else:
            cleaned += char

    # split text by whitespace into a list of words
    words = cleaned.split()
    return words


def count_frequencies(words):
    # count occurrences of each word
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def get_frequency(item):
    # tuple key function for sorted
    return item[1]


def display_results(counts, total_words):
    if not counts:
        print("\nNo valid words found in the provided text.")
        return

    unique_count = len(counts)

    # convert dictionary items into a list of tuples to sort by count
    items_list = list(counts.items())
    sorted_words = sorted(items_list, key=get_frequency, reverse=True)

    most_common = sorted_words[0]
    least_common = sorted_words[-1]

    print("\n" + "=" * 45)
    print("            WORD FREQUENCY REPORT")
    print("=" * 45)
    print(f"Total Words Processed : {total_words}")
    print(f"Unique Words Count    : {unique_count}")
    print(f"Most Common Word      : '{most_common[0]}' ({most_common[1]} times)")
    print(f"Least Common Word     : '{least_common[0]}' ({least_common[1]} times)")
    print("-" * 45)
    print(f"{'WORD':<25} | {'FREQUENCY':<10}")
    print("-" * 45)

    for word, freq in sorted_words:
        print(f"{word:<25} | {freq:<10}")
    print("=" * 45)


def run_word_counter():
    print("=========================================")
    print("     Welcome to Word Frequency Counter   ")
    print("=========================================")

    while True:
        print("\nPlease enter or paste your text below:")
        user_input = input("> ").strip()

        if user_input == "":
            print("Input text was empty. Try typing a sentence or paragraph.")
            continue

        word_list = clean_text(user_input)
        total_words = len(word_list)
        word_counts = count_frequencies(word_list)

        display_results(word_counts, total_words)

        print("\nWould you like to analyze another text?")
        choice = input("Enter 'y' for yes, any other key to exit: ").strip().lower()
        if choice != "y":
            print("\nThank you for using Word Frequency Counter! Goodbye.")
            break


if __name__ == "__main__":
    run_word_counter()
