import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox
import random
from functools import partial

class Game:
    def __init__(self,name):
        self.name = name 
        self.score = 0
        self.choices = ["Rock 🪨", "Paper 📰", "Scissors ✂️"]

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)

        result = ""
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock 🪨" and computer_choice == "Scissors ✂️") or \
             (player_choice == "Paper 📰" and computer_choice == "Rock 🪨") or \
             (player_choice == "Scissors ✂️" and computer_choice == "Paper 📰"):
            result = "You win! 🎉"
            self.score += 1
        else:
            result = "Computer wins! 💻"
        
        return f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}"

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game")
        self.setGeometry(100,100,300,200)
            
        self.game = Game("Name")
        self.initUI()

    def initUI(self) -> None:
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.score_label = QLabel(f"Your score is: {self.game.score}")

        button_layout = QHBoxLayout()
        self.rock_button = QPushButton("Rock 🪨")
        self.paper_button = QPushButton("Paper 📰")
        self.scissors_button = QPushButton("Scissors ✂️")

        button_layout.addWidget(self.rock_button)
        button_layout.addWidget(self.paper_button)
        button_layout.addWidget(self.scissors_button)

        self.rock_button.clicked.connect(partial(self.play_game, "Rock 🪨"))
        self.paper_button.clicked.connect(partial(self.play_game, "Paper 📰"))
        self.scissors_button.clicked.connect(partial(self.play_game, "Scissors ✂️"))

        main_layout.addWidget(self.score_label)
        main_layout.addLayout(button_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def play_game(self, player_choice):
        result_text = self.game.play(player_choice)
        self.score_label.setText(f"Your score is: {self.game.score}")
        QMessageBox.information(self, "Result", result_text)

if __name__ == "__main__":
    game = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(game.exec())