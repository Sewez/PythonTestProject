with open("test.txt", 'w+') as f:
	i = 68
	while i < 99:
		stinglist = ["case {0}:\n".format(i), "\tVEHCONFIG.byte(0) = {0};\n".format(format(i, '#04x')), "\tVEHCONFIG.byte(1) = 0x00;\n", \
					"\tVEHCONFIG.byte(2) = 0x00;\n", "\tVEHCONFIG.byte(3) = 0x00;\n", "\tVEHCONFIG.byte(4) = 0x00;\n", "\tVEHCONFIG.byte(5) = 0x00;\n", \
					"\tVEHCONFIG.byte(6) = 0x00;\n", "\tVEHCONFIG.byte(7) = 0x00;\n", "\toutput(VEHCONFIG);\n", "break;\n"]
		f.writelines(stinglist)
		#f.write("VEHCONFIG.byte(0) = 0x44;\n")
		i += 1
	
