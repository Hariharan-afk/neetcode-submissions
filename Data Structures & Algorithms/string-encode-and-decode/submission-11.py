
class Solution:

    def encode(self, strs: List[str]) -> str:
        

        self.encoder_format = "\n&&"
        encoded = ""

        if not strs:
            return "no elements"

    

        encoded  = f"{self.encoder_format}".join(strs)

        return encoded
        

    def decode(self, s: str) -> List[str]:
        
        if s == "no elements":
            return []

        decoded = s.split(f"{self.encoder_format}")

        

        return decoded

        