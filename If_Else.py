print("Hello World")

x = 70
y = 70
z = 50

if x == y:
	print("x is equal to y ")
elif z < y:
    print("z is smaller than y")
elif x > z:
    print("x is greater and equal to y")
else:
    print("nothing")

if x > y: print("x is greater than y")

x = 50
y = 150
print(x) if x > y else print(y)

x = 50
y = 50
print("x is greater than y") if x > y else print("x is less than y") if x < y else print("X is equal to Y")

x = 50
y = 40
z = 100
if x > y and z > x:
    print("All conditions are true")

x = 50
y = 40
z = 100

if x > y and z > x:
    print("All conditions are true")
elif y < z and z > x:
    print("some conditons are true")
else:
    print("default")

x = int(input("Examination result :"))

if x < 101 and x >= 90 or x == 100:
    print("Grade A")
elif x <= 89 and x >= 70:
    print("Grade B")
elif x <= 69 and x >= 60:
    print("Grade C")
elif x <= 59 and x >= 40:
    print("Grade D")
elif x <= 39 and x > 0 or x == 0:
    print("Fail")
else:
    print("Wrong Number. Try Again!")
