graph={
 'F':({'C':8,'D':14},0),'E':({'B':11,'C':11},10),'D':({'A':5,'C':6,'F':14},5),
 'C':({'A':12,'E':11,'F':8},5),'B':({'A':10,'E':11},15),'A':({'B':10,'C':12,'D':5},10)
}

def greedy(g,dst,path,q):
    for n in g[path[-1]][0]:
        if n not in path: q[n]=g[n][1]
    if not q: return []
    mn=min(q,key=q.get); del q[mn]
    return path+[mn] if mn==dst else greedy(g,dst,path+[mn],q)

print("Greedy Path:", "->".join(greedy(graph,"F",["A"],{})) or "Not found")
