# -*- coding: utf-8 -*-
"""eigencalc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k289fA05axyP1110-ygyQI9cecmJroF9
"""

import numpy as np
 
#This def is for the purpose of viewing the matrix
def display_matrix(matrix):
    
    print('|{:3}  {:3}  {:3}|'.format(matrix[1],matrix[2],matrix[3]))
    print('|{:3}  {:3}  {:3}|'.format(matrix[4],matrix[5],matrix[6]))
    print('|{:3}  {:3}  {:3}|'.format(matrix[7],matrix[8],matrix[9]))
 
#Def for preparing the characteristic equation
def chareqn(matA):
    
    #finding sum of diagonal
    sumofd = matA[0]+matA[4]+matA[8]
    print(f'sumofdiag = {sumofd}')
    
    #finding minor
    minorA = (matA[4]*matA[8])-(matA[5]*matA[7])+(matA[0]*matA[8])-(matA[6]*matA[2])+(matA[0]*matA[4])-(matA[3]*matA[1])
    print(f'minor = {minorA}')
    
    #finding determinant
    det = matA[0]*((matA[4]*matA[8])-(matA[5]*matA[7]))-matA[1]*((matA[3]*matA[8])-(matA[6]*matA[5]))+matA[2]*((matA[3]*matA[7])-(matA[4]*matA[6]))
    print(f'det = {det}')
 
    #printing the characteristic eqn as a whole
    print(f'Characteristic equation = λ³-{sumofd}λ²+{minorA}λ-{det}')
 
    #accepted the root values to 3 different variables
    root1,root2,root3 = np.roots([1,sumofd,minorA,det])
    r1 = (int(np.round(root1,0)))*-1
    r2 = (int(np.round(root2,0)))*-1
    r3 = (int(np.round(root3,0)))*-1
    print(f'λ1 = {r1}')
    print(f'λ2 = {r2}')
    print(f'λ3 = {r3}')
    return r1,r2,r3
 
#def to find eigenvector using the found eigenvalues
def eigenVector(r1,r2,r3,matA):
    #loop for taking 1 eigenvalue at a time
    for i in range(1,4):
        if i==1:    
            matr=['']
            print(f'At λ = {r1}, (A-{r1}I)X=0')
            for k in range(9):    
                if k==0 or k==4 or k==8:    
                    matr.append(matA[k]-r1)
                else:
                    matr.append(matA[k])
            mat = [str(j) for j in matr]
            display_matrix(mat)
        if i==2:
            matr=['']    
            print(f'At λ = {r2}, (A-{r2}I)X=0')
            for k in range(9):    
                if k==0 or k==4 or k==8:    
                    matr.append(matA[k]-r2)
                else:
                    matr.append(matA[k])
            mat = [str(j) for j in matr]
            display_matrix(mat)
        if i==3:
            matr=['']    
            print(f'At λ = {r3}, (A-{r3}I)X=0')
            for k in range(9):    
                if k==0 or k==4 or k==8:    
                    matr.append(matA[k]-r3)
                else:
                    matr.append(matA[k])
            mat = [str(j) for j in matr]
            display_matrix(mat)
 
#matrixok put at false for while loop to execute
matrixok = False
while matrixok==False:
    matrix = ['']
 
    #accepting 9 elements for the matrix from the user as a loop
    for i in range(1,10):
        text = f'Input element no. {i}= '
        a = str(input(text))
        matrix.append(a)
 
    #calling the display_matrix def to view the matrix    
    display_matrix(matrix)
 
    #0th element is popped out and the list is converted from str to int
    matrix.pop(0)
    matA = [int(i) for i in matrix]
 
    #accepting user confirmation of the matrix
    a = input('Is the matrix correct? (y/n)')
    if a == 'y' or a == 'Y':
        matrixok = True 
 
    #calling the chareqn def for the characteristic equation if the 
    # user satisfied with the matrix 
        r1,r2,r3 = chareqn(matA)
 
eigenVector(r1,r2,r3,matA)