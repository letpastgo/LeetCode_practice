class Solution {
public:
    bool CheckRepeat(string &str, int i, int j)
    {
        vector<int> vec_record(128);
        
        for(int idx = i ; idx <= j ; idx++)
        {
            vec_record[str[idx]]++;
            if(vec_record[str[idx]] > 1)
                return false;
        }
        return true;
    }
    
    int lengthOfLongestSubstring1(string s) {
        
        int n = s.length();
        int res = 0;
        for(int i = 0; i < n ; i++)
        {
            for(int j = 0 ; j < n ; j++)
            {
                if(CheckRepeat(s, i, j))
                    res = max(res, j - i + 1);
            }
            
        }
        
        return res;
    }


    int lengthOfLongestSubstring2(string s) {
        vector<int> chars(128);
        int left= 0;
        int right = 0;
        int res = 0;
        
        
        
        while(right < s.length())
        {
            char cr = s[right];
            chars[cr]++;
            while(chars[cr] > 1)
            {
                char cl = s[left];
                chars[cl]--;
                left++;
            }
            res = max(res, right - left + 1);
            right++;
        }
        return res; 
        
    }


    int lengthOfLongestSubstring3(string s) {
        vector<int> chars(128, -1);
        int left = 0;
        int right = 0;
        int res = 0;
        int index;
        
        while(right < s.length())
        {
            char c = s[right];
            index = chars[c];
            if(index != -1 && index >= left && index < right)
                left = index + 1;
            res = max(res, right - left + 1);
            chars[c] = right;
            right++;
        }
        return res; 
        
    }
};
