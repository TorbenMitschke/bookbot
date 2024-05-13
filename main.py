from collections import defaultdict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = get_number_of_words(text)
    char_to_count = get_char_to_count_dictionary(text)
    sorted_list_by_count = get_sorted_list_of_char_to_count(char_to_count)
    get_report(book_path, wc, sorted_list_by_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_char_to_count_dictionary(text):
    char_to_count = defaultdict(lambda: 0)
    for character in text:
        if character.isalpha():
            char_to_count[character.lower()] += 1
    return char_to_count

def sort_on(char_to_count):
        return char_to_count["count"]

def get_sorted_list_of_char_to_count(char_to_count):
    sorted_list_of_char_to_count = []
    for key in char_to_count:
        sorted_list_of_char_to_count.append({"character": key, "count": char_to_count[key]})
    sorted_list_of_char_to_count.sort(reverse=True, key=sort_on)
    return sorted_list_of_char_to_count

def get_report(document_name, word_count, sorted_list):
    print(f"--- Begin report of {document_name} ---\n")
    print(f"{word_count} words found in the document.\n")
    for character_count in sorted_list:
        print(f"The character '{character_count["character"]}' was found {character_count["count"]} times")
    print(f"\n------------ End of report ------------")


if __name__ == '__main__':
    main()