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

def validate_file(data):
    # Check not empty
    if not validate_not_empty(data):
        return False, "File is empty"
    
    headers = data[0]
    rows = data[1:]

    # check headers
    if not validate_headers(headers):
        return False, "Invalid headers"
    
    #check row in rows:
    for row in rows:
        if not validate_row_length(row):
            return False, "Invalid row length"
    
    # check unique batch IDs
    if not validate_unique_batch_ids(dict_rows):
        return False, "duplicate batch IDs found"
    
    # check readings
    for row in rows:
        readings = row[2:]
        if not validate_readings(readings):
            return False, "Invalid reading values"
        
    return True, "File is valid"