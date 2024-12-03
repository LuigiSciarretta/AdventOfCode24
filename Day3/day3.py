import os
import re

def read_input(file_name:str) -> str:
    currenct_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(currenct_dir)
    for file in files:
        try:
            if file.startswith(file_name) and file.endswith('txt'):
                with open(os.path.join(currenct_dir, file), 'r') as input:
                    content = input.read()
        except Exception as e:
            print(f"Errore in the reading input: {e}")
    return content


def capture_valid_istruction(input: str) -> int:
    import re
    multiply_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    all_patterns = multiply_pattern.findall(input)

    if all_patterns:
        solution = sum(map(lambda x: int(x[0]) * int(x[1]), all_patterns))
        return solution
    else:
        print("Problem with regex")



def main():  
    input = read_input('input')
    solution1 = capture_valid_istruction(input)
    print(f"Ths solution of first puzzle is {solution1}")


if __name__ == '__main__':
    main()