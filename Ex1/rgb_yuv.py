def RGBtoYUV(r, g, b):
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g + + 0.071 * b + 128

    return y, u, v


def YUVtoRGB(y, u, v):
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    r = 1.164 * (y - 16) + 1.596 * (v - 128)
    return r, g, b


print("1. RGBtoYUV\n"
      "2. YUVtoRGB\n")
selection = int(input("Introdueix la teva opció\n"))
if selection == 1:
    r = float(input("Introdueix el valor vermell\n"))
    b = float(input("Introdueix el valor blau\n"))
    g = float(input("Introdueix el valor verd\n"))
    print("valor YUV:", RGBtoYUV(r, g, b))
else:
    y = float(input("Introdueix el valor Y\n"))
    u = float(input("Introdueix el valor U\n"))
    v = float(input("Introdueix el valor V\n"))
    print("valor RGB:", YUVtoRGB(y, u, v))
