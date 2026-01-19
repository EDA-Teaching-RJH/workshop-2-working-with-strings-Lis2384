import math  

def main():
    maths1 = int(input("What is a =")) #TO DO  
    maths2 = int(input("what is b ="))
    print(pythag(maths1,maths2))

def pythag(A,B):
    mathsM = (A**2 + B**2)
    mathsC = (mathsM**0.5)
    return(mathsC)


main()
