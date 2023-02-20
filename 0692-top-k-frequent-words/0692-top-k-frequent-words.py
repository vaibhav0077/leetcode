class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
        sorted_dict = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in sorted_dict[:k]]