fruits=['apple','strawberry','banana','watermelon']
#loop through list: prints each element in list,tuples,dictionary,set,strings etc
for x in fruits:
    print(x)
print("\n")

#looping through string: prints each letter in string
print("Print each letter from a string")
for y in "banana":
    print(y)
print("\n")

#break statement: Exit the loop when x is "banana"
print("Exit the from fruit list at banana")
for x in fruits:
    print(x)
    if x =='banana':
        break
print("\n")

#continue statement:With the continue statement we can stop the current iteration of the loop
print("Stop at banana and continue onwards")
for x in fruits:
    if x=='banana':
        continue
        print(x)
print("\n")

#range function
print("print range 0 to 9")
for x in range(10):
    print(x)


print("\n")
#range using start parameter
print("print range starts at 2")
 x in range(2,12):
    print(x)

print("\n")

#range with specified sequence addition number 2 is start, 12 is end and sequence is 3
for x in range(2,12,3):
    print(x)

print("\n")

#Else in loop
