def factorial (x) :
    if x == 0 :
        return 1;
    else :
        return x * factorial(x-1);           


if  __name__ == "__main__":
    
    numList = [];
    
    for i in range(0,8) :
        numList.append(2 * i);

    for i in range(len(numList)) :
        x = numList[i];
        res = factorial(x);
        print(str(x) +" factorial is " + str(res));
