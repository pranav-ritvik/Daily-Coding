/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int num) {
        while(head!=null && head.val == num){
            head = head.next;
        }
        ListNode current = head;
        while(current != null && current.next != null){
            if(current.next.val == num){
                current.next = current.next.next;
            }else{
                current = current.next;
            }
        }
        return head;
    }
}
