with open('student_names.txt', 'r') as student_names:
    names = student_names.read()

random_names = ['maria', 'sami', 'lyes', 'hiba', 'fifi']

with open('student_names.txt', 'a') as student_names:
    for name in random_names:
        student_names.write('\n' + name)

with open('student_names.txt', 'r') as student_names:
    names = student_names.readlines()
    print("first 5 lines :")
    print(names[:5])
    print("last 5 lines :")
    print(names[-5:])
with open('student_names.txt', 'r') as student_names:
    name = student_names.readline()
    while name != '':
        if(name == 'adam\n'):
            break
        name = student_names.readline()
    if(name=='adam\n'):
        print('adam does exist in our list')
    else:
        print("adam isn't in our list")
for i in range(65,91):
    open(chr(i) + '.txt', 'w')
