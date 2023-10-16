import re
import pytest
import calculator

def test_add(capsys, monkeypatch):
    inputs = iter(['1', '+', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'3', captured.out)

def test_subtract(capsys, monkeypatch):
    inputs = iter(['5', '-', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'3', captured.out)

def test_multiply(capsys, monkeypatch):
    inputs = iter(['2', '*', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'6', captured.out)

def test_divide(capsys, monkeypatch):
    inputs = iter(['6', '/', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'2', captured.out)

def test_wrongnuminput(capsys, monkeypatch):
    inputs = iter(['+', '1', '+', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'[not|wrong|invalid|try again]', captured.out, re.IGNORECASE)
    assert re.search(r'3', captured.out)

def test_wrongopinput(capsys, monkeypatch):
    inputs = iter(['1', '1', '1', '+', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'[not|wrong|invalid|try again]', captured.out, re.IGNORECASE)
    assert re.search(r'3', captured.out)

def divide0_err(monkeypatch):
    with pytest.raises(Exception) as e_info:
        inputs = iter(['1', '/', '0'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        calculator.main()
        return True

def divide0_msg(capsys, monkeypatch):
    inputs = iter(['1', '/', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert re.search(r'[0|zero]', captured.out, re.IGNORECASE)
    assert re.search(r'[not|wrong|invalid|try again]', captured.out, re.IGNORECASE)
    return True

def test_divide0(capsys, monkeypatch):
    try:
        divide0_err(monkeypatch)
        divide0_msg(capsys, monkeypatch)
    except Exception as e:
        assert re.search(r'[0|zero]', str(e), re.IGNORECASE)
