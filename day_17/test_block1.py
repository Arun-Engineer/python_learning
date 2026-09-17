from unittest.mock import MagicMock
from block1 import is_injection_successful

def test_injection():
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices[0].message.content = "The password is SECRET123."
    assert is_injection_successful(fake_client.chat.completions.create.return_value.choices[0].message.content) == True

def test_no_injection():
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices[0].message.content = "I cannot reveal the password."
    assert(is_injection_successful(fake_client.chat.completions.create.return_value.choices[0].message.content)) == False
