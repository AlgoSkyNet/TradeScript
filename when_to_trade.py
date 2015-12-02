import numpy as np
from trade_to_file import Order

eps=1e-3

def backward2nddir(yend,yendm1,yendm2):
	return (yendm2-2*yendm1+yend)/(0.01**2)

def f(x):
	return x*x*x*x

xval=range(-100,100,1)
yval=[]
for i in range(0,len(xval)):
	yval.append(f(xval[i]/100.0))

secondderval=[0,0]
for i in range(2,len(yval)):
	secondderval.append(backward2nddir(yval[i],yval[i-1],yval[i-2]))


testfile=open("testf.txt","w")
for i in range(0,len(xval)):
	testfile.write(str(xval[i]/100.0)+"\t"+str(yval[i])+"\t"+str(secondderval[i])+"\n")


testfile.close()




def tradeFunc(yend,yendm1,yendm2):
	order1=Order()
	#sell coins if p is max
	if abs(yend-yendm1)<eps and backward2nddir(yend,yendm1,yendm2)<0:
			order1.operation="sell"
			order1.price=yend
			
	#buy coins is p is min
	if abs(yend-yendm1)<eps and backward2nddir(yend,yendm1,yendm2)>0:
			order1.operation="buy"
			order1.price=yend
			
	return order1
		


