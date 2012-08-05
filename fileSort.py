# Moooo
# Stuff


import ConfigParser,mimetypes
import sys,os

#############
# Functions #
#############

#- Utilities -#

def verbose_a(action,f,place=''):
	if VV:
		sent=action+' '+f
		if place: sent+=' to '+place
		print "    "+sent

def s_info(**kwargs):
	for name,attr in kwargs.iteritems():
		print '\n	',name.capitalize()+':',attr
	return ' '

#- Applied functions -#
def move(f,place):
	verbose_a('moving',f,place)

def copy(f,place):
	verbose_a('copying',f,place)

def delete(f,place):
	verbose_a('deleting',f)
	os.remove(f)

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
	sys.exit()

mimetypes.init()
VV=True

if (len(sys.argv)<2): raise(ValueError("Enter Config Path !"))

try:
	parser=ConfigParser.SafeConfigParser()
	parser.read(sys.argv[1])
except:
	print "Your config file is strange"
	sys.exit()

for section in parser.sections():
	if VV: print "Working in", section
	try: files=os.listdir(section)
	except OSError:
		print "The path you provided is incorrect:",s_info(section=section)
		continue
	

	for element,action in parser.items(section):
		try:
			seeked,value=element.split('.')
			value=value.split('(')
			pattern=value[0]
			value=value[1][:-1]
			
			seek=PATTERNS[pattern]
			infos=INFOS[seeked]
		except KeyError: 
			sys.stderr.write("Warnning: "+str(sys.exc_info()[1])+" is not a valable name (skipped)\n")
			continue
		except ValueError,IndexError:
			sys.stderr.write("Warnning: Malformed config file ({}) (skipped)\n".format(element))
			continue
		except:
			print "Unexpected error", sys.exc_info()[0]
			sys.exit()
		
		#if seeked not in INFOS:	
		#	print "Warnning: {} is not an implemented attribute (skip) (section:{})".format(seeked,section)
		#	continue
		
		t_action=action[:1]
		if (t_action==":" or t_action=="!"): action = action[1:]
		else: t_action=''
		
		
		for f in files:
			try:
				if seek(value.lower(),str(infos(section+'/'+f)[0]).lower()):
					FUNCTIONS[t_action](f,action)
			except:
				print "Unexpected error:", sys.exc_info(), sys.exit()
    			
