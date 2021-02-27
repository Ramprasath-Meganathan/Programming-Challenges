if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    for name,score in student_marks.items():
        if name==query_name:
            print("{:.2f}".format(sum(score)/len(score)))
        
