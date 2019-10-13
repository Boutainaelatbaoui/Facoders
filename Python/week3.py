username = input('Enter student\'s name: ')

s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s = 0
for s in s1 and s2 and s3  :
    if s == username :
        print('Ahmad',sum(s1[1:6]))
        break
    elif s == username :
        print('Sami',sum(s2[1:6]))
        break
    elif s == username :
        print('Faris',sum(s2[1:6]))
        break
    else :
        print('student is not recorded 0')
        break
