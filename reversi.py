#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install japanmap')
get_ipython().system('pip install matplotlib')
import matplotlib.pyplot as plt
import japanmap as jm
from japanmap import picture


# In[2]:


def gameinit():
    p1trt.clear()
    p2trt.clear()
    p1trt.extend([24,26])
    p2trt.extend([25,29])


# In[7]:


def colchange():
    mapcol.clear()
    for trt in p1trt:mapcol[trt]=p1col
    for trt in p2trt:mapcol[trt]=p2col


# In[8]:


def turn(prfname,player):
    prfnum=jm.pref_code(prfname)
    if (prfnum in p1trt) or (prfnum in p2trt):
        return False
    else:
        flg=False
        if(player==True):
            for revtrt in p2trt:
                for atktrt in jm.adjacent(revtrt):
                    if(revtrt in jm.adjacent(prfnum) and atktrt not in jm.adjacent(prfnum)):
                        if(prfnum not in p1trt):p1trt.append(prfnum)
                        p1trt.append(revtrt)
                        p2trt.remove(revtrt)
                        flg=True
                        break
        else :
            for revtrt in p1trt:
                for atktrt in jm.adjacent(revtrt):
                    if(revtrt in jm.adjacent(prfnum) and atktrt not in jm.adjacent(prfnum)):
                        if(prfnum not in p2trt):p2trt.append(prfnum)
                        p2trt.append(revtrt)
                        p1trt.remove(revtrt)
                        flg=True
                        break
        return flg


# In[9]:


def move():
    colchange()
    plt.imshow(picture(mapcol))


# In[10]:


def result():
    print(len(p1trt))
    print('vs')
    print(len(p2trt))


# In[11]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[12]:


def gamemain():
    gameinit()
    turnply=1
    while(1):
        if(turnply%2):
            print('player1s turn')
        else:
            print('player2s turn')
        print('put prefecture name or result or end')
        str=input()
        if(str=='result'):
            result()
            continue
        if(str=='end'):
            break
        else:
            ismove=turn(str,turnply%2)
            if(ismove):
                move()
                turnply+=1
            else:
                print('invalid input')


# In[16]:


p1trt=[]
p2trt=[]
p1col='Red'
p2col='Blue'
mapcol={}


# In[20]:


gamemain()

