import re
import validateNewPw

def test_goodpw(capsys, monkeypatch):
    inputs = 'AbcdefgH!jk1'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[good|valid|ok]', captured.out, re.IGNORECASE)

def test_badpw_alpha(capsys, monkeypatch):
    inputs = iter(['password', 'AbcdefgH!jk1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[bad|invalid]', captured.out, re.IGNORECASE)

def test_badpw_short(capsys, monkeypatch):
    inputs = iter(['ab!C3', 'AbcdefgH!jk1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[bad|invalid]', captured.out, re.IGNORECASE)

def test_badpw_upperlower(capsys, monkeypatch):
    inputs = iter(['TeStPaSsWoRd', 'AbcdefgH!jk1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[bad|invalid]', captured.out, re.IGNORECASE)

def test_badpw_lowerspecial(capsys, monkeypatch):
    inputs = iter(['password!@!', 'AbcdefgH!jk1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[bad|invalid]', captured.out, re.IGNORECASE)

def test_badpw_lowernum(capsys, monkeypatch):
    inputs = iter(['password1234', 'AbcdefgH!jk1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    validateNewPw.main()
    captured = capsys.readouterr()
    assert re.search(r'[bad|invalid]', captured.out, re.IGNORECASE)
