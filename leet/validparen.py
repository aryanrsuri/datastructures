from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        parens = {
                "(": ")",
                "[": "]",
                "{": "}"
                }
        for char in s:
            if char in parens:
                q.append(parens[char])
                continue;
            if len(q) == 0 or char != q.pop():
                return False
        return len(q) == 0;

def main():
    test = Solution()
    print (   test.isValid("()") )
    print ( test.isValid("([") )
    print ( test.isValid("][") )
    print ( test.isValid("()[]{}") )
if __name__ == "__main__":
    main()

    

