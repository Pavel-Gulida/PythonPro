# vse za 26:37
def task(l):
    top = 0
    local_depth = 0
    depth=0
    for i in range(len(l)):
        if(l[i] > top):
            top = l[i]
        if (l[i] == top):
            depth=local_depth
        if(top - l[i] > local_depth):
            local_depth = top - l[i]
    return depth

print(task([6,1,2,2,3,0,1,5,6,7,5,8,1]))