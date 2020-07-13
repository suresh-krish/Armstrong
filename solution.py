# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        num1 = str(num)
        n = len(num1)
        sum = 0
        for i in range(0,n):
                sum = sum + num1[i] ** n

        if str(sum) == num1:
                return True
        else:
                return False

