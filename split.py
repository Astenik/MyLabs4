def  split(source, sep):
      '''this function returns list consists of the subjunctiveս of source. 
      source is the first argument of function.'''
      lst = []
      index = 0
      j = 0
      while  j <= len(source):
            name = ''
            for ind in range(len(source)):
                 if source[ind] == sep:
                       index = ind
                       break
                 else: 
                       name += source[ind] 
                       continue
            lst.append(name)
            string = ''
            for i in range(index + 1, len(source)):
                  string += source[i]
            source = string
            j += 1
      return lst

string = input("insert your string: ")
print(f"your list consists of your string is: {split(string, ',')}")
