def trick1(num):
    answer = ((num * 2 + 6 ) / 2 ) - num
    print("Your answer is", int(answer))

# Display
print("Math")
print("1.Pick a number less than 10")
print("2.Double the number")
print("3.Add 6 to the answer")  # ERROR: Missing period
print("4.Divide the answer by 2")
print("5.Subtract your original number from the answer\n")

num = int(input("Enter a number less than 10: "))

if num <= 10:
    trick1(num)
else:
  print("The number you entered is not less than 10. Please try again.")
