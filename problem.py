class Problem:
    def __init__(self, targets):
        self.array = [0]*6
        self.loc = 6
        self.score = 0
        count = 0
        for target in targets:
            self.array[target] = count + 7
            count += 1
    
    # def __init__(self, prob):
    #     self.array = prob.array
    #     self.loc = prob.loc
    #     self.score = prob.score

    def __str__(self):
        return f"Player is at: {self.loc}, and has scored {self.score} points, States: {self.array}"
    
    def stay(self):
        self.array = list(map(lambda x: x if x == 0 else x - 1,self.array))

    def copy(self):
        p = Problem([])
        p.array = self.array
        p.loc = self.loc
        p.score = self.score 
        return p

    def select(self, state):
        if self.loc == 6:
            self.loc = state 
            self.stay()

    def swipe(self):
        if not self.array[self.loc] == 0:
            if 7 > self.array[self.loc]:
                self.score += (7 - self.array[self.loc])**2 
            self.array[self.loc] = 0
    
    def iswipe(self, loc):
        dist = (self.loc - loc)%6
        if dist < 3:
            for i in range(dist):
                self.left()
            self.swipe()
        else:
            for i in range(6 - dist):
                self.right()
            self.swipe()

    def left(self):
        self.loc = (self.loc - 1)%6
        self.stay()  

    def right(self):
        self.loc = (self.loc + 1)%6
        self.stay()  

    def eqClass(self):
        if self.loc == 6:
            return tuple(self.array + [0]), False
        sig = self.array[self.loc:] + self.array[:self.loc]
        small = list(filter(lambda x: x != 0, sig))
        if len(small) > 1 and (small[0] > small[-1]):
            sig.reverse()
            t = tuple(sig)
            return t, True
        t = tuple(sig)
        return t, False
        



