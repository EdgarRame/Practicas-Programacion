#Cabezal
print("**** FizzBuzz ****")

# Impresión de números del 1 al 20
for i in range(1, 21):
    if i %3 == 0:
        print("Fizz")
    elif i %5 == 0:
        print("Buzz")
    elif i %3 ==0 and i %5 == 0:
        print("FizzBuzz")