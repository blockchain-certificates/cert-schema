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


def base64url_no_pad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')


MULTICODEC_PREFIXES = {
    'sha256': 0x12
}


def compute_digest_multibase(data, hashing_algorithm):
    if isinstance(data, str):
        data_to_bytes = data.encode('utf-8')

        if hashing_algorithm not in MULTICODEC_PREFIXES:
            raise ValueError('Unsupported hashing algorithm for multibase digest: {}'.format(hashing_algorithm))

        hash_func = getattr(hashlib, hashing_algorithm)
        hash_buffer = hash_func(data_to_bytes).digest()

        codec_byte = MULTICODEC_PREFIXES[hashing_algorithm]
        sha_header = bytes([codec_byte, len(hash_buffer)])
        multiformat_bytes = sha_header + hash_buffer

        digest = 'u' + base64url_no_pad(multiformat_bytes)
        logging.info('Computed digest {} with hashing algorithm: {}'.format(digest, hashing_algorithm))
        return {hashing_algorithm: digest}
