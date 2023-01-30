# this is helper function for main function.
def design(n):
    sn = ''
    for i in n:
        sn += i
        sn += '-'
    return  sn[ :-1][ : 0: -1] + sn[ : -1] 

# Main function to print rangoli  
def print_rangoli(size):
    s = 'abcdefghijklmnopqrstuvwxyz'
    # slicing required string and reverting it
    sn = s[ :size][ : : -1]
    for i in range(size - 1):
        print(design(sn[i : : -1]).center(4 * size - 3, '-'))
    print(design(sn[len(sn) -1 : : -1]).center(4 * size - 3, '-'))
    for i in range(size - 2, -1, -1):
        print(design(sn[i : : -1]).center(4 * size - 3, '-'))
print_rangoli(26)