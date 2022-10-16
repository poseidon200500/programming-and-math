m = []
for i in range(3):
    m.append(list(map(int,input()).split))

glav = m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][1]*m[1][0]
poboch = m[0][2]*m[1][1]*m[2][0] + m[0][1]*m[1][0]*m[2][2] + m[1][2]*m[2][1]*m[0][0]

opred = glav-poboch
print(opred)