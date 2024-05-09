def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = number_of_words(text)
    print(f"{wc} words were found in the document.")
    char_dict = get_char_count_dict(text)
    print(char_dict)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def get_char_count_dict(text):
    lower_cased = text.lower()
    letter_count = {}
    for character in lower_cased:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count

if __name__ == '__main__':
    main()