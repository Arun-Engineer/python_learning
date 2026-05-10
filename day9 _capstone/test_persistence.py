import os
from models import Bug
from persistence import load_bugs, save_bugs

def test_save_and_load_round_trip():
    """Saving Bugs then loading them returns equivalent Bugs."""
    test_file = "test_roundtrip.json"

    # Arrange
    original = [
        Bug(id=1, title= "A", severity= 1, status= "open", team= "web"),
        Bug(id=2, title= "B", severity= 4, status= "open", team= "mobile"),
        Bug(id=3, title= "C", severity= 2, status= "closed", team= "web"),
        Bug(id=4, title= "D", severity= 5, status= "open", team= "web"),
        Bug(id=5, title= "E", severity= 3, status= "open", team= "mobile"),
    ]

    # Act
    save_bugs(original, test_file)
    loaded = load_bugs(test_file, fallback=[])

    # Assert
    assert loaded == original

    # Cleanup
    os.remove(test_file)

def test_load_missing_file_returns_fallback():
    """When file doesn't exist, fallback is returned."""

    fallback = [Bug(id=99, title="Default", severity=1, status="open", team="x")]
    result = load_bugs("nonexistent_file.json", fallback=fallback)
    assert result == fallback