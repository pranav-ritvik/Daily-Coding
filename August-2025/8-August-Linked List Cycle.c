bool hasCycle(struct ListNode *head) {
    if(head == NULL){return 0;}
    struct ListNode* big = head;
    struct ListNode* baby = head;
    do{
    if(big -> next == NULL || big -> next -> next == NULL){
        return 0;
    }
    big = big -> next -> next;
    baby = baby -> next;
    }while(big!=baby);
    return 1;
}
