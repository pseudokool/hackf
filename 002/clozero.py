import sys

# check for test cases
if len(sys.argv) <2:
	print 'Please supply test cases'
	sys.exit(0)


# read and iterate through test cases
test_cases = []
cidx1 = 0
cidx2 = 0

try:
	with open(sys.argv[1], 'r') as f:
		for test_case in f:
			test_cases.append(int(test_case.rstrip('\n'))) 		
	f.closed
except IOError:
	print 'Something went wrong while opening %s' % sys.argv[1]

# iterate
for idx1,test_case in enumerate(test_cases):
	for idx2,test_case2 in enumerate(test_cases):
		#print "This:%d Chosen:%d" % (abs(test_case+test_case2), abs(test_cases[cidx1]+test_cases[cidx2]))	
		
		# skip same index
		if idx1==idx2:
			continue

		if abs(test_case+test_case2) < abs(test_cases[cidx1]+test_cases[cidx2]):
			cidx1=idx1
			cidx2=idx2

			#print "%d and %d" % (test_case,test_case2)

print "Lowest Sum for %d %d" % (test_cases[cidx1],test_cases[cidx2])