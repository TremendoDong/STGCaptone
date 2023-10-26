# TremendoDong_u3249826_ST1Assignment2_Week7[b]

def read_words_from_file(filename='words.txt'):
    with open(filename, 'r') as file:
        return [word.strip() for word in file.readlines()]

def main():
    words = read_words_from_file()
    num_words = len(words)
    longest_word = max(words, key=len)
    avg_length = sum(len(word) for word in words) / num_words

    print(f"Number of words in the file: {num_words}")
    print(f"Longest word in the file: {longest_word}")
    print(f"Average length of all of the words: {avg_length:.2f}")

if __name__ == "__main__":
    main()
