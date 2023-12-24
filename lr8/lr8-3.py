
from collections import Counter

def most_common_top3(st):
    strng = Counter("".join(st.split()))
    return strng.most_common(3)

print(most_common_top3('Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью'))