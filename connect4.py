board = [[0 for j in range(7)] for i in range(8)]
game_running = True
current_player = 1
win_combinations = [
	[(0, 0), (1, 0), (2, 0), (3, 0)],
	[(0, 0), (0, 1), (0, 2), (0, 3)],
	[(0, 0), (1, 1), (2, 2), (3, 3)]
]

while game_running:
	switch_player()
	get_player_input()
	display_board()
	check_for_victory()

def switch_player():
	if current_player == 1:
		current_player = 2
	else:
		current_player = 1

def get_player_input():
	column_number = raw_input('Player ' + current_player + '\'s turn. Which row?')
	column = board[column_number]
	for (cell, i) in enumerate(column):
		if cell == 0:
			column[i] = current_player
			break

def check_for_victory():
	for column in board:
		break

def display_board():
	print board
