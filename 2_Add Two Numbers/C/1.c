/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/*
search two linked list to find the sum of corresponding items
consider the possible of carry of the highest digit and unpaired digit  
*/

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    
    int plus = 0;
    int res;
    struct ListNode* head = NULL;
    struct ListNode** cur = &head;
    
    int val1,val2;
    while(1) 
    {
        if(!(l1 || l2))
            break;
        
        val1 = l1 ? l1->val : 0;
        val2 = l2 ? l2->val : 0;
        res = val1 + val2 + plus;
        if(res >= 10)
        {
            res-=10;
            plus = 1;
        }
        else
            plus = 0;
        
        *cur = (struct ListNode *)malloc(sizeof(struct ListNode));
        (*cur)->val = res;
        (*cur)->next = NULL;
        cur = &(*cur)->next;
        
        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    }
    if(plus!=0)
    {
        *cur = (struct ListNode *)malloc(sizeof(struct ListNode));
        (*cur)->val = plus;
        (*cur)->next = NULL;
    }

    return head;
}

