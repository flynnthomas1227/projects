#This program takes a line, square or n-dimensional cube with side
#length 1 unit, and calculates the expected distance between 2
#randomly generated points.

#This imports built in functions from random in python.
import random

#This creates a prompt for the user to analyze what dimension they want.
n = input('What dimension do you want to analyze?...')

#This takes the response from the user and turns it into
#into a number to be used later.
i = eval(n)

#This creates a prompt for the user to enter how many iterations
#to perform randomly generating points to control the accuracy
#of the calculated value
j = input('How many experimental trails do you wish to run to estimate the value?...')

#This takes the response from the user and turns it into
#into a number to be used later.
k= eval(j)

#This is an if statement that will run the rest of the program if the
#dimension input is valid(positive integer) and returns "invalid dimension
#input" otherwise.
if type(i) == int and i >= 0:

    #This is an if statement that will run the rest of the program if the
    #iteration amount input is valid(positive integer) and returns "invalid
    #trial number input" otherwise.
    if type(k) == int  and k > 0:

        #This uses the distance formula with the given dimension to
        #calculate the distance between 2 randomly generated points
        #however many times the user specified in the beginning. Then
        #it uses the average of all the distances as an expected distance value.
        my_list = list(range(i))
        my_list_of_lists = [[(abs(random.uniform(0,1)-random.uniform(0,1))**2) for x in my_list] for y in range(k)]
        my_distances = [(sum(z))**(1/2) for z in my_list_of_lists]
        expected_distance = (sum(my_distances)/k)
    
       
        print('The expected value of the distance is {:.4f}.'.format(expected_distance))
    

    else:
        print('invalid trail number input')
else:
    print('invalid dimension input')



    
    
