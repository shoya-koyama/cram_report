s = input()

count = 0

for i in range(len(s)-1):
    count += 1
    if count == 1:
        print("Yes")
    elif int(s[i]) > int(s[i+1]): 
        print("Yes")
    else:
        print("No")

# def like_number(x):
#     # Convert the number to string to check each digit
#     s = str(x)
    
#     # If it's a single-digit number, it's a 321-like number
#     if len(s) == 1:
#         return "Yes"
    
#     # Check each digit with its next digit
#     for i in range(len(s) - 1):
#         if int(s[i]) <= int(s[i + 1]):
#             return "No"
    
#     # If the loop completes without returning "No", then it's a 321-like number
#     return "Yes"

# # Test the function
# test_numbers = [321, 4321, 123, 9, 4312]
# results = [like_number(x) for x in test_numbers]
# results


x = int(input().strip())
s = str(x)

if len(s) == 1:
    print("Yes")
else:
    like = True
    for i in range(len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            like = False
            break

    if like:
        print("Yes")
    else:
        print("No")

def find_nth_321_like_number(n):
    count = 0
    num = 0
    
    while True:
        s = str(num)
        if len(s) == 1 or all(int(s[i]) > int(s[i+1]) for i in range(len(s) - 1)):
            count += 1
            if count == n:
                return num
        num += 1

