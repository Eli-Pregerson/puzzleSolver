from problem import Problem
import copy

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
    else:
        pstay = copy.deepcopy(prob)
        pstay.stay()
        sstay = run(pstay)
        sswipe = 0
        if not prob.array[prob.loc] == 0:
            pswipe = copy.deepcopy(prob)
            pswipe.swipe()
            sswipe = run(pswipe)
        pright = copy.deepcopy(prob)
        pright.right()
        sright = run(pright)

        pleft = copy.deepcopy(prob)
        pleft.left()
        sleft = run(pleft)

        if sswipe > sstay and sswipe > sright and sswipe >sleft:
            prob.swipe()
        elif sstay > sright and sstay >sleft:
            prob.stay()
        elif sright >sleft:
            prob.right()
        else:
            prob.left()

def run(prob, printing = False):
    while not prob.array == [0]*6:
        if printing:
            print(prob)
        act(prob)
    return prob.score

p = Problem([0, 3, 5, 4])
print(run(p, True))

