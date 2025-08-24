import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QComboBox
)
import tiktoken


class TokenCounter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LLM Token Counter")
        self.resize(500, 350)

        layout = QVBoxLayout()
        layout.setSpacing(12)

        # Label
        self.label = QLabel("Enter your prompt:")
        layout.addWidget(self.label)

        # Text editor
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.count_tokens)
        layout.addWidget(self.text_edit)

        # Model selector
        self.model_label = QLabel("Choose a model:")
        layout.addWidget(self.model_label)

        self.model_combo = QComboBox()
        self.model_combo.addItems([
            "gpt-3.5-turbo",
            "gpt-4",
            "davinci"
        ])
        self.model_combo.currentIndexChanged.connect(self.count_tokens)
        layout.addWidget(self.model_combo)

        # Result label
        self.result_label = QLabel("Token count: 0")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.apply_styles()
        self.count_tokens()  # initialize count

    def count_tokens(self):
        prompt = self.text_edit.toPlainText()
        model_name = self.model_combo.currentText()

        try:
            enc = tiktoken.encoding_for_model(model_name)
        except KeyError:
            enc = tiktoken.get_encoding("cl100k_base")

        tokens = enc.encode(prompt)
        count = len(tokens)
        self.result_label.setText(f"Token count: {count}")

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 6px;
            }
            QComboBox {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 4px;
            }
            QLabel {
                font-weight: bold;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TokenCounter()
    window.show()
    sys.exit(app.exec())
