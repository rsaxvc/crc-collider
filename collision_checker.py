import zlib
import crc16

crc_table = dict()
crc_table["adler32"] = ( zlib.adler32, dict() )
crc_table["crc32"] = ( zlib.crc32, dict() )
crc_table["crc16"] = ( crc16.crc16xmodem, dict() )

import fileinput
for line in fileinput.input():
	line = line.rstrip()
	for crc_type in crc_table:
		crc = crc_table[crc_type][0](line)
		if( crc in crc_table[crc_type][1] ):
			crc_table[crc_type][1][crc] += 1
		else:
			crc_table[crc_type][1][crc] = 0
import operator
for crc_type in crc_table:
	print crc_type
	old = 0
	count = 0
	for x in sorted( crc_table[crc_type][1].items(), key=operator.itemgetter(1)):
		if( x[1] != old ):
			print "\t",old, count
			old = x[1]
			count = 0
		else:
			count += 1
	print "\t",old, count
