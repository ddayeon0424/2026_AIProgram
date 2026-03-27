Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#1
num = 100
print('num = ', num)
num =  100
num = num + 100
print('num = ', num)
num =  200
num = num + 100
print('num = ', num)
num =  300
num = 0
for i in range(100):
    num += 100
    print('ith num = ', i, num)

    
ith num =  0 100
ith num =  1 200
ith num =  2 300
ith num =  3 400
ith num =  4 500
ith num =  5 600
ith num =  6 700
ith num =  7 800
ith num =  8 900
ith num =  9 1000
ith num =  10 1100
ith num =  11 1200
ith num =  12 1300
ith num =  13 1400
ith num =  14 1500
ith num =  15 1600
ith num =  16 1700
ith num =  17 1800
ith num =  18 1900
ith num =  19 2000
ith num =  20 2100
ith num =  21 2200
ith num =  22 2300
ith num =  23 2400
ith num =  24 2500
ith num =  25 2600
ith num =  26 2700
ith num =  27 2800
ith num =  28 2900
ith num =  29 3000
ith num =  30 3100
ith num =  31 3200
ith num =  32 3300
ith num =  33 3400
ith num =  34 3500
ith num =  35 3600
ith num =  36 3700
ith num =  37 3800
ith num =  38 3900
ith num =  39 4000
ith num =  40 4100
ith num =  41 4200
ith num =  42 4300
ith num =  43 4400
ith num =  44 4500
ith num =  45 4600
ith num =  46 4700
ith num =  47 4800
ith num =  48 4900
ith num =  49 5000
ith num =  50 5100
ith num =  51 5200
ith num =  52 5300
ith num =  53 5400
ith num =  54 5500
ith num =  55 5600
ith num =  56 5700
ith num =  57 5800
ith num =  58 5900
ith num =  59 6000
ith num =  60 6100
ith num =  61 6200
ith num =  62 6300
ith num =  63 6400
ith num =  64 6500
ith num =  65 6600
ith num =  66 6700
ith num =  67 6800
ith num =  68 6900
ith num =  69 7000
ith num =  70 7100
ith num =  71 7200
ith num =  72 7300
ith num =  73 7400
ith num =  74 7500
ith num =  75 7600
ith num =  76 7700
ith num =  77 7800
ith num =  78 7900
ith num =  79 8000
ith num =  80 8100
ith num =  81 8200
ith num =  82 8300
ith num =  83 8400
ith num =  84 8500
ith num =  85 8600
ith num =  86 8700
ith num =  87 8800
ith num =  88 8900
ith num =  89 9000
ith num =  90 9100
ith num =  91 9200
ith num =  92 9300
ith num =  93 9400
ith num =  94 9500
ith num =  95 9600
ith num =  96 9700
ith num =  97 9800
ith num =  98 9900
ith num =  99 10000
>>> #2
>>> age = int(input("나이를 입력하세요:"))
나이를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    age = int(input("나이를 입력하세요:"))
ValueError: invalid literal for int() with base 10: ''
>>> age = int(input("나이를 입력하세요:"))
나이를 입력하세요:20
