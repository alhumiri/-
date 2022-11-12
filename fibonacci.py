path = 'C:\days.txt'
def fib(n):  # العودة إلى تسلسل فيبوناتشي من n
    result = []
    a, b =0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    file = open(path,'w')
    text=str(result)
    file.write(text)
    file.close()
    file = open(path,'r')
    print(file.readlines())
    file.close()
fib(100)
print()




#كتابه على الملف





