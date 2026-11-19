
class Solution:

    def encode(self, strs: List[str]) -> str:
        

        self.encoder_format = "\n\n"
        encoded = ""

        if not strs:
            return "no elements"

        # for i in range(len(strs)):
        #     if not strs[i]:
        #         if not encoded:
        #             encoded += "empty"
        #         else:
        #             encoded += " empty"
            
        #     else:
        #         string = encoder(strs[i])
        #         if not encoded:     
        #             encoded += string
        #         else:
        #             encoded = encoded + " " + string 

        encoded  = f"{self.encoder_format}".join(strs)

        return encoded
        

    def decode(self, s: str) -> List[str]:
        
        if s == "no elements":
            return []

        decoded = s.split(f"{self.encoder_format}")

        

        return decoded

        