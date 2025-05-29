from sympy import solve, Symbol
x = Symbol('x')
ptb2 = x**2 + 9*x + 8
nghiemx = solve(ptb2, dict=True)
print(nghiemx)

ptb21 = x**2 + 1*x + 10 
nghiemx1 = solve(ptb21, dict = True)
print(nghiemx1)
