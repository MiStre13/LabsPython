s = 'Шила(лишнее (лишнее) лишнее) в мешке не утаишь (лишнее)'
def remove_braces(st):
    print(st.rfind(')'))
    print(st.rfind('('))


print(remove_braces(s))