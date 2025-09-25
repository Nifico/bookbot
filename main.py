from stats import get_num_words
from stats import get_char_num
from stats import get_sorted_list
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    book = "empty"
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    #print(f"{get_num_words(book)} words found in the document")

    #print(f"count\n{get_char_num(book)}" )
    sorted_list = get_sorted_list(get_char_num(book))
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {get_num_words(book)} total words")
    print(f"--------- Character Count -------")
    for i in range(len(sorted_list)):
        if sorted_list[i]['char'].isalpha():
            print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")
main()