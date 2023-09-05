import sympy
from IPython.display import display,Math
from sympy.abc import X

p1= 2*X**3 + X**2 -X
p2 = 4*X**2 - 3*X**3- 2*X

display(Math(f"({sympy.latex(p1)}) - ({sympy.latex(p2)}) =" +sympy.latex(p1-p2)))


p3 = sympy.Poly(2*X**3 + X**2 -X)
p4 = 2*X**3 + X**2 -X
display(Math("cho polynomials:"+ sympy.latex((p4))))
print("Thế số 5 vào đa thức ta có")
p3.eval(5)