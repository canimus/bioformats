import javabridge
import bioformats as bf
import numpy as np
import sys
from xml.etree import ElementTree as ETree
import argparse

parser = argparse.ArgumentParser(description='Bioformat extraction robot, please specify original file')
parser.add_argument('--file', metavar='file', help='file containing the image .lif extension')
parser.add_argument('--series', metavar='series', help='series number to extract from file')
parser.add_argument('--channel',metavar='channel', help='channel number to use')
parser.add_argument('--dest', metavar='dest', help='the numpy array format text file name as destination of extraction')

# Reading the file
args = parser.parse_args()

# Program Here
javabridge.start_vm(class_path=bf.JARS)

reader = bf.ImageReader(args.file, perform_init=True)
#meta = bf.get_omexml_metadata(args.file)
#xmlome = bf.OMEXML(meta)
#mdroot = ETree.fromstring(meta.encode('utf-8'))
for i in range(0,407):
    n,m = reader.read(c=args.channel, series=i, rescale=False, wants_max_intensity=True)
    np.savetxt(str(i)+args.dest, n)

javabridge.kill_vm()