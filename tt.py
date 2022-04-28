from numpy import matrix as Ma
from numpy import sin, cos
from PIL import Image

# kangjian 20220219
PI = 3.14159265
im = Image.new('RGB', (2400, 2400), (1, 1, 80))
C = (255, 255, 255)


def Bezier3(P, S, C):  ##控制点,起始点,颜色
    M = Ma('1,-3,3,-1;0,3,-6,3;0,0,3,-3;0,0,0,1')
    Temp = P @ M
    for i in range(300):
        t = i / 300
        U = Ma([[1], [t], [t * t], [t * t * t]])
        X = Temp @ U
        px = int(X[0] + S[0])
        py = int(X[1] + S[1])
        im.putpixel((px, py), C)
        im.putpixel((px, py + 1), C)  # 加粗
        im.putpixel((px + 1, py), C)
        im.putpixel((px + 1, py + 1), C)
        im.putpixel((px + 2, py + 1), C)
        im.putpixel((px + 3, py + 1), C)
        im.putpixel((px - 2, py + 1), C)
        im.putpixel((px - 1, py + 1), C)


def leaf1(S, a):  # 原点,角度
    Q = [[[284, 11], [371, 99], [268, 181], [289, 249]],
         [[285, 13], [258, 63], [263, 140], [302, 166]],
         [[374, 143], [312, 168], [282, 222], [296, 291]],
         [[370, 148], [385, 227], [326, 255], [292, 266]],
         [[219, 176], [282, 221], [291, 269], [292, 311]],
         [[222, 178], [192, 273], [331, 293], [306, 439]],
         [[184, 317], [267, 319], [324, 396], [280, 439]],
         [[188, 314], [201, 390], [291, 387], [294, 422]],
         [[435, 269], [352, 262], [309, 334], [345, 404]],
         [[435, 265], [428, 320], [389, 352], [332, 351]],
         [[299, 266], [294, 309], [309, 337], [331, 351]],
         [[129, 450], [160, 449], [199, 407], [293, 450]],
         [[126, 453], [219, 522], [313, 461], [336, 393]],
         [[356, 412], [414, 404], [488, 438], [556, 526]],
         [[349, 404], [378, 466], [467, 485], [507, 480]],
         [[293, 452], [322, 453], [379, 447], [399, 460]]]
    for Qi in Q:
        P = Ma([[i[0] - 321 for i in Qi], [i[1] - 472 for i in Qi]])
        T = Ma([[cos(a), -sin(a)], [sin(a), cos(a)]])
        P = T @ P
        Bezier3(P, S, C)


def snow1(S):
    for j in range(6):
        a = -j * 2 * PI / 6
        for i in range(600):
            t = i * 2 * PI / 600  # 半径
            r = 8 * (1 + 0.8 * cos(8 * t)) * (1 + sin(t))
            x = r * cos(t)
            y = -r * sin(t) - 20  # 偏移
            x1 = x * cos(a) - y * sin(a) + S[0]  # 旋转
            y1 = x * sin(a) + y * cos(a) + S[1]
            im.putpixel((int(x1), int(y1)), C)


for i in range(6):
    x = int(1200 + 500 * cos(i * PI / 3 + PI / 2))
    y = int(1200 - 500 * sin(i * PI / 3 + PI / 2))
    leaf1((x, y), -i * PI / 3)

for i in range(6):
    x = int(1200 + 140 * cos(i * 2 * PI / 6 + PI / 3))
    y = int(1200 - 140 * sin(i * 2 * PI / 6 + PI / 3))
    snow1((x, y))
for i in range(6):
    x = int(1200 + (225) * cos(i * 2 * PI / 6))
    y = int(1200 - (225) * sin(i * 2 * PI / 6))
    snow1((x, y))

for j in range(4):
    for i in range(12):
        x = int(1200 + (45 * j + 270) * cos(i * 2 * PI / 12 + (1 + j) % 2 * PI / 12))
        y = int(1200 - (45 * j + 270) * sin(i * 2 * PI / 12 + (1 + j) % 2 * PI / 12))
        snow1((x, y))

for i in range(24):
    x = int(1200 + (180 + 270) * cos(i * 2 * PI / 24 + PI / 24))
    y = int(1200 - (180 + 270) * sin(i * 2 * PI / 24 + PI / 24))
    snow1((x, y))

for i in range(2400):
    a = i * 2 * PI / 2400
    r = 500 + 5 * sin(12 * a + PI / 6)
    x = int(r * cos(a) + 1200)
    y = int(r * sin(a) + 1200)
    im.putpixel((x, y), C)
    im.putpixel((x + 1, y), C)
    im.putpixel((x + 1, y + 1), C)
im.save("bigsnow1.jpg")
im.show()
