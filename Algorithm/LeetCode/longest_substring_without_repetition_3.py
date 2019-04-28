class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 1
        max = 1
        word_length = len(s)
        if word_length <= 1:
            return word_length

        unique = set()
        target_index = 0
        curr_index = 1
        unique.add(s[target_index])

        while (target_index < word_length and curr_index < word_length):
            target_char = s[target_index]
            curr_char = s[curr_index]

            if (curr_char in unique):
                while (curr_char in unique):
                    unique.remove(s[target_index])
                    count -= 1
                    target_index += 1
            else:
                count += 1
                unique.add(curr_char)
                if max < count:
                    max = count
                curr_index += 1

        return max