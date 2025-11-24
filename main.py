import sys

from stats import get_num_words, get_num_of_chars, sort_dict


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_content = get_book_text(sys.argv[1])
    num_words = get_num_words(book_content)
    num_chars = get_num_of_chars(book_content)
    sorted_dict = sort_dict(num_chars)

    print(
        "============ BOOKBOT ============\n" +
        f"Analyzing book found at {sys.argv[1]}...\n" +
        "----------- Word Count ----------\n" +
        f"Found {num_words} total words\n" +
        f"--------- Character Count -------"
    )

    for elem in sorted_dict:
        if not elem["char"].isalpha():
            continue
        print(f"{elem["char"]}: {elem["num"]}")
        

    print("============= END ===============")

if __name__ == "__main__":
    main()