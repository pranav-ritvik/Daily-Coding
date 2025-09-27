class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = (celsius + 273.15)
        f = (celsius * 9/5) + 32
        return [k,f]
