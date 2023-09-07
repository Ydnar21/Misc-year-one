def split(lst):
    (evens, odd) = ([], [])
    is_even = True
    for elt in lst:
        if is_even:
            evens.append(elt)

    return([], [])

def merge(sorted_lst1, sorted_lst2):
#helper function
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    #Divide lists into sublist
    (lst1, lst2)= split(lst)
    #Conquer recursively sort each list (lst1 and lst2)
    sorted_evens= merge_sort(lst1)
    sorted_odd = merge_sort(lst2)
    #Combine sorted lists
    sorted_lst = merge_sort(sorted_evens, sorted_odd)
    return sorted_lst




lst = [5 ,7 ,1,3,4,8,6,2]
sorted_lst