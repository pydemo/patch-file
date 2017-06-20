import binascii
import os, sys
e=sys.exit
f1= 'GSM.GSM_OCC_PRICING-00.dmp_ora'
f2='GSM.GSM_OCC_PRICING-00.dmp'
f3='GSM.GSM_OCC_PRICING-00.dmp_byte'
if 0:
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
			print addr,',',
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
"""
  20508   0  50
  20509   0 126
  20510   0 173
  20526   0  10
  20532   0  50
  20533   0 174
  20534   0 120
2674717   0 226
2674718   0  47
2674734   0  10
2674740   0   1
2674741   0 104
2674742   0 110"""

addr=[3 , 4 , 5 , 6 , 48 , 58 , 64 , 65 , 66 , 541 , 545 , 552 , 559 , 20508 , 20509 , 20510 , 20526 , 20532 , 20533 , 20534 ]
last_range=[85987, 85986, 85970, 85964, 85963, 85962]

def get_bytes(addr):
	out =[]
	with open(f1 , 'r+b') as f:
		for a in addr:
			f.seek(a-1)
			data= f.read(1)
			hex= binascii.hexlify(data)
			binary = int(hex, 16)
			octa= oct(binary)
			out.append((a,octa))

	return out


def patch_file(fn, bytes_to_update):
	with open(fn , 'r+b') as f:
		for (a,to_octal) in bytes_to_update:
			print (a,to_octal)
			f.seek(int(a)-1)
			f.write(chr(int (to_octal,8)))

#print [fsize-x for x in [913437 , 913438 , 913454 , 913460 , 913461 , 913462]]
if 1:
	from_file=f1
	fsize=os.stat(from_file).st_size
	bytes_to_read = addr + [fsize-x for x in last_range]

	bytes_to_update = get_bytes(bytes_to_read)	
	to_file =f3
	patch_file(to_file,bytes_to_update)
	
