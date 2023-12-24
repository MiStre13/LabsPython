



def first_last(let, st):
    lst = (st.find(let),st.rfind(let))
    return lst

stroka = 'jili bili deda i babaj'
print(first_last('j',stroka))