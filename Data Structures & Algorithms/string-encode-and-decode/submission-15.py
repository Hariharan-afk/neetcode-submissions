
class Solution:

    def encode(self, strs: List[str]) -> str:
        

        self.encoder_format = "ninjalanja"
        if not strs:
            return "no elements"

        return  f"{self.encoder_format}".join(strs)

        

    def decode(self, s: str) -> List[str]:
        
        if s == "no elements":
            return []

        return  s.split(f"{self.encoder_format}")

        