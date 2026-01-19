def main():
    slow = input("Input:")
    myFunction(slow)
    print(myFunction(slow))

def myFunction(text):
  #Your code goes here.
 T2 = text.replace(' ','...')
 return(T2)
main()
