import tkinter as tk
import random

BOARD_SIZE = 20  # ⬅️ Set board size here

def new_game():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_spots = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                empty_spots.append((row, col))

    if len(empty_spots) == 0:
        return False

    row, col = random.choice(empty_spots)
    chance = random.random()
    board[row][col] = 4 if chance < 0.1 else 2
    return True

def merge(row):
    non_zero = [num for num in row if num != 0]
    merged = []
    skip = False
    for i in range(len(non_zero)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(non_zero[i] * 2)
            skip = True
        else:
            merged.append(non_zero[i])
    while len(merged) < BOARD_SIZE:
        merged.append(0)
    return merged

def move_left(board):
    for i in range(BOARD_SIZE):
        board[i] = merge(board[i])

def move_right(board):
    for i in range(BOARD_SIZE):
        reversed_row = list(reversed(board[i]))
        merged_row = merge(reversed_row)
        board[i] = list(reversed(merged_row))

def move_up(board):
    for col in range(BOARD_SIZE):
        column = [board[row][col] for row in range(BOARD_SIZE)]
        merged_col = merge(column)
        for row in range(BOARD_SIZE):
            board[row][col] = merged_col[row]

def move_down(board):
    for col in range(BOARD_SIZE):
        column = [board[row][col] for row in range(BOARD_SIZE)]
        reversed_col = list(reversed(column))
        merged_col = merge(reversed_col)
        merged_col = list(reversed(merged_col))
        for row in range(BOARD_SIZE):
            board[row][col] = merged_col[row]

def is_game_over(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return False
            if j + 1 < BOARD_SIZE and board[i][j] == board[i][j + 1]:
                return False
            if i + 1 < BOARD_SIZE and board[i][j] == board[i + 1][j]:
                return False
    return True

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game - 20x20")
        self.board = new_game()
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.create_ui()
        self.update_ui()

        self.root.bind("<Up>", lambda event: self.handle_move("w"))
        self.root.bind("<Left>", lambda event: self.handle_move("a"))
        self.root.bind("<Down>", lambda event: self.handle_move("s"))
        self.root.bind("<Right>", lambda event: self.handle_move("d"))

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                label = tk.Label(frame, text="", width=3, height=1, font=("Helvetica", 10), bg="lightgray", relief="ridge")
                label.grid(row=i, column=j, padx=1, pady=1)
                self.grid[i][j] = label

    def update_ui(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = self.board[i][j]
                self.grid[i][j].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {
            0: "lightgray",
            2: "lightyellow",
            4: "lightgoldenrod",
            8: "orange",
            16: "darkorange",
            32: "coral",
            64: "tomato",
            128: "gold",
            256: "khaki",
            512: "yellow",
            1024: "lightgreen",
            2048: "green",
            4096: "darkgren",
            8192: "darkgren",
            16384: "darkgren"

        }
        return colors.get(value, "black")

    def handle_move(self, direction):
        old_board = [row[:] for row in self.board]

        # if direction == "w":
        #     move_up(self.board)
        # elif direction == "a":
        #     move_left(self.board)
        # elif direction == "s":
        #     move_down(self.board)
        # elif direction == "d":
        #     move_right(self.board)

        # if self.board != old_board:
        #     add_new_tile(self.board)

        self.update_ui()

        if is_game_over(self.board):
            self.show_game_over()

    def show_game_over(self):
        game_over_label = tk.Label(self.root, text="Game Over!", font=("Helvetica", 32), fg="red")
        game_over_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
