def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    list_dicts = get_list_dicts(num_chars)
    report = get_report(list_dicts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for key, value in report:
        print(f"The {key} character was found {value} times")
    print("--- End report ---")


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
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return dict(sorted(char_count.items()))


def get_list_dicts(num_chars):
    
    list_of_dicts = []

    for key, value in num_chars.items():
        list_of_dicts.append({key: value})
        
    return list_of_dicts

def get_report(list_dicts):

    for dict in list_dicts:
        for key, value in dict.items():
            yield key, value

    
main()


