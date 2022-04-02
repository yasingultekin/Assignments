while True :
    
    number = input("Enter a positive integer number: ")
    digits = len(number)
    summ = 0
    
    if not number.isdigit() :
        
        print(number, "is invalid entry. Please enter valid input.")
        
    elif int(number) >= 0 :
        
        for i in range(digits) :
            
            summ = summ + int(number[i]) ** digits
            
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break
