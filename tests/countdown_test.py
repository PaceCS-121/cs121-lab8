import re
import countdown
import importlib
import time

def test_import():
    assert 'time' in importlib.sys.modules

def test_userinput_num(capsys, monkeypatch):
    inputs = '2'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    countdown.main()
    captured = capsys.readouterr()
    assert re.search(r'2\s1', captured.out)

def test_userinput_nan(capsys, monkeypatch):
    inputs = iter(['two', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    countdown.main()
    captured = capsys.readouterr()
    assert re.search(r'.*', captured.out)

def test_timing(capsys, monkeypatch):
    inputs = '2'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    starttime = time.time()
    countdown.main()
    endtime = time.time()
    exectime = endtime - starttime
    assert 2 <= exectime <= 5