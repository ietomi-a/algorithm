
def find( x: int, par:list ):
    if par[x] == None:
        return x
    else:
        par[x] = find( par[x], par )
        return par[x]
    # 以下は par に何か想定外の事が起きている場合に生じる.
    return None

def is_same( x, y, par ):
    return find(x,par) == find(y, par)

def union( x, y , par ):
    x = find(x, par)
    y = find(y, par)
    if x == y: # すでに同じグループ.
        return
    par[x] = y
    return

node_num = 11
par = [ None for _ in range(node_num) ]
print(par)
a = find( 9, par )
print(a)

print(is_same( 9, 7, par))
union( 9, 7, par )
print(is_same( 9, 7, par))
