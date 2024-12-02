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


def manage_input(content: str) -> list[list[int]]:
    rows = content.strip().split('\n')  
    final_report = [[int(value) for value in row.split(' ')] for row in rows]
    return final_report




def count_safe_report(final_report: list[list[int]]):
    count_safe_repo = 0

    for report in final_report:
        increasing = False
        first_distance = report[1] - report[0]
        valid_report = True
        if first_distance > 0:
            increasing = True
        else:
            increasing = False 
        for i in range(len(report) -1):
            distance = report[i+1] - report[i] 
            # increasing case
            if increasing is True:
                if distance < 0:
                    valid_report = False
                    break
                else:
                    admissible_distance = check_distance(distance)
                    if admissible_distance is False:
                        valid_report = False

            else: #decreasing case
                if distance > 0:
                    valid_report = False
                    break
                else:
                    admissible_distance = check_distance(distance)
                    if admissible_distance is False:
                        valid_report = False
                        break

        if valid_report == True:
            count_safe_repo+=1

    return count_safe_repo
            

def check_distance(distance: int) -> bool:
    abs_distance = abs(distance)
    if abs_distance >= 1 and abs_distance <=3: 
        return True
    else:
        return False



def main():  
    input = read_input('input')
    final_report = manage_input(input)
    count_safe_repo = count_safe_report(final_report)
    print(f"Number of safe report: {count_safe_repo}")



if __name__ == '__main__':
    main()