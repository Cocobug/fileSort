# -*- coding:utf8 -*-

###########################################
# Auteur: Malphaet                        #
# Copyright 2011: Malphaet                #
###########################################
# This file is part of fileSort.
#
# fileSort is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fileSort is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fileSort. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

######################
#     Functions      #
######################

######################
#----- Utilities ----#
#--------------------#
def a_dirs(a,b):
	return os.path.join(a.strip(),b.strip())

def get_dir(a,b):
	a=a.strip()
	if a[0]=='~': return os.path.expanduser(a)
	if a[0]=='/': return a
	if a[:2]=='./': a=a[2:]
	
	return a_dirs(b,a)
	
def verbose_a(action,f,place=''):
	if VV:
		sent=action.capitalize()+' '+f
		if place: sent+=' to '+place
		print " -> "+sent

def s_info(**kwargs):
	for name,attr in kwargs.iteritems():
		print '\n	',name.capitalize()+':',attr
	return ' '

#######################
#- Applied functions -#
#---------------------#

def relink(f,place,folder,function):
	place=get_dir(place,folder)
	src,dest=get_dir(f,folder),a_dirs(place,NAME(f))
	if os.path.exists(dest) and not OVERWRITE: 
		print "    Destination file exist (skipped)"
		return
	try:
		os.makedirs(place)
		print "Creating",place
	except: pass
	try:
		function(src,dest)
	except: print "Moving Failed",sys.exc_info()[1]

def move(f,place,section):
	relink(f,place,section,shutil.move)
	verbose_a('moving',f,place)

def copy(f,place,section):
	relink(f,place,section,shutil.copy2)
	verbose_a('copying',f,place)

def delete(f,place,section):
	verbose_a('deleting',f)
	try:
		os.remove(a_dirs(section,f))
	except: print "Removing Failed", sys.exc_info()[1]

def guess_type(temp_infos,value):
	if type(value)!=str: return value
	if type(temp_infos)==str:
		value,temp_infos=value.lower(),str(temp_infos).lower()
	else:
		if type(temp_infos)==int:
			value=int(value)
		else:
			if type(temp_infos)==float:
				value=time.mktime(time.strptime(value,"%d %m %y, %H %M %S"))
	return value
##########################
#--- Pattern Functions --#
#------------------------#

def IS(a,b):
	return a==b

def IS_NOT(a,b):
	return not IS(a,b)

def CONTAINS(a,b):
	return a in b

def CONTAINS_NOT(a,b):
	return not CONTAINS(a,b)

def STARTS(a,b):
	si=len(a)
	if len(b)<si: return False
	return b[:len(a)]==a

def ENDS(a,b):
	la,lb=len(a),len(b)
	if lb<la: return False
	return b[lb-la:]==a

def MORE(a,b):
	return a<=b

def LESS(a,b):
	return not MORE(a,b)

##########################
#- Recognition funtions -#
#------------------------#

def TYPE(f):
	t=mimetypes.guess_type(f)[0]
	if t!=None: return t
	else: return ""
def NAME(f):
	return os.path.basename(f)
def EXT(f):
	return os.path.splitext(f)[1]
def SIZE(f):
	return int(os.path.getsize(f))
def TIME(f):
	return os.path.getctime(f)
