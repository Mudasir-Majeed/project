# can we have a set wit 18(int) and '18'(str) as a value in it
s1={18,"18"}
print(s1)
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
# creat an empty dictionery . Allow 4 friends to enter their favourite language as value and use keys as their names. Asume that the names are unique
favLang={}
a=input("Enter your favourit language Mudasir\n")
b=input("Enter your favourit language Ulfat\n")
c=input("Enter your favourit language shayan\n")
d=input("Enter your favourit language Ifham\n")
favLang['Mudasir']=a
favLang['Ulfat']=b
favLang['shayan']=c
favLang['Ifham']=d
print(favLang)
# in dictionery keys should be unique but values should not be unique
# can you change the values inside a list which is cintained in a set 
# s={8,7,12,"Mudu",[1,2]}
# no we can't because list, tuple can't be changed