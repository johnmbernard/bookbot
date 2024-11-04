def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"dictionary of character counts: {num_chars}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_chars(text):
    lower_case = text.lower()
    char_count = {}

    for char in lower_case:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return dict(sorted(char_count.items()))


    
main()


