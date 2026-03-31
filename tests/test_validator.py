from src.validator import validate_headers

def test_valid_headers():
    headers = ["batch_id", "timestamp"] + [f"reading{i}" for i in range(1, 11)]
    assert validate_headers(headers) == True


def test_invalid_headers():
    headers = ["batch", "time"]  # wrong headers
    assert validate_headers(headers) == False

def test_empty_file():
    data = []
    assert validate_not_empty(data) == False

def test_row_length_valid():
    row = ["1", "12:00"] + ["1.0"] * 10
    assert validate_row_length(row) == True

def test_row_length_invalid():
    row = ["1", "12:00"] + ["1.0"] * 5
    assert validate_row_length(row) == False
