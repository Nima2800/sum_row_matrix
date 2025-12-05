
def get_matrix(number_row):
    return [list(map(int , (input()).split(" "))) for _ in range(number_row)]
        
def calculate_rows(matrix_list):
    return [sum(matrix_list[i]) for i in range(len(matrix_list))]

def calculate_column(matrix_list):
    return [(matrix_list[0][i] + matrix_list[1][i] +matrix_list[2][i]) for i in range(len(matrix_list))]

if __name__ == "__main__": 
    my_list = get_matrix(3)
    rows = calculate_rows(my_list)
    columns = calculate_column(my_list)
    print(columns)
    print(f'''Row sums:

Row 1: {rows[0]}

Row 2: {rows[1]}

Row 3: {rows[2]}
          
Column sums:

Column 1: {columns[0]}

Column 2: {columns[1]}

Column 3: {columns[2]}''')