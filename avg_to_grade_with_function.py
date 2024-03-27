def get_info(): #5개의 학생(이름, 학번)으로부터 3개의 교과목을 입력
    student_name =[]
    student_id = []
    english_score =[]
    c_score = []
    python_score = []

    for i in range(5):
        student_name.append(input(f" {i+1}번째 학생의 이름 :"))
        student_id.append(input("학생의 학번 :"))
        english_score.append(int(input("학생의 영어 점수 :")))
        c_score.append(int(input("학생의 c언어 점수 :")))
        python_score.append(int(input("학생의 python 점수 :")))

    return student_name, student_id, english_score, c_score, python_score

def calculate(eng_score, c_score, python_score): #3개의 교과목 점수를 받아서 평균과 총점을 구해주는 함수
    total_score = []
    avg_score = []
    total = 0

    for i in range(5):
        total = eng_score[i] + c_score[i] + python_score[i]
        total_score.append(total)

    for i in range(5):
        avg_score.append(total_score[i] / 3)

    return total_score, avg_score

def get_grade(avg_score): #평균 점수를 받아서 학점을 구해주는 함수
    grade = []
    for i in range(5): 
        if (avg_score[i] >= 90):
            grade.append("A")

        elif (avg_score[i] >= 80):
            grade.append("B")

        elif (avg_score[i] >= 70):
            grade.append("C")

        elif (avg_score[i] >= 60):
            grade.append("D")

        else:
            grade.append("F")

    return grade

def sorted_rank(total_score):
    rank = [sorted(total_score, reverse = True).index(i) for i in total_score]
    return rank

def print_info(student_name, student_id, eng_score, c_score, python_score, total, avg, grade, rank):
    print("성적 관리 프로그램")
    print("=" * 94)
    print("학번\t이름\t영어\tc-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 94)
    for i in range(0,5):
        print(f"{student_id[i]}\t{student_name[i]}\t{eng_score[i]}\t{c_score[i]}\t{python_score[i]}\t{total[i]}\t{avg[i]: 4.2f}\t{grade[i]}\t{rank[i]+1}\t")


student_name, student_id, english_score, c_score, python_score= get_info()

total_score, avg_score =calculate(english_score, c_score, python_score)

grade = get_grade(avg_score)

rank = sorted_rank(total_score)
    
print_info(student_name, student_id, english_score, c_score, python_score,total_score, avg_score, grade,rank)
