/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/*
use linked list and hash map package
algorithm : two-pass hash table
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
    
    for(i = 0 ; i < numsSize ; i++)
    {
        s = (struct h_table *)malloc(sizeof(struct h_table));
        s->index = i;
        s->value = nums[i];
        HASH_ADD_INT(table , value , s);
    }

    for(i = 0 ; i < numsSize ; i++)
    {
        complement = target -nums[i];
        HASH_FIND_INT(table , &complement , s);
        if(s && s->index != i)
        {
            ret[0] = i;
            ret[1] = s->index;
        }
    }
    
    struct h_table *cur, *tmp;
    HASH_ITER(hh , table , cur , tmp)
    {
        HASH_DEL(table , cur);
        free(cur);
    }
    
    
    *returnSize = 2;
    return ret;
        
}

