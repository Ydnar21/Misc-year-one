from dataclasses import dataclass
"""
Author:Randy Dickersbach
File:birthday.py
"""
@dataclass(frozen = True )
class Birthday:
    """
    The class Birthday with a key of Month, date, and year
    """
    Month: str
    date: int
    year: int

def build_dictionary(file_name):
    """
    This builds the dictionary that includes the key month, date, and year.
    :param file_name: this is the birthday2000.txt that has a list of oh so many birthdays
    :return:the dictionary
    """
    dic={}

    with open(file_name) as f:
        for line in f:
            birthday = line.split()
            birthdays=(Birthday(birthday[0],int(birthday[1]),int(birthday[2])))
            if birthdays in dic:
                dic[birthdays] += 1
            else:
                dic[birthdays] = 1
    return dic

def birthdays_atleast(dic, min_count):
    """
    This checks to see how many birthdays are ona certain date
    :param dic: THis is the dictionary
    :param min_count: Least amount of birthdays on that day
    :return: the list
    """
    list = []
    for birthday in dic:
        if dic[birthday] >= min_count:
            list.append(birthday)
    return list





def to_strings(list_birthdays):
    """
    This changes the results that we got into a string and displays like 1/1/2019 instead of JAN date=1 year=2019
    :param list_birthdays: the dictionary that has the date where the the most birthdays occur.
    :return:
    """
    changed_form=[]
    for i in range(0, len(list_birthdays)):
        date_form = " "
        month_form = list_birthdays[i]
        if month_form.Month == "JAN":
            date_form= "1/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "FEB":
            date_form= "2/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "MAR":
            date_form= "3/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "APR":
            date_form= "4/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "MAY":
            date_form= "5/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "JUN":
            date_form= "6/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "JUL":
            date_form= "7/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "AUG":
            date_form= "8/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "SEP":
            date_form= "9/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "OCT":
            date_form= "10/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "NOV":
            date_form= "11/"+str(month_form.date)+ "/"+ str(month_form.year)
        if month_form.Month == "DEC":
            date_form= "12/"+str(month_form.date)+ "/"+ str(month_form.year)

        changed_form.append(date_form)

    return changed_form

def main():
    """
    Calls all the functions
    Asks the user for the dates with 23 birthdays
    :return: The birthdays in both forms wanted.
    """
    dic = build_dictionary("birthday2000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(dic, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)

main()