class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        jodo_ka_dard = 0
        pikachu = 1
        while n > 0:
            digit = n % 10
            jodo_ka_dard += digit
            pikachu *= digit
            n //= 10
        return pikachu - jodo_ka_dard
        