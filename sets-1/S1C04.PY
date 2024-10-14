import S1C03
import os
import linecache

def main():
	contents=linecache.getlines('4.txt')
	candidate=[]
	for string in contents:
		hex_string=bytes.fromhex(string)
		candidate.append(S1C03.Traversal_singlechar(hex_string))
	print (sorted(candidate,key=lambda c:c['score'])[-1]['plaintext'])
if __name__ == '__main__':
	main()
