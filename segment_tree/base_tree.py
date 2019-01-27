# coding: utf-8

# 以下のようなツリー.
#             0
#      1             2
#   3     4       5      6
# 7  8  9  10   11 12  13 14
#
# 葉である 7, 8, 9,10,11,12,13,14 のノードの列を
# 0,1,2,3, 4,5,6,7 のインデックスをもつ配列として考える.


BIG_INT = 2**32-1  # この数値以下のものを取り扱う.
tree_depth = 4
SEQ_NUM = 2 ** (tree_depth -1)
node_num = 2 ** tree_depth - 1
node_list = [ BIG_INT for _ in range(node_num) ]
# print(node_list)
#exit(1)

def get_parent( n ):
    return (n-1) // 2

def get_childs( n ):
    return 2*n+1, 2*n+2

def is_root( n ):
    return n == 0

def get_node( i ):
    # 葉である 7, 8, 9,10,11,12,13,14 のノードの列を
    # 0,1,2,3, 4,5,6,7 のインデックスをもつ配列として考える.
    n = i + SEQ_NUM - 1
    return n

def update( i, v, node_list ):
    n = get_node( i )
    node_list[n] = v
    while not is_root( n ):
        n = get_parent( n )
        left, right = get_childs( n )
        node_list[n] = min( node_list[left], node_list[right] )
    return


# [a,b) と区間[l,r) の共通部分からの最小値を返す.
# ノード k は区間[l,r) に対応するノードの番号を与える.
# (ノード k と区間[l,r)の対応が取れていない場合の動作は何も保証しないので注意.)
def query_core( a, b, k, l, r, node_list):
    if r <= a or b <= l: # クエリの区間と区間[l,r)が交差しない場合.
        return BIG_INT
    if a <= l and r <= b: # クエリの区間に区間[l,r) が含まれる場合.
        return node_list[k]
    left, right = get_childs(k)
    m = (l+r)//2
    vl = query_core( a, b, left, l, m, node_list )
    vr = query_core( a, b, right, m, r, node_list )    
    return min( vl, vr )

# 区間[a,b) から最小値を探す.
def query( a, b, node_list):
    k = 0
    l,r = 0, SEQ_NUM
    ret = query_core( a, b, k, l, r, node_list )
    return ret


assert get_parent( 9 ) == 4
assert get_parent( 0 ) < 0  # root であることはこれでも判定できる.
assert get_childs( 5 ) == (11,12)

sample_list = [5,3,7,9, 1,4,6,2]
for i,v in enumerate(sample_list):
    update( i, v, node_list )
# print(node_list)


assert query( 0, 4, node_list) == 3
assert query( 2, 4, node_list) == 7
assert query( 2, 5, node_list) == 1
