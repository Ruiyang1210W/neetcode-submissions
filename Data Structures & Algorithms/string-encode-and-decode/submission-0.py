class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            # Find # 当前单词长度终点
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) #拿到#前面的数字转化为整数

            #根据长度切出单词
            word = s[j + 1 : j + 1 + length]
            decode.append(word)

            i = j + 1 + length
    
        return decode

