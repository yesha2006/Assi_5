numbers=[1,2,3,4,5,6,7,8,9,10]

first_five = numbers[0:5]
print(f"Extracted first five elements are {first_five}")

#method 1
#first_five.reverse()
#print(f"Reversing extracted elements are {first_five}")

#method 2
reversed_numbers = first_five[::-1]
print(f"Reversed numbers are {reversed_numbers}")
