import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QVBoxLayout, QWidget, QLineEdit, QTextEdit,QHBoxLayout, QMessageBox

class Bank:
    def __init__(self, name: str, account_number: str, balance: float) -> None:
        self.name: str = name
        self.account_number: str = account_number
        self.__balance: float = balance
        self.__transactions: list = []
    
    def get_balance(self) -> str:
        return f"Your balance on the account '{self.account_number}' is ${self.__balance}"
    
    def credit(self, amount: float) -> str:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"${amount} is credited to the account '{self.account_number}' successfully!")
            return f"${amount} is credited to your account '{self.account_number}'"
        else:
            return "Amount can't be negative"

    def debit(self, amount: float) -> str:
        if self.__balance > amount > 0:
            self.__balance -= amount
            self.__transactions.append(f"${amount} is debited from the account {self.account_number} successfully!")
            return f"${amount} is debited from your account '{self.account_number}'"
        elif amount > self.__balance:
            return "Not enough balance" 
        elif amount < 0:
            return "Amount can't be negative"
        
    def get_transactions(self) -> str:
        transactions = ["Your last transactions are:"]
        transactions.extend(self.__transactions[-5:])
        return "\n".join(transactions)

class BankApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Account Management")
        self.setGeometry(100, 100, 500, 400)
        
        
        self.customer = Bank("CUSTOMER", "MYBANK001", 2000)
        
        self.initUI()
        
    def initUI(self) -> None:

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        self.account_label = QLabel(f"Account: {self.customer.account_number}")
        
        self.transaction_history = QTextEdit()
        self.transaction_history.setReadOnly(True)
        self.transaction_history.setPlaceholderText("Transaction history will appear here...")
        
        amount_layout = QHBoxLayout()
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        amount_layout.addWidget(QLabel("Amount:"))
        amount_layout.addWidget(self.amount_input)
        
        button_layout = QHBoxLayout()
        self.credit_btn = QPushButton("Credit")
        self.debit_btn = QPushButton("Debit")
        self.balance_btn = QPushButton("Check Balance")
        self.history_btn = QPushButton("Transaction History")
        
        button_layout.addWidget(self.credit_btn)
        button_layout.addWidget(self.debit_btn)
        button_layout.addWidget(self.balance_btn)
        button_layout.addWidget(self.history_btn)
        
        self.credit_btn.clicked.connect(self.credit_action)
        self.debit_btn.clicked.connect(self.debit_action)
        self.balance_btn.clicked.connect(self.show_balance)
        self.history_btn.clicked.connect(self.show_history)
        
        main_layout.addWidget(self.account_label)
        main_layout.addLayout(amount_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.transaction_history)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
    
    def credit_action(self) -> None:
        amount_text:float = self.amount_input.text()
        if amount_text:
            try:
                amount = float(amount_text)
                result = self.customer.credit(amount)
                self.transaction_history.append(result)
                self.amount_input.clear()
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Please enter a valid number")
        else:
            QMessageBox.warning(self, "Missing Input", "Please enter an amount")
    
    def debit_action(self) -> None:
        amount_text:float = self.amount_input.text()
        if amount_text:
            try:
                amount = float(amount_text)
                result = self.customer.debit(amount)
                self.balance_label.setText(self.customer.get_balance())
                self.transaction_history.append(result)
                self.amount_input.clear()
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Please enter a valid number")
        else:
            QMessageBox.warning(self, "Missing Input", "Please enter an amount")
    
    def show_balance(self) -> None:
        balance:str=self.customer.get_balance()
        QMessageBox.information(self, "Balance", balance)
    
    def show_history(self) -> None:
        self.transaction_history.setText(self.customer.get_transactions())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    sys.exit(app.exec())