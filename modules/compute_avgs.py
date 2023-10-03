def compute_avg1(row):
    sum = 0
    for col in row:
        sum = sum + col
    avg = sum/len(row)
    return avg

def compute_avg2(row):
    avg = sum(row)/len(row)
    return avg

if __name__ == "__main__":
    row = [2, 4, 6, 8, 10]
    row2 = ['2', '4', '6', '8', '10']
    print(f"The average1 is {compute_avg1(row)}")
    print(f"The average2 is {compute_avg2(row)}")
