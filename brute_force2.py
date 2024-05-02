from problem import Problem
import copy
import sys

def act(prob):
    if prob.loc == 6:
        scores = [0]*6
        max_score = 0
        max_loc = 0
        for i in range(6):
            p = copy.deepcopy(prob)
            p.select(i)
            score = run(p)
            if score > max_score:
                max_score = score
                max_loc = i
        prob.select(max_loc)
        return f"select {max_loc}"
    else:
        pstay = copy.deepcopy(prob)
        pstay.stay()
        bestscore = run(pstay)
        bestAct = 6
        for i in range(6):
            if (not prob.array[i] == 0):
                numsteps = min((i - prob.loc)%6, (prob.loc - i)%6)
                if numsteps < prob.array[i]:
                    pswipe = copy.deepcopy(prob)
                    pswipe.iswipe(i)
                    sswipe = run(pswipe)
                    if sswipe > bestscore:
                        bestscore = sswipe
                        bestAct = i
        if bestAct == 6:
            prob.stay()
            return "stay"
        else:
            prob.iswipe(bestAct)
            return f"swipe {bestAct}" 

        

def run(prob, printing = False):
    while not prob.array == [0]*6:
        k=act(prob)
        if printing:
            print(k)
        
    return prob.score

# p = Problem([3,1,4])
# print(run(p, True))
# print(p)
# p.select(2)
# print(p)
# p.iswipe(0)
# print(p)
if __name__ == "__main__":
    vals = list(map(lambda x: int(x),sys.argv[1:]))
    p = Problem(vals)
    print(run(p, True))
