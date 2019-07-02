class Solution:
    def intToRoman(self, num: int) -> str:
        value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        
        for idx, value in enumerate(value_list):
            while num >= value:
                num -= value
                result += roman_list[idx]
        return result
        