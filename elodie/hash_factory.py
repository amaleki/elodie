import hashlib
import xxhash 

class HashFactory:

    def __init__(self, hash=None):

        self.hash_factory=hash
    
    def digest(self, file_path, blocksize=65536):

        hash = self.hash_factory()
        checksum = hash.digest(file_path, blocksize)
        return checksum

class XX32:
    def digest(self,  file_path, blocksize=65536):
        hasher = xxhash.xxh32()
        with open(file_path, 'rb') as f:
            buf = f.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)
            return hasher.hexdigest()
        return None   

class XX64:
    def digest(self, file_path, blocksize=65536):
        
        hasher = xxhash.xxh64()
        with open(file_path, 'rb') as f:
            buf = f.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)
            return hasher.hexdigest()
        return None

class MD5:
    def digest(self):
        return ""

class SHA256:
    def digest(self, file_path, blocksize=65536):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)
            return hasher.hexdigest()
        return None