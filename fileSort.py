# Moooo
# Stuff


import ConfigParser,mimetypes
import sys,os
#############
# Functions #
#############

#- Applied functions -#
def move(f,place):
	print 'moving',f,'to',place

def copy(f,place):
	print 'copying',f,'to',place

def delete(f,place):
	print 'deleting',f

FUNCTIONS={'':move,'!':delete,':':copy}

#- Recognition funtions -#

def TYPE(f):
	return mimetypes.guess_type(f)
def NAME(f):
	return f.split('/')[-1]

INFOS={'type':TYPE,'name':NAME}

#- Pattern Functions -#

def IS(a,b):
	return a==b

def IS_NOT(a,b):
	return not IS(a,b)

def CONTAINS(a,b):
	return a in b

def CONTAINS_NOT(a,b):
	return not CONTAINS(a,b)

PATTERNS={'is':IS,'is_not':IS_NOT,'contains':CONTAINS,'contains_not':CONTAINS_NOT}

################
# Main Program #
################

if __name__!="__main__":
	raise

mimetypes.init()

if (len(sys.argv)<2): raise(ValueError("Enter Config Path !"))

try:
	parser=ConfigParser.SafeConfigParser()
	parser.read(sys.argv[1])
except:
	print "Your config file is strange"
	raise

for section in parser.sections():
	for element,action in parser.items(section):
		files=os.listdir(section)
		
		seeked,value=element.split('.')
		value=value.split('(')
		pattern=value[0]
		value=value[1][:-1]

#		print seeked,pattern,value

		t_action=action[:1]
		if (t_action==":" or t_action=="!"): action = action[1:]
		else: t_action=''
		
		for f in files:
#			print str((INFOS[seeked](section+'/'+f))[0]),f
			if PATTERNS[pattern](value,str((INFOS[seeked](section+'/'+f))[0])):
				FUNCTIONS[t_action](f,action)
