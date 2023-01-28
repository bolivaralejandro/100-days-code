# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = (lower_case_string.count('t'))
r = (lower_case_string.count('r'))
u = (lower_case_string.count('u'))
e = (lower_case_string.count('e'))

true = t + r + u + e

l = (lower_case_string.count('l'))
o = (lower_case_string.count('o'))
v = (lower_case_string.count('v'))
e = (lower_case_string.count('e'))

love = l + o + v + e

love_scrore = int(str(true) + str(love))

if (love_scrore < 10) or (love_scrore > 90):
    print(f"Your score is {love_scrore}, you go together like coke and mentos.")
elif love_scrore > 40 and love_scrore < 50:
    print(f"Your score is {love_scrore}, you are alright together.")
else:
    print(f"Your score is {love_scrore}")