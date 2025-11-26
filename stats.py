def get_num_words(book: str) -> int:
    return len(book.split())

def get_num_of_chars(book: str) -> dict[str, int]:
    num_chars: dict[str, int] = {}
    for char in book.lower():
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars

def sort_dict(num_chars: dict[str, int]) -> list:
    sorted_dict = []
    for char in num_chars:
        num = num_chars[char]
        sorted_dict.append({"char": char, "num": num})
    sorted_dict.sort(reverse=True, key=lambda ch: ch["num"])
    return sorted_dict
