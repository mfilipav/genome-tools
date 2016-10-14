# Algorithm for finding the most frequent k-mers in a DNA sequence (Text)
# checks all k-mers appearing in the sequence and then computes how many
# times each k-mer appears in sequence. Prints most frequent appearances
# In the future implement frequency array for longer texts

Text = "CTTCTGACCAAGTGAATGGCGATGGTGCGATGGTAAGTGAATGAGAAATAAAAGTGAATGAAGTGAATGGACTATCCATAGAAATAAAAGTGAATGGACTATCCATGCGATGGTCTTCTGACCAGAAATAAGACTATCCATCTTCTGACCCTTCTGACCGCGATGGTGACTATCCATAAGTGAATGGCGATGGTAGAAATAAGACTATCCATGCGATGGTAAGTGAATGGCGATGGTAAGTGAATGGACTATCCATAAGTGAATGAAGTGAATGAAGTGAATGCTTCTGACCAAGTGAATGAAGTGAATGGCGATGGTGACTATCCATAAGTGAATGAAGTGAATGGACTATCCATGACTATCCATGACTATCCATGACTATCCATGACTATCCATAAGTGAATGAGAAATAAAGAAATAAAGAAATAAGCGATGGTAGAAATAAGACTATCCATAGAAATAAGCGATGGTGCGATGGTGCGATGGTGACTATCCATGCGATGGTAGAAATAAGCGATGGTGCGATGGTAAGTGAATGAGAAATAAAAGTGAATGGCGATGGTAAGTGAATGGACTATCCATCTTCTGACCAAGTGAATGGACTATCCATCTTCTGACCGACTATCCATCTTCTGACCCTTCTGACCGCGATGGTAAGTGAATGAAGTGAATGCTTCTGACCAAGTGAATGGCGATGGTGCGATGGTCTTCTGACCGACTATCCATGCGATGGTGACTATCCATGACTATCCATAAGTGAATGAGAAATAAGCGATGGTCTTCTGACCAAGTGAATGAAGTGAATGAAGTGAATGGACTATCCATAGAAATAACTTCTGACCAGAAATAAGACTATCCATAAGTGAATGGACTATCCATAAGTGAATGGACTATCCATAAGTGAATGCTTCTGACCGCGATGGT"
k = 12
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    ItemsNoDuplicates = []

    [ItemsNoDuplicates.append(item) for item in Items
        if not ItemsNoDuplicates.count(item)]
    ItemsNoDuplicates.sort()
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
# PatternCount(Pattern, Text
words = FrequentWords(Text, k)
# print(words)
for i in words: print(i, end=" ")