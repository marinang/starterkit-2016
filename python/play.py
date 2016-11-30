#!/usr/bin/env python


def func(base, summed, exp=2):
	'''function used as example
	take 2 numbers and return the ...'''
	
	return base**exp+summed

	#func(*ll) ll=[1,2,3]
	#func(**dd) dd={'base':2, 'exp':4, 'summed':3}
	#The base i {base}, lalala {lalala}'.format(**dd)
	#'The base i {0}, lalala {1}'.format(*[1,3])

def sumArgs(*argv):
	for i in argv:
		print i
	return sum(argv)

def printDict(**argk):
	for key,val in argk.iteritems(): 
		print key,val


def printFunction(func,*argv,**argk):
	print 'The result of the function is', func(*argv,**argk)

a = 42

if __name__ == '__main__':
	print 'Hello World !'
	print a

	b = 34
