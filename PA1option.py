ciphertext = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
ciphertext_bytes = bytes.fromhex(ciphertext)

max_key_length = 13
possible_key_length = [0] * max_key_length
ciphertext_length = len(ciphertext_bytes)

def compare_bytes(a: bytes, b: bytes):
    fitting_index = 0
    for le1, le2 in zip(a, b):
        if le1 ==le2:
            fitting_index += 1
    return fitting_index / min(len(a), len(b))

def guess_key_length(cipher_bytes: bytes):
    fitting_index_dict = {}
    for key_len in range(1, max_key_length+1):
        ciphertext_chunks = []
        for i in range(0, ciphertext_length, key_len):
            ciphertext_chunks.append(cipher_bytes[i: i+key_len])
        chunks_length = len(ciphertext_chunks)
        fitting_index = 0
        for i in range(chunks_length):
            fitting_sum = 0
            for j in range(i+1, chunks_length):
                fitting_sum += compare_bytes(ciphertext_chunks[i], ciphertext_chunks[j])
            fitting_index += (fitting_sum / (chunks_length - i))
        fitting_index_dict[key_len] = fitting_index
    return fitting_index_dict

fitting_index = guess_key_length(ciphertext_bytes)
for key, value in fitting_index.items():
    print(key, ":", value.__round__(4))

key_length = 7

def split_bytes_by_modulo(input_bytes, key_len):
    result_bytes = [b""] * key_len
    for index, byte in enumerate(input_bytes):
        group_index = index % key_len
        result_bytes[group_index] += bytes([byte])
    return result_bytes

def judge(x):
    return 65 <= x <= 90 or 97 <= x <= 122 or 32 <= x <= 33 or 44 <= x <= 46

def get_key(key_len: int, cipher_text_byte_chunks):
    key = []
    for i in range(key_len):
        length = len(cipher_text_byte_chunks[i])
        for k in range(256):
            for l in range(length):
                if not judge(cipher_text_byte_chunks[i][l] ^ k):
                    break
                if l == length - 1:
                    key.append(k)
    
    return key

def repeating_xor(text: bytes, key) -> bytes:
    quotient, remainder = divmod(len(text), len(key))
    key_extend = bytes(key * quotient + key[:remainder])
    return bytes([x ^ y for x, y in zip(text, key_extend)])

ciphertext_byte_chunk = split_bytes_by_modulo(ciphertext_bytes, key_length)
final_key = get_key(key_length, ciphertext_byte_chunk)
plaintext = repeating_xor(ciphertext_bytes, final_key)
print(plaintext.decode())
print(final_key)
