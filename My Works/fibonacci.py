a=1
b=1
fibonacci=[a,b]
for i in range(0,10):
    a,b=b,a+b
    fibonacci.append(b)
    print("a: ",a,"b: ",b)
print(fibonacci)