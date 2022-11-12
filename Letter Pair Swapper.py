



#Swaps adjacent pairs of letters

def swap_pairs(string):
    result = str("")
    for i in range(0, len(string)-1, 2):
        result += string[i+1]
        result += string[i]
    if (len(string) % 2 != 0):
        result += string[len(string)-1]
    return result

print(swap_pairs(str(input("Enter a string: "))))

