import Tkinter
from connect4 import Connect4

class TkinterConnect4 (Connect4):

	def setup(self):
		Connect4.setup(self)
		self.root = Tkinter.Tk()
		self.label = Tkinter.Label(self.root, text=str(self.board))
		self.label.pack()
		self.textbox = Tkinter.Text(self.root, width=2, height=1)
		self.textbox.pack()
		self.button = Tkinter.Button(self.root, text="Go", command=self.run_player_turn)
		self.button.pack()
		self.instruction = Tkinter.Label(self.root, text="")
		self.instruction.pack()
		self.current_player = 1
		self.display_board()

	def run(self):
		self.root.mainloop()

	def get_player_input(self):
		return int(self.textbox.get('1.0', Tkinter.END)) - 1

	def run_player_turn(self):
		if self.game_running:
			self.place_piece(self.get_player_input())
			self.display_board()
			if self.check_for_victory():
				self.end_game(self.current_player)
			self.switch_player()

	def display_board(self):
		self.label.config(text='\n'.join([' '.join([str(cell) for cell in row]) for row in self.get_rotated_board()]))

	def end_game(self, winner):
		self.game_running = False
		win_text = 'Player ' + str(winner) + ' wins!'
		print win_text
		self.instruction.config(text=win_text)

if __name__ == '__main__':
	connect4 = TkinterConnect4()
	connect4.setup()
	connect4.run()
