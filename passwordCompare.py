import hashlib

hashA = str(input('Digite seu primeiro hash')).encode('utf-8')
hashB = str(input('Digite seu segundo hash')).encode('utf-8')

hash1 = hashlib.new('md5')
hash1.update(hashA)

hash2 = hashlib.new('md5')
hash2.update(hashB)


if hash1.digest() != hash2.digest():
    print(f'O hash {hash1.hexdigest()} é diferente de {hash2.hexdigest()}')
else:
    print('Os hashs sao iguais')
    print(f'Os hash sao: {hash1.hexdigest()}')