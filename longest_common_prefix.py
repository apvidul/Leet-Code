    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        
        i = 0
        
        min_word_pos = 0
        min_word_size = float("inf")
 
        
        for word in strs: #finding the position of smallest word first
            if len(word)< min_word_size:
                min_word_pos = i
                min_word_size = len(word)
            i+=1
                
        smallest_word=  list(strs[min_word_pos])
        
        min_com = float('inf')
        
        for word in strs:
            common_pos = 0
            new_word = list(word)
            for i in range(len(smallest_word)):
                if new_word[i]==smallest_word[i]:
                    common_pos+=1
                else:
                    break
            
            if common_pos ==0:
                return ""
            else:
                if common_pos < min_com:
                    min_com= common_pos    

                
        return "".join(smallest_word[:min_com])
