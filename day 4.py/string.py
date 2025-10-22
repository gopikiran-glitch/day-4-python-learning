s = """I am Gopi
Python String on NMK"""
print(s)

s = '''I'm a 
NMK traine'''
print(s)


s = "GeeksforGeeks"
print(s[0])   
print(s[4])   


s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])    
print(s[3:])     
print(s[::-1])   


s = "Python"
for char in s:
    print(char)


s = "hello geeks"
s1 = "H" + s[1:]                   
s2 = s.replace("geeks", "NMK")  
print(s1)
print(s2)


s = "   Gfg   "
print(s.strip())    
s = "Python is fun"
print(s.replace("fun", "awesome"))


s = "Hello "
print(s * 3)


s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

s = "NMK"
print("N" in s)
print("h" in s)