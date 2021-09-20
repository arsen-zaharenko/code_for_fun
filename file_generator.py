from random import random, randint
import sys
import argparse

def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '#', print_end = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(iteration)
    filled_length = int(length * iteration // total)
    bar = '|' + fill * filled_length + '-' * (length - filled_length) + '|'
    print(prefix, bar, percent, '%', suffix, end = print_end)
    if iteration == total: 
        print()

def generate():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n',type = str, default = 'file',help = "This is name of file (default = 'file')")
	parser.add_argument('-s',type = int, default = 1,help = "This is size of file (default = 1)")
	parser.add_argument('-la',type = int,default = 3,help = "This is 'a' for length of words (default = 3)")
	parser.add_argument('-lb',type = int,default = 10,help = "This is 'b' for length of words (default = 10)")
	parser.add_argument('-wa',type = int,default = 10,help = "This is 'a' for quantity of words (default = 10)")
	parser.add_argument('-wb',type = int,default = 100,help = "This is 'b' for quantity of words (default = 100)")
	
	args = parser.parse_args()
	name = args.n
	size = args.s
	length_a = args.la
	length_b = args.lb
	if length_a > length_b or length_a < 1 or length_b < 1:
		print('Invalid input')
		sys.exit(0)
	words_a = args.wa
	words_b = args.wb
	if words_a > words_b or words_a < 1 or words_b < 1:
		print('Invalid input')
		sys.exit(0)

	file = open(name + '.txt', 'tw', encoding='utf-8')
	size = size_max = size*1048576	

	progress = 0

	while size:
		words_rand = randint(words_a,words_b)
		for i in range(words_rand):
			length_rand = randint(length_a,length_b)
			for j in range(length_rand):
				if randint(0,1):
					file.write(chr(randint(65,90)))
				else:
					file.write(chr(randint(97,122)))	
				if int((1 - size/size_max)*100) == progress:
					print_progress_bar(progress + random(), 100, prefix = 'Progress:')
					progress += 1
				size -= 1
				if not size:
					file.close()
					print_progress_bar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
					sys.exit(0)
			if i < words_rand - 1:
				file.write(' ')
				if int((1 - size/size_max)*100) == progress:
						print_progress_bar(progress + random(), 100, prefix = 'Progress:')
						progress += 1
				size -= 1
			if not size:
				file.close()
				print_progress_bar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
				sys.exit(0)
		file.write('\n')
		if int((1 - size/size_max)*100) == progress:
					print_progress_bar(progress + random(), 100, prefix = 'Progress:')
					progress += 1
		size -= 2
		if not size:
			file.close()
			print_progress_bar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
			sys.exit(0)

if __name__ == '__main__':
	generate()