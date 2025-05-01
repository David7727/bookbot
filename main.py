import sys
from textstats import word_count, counter, create_character_reports

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    booktext = get_book_text(path)
    num_words = word_count(booktext)
    char_counts = counter(booktext)
    reports = create_character_reports(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for report in reports:
        print(f"{report['char']}: {report['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
