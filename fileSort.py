# Moooo
# Stuff


import ConfigParser,mimetypes,argparse
import sys,os,shutil

#############
# Functions #
#############

#- Utilities -#

def a_dirs(a,b):
	if a[-1]!='/': a=a+'/'
	if b.strip()[:2]=='./': b=b[3:]
	return a+b

def verbose_a(action,f,place=''):
	if VV:
		sent=action+' '+f
		if place: sent+=' to '+place
		print " -> "+sent.capitalize()

def s_info(**kwargs):
	for name,attr in kwargs.iteritems():
		print '\n	',name.capitalize()+':',attr
	return ' '

#- Applied functions -#

def relink(f,place,folder,function):
	verbose_a('copying',f,place)
	place,src,dest=a_dirs(section,place),a_dirs(section,f),a_dirs(a_dirs(section,place),NAME(f))
	if os.path.exists(dest) and not OVERWRITE: 
		print "    Destination file exist (skipped)"
		return
	try:
		os.makedirs(place)
		print "Creating",place
	except: pass
	try:
		function(src,dest)
	except: print "Moving Failed",sys.exc_info()

def move(f,place,section):
	relink(f,place,section,shutil.copy2)

def copy(f,place,section):
	relink(f,place,section,shutil.copy2)

def delete(f,place,section):
	verbose_a('deleting',f)
	try:
		os.remove(a_dirs(section,f))
	except: "Removing Failed", sys.exc_info()[1]

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

parser=argparse.ArgumentParser(description="Read a config file and apply it's rules")
parser.add_argument('conf', metavar='config', nargs='+', type=str,help='a config file to apply')
parser.add_argument('-v','--verbose', dest='VV', action='store_const', const=True, help='be verbose')
parser.add_argument('-f','--force', dest='OVERWRITE', action='store_const', const=True, default=False, help='overwrite destination data')
args = parser.parse_args()

VV,OVERWRITE,conf=args.VV,args.OVERWRITE,args.conf

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
			value=value[1].strip()[:-1]
			
			seek=PATTERNS[pattern]
			infos=INFOS[seeked]
		except KeyError: 
			sys.stderr.write("Warnning: "+str(sys.exc_info()[1])+" is not a correct name (skipped)\n")
			continue
		except (ValueError, IndexError):
			sys.stderr.write("Warnning: Malformed config file (-> {}) (skipped)\n".format(element))
			continue
		except:
			print "Unexpected error", sys.exc_info()
			sys.exit()
		
		t_action=action[:1]
		if (t_action==":" or t_action=="!"): action = action[1:]
		else: t_action=''
		
		
		for f in files:
			try:
				if seek(value.lower(),str(infos(a_dirs(section,f))[0]).lower()):
					FUNCTIONS[t_action](f,action,section)
			except:
				print "Unexpected error:", sys.exc_info(), sys.exit()
    			
