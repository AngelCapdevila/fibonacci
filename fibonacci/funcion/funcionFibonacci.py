'''
Created on 25 nov. 2016

@author: usuario
'''
def fibonacci(num):
    if num==1:
        return 1
    if num==0:
        return 0 
    else:
        return fibonacci(num-1)+fibonacci(num-2)
if __name__=="__main__":
    num=int(input("escriba el numero sobre el que se desea saber la funcion de fibonacci"))
    print (fibonacci (num))
