from block_extractor.simple_block import SimpleBlock
from typing import List


class LayoutGraph:
    def __init__(self, nodes: List[SimpleBlock]):
        self.nodes = nodes
        self.inEdges = [[] for i in range(len(nodes))]
        self.outEdges = [[] for i in range(len(nodes))]

    def add_edge(self, edge_type: str, _from_idx: int, _to_idx: int):
        self.inEdges[_to_idx].append((edge_type, _from_idx))
        self.outEdges[_from_idx].append((edge_type, _to_idx))

    def print_layout(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.inEdges[i])):
                edge_type, from_idx = self.inEdges[i][j]
                print("{}, {} -> {}".format(edge_type, from_idx, i))