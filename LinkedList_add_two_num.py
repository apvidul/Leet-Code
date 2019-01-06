# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count1=0
        count2=0
        #**************Finding the larger of the two lists*************
        ptr = l1
        while(ptr!=None):
            count1+=1
            ptr = ptr.next
        
        ptr = l2
        while(ptr!=None):
            count2+=1
            ptr = ptr.next
            
        #*********************When List 1 is larger****************************************
        summ = carry = 0
        
        head1 = l1
        head2 = l2
        
        if count1>count2:
            while(l2!=None):

                summ = l1.val + l2.val + carry

                if summ/10 == 1:
                    carry = 1
                    l1.val = summ % 10
                else:
                    carry = 0
                    l1.val = summ 
                    
                l1=l1.next
                l2=l2.next
        
            while(carry!=0):
                if l1 ==None:
                    node = ListNode(1)
                    end.next = node
                    return head1
                l1.val = l1.val + 1 
                
                if l1.val/10 ==1:
                    carry = 1
                    l1.val = l1.val%10
                    end=l1
                    l1= l1.next
                else:
                    carry = 0
            return head1
        #*********************When both list are of same size*******************************   
        
        elif count1==count2:

            while(l2!=None):
                
                summ = l1.val + l2.val + carry
    

                if summ/10 == 1:
                    carry = 1
                    l1.val = summ % 10
                else:
                    carry = 0
                    l1.val = summ 
                    
                print l1.val
                    

                l2=l2.next
                end = l1
                l1=l1.next
                
            if carry ==1:
                node = ListNode(1)
                end.next = node
                
            return head1
        
        #*********************When second list is larger***********************************
        elif count2>count1:
            while(l1!=None):
                summ = l1.val + l2.val + carry

                if summ/10 == 1:
                    carry = 1
                    l2.val = summ % 10
                else:
                    carry = 0
                    l2.val = summ 
                    
                    
                l1=l1.next
                l2=l2.next
                
            while(carry!=0):
                if l2 ==None:
                    node = ListNode(1)
                    end.next = node
                    return head2
                l2.val = l2.val + 1 
                
                if l2.val/10 ==1:
                    carry = 1
                    l2.val = l2.val%10
                    end =l2
                    l2 = l2.next
                else:
                    carry = 0
            return head2
                    
                    

                

            
    
    
                
            

                    
                    
            
    
            
            
            
            
        
