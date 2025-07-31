import hashlib
import base64
import logging

def compute_digest_sri(data, hashing_algorithm):
    if isinstance(data, str):
        data_to_bytes = data.encode('utf-8')

        hash_func = getattr(hashlib, hashing_algorithm)
        hash = hash_func(data_to_bytes).digest()
        encoded = base64.b64encode(hash)  # returns bytes
        digest = encoded.decode('utf-8')
        logging.info('Computed digest {} with hashing algorithm: {}'.format(digest, hashing_algorithm))
        return {hashing_algorithm: digest}
