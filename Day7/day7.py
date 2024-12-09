import os
from itertools import product



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


def manage_input(input:str):
    return {int(riga.split(':')[0]): list(map(int, list(filter(lambda x: x.isdigit(), riga.split(':')[1].split(' '))))) for riga in input.split('\n')}



def left_to_right(number_list:list, operator_combinations, result):
    accumulator = number_list[0]

    for i in range(len(operator_combinations)):
        if operator_combinations[i] == '+':
            accumulator+=number_list[i+1]
            if accumulator > result:
                break
        elif operator_combinations[i] == '*':
            accumulator*=number_list[i+1]
            if accumulator > result:
                break
        
    if accumulator == result:
        return result
    else: 
        return None



def compute_sol(input: dict[int,list]) -> int:
    operators = ['+', '*']
    final_result = []

    for result, number_list in input.items():
        operator_combinations: list[tuple] = list(product(operators, repeat=len(number_list) - 1))
        for combination in operator_combinations:
            combination_list = list(combination)
            final_value = left_to_right(number_list, combination_list, result)
            if final_value is not None:
                final_result.append(final_value)

    return sum(final_result)

def main():
    input = read_input('input')
    final_input = manage_input(input)
    print(compute_sol(final_input))


if __name__ == '__main__':
    main()























