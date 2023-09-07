def main():
    lst=open(input("File Name?").split()).readline()
    biggie_sort(lst)

def biggie_sort(lst):
    for i in len(lst):
        curr_max = 0
        find_maximum_num(lst)
        swap()


    lst.close()
#Find Maximum
def find_maximum_from(lst):
    for j in len(lst)-1:
        if list[j] > list[curr_max]:
            curr_max = j
            print(curr_max)

#Swap Maximum to the Right
def swap():
    temp = list[i]
    list[i] = list[curr_max]
    list[curr_max] = temp

main()