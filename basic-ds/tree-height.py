# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.heights = [0]*self.n
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight
        def find_height(self, vertex):
                if not self.heights[vertex]:
                        self.heights[vertex] = 1 if self.parent[vertex] == -1 else 1 + self.find_height(self.parent[vertex])
                return self.heights[vertex]
        def compute_height_fast(self):
                maxHeight = 0
                for vertex in range(self.n):
                        maxHeight = max(maxHeight, self.find_height(vertex))
                return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_fast())

threading.Thread(target=main).start()
