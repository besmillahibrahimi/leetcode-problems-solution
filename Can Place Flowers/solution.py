class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        l = len(flowerbed)
        for i, v in enumerate(flowerbed):
            if v == 0:
                p = 0 if i == 0 else i - 1
                ne = i + 1 if i < l - 1 else l - 1
                if flowerbed[p] == 0 and flowerbed[ne] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        break
        return n == 0
