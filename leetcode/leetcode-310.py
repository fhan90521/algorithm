class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:
            return [0]
        
        node_dict=collections.defaultdict(list)

        for edge in edges:
            node_dict[edge[0]].append(edge[1])
            node_dict[edge[1]].append(edge[0])
        leaf=[]
        for i in range(n):
            if len(node_dict[i])==1:
                leaf.append(i)
        while n>2:
            n-=len(leaf)
            new_leaf=[]
            for node in leaf:
                parent = node_dict[node].pop()
                node_dict[parent].remove(node)
                if len(node_dict[parent])==1:
                    new_leaf.append(parent)
            leaf=new_leaf
            
        return leaf