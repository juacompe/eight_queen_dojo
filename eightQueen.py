from unittest import TestCase

def getPeacefulQueens(queen_count, queens=[]):
    if queen_count == len(queens):
        return queens

    for queen in possibleQueensInRow(queen_count, queens):
        solution = getPeacefulQueens(queen_count, queens + [queen])
        if solution:
            return solution
    
def possibleQueensInRow(queen_count, queens):
    for column in range(queen_count):
        queen = Queen(len(queens), column)
        if not queen.fightWithOthers(queens):
            yield queen

def printQueens(queens):
    for queen in queens:
        print ' ' * queen.column + '*'

class Queen():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def fightWith(self, another_queen):
        return (self.row == another_queen.row or 
                self.column == another_queen.column or 
                self.row - self.column == another_queen.row - another_queen.column or
                self.row + self.column == another_queen.row + another_queen.column) 

    def fightWithOthers(self, queens):
        for existing_queen in queens:
            if self.fightWith(existing_queen):
                return True

    def __repr__(self):
        return "%d.%d"%(self.row, self.column) 

class EightQueenTest (TestCase):

    queens = getPeacefulQueens(8)

    def test_two_queens_should_not_fight(self):
        self.assertFalse(self.queens[0].fightWith(self.queens[1]))

    def test_all_the_queens_should_be_inside_board(self):
        for queen in self.queens:
            self.assertTrue(queen.column < 8, "queen's colunm is %d" % queen.column)

    def test_all_the_queens_should_not_fight_reverse_diagnally(self):
        self.assertNotEqual(self.queens[3].column + self.queens[3].row,
                    self.queens[4].column + self.queens[4].row)

    def test_the_queen_index4_should_not_fight_the_queen_index0(self):
        self.assertFalse(self.queens[4].fightWith(self.queens[0]))

    def test_the_queen_index7_should_not_fight_the_queen_index0(self):
        self.assertFalse(self.queens[7].fightWith(self.queens[0]))

