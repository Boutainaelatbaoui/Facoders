grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7],
'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

grade_name = ['grade_one', 'grade_two', 'grade_three']
students_names = ['Faris']
input('Choose one: students_names, student_score, students_count')
x = input('Enter a function: ')
def students_names(grade_name):
    if x == 'students names' :
        a = list(grade_one.keys())
        b = list(grade_two.keys())
        c = list(grade_three.keys())
        return a, b, c
print(students_names(grade_name))
y = input('Enter done or more: ')
if y == 'more' :
    x = input('Enter a function: ')
else :
    exit()
def students_score(grade_name,students_names) :
    if x == 'student score' :
        d = sum(grade_one.get('Faris'))
        return d
print(students_score(grade_name,students_names))
y = input('Enter done or more: ')
if y == 'more' :
    x = input('Enter a function: ')
else :
    exit()   
def students_count(grade_name) :
    if x == 'students count' :
        f = len(list(grade_one.keys()))
        return f
print(students_count(grade_name))
y = input('Enter done or more: ')
if y == 'more' :
    x = input('Enter a function: ')
else :
    exit()
