#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    word = input("Enter a word: ")
    if word == "Bon":
        print("Voyage")
        break


# In[ ]:


value = 0
while True:
    value  = value + 50
    print("Current value:", value)
    if value > 300:
        print("Value exceeded 300. Breaking the loop.")
        break


# In[ ]:


n = input('enter name')
for i in n:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    else:S
        print(i)


# In[ ]:


address = input("enter your address ")
print("numbers are")
for ch in address:
    if ch >= '0' and ch <= '9':
        print(ch, end='')

