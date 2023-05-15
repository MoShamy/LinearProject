# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:22:28 2023

@author: ahmed hassanin 
This is a code that utilizes Cramer's rule to solve a linear system'
"""
import numpy as np
import sympy as sp
import math
import sys

#taking the number n from user
n=abs (int (input ('please enter the number of variables n ' )))
x=[]
constarray=[]
print (f'The number of equations and variables is {n}')

#recording the values for the variables from the user
for i in range(n):
        print (f'enter values for equation {i+1}')
        for j in range(n):
            x.append(float (input (f'enter x{j+1} ')))
        constarray.append(float(input('= ')))

#forming two matricies with the coefficients and constant values in numpy 
matrix = np.array(x)
constarray=np.array(constarray)
matrix = matrix.reshape(n, n)

#calculating the detereminante of the coefficient matrix
new_matrix=np.array (matrix)
determinant = math.floor(np.linalg.det(matrix))
#determinant = sp.nsimplify(determinant)


#checking if the coefficient matrix is invertible before applying Cramer's rule  
if determinant == 0:
    print("Error: The coefficient matrix is not invertible")
    sys.exit(1)

#calculating the values of the variables according to Cramer's rule
for k in range (n):
    new_matrix[:, k]=constarray
    #print (np.linalg.det(new_matrix))
    #print (determinant)
    result= sp.nsimplify(np.linalg.det(new_matrix))/determinant
    print (f'value of x{k+1} = {result} ')
    new_matrix=np.array (matrix)




    