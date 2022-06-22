import math
def rek(n,l1,l2,a0,a1):
    if (n ==1):
        return a1
    elif (n == 0):
        return a0

    else:
        niz = []
        niz.append(a0)
        niz.append(a1)

        for i in range(2,n+1,1 ):
            niz.append(l1*niz[i-1] + l2*niz[i-2])
        return niz[n]


l1 = float(input("Unesi prvi koeficijent rekurzivne relacije >"))
l2 = float(input("Unesi drugi koeficijent rekurzivne relacije >"))
a0 = float(input("Unesi vrijednost nultog clana niza a_0 >"))
a1 = float(input("Unesi vrijednost prvog clana niza a_1 >"))
n = int(input("Unesi redni broj n trazenog clana niza >"))

#metoda opce formule
a=1
b=-l1
c=-l2
x0 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
x1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)


if (x0 != x1):
    C2 = -(a1 - a0*x0)/(x0-x1)
    C1 = a0 - C2
    an = C1*x0**n + C2*x1**n
elif (x0 == x1):
    lambda1 = a0
    lambda2 = a1 - lambda1
    an = lambda1*x0**n + lambda2*n*x1**n

print("Vrijednost n-tog clana niza pomocu formule >", an)
print("Vrijednost n-tog clana niza iz rekurzije > ", rek(n, l1, l2, a0, a1))
