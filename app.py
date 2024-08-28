class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print('Welcome to Tic-Tac-Toe!')
        while (not self.winner or self.tie == False):
            Game.print_board(self)
            Game.print_message(self)
            Game.get_move(self)
            Game.check_winner(self)
            Game.check_tie(self)
            Game.switch_turn(self)
        print(f'The winner is {self.winner}, congraulations!')

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if(self.tie == True):
            print('Tie game!')
        elif(self.winner):
            print(f'{self.winner} wins the game!')
        else:
            print(f"it's player {self.turn}'s turn!")
    
    def get_move(self):
        while True:
            self.move = input(f"Enter your move: ").lower()
            if(self.move in self.board):
                break
            else:
                print('Invalid input; try again!')
    
    def check_winner(self):
        pass

    def check_tie(self):
        if(None in self.board and not self.winner):
            self.tie=True

    def switch_turn(self):
        pass

game_instance = Game()
game_instance.play_game()