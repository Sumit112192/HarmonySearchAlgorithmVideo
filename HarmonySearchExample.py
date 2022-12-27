import random

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

HM = []

for i in range(HMS):
    x1 = random.uniform(LPVB, UPVB)
    x2 = random.uniform(LPVB, UPVB)
    HM.append([x1, x2, f(x1, x2)])
HM = sorted(HM, key = lambda x: x[2])


iterations = 10000
while(iterations--):
    x = [0, 0]
    for i in range(2):
        ran = random.uniform(0, 1)
       
        if ran < HMCR:
            index = int(ran*(HMS - 1))
            x[i] = HM[index][i]
            ran2 = random.uniform(0, 1)
            if ran2 < PAR:
                if ran2 <= 0.5:
                    temp = x[i]-ran*bw
                    if LPVB<temp:
        
        
        else:
            x[i] = random.uniform(LPVB, UPVB)
        
