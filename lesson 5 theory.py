Primes=[2,3,5,7,11,13]
Rainbow=['Red','Orange','Yellow','Green','Blue','Indigo','Violet']
print(Primes[3] ==2)
print(len(Primes) == 6)
print(len(Primes))

Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
print(Rainbow[3])
Rainbow[0] = '--red--'
Rainbow[3] = 'Green'
print('Print the rainbow')
for colours in range(len(Rainbow)):
    print(Rainbow[colours])

thislist=["apple", "banana", "cherry"]
print(thislist[-1])

thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist=["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
