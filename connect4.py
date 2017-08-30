class Connect4:

	def setup(self):
		self.board = [[0 for j in range(7)] for i in range(8)]
		self.game_running = True
		self.current_player = 1
		self.win_combinations = [
			[(0, 0), (1, 0), (2, 0), (3, 0)],
			[(0, 0), (0, 1), (0, 2), (0, 3)],
			[(0, 0), (1, 1), (2, 2), (3, 3)]
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
		column_number = int(raw_input('Player ' + str(self.current_player) + '\'s turn. Which row?'))
		column = self.board[column_number]
		for (cell_value, row_number) in enumerate(column):
			if cell_value == 0:
				column[row_number] = self.current_player
				break

	def check_for_victory(self):
		for column in self.board:
			break

	def display_board(self):
		print self.board

Connect4().setup().run()
