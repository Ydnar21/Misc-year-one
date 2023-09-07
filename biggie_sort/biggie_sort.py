def main():
    lst=[]
    file=open(input("Enter File Name?"))
    with open(file) as f:
        for line in f:
            lst.append(int(line))


    print("Unsorted List: ", lst)
    biggie_sort(lst)
    new_sort=lst[::-1]
    print("Sorted List: ", new_sort)
def biggie_sort(lst):
    # This value of i corresponds to how many values were sorted
    find_max_from(lst)
        # We assume that the first item of the unsorted segment is the smallest
def find_max_from(lst):
    for i in range(len(lst)):
        highest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[highest_value_index]:
                highest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        lst[i], lst[highest_value_index] = lst[highest_value_index], lst[i]





if __name__ == '__main__':
    main()