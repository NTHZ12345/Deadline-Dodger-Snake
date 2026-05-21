# Deadline Dodger Snake
# COMP9001 Final Project
# Run with: python main.py
# Controls: W/A/S/D + Enter

import random

WIDTH = 12
HEIGHT = 8
HIGH_SCORE_FILE = "high_score.txt"

snake = [(3, 3), (3, 2), (3, 1)]
food = (5, 6)
score = 0
current_direction = "d"


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(high_score))


high_score = load_high_score()


def reset_high_score():
    global high_score

    high_score = 0
    save_high_score(high_score)
    print("High score has been reset.")


def reset_game():
    global snake, food, score, current_direction

    snake = [(3, 3), (3, 2), (3, 1)]
    food = generate_food()
    score = 0
    current_direction = "d"


def show_intro():
    print("==============================")
    print("   DEADLINE DODGER SNAKE")
    print("==============================")
    print("Collect study points. Avoid burnout.")
    print("S = Student Snake")
    print("F = Focus Point")
    print("Controls: W/A/S/D + Enter")
    input("Press Enter to start...")


def draw_board():
    print("\nStudy Points:", score)
    print("Best Record:", high_score)

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if row == 0 or row == HEIGHT - 1 or col == 0 or col == WIDTH - 1:
                print("#", end="")
            elif (row, col) in snake:
                print("S", end="")
            elif (row, col) == food:
                print("F", end="")
            else:
                print(" ", end="")
        print()


def generate_food():
    while True:
        new_food = (
            random.randint(1, HEIGHT - 2),
            random.randint(1, WIDTH - 2)
        )

        if new_food not in snake:
            return new_food


def move_snake(direction):
    global food, score, high_score, current_direction

    opposites = {
        "w": "s",
        "s": "w",
        "a": "d",
        "d": "a"
    }

    if direction in opposites:
        if direction != opposites[current_direction]:
            current_direction = direction
    else:
        print("Invalid move!")
        return True

    head_row, head_col = snake[0]

    if current_direction == "w":
        head_row -= 1
    elif current_direction == "s":
        head_row += 1
    elif current_direction == "a":
        head_col -= 1
    elif current_direction == "d":
        head_col += 1

    if head_row == 0:
        head_row = HEIGHT - 2
    elif head_row == HEIGHT - 1:
        head_row = 1

    if head_col == 0:
        head_col = WIDTH - 2
    elif head_col == WIDTH - 1:
        head_col = 1

    new_head = (head_row, head_col)

    if new_head in snake:
        print("\nBURNOUT!")
        print("Study Points Earned:", score)

        if score > high_score:
            high_score = score
            save_high_score(high_score)
            print("New Best Record:", high_score)
        else:
            print("Best Record:", high_score)

        return False

    snake.insert(0, new_head)

    if new_head == food:
        score += 10
        food = generate_food()
    else:
        snake.pop()

    return True


if __name__ == "__main__":

    show_intro()

    playing = True

    while playing:
        running = True

        while running:
            draw_board()
            direction = input("Move (W/A/S/D): ").lower()
            running = move_snake(direction)

        choice = input("\nPlay again? (Y/N) or reset high score? (R): ").lower()

        if choice == "y":
            reset_game()
        elif choice == "r":
            reset_high_score()
            reset_game()
        else:
            playing = False
            print("Thanks for playing!")