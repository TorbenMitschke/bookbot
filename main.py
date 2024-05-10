def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = get_number_of_words(text)
    char_dict = get_char_count_dict(text)
    sorted_list_by_count = get_sorted_list_of_dict(char_dict)
    get_report(book_path, wc, sorted_list_by_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_char_count_dict(text):
    lower_cased = text.lower()
    char_count = {}
    for character in lower_cased:
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
    return char_count

def sort_on(dict):
        return dict["count"]

def get_sorted_list_of_dict(dict):
    sorted_list_of_dict = []
    for key in dict:
        sorted_list_of_dict.append({"character": key, "count": dict[key]})
    sorted_list_of_dict.sort(reverse=True, key=sort_on)
    return sorted_list_of_dict

def get_report(document_name, word_count, sorted_list):
    print(f"--- Begin report of {document_name} ---\n")
    print(f"{word_count} words found in the document.\n")
    for character_count in sorted_list:
        print(f"The character '{character_count["character"]}' was found {character_count["count"]} times")
    print(f"\n------------ End of report ------------")


if __name__ == '__main__':
    main()