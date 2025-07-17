from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QFileDialog,
    QPushButton, QGroupBox, QHBoxLayout, QSizePolicy,
)
from PySide6.QtCore import Qt
from Algorithm.Encryptor import Encrypt_CVAR
from Algorithm.Exceptions import EncryptionError

class CVAREncryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐 PUBG Mobile CVAR Encryptor")
        self.setMinimumSize(650, 500)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)

        input_group = QGroupBox("Plain CVAR Text Input")
        input_layout = QVBoxLayout()
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Paste plain CVAR text here, multiple lines supported...")
        self.input_field.setAcceptRichText(False)
        input_layout.addWidget(self.input_field)
        input_group.setLayout(input_layout)
        input_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        output_group = QGroupBox("Encrypted CVAR Output")
        output_layout = QVBoxLayout()
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setAcceptRichText(False)
        self.output_field.setPlaceholderText("Encrypted +CVars= hex will appear here...")
        output_layout.addWidget(self.output_field)
        output_group.setLayout(output_layout)
        output_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.encrypt_btn = QPushButton("Encrypt")
        self.encrypt_btn.setToolTip("Encrypt input CVAR text into PUBG +CVars= hex lines")
        self.encrypt_btn.setFixedWidth(140)
        self.encrypt_btn.clicked.connect(self.handle_encrypt)
        button_layout.addWidget(self.encrypt_btn)

        self.export_btn = QPushButton("Export File")
        self.export_btn.setToolTip("Export encrypted output to a text file")
        self.export_btn.setFixedWidth(140)
        self.export_btn.clicked.connect(self.export_to_txt)
        button_layout.addWidget(self.export_btn)

        button_layout.addStretch()

        main_layout.addWidget(input_group, stretch=3)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(output_group, stretch=4)

        self.setLayout(main_layout)

    def handle_encrypt(self):
        text = self.input_field.toPlainText().strip()
        if not text:
            self.output_field.setPlainText("[Error] Input is empty.")
            return

        lines = text.splitlines()
        encrypted_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                encrypted = Encrypt_CVAR(line)
                encrypted_lines.append("+CVars=" + encrypted.upper())
            except EncryptionError as e:
                encrypted_lines.append(f"[Error] {str(e)}")

        self.output_field.setPlainText("\n".join(encrypted_lines))

    def export_to_txt(self):
        text = self.output_field.toPlainText()
        if not text.strip():
            return
        filename, _ = QFileDialog.getSaveFileName(self, "Export Encrypted Text", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)