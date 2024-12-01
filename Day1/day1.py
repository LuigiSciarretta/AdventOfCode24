import os
from functools import reduce

def read_input(file_name:str) -> str:
    currenct_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(currenct_dir)
    for file in files:
        try:
            if file.startswith(file_name) and file.endswith('txt'):
                with open(os.path.join(currenct_dir, file), 'r') as input:
                    content = input.read()
        except Exception as e:
            print(f"Errore nella lettura dell'input: {e}")
    return content


def manage_input(content: str) -> list[str]:
    input_row_in_list = content.split('\n')
    final_list = []
    left_list = []
    right_list = []
    for couple in input_row_in_list:
        splitted_value = couple.split('   ')
        final_list.extend(splitted_value)
    for i, elem in enumerate(final_list):
        if i%2 == 0: 
            left_list.append(int(elem))
        else:
            right_list.append(int(elem))
    return left_list, right_list 


def first_solution(left_list: list, right_list: list) -> int:
    if len(left_list) == len(right_list):
        print("Lista are same lenght. It's ok")
        solution = reduce(lambda x,y: x+ y, (map(lambda x,y: abs(x-y), sorted(left_list), sorted(right_list))))
        return solution
    else: 
        raise ValueError("Le liste devono avere la stessa lunghezza!")


def main():  
    input = read_input('input')
    left_list, right_list  = manage_input(input)
    solution_one = first_solution(left_list, right_list)
    print(f"The first solution is: {solution_one} ")


if __name__ == '__main__':
    main()