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
                      for ind1 in range(i + ind*len(old)):
                            name += source[ind1]
                      name += new
                      for ind2 in range((ind + 1)*len(old) + i, len(source)):
                            name += source[ind2]
                      source = name
                  else:
                        continue
             i += 1
        return name

print(repleace('enastenikenkjuy', 'en', 'x'))
