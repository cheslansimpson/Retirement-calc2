import sys

# Usage: python html_regression_check.py <filename.html>

def check_html_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Check first non-empty line is <!DOCTYPE html>
    for i, line in enumerate(lines):
        if line.strip() == '':
            continue
        if line.strip().lower() == '<!doctype html>':
            print('PASS: File starts with <!DOCTYPE html>')
        else:
            print(f'FAIL: First non-empty line is not <!DOCTYPE html> (found: {line.strip()})')
            return False
        break
    else:
        print('FAIL: File is empty or only whitespace')
        return False
    # Check for stray code before <!DOCTYPE html>
    for j in range(i):
        if lines[j].strip() != '':
            print(f'FAIL: Stray code or text before <!DOCTYPE html>: {lines[j].strip()}')
            return False
    print('PASS: No code or text before <!DOCTYPE html>')
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python html_regression_check.py <filename.html>')
        sys.exit(1)
    result = check_html_file(sys.argv[1])
    sys.exit(0 if result else 2)
