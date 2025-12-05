
def get_matrix(number_row):
    return [map(int , (input()).split(" ")) for _ in range(number_row)]
        
def calculate_rows(matrix_list):
    return [sum(matrix_list[i]) for i in range(len(matrix_list))]


if __name__ == "__main__": 
    list = get_matrix(3)
    answer = calculate_rows(list)
    print(f'''Column sums:

Column 1: {answer[0]}

Column 2: {answer[1]}

Column 3: {answer[2]}''')