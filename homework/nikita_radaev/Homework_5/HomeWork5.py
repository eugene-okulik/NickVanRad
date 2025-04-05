person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
a, b, c, d, e = person
print(a, b, c, d, e)

text_1 = 'результат операции: 42'
a = text_1.index(': ') + 1
b = text_1[a:]
print(int(b) + 10)
text_2 = 'результат операции: 514'
c = text_2.index(': ') + 1
d = text_2[c:]
print(int(d) + 10)
text_3 = 'результат работы программы: 9'
e = text_3.index(': ') + 1
f = text_3[e:]
print(int(f) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print(students, 'study these subjects:', subjects)
