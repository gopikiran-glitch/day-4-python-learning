tup = (5, 'Welcome', 7, 'Geeks')
print(tup)
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)
tup1 = ('Geeks',) * 3
print(tup1)
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)





tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])  
print(tup[:3])
tup = ("Geeks", "For", "Geeks")
a, b, c = tup
print(a)
print(b)
print(c)

tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)




tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)