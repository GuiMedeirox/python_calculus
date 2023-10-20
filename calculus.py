import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
a = sp.symbols('a')
inf = sp.oo

q3_2_1 = (3**x + 9**x)**(1/x)
q3_2_2 = (((x+2)**(x+2))*(((x+3)**(x+3))))/((x+5)**((2*x)+5))
q3_2_3 = (sp.tan(x)/sp.tan(a))**(sp.cot(x-a))
q3_2_4 = ((1)/(sp.ln(x+(1+(x**2))**(1/2))))-((1)/(sp.ln(1+x)))
q3_3 = (((x**3)+(x**2)+x+1)**(1/3))-((((x**2)+x+1)**(1/2))*(sp.ln((sp.exp(1)**x)+x)/(x)))
q4_3_1 = (sp.acos(x)**2)+((sp.ln(sp.acos(x)**2))-(sp.ln(sp.acos(x)))+(1/2))
q4_3_2 = ((1/2)*(sp.atan((1+x**4)**(1/4))))+((1/4)*(sp.ln(((1+x**4)**(1/4)+1)/((1+x**4)**(1/4)-1))))
q4_3_3 = (sp.exp(1)**((x**2)*(-1)) * sp.asin(sp.exp(1)**((x**2)*(-1))))/((1-sp.exp(1)**((x**2)*(-1)))**(1/2))+(1/2)*(sp.ln(1-sp.exp(1)**((x**2)*(-1))))

def calc_limit_graph(func, point): 
  
  if(func == sp.sympify(q3_2_3)): 
    limit_left = sp.limit(func, x, a, dir='-' )
    limit_right = sp.limit(q3_2_1, x, a, dir='+' )
    print(limit_left)
    return limit_left

  elif(func != sp.sympify(q3_2_3)):
    limit_left = sp.limit(func, x, point, dir='-' )
    limit_right = sp.limit(func, x, point, dir='+' )
    print(limit_left if limit_left==limit_right else "this limit isn't continuous")
    return limit_left,limit_right

def calc_diff_graph(func):
  print(sp.diff(func,x))
  return sp.diff(func,x)


print("Digita qual equação você quer: \n")
print("a) 3.2.1")
print("b) 3.2.2")
print("c) 3.2.3")
print("d) 3.2.4")
print("e) 3.3")
print("f) 4.3.1")
print("g) 4.3.2")
print("h) 4.3.3")

opt = input()

if(opt=="a"): 
  calc_limit_graph(q3_2_1,inf)


elif(opt=="b"): 
  calc_limit_graph(q3_2_2,inf)

elif(opt=="c"): 
  calc_limit_graph(q3_2_3,a)

elif(opt=="d"): 
  calc_limit_graph(q3_2_4,0)

elif(opt=="e"): 
  calc_limit_graph(q3_3,inf)

elif(opt=="f"): 
  calc_diff_graph(q4_3_1)

elif(opt=="g"): 
  calc_diff_graph(q4_3_2)

elif(opt=="h"): 
  calc_diff_graph(q4_3_3)