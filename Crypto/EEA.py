
def ExtendedGCF(a,b):
    if a==0:
        return b,0,1
    gcd,x1,y1 = ExtendedGCF(b%a,a)
    x = y1 - (b//a) * x1
    y=x1


    return gcd,x,y
def multiplicativeInverse(g,a,b,x,y):
    if g==1:
        inverseA= (a*x) % b
        if(inverseA==1):
            return x
    else:
        return "Inverse does not exist"

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
g,x,y = ExtendedGCF(a,b)
inverse =multiplicativeInverse(g,a,b,x,y)

print("GCD (", a,",",b,") = ", g)
print("Inverse =" ,inverse)


'''
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1


# Driver Code
a = 7111111
m = 123456

# Function call
print(modInverse(a, m))

# This code is contributed by Nikita Tiwari.
'''