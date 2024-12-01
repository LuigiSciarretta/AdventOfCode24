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
            print(f"Errore in the reading input: {e}")
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


def second_solution_with_lib(left_list: list, right_list: list) -> int:
    """ This is the 2 solution with Counter and python approach like map, reduce and filter"""
    from collections import Counter
    
    counter_right_list: dict[int, int] = Counter(right_list)
    right_list_counter = {x: counter_right_list[x] for x in left_list if x in counter_right_list}
    product_list = list(map(lambda x: x * right_list_counter.get(x, 0), left_list))
    solution = reduce(lambda x, y: x+y, product_list, 0)
    return solution

def second_solution(left_list: list, right_list:list) -> int:
    """ This is the 2 solution from scratch"""
    counter_right_list = {}
    for elem in right_list:
        if elem in counter_right_list:
            counter_right_list[elem]+=1
        else:
            counter_right_list[elem] = 1
    
    product_list = []
    for left_value in left_list:
        if left_value in counter_right_list:
            product_list.append(left_value*counter_right_list[left_value])
    
    solution = 0
    for product_vale in product_list:
        solution += product_vale
    return solution 

    


def main():  
    input = read_input('input')
    left_list, right_list  = manage_input(input)
    solution_one = first_solution(left_list, right_list)
    solution_two = second_solution_with_lib(left_list, right_list)
    solution_two_nolib = second_solution(left_list, right_list)
    print(f"The first solution is: {solution_one} ")
    print(f"The second solution is: {solution_two}")
    print(f"The second solution without lib is: {solution_two_nolib}")



if __name__ == '__main__':
    main()