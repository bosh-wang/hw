import re

def get_current_coverage(filename):
    with open(filename, 'r') as file:
        content = file.read()

    match = re.search(r'All files\s*\|\s*([\d.]+)', content)
    if match:
        return float(match.group(1))
    else:
        raise ValueError("")

def get_previous_coverage(filename):
    try:
        with open(filename, 'r') as file:
            return float(file.read().strip())
    except FileNotFoundError:
        return 0.0

def save_coverage(filename, coverage):
    with open(filename, 'w') as file:
        file.write(str(coverage))

def main():
    current_coverage_file = 'output.txt'
    previous_coverage_file = 'previous_coverage.txt'
    
    current_coverage = get_current_coverage(current_coverage_file)
    previous_coverage = get_previous_coverage(previous_coverage_file)
    
    print(f"current coverage: {current_coverage}%")
    print(f"former coverage: {previous_coverage}%")

    if current_coverage >= previous_coverage:
        print("higher")
        save_coverage(previous_coverage_file, current_coverage)
        return True
    else:
        print("lower")
        return False

if __name__ == "__main__":
    main()
