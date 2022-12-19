import re
import argparse
import os
import glob

def removeSpace(sentences):
	for idx, val in enumerate(sentences):
		if val[0] == ' ':
			val = val[1:]
		sentences[idx] = val
	return sentences

parser = argparse.ArgumentParser(prog='wordFinder', description='Get the sentence out of a word or phrase')
parser.add_argument('-d', '--directory', type=str, default=os.getcwd(), help='enter the directory')
parser.add_argument('-w','--word', type=str, nargs='*', help='word or phrase to search')
parser.add_argument('-a','--all', action='store_true', help='scan all .txt')
parser.add_argument('-n','--names', type=str, nargs='*', help='enter name of the file(s)')
parser.add_argument('-e','--extensions', type=str, nargs='*', default=['.txt','.doc','.docx'], help='specify file extension')
parser.add_argument('-s','--sentences', type=int, default=1, help='number of sentences that come after')
args = parser.parse_args()

if args.directory == os.getcwd() and args.all == False:
	fileList = args.names

elif args.directory == os.getcwd() and args.all == True:
	allExtensions = ['*'+i for i in args.extensions]
	fileList = [file for i in allExtensions for file in glob.glob(i)]

elif args.directory != os.getcwd() and args.all == False:
	fileDirectory = args.directory
	fileList = args.names

elif args.directory != os.getcwd() and args.all == True:
	os.chdir(args.directory)
	allExtensions = ['*'+i for i in args.extensions]
	fileList = [file for i in allExtensions for file in glob.glob(i)]



pattern = re.compile('[\w+\s]+[.?!]')
for file in fileList:
	print('                  '+file)
	with open(file) as f:
		allSentences = re.findall (pattern, f.read())
		allSentences = removeSpace(allSentences)
		for index, sentence in enumerate(allSentences):
			if args.word[0].lower() in sentence.lower():
				for num in range(args.sentences):
					if index + num >= len(allSentences):
						print(allSentences[index])
						break
					else:
						print(allSentences[index + num])
				print('\n')
	print('\n')
