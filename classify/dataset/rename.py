import argparse
import os

def run(args):
	input_file = args.input
	name_img = args.nameimage # from dest="output"
	# print(input_file+";"+name_img)
	i = 0
	for filename in os.listdir(input_file):
		my_dest = name_img + str(i) + ".jpg"
		my_source =input_file + filename
		my_dest =input_file + my_dest
		# rename() function will
		# rename all the files
		os.rename(my_source, my_dest)
		i += 1

def main():
	parser=argparse.ArgumentParser(description="Remane")
	parser.add_argument("-in",help="fasta input file" ,dest="input", type=str, required=True)
	parser.add_argument("-image",help="name image" ,dest="nameimage", type=str, required=True)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)
#python rename.py -in ball/ -image ball_

if __name__=="__main__":
	main()
