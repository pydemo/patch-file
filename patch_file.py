import binascii
import os
f1= 'GSM.GSM_OCC_PRICING-00.dmp_ora'
f2='GSM.GSM_OCC_PRICING-00.dmp'
f3='GSM.GSM_OCC_PRICING-00.dmp_byte'
with open(f1 , 'r+b') as f:
	f.seek(2)
	data= f.read(1)
	hex= binascii.hexlify(data)
	binary = int(hex, 16)
	print 'ORA: >|%s|%s|%s|%s|<' % (data, hex, binary, chr(binary))
if 0:
	with open(f2 , 'r+b') as f:
		f.seek(2)
		data= f.read(1)
		hex= binascii.hexlify(data)
		binary = int(hex, 16)
		print data, hex, binary, chr(111), len(chr(111))
		f.seek(2)
		f.write(chr(111))
		f.seek(2)
		data= f.read(1)
		hex= binascii.hexlify(data)
		binary = int(hex, 16)
		print data, hex, binary, chr(111), len(chr(111))
def patch_file(fn, diff):
	for line in diff.split(os.linesep):
		if line:
			addr, to_octal, _ = line.strip().split()
			with open(fn , 'r+b') as f:
				f.seek(int(addr)-1)
				f.write(chr(int (to_octal,8)))

diff="""
     3 157 266
     4 232 276
     5 272 273
     6  16  25
    48  64  57
    58 340   0
    64   1   0
    65 104   0
    66 110   0
   541  61  60
   545  61  60
   552  61  60
   559  61  60
 20508  15   0
 20509 157   0
 20510 230   0
 20526  10   0
 20532  15   0
 20533 225   0
 20534 150   0
913437 226   0
913438  37   0
913454  10   0
913460   1   0
913461 104   0
913462 100   0
"""

patch_file(f3,diff)		

	

	
