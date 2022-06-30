def repleace(source, old, new, count = -1):
       q = 0
       for i in range(len(source)):
               if source[i:(i + len(old))] == old:
                       string = ''
                       string += source[:i]
                       string += new
                       string += source[(i + len(old)):]
                       source = string
                       q += 1
               if q == count:
                        break
               else:
                        continue
       return string

source = input("insert the string: ")
old = input("insert old string: ")
new = input("insert new string: ")
print(f'your new string is: {repleace(source, old, new, 2)}')
