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



# 区間[l,r) の和に対する遅延評価.
# ノード k は区間[l,r) に対応するノードの番号を与える.
# (ノード k と区間[l,r)の対応が取れていない場合の動作は何も保証しないので注意.)
def eval_lazy( k, l, r, node_list, lazy_list):
    if lazy_list[k] == 0:
        return
    node_list[k] += lazy_list[k]
    if r - l > 1:  # ノード k が最下段出ない場合.
        left, right = get_childs(k)
        lazy_list[left] += lazy_list[k] // 2
        lazy_list[right] += lazy_list[k] // 2

        # 伝播が終わったので、自ノードの遅延配列を空にする
        lazy_list[k] = 0;
    return

# 区間[a,b) と区間[l,r)の共通部分に対して一様に x を加える,
# という計算の遅延評価版.
def add_lazy( a, b, x, k, l, r, node_list, lazy_list ):
    # 区間の遅延評価をして、lazy_list を空にしておく.
    eval_lazy(k, l, r, node_list, lazy_list)
    if b <= l or r <= a: # 交差した部分がない場合は何もしない
        return

    if a <= l and r <= b : # [l,r) が[a,b) に含まれる場合.
        lazy_list[k] += (r - l) * x
        eval_lazy( k, l, r, node_list, lazy_list)
    else:
        m = (l+r) // 2
        left, right = get_childs(k)
        add_lazy( a, b, x, left, l, m, node_list, lazy_list )
        add_lazy( a, b, x, right, m, r, node_list, lazy_list )
        node_list[k] = node_list[left] + node_list[right]
    return
        
def getsum( a, b, k, l, r, node_list, lazy_list ):
    if b <= l or r <= a: # 区間が交差していない場合.
        return 0;
    #  関数が呼び出されたら評価！
    eval_lazy( k, l, r, node_list, lazy_list)
    if a <= l and r <= b:
        return node_list[k]
    left, right = get_childs(k)
    m = (l+r) // 2
    vl = getsum(a, b, left, l, m, node_list, lazy_list)
    vr = getsum(a, b, right, m, r, node_list, lazy_list)
    return vl + vr

sample_list = [1,3,2,6, 5,4,7,9]
for i,v in enumerate(sample_list):
    set_seq( i, v, node_list )
print(node_list)
build_tree( 0, node_list )
print(node_list)

# x = query( 0, 7, node_list)  # 28
# x = query( 1, 7, node_list) # 27
# print(x)

update_list = [4,6,5,9,8]
# node_list = greedy_update(update_list)
# print(node_list)
lazy_list = [ 0 for _ in range(node_num) ]
print(lazy_list)
x = 3
k = 0
l,r = 0, SEQ_NUM
add_lazy( 0, 5, 3, k, l, r, node_list, lazy_list )
print(getsum( 0, SEQ_NUM, k, l, r, node_list, lazy_list ))
