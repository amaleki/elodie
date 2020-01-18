import hashlib
import xxhash 

class HashFactory:

    def digest(self, file_path, hash_type, blocksize=65536):
        hash = self._get_hash(hash_type)
        return hash(file_path, blocksize)

    def _get_hash(self, hash_type):
        if hash_type =='SHA256':
            return self._hash_sha256 
        elif hash_type == 'XXH32':
            return self._hash_xxh32
        elif hash_type ==  'XXH64':
            return self._hash_xxh64
        else:
            raise ValueError(hash_type)

    def _hash_xxh32(self, file_path, blocksize):
        hasher = xxhash.xxh32()
        return self._process_hash(hasher, file_path, blocksize)   

    def _hash_xxh64(self,file_path, blocksize):
        hasher = xxhash.xxh64()
        return self._process_hash(hasher, file_path, blocksize)

    def _hash_sha256(self, file_path, blocksize):
        hasher = hashlib.sha256()
        return self._process_hash(hasher, file_path, blocksize)

    def _process_hash(self, hasher, file_path, blocksize):
        '''   
        See http://stackoverflow.com/a/3431835/1318758. 
        '''
        with open(file_path, 'rb') as f:
            buf = f.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)
            return hasher.hexdigest()
        return None