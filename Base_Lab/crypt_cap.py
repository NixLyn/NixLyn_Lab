import pyshark
from cryptography.fernet import Fernet

# Decrypts a packet if it is encrypted
def decrypt_packet(packet):
    if 'TLS' in packet:
        cipher_suite = packet.tls.handshake_ciphersuite[0]
        if cipher_suite in {'AES256-GCM-SHA384', 'AES128-GCM-SHA256'}:
            # Generate a key based on the cipher suite
            key = Fernet.generate_key()
            f = Fernet(key)
            iv = packet.tls.record_iv
            cipher_text = packet.tls.record_content
            plain_text = f.decrypt(cipher_text, iv)
            return plain_text.decode('utf-8')
    return None

# Captures HTTP traffic and decrypts any encrypted packets
def capture_and_decrypt():
    capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp port 80')
    capture.sniff(timeout=10)
    decrypted = []
    for packet in capture:
        plain_text = decrypt_packet(packet)
        if plain_text is not None:
            decrypted.append(plain_text)
    return decrypted

# Example usage
decrypted_packets = capture_and_decrypt()
for packet in decrypted_packets:
    print(packet)
