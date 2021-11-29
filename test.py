num_list = [2, 4, 5, 6, 7]
sumNum = 0
def list_sum(num_list):
    for i in num_list:
        sumNum = sumNum + num_list[i]
    print(sumNum)
    
list_sum()