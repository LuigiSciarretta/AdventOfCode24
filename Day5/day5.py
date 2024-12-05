import os
from collections import defaultdict


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


def manage_input(input: str) -> list[tuple] | list[list]:
    rules = [tuple(map(lambda x: int(x), riga.split('|'))) for riga in input.split('\n\n')[0].strip().split('\n')]
    updates = [list(map(lambda x: int(x), riga.split(','))) for riga in input.split('\n\n')[1].strip().split('\n')]
    dict_order = defaultdict(list)
    for first, second in rules:
        #print(first,second)
        dict_order[first].append(second) #il dict contiente tutte
    return updates ,dict_order

#devo costruire il dizionario
# dict_order: elemento : [tutti i suoi successori]

def first_solo(updates: list[list], dict_order: dict[int, list]): #, updates:str
    central_value = 0
    for update in updates:
        is_ordered = True
        for i in range(len(update)):
            for j in update[i+1:]:
                if update[i] not in dict_order or j not in dict_order[update[i]]:
                    is_ordered = False
                    break

        if is_ordered:
            central_value+= update[len(update)//2]
    return central_value




def main():
    input = read_input('input')
    updates, dict_order = manage_input(input)
    #print(dict_order.keys(), dict_order.values())
    print(f"The solution of first puzzle is: {first_solo(updates, dict_order)} ")


if __name__ == '__main__':
    main()