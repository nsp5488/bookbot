import os

def get_num_words(text:str) -> int:
    return len(text.split())

def get_letter_counts(text:str):
    d = dict()
    for c in text.strip():
        c = c.lower()
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def convert_dict(d):
    letters = []
    for key in d:
        letters.append({'character':key,'count': d[key]})

    
    letters.sort(reverse=True, key=lambda x : x['count'])
    return letters

def main():
    book_name = 'frankenstein.txt'
    book_path = os.path.join('books', book_name)
    contents = None
    with open(book_path) as f:
        contents = f.read()
    
    if contents != None:
        num_words = get_num_words(contents)
        letter_counts = get_letter_counts(contents)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document\n")

        for letter in convert_dict(letter_counts):
            if letter['character'].isalpha():
                print(f"The {letter['character']} character was found {letter['count']} times")
        print("--- End report ---")




if __name__ == '__main__':
    main()