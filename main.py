import math


def getAngleA(angleB, angleC):
    return 180 - (angleB + angleC)


def getAngleB(angleA, angleC):
    return 180 - (angleA + angleC)


def getAngleC(angleA, angleB):
    return 180 - (angleA + angleB)


def hyp(sideX, sideY):
    return math.sqrt(sideX**2 + sideY**2)


def nonHyp(sideX, sideY):
    return math.sqrt(sideX**2 - sideY**2)


def getPerimeter(sideA, sideB, sideC):
    return sideA + sideB + sideC


def getArea(sideA, sideB):
    return (sideA * sideB) / 2


print('\n\n\n')
sideA = int(input('\nEnter length of side a (0 for unknown): '))
sideB = int(input('\nEnter length of side b (0 for unknown): '))
sideC = int(input('\nEnter length of side c (0 for unknown): '))
angleA = int(input('\nEnter degrees of angle A (0 for unknown): '))
angleB = int(input('\nEnter degrees of angle B (0 for unknown): '))
angleC = int(input('\nEnter degrees of angle C (0 for unknown): '))
perimeter = int(input('\nEnter perimeter (0 for unknown): '))
area = int(input('\nEnter area (0 for unknown): '))

print('\n')

if angleA == 0 and angleB != 0 and angleC != 0:
    angleA = getAngleA(angleB, angleC)
    print('Angle A is ' + str(angleA))
elif angleB == 0 and angleA != 0 and angleC != 0:
    angleB = getAngleB(angleA, angleC)
    print('Angle B is ' + str(angleB))
elif angleC == 0 and angleA != 0 and angleB != 0:
    angleC = getAngleC(angleA, angleB)
    print('Angle C is ' + str(angleC))

if angleA == 90 or angleB == 90 or angleC == 90:
    if sideA == 0 and sideB != 0 and sideC != 0:
        if angleA == 90:
            sideA = hyp(sideB, sideC)
        elif angleB == 90:
            sideA = nonHyp(sideB, sideC)
        elif angleC == 90:
            sideA = nonHyp(sideC, sideB)
        print('Side a is ' + str(sideA))
    elif sideB == 0 and sideA != 0 and sideC != 0:
        if angleA == 90:
            sideB = nonHyp(sideA, sideC)
        elif angleB == 90:
            sideB = hyp(sideA, sideC)
        elif angleC == 90:
            sideB = nonHyp(sideC, sideA)
        print('Side b is ' + str(sideB))
    elif sideC == 0 and sideA != 0 and sideB != 0:
        if angleA == 90:
            sideC = nonHyp(sideA, sideB)
        elif angleB == 90:
            sideC = nonHyp(sideB, sideA)
        elif angleC == 90:
            sideC = hyp(sideB, sideA)
        print('Side c is ' + str(sideC))

if perimeter == 0 and sideA != 0 and sideB != 0 and sideC != 0:
    perimeter = getPerimeter(sideA, sideB, sideC)
    print('The perimeter is ' + str(perimeter))

if area == 0:
    if angleC == 90:
        area = getArea(sideA, sideB)
    elif angleA == 90:
        area = getArea(sideB, sideC)
    elif angleB == 90:
        area = getArea(sideC, sideA)

    print('The area is ' + str(area))
