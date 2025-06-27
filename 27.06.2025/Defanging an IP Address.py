class Solution(object):
    def defangIPaddr(self, address):
        address2 = list(address) 
        output = []  
    
        for i in address2:
            if i == ".":
                output.extend(["[", ".", "]"])  
            else:
                output.append(i) 

        return ''.join(output) 

 

        
