#define MOD 1000000007

typedef long long ll;

struct Node {
  Node *left, *right;
  ll v;
  Node() : left(nullptr), right(nullptr), v(0) {}
};

// Dynamic Segment Tree
class SegmentTree {
private:
  Node *root;
  int n; // 2のべきで n0 以上のものの最小値.
  int n0; // 要素数.

  // n は区間[l,r) を表す node でないとだめ。
  ll query( int a, int b, Node *n, int l, int r ){
    if( a <= l && r <= b ){ // [l,r) が [a,b) に含まれる場合.
      return n->v;
    }
    if( r <= a || b <= l ){ // 交差なし.
      return 0;
    }
    int m = (l + r) >> 1;
    ll lv = n->left ? query(a, b, n->left, l, m) : 0;
    ll rv = n->right ? query(a, b, n->right, m, r) : 0;
    return (lv + rv) % MOD;
  }

public:
  SegmentTree(int n) : n(n) {
    n0 = 1;
    while( n0 < n ){ n0 <<= 1; }
    root = new Node();
  }
  ~SegmentTree(){
    delete root;
    root = nullptr;
  }

  ll query(int a, int b) {
    return query(a, b, root, 0, n0);
  }

  ll lquery(int b) {
    return query(0, b, root, 0, n0);
  }

  ll rquery(int a) {
    return query(a, n0, root, 0, n0);
  }

  // インデックス k の配列に x を足す.
  void update( int k, ll x ){
    Node *n = root;
    int l = 0;
    int r = n0;
    n->v = (n->v + x) % MOD;
    while( r - l > 1 ){
      int m = (l + r) >> 1;
      if( k < m ){
        if( !n->left ){ n->left = new Node(); }
        n = n->left;
        r = m;
      } else {
        if( !n->right ){ n->right = new Node(); }
        n = n->right;
        l = m;
      }
      n->v = (n->v + x) % MOD;
    }
  }

};
