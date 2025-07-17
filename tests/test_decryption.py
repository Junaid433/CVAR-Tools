import pytest
from unittest.mock import patch, mock_open

from Algorithm.Decryptor import Decrypt_CVAR
from Algorithm.Exceptions import DecryptionError
from UI.Decryption import CVARDecryptor
from Algorithm.Encryptor import Encrypt_CVAR


def test_decrypt_valid_line():
    encrypted = Encrypt_CVAR("r.UserQualitySetting=0")
    decrypted = Decrypt_CVAR(encrypted)
    assert "r.UserQualitySetting" in decrypted


def test_decrypt_raises_error_on_invalid():
    with pytest.raises(DecryptionError):
        Decrypt_CVAR("ZZZZ")


def test_decrypt_handle_decrypt(qapp, qtbot):
    widget = CVARDecryptor()
    qtbot.addWidget(widget)

    encrypted1 = Encrypt_CVAR("r.UserQualitySetting=0")
    encrypted2 = Encrypt_CVAR("r.UserShadowSwitch=1")
    input_text = f"+CVars={encrypted1}\n+CVars={encrypted2}"

    widget.input_field.setPlainText(input_text)
    widget.handle_decrypt()

    output = widget.output_field.toPlainText()
    assert "r.UserQualitySetting" in output
    assert "r.UserShadowSwitch" in output


@patch("builtins.open", new_callable=mock_open)
@patch("PySide6.QtWidgets.QFileDialog.getSaveFileName")
def test_decrypt_export_to_txt(mock_get_save, mock_file, qapp, qtbot):
    mock_get_save.return_value = ("test_decrypt_output.txt", "Text Files (*.txt)")

    widget = CVARDecryptor()
    qtbot.addWidget(widget)

    widget.output_field.setPlainText("r.UserQualitySetting=0\nr.UserShadowSwitch=1")
    widget.export_to_txt()

    mock_file.assert_called_once_with("test_decrypt_output.txt", "w", encoding="utf-8")
    handle = mock_file()
    handle.write.assert_called_once_with("r.UserQualitySetting=0\nr.UserShadowSwitch=1")
