class Solution(object):
    def _canConstruct(self, ransomNote, magazine):
        m = list(magazine)
        for c in ransomNote:
            # If there are none of c left in the String, return False.
            if c not in m:
                return False
            # Find the index of the first occurrence of c in the magazine.
            idx = m.index(c)
            # Use splicing to make a new string with the characters 
            # before "location" (but not including), and the characters 
            #after "location".
            del m[idx]
            # If we got this far, we can successfully build the note.
        return True
        
    def canConstruct(self, ransomNote, magazine):
        notesCounter = collections.Counter(ransomNote)
        magazineCounter = collections.Counter(magazine)
        
        for char, count in notesCounter.items():
            if char not in magazineCounter:
                return False
            if magazineCounter[char] < count:
                return False
        return True