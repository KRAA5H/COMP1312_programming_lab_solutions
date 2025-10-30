# Complete the implementation for flatten_ragged_list
def flatten_ragged_list(ragged_list: list): 
    temp = []

    for i in ragged_list:
        for x in i:
            temp.append(x)

    return temp

def access_element(ragged_list: list, i: int , j: int): 
    if ragged_list == None:
        return (3, None)
    elif i >= len(ragged_list):
        return (1, None)

    
    try:
        return (0, ragged_list[i][j])
    except:
        return (3, None)


def calculate_statistics(ragged_list: list):        
    return (len(flatten_ragged_list(ragged_list)), sum(flatten_ragged_list(ragged_list))/len(flatten_ragged_list(ragged_list)), max(flatten_ragged_list(ragged_list)), sum(flatten_ragged_list(ragged_list))) 





if __name__ == "__main__":
    ragged_list = [[1, 2, 6], [4, 5, 3]]
    print(calculate_statistics(ragged_list))