#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst=[]
while True:
    
    element = input("Enter the element:")
    if element =='':
        break
        
    else:
        lst.append(element)
        for i in range(len(lst)-1):
            print(lst[i],end='')
            
            if lst[i+1]==lst[-1]:
                print(" and", lst[i+1],end='')
                
            else:
                print(',', end='')
                


# In[ ]:







# In[ ]:





# In[ ]:




