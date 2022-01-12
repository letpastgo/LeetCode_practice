#include <iostream>
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;
using std::cout;
using std::vector;
using std::sort;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> rec_arr_vec(2);

    for(int i = 0; i < nums.size() ; i++)
    {
        for(int j = 0; j < nums.size() ; j++)
        {
            if((nums[i] + nums[j]) == target)
            {
                rec_arr_vec[0] = i;
                rec_arr_vec[1] = j;
                return rec_arr_vec;
            }
        }
    }
    return {};

}

vector<int> twoSum2(vector<int>& nums, int target) {
    vector<int> tmp, rec_arr_vec;

    tmp = nums;
    sort(tmp.begin(), tmp.end());

    int left = 0, right = tmp.size() - 1;
    int n1, n2;

    while(left <= right)
    {
        if((tmp[left] + tmp[right]) == target)
        {
            n1 = tmp[left];
            n2 = tmp[right];
            break;
        }
        if((tmp[left] + tmp[right]) > target)
            right -= 1;
        else
            left += 1;
    }

    for(int i = 0; i < nums.size(); i++)
    {
        if(nums[i] == n1)
            rec_arr_vec.emplace_back(i);
        else if(nums[i] == n2)
            rec_arr_vec.emplace_back(i);
    }

    return rec_arr_vec;

}

vector<int> twoSum3(vector<int>& nums, int target) 
{
    vector<int> rec_arr_vec;
    unordered_map<int, int> mp;
    
    for(int i = 0 ; i < nums.size(); i++)
    {
        if(mp.find(target - nums[i]) != mp.end())
        {
            rec_arr_vec.emplace_back(i);
            rec_arr_vec.emplace_back(mp[target - nums[i]]);
            return rec_arr_vec;
        }
        mp[nums[i]] = i; 
    }
    return rec_arr_vec;
}

//https://leetcode.com/problems/two-sum/discuss/1673447/3-approch-with-neat-explanation-must-see
int main()
{

    //Solution1: Brute Force
    vector<int> arr_vec(4);
    arr_vec = {2,7,11,5};
    vector<int> rec_arr_vec(2);


    //int target = 9;
    //rec_arr_vec = twoSum(arr_vec, target);

//    for(int i = 0; i < 2; i++)
//        cout << rec_arr_vec[i] << " ";

    //Solution2: Two-pass Hash Table

    int target = 9;
    rec_arr_vec = twoSum2(arr_vec, target);

    for(int i = 0; i < 2; i++)
        cout << rec_arr_vec[i] << " ";


    return 0;
}
