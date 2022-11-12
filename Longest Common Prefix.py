#Finding longest common prefix between words
def prefix(s1, s2):
    x = len(s1)
    for i in range(x,0,-1):
        if s2.startswith(s1[:i]):
            return s1[:i]




def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if prefix(s1,s2)!= None:
    
        print("The common prefix is",prefix(s1,s2))
    else:
        print("No common prefix") 


main()
