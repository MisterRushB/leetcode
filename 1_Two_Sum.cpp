#include <iostream>
#include <vector>

class Solution {
    
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> sol;
        bool found=false;
        for (int i=0;i<nums.size();i++){ 
            for (int j=0;j<nums.size();j++){ 
                if (i!=j){ 
                   if(nums[i]+nums[j]==target){ 
                       sol.push_back(i); 
                        sol.push_back(j); 
                        found=true;
                   }
                  
                }
                
            }
            if (found==true){ 
                break;
            }
        }
        return sol;
    }
};
