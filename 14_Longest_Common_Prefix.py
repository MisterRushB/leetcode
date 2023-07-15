def commonPrefix(str): 
    i=-1
    points=0
    # for word in str: 
    #     print((str[0])[:i])
    #     if str[0][0:i]==word: 
    #         points+=1
    #     if points==len(str[0]):
    #         return str[:i]
    #     i-=1

    for i in range(len(str[0])):
        i*=-1 
        for word in str:
            print(str[0][0:i])
            if str[0][0:i]==word: 
                points+=1
            if points==len(str[0]):
                return str[:i]
        

if __name__=="__main__": 
    list=["flower","flow","flight"]
    print(commonPrefix(list))