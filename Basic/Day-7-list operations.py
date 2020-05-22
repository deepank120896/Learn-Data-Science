# Consider a list (list = []). You can perform the following commands:

# Input Format
# The first line contains an integer, denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())

    l = []
    for i in range(N):
        inp = input()

        if inp.find('insert')>=0:
            op=inp.split()
            a=int(op[1])
            b=int(op[2])
            l.insert(a,b)
        elif inp.find('print')>=0:
            print(l)
        elif inp.find('remove')>=0:
            op=inp.split()
            a=int(op[1])
            l.remove(a)
        elif inp.find('append')>=0:
            op=inp.split()
            a=int(op[1])
            l.append(a)
        elif inp.find('sort')>=0:
            l.sort()
        elif inp.find('pop')>=0:
            l.pop()
        elif inp.find('reverse')>=0:
            l.reverse()


           
