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

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;

        ListNode * dummy = new ListNode(-1);
        ListNode* prev = dummy;
        while (l1 || l2 || carry) {
            int sum = carry;

            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            if (sum > 9) {
                carry = sum/10;
                sum %= 10;
            }
            else{
                carry = 0;
            }

            auto node = new ListNode(sum);
            prev->next = node;
            prev = node;
        }

        return dummy->next;
    }
};
