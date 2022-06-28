def join(lst, sep):
     '''this function returns string consists of members of list that are connected to each other with sep.
     sep is the second argument of the function.
     list is the first argument of the function.'''
     string = ''
     for ind in range(len(lst) - 1):
          string += lst[ind]
          string += sep
     string += lst[len(lst) - 1]
     return string

lst = []
mem = input("insert the member of your list: ")
lst.append(mem)
while mem != '':
      mem = input("insert the member of your list: ")
      lst.append(mem)
sep = input("insert the sep: ")
print(join(lst, sep))
