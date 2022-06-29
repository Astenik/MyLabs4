def  split(source, sep, count = -1):
       '''this function returns the list consists of your source string that is splited with sep string.
       source is the first argument of function. sep is the secont argument of function.
       the third argument is count that defoult is -1.'''
       lst = []
       index = 0
       j = 0
       num = sep[0]
       q = 0
       while  j < len(source):
            name = ''
            for i in range(len(source)):
                 if (source[i] == num) and (source[i:(i + len(sep))] == sep):
                       index = i
                       q += 1
                       break
                 elif source[i] != num:
                       name += source[i] 
                       continue
            lst.append(name)
            string = ''
            for ind in range(index + len(sep), len(source)):
                  string += source[ind]
            source = string
            if q == count:
                  lst.append(source)
                  break
            j += 1
       return lst

string = input("insert your string: ")
sep = input("insert the sep: ")
count = int(input("insert the count: "))
print(f"your list consists of your string is: {split(string, sep, count)}")
         
