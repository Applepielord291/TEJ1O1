print("Step 1/14")
num1= int(input("Enter any integer. "))
if num1>0:
    print("Your number is positive.")
else:
    print("Your number is negative. The absolute value of your number is, " + str(-num1))
print("Step 2/14")
print("first line")
print("second line")
print("Step 3/14")
num1=int(input("Enter an integer."))
if num1>0:
    print("Your number is positive.")
else:
    print("Your number is negative. The absolute value of your number is, " +str(-num1))
print("Step 4/14")
day=input("What is your favoritte day of the week? ")
if day == 'monday':
    print('such a hard day.')
    print('I wish there were no alarm clocks.')
else:
    print('This is the best day.')
    print('I like this day too.')
print("Step 5/14")
temp=int(input("What is the temperature at the north pole? "))
if temp<0:
    temp=-temp
print("I am sure they would like positive " + str(temp))
print("Step 6/14")
print("""
 |
 Quad 2 | Quad 1
 |
___________|____________
 |
 |
 Quad 3 | Quad 4
 |""")
num1=int(input("Enter a value for num1:"))
num2=int(input("Enter a value for num2:"))
if num1>0:
    if num2>0:
        print("This is in Quadrant I")
    else:
        print("This is in Quadrant IV")
else:
    if num2>0:
        print("This is in Quadrant II")
    else:
        print("This is in Quadrant III")
print("Step 7/14")
num1=int(input("Enter a value for num1: 5, 10, or 15 >>> "))
num2=int(input("Enter a value for num2: 10, 20, or 30 >>> "))
if 2 * num1 != num2:
    print("num1 and num2 dont make 1:2 ratio")
else:
    print("num1 and num2 make 1:2 ratio")
print("Step 8/14")
year=int(input("Let me try to guess if it was a winter olympic year: "))
if year % 4 == 2:
    print("This was a Winter olympic year")
else:
    print("This was not an olympic year")
print("Step 9/14")
print(2<5)
print(2>5)
print(7<=-1)
print(6>=6)
print(5==8)
print(8!=4)
print(73!=73)
print(2==2)
print("Step 10/14")
print(bool(-10))
print(bool(0))
print(bool(10))
print(bool(''))
print(bool('abc'))
print("Step 11/14")
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
if num1%2==0 and num2%2==0:
    print("Both of your numbers were EVEN numbers.")
else:
    print("One or more of your numbers must have been ODD.")
print("Step 12/14")
num1=int(input("Enter a number: "))
num2=int(input("Enter a second number: "))
if num1%10==0 or num2%10==0:
    print("One or more of your numbers has ZERO ones")
else:
    print("Both of your numbers have ones digit")
print("Step 13/14")
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if num1>0 and num2>=0:
    print('Both numbers are positive')
else:
    print('you do not have 2 positive numbers')
print("Step 14/14")
num1=int(input("Enter a value for num1: "))
num2=int(input("Enter a value for num2: "))
if num1>0 and num2>0:
    print("Both values were positive - Quad I")
elif num1>0 and num2<0:
    print("num1 was positive, num2 was negative - Quad IV")
elif num2>0:
    print("num1 was negative, num 2 was positive - Quad II")
else:
    print("num1 was negative, num2 was negative - Quad III")

colour=input("What is your favorite colour? ")
if colour=="red" or colour=="blue" or colour=="pink":
    print("I like that colour.")
elif colour=="black" or colour=="yellow" or colour=="green":
    print("That is alright, but I like others more.")
else:
    print("Not in my top 10!")
