print("do not give space when typing input(caution)")
i = input("enter the first number : ")
j = input("enter the second number : ")
c = input("choose +, -, / or * : ")

if c == '+':
    print(int(i)+int(j))

elif c == '-':
    print(int(i)-int(j))

elif c == '/':
    print(int(i)/int(j))

elif c == '*':
    print(int(i)*int(j))

else:
    print('enter a valid operation')
