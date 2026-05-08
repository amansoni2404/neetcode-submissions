class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined = "".join(s.split())
        for i in joined:
            if not i.isalnum():
                joined = joined.replace(i, "")
        print("Joined:", joined)
        front = 0
        back = len(joined)-1
        while front < back:
            if joined[front].lower() != joined[back].lower():
                return False
            front += 1
            back -= 1
        return True