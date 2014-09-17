days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month):
    return days_in_month[month - 1]

# print how_many_days(1)
# print how_many_days(9)

def replace_spy(list):
    list[2] = list[2] + 1

spy = [0, 0, 7]
replace_spy(spy)
# print spy

light_km_s = 300000.0
light_m = light_km_s * 1000
mili = 1.0 / 1000
nano = 1.0 / 1000 / 1000 / 1000
bits_in_terabyte = 1024 * 1024 * 1024 * 1024 * 8.0

# print light_m * nano * 0.4
# print light_m * nano * 12
# print light_km_s * mili * 7
# print 100 / bits_in_terabyte / nano


def sum_list(list):
    sum = 0
    for element in list:
        sum = sum + element
    return sum

# print sum_list([1, 7, 4])


def measure_udacity(list):
    udacity = 0
    for name in list:
        if 'U' == name[0]:
            udacity = udacity + 1
    return udacity

# print measure_udacity(['Dave','Sebastian','Katy'])
# print measure_udacity(['Umika','Umberto'])


def find_element(list, element):
    if element in list:
        return list.index(element)
    return -1

# print find_element([1,2,3],3)
# print find_element(['alpha','beta'],'gamma')


def union(list_a, list_b):
    for e in list_b:
        if e not in list_a:
            list_a.append(e)

a = [1,2,3]
b = [2,4,6]
union(a, b)
print a
print b


# Homework
p = [4, 5, 32]
def proc(p):
    q = p
    p.append(3)
    q.pop()
    print p

proc(p)
print p

def product_list(list):
    result = 1
    for e in list:
        result = result * e
    return result

print product_list([9])
print product_list([3, 4, 5])

def greatest(list):
    bigger = 0
    for e in list:
        if e > bigger:
            bigger = e
    return bigger

print greatest([4, 23, 47])

def total_enrollment(unis):
    sum_students = 0
    sum_tuition = 0
    for uni in unis:
        sum_students = sum_students + uni[1]
        sum_tuition = sum_tuition + uni[1] * uni[2]
    return [sum_students, sum_tuition]

udacious_univs = [['Udacity',90000,0]]
usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

# print total_enrollment(udacious_univs)
# (90000,0)
# print total_enrollment(usa_univs)
#(77285,3058581079L)

# Sudoku
#A valid sudoku square satisfies these two properties:

#   1. Each column of the square contains each of the numbers from 1 to n exactly once.
#   2. Each row of the square contains each of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

def check_sudoku(sudoku):
    transverse = []
    for line in sudoku:
        transverse.append([])

    for line in sudoku:
        index = 0
        while line:
            e = line.pop()
            if e in line:
                return False
            transverse[index].append(e)
            index = index + 1
    for column in transverse:
        while column:
            e = column.pop()
            if e in column:
                return False
    return True

print check_sudoku(incorrect)
