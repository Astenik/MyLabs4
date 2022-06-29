def repleace(source, old, new):
        '''this funtion repleace old with new in source.'''
        i = 0
        while len(source) - i >= len(old):
             string = ''
             lst = []
             for j in range(i, len(source)): 
                    string += source[j]
                    if len(string) == len(old):
                         lst.append(string)
                         string = ''
                         continue
                    else:
                        continue
             for ind in range(len(lst)):
                  if lst[ind] == old:
                       name = ''
                       for ind1 in range(i):
                             name += source[ind1]
                       for ind2 in range(ind):
                             name += lst[ind2]
                       name += new
                       for ind3 in range(i + (ind + 1)*len(old), len(source)):
                             name += source[ind3]
                       source = name
                       continue
                  else:
                       continue
             i += 1
        return name
name = input("insert name: ")
old = input("insert the old name: ")
new = input("insert new name: ")
print(repleace(name, old, new))
