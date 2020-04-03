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

#---------------------Assignment-2(3)---- division func

n=int(input("Enter the value of n : "))
def newfact(n):
    if n>1:
        return n* newfact(n-1)
    else:
        return 1
j=newfact(n)

x=float(input("Enter float value : "))
result=float(x*n)
finalResult=float(result/j)
print(finalResult)
result=eval(x*n/j)
print(result)
print("Facorial : ",j)







