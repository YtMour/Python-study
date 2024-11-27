from Crypto.Hash import MD5, SHA256,SHA3_256
h=MD5.new()
h.update(b"15936888866")
print(h.hexdigest())

h=SHA256.new(b"15936888866")
print(h.hexdigest())

h2=SHA3_256.new()
h2.update(b"15936888866")
print(h2.hexdigest())
