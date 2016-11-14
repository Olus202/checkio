def checkio(array):
    
    if len(array) == 0:
        return 0
        
    sum = 0
    last = array[-1]
    
    for i in range(len(array)):
        if i % 2 == 0:
            sum += array[i]
    return sum * last
