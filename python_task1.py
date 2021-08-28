import random
num =random.randrange(1000,10000)
copy1=num
n=int(input("guess the 4digit number:"))
points =20
nu4=int(num%10)
nu3=int((num/10)%10)
nu2=int((num/100)%10)
nu1=int((num/1000)%10)

#function for working of program
def checkdigitmatch(c,points,n,num,t):
    while (n != num):
        t += 1#number of tries variable
        c = 0#counter variable
        n4 = int(n % 10)
        n3 = int((n / 10) % 10)
        n2 = int((n / 100) % 10)
        n1 = int((n / 1000) % 10)
        if (nu1 == n1):
            c += 1
            print(nu1, "1st digit is correct")
        if (nu2 == n2):
            c += 1
            print(nu2, "2nd digit is correct")
        if (nu3 == n3):
            c += 1
            print(nu3, " 3rd digit is correct")
        if (nu4 == n4):
            c += 1
            print(nu4, "4th digit is correct")

        if (c < 4) and (c != 0):
            print("not right number you got", c, "digits correct")
            points -= 2
            n = int(input("enter the next guess number:"))

        if (c == 0):
            print("all digits are wrong:")
            n = int(input("enter the next guess number"))
            points -= 2
        if(n==num):
            return c,points,n,num,t

#end  result function
def result(t1,points1):
        points1 += 5
        print("you won the game")
        print("your score:", points1)
        print("tries:", t1)
#condition for master mind game code
if(n==num):
    print("you guessed the number correctly")
else:
    t=0
    c=0
    c1,points1,n1,num1,t1= checkdigitmatch(c,points,n,num,t)

    if(n1==num1):
            result(t1,points1)
