import javabridge
import bioformats as bf
import numpy as np
import argparse
from threading import Thread

parser = argparse.ArgumentParser(description='Bioformat extraction robot, please specify original file')
parser.add_argument('--file', metavar='file', help='file containing the image .lif extension')
parser.add_argument('--size', metavar='size', help='which series ranges to extract')
parser.add_argument('--dest', metavar='dest', help='the numpy array format text file name as destination of extraction')

# Reading the file
args = parser.parse_args()

# Converting range
t = tuple([int(x) for x in args.size.split(",")])
window = range(*t)

# Program Here
javabridge.start_vm(class_path=bf.JARS)

reader = bf.get_image_reader('r1', path="./180509_Permeabilisation_Test.lif")
#meta = bf.get_omexml_metadata(args.file)
#xmlome = bf.OMEXML(meta)
#mdroot = ETree.fromstring(meta.encode('utf-8'))
for i in window:
    n,m = reader.read(c=0, series=i, rescale=False, wants_max_intensity=True)
    np.savetxt(str(i)+args.dest, n)


bf.clear_image_reader_cache()
javabridge.kill_vm()