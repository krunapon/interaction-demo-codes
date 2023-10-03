from functools import reduce

def compute_avg3(row):
    sum = 0
    for col in row:
        sum = sum + int(col)
    avg = sum/len(row)
    return avg    

def compute_avg4(row):
    row_ints = map(int, row)
    avg = reduce(lambda a, b: a + b, row_ints)/len(row)
    return avg

def compute_avg5(row):
    return reduce(lambda a, b: a + b, map(int, row))/len(row)

if __name__ == "__main__":
    row = ['2', '4', '6', '8', '10']
    print(f"The average3 is {compute_avg3(row)}")
    print(f"The average4 is {compute_avg4(row)}")
    print(f"The average5 is {compute_avg5(row)}")