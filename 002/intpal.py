import sys

# generic mod check 
def is_palindrome(test_case):
	return str(test_case) == str(test_case)[::-1]

# processing here
def process_this(test_case):

	test_case_current = test_case.rstrip('\n')

	if is_palindrome(test_case_current):
		#print 'Whoops, %s this is already a palindrome' % test_case
		print '0 %s' % (test_case_current)
	else:
		itr = 0
		while True:
			itr+=1
			test_case_current = int(test_case_current)+int(str(test_case_current)[::-1])

			if is_palindrome(test_case_current):
				print '%d %d' % (itr,test_case_current)
				break	

# check for test cases
if len(sys.argv) <2:
	print 'Please supply test cases'
	sys.exit(0)


# read and iterate through test cases
try:
	with open(sys.argv[1], 'r') as f:
		for test_case in f:
			#print '---------------------------'
			process_this(test_case)		

	f.closed
except IOError:
	print 'Something went wrong while opening %s' % sys.argv[1]

