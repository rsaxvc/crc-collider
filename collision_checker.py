import zlib
import crc16

d = dict()
d["adler32"] = dict()
d["crc32"] = dict()
d["crc16"] = dict()
c = dict()
c["adler32"] = zlib.adler32
c["crc32"] = zlib.crc32
c["crc16"] = crc16.crc16xmodem
with open("wordsEn.txt") as f:
	for line in f:
		line = line.rstrip()
		for crc_type in c:
			crc = c[crc_type](line)
			if( crc in d[crc_type] ):
				d[crc_type][crc] += 1
			else:
				d[crc_type][crc] = 0

import operator
for crc_type in d:
	print crc_type
	old = 0
	count = 0
	for x in sorted( d[crc_type].items(), key=operator.itemgetter(1)):
		if( x[1] != old ):
			print "\t",old, count
			old = x[1]
			count = 0
		else:
			count += 1
	print "\t",old, count
