class Num:
    def __init__(self,x): 
        self.x=x
    def isPalin(self): 
        """ Returns string which states if the given number is Palindrome or not."""
        if self.x[:]==self.x[::-1]: 
            print("Palindrome")
        else: print("Not Palindrome")


if __name__=="__main__": 
    x=input('Enter the input: \n')
    o1=Num(x)
    o1.isPalin()    

