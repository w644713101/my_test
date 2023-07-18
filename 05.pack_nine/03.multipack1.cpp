
/*
多重背包和01背包和完全背包的区别就是，每个物品的个数有所限制
v, w, s

数据范围
0<N,V≤100
0<vi,wi,si≤100

可以用O(n3)做

f[i] 表示总体积是i的情况下，最大价值是多少
*/
for (int i = 0; i < n; i++)
    for (int j = m; j >= 0; j--)  // 从大到小
        for (int k = 1; k <= s[i] && k * v[i] <= j; k++)  // 假如每个物品有s个
            f[j] = max(f[j], f[j - k*v] + k * v[i]
