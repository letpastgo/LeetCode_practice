/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target , int* returnSize){
    
    struct h_table
    {
       int index;
       int value; 
       UT_hash_handle hh;  
    };
    
    /*struct h_table *table = (struct h_table *)malloc(numsSize*sizeof(struct h_table)); */
    struct h_table *table = NULL;
    struct h_table *s;
    int *ret = (int *)malloc(2 * sizeof(int));
    int i , complement;
    
    for(i = 0 ; i < numsSize ;  i++)
    {
        complement = target - nums[i];
        HASH_FIND_INT(table , &complement , s);
        if(s)
        {
            ret[0] = s->index;
            ret[1] = i;
            break;
        }
        else
        {
            if(!s)
                s = (struct h_table *)malloc(sizeof(struct h_table));
                s->index = i;
                s->value = nums[i];
            HASH_ADD_INT(table , value , s);
        }
            
    }
    
            
    *returnSize = 2;
    return ret;
}
