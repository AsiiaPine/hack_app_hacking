code = open("hack_app", "rb")
contents = code.read()
new_contents = contents.replace(b'\x75\x07\xc7\x45\xe4\x01\x00\x00', b'\x74\x07\xc7\x45\xe4\x01\x00\x00')

new_code = open("hack_app_patched", "wb")
new_code.write(new_contents)
new_code.close()
code.close()