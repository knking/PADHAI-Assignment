#-----------------------------Assignment 1(BMI)---------------------

# weight=int(input("Enter your weight in kg's : "))
# preference=input("What is your preferred unit of height? Type F for feet and M for meters : ")
#
# if preference=="f":
#     print("Enter your height in feat and inches")
#     feet=int(input("Enter feat : "))
#     inches=int(input("Now enter inches : "))
#     meters=float(feet+inches/12)*0.3048
#
# else :
#     meters=float(input("Enter your height in meters : "))
# height=meters
# BMI=weight/height**2
# print(BMI)
#
# if BMI<18.5:
#     print("UNDER WEIGHT")
# elif 18.5 <= BMI < 25 :
#     print("NORMAL")
# elif  25 <= BMI < 30 :
#     print("OERWEIGHT")
# else:
#     print("VERY OVERWEIGHT")

#--------------------Assignment-2(fatorial)-----------------

# num=int(input("Enter natural number to find factorial : "))
# j=1
# for i in range(1,num+1):
#     j=j*i
# print(j)


#--------------------Assignmen-2(fact)


# def fact(n):
#     if n >1:
#        return (n*fact(n-1))
#     else:
#         return 1
# print(fact(5))

#---------------------Assignment-2(3)---- Compute x*n/n!

#n=int(input("Enter the value of n : "))
# def newfact(n):
#     if n>1:
#         return n* newfact(n-1)
#     else:
#         return 1
#
# def compute_ratio(x,n):
#     ratio=x**n/newfact(n)
#     return ratio
# print(compute_ratio(2,3))

#-----------------Assignment -2(4)----compute x*n/n! upto n

def newfact(n):
    if n>1:
        return n* newfact(n-1)
    else:
        return 1

def compute_ratio(x,n):
    ratio=x**n/newfact(n)
    return ratio

def compute_sum(x,N):
    sum=1
    for i in range(N):
        sum+=compute_ratio(x,i+1)
    return sum
print(compute_sum(2,3))
















