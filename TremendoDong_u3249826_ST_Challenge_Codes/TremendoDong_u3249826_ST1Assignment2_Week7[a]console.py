# TremendoDong_u3249826_ST1Assignment2_Week7[a]console

def main():
    num_words = int(input("How many words would you like to write to the file? "))
    with open('words.txt', 'w') as file:
        for i in range(num_words):
            word = input(f"Enter word {i+1}: ")
            file.write(word + '\n')

if __name__ == "__main__":
    main()
