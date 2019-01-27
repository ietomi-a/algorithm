#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;

// __gnu_pbds の tree については以下のサイトを参考にせよ。
// http://hogloid.hatenablog.com/entry/2014/09/23/132440

struct SegmentTree
{
  int sz;
  vector< tree< int, null_type, less< int >, rb_tree_tag, tree_order_statistics_node_update > > seg;

  SegmentTree(int n)
  {
    sz = 1;
    while(sz < n) sz <<= 1;
    seg.resize(2 * sz - 1);
  }

  int query(int a, int b, int lower, int upper, int k, int l, int r)
  {
    if(a >= r || b <= l) {
      return (0);
    } else if(a <= l && r <= b) {
      return (seg[k].order_of_key(upper) - seg[k].order_of_key(lower));
    } else {
      return (query(a, b, lower, upper, 2 * k + 1, l, (l + r) >> 1) + query(a, b, lower, upper, 2 * k + 2, (l + r) >> 1, r));
    }
  }

  int query(int a, int b, int l, int r)
  {
    return (query(a, b, l, r, 0, 0, sz));
  }

  void update(int k, int x, bool type)
  {
    k += sz - 1;
    if(type) seg[k].insert(x);
    else seg[k].erase(x);
    while(k > 0) {
      k = (k - 1) >> 1;
      if(type) seg[k].insert(x);
      else seg[k].erase(x);
    }
  }
};

