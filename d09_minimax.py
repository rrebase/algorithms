# A Tic-tac-toe game using the minimax algorithm

# TODO: GUI, Alpha–beta pruning

class Tic:
    """
    Tic tac toe game class.
    """

    # all the possible winning combos
    winning_combos = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6))

    COMPUTER = 0
    HUMAN = 1

    def __init__(self):
        """
        Initialize a game, all cells are set to None.
        """
        self.game_state = {}
        for i in range(9):
            self.game_state[i] = None

    def make_move(self, cell, player):
        """
        Makes a move.
        :param cell: number from 0 to 8, marking the position on board
        :param player: Tic.COMPUTER or Tic.HUMAN
        """
        self.game_state[cell] = player

    def get_moves(self):
        """
        Get a list of moves that are not None.
        :return: list of moves
        """
        moves = []
        for cell in self.game_state.keys():
            if self.game_state[cell] is None:
                moves.append(cell)
        return moves

    def check_for_winner(self):
        """
        Check for a winner.
        :return: None is there isn't a winner in this state
                 0 if the COMPUTER has won
                 1 if the HUMAN has won
        """
        for combo in Tic.winning_combos:
            if (self.game_state[combo[0]] == self.game_state[combo[1]]
                    and self.game_state[combo[0]] == self.game_state[combo[2]]
                    and self.game_state[combo[0]] is not None):
                return self.game_state[combo[0]]
        return None

    def evaluate(self):
        """
        Evaluate the current position.
        :return: score
        """
        winner = self.check_for_winner()
        if winner == Tic.COMPUTER:
            return 100
        elif winner == Tic.HUMAN:
            return -100
        return 0

    def minimax(self, depth, maximizing_player):
        """
        Minimax algoritm.
        :param depth: amount of moves to explore
        :param maximizing_player: bool, True if is maximizing, else minizimizing
        :return: tuple (best_score, best_move)
        """
        moves = self.get_moves()
        best_move = -1
        if maximizing_player:
            best_score = float("-inf")
        else:
            best_score = float("inf")
        if depth == 0 or not moves or self.check_for_winner() is not None:
            best_score = self.evaluate()
        else:
            for move in moves:
                if maximizing_player:
                    self.make_move(move, Tic.COMPUTER)
                    currest_score = self.minimax(depth - 1, False)[0]
                    if currest_score > best_score:
                        best_score = currest_score
                        best_move = move
                    best_score -= 1
                else:
                    self.make_move(move, Tic.HUMAN)
                    currest_score = self.minimax(depth - 1, True)[0]
                    if currest_score < best_score:
                        best_score = currest_score
                        best_move = move
                self.make_move(move, None)

        return best_score, best_move

    def print_board(self):
        """
        Pretty print the current board.
        """
        for i in range(9):
            if i == 3 or i == 6 or i == 9:
                print()
            if self.game_state[i] is None:
                print("-", end="")
            else:
                print(self.game_state[i], end="")
        print("\n")


    def start_game(self):
        """
        Start the game loop.
        """
        current_player = Tic.COMPUTER
        winner = None
        print("Move by entering the appropriate cell number:\n"
              "+-+-+-+\n"
              "|0|1|2|\n"
              "+-+-+-+\n"
              "|3|4|5|\n"
              "+-+-+-+\n"
              "|6|7|8|\n"
              "+-+-+-+\n")
        while self.get_moves():

            # making a move
            if current_player == Tic.COMPUTER:
                move = self.minimax(5, True)[1]
            else:
                while True:
                    try:
                        move = int(input("Your move:\n"))
                    except Exception:
                        print("Illegal move, try again.")
                        continue
                    if move in self.get_moves():
                        break
                    else:
                        print("Illegal move, try again.")
            self.make_move(move, current_player)
            self.print_board()

            # check for a winning position
            check = self.check_for_winner()
            if check == 0:
                winner = 0
                break
            elif check == 1:
                winner = 1
                break

            # change player
            if current_player == 0:
                current_player = 1
            else:
                current_player = 0

        if winner == 0:
            print("You lost!")
        elif winner == 1:
            print("You won!")
        else:
            print("Draw!")


if __name__ == '__main__':
    tic = Tic()
    tic.start_game()
