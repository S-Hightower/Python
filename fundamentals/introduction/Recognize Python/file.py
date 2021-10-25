num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data type:primitive
string = 'Hello World' #data type:primitive
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #data type:composite list add value
print(person['name']) #log statement
person['name'] = 'George'#data type:composite list add value
person['eye_color'] = 'blue' #data type:composite list add value
print(fruit[2]) #log statement

if num1 > 45: #if conditional
    print("It's greater")#log statement
else: #else conditional
    print("It's lower")#log statement

if len(string) < 5:#if conditional
    print("It's a short word!")#log statement
elif len(string) > 15: #else if conditional
    print("It's a long word!")#log statement
else:#else conditional
    print("Just right!")#log statement

for x in range(5): #for loop:start
    print(x)#log statement
for x in range(2,5):#for loop:start
    print(x)#log statement
for x in range(2,10,3):#for loop:start
    print(x)#log statement
x = 0 #variable declaration
while(x < 5):# while loop:start
    print(x)#log statement
    x += 1#while loop: increment

pizza_toppings.pop()#list:composite list delete value
pizza_toppings.pop(1)#list:composite list delete value

print(person) #log statement
person.pop('eye_color')#list:composite list delete value
print(person) #log statement

for topping in pizza_toppings:#for loop:start
    if topping == 'Pepperoni':#if conditional
        continue#for loop:continue
    print('After 1st if statement') #log statement
    if topping == 'Olives':#if conditional
        break#for loop:break

def print_hello_ten_times():#function
    for num in range(10):#for loop:start
        print('Hello') #log statement

print_hello_ten_times()#function

def print_hello_x_times(x):#function
    for num in range(x):#for loop:start
        print('Hello') #log statement

print_hello_x_times(4) #function

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop:start
        print('Hello')#log statement function:return

print_hello_x_or_ten_times()#function
print_hello_x_or_ten_times(4)#function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)