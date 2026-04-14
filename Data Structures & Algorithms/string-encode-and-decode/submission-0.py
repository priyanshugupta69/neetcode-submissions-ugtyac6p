class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        if len(strs) == 0:
            return encode_str
        size_arr = []
        encode_str = ",".join(str(len(s)) for s in strs)
        encode_str += '#'

        for i in strs:
            encode_str += "".join(i)
        
        return encode_str




    def decode(self, s: str) -> List[str]:
        
        if s == "":
            return []

        print(s)

        parse = s.split('#', maxsplit=1)

        lenghts = parse[0].split(',')

        lenghts = [int(i) for i in lenghts]

        words = parse[1]
        
        print("lenghts", lenghts, "words", words)
        
        ans = []
        j = 0
        for i in lenghts:
            count = i
            temp = ""
            while(count > 0):
                temp += words[j]
                count += -1
                j += 1
            ans.append(temp)
        return ans




