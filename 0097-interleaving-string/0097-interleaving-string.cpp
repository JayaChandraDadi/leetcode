class Solution {
public:
    int m = 0;
    int n = 0;
    int l = 0;
    map<pair<int,int>,int>dp;
    int solve(int i, int j, int k , string s1, string s2, string s3)
    {
        if(k == l) return 1;

        if (dp.count({i,j})) 
            return dp[{i,j}];

        int ans = 0;

        if (i < n and s1[i] == s3[k] )
            ans = ans or solve(i+1, j, k+1, s1, s2, s3);
        if (j < m and s2[j] == s3[k])
            ans = ans or solve(i, j+1, k+1, s1, s2, s3);

        dp[{i,j}] = ans;

        return ans;

    }
    bool isInterleave(string s1, string s2, string s3) {
        
        dp.clear();
        n = s1.length();
        m = s2.length();
        l = s3.length();

        if(n+m != l) return false;
        return solve(0,0,0,s1,s2,s3);
    }
};