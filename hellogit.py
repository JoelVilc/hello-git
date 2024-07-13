print("Hello Git")

def main (*args):
    par = 0
    impar = 0
    for i in args:
        if i%2 == 0:
            par += i
        else:
            impar += i
    return par, impar

par, impar = main(3,4,5,6,7)
print(f"Par:{par}, Impar:{impar}")