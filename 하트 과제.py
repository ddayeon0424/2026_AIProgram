# 하트 윗부분
print("  *** *** ")
print(" ***** ***** ")

# 하트 아랫부분
for i in range(7, 0, -1):  
    for j in range(7 - i):
        print(" ", end="")
        
    for j in range(2 * i - 1):
        print("*", end="")
        
    print()
