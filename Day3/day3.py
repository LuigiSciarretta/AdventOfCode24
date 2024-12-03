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


def capture_valid_instruction(input: str) -> int:
    multiply_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    all_patterns = multiply_pattern.findall(input)

    if all_patterns:
        solution = sum(map(lambda x: int(x[0]) * int(x[1]), all_patterns))
        return solution
    else:
        print("Problem with regex")


def capture_valid_instruction_with_statment(input: str) -> int:
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    do_match = [match.start() for match in re.finditer(do_pattern, input)]
    dont_match = [match.start() for match in re.finditer(dont_pattern, input)]

    enable_multiply = True  
    total_sum = 0
    last_position = 0  

    do_list = [(start_pos, 'do') for start_pos in do_match]
    dont_list = [(start_pos, 'dont') for start_pos in dont_match]
    do_dont_list = sorted(do_list + dont_list)
    
    for start_pos, pattern_type in do_dont_list:
        segment = input[last_position:start_pos]
        if enable_multiply:
            total_sum += capture_valid_instruction(segment)
        last_position = start_pos
        if pattern_type == 'do':
            enable_multiply = True
        elif pattern_type == 'dont':
            enable_multiply = False
    
    final_segment = input[last_position:]
    if enable_multiply:
        total_sum += capture_valid_instruction(final_segment)

    return total_sum
    

def main():  
    input = read_input('input')
    print(f"Ths solution of first puzzle is {capture_valid_instruction(input)}")
    print(f"Ths solution of second puzzle is {capture_valid_instruction_with_statment(input)}")

if __name__ == '__main__':
    main()