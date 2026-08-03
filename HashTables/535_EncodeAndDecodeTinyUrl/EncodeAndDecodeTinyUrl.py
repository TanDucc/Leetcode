class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
        
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]    

# Example usage:
codec = Codec()
longUrl1 = "https://leetcode.com/problems/design-tinyurl"
shortUrl1 = codec.encode(longUrl1)
print(shortUrl1)  # Outputs a shortened URL    

longUrl2 = "https://www.google.com"
shortUrl2 = codec.encode(longUrl2)
print(shortUrl2)  # Outputs another shortened URL