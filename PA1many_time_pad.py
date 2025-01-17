ciphertexts = [  
    "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e",  
    "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",  
    "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb",  
    "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",  
    "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070",  
    "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4",  
    "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",  
    "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3",  
    "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",  
    "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83",  
    "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904",  
]  
  
  
# 字节序列进行异或  
def xor_bytes(seq1: bytes, seq2: bytes) -> bytes:  
    # zip(seq1, seq2)将各个比特对应,然后for循环进行每个比特的异或  
    return bytes(b1 ^ b2 for b1, b2 in zip(seq1, seq2))  
  
  
key = [0] * 200  
# 我们后续需要调整这个空格数的阈值,得到最接近的答案。  
# 当阈值过高,则会导致本来确实为空格的字节被忽略,导致密钥不完整  
# 当阈值过低,则会导致本来不为空格的字节误认为是空格,导致密钥错误  
# 所有寻找一个能够正确识别最大多数空格的阈值  
space_threshold = 6  
ciphertexts_length = len(ciphertexts)  
"""  
总体思路：  
我们要解出明文,那么我们就需要知道密钥；  
我们知道,a=b^c,则b=a^c,又ciphertext=key^plaintext 因而,当知道明文和密文,我们只需要将其异或,就可以得到密钥key；  
根据提示,空格与字母的异或结果仍为字母；由此,当两个字符互相异或时,若结果为字母,那么这两个字符很有可能一个是空格,一个是字母；  
我们不妨让一个密文与其他密文异或,若异或结果某个位置是字母,那么我们就在这个密文相应位置计数+1,  
与其他10条密文异或之后,我们就可以得到这个位置可能是空格的次数,这就是上面阈值的设定；  
多次一密,每个明文的对应位置的字节,密钥的字节是相同的,因而只需要选出明文中本是空格的密文,按原来的位置组合,将其与空格异或,就可以得到大致的密钥；  
当遍历完十条密文之后,我们就可以得到许多明文是空格的密文的字节,把他们组合起来,与空格异或即可；  
有了密钥只需要与密文异或,就得到了明文。  
当然,密钥是猜测的,会有瑕疵,因而解出的明文会有少量错误,我们可以人工修正明文,再次与密文异或,便得到了正确的密钥。  
由此,所有的密文我们就都可以破解了。  
"""  
  
for i in range(ciphertexts_length):  
    ciphertext1 = bytes.fromhex(ciphertexts[i])  
    ciphertext1_length = len(ciphertext1)  
    candidate_space = [0] * ciphertext1_length  
  
    for j in range(ciphertexts_length):  
        if j == i:  
            continue  
        ciphertext2 = bytes.fromhex(ciphertexts[j])  
        xor_text = xor_bytes(ciphertext1, ciphertext2)  
        '''  
        不能用index获取位置,因为index获取的是第一个的位置!!!
        for letter in xor_text:            if letter.isalpha():                print(xor_text.index(letter))  
                candidate_space[xor_text.index(letter)] += 1        '''        
        len_xor_text = len(xor_text)  
        for k in range(len_xor_text):  
            if xor_text[k: k + 1].isalpha() or xor_text[k: k + 1] == chr(0):  
                candidate_space[k] += 1  
  
    for s in range(ciphertext1_length):  
        if candidate_space[s] >= space_threshold:  
            key[s] = ciphertext1[s] ^ ord(' ')  
  
print("根据猜测的密钥求解的明文：", xor_bytes(key, bytes.fromhex(ciphertexts[-1])).decode())  
# 输出  
"""  
Thm secuet message is: Whtn usi|g wsstream cipher, never use the key more than once  
由于是猜测的,密钥可能并不完全正确,我们可以自主修正一下：  
The secret message is: When using a stream cipher, never use the key more than once  
"""  
  
# 我们根据修正了的第十一条明文,与第十一条密文再次异或,便得到了正确的密钥,由此,我们可以列出其他密文的明文。  
plaintext = "The secret message is: When using a stream cipher, never use the key more than once"  
correct_key = xor_bytes(plaintext.encode(), bytes.fromhex(ciphertexts[10]))  
print("根据修正后的明文得到的正确密钥：", correct_key.hex())  
# 这是16进制的正确的密钥：  
# 66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a61  
for i in range(len(ciphertexts)):  
    print(f"明文 {i + 1}:", xor_bytes(correct_key, bytes.fromhex(ciphertexts[i])).decode())