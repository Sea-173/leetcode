class Solution:
    def intToRoman(self, num: int) -> str:
        count = 1000
        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        result = ""
        while count >= 1:
            cur = num // count
            if cur <= 0:
                count = count // 10
                continue
            num = num % count
            # print(cur, count, num)
            if cur < 4:
                for i in range(cur):
                    result += roman[count]
            elif cur == 4:
                result = result + roman[count] + roman[5*count]
            elif cur < 9:
                result = result + roman[5*count]
                for i in range(cur-5):
                    result += roman[count]
            elif cur == 9:
                result += roman[count]
                result += roman[count*10]
            count = count // 10
        return result

s1 =Solution()
print(s1.intToRoman(58))