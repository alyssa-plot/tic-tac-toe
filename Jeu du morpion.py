#Pour y jouer, vous devez selectionner la colonne horizontale (1, 2 ou 3) ainsi que son emplacement (1, 2 ou 3)
#les commentaires sont là pour m'y retrouver et comprendre 

import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def joueur_hasard(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def player_win(self, player):
        win = None

        n = len(self.board)

        #On vérifie les rows 
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        #On vérifie les columns cette fois
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        #Diagonal pour le morpion
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.joueur_hasard() == 1 else 'O'
        while True:
            print(f"Au tour du joueur {player}")

            self.show_board()

            #Le texte affiché quand le joueur joue
            row, col = list(
                map(int, input("Entrez le chiffre du row et de sa column :").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            #S'il y a quelqu'un qui gagne
            if self.player_win(player):
                print(f"Joueur {player} a gagné!")
                break

            #Si égalité:
            if self.is_board_filled():
                print("Egalité!")
                break

            #Chacun son tour pour jouer
            player = self.swap_player_turn(player)

        #Finalité du morpion
        print()
        self.show_board()


#Lancer la partie
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
