def repleace(source, old, new, count):
      '''this function replease new in source insted of old.'''
      q = 1
      f = 0
      while q <= count:
         string = ' '   
         i = 0
         lst = []
         while i < len(old):
              for num in range(f, len(source)):
                  if old[i] == source[num]:
                        string += source[num]
                        lst.append(num)
                        break
                  else:
                      continue
              i += 1 
         h = 0
         for d in range(1, len(lst)):
                   if lst[d] - lst[d - 1] != 1:
                       h += 1
                   else: 
                         continue
         if h == 0:
              name = ' '
              l = 0
              while l < lst[0]:
                   name += source[l]
                   l += 1
              for n in new:
                   name += n
              for k in range(lst[len(lst) - 1] + 1, len(source)):
                   name += source[k]
         else:
              continue
         q += 1     
         f = lst[len(lst) - 1] + 1
         source = name
      return name


print(repleace('astenik', 'as', 'As', 1))
