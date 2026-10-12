from mailer import build_body


def test_body_contains_hostname():
    body = build_body("teszt-gep", "12:34:56")
    assert "teszt-gep" in body


def test_body_contains_time():
    body = build_body("teszt-gep", "12:34:56")
    assert "12:34:56" in body