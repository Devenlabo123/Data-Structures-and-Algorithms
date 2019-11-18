# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:06:30 2019

@author: Deven
"""


def hash_search(current_hash, val):
    i = 0
    o = 11
   # j = make_hash(current_hash, val * o)
    j = None
    if val == None:
        return
    while i != len(current_hash) or current_hash[j] == None:
        j = make_hash(current_hash, val * o)
        if current_hash[j] == val:
            return j
        i = i + 1
        o = o + 1
    print('value not found')
  #  return None
         
def hash_insert(current_hash, val):
        
    if check_for_increase(current_hash):
        print('doubling length')
        double_length(current_hash)
        
        
    i = 0
    o = 11
    while i != len(current_hash):
        j = make_hash(current_hash, val * o)
        if current_hash[j] == None or current_hash[j] == val:
            current_hash[j] = val
            return j
        i = i + 1
        o = o + 1
    
    print('hash overflow')
    return
    
    
     #   hash_insert(current_hash, val)
    #### Double length of table #####
    
def make_hash(current_hash, s):
    return hash(str(s)) % len(current_hash)


def delete_value(current_hash, val):
    
    del_index = hash_search(current_hash, val)
    
    
    if del_index:
        current_hash[del_index] = 'DELETED'
    else:
        print('Value could not be deleted')
        
        
    if check_for_deletion(current_hash):
        print('half length')
        halve_hash(current_hash)
   
    return

def check_for_increase(current_hash):
    a = num_inserts(current_hash)
    
    if a > (len(current_hash) / 2):
        return True
    else:
        return False
    
      
def num_inserts(current_hash):
    num = 0
    for i in range(len(current_hash)):
        if current_hash[i] != None:
            num = num + 1
    return num

def double_length(current_hash):
    a = {}
    for i in range(len(current_hash)):
        a[i] = current_hash[i]
 #   current_hash = {}
    
    for i in range(len(a) * 2):
        current_hash[i] = None
    
    for x in range(len(a)):
        if a[x] != None and a[x] != 'DELETED':
            hash_insert(current_hash, a[x])

    return
        
        
def num_deletions(current_hash):
    num = 0
    for i in range(len(current_hash)):
        if current_hash[i] == 'DELETED':
            num = num + 1
    return num
        
def check_for_deletion(current_hash):
    a = num_deletions(current_hash)

    if a > (len(current_hash) / 4):
        return True
    else:
        return False
    
def halve_hash(current_hash):
    a = {}
    
    len_current = len(current_hash)
    half_length = int(len_current/2)
    
    for i in range(len(current_hash)):
        a[i] = current_hash[i]
    
    
    for i in range(half_length + 1):
        current_hash[i] = None
    
    for i in range(half_length + 1, half_length * 2 ):
        del current_hash[i]
    
    for i in range(0, len(a)):
        if a[i] != None and a[i] != 'DELETED':
            print('added ' + str(a[i]))
            hash_insert(current_hash, a[i])
    return

#def resize_table(current_hash):


d = {}

for i in range(5):
    d[i] = None

print('insert 2')  
hash_insert(d, 2)
print(d)

print('insert 434')
hash_insert(d, 434)
print(d)

print('insert 22332')
hash_insert(d, 22332)
print(d)

print('insert 1234')
hash_insert(d, 1234)
print(d)

print('insert 9')
hash_insert(d, 9)
print(d)

print('insert 34352')
hash_insert(d, 34352)
print(d)


#delete_value(d, 54563)
print('delete 434')
delete_value(d, 434)
print(d)

print('delete 434')
delete_value(d, 34352)
print(d)

print('delete 22332')
delete_value(d, 22332)
print(d)
print()
print('second test')
import random

test_hash = {}
for i in range(5):
    test_hash[i] = None

for i in range(50):
   # test_hash[i] = random.randrange(1, 101, 1)
   r = random.randrange(1, 101, 1)
   print('insert: ' + str(r) )
   hash_insert(test_hash, r)
   print(test_hash)
   
for i in range(42):
   # test_hash[i] = random.randrange(1, 101, 1)
   print('Delete: ' + str(test_hash[i]) )
   delete_value(test_hash, test_hash[i])
   print(test_hash)
   
print(test_hash)
