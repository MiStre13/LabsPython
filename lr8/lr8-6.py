s = 'Жилибылидедушкаибабушка'
s2= ""
def camel(st):
    s2= ""
    for i in range(len(st)):
        if i%2==0:
            s2+=s[i].upper()
        else:
            s2+=s[i].lower()
    return s2
print(camel(s))