def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = get_number_of_words(text)
    print(f"{wc} words found in the document.")
    char_dict = get_char_count_dict(text)
    print(char_dict)
    list_of_dict = get_list_of_dict(char_dict)
    print(list_of_dict)

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
        list_of_dict.append({key: dict[key]})
    return list_of_dict

if __name__ == '__main__':
    main()