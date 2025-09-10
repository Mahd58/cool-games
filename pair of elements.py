# Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
t=(10,20,30,40,50,60,70)
look_up={}
target=int(input("Enter the sum:"))
for i,num in enumerate(t):
    print(look_up)
    if target-num in look_up:
        print(target-num)
    look_up[num]=i