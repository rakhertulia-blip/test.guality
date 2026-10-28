# Задание 1
def classify_score(score):
    if score < 0 or score > 100:
        return None
    if score >= 60:
        return "pass"
    return "fail"

# Задание 2
def normalize_status(text):
    text = text.strip().lower()

    if text == "pending" or text == "pass" or text == "fail":
        return text
    return None
# Задание 3
def apply_result(record,status):
    new_status = normalize_status(status)
    if new_status is None:
        return False
    record["status"] = new_status
    return True

#  Задание 4
def summarize(records):
    result = {"total": len(records),"pending": 0,"pass": 0,"fail": 0}

    for record in records:
        result[record["status"]] += 1

    return result 