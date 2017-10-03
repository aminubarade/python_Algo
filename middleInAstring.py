s = "messtersacksh"
sl= list(s)
c = len(sl)//2
if (len(s)%2==0):
  mid = sl[c-1]+sl[c]
  print (mid)
else:
  mid = sl[c]
  print (mid)