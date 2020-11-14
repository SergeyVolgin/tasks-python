def longitude(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
triangles = []

for i in v:
    a = longitude(i[0], i[1])
    b = longitude(i[0], i[2])
    c = longitude(i[1], i[2])
    triangle = []
    p = (a + b + c)/2
    area = math.sqrt(p + (p - a) * (p - b) * (p - c))
    triangle.append(p*2)
    triangle.append(area)
    triangles.append(triangle)

def is_sim(sample, triange):
    if int (sample[0]/triangle[0])**2 == int (sample[1]/triangle[1]):
        return "Подобен"
    else:
        return "Не подобен"

for i in range(0, len(triangles) - 1):
    if is_sim(triangles[0], triangles[i]):
        print str(i+1)
