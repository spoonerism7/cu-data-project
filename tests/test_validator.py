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