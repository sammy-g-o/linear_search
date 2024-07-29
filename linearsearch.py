"""uses linear search algorithm to search for a key value between a range of values user will be prompted for"""
def linearsearch(array,key):
    """for linear search"""
    index = 0
    while True:
        if array[index] != key:
            index +=1
        else:
            return f"The key {key} was found in index {index}"
        if key not in array:
            return f"{key} not in array"
print(linearsearch(list(range(int(input("Enter 1st value of range")),int(input("Enter 2nd value of range")))),int(input("Enter key value algorithm should search for in range"))))
