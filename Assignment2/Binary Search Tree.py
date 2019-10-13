class Node:
    def __init__(self, val):
        self.parent = None
        self.l_child = None
        self.r_child = None
        self.data = val
        
#### 12.1-4 ####
def post_order_print(root):
    if not root:
        return        
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    print(root.data)
    
#### 12.1-4 ####
def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


#### 12.2-2 ####
def tree_min(parent_node):
    while parent_node.l_child != None:
       parent_node = parent_node.l_child       
   
    return parent_node

#### 12.2-2 ####
def tree_max(parent_node):
    while parent_node.r_child != None:
       parent_node = parent_node.r_child

    return parent_node


#### 12.2-3 ####
def predecessor(root, value):
    pred_node = binary_search(root, value)
    
    if value == tree_min(root).data:
        return tree_min(root)
    
    elif pred_node.l_child is not None:
        return tree_max(pred_node.l_child)
   
    
    parent = pred_node.parent
    child = pred_node
    
    
    while parent is not None and child is parent.l_child:
        if(parent.data == root.data):
            return child
        child = parent
        parent = child.parent
        
    return parent

 #### 12.3-1 ####
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                node.parent = root
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                node.parent = root
                root.r_child = node
            else:
                binary_insert(root.r_child, node)
   
 #### 12.3-1 ####                
def tree_delete_transplant(delete_node):
    if delete_node.l_child is None:
        transplant(delete_node, delete_node.r_child)
    elif delete_node.r_child is None:
        transplant(delete_node, delete_node.l_child)
    else:
        y = tree_min(delete_node.r_child)
        
        if y.parent is not delete_node:
            transplant(y, y.r_child)
            y.r_child = delete_node.r_child
            y.r_child.parent = y
        
        transplant(delete_node,y)
        y.l_child = delete_node.l_child
        y.l_child.parent = y
    
 #### 12.3-1 ####   
def transplant(delete_node, delete_node_child):
    if delete_node.parent is None:
        delete_node = delete_node_child
    elif delete_node is delete_node.parent.l_child:
        delete_node.parent.l_child = delete_node_child
    else:
        delete_node.parent.r_child = delete_node_child
        
    if delete_node_child is not None:
        delete_node_child.parent = delete_node.parent
    

#### 12.3-5 ####
def successor(root, value):
    pred_node = binary_search(root, value)

    if value == tree_max(root).data:
        return tree_max(root)
    
    elif pred_node.r_child is not None:
        return tree_min(pred_node.r_child)  
    
    parent = pred_node.parent
    child = pred_node
    
    while parent is not None and child is parent.r_child:
        child = parent
        parent = child.parent
        
    return parent
    
                
def binary_search(root, val):
    if root.data == val:
    #    print('value found on root')
        return root
    elif root.data > val:
      #  print('left')
        if root.l_child.data == val:
        #    print('value found on left')
            return root.l_child
        else:
            return binary_search(root.l_child, val)
     
    else:
     #   print('right')
        if root.r_child.data == val:
           # print('value found on right')
            return root.r_child
        else:
            return binary_search(root.r_child, val)
    

      
        
r = Node(23)
binary_insert(r, Node(12))
binary_insert(r, Node(34))    
binary_insert(r, Node(6))
binary_insert(r, Node(46))
binary_insert(r, Node(55))
binary_insert(r, Node(4))
binary_insert(r, Node(30))
binary_insert(r, Node(8))
binary_insert(r, Node(18))
binary_insert(r, Node(14))
binary_insert(r, Node(26))
binary_insert(r, Node(28))
binary_insert(r, Node(13))
binary_insert(r, Node(39))
binary_insert(r, Node(26))
binary_insert(r, Node(6))
binary_insert(r, Node(30))




print("tree min")
print(tree_min(r).data)
print()
print("tree max")
print(tree_max(r).data)
print()


print("Testing 28")
print("predecessor")
print(predecessor(r, 28).data)
print()

print("successor")
print(successor(r, 28).data)
print()

print("Testing 55 (Max Value)")
print("predecessor")
print(predecessor(r, 55).data)
print()

print("successor")
print(successor(r, 55).data)
print()

print("Testing 4 (min value)")
print("predecessor")
print(predecessor(r, 4).data)
print()

print("successor")
print(successor(r, 4).data)
print()

print("Testing 26")
print("predecessor")
print(predecessor(r, 26).data)
print()

print("successor")
print(successor(r, 26).data)
print()

print("Testing 18")
print("predecessor")
print(predecessor(r, 18).data)
print()

print("successor")
print(successor(r, 18).data)
print()

print("post order")
post_order_print(r)
print()


print("pre order")
pre_order_print(r)

print()

print('Pre order after deleting 30')
a = binary_search(r,30)
tree_delete_transplant(a)

pre_order_print(r)
print()


print('Pre order after deleting 12')
a = binary_search(r,12)
tree_delete_transplant(a)

pre_order_print(r)

print()
print('Pre order after inserting 25')
binary_insert(r, Node(25))
pre_order_print(r)

print()
print('pre order after deleting 26')
a = binary_search(r,26)
tree_delete_transplant(a)
a = binary_search(r,26)
tree_delete_transplant(a)

pre_order_print(r)


'''         
def binary_delete(root, val):
    delete_node = binary_search(root, val)
    delete_node_parent = delete_node.parent
    
    ## if the node you want to delete does not have any children you can just remove it
    if delete_node.l_child is None and delete_node.r_child is None:
        if delete_node.data == delete_node_parent.l_child.data:
            delete_node_parent.l_child = None
        else:
            delete_node_parent.r_child = None
    
    ## if 
    elif delete_node.l_child is None or delete_node.r_child is None:
        if delete_node.r_child is None:
            if delete_node.data == delete_node_parent.l_child.data:
                delete_node_parent.l_child = delete_node.l_child
            else:
                delete_node_parent.r_child = delete_node.l_child
        else:
            if delete_node.data == delete_node_parent.l_child.data:
                delete_node_parent.l_child = delete_node.r_child
            else:
                delete_node_parent.r_child = delete_node.r_child
 #   else:
'''
