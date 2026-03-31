def validate_headers(headers):
    expected = ["batch_id", "timestamp"] + [f"reading{i}" for i in range(1, 11)]
    return headers == expected

def validate_not_empty(data):
    return len(data) > 0

def validate_row_length(row):
    return len(row) == 12