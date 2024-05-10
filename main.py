def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = get_number_of_words(text)
    char_dict = get_char_count_dict(text)
    list_of_dict = get_list_of_dict(char_dict)
    sorted_list_by_count = get_sorted_list(list_of_dict)
    get_report(book_path, wc, sorted_list_by_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_char_count_dict(text):
    lower_cased = text.lower()
    letter_count = {}
    for character in lower_cased:
        if character.isalpha():
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    return letter_count

def get_list_of_dict(dict):
    list_of_dict = []
    for key in dict:
        list_of_dict.append({"character": key, "count": dict[key]})
    return list_of_dict

def get_sorted_list(list):
    def sort_on(dict):
        return dict["count"]
    list.sort(reverse=True, key=sort_on)
    return list

def get_report(document_name, word_count, sorted_list):
    print(f"--- Begin report of {document_name} ---\n")
    print(f"{word_count} words found in the document.\n")
    for character_count in sorted_list:
        print(f"The character '{character_count["character"]}' was found {character_count["count"]} times")
    print(f"\n------------ End of report ------------")


if __name__ == '__main__':
    main()