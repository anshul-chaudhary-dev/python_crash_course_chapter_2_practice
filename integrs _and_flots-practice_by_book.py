#Itegers =you can add (+),subtract(-),multiply(*),divide(/) intiger in pyhton
2+3
3-2
2*3
21/3
#In a terminal sessions, python simply returns the result of the opresation . 
#Python uses two multiplications symbols to represent exponenets.
3**2
3 ** 3
10**6
#Pythobn supprtd the order of oprations too so you can use multiple oprations in one expressions.
#you can also use parentheses to modify the order of oprations so pyhton can evaluate your expressions in the order you specify.
# for example:
2+3*4
(2+3)*4
#The spacing in these exampkes has no effects on how python evalutes in the expressions; it simply hels you more quickly spot the opration that have priority when you'r reading throuh the code.



#Floats = Pthon calls any number with a decimaal point a float . this term is used in most programming language, and it refers to the fect taht a decimal point can appear at any positon in a number.
#Every programming language most be carefully designed to properly manage decimal numbers so numbers behave appropriately, no mtter where the decimal point appears.
#For the most part, you can use floats without worrying about how they behav. Simply enter the number you want to use, and Python will most likely do whta you expect:
0.1 + 0.1
0.2 +0.2
2*0.1
2*0.2
#However, be aware that you can sometimes get an arbitrary number of decimal places in your answer:
0.2+0.1
"the answer is = 0.30000000000004"
3 * 0.1
"the answer is also = 0.3000000000000004"
#This happen in all language and is of little consern. Python tries to find a wy to represent the redult as precisely as possible, wihch is sometimes difficult given how computer have to represnt numbers internslly.
#just ignore the extra deceimal places for now; you'll learn way to deal with the extrs places when you need to in the projects in the part II.



#Integers and Floats
#When you devide any two numbers, even they are integrs that result in a hole number, you'll always get a float:
4/2
# If you mix an integer and a float in any other operations, you'll get a float as well
1+2.0
2*3.0
3.0**2
#Python defalt to afloat in any operation that uses a float, even if the output is hole number.


#Underscores in numbers
#When you're writing long numbers you can group digits useing underscores to make large number more readabled.
universe_age  = 14_000_000_000

#When you print a number that was defind using underscors, python print only the digits.
print(universe_age)
#the answer is 14000000000
#Python ignors the underscors when storing these kind of values.
#Even if you don't group the digits inthrees, the value will still be unaffected. 
#To python ,100 is the same as 1_000 which is the same as 10_00.
#this feature work for both integers and floats.

