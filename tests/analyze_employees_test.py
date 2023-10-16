import re
import analyze_employees

def test_top3(capsys):
    output = r'(?=.*[top|best])(?=.*Grace)(?=.*Alice)(?=.*Frank)'
    analyze_employees.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def test_longest(capsys):
    output = r'(?=.*longest)(?=.*Alice)(?=.*Frank)(?=.*Bryan)'
    analyze_employees.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def test_deptbreakdown(capsys):
    outputs = [
        r'sales',
        r'(?=.*[total|num])(?=.*3)',
        r'(?=.*salary)(?=.*72500)',
        r'(?=.*years)(?=.*7)',
        r'marketing',
        r'(?=.*[total|num])(?=.*2)',
        r'(?=.*salary)(?=.*67500)',
        r'(?=.*years)(?=.*6.5)',
        r'it',
        r'(?=.*[total|num])(?=.*1)',
        r'(?=.*salary)(?=.*70000)',
        r'(?=.*years)(?=.*8)',
        r'engineering',
        r'(?=.*[total|num])(?=.*1)',
        r'(?=.*salary)(?=.*65000)',
        r'(?=.*years)(?=.*8)',
        r'product development',
        r'(?=.*[total|num])(?=.*1)',
        r'(?=.*salary)(?=.*99000)',
        r'(?=.*years)(?=.*10)',
        r'executive office',
        r'(?=.*[total|num])(?=.*1)',
        r'(?=.*salary)(?=.*550000)',
        r'(?=.*years)(?=.*3)',
    ]
    analyze_employees.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_deptdetails(capsys):
    outputs = [
        r'(?=.*[large|big])(?=.*Sales)(?=.*Marketing)(?=.*IT)',
        r'(?=.*[cost|expens])(?=.*Executive Office)(?=.*Sales)(?=.*Marketing)',
    ]
    analyze_employees.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)