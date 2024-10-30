Name = input("Enter first name: ").capitalize()
Age = int(input("Enter age (years): "))
phone_number = input("Enter phone number: ")
new_phone_number = phone_number[0:12]
last_name = input("Enter last name: ").capitalize()
full_name = Name + last_name
user_info = Name +" "+last_name+" "+str(new_phone_number)+" "+ str(Age)
print(user_info)
#task 2
word = input("Enter a word: ")
if word == word[::-1]:
    print("True")
else:
    print("False")













