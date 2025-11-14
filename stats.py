
def get_book_text(filepath):
    with open(filepath) as b:
        contents = b.read()
    return contents


def get_word_count(filepath):
    contents = filepath.split()
    word_count = len(contents)
    print("Found " + str(word_count) + " total words")


def get_character_count(filepath):
    characters = {}
    a = filepath
    for letter in a:
        letter = letter.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(item):
    return item["num"]

def sorter(characters):
    result = []
    for Key in characters:
        my_dict = {"char": Key, "num": characters[Key]}
        result.append(my_dict)
    result.sort(reverse=True, key=sort_on)
    return result

def alphabetizer(result):
    for char in result:
        if char["char"].isalpha():
            final = f'{char["char"]}: {char["num"]}'
            print(final)