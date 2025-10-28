/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode small = head;
        ListNode big = head;
        while(big!=null && big.next!=null){
            big = big.next.next;
            small = small.next;
            if(small==big){
                return true;
            }
        }
        return false;
    }
}
