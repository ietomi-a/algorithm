# coding: utf-8

# 以下のようなツリー.
#             0
#      1             2
#   3     4       5      6
# 7  8  9  10   11 12  13 14
#
# 葉である 7, 8, 9,10,11,12,13,14 のノードの列を
# 0,1,2,3, 4,5,6,7 のインデックスをもつ配列として考える.


tree_depth = 4
SEQ_NUM = 2 ** (tree_depth -1)
node_num = 2 ** tree_depth - 1
node_list = [ None for _ in range(node_num) ]
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


assert get_parent( 9 ) == 4
assert get_parent( 0 ) < 0  # root であることはこれでも判定できる.
assert get_childs( 5 ) == (11,12)

# ここから上は node インデックスに対する操作.
# --------------------------------------------------------

# 葉の値が全て与えられたとして、それに基づく
# sum 演算に対するセグメントツリーを構築し、指定したノードにおける値を返す.
def build_tree( n, node_list ):
    if node_list[n]:
        return node_list[n]
    else:
        left, right = get_childs( n )        
        l_v = build_tree( left, node_list )
        r_v = build_tree( right, node_list )
        node_list[n] = l_v + r_v
        return node_list[n]

# 葉の値を設定する.
def set_seq( i, v, node_list ):
    n = get_node( i )
    node_list[n] = v
    return


# [a,b) と区間[l,r) の共通部分の総和を返す
# ノード k は区間[l,r) に対応するノードの番号を与える.
# (ノード k と区間[l,r)の対応が取れていない場合の動作は何も保証しないので注意.)
def query_core( a, b, k, l, r, node_list):
    if r <= a or b <= l: # クエリの区間と区間[l,r)が交差しない場合.
        return 0
    if a <= l and r <= b: # クエリの区間に区間[l,r) が含まれる場合.
        return node_list[k]
    left, right = get_childs(k)
    
    vl = query_core( a, b, left, l, (l+r)//2, node_list )
    vr = query_core( a, b, right, (l+r)//2, r, node_list )    
    return  vl + vr

# 区間[a,b) から最小値を探す.
def query( a, b, node_list):
    k = 0
    l, r = 0, SEQ_NUM
    ret = query_core( a, b, k, l, r, node_list )
    return ret


sample_list = [1,3,2,6, 5,4,7,9]
for i,v in enumerate(sample_list):
    set_seq( i, v, node_list )
print(node_list)
build_tree( 0, node_list )
print(node_list)

# x = query( 0, 7, node_list)  # 28
# x = query( 1, 7, node_list) # 27
# print(x)

# 更新. 更新に対する処理をまだ考えていない。。
node_list = [ None for _ in range(node_num) ]
for i,v in enumerate(sample_list):
    set_seq( i, v, node_list )
update_list = [4,6,5,9,8]
for i,v in enumerate(update_list):
    set_seq( i, v, node_list )
build_tree( 0, node_list )
print(node_list)
