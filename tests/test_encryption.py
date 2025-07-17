import pytest
from unittest.mock import patch, mock_open

from Algorithm.Encryptor import Encrypt_CVAR
from Algorithm.Exceptions import EncryptionError
from UI.Encryption import CVAREncryptor


def test_encrypt_valid_line():
    plain_text = "r.UserQualitySetting=0"
    encrypted = Encrypt_CVAR(plain_text)
    assert isinstance(encrypted, str)
    assert len(encrypted) % 2 == 0
    assert all(c in "0123456789abcdefABCDEF" for c in encrypted)


def test_encrypt_raises_error_on_invalid():
    with pytest.raises(EncryptionError):
        Encrypt_CVAR("")  # Empty input should raise


def test_encrypt_handle_encrypt(qtbot):
    widget = CVAREncryptor()
    qtbot.addWidget(widget)

    widget.input_field.setPlainText("r.UserQualitySetting=0\nr.UserShadowSwitch=1")
    widget.handle_encrypt()

    output = widget.output_field.toPlainText()
    lines = output.strip().splitlines()
    assert all(line.startswith("+CVars=") for line in lines)
    assert "r.UserQualitySetting" not in output


@patch("builtins.open", new_callable=mock_open)
@patch("PySide6.QtWidgets.QFileDialog.getSaveFileName")
def test_encrypt_export_to_txt(mock_get_save, mock_file, qtbot):
    mock_get_save.return_value = ("test_encrypt_output.txt", "Text Files (*.txt)")

    widget = CVAREncryptor()
    qtbot.addWidget(widget)

    widget.output_field.setPlainText("+CVars=ABCDEF1234")
    widget.export_to_txt()

    mock_file.assert_called_once_with("test_encrypt_output.txt", "w", encoding="utf-8")
    handle = mock_file()
    handle.write.assert_called_once_with("+CVars=ABCDEF1234")
