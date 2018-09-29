from typing import Tuple
import copy

class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1


def add(root, word: str):

    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node

    node.word_finished = True


def findRoot(root, word: str) -> str:#Tuple[bool, int, str]:

    wordRoot = []
    temp = []
    node = root

    if not root.children:
        return False, 0

    for char in word:
        char_not_found = True

        for child in node.children:
            if child.char == char:
                char_not_found = False
                temp.append(char)
                #print(char)
                node = child
                if node.word_finished == True:
                    wordRoot = copy.copy(temp)
                break

        if char_not_found:
            return wordRoot#False, 0, wordRoot

    return wordRoot#True, node.counter, wordRoot


def fillTrie(root):
    inF = open(r'root.txt', 'r')

    data = inF.readlines()
    data = [x.strip() for x in data]

    for d in data:
        add(root, d)

if __name__ == "__main__":

    root = TrieNode('*')

    fillTrie(root)

    print("".join(findRoot(root, 'hesaplaşma')))
