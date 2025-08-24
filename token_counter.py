import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QTextEdit, QComboBox, QPushButton
)
import tiktoken  # pip install tiktoken PySide6


class TokenCounter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LLM Token Counter")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your prompt:")
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.model_label = QLabel("Choose a model:")
        layout.addWidget(self.model_label)

        self.model_combo = QComboBox()
        self.model_combo.addItems([
            "gpt-3.5-turbo",
            "gpt-4",
            "davinci"
        ])
        layout.addWidget(self.model_combo)

        self.button = QPushButton("Count tokens")
        self.button.clicked.connect(self.count_tokens)
        layout.addWidget(self.button)

        self.result_label = QLabel("Token count: 0")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def count_tokens(self):
        prompt = self.text_edit.toPlainText()
        model_name = self.model_combo.currentText()

        try:
            enc = tiktoken.encoding_for_model(model_name)
        except KeyError:
            # fallback to a default encoding
            enc = tiktoken.get_encoding("cl100k_base")

        tokens = enc.encode(prompt)
        count = len(tokens)
        self.result_label.setText(f"Token count: {count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TokenCounter()
    window.show()
    sys.exit(app.exec())
