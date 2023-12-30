s = "0100"


s = list(s)

k = j = len(s)//2

count= 0
for i in range(len(s)):
    if k == 0 and j == len(s)-1 : break
    print(count)
    if k>1 :
        if s[k]==s[k-1]:
            if s[k-1] =="0":
               
                count +=1
                
            if s[k-1] == "1":
         
                count+=1
            k -=1
        else:
            k -=1
            
    if j < len(s)-1:        
        if s[j]==s[j+1]:
            if s[j+1] =="0":
                
   
                count +=1
                
            if s[j+1] == "1":
           
                count+=1
            j+=1    
                
        else:
            j+=1        
            
print(count)

print(s)