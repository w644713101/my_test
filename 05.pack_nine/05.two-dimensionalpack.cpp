/*
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。

每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。

输入格式
第一行三个整数，N,V,M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。

接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
    0<N≤1000
    0<V,M≤100
    0<vi,mi≤100
    0<wi≤1000

二维费用的背包问题，就是01背包问题出了要考虑体积以外，还要考虑重量的问题

*/
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 110;

int n, v, m;
int f[N][M];

int main()
{
    cin >> n >> v >> m >> ;  // n 是物品个数 v是容量 m是重量
    for (int i = 0; i < n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;  // a 是当前物品的体积， b是当前物品的重量， c是当前物品的价值
        for (int j = v; j >= a; j --)
        {
            for (int k = m; k >= b; k --)
                f[j][k] = max(f[j][k], f[j - a][k - b] + c)
        }
    }

    cout << f[v][m] << endl;
    return 0;
}





