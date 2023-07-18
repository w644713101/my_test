/*
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000

f[i][j] 表示只看前i个物品，总体积是j的情况下，总价值最大是多少

f[i][j]:  有两种情况

    1.不选第i个物品, f[i][j] = f[i - 1][j];
    2.选第i个物品, f[i][j] = f[i - 1][j - v[i]];

f[i][j] = max{1.  2.}
f[0][0] = 0;


*/

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, m;
int f[N][N];
int v[N], w[N];

int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i ++ ) cin >> v[i] >> w[i];

    for (int i = 1; i <= n; i ++)
        for (int j = 0; j <= m; j ++)
        {
            f[i][j] = f[i - 1][j];   // 因为i是从1开始遍历的，所以不会越界
            if (j >= v[i])
                f[i][j] = max(f[i][j], f[i - 1][j - v[i]]+w[i])
        }

    int res = 0;
    for (int i = 0; i <= m; i++) res = max(res, f[n][i]);

    count << res << endl;
    return 0
}


/*
讲f优化成1维数组
f[j] 代表体积为j时，总价值最大是多少
*/

int n, m;
int f[N];
int v[N], w[N];

int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i ++ ) cin >> v[i] >> w[i];

    for (int i = 1; i <= n; i ++)
        for (int j = m; j >= v[i]; j --)  // 这块控制的是能不能把 v[i]放进去
            f[j] = max(f[j], f[j - v[i]]+w[i])

    cout << f[m] << endl;
    /*
    之所以能f[m]作为最大值，是因为最开始初始化的是f[i]所有都是0
    而不是f[0] = 0

    这个初始化主要影响的是第 83 行，从最大容积遍历时，能不能拿到f[j-v[i]]+w[i]的值，
    若初始化是f[0] = 0 的话，第一次遍历只能给f[1] 赋值
    */
    return 0
}
