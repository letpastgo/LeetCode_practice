/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target , int* returnSize){
    
    int *ret =(int *)malloc(2*sizeof(int));
    
    int sum = 0;
    int i , j;
    for(i = 0 ; i < numsSize ; i++)
    {
        for(j = i + 1 ; j < numsSize ; j++)
        {
            sum = nums[i] + nums[j];
            if(sum == target)
            {
                returnSize[0]=2;
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }  
    }
        

    return 0;
}
