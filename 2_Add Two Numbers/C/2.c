/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    
    int plus = 0;
    int res;
    struct ListNode* head = NULL;
    struct ListNode* cur = NULL;
    
    int first = 0;
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
        
        if(first == 0)
        {
            head = (struct ListNode *)malloc(sizeof(struct ListNode));
            head->val = res;
            head->next = NULL;
            cur = head;
            first = 1;
        }
        else 
        {
            cur->next = (struct ListNode *)malloc(sizeof(struct ListNode));
            cur = cur->next;
            cur->val = res;
            cur->next = NULL;
        }
        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    }
    if(plus!=0)
    {
        cur->next = (struct ListNode *)malloc(sizeof(struct ListNode));
        cur = cur->next;
        cur->val = plus;
        cur->next = NULL;
    }

    return head;
}
