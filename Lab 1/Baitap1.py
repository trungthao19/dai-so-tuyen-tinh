from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
solve(bieuthuc)
print("Nghiệm phương trình x + 3 = 5 là:", solve(bieuthuc))
bieuthuc2 = x**2 + 3 - 5
nghiem2 = solve(bieuthuc2)
print("Nghiệm phương trình x^2 + 3 = 5 là:", nghiem2)

print( nghiem2[0]) 
print( nghiem2[1])