'''import sys
for line in sys.stdin:
	line=line.strip()
	words=line.split()
	for word in words:
		print('%s \t %s'%(word,1))'''


for line in open(r'data.txt'):
	print(line)
	line=line.strip()
	words=line.split()
	print(words)
	for word in words:
		print('%s \t %s'%(word,1))