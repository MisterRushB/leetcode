def RomanToInteger(str): 
    sum=0
    buffer=0
    # x=OrderedDict(("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000))
    dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}  
    for i in range(len(str)): # i from 0 to 6. currently 1
        for key in dict.keys():  # 
            if str[i]==key:  # c ==c 
                if buffer<dict[key] and i>0: # 1000<100 False and i>0 True
                    sum-=buffer
                    sum+=(dict[key]-buffer)
                    continue
                sum+=dict[key]
                buffer=dict[key] 
    return sum

if __name__=="__main__":
    userInput=input("Enter: ")
    print(RomanToInteger(userInput))