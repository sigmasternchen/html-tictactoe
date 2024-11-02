import copy

FREE = 0
DRAW = 0
NOT_DETERMINED = -1

WIN = 1
LOSS = -1

PLAYER1 = 1
PLAYER2 = 2


class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + str(self.y)

    def __repr__(self):
        return str(self)


class Board:
    field = [
        [FREE, FREE, FREE],
        [FREE, FREE, FREE],
        [FREE, FREE, FREE]
    ]
    current = PLAYER1

    def moves(self):
        moves = []
        for y in range(3):
            for x in range(3):
                if self.field[y][x] == FREE:
                    moves.append(Move(x, y))

        return moves

    def apply(self, move):
        board = Board()
        board.field = copy.deepcopy(self.field)
        board.field[move.y][move.x] = self.current
        board.current = PLAYER2 if self.current == PLAYER1 else PLAYER1
        return board

    def winner(self):
        for y in range(3):
            player = self.field[y][0]
            won = True
            if player != FREE:
                for x in range(3):
                    if self.field[y][x] != player:
                        won = False
                        break
                if won:
                    return player

        for x in range(3):
            player = self.field[0][x]
            won = True
            if player != FREE:
                for y in range(3):
                    if self.field[y][x] != player:
                        won = False
                        break
                if won:
                    return player

        player = self.field[0][0]
        won = True
        if player != FREE:
            for i in range(3):
                if self.field[i][i] != player:
                    won = False
                    break
            if won:
                return player

        player = self.field[2][0]
        won = True
        if player != FREE:
            for i in range(3):
                if self.field[2 - i][i] != player:
                    won = False
                    break
            if won:
                return player

        for y in range(3):
            for x in range(3):
                if self.field[y][x] == FREE:
                    return NOT_DETERMINED

        return DRAW


    def get_id(self):
        id = 0
        for y in range(3):
            for x in range(3):
                id += self.field[y][x] * int(pow(3, (y * 3 + x)))
        if id == 0:
            return ""
        else:
            return hex(id)[2:]


    def visualize(self):
        for y in range(3):
            for x in range(3):
                print(self.field[y][x], end=' ')
            print("")
