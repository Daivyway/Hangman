import requests

def main():
    # Fetch a random word from the API
    response = requests.get("https://random-word-api.herokuapp.com/word")
    if response.status_code == 200:
        word = response.json()[0]
    else:
        print("Failed to fetch a random word. Using a default word.")
        word = "hangman"

    wrong = 0 # Initialize the number of wrong guesses

    stages = [
        "",
        "________           ",
        "|                  ",
        "|        |         ",
        "|        0         ",
        "|       /|\\       ",
        "|       / \\       ",
        "|                  "
    ]

    rletters = list(word) # Create a list of letters in the word
    board = ["__"] * len(word)
    win = False
    print("Welcome to the execution! Guess the word before the hangman is fully drawn.")

    # While loop to allow the user to guess letters until they either win or lose
    while wrong < len(stages) - 1:
        print("\n")

        msg = "Enter letter: "
        char = input(msg)

        # Check if the guessed letter is in the word
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))

        e = wrong + 1

        print("\n".join(stages[0: e]))

        # Check if the user has won by checking if there are any underscores left in the board
        if "__" not in board:
            print("You won! The word was: ")
            print(" ".join(board))

            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lost! The word was: {}".format(word))


if __name__ == "__main__":
    main()