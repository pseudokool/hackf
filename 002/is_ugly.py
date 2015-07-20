import sys

# generic mod check 
def is_div(dividend, divisor):
	if int(dividend.rstrip('\n'))%divisor==0:
		return True
	else:
		return False


# check for test cases
if len(sys.argv) <2:
	print 'Please supply test cases'
	sys.exit(0)


# read and iterate through test cases
try:
	with open(sys.argv[1], 'r') as f:
		for test_case in f:
			
			if is_div(test_case, 2) or is_div(test_case, 3) or is_div(test_case, 5) or is_div(test_case, 7):
				print test_case.rstrip('\n') 		
	f.closed
except IOError:
	print 'Something went wrong while opening %s' % sys.argv[1]

