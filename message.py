names = input('Enter names separated by commas: ').split(',')
#names.upper()
assignments = list(map(int,input('Enter assignment counts separated by commas: ').split(',')))
grades = list(map(int,input('Enter grades separater ny commas: ').split(',')))
for i in range(len(names)):
    print('Hi {},\n'.format(names[i].title()))
    print('This is a reminder that you have {} assignments left to sumit \
before you can graduate. Your current grade is {} and can increase to {} if \
you submit all assignments before the due data.\n'\
    .format(assignments[i],grades[i],grades[i]+assignments[i]*2))