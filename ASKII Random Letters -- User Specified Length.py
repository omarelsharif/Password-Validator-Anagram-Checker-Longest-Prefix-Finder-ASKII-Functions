def randoms(i):
    i = i
    run = "yes"
    if run == "yes":
        randstring = [] 
        for x in range(0,i):
            import random
            
                
            z= random.randint(97,122)
            
              
            print(chr(z), end="")



def main():
    i = int(input("Enter the length of the string: "))
    print ("The random string is:", end="")
    randoms(i) 


main()
