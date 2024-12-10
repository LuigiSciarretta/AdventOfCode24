import os
from itertools import zip_longest


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


def sol1(input):
    input = input.strip()
    num_blocchi = map(int, list(input[::2]))
    free_space = map(int, list(input[1::2]))

    final_list = []
    for i, (blocco, free) in enumerate(zip_longest(num_blocchi, free_space, fillvalue=0)):
        final_list.extend([i]*blocco)
        final_list.extend(['.']*free)

    for i in range(len(final_list)):
        if final_list[i] == '.':
            for j in range(len(final_list)-1, i,-1):
                if final_list[j] != '.':
                    final_list[i] = final_list[j]   
                    final_list[j] = '.'
                    break
            else:
                break
                   
    terminated_int_list = list(filter(lambda x: isinstance(x, int), final_list))
    final_sum = 0
    for i, value in enumerate(terminated_int_list):
        final_sum+=(i*value)
    return final_sum


def main():
    input = read_input('input')
    print(f"The solution of first puzzle is: {sol1(input)}")


if __name__ == '__main__':
    main()