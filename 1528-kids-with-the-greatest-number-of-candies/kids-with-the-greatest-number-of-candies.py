class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        kuch_kuch = []
        for y in candies:
            if y + extraCandies >= x:
                kuch_kuch.append(True)
            else:
                kuch_kuch.append(False)
        return kuch_kuch
                
