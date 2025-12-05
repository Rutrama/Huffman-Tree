import time
import os
import re
from collections import Counter
import heapq
from typing import List, Dict, Optional, Tuple

CodeTable = Dict[str, str] 
FrequencyMap = Dict[str, int]

class HuffmanNode:
    """Representa um nó na Árvore de Huffman."""
    
    def __init__(self, word: Optional[str] = None, frequency: int = 0, 
                 left: Optional['HuffmanNode'] = None, 
                 right: Optional['HuffmanNode'] = None):
        self.word = word        
        self.frequency = frequency  
        self.left = left        
        self.right = right      

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """Define a comparação para a Fila de Prioridade (heapq). Prioriza a menor frequência."""
        return self.frequency < other.frequency
