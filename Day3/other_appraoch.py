
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



# def capture_valid_instruction_with_statment_first_approach(input: str) -> int:
#     import re
#     do_pattern = re.compile(r'do\(\)')
#     dont_pattern = re.compile(r"don't\(\)")

#     do_match = [(match.start(), match.end()) for match in re.finditer(do_pattern, input)]
#     dont_match = [(match.start(), match.end()) for match in re.finditer(dont_pattern, input)]
#     # print('do match', do_match)
#     # print('dont match', dont_match)

#     # invalid_index =[]
#     # for dont_start, dont_end in dont_match:
#     #     for do_start, do_end in do_match:
#     #         if do_start > dont_end:
#     #             invalid_index.append((int(dont_start), int(do_end)))
#     #             break
#     # print('invalid_index', invalid_index)
#     invalid_index =[]
#     for dont_start, dont_end in dont_match:
#         for do_start, do_end in do_match:
#             if do_start > dont_start:
#                 invalid_index.append((int(dont_start), int(do_end)))
#                 break
#     print('invalid_index', invalid_index)

#     multiply_pattern = re.compile(r'mul\((\d+),(\d+)\)')
#     #all_patterns = multiply_pattern.finditer(input)

#     final_input = ''
#     start = 0
#     multiply_match = [(int(match.start()), int(match.end())) for match in re.finditer(multiply_pattern, input)]
#     #print('multiply_match', multiply_match) 
#     for invalid_index_start, invalid_index_end in invalid_index:
#         #valid_incremental_input = input[:invalid_index_start] + input[invalid_index_end:]
#         final_input+=input[start:invalid_index_start] #final_input+=input[start:invalid_index_start]
#         start = invalid_index_end
#     #manage last part 
#     final_input += input[start:]
#     #print('final_input',final_input)
#     sol2 = capture_valid_instruction(final_input)
#     return sol2


def capture_valid_instruction_with_statment_first_approach(input: str) -> int:
    import re
    
    # Identificazione pattern "do()" e "don't()"
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    do_match = [(match.start(), match.end()) for match in re.finditer(do_pattern, input)]
    dont_match = [(match.start(), match.end()) for match in re.finditer(dont_pattern, input)]
    
    # Creazione lista di intervalli non validi
    invalid_index = []
    for dont_start, dont_end in dont_match:
        for do_start, do_end in do_match:
            if do_start > dont_start:  # Trova il primo `do` successivo al `don't`
                invalid_index.append((dont_start, do_end))
                break
    
    # Unione degli intervalli per evitare sovrapposizioni
    merged_invalid_index = []
    for start, end in sorted(invalid_index):
        if not merged_invalid_index or merged_invalid_index[-1][1] < start:
            merged_invalid_index.append((start, end))
        else:
            merged_invalid_index[-1] = (merged_invalid_index[-1][0], max(merged_invalid_index[-1][1], end))
    
    # Creazione input valido escludendo gli intervalli non validi
    final_input = ''
    start = 0
    for invalid_start, invalid_end in merged_invalid_index:
        final_input += input[start:invalid_start]
        start = invalid_end
    final_input += input[start:]  # Aggiunge il segmento rimanente
    
    # Calcolo della soluzione usando il testo valido
    sol2 = capture_valid_instruction(final_input)
    return sol2

    

def main():  
    input = read_input('input')
    print(f"Ths solution of first puzzle is {capture_valid_instruction(input)}")
    print(f"Ths solution of second puzzle is {capture_valid_instruction_with_statment(input)}")
    print(f"Ths solution of second puzzle is {capture_valid_instruction_with_statment_first_approach(input)}")

if __name__ == '__main__':
    main()