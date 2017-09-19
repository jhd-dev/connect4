from numpy import rot90

class Connect4:

	game_running = False
	win_combinations = [
		[(0, 0), (1, 0), (2, 0), (3, 0)],
		[(0, 0), (0, 1), (0, 2), (0, 3)],
		[(0, 0), (1, 1), (2, 2), (3, 3)],
		[(0, 0), (-1, 1), (-2, 2), (-3, 3)]
	]

	def setup(self):
		self.board = [[0 for j in range(6)] for i in range(7)]
		self.game_running = True
		self.current_player = 2

	def run(self):
		while self.game_running:
			self.switch_player()
			self.place_piece(self.get_player_input())
			self.display_board()
			if self.check_for_victory():
				self.end_game(self.current_player)

	def switch_player(self):
		if self.current_player == 1:
			self.current_player = 2
		else:
			self.current_player = 1

	def get_player_input(self):
		return int(raw_input('Player ' + str(self.current_player) + '\'s turn. Which column? ')) - 1

	def place_piece(self, column_number):
		column = self.board[column_number]
		for (row_number, cell_value) in enumerate(column):
			if cell_value == 0:
				column[row_number] = self.current_player
				break

	def check_for_victory(self):
		for (x, column) in enumerate(self.board):
			for (y, cell_value) in enumerate(column):
				for combination in self.win_combinations:
					if self.check_winning_combination(x, y, combination):
						return True
		return False

	def check_winning_combination(self, x, y, combination):
		for coordinates in combination:
			if not (self.board[x + coordinates[0]] and self.board[x + coordinates[0]][y + coordinates[1]]):
				return False
			if not (self.board[x + coordinates[0]][y + coordinates[1]] == self.board[x][y]):
				return False
		return True

	def display_board(self):
		rotated_board = self.get_rotated_board()
		for row in rotated_board:
			print row

	def end_game(self, winner=0):
		if winner == 0:
			print 'It\'s a tie!'
		else:
			self.game_running = False
			print 'Player ' + str(winner) + ' wins!'

	def get_rotated_board(self):
		return rot90(self.board)

if __name__ == '__main__':
	connect4 = Connect4()
	connect4.setup()
	connect4.run()
