def split(source, sep, count = -1):
        '''this function returns the list consists of your source string that is splited with sep string.
       source is the first argument of function. sep is the secont argument of function.
       the third argument is count that defoult is -1.'''
       lst = []
       ind = 0
       q = 0
       i = 0
       while i < len(source):
             if source[i:(i + len(sep))] == sep:
                   lst.append(source[ind:i])
                   ind = i + len(sep)
                   q += 1
                   i += len(sep)
                   if q == count:
                         lst.append(source[ind:])
                         break
             else:
                    i += 1
             if len(source[i:]) < len(sep):
                    lst.append(source[ind:])
                    break
             else:
                   continue
       return lst


string = input("insert your string: ")
sep = input("insert the sep: ")
count = int(input("insert the count: "))
print(f"your list consists of your string is: {split(string, sep, count)}")
