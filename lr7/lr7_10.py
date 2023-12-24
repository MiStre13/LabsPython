def calculate_passing_score(filename, k):
    with open(filename, 'r') as file:
        lines = file.readlines()

    scores = []
    for line in lines[1:]:
        data = line.strip().split()
        name = ' '.join(data[:-3])
        exam_scores = list(map(int, data[-3:]))
        if all(score >= 40 for score in exam_scores):
            scores.append(sum(exam_scores))

    scores.sort(reverse=True)
    num_accepted = min(k, len(scores))

    if num_accepted == 0:
        return 0
    elif num_accepted < len(scores) and scores[num_accepted-1] == scores[num_accepted]:
        return 1
    else:
        return scores[num_accepted-1]

filename = '/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr10.txt' 
k = 10  # Места

passing_score = calculate_passing_score(filename, k)
print("Проходной балл:", passing_score)
