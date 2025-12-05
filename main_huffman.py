import time
import os
import re
from typing import List, Tuple

from huffman_io import read_input_texts, compress_text, write_output_file, draw_huffman_tree, OUTPUT_FILE
from huffman_core import calculate_word_frequencies, build_huffman_tree, generate_huffman_codes
from huffman_structures import HuffmanNode, CodeTable

def main():
    print("Iniciando compressão de Huffman...")
    
    # Lê o texto do arquivo input.dat
    text_blocks = read_input_texts()
    
    if not text_blocks:
        print("Nenhum bloco de texto encontrado para processamento.")
        return

    # Concatena todas as palavras do texto
    full_text = ' '.join(text_blocks)
    
    # Cálcula a Frequência de cada palavra na string concatenada
    print("Calculando frequências do arquivo completo...")
    frequencies = calculate_word_frequencies(full_text)
    
    # Constrói da Árvore de Huffman
    root_node = build_huffman_tree(frequencies)
    
    if not root_node:
        print("Frequências vazias. Abortando.")
        return

    draw_huffman_tree(root_node)

    # Gera os Códigos de Huffman com base na árvore
    codes = generate_huffman_codes(root_node)
    print(f"Árvore de Huffman construída com {len(codes)} símbolos únicos.")
    
    results: List[Tuple[str, str]] = []
    total_original_words = 0
    total_compressed_bits = 0

    # Gera o texto comprimido usando o código gerado
    print("\nComprimindo blocos de texto...")
    for i, original_text in enumerate(text_blocks):
        
        compressed_data = compress_text(original_text, codes)
        results.append((original_text, compressed_data))
        
        # Métricas
        original_words = len(re.findall(r'\b\w+\b|[.,?!]', original_text.lower()))
        total_original_words += original_words
        total_compressed_bits += len(compressed_data)
        
        print(f"  - Bloco {i+1}: {original_words} palavras -> {len(compressed_data)} bits.")
        
    # Escreve o Arquivo de Output
    write_output_file(root_node, codes, results)
        
    print(f"\nProcessamento concluído. Palavras totais: {total_original_words}.")
    print(f"Saída completa gravada em {OUTPUT_FILE}")

if __name__ == '__main__':
    main()