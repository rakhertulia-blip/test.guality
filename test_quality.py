from quality import classify_score, normalize_status, apply_result, summarize


# Задание 1. Тестирование баллов
def test_score():
    assert classify_score(-1) is None, "Вход -1"
    assert classify_score(0) == "fail", "Вход 0"
    assert classify_score(59) == "fail", "Вход 59"
    assert classify_score(60) == "pass", "Вход 60"
    assert classify_score(61) == "pass", "Вход 61"
    assert classify_score(100) == "pass", "Вход 100"
    assert classify_score(101) is None, "Вход 101"


# Задание 2. Тестирование статусов
def test_status():
    assert normalize_status("pass") == "pass", "Статус pass"
    assert normalize_status(" FAIL ") == "fail", "Статус с пробелами"
    assert normalize_status(" Pending ") == "pending", "Статус Pending"
    assert normalize_status("") is None, "Пустая строка"
    assert normalize_status(" ") is None, "Строка из пробелов"
    assert normalize_status("done") is None, "Недопустимый статус"


# Задание 3. Тестирование изменения записи
def test_apply():
    record = {"id": 7, "title": "Вход EKEB", "status": "pending"}
    before = record.copy()

    assert apply_result(record, " PASS ") is True
    assert record["status"] == "pass"
    assert record["id"] == before["id"]
    assert record["title"] == before["title"]

    record = {"id": 7, "title": "Вход EKEB", "status": "pending"}
    before = record.copy()

    assert apply_result(record, "done") is False
    assert record == before

    record = {"id": 7, "title": "Вход EKEB", "status": "pass"}
    before = record.copy()

    assert apply_result(record, "pass") is True
    assert record["status"] == "pass"
    assert record["id"] == before["id"]
    assert record["title"] == before["title"]


# Задание 4. Тестирование сводки
def test_summary():
    records = [{"id": 1, "title": "Вход EKEB", "status": "pass"},{"id": 4, "title": "Профиль", "status": "fail"},{"id": 7, "title": "Расписание", "status": "pass"},{"id": 9, "title": "Выход", "status": "pending"}]

    before = []
    for record in records:
        before.append(record.copy())

    expected = {"total": 4,"pending": 1,"pass": 2,"fail": 1}

    assert summarize(records) == expected
    assert records == before

    assert summarize([]) == {"total": 0,"pending": 0,"pass": 0,"fail": 0}

    one_record = [{"id": 1, "title": "Профиль", "status": "fail"}]

    assert summarize(one_record) == {"total": 1,"pending": 0,"pass": 0,"fail": 1}


def main():
    test_score()
    print("PASS test_score")

    test_status()
    print("PASS test_status")

    test_apply()
    print("PASS test_apply")

    test_summary()
    print("PASS test_summary")

    print("Итого: 4/4 теста пройдены")


if __name__ == "__main__":
    main()