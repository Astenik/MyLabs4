def  repleace(source, old, new, count = -1):
        '''this funtion repleace old with new in source.'''
       index = 0
       name = source
       num = old[0]
       q = 0
       while  name != None:
            for i in range(len(source)):
                 if (source[i] == num) and (source[i:(i + len(old))] == old):
                       index = i
                       q += 1
                       break
                 elif source[i] != num:
                       continue
            string = ''
            string += source[:index]
            string += new
            string += source[(index + len(old)):]
            source = string
            if q == count:
                  break
            else:
                 continue
            name = source[(index + len(old)):]
       return string
source = input("insert your string: ")
old = input("insert old string: ")
new = input("insert new string: ")
count = int(input("insert count: "))
print(f'your new string is: {repleace(source, old, new, count)}')
