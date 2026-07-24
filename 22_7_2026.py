text = "Python"
print(text[0])
print(text[-1])


text= "Programming is life      "

print(text[0:6])
print(text[2:6])
print(text[4:6])
print(text[6:6])
print(text[3:6])

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())

text2 = "I like Java"
new_text = text2.replace("Java", "Python")
print(new_text)

words = ["Python", 'Data', 'Science']

text = ' '.join(words)

print(text)

## Without exception
num =10
# print(num/0)


try:
    print(num/0)
except:
    print("cannot divide by zero")


try:
    number = int(input('Enter a Number \n'))
    print("Division: ", number/0)
except ValueError:
    print("value error, Integer needed")
except ZeroDivisionError:
    print('Division Error')
    
    
try:
    num = int(input('enter a number \n'))
except:
    print('Error')
else:
    print('Valid Input')
finally:
    print("Program Closed")