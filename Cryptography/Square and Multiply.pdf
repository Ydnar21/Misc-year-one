def smalgo(b, e, mod):
    # base case
    if (e == 0):
        return 1
    if (e == 1):
        return b % mod

    num = smalgo(b, int(e / 2),mod)
    num = (num * num) % mod

    if e % 2 == 0:
        return num

    else:
        return ((b % mod) * num) % mod
def main():

    b = int(input("Enter base value: "))
    e = int(input("Enter exponent value: "))
    mod = int(input("Enter mod num: "))
    print(smalgo(b,e,mod))


if __name__ == '__main__':
    main()