from problem import Problem
import copy
import sys

def act(prob, storedVals):
    eqClass, flipped = prob.eqClass()
    if eqClass in storedVals.keys():
        value = storedVals[eqClass]
        if value == 6:
            prob.stay()
            return "stay"
        if len(eqClass) == 7:
            prob.select(value)
            return f"select {value}"
        loc = decode(value, flipped, prob.loc)
        prob.iswipe(loc)
        return f"swipe {loc}"

    if prob.loc == 6:
        scores = [0]*6
        max_score = 0
        max_loc = 0
        for i in range(6):
            p = copy.deepcopy(prob)
            p.select(i)
            score = run(p, storedVals=storedVals)
            if score > max_score:
                max_score = score
                max_loc = i
        prob.select(max_loc)
        storedVals[eqClass] = max_loc
        return f"select {max_loc}"
    else:
        pstay = copy.deepcopy(prob)
        pstay.stay()
        bestscore = run(pstay, storedVals=storedVals)
        bestAct = 6
        for i in range(6):
            if (not prob.array[i] == 0):
                numsteps = min((i - prob.loc)%6, (prob.loc - i)%6)
                if numsteps < prob.array[i]:
                    pswipe = copy.deepcopy(prob)
                    pswipe.iswipe(i)
                    sswipe = run(pswipe, storedVals=storedVals)
                    if sswipe > bestscore:
                        bestscore = sswipe
                        bestAct = i
        if bestAct == 6:
            prob.stay()
            storedVals[eqClass] = 6
            return "stay"
        else:
            loc = encode(bestAct, flipped, prob.loc)
            prob.iswipe(bestAct)
            storedVals[eqClass] = loc
            return f"swipe {bestAct}" 

def encode(value, flipped, location):
    loc = (value - location) % 6
    if flipped:
        loc = 5 - loc
    return loc

def decode(value, flipped, location):
    if flipped:
        value = 5 - value
    loc = (value + location) % 6
    return loc

def run(prob, printing = False, storedVals = {}):
    while not prob.array == [0]*6:
        k=act(prob, storedVals)
        if printing:
            print(k)
            # print(prob.eqClass())
        
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
    # print(p.eqClass()[0])
    # p.select(3)
    # print(p.eqClass()[0])
    print(run(p, printing=True))
    
    # print(decode(encode(5, True, 4), True, 4))


