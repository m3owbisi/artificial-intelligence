import random

dist=[[0,2,9,10],[2,0,6,4],[9,6,0,3],[10,4,3,0]]

def cost(tour): return sum(dist[tour[i-1]][tour[i]] for i in range(len(tour)))

def neighbour(t): a,b=random.sample(range(len(t)),2); t[a],t[b]=t[b],t[a]; return t

def hill_climb():
    cur=random.sample(range(4),4); cur_cost=cost(cur)
    for _ in range(10):
        n=neighbour(cur[:]); n_cost=cost(n)
        if n_cost<cur_cost: cur,cur_cost=n,n_cost
    return cur, cur_cost

t,c=hill_climb()
print("Best tour:",t,"Cost:",c)
