#Basic - Print all integers from 0 to 150.
for r in range(151):
    print(r)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for w in range(1001):
    if(w % 5 == 0):
        print(w)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(101):
    if(x % 10 == 0):
        #print("Coding Dojo")
        #continue
    elif(x % 5 == 0):
        #print("Coding")
        #continue
    print(x)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
finalSum = 0
for x in range(0, 500001):
    if x % 2 != 0:
        finalSum = finalSum + x
print(finalSum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for y in range(2018, 0, -4):
    print(y)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)