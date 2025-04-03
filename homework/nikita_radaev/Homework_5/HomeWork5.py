person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
a,b,c,d,e = person
print (a,b,c,d,e)


text_1 = 'результат операции: 42'
a =text_1[-2:]
print(int(a) + 10)
text_2 = 'результат операции: 514'
b =text_2[-3:]
print(int(b) + 10)
text_3 = 'результат работы программы: 9'
c =text_3[-1:]
print(int(c) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print(students ,'study these subjects:', subjects)