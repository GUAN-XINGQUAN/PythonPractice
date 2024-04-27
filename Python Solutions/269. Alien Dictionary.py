class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not self.validateArguments(words):
            return ""
        charSet = self.getAllChar(words)
        order = self.getOrder(words)
        node2Indegree, node2Neighbors = self.constructGraph(charSet, order)
        result = self.topologicalSort(node2Indegree, node2Neighbors)
        return result

    def validateArguments(self, words: list[str]) -> bool:
        if not words:
            return False
        for idx in range(1, len(words)):
            wordA, wordB = words[idx-1], words[idx]
            # "abcd", "abc"
            if wordA.startswith(wordB) and len(wordA) > len(wordB):
                return False
        return True
    
    def getAllChar(self, words:list[str]) -> set[str]:
        """
        time complexity: O(word_list_length * word_length)
        """
        charSet = set()
        for idx in range(len(words)):
            for i in range(len(words[idx])):
                charSet.add(words[idx][i])
        return charSet
    
    def getOrder(self, words: list[str]) -> list[tuple]:
        """
        words = ["wrt", "wrf", "er"]
        return = [("t", "f"), ("w", "e")]

        time complexity: O(word_list_length * word_length)
        """
        order = []
        for idx in range(1, len(words)):
            wordA, wordB = words[idx-1], words[idx]
            comp = self.compareTwoWords(wordA, wordB)
            if comp is None:
                continue
            order.append(comp)
        return order

    def compareTwoWords(self, wordA: str, wordB: str) -> tuple[str]:
        """
        wordA = "wrt"
        wordB = "wrf
        return ("t", "f")

        time complexity: O(word_length)
        """
        idxA, idxB = 0, 0
        while idxA < len(wordA) and idxB < len(wordB):
            if wordA[idxA] != wordB[idxB]:
                return wordA[idxA], wordB[idxB]
            idxA += 1
            idxB += 1
        return None
        
    def constructGraph(self, charSet: set, order: list[tuple]) -> tuple[dict, dict]:
        """
        charSet = {"a", "b", "c"}
        order = [("a", "b"), ("b", "c")]
        return:
            node2Indegree = {"a": 0, "b": 1, "c": 1}
            node2Neighbors = {"a": ["b"], "b": ["c"], "c": []}
        
        time complexity: O(num_char + num_order) = O(26 + word_list_length)
        """
        node2Indegree = {x: 0 for x in charSet}
        node2Neighbors = {x: [] for x in charSet}
        for prevNext in order:
            prevChar, nextChar = prevNext[0], prevNext[1]
            node2Indegree[nextChar] += 1
            node2Neighbors[prevChar].append(nextChar)
        return node2Indegree, node2Neighbors
    
    def topologicalSort(self, node2Indegree: dict, node2Neighbors: dict) -> list[str]:
        # BFS
        charQueue = deque()
        order = []
        for node, degree in node2Indegree.items():
            if degree == 0:
                charQueue.append(node)
                order.append(node)
        while charQueue:
            curChar = charQueue.popleft()
            for eachNeighbor in node2Neighbors[curChar]:
                node2Indegree[eachNeighbor] -= 1
                if node2Indegree[eachNeighbor] == 0:
                    charQueue.append(eachNeighbor)
                    order.append(eachNeighbor)
        if len(order) == len(node2Indegree):
            return "".join(order)
        return ""


"""
Step - 1:
    get character relationship from every pair of words

Step - 2:
    convert what I got from Step - 1 into a directed graph
    node: character
    edge: the relationship

Step - 3:
    perform topological sort to get the order of the graph

Step - 4:
    if all characters are included and no cycle and no characters are left
    then return order

INPUT:
    wrt wrf er  ett rftt

t -> f
w -> e
r -> t
e -> r

w -> e -> r -> t -> f
"""