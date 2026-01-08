print("step 1/10")
sum=0
sum=sum+1
sum=sum+2
sum=sum+3
sum=sum+4
sum=sum+5
print(sum)
print("step 2/10")
print("This will perform the sum of 1 through 5")
sum=0
sum=sum+1
sum=sum+2
sum=sum+3
sum=sum+4
sum=sum+5
print("The sum is: " + str(sum))
print("step 3/10")
for test in 1,2,3,"one","two",'three':
    print(test)
print("my loop is done.")

for test in 1,2,3,"one","two",'three':
    print(test*3)
print("step 4/10")
for letters in "watermelon":
    print(letters)


for watch_this in "Print this out!":
    print(watch_this)
print("step 5/10")
for loop in range(2, 10):
    print(loop,loop*4)
print("End of this loop!")
print("step 6/10")
for numbers in range(3, 12):
    print(numbers)
print("This printed 9 values!")
print("step 7/10")
for value in range(5):
    print(value)
print("end of my loop!")

for value in range(5):
    print(value)
print("my value was 5, it counted the min=0 and max=5, so 0,1,2,3,4.")
print("step 8/10")
for num in range(-5):
    print("This wont be printed")
for num2 in range(8,6):
    print('nothing will be printed')
print("step 9/10")
answer=0
num=5
for count in range(1,num+1):
    answer+=count
print(answer)

answer=0
num=100
for count in range(1,num+1):
    answer+=count
print(answer)

answer=0
num=100
for count in range(50,num+1):
    answer+=count
print(answer)
print("step 10/10")
for step in range(15,0,-2):
    print(step)
