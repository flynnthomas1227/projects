#This is a program that solves for the roots of any quadratic equation
#"ax^2+bx+c=0" when given the coefficients a, b, and c

        #-Written by Thomas Flynn

def linear_solver(a,b):
#this function returns the solution to the equation
# ax+b=0, under the assumption that a is non-zero
    return(-b/a)

def constant_solver(a):
#this considers a = 0
#if a is 0, it returns true;else it returns false
    return(a == 0)

def quadratic_solver(a,b,c):
#this function takes a,b,c as inputs and gives two outputs for the
#plus and minus in the quadratic formula
    
#how to compute 2 values
    
    soln_one = (-b + (b**2-4*a*c)**(1/2))/(2*a)
    soln_two = (-b - (b**2-4*a*c)**(1/2))/(2*a)

#the first "if" should be to test if the soln is real, then the following
#code arranges the solutions returned in the correct order
    if b**2 - 4 * a * c>=0:
        if soln_one>soln_two:
            return([soln_two,soln_one])
        else:
            return([soln_one,soln_two])
    else:
        if soln_one.imag > soln_two.imag:
            return([soln_two,soln_one])
        else:
            return([soln_one,soln_two])
    


def polynomial_solver(a,b,c):
#this function is the main solver function
#which calls one of several functions depending on the values of a,b,and c
    
    if a != 0:
        solns = quadratic_solver(a,b,c)
        print('There are two solutions x = {:.4f} and x = {:.4f}.' \
              .format(solns[0],solns[1]))
    elif b != 0:
        soln = linear_solver(b,c)
        print('There is one solution: x = {:.4f}.'.format(soln))
    else:
        p = constant_solver(c)
        if p is True:
            print('Every complex number is a solution')
        else:
            print('There is no solution')
    

