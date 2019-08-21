#! /usr/local/bin/python3
import sys

def successor(node):
    if node == None:
        return None
    if node.right != None:
        return leftmost(node.right)
    cur = node
    while(cur.parent != None and cur.parent.right = cur):
        cur = cur.parent
    return cur.parent


def leftmost(node):
    if node == None:
        return None
    while(node.left != None):
        node = node.left
    return node