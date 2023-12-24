n = int(input("Введите сумму : "))

notes = [64,32,16,8,4,2,1]
counts = [0]*len(notes)

for i in range(len(notes)):
    counts[i] = n//notes[i]
    n %= notes[i]

for i in range(len(counts)):
    if counts[i]>0:
        print(f"Купюра номиналом {notes[i]} : {counts[i]}")
    
