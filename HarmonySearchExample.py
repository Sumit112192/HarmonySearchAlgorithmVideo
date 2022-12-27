def f(x1, x2):
   return 4*x1**2-2.1*x1**4+(1/3)*x1**6+x1*x2-4*x2**2+4*x2**4


# PVB = Possible Value Bound
# U = Upper
# L = Lower
UPVB = 10
LPVB = -10

HMS = 10
HMCR = 0.85
PAR = 0.45
bw = (UPVB-LPVB)/100


