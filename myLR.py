'''from numpy import *

def linreg(inputs,targets):

	inputs = concatenate((inputs,-ones((shape(inputs)[0],1))),axis=1)
	beta = dot(dot(linalg.inv(dot(transpose(inputs),inputs)),transpose(inputs)),targets)
	return beta

inputs = array([[0,0],[0,1],[1,0],[1,1]])
ANDtargets = array([[0],[0],[0],[1]])
print ("AND data")
ANDbeta = linreg(inputs,ANDtargets)
testin = concatenate((inputs,-ones((shape(inputs)[0],1))),axis=1)

ANDout = dot(testin,ANDbeta)
print (ANDbeta)
print (ANDout)'''

import numpy as np

x = np.array([[1.0,2.0],[1.3,2.3]])
y = np.array([[5.0],[5.9]])
x = np.concatenate((x,-np.ones((x.shape[1],1))),axis=1)
print(x)
beta = np.dot(np.dot(np.linalg.inv(np.dot(x.T,x)),x.T),y)
print(beta)
print(np.dot(x,beta))
