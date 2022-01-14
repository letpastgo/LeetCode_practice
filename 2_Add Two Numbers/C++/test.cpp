/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

https://leetcode.com/problems/add-two-numbers/solution/

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        /*Solution1*/
        ListNode *l3 = new ListNode(0);
        ListNode *head = l3;
        int sum = 0;
        
        while(true)
        {
            int sum = l3->val;
            if(l1 != NULL)
            {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL)
            {
                sum += l2->val;
                l2 = l2->next;
            }
            l3->val  = sum%10;
            if(l1 == NULL && l2 == NULL && sum < 10)
                break;
            l3->next = new ListNode(sum /= 10);
            l3 = l3->next;
        }
        
        return head;
      
        /*Solution2*/
        int sum = 0;
        ListNode *l3 = NULL;
        ListNode **Node = &l3;
        
        while(l1 != NULL || l2 != NULL || sum >0 )
        {
            if(l1 != NULL)
            {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL)
            {
                sum += l2->val;
                l2 = l2->next;
            }
            *Node = new ListNode(sum%10);
            sum /= 10;
            
            Node = &((*Node)->next);
        }
        return l3;
      
        /*Solution3*/
        ListNode* ln = NULL;
        int val = 0;
        while (l1 || l2 || val)
        {
          if (l1)
          {
              val += l1->val;
              l1 = l1->next;
          }

          if (l2)
          {
              val += l2->val;
              l2 = l2->next;
          }

          ListNode* newNode = new ListNode(val % 10);

          if (ln == NULL)
              ln = newNode;
          else
          {
              ListNode* head = ln;
              while (ln->next)
                  ln = ln->next;

              ln->next = newNode;
              ln = head;
          }

          val = val / 10;

      }

      return ln;
    }
};
