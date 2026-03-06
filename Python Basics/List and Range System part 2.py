from random import randint

list = []
for i in range(10):
  list.append(randint(1,50))

print(list)

num = randint(1,50)

if num in list:
    print("Number",num,"found in the list!")
else:
    print("Number",num,"not found in the list.")
