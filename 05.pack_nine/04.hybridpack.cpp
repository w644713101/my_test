/*

有 N 种物品和一个容量是 V 的背包。

物品一共有三类：

第一类物品只能用1次（01背包）；
第二类物品可以用无限次（完全背包）；
第三类物品最多只能用 si 次（多重背包）；
每种体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

si=−1 表示第 i 种物品只能用1次；
si=0 表示第 i 种物品可以用无限次；
si>0 表示第 i 种物品可以使用 si 次；
输出格式
输出一个整数，表示最大价值。

数据范围
    0<N,V≤1000
    0<vi,wi≤1000
    −1≤si≤1000

混合背包是01背包和完全背包的混合，根据不同的类型判断枚举是从大到小还是从小到大
*/
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int v, w, s;
        cin >> v >> w >> s;
        if (s < 0) things.push_back({-1, v, w});  // s == -1 01背包
        else if (s == 0) things.push_back({0, v, w});  // s == 0 完全背包
        else  // s > 0 有限次，多重背包，二进制优化
        {
            for (int k = 1; k <= s; k *= 2)
            {
                s -= k;
                things.push_back({-1, v * k, w * k});
            }
            if (s > 0) things.push_back({-1, v * s, w * s});
        }
    }

    for (auto thing : things)
    {
        if (thing.kind < 0)  // 01背包
        {
            for (int j = m; j >= m; j++) f[j] = max(f[j], f[j - things.v]+thins.w);
        }
        else
        {
            for (int j = things.v; j <= m; j--) f[j] = max(f[j], f[j - things.v]+things.w);
        }
    }

    cout << f[m] << endl;
    return 0;
}






