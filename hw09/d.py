def build_dictionary(file_name):
    """
    This builds the dictionary that includes the key month, date, and year.
    :param file_name: this is the birthday2000.txt that has a list of oh so many birthdays
    :return:the dictionary
    """
    dic={}

    with open(file_name) as f:
        for line in f:
            info = line.strip().split()
            for info[1] not in dic:
                dic[info[1]]=[info[0]]
            else:
                dic[info[1].append(info[0]])]
    return dic



print(build_dictionary("L"))