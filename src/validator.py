def validate_headers(headers):
    expected = ["batch_id", "timestamp"] + [f"reading{i}" for i in range(1, 11)]
    return headers == expected

def validate_not_empty(data):
    return len(data) > 0

def validate_row_length(row):
    return len(row) == 12

def validate_unique_batch_ids(rows):
    seen = set()
    for row in rows:
        if row["batch_id"] in seen:
            return False
        seen.add(row["batch_id"])
    return True

def validate_readings(readings):
    return all(0 <= float(r) <= 9.9 for r in readings)