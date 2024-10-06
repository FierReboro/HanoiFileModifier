import os

if __name__ == "__main__":
	file_to_modify = "f1.txt"
	tempfile = "f2.txt"

def __seek_read(file_, pointer):
	file_.seek(pointer)
	b = file_.read(1)
	return b

def __modifier(c):
	if len(c) == 0:
		return b''
	c = c.rstrip()
	print(77777, c)
	return c + b'\n'

def __transfer(sfile, targetfile, pointer, increment, func=__modifier):
#reads lines from sfile(the source) and appends it to targetfile,... 
#...and the line gets truncated from sfile
	sfile.seek(pointer+increment)
	sourcline = sfile.readline()
	sourcline = func(sourcline)
	targetfile.write(sourcline)
	sfile.truncate(pointer+increment)
	sfile.flush()
	targetfile.flush()
	print("sfile is now ",os.path.getsize(file_to_modify),"bytes\n", "tempfile is now ", os.path.getsize(tempfile), "bytes")

def start(sfile, tempfile):
	sfile = open(sfile, "br+")
	tempfile = open(tempfile, "ba")
	z = sfile.seek(0,2) #"final byte"
	while True:
		p = __seek_read(sfile, z) #"char at pointer"
		if p == b'\n':
			__transfer(sfile, tempfile, z, 1)
				#we temporarily add 1 to z, since z is where the "\n" is located
				#we only want the characters after it.
		elif z==0:
			__transfer(sfile, tempfile, z, 0) 
				#"if z==0, adding 1 will move the seek(z) to 1, 
				#therefore 1 byte will remain at the end of operation
		z -= 1
		if z == -1:
			break

if __name__ == "__main__":
	start(file_to_modify, tempfile)
	start(tempfile, file_to_modify)
