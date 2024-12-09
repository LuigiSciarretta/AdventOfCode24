import os
from itertools import cycle

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
    return [list(riga) for riga in input.split('\n')]

def find_police_position(matrice: list[list]):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == '^':
                pos = (i,j)
                return i, j
            

def go_straight(i, j, direzioni_cicliche, direzione_corrente, cambia_direzione: bool):
    # direzioni = [(-1, 0), (0, 1), (1, 0) ,(-1, 0)]
    #parto dall'elemento zero e qunado il flag diventa false allora prendo l'elemento successivo

    if cambia_direzione is False:
        dx, dy = direzione_corrente
    else:
        dx, dy = next(direzioni_cicliche)
    
    new_pos_i = i + dx
    new_pos_j = j + dy
    return new_pos_i, new_pos_j, (dx, dy)




def my_sol(matrice, i_start, j_start):
    n = len(matrice)
    m = len(matrice[0])
    max_step = n * m
    steps = 0
    i, j = i_start, j_start
    count_pos = 0
    visited = set()  # Set per tracciare le posizioni visitate
    direzioni = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Direzioni: su, destra, giù, sinistra
    direzioni_cicliche = cycle(direzioni)
    direzione_corrente = next(direzioni_cicliche)  # Prima direzione: su
    cambia_direzione = False

    # Aggiungi la posizione iniziale
    visited.add((i, j))
    
    while steps < max_step and 0 <= i < n and 0 <= j < m:
        steps+=1
        new_pos_i, new_pos_j, direzione_corrente = go_straight(i, j, direzioni_cicliche, direzione_corrente, cambia_direzione)

        # Controlla se la nuova posizione è valida
        if 0 <= new_pos_i < n and 0 <= new_pos_j < m:
            if matrice[new_pos_i][new_pos_j] == '#':  # Ostacolo trovato
                cambia_direzione = True  # Cambia direzione
            else:
                # Se la posizione non è un ostacolo e non è già stata visitata, aggiorna la posizione
                if (new_pos_i, new_pos_j) not in visited:
                    visited.add((new_pos_i, new_pos_j))
                    i, j = new_pos_i, new_pos_j
                    count_pos += 1  # Incrementa il contatore delle posizioni visitate
                    cambia_direzione = False
        else:
            # Se il guardiano esce dall'area mappata
            break

    return visited, count_pos + 1  # Includi la posizione iniziale nel conteggio



def my_sol_(matrice, i_start, j_start):
    n = len(matrice)
    m = len(matrice[0])
    max_step = n * m  
    steps = 0
    i, j = i_start, j_start
    visited = set()  
    direzioni = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    direzioni_cicliche = cycle(direzioni)
    direzione_corrente = next(direzioni_cicliche) 
    cambia_direzione = False

    visited.add((i, j))  

    while steps < max_step:
        steps += 1
        new_pos_i, new_pos_j, nuova_direzione = go_straight(i, j, direzioni_cicliche, direzione_corrente, cambia_direzione)

        if not (0 <= new_pos_i < n and 0 <= new_pos_j < m) or matrice[new_pos_i][new_pos_j] == '#':
            cambia_direzione = True
            direzione_corrente = nuova_direzione  
        else:
            cambia_direzione = False
            i, j = new_pos_i, new_pos_j 
            visited.add((i, j))

        if not (0 <= i < n and 0 <= j < m):
            break

    return len(visited)


def main():
    input = read_input('input')
    matrice = manage_input(input)
    start_x, start_y = find_police_position(matrice)
    sol_1 = my_sol_(matrice, start_x, start_y)

    print(sol_1)


if __name__ == '__main__':
    main()




