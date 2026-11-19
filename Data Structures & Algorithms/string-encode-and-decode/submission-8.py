
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        def encoder(s:str) -> str:
            s = s.split(" ")
            msg = "**".join(s)

            return msg

        encoded = ""

        if not strs:
            return "no elements"

        for i in range(len(strs)):
            if not strs[i]:
                if not encoded:
                    encoded += "empty"
                else:
                    encoded += " empty"
            
            else:
                string = encoder(strs[i])
                if not encoded:     
                    encoded += string
                else:
                    encoded = encoded + " " + string 

        return encoded
        

    def decode(self, s: str) -> List[str]:
        
        if s == "no elements":
            return []

        decoded = s.split(" ")

        for i in range(len(decoded)):

            if decoded[i] == "empty":
                decoded[i] = ""
            
            else:
                s = decoded[i].split("**")
                msg = " ".join(s)
                decoded[i] = msg

        return decoded

        