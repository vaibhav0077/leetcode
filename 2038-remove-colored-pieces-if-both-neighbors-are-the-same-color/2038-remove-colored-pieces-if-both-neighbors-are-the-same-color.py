class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Check there are enough colors
        if len(colors) < 3:
            return False
        # Stores the number of removable chars for each person
        n_alice, n_bob = 0, 0
        # The pointers for the sliding window
        i, j, k = 0, 1, 2

        while k < len(colors):
            # If this color is removable, count it
            if colors[i] == colors[j] == colors[k]:
                if colors[j] == 'A':
                    n_alice += 1
                else:
                    n_bob += 1
            i += 1
            j += 1
            k += 1

        # Return True iff Alice may remove more than Bob
        return n_alice > n_bob