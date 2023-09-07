from merge_sort import merge_sort
import random
from quick_sort import quick_sort
import time
"""
Author:Randy Dickersbach
File: bumper_sort.py

"""

MAX_NUM=300
"""
Global Variable
"""
def bumper_sort(data,highest_num=MAX_NUM):
    """


    :param data: The list of data that the user wants to sort
    :param highest_num: the max value of "k" is 300
    :return: the sorted list as result
    """
    hist=[random.randrange(0,1) for i in range(highest_num+1)]
    for v in range(len(data)):
        curr_value= data[v]
        hist[curr_value]+=1
    result=[]
    for i in range(len(hist)):
        current= hist[i]
        for num in range(current):
            result.append(i)
    return result







def main():
    """
    This prints out all the sorting times to see which one is the fastest.
    This also prints out the original list and sorted list for each sorting method
    """
    data = [2,5,3,0,2,3,0,3]
    new_list = [random.randrange(0, 301) for i in range(100000)]
    print("Small list, unsorted: ", data)
    print("Small list, bump-sorted: ", bumper_sort(data))
    print("Large list, unsorted: ", new_list)
    print("Large list, bump-sorted: ", bumper_sort(new_list))
    print("")

    print("Sorting a randomized list of 100000 elements to get a better view")
    merge_start = time.process_time()
    merge_sort(new_list)
    merge_end = time.process_time()
    merge_time = merge_end - merge_start
    print("Merge_sort time: ", merge_time,"seconds")
    quick_start = time.process_time()
    quick_sort(new_list)
    quick_end = time.process_time()
    quick_time = quick_end - quick_start
    print("Quick_sort time: ", quick_time,"seconds" )
    bump_start = time.process_time()
    bumper_sort(new_list)
    bump_end = time.process_time()
    bump_time = bump_end - bump_start
    print("Bumper_sort time: ",bump_time,  "seconds")
    sort_start = time.process_time()
    sorted(new_list)
    sort_end = time.process_time()
    sort_time = sort_end - sort_start
    print("Sorted time: ", sort_time)
    print("")
    huge_list = [random.randrange(0, 301) for i in range(1000000)]
    print("Sorting a randomized list of 1000000 elements")
    merge_start = time.process_time()
    merge_sort(huge_list)
    merge_end = time.process_time()
    merge_time= merge_end-merge_start
    print("Merge_sort time: ", merge_time, "seconds")
    quick_start = time.process_time()
    quick_sort(huge_list)
    quick_end = time.process_time()
    quick_time= quick_end-quick_start
    print("Quick_sort time: ", quick_time, "seconds")
    bump_start = time.process_time()
    bumper_sort(huge_list)
    bump_end = time.process_time()
    bump_time=bump_end-bump_start
    print("Bumper_sort time: ", bump_time, "seconds")
    sort_start = time.process_time()
    sorted(huge_list)
    sort_end= time.process_time()
    sort_time = sort_end - sort_start
    print("Sorted time: ", sort_time)

main()

