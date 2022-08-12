class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n, m):
        self.pole = []
        for _ in range(n):
            self.pole.append(['x'] * n)


