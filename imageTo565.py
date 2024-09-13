
#!/usr/bin/python
import os,sys,struct
from PIL import Image

# 图片(jpg/png)转RGB565
def main():
	infile = "乐乐龙.png"
	outfile = "res.h"
	im=Image.open(infile)
	im.show()
	print("read %s\nImage Width:%d Height:%d" % (infile, im.size[0], im.size[1]))

	f = open(outfile, "wb")
	pix = im.load()  #load pixel array
	for h in range(im.size[1]):
		for w in range(im.size[0]):
			R = pix[w, h][0] >> 3
			G = pix[w, h][1] >> 2
			B = pix[w, h][2] >> 3
			rgb = (R << 11) | (G << 5) | B
			# 转换的图是小端的，所以先后半字节，再前半字节
			f.write(struct.pack('B', rgb & 255))
			f.write(struct.pack('B', (rgb >> 8) & 255))

	f.close()
	print("write to %s" % outfile)

if __name__ == "__main__":
	sys.exit(main())

