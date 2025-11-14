
from stats import get_word_count
from stats import get_character_count
from stats import sorter
from stats import alphabetizer
import sys
def get_book_text(filepath):
    with open(filepath) as b:
        contents = b.read()
    return contents
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]



def main(filepath):
    a = get_book_text(filepath)
    c = get_character_count(a)
    d = sorter(c)
    starter_message = f"Analyzing book found at {filepath}..."
    print("============ BOOKBOT ============")
    print(starter_message)
    print("----------- Word Count ----------")
    get_word_count(a)
    print("--------- Character Count -------")
    alphabetizer(d)
    print("============= END ===============")
main(book_path)
