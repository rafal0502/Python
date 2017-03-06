import hashlib

def get_hash(f_path):
    h = hashlib.new('md5')
    f = open(f_path, 'rb')
    h.update(f.read())      #obiekt hashujacy zaimpl. o ob. f.read()
    hash_text = h.hexdigest()
    # 'eb63071881718ed66bb75ce670e65b9e'
    f.close()
    return hash_text

print(get_hash('plik_testowy.txt'))
