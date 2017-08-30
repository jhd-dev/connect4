from numpy import rot90

class Connect4:

	game_running = False

	def setup(self):
		self.board = [[0 for j in range(6)] for i in range(7)]
		self.game_running = True
		self.current_player = 2
		self.win_combinations = [
			[(0, 0), (1, 0), (2, 0), (3, 0)],
			[(0, 0), (0, 1), (0, 2), (0, 3)],
			[(0, 0), (1, 1), (2, 2), (3, 3)],
			[(0, 0), (-1, 1), (-2, 2) (-3, 3)]
		]
		return self

	def run(self):
		while self.game_running:
			self.switch_player()
			self.get_player_input()
			self.display_board()
			self.check_for_victory()

	def switch_player(self):
		if self.current_player == 1:
			self.current_player = 2
		else:
			self.current_player = 1

	def get_player_input(self):
		column_number = int(raw_input('Player ' + str(self.current_player) + '\'s turn. Which column? ')) - 1
		column = self.board[column_number]
		for (row_number, cell_value) in enumerate(column):
			if cell_value == 0:
				column[row_number] = self.current_player
				break

	def check_for_victory(self):
		for (x, column) in enumerate(self.board):
			for (y, cell_value) in enumerate(column):
				self.check_winning_space()

	def check_winning_space():
		for combination in self.win_combinations:
			for coordinates in combination:
				if not (self.board[x + coordinates[0]] and self.board[x + coordinates[0]][y + coordinates[1]]):
					break
				if not (self.board[x + coordinates[0]][y + coordinates[1]] == cell_value):
					break

	def display_board(self):
		rotated_board = rot90(self.board)
		for row in rotated_board:
			print row

Connect4().setup().run()
