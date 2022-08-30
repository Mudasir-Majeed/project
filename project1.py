# creat an achronym using python
# a program that generats a short form of a word from agiven sentance
user_input=input("Enter a phrase ")
text= user_input.split()
a=" "
for i in text:
    a=a+str(i[0]).upper()
print(a)