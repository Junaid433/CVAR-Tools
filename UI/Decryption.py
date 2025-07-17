from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QFileDialog,
    QTextEdit, QPushButton, QHBoxLayout, QSizePolicy
)
from PySide6.QtCore import Qt
from Algorithm.Decryptor import Decrypt_CVAR
from Algorithm.Exceptions import DecryptionError

class CVARDecryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧩 PUBG Mobile CVAR Decryptor")
        self.setMinimumSize(650, 500)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)

        input_group = QGroupBox("Encrypted Hex String(s) Input")
        input_layout = QVBoxLayout()
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Paste +CVars=hex lines here, multiple lines supported...")
        self.input_field.setAcceptRichText(False)
        input_layout.addWidget(self.input_field)
        input_group.setLayout(input_layout)
        input_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        output_group = QGroupBox("Decrypted CVAR Text Output")
        output_layout = QVBoxLayout()
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(False)
        self.output_field.setAcceptRichText(False)
        self.output_field.setPlaceholderText("Decrypted CVAR text will appear here...")
        output_layout.addWidget(self.output_field)
        output_group.setLayout(output_layout)
        output_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.decrypt_btn = QPushButton("Decrypt")
        self.decrypt_btn.setToolTip("Decrypt input +CVars= hex lines into plain CVAR text")
        self.decrypt_btn.setFixedWidth(140)
        self.decrypt_btn.clicked.connect(self.handle_decrypt)
        button_layout.addWidget(self.decrypt_btn)

        self.export_btn = QPushButton("Export File")
        self.export_btn.setToolTip("Export decrypted output to a text file")
        self.export_btn.setFixedWidth(140)
        self.export_btn.clicked.connect(self.export_to_txt)
        button_layout.addWidget(self.export_btn)

        button_layout.addStretch()

        main_layout.addWidget(input_group, stretch=3)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(output_group, stretch=4)

        self.setLayout(main_layout)

    def handle_decrypt(self):
        text = self.input_field.toPlainText().strip()
        lines = text.splitlines()
        decrypted_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("+CVars="):
                line = line[len("+CVars="):]
            try:
                decrypted = Decrypt_CVAR(line)
                decrypted_lines.append(decrypted)
            except DecryptionError as e:
                decrypted_lines.append(f"[Error] {str(e)}")

        self.output_field.setPlainText("\n".join(decrypted_lines))

    def export_to_txt(self):
        text = self.output_field.toPlainText()
        if not text.strip():
            return
        filename, _ = QFileDialog.getSaveFileName(self, "Export Decrypted Text", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)