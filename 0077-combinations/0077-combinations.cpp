class Solution {
public:
    vector<vector<int>>mp;

    //1, 2, 3, 4


    void solve(int i, int n, int k, vector<int>&v)
    {
        if(v.size() > k) return;

        if(i == n) 
        {   
            if(v.size() == k)
                mp.push_back(v);
            return;
        }

        v.push_back(i+1);
        solve(i+1, n, k, v);
        v.pop_back();
        solve(i+1,n,k,v);
    }

    vector<vector<int>> combine(int n, int k) {
        mp.clear();
        vector<int>v;
        solve(0, n, k, v);
        return mp;
    }
};