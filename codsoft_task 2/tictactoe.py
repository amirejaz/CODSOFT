from tkinter import *
from tkinter import messagebox

def evaluate(board):
    # Rows, columns, and diagonals to check for a win
    lines = board + [[board[i][j] for i in range(3)] for j in range(3)] + \
            [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

    for line in lines:
        if all(cell == "X" for cell in line):
            return 10
        elif all(cell == "O" for cell in line):
            return -10
    return 0

def is_moves_left(board):
    return any(cell == "-" for row in board for cell in row)

def minimax(board, depth, is_maximizer, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_maximizer:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = "-"
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = "-"
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = (-1, -1)
    best_val = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "X"
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = "-"

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("440x440+400+80")
        self.root.resizable(False,False)
        self.root.config(bg="palegreen3")

        self.board = [["-" for _ in range(3)] for _ in range(3)]
        self.player_turn = True  # True for human, False for AI

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(root, text="", font=("normal", 30), width=6, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        quitbtn = Button(self.root, text="Quit",cursor="hand2",command=self.quit_, bg="red", fg="white", font=("Helvetica", 25)).place(x=160, y=380, width=120, height=30)

    def on_button_click(self, row, col):
        if self.player_turn and self.board[row][col] == "-":
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled")
            self.player_turn = not self.player_turn
            self.check_game_result()

            if not self.player_turn:
                self.ai_move()

    def ai_move(self):
        row, col = find_best_move(self.board)
        self.board[row][col] = "X"
        self.buttons[row][col].config(text="X", state="disabled")
        self.player_turn = not self.player_turn
        self.check_game_result()

    def check_game_result(self):
        result = evaluate(self.board)
        if result == 10:
            self.show_winner("AI")
        elif result == -10:
            self.show_winner("Human")
        elif not is_moves_left(self.board):
            self.show_draw()

    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.root.quit()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.root.quit()

    def quit_(self):
            op = messagebox.askyesno("Confirm", "Do you really want to Quit?", parent=self.root)
            if op == True:
                self.root.destroy()
                from tictactoeHome import HomeGUI
                root = Tk()
                obj = HomeGUI(root)
                root.mainloop()

def main():
    root = Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
