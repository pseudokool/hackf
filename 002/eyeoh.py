import sys, pprint, logging

# check for test cases
if len(sys.argv) <2:
	print 'Please supply test cases'
	sys.exit(0)

# string to array, split on whitespace
def r2a(test_case):
	#print test_case
	#sys.exit(0)
	return test_case.split()

# process
def process(darr, c1, c2, cop):
	team = None
	gd = None

	for dr in darr:
		
		# test condition here	
		try:	
			
			if dr[0].endswith(".") or int(dr[0])>0:
				#print dr[8]
				#print '---------------------'
				
				# update for no initials
				if gd is None:
					gd = abs(int(dr[c1])-int(dr[c2]))
					team = dr[cop]
					#print 'Ngd:%s Nteam:%s' % (gd,team)

					continue

				# process for non nulls
				#print 'Wgd:%s Wteam:%s' % (gd,team)
				
				#print 'C_GF:%d C_GA:%d ' % (int(dr[6]),int(dr[8]))

				if abs(int(dr[c1])-int(dr[c2]))<gd:
					gd = abs(int(dr[c1])-int(dr[c2]))
					team = dr[cop]
		except Exception:
			logging.warning('Empty array')

	#print '\n%s %' % gd
	print '%s' % team

	return True

# read and iterate through test cases
farr = []	# files to process
try:
	for farg in range(1, len(sys.argv)):
		
		with open(sys.argv[farg], 'r') as f:
			darr = []	# data 

			fcnt=0
			for test_case in f:
				fcnt=fcnt+1
					
				if fcnt==1:
					continue

				darr.append(r2a(test_case.rstrip('\n'))) 		
				
		farr.append(darr)	

	print len(farr)
	process(farr[0], 6, 8, 1)
	process(farr[1], 1, 2, 0)
					
	f.closed
except IOError:
	print 'Something went wrong while opening %s' % sys.argv[1]

pp = pprint.PrettyPrinter(indent=2)
#print pp.pprint(farr)