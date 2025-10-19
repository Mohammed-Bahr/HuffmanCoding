# # class AdaptiveHuffmanNode:
# #     def __init__(self, char=None, weight=0, order=0):
# #         self.char = char
# #         self.weight = weight
# #         self.order = order
# #         self.left = None
# #         self.right = None
# #         self.parent = None
    
# #     def is_leaf(self):
# #         return self.left is None and self.right is None


# # class AdaptiveHuffman:
# #     def __init__(self):
# #         self.node_order = 256
# #         self.nyt = AdaptiveHuffmanNode(None, 0, self.node_order)  # Not Yet Transmitted
# #         self.root = self.nyt
# #         self.leaves = {}  # Maps characters to their leaf nodes
# #         self.nodes = [self.root]
    
# #     def find_highest_order(self, weight):
# #         """Find node with same weight but highest order"""
# #         result = None
# #         for node in self.nodes:
# #             if node.weight == weight:
# #                 if result is None or node.order > result.order:
# #                     result = node
# #         return result
    
# #     def swap_nodes(self, n1, n2):
# #         """Swap two nodes in the tree"""
# #         if n1 == n2 or n1.parent == n2 or n2.parent == n1:
# #             return
        
# #         p1, p2 = n1.parent, n2.parent
        
# #         if p1:
# #             if p1.left == n1:
# #                 p1.left = n2
# #             else:
# #                 p1.right = n2
        
# #         if p2:
# #             if p2.left == n2:
# #                 p2.left = n1
# #             else:
# #                 p2.right = n1
        
# #         n1.parent, n2.parent = p2, p1
# #         n1.order, n2.order = n2.order, n1.order
        
# #         if n1 == self.root:
# #             self.root = n2
# #         elif n2 == self.root:
# #             self.root = n1
    
# #     def update_tree(self, node):
# #         """Update tree after processing a character"""
# #         while node:
# #             highest = self.find_highest_order(node.weight)
            
# #             if highest != node and highest != node.parent:
# #                 self.swap_nodes(node, highest)
            
# #             node.weight += 1
# #             node = node.parent
    
# #     def get_path(self, node):
# #         """Get binary path from root to node"""
# #         path = ""
# #         curr = node
        
# #         while curr.parent:
# #             if curr.parent.left == curr:
# #                 path = "0" + path
# #             else:
# #                 path = "1" + path
# #             curr = curr.parent
        
# #         return path
    
# #     def char_to_binary(self, char):
# #         """Convert character to 8-bit binary string"""
# #         return format(ord(char), '08b')
    
# #     def binary_to_char(self, binary):
# #         """Convert 8-bit binary string to character"""
# #         return chr(int(binary, 2))
    
# #     def encode_char(self, char):
# #         """Encode a single character"""
# #         code = ""
        
# #         if char in self.leaves:
# #             # Character exists in tree
# #             node = self.leaves[char]
# #             code = self.get_path(node)
# #             self.update_tree(node)
# #         else:
# #             # New character - send NYT path + character
# #             code = self.get_path(self.nyt)
# #             code += self.char_to_binary(char)
            
# #             # Create new internal node and leaf
# #             new_internal = AdaptiveHuffmanNode(None, 0, self.node_order - 1)
# #             new_leaf = AdaptiveHuffmanNode(char, 0, self.node_order - 2)
            
# #             new_internal.left = self.nyt
# #             new_internal.right = new_leaf
# #             new_internal.parent = self.nyt.parent
            
# #             if self.nyt.parent:
# #                 if self.nyt.parent.left == self.nyt:
# #                     self.nyt.parent.left = new_internal
# #                 else:
# #                     self.nyt.parent.right = new_internal
# #             else:
# #                 self.root = new_internal
            
# #             self.nyt.parent = new_internal
# #             new_leaf.parent = new_internal
            
# #             self.nyt.order = self.node_order - 1
# #             self.node_order -= 2
            
# #             self.leaves[char] = new_leaf
# #             self.nodes.extend([new_internal, new_leaf])
            
# #             self.update_tree(new_internal)
        
# #         return code
    
# #     def encode(self, text):
# #         """Encode entire text"""
# #         encoded = ""
# #         for char in text:
# #             encoded += self.encode_char(char)
# #         return encoded
    
# #     def decode(self, encoded):
# #         """Decode encoded text"""
# #         decoded = ""
# #         curr = self.root
# #         i = 0
        
# #         while i < len(encoded):
# #             if curr == self.nyt:
# #                 # Read next 8 bits for new character
# #                 if i + 8 > len(encoded):
# #                     break
# #                 char_bits = encoded[i:i+8]
# #                 char = self.binary_to_char(char_bits)
# #                 decoded += char
# #                 i += 8
                
# #                 self.encode_char(char)  # Update tree
# #                 curr = self.root
# #             elif curr.is_leaf():
# #                 decoded += curr.char
# #                 self.encode_char(curr.char)  # Update tree
# #                 curr = self.root
# #             else:
# #                 if encoded[i] == '0':
# #                     curr = curr.left
# #                 else:
# #                     curr = curr.right
# #                 i += 1
        
# #         return decoded
    
# #     def display_stats(self, original, encoded):
# #         """Display compression statistics"""
# #         print("\n=== Adaptive Huffman Coding Stats ===")
# #         print(f"Original text: {original}")
# #         print(f"Original size: {len(original) * 8} bits")
# #         print(f"Encoded size: {len(encoded)} bits")
# #         compression = (1 - len(encoded) / (len(original) * 8)) * 100
# #         print(f"Compression ratio: {compression:.2f}%")


# # def main():
# #     # Create separate encoder and decoder
# #     adaptive_encoder = AdaptiveHuffman()
# #     adaptive_decoder = AdaptiveHuffman()
    
# #     text = "mohammed"
# #     print(f"Original: {text}")
    
# #     # Encode
# #     encoded = adaptive_encoder.encode(text)
# #     print(f"\nEncoded: {encoded}")
    
# #     # Decode
# #     decoded = adaptive_decoder.decode(encoded)
# #     print(f"Decoded: {decoded}")
    
# #     # Stats
# #     adaptive_encoder.display_stats(text, encoded)
    
# #     # Verify
# #     print(f"\nVerification: {'SUCCESS' if text == decoded else 'FAILED'}")
    
# #     # Example with longer text
# #     print("\n" + "="*50)
# #     print("Example with longer text:")
    
# #     encoder2 = AdaptiveHuffman()
# #     decoder2 = AdaptiveHuffman()
    
# #     long_text = "this is an example of adaptive huffman coding algorithm"
# #     print(f"Text: {long_text}")
    
# #     encoded2 = encoder2.encode(long_text)
# #     decoded2 = decoder2.decode(encoded2)
    
# #     encoder2.display_stats(long_text, encoded2)
# #     print(f"Verification: {'SUCCESS' if long_text == decoded2 else 'FAILED'}")


# # if __name__ == "__main__":
# #     main()


















# import heapq
# from collections import Counter, defaultdict


# class HuffmanNode:
#     def __init__(self, char=None, freq=0):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None
    
#     # For priority queue comparison
#     def __lt__(self, other):
#         return self.freq < other.freq


# class HuffmanCoding:
#     def __init__(self):
#         self.root = None
#         self.codes = {}
#         self.reverse_codes = {}
#         self.frequency = {}
    
#     def calculate_frequency(self, text):
#         """Calculate frequency of each character"""
#         self.frequency = dict(Counter(text))
    
#     def build_huffman_tree(self):
#         """Build Huffman Tree using min-heap"""
#         # Create min heap with leaf nodes
#         heap = []
#         for char, freq in self.frequency.items():
#             node = HuffmanNode(char, freq)
#             heapq.heappush(heap, node)
        
#         # Build tree by combining nodes
#         while len(heap) > 1:
#             left = heapq.heappop(heap)
#             right = heapq.heappop(heap)
            
#             # Create internal node
#             merged = HuffmanNode(None, left.freq + right.freq)
#             merged.left = left
#             merged.right = right
            
#             heapq.heappush(heap, merged)
        
#         self.root = heap[0]
    
#     def generate_codes(self, node=None, code=""):
#         """Generate Huffman codes by traversing tree"""
#         if node is None:
#             node = self.root
        
#         # Leaf node - store the code
#         if node.char is not None:
#             self.codes[node.char] = code if code else "0"
#             self.reverse_codes[code if code else "0"] = node.char
#             return
        
#         # Traverse left with '0' and right with '1'
#         if node.left:
#             self.generate_codes(node.left, code + "0")
#         if node.right:
#             self.generate_codes(node.right, code + "1")
    
#     def encode(self, text):
#         """Encode text using Huffman coding"""
#         if not text:
#             return ""
        
#         # Step 1: Calculate frequency
#         self.calculate_frequency(text)
        
#         # Step 2: Build Huffman Tree
#         self.build_huffman_tree()
        
#         # Step 3: Generate codes
#         self.generate_codes()
        
#         # Step 4: Encode the text
#         encoded_text = ""
#         for char in text:
#             encoded_text += self.codes[char]
        
#         return encoded_text
    
#     def decode(self, encoded_text):
#         """Decode encoded text using Huffman tree"""
#         if not encoded_text or not self.root:
#             return ""
        
#         decoded_text = ""
#         current = self.root
        
#         for bit in encoded_text:
#             # Traverse tree based on bit
#             if bit == '0':
#                 current = current.left
#             else:
#                 current = current.right
            
#             # Reached leaf node
#             if current.char is not None:
#                 decoded_text += current.char
#                 current = self.root
        
#         return decoded_text
    
#     def display_codes(self):
#         """Display Huffman codes in formatted table"""
#         print("\n╔════════════════════════════════╗")
#         print("║     HUFFMAN CODES TABLE        ║")
#         print("╠═══════╦══════════╦═════════════╣")
#         print("║ Char  ║ Freq     ║ Code        ║")
#         print("╠═══════╬══════════╬═════════════╣")
        
#         for char in sorted(self.codes.keys()):
#             code = self.codes[char]
#             freq = self.frequency[char]
#             print(f"║   {char}   ║    {freq:<5}║ {code:<11} ║")
        
#         print("╚═══════╩══════════╩═════════════╝")
    
#     def display_tree(self, node=None, prefix="", is_left=None):
#         """Display tree structure"""
#         if node is None:
#             node = self.root
        
#         if node is None:
#             return
        
#         print(prefix, end="")
        
#         if is_left is None:
#             print("Root: ", end="")
#         else:
#             print("├──" if is_left else "└──", end="")
        
#         if node.char is not None:
#             print(f"['{node.char}': {node.freq}]")
#         else:
#             print(f"[{node.freq}]")
        
#         if node.left or node.right:
#             if is_left is None:
#                 new_prefix = prefix
#             else:
#                 new_prefix = prefix + ("│   " if is_left else "    ")
            
#             if node.left:
#                 self.display_tree(node.left, new_prefix, True)
#             if node.right:
#                 self.display_tree(node.right, new_prefix, False)
    
#     def display_stats(self, original, encoded):
#         """Display compression statistics"""
#         original_bits = len(original) * 8
#         encoded_bits = len(encoded)
#         compression_ratio = (1 - encoded_bits / original_bits) * 100
        
#         print("\n╔════════════════════════════════════════╗")
#         print("║      COMPRESSION STATISTICS            ║")
#         print("╠════════════════════════════════════════╣")
#         print(f"║ Original text length: {len(original)} characters")
#         print(f"║ Original size: {original_bits} bits")
#         print(f"║ Encoded size: {encoded_bits} bits")
#         print(f"║ Compression ratio: {compression_ratio:.2f}%")
#         print(f"║ Space saved: {original_bits - encoded_bits} bits")
#         print("╚════════════════════════════════════════╝")


# def main():
#     huffman = HuffmanCoding()
    
#     text = "mohammed"
    
#     print("=" * 40)
#     print("   STANDARD HUFFMAN CODING DEMO")
#     print("=" * 40)
#     print(f"\nOriginal Text: \"{text}\"")
    
#     # Encode
#     encoded = huffman.encode(text)
#     print(f"\nEncoded Binary: {encoded}")
    
#     # Display codes
#     huffman.display_codes()
    
#     # Display tree
#     print("\n=== Huffman Tree Structure ===")
#     huffman.display_tree()
    
#     # Decode
#     decoded = huffman.decode(encoded)
#     print(f"\nDecoded Text: \"{decoded}\"")
    
#     # Display statistics
#     huffman.display_stats(text, encoded)
    
#     # Verification
#     status = "SUCCESS ✓" if text == decoded else "FAILED ✗"
#     print(f"\n✓ Verification: {status}")
#     print("\n" + "=" * 40)
    


# if __name__ == "__main__":
#     main()


import heapq
from collections import defaultdict

class HNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, text=""):
        self.root = None
        self.text = text
        self.frequency = defaultdict(int)
        self.chCodes = {}

    def Freq_Count(self, text):
        for ch in text:
            self.frequency[ch] += 1

    def buildTree(self):
        minHeap = []
        for ch, freq in self.frequency.items():
            heapq.heappush(minHeap, HNode(ch, freq))

        while len(minHeap) > 1:
            left = heapq.heappop(minHeap)
            right = heapq.heappop(minHeap)

            newNode = HNode('\0', left.freq + right.freq)
            newNode.left = left
            newNode.right = right

            heapq.heappush(minHeap, newNode)

        return minHeap[0] if minHeap else None

    def To_Bits_Coded(self, node, code):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.chCodes[node.data] = code
            return
        self.To_Bits_Coded(node.left, code + "0")
        self.To_Bits_Coded(node.right, code + "1")

    def printTree(self, node, prefix="", isLeft=True):
        if node is None:
            return

        print(prefix + ("├──" if isLeft else "└──"), end="")
        if node.left is None and node.right is None:
            print(f"['{node.data}': {node.freq}]")
        else:
            print(f"[{node.freq}]")

        if node.left or node.right:
            self.printTree(node.left, prefix + ("│   " if isLeft else "    "), True)
            self.printTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    def encode(self):
        if not self.text:
            return ""

        self.Freq_Count(self.text)
        self.root = self.buildTree()
        self.To_Bits_Coded(self.root, "")

        encoded = ""
        for ch in self.text:
            encoded += (self.chCodes[ch] + "_")
        return encoded  

    # فك التشفير
    def decode(self, encodedText):
        if not encodedText or self.root is None:
            return ""

        decoded = ""
        current = self.root
        for bit in encodedText:
            current = current.left if bit == '0' else current.right
            if current.left is None and current.right is None:
                decoded += current.data
                current = self.root

        return decoded

    # عرض الأكواد
    def displayCodes(self):
        print("\n╔════════════════════════════════╗")
        print("║     HUFFMAN CODES TABLE        ║")
        print("╠═══════╦══════════╦═════════════╣")
        print("║ Char  ║ Freq     ║ Code        ║")
        print("╠═══════╬══════════╬═════════════╣")
        for ch, code in self.chCodes.items():
            print(f"║   {ch}   ║    {self.frequency[ch]}     ║ {code:<12}║")
        print("╚═══════╩══════════╩═════════════╝")

    # عرض الشجرة
    def displayTree(self):
        print("\n=== Huffman Tree Structure ===")
        self.printTree(self.root, "", False)

    # حساب نسبة الضغط
    def displayStats(self, encoded):
        originalBits = len(text) * 8
        encodedBits = len(encoded)
        ratio = (1.0 - (encodedBits / originalBits)) * 100

        print("\n╔════════════════════════════════════════╗")
        print("║      COMPRESSION STATISTICS            ║")
        print("╠════════════════════════════════════════╣")
        print(f"║ Original text length: {len(text)} characters")
        print(f"║ Original size: {originalBits} bits")
        print(f"║ Encoded size: {encodedBits} bits")
        print(f"║ Compression ratio: {ratio:.2f}%")
        print(f"║ Space saved: {originalBits - encodedBits} bits")
        print("╚════════════════════════════════════════╝")


# ==================== MAIN ====================
if __name__ == "__main__":
    text = "mohammed bahr"
    huffman = HuffmanCoding(text)

    print("========================================")
    print("   STANDARD HUFFMAN CODING DEMO")
    print("========================================")
    print(f"\nOriginal Text: \"{text}\"")

    # Encode
    encoded = huffman.encode()
    print(f"\nEncoded Binary: {encoded}")

    # Display codes
    huffman.displayCodes()

    # Display tree
    huffman.displayTree()

    # Decode
    decoded = huffman.decode(encoded)
    print(f"\nDecoded Text: \"{decoded}\"")

    # Display statistics
    huffman.displayStats(encoded)

    # Verification
    print(f"\n✓ Verification: {'SUCCESS ✓' if text == decoded else 'FAILED ✗'}")
    print("\n========================================")
