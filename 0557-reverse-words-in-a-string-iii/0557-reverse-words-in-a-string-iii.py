class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        finals = ""
        for x in s:
            if x != " ":
                temp+=x
            else:
                finals += temp[::-1]
                finals += " "
                temp = ""
        finals += temp[::-1]
        return finals