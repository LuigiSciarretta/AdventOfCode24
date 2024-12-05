import os


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
    matrix = list(map(lambda x: list(x) , content.splitlines()))
    return matrix 


def count_xmas_occurrence(data: list[list]):
    possible_directions = [
    (1, 1),  
    (-1, -1),
    (1, -1), 
    (-1, 1), 
    (0, 1), 
    (0, -1),
    (1, 0),  
    (-1, 0), 
    ]
    number_of_occurence = 0
    target_word = 'XMAS' 

    for i in range(len(data)): 
        for j in range(len(data[i])): 
            for di, dj in possible_directions:
                if check_valid(i,j, di, dj, target_word, data):
                    number_of_occurence+=1
    return number_of_occurence


def check_valid(i: int, j: int, di: int, dj: int, word: str, matrix: list) -> bool:
    for n in range(len(word)):  
        new_i = i + di * n 
        new_j = j + dj * n  
        
        if not (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[i])):
            return False  
        if matrix[new_i][new_j] != word[n]:
            return False  

    return True  


def check_x_mas_occurrence(matrix: list[list]):
    number_of_occurence = 0
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            if matrix[i][j] == 'A':
                if not(i <= 0 or j <= 0 or i >= len(matrix)-1 or j >= len(matrix[0])-1): #giusto
                
                #if not(i-1 <= 0 or j-1 <= 0 or i+1>len(data) or j+1 >= len(data[i])): #mia cambiare meglio
                    diag_dx = matrix[i-1][j-1] + matrix[i+1][j+1]
                    diag_sx = matrix[i-1][j+1] + matrix[i+1][j-1]
                    
                    if (diag_dx == "MS"  or diag_dx == "SM") and (diag_sx == "MS"  or diag_sx == "SM"):
                        number_of_occurence+=1
    return number_of_occurence






def main():  
    input = read_input('input')
    matrix = manage_input(input)

    print(f"Ths solution of first puzzle is {count_xmas_occurrence(matrix)}")
    print(f"Ths solution of second puzzle is {check_x_mas_occurrence(matrix)}")

if __name__ == '__main__':
    main()