#psuedocode
#ask user for numbers
#creat a function
# pass numbers to the function 
# define function 
# insert value to it
# create formula of average according to BODMAS rule
# declare them as new variable for ease 
# return that variable
# print answer 
def average(num1,num2,num3):
    return (num1+num2+num3)/2
num1=float(input("write first number: "))
num2=float(input("write second number :"))
num3=float(input("write third number:"))
average_result = average(num1,num2,num3)
print("The average of 3 numbers are: " , average_result)