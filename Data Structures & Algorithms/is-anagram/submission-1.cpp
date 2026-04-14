class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> m;

        for (int i = 0; i < s.size(); i++) {
            m[s[i]] += 1;
        }

        for (int i = 0; i < t.size(); i++) {
            m[t[i]] -= 1;
        }

        for (auto it : m) {
            if (it.second != 0) return false;
        }

        return true;
    }
};