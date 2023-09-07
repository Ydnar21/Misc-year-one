import os
import subprocess
import socket
import csv

from pip._internal import commands


def user():
    while True:
        filename = input("Enter the file name here: ")
        cmd = "ls"
        print(cmd)
        find = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
        #print(find)
        path = subprocess.Popen("readlink -f "+ filename)
        print(path)
        print("Current Directory: ")
        print()
        #symlink(find)



def symlink(find):
    src = find
    dst = "./Desktop"
    os.symlink(src, dst)
    os.getcwd()



def main():

    user()


main()