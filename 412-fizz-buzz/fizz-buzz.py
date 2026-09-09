class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_wala = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                final_wala.append("FizzBuzz")
            elif i % 3 == 0:
                final_wala.append("Fizz")
            elif i % 5 == 0:
                final_wala.append("Buzz")
            else:
                final_wala.append(str(i))
        return final_wala
