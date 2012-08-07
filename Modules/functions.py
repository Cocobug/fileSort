# -*- coding:utf8 -*-

###########################################
# Date: 2012                              #
# Auteur: Malphaet                        #
# Nom: fileSort                           #
# Version: 0.1a                           #
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

def verbose_a(action,f,place=''):
	if VV:
		sent=action+' '+f
		if place: sent+=' to '+place
		print " -> "+sent.capitalize()

def s_info(**kwargs):
	for name,attr in kwargs.iteritems():
		print '\n	',name.capitalize()+':',attr
	return ' '

#######################
#- Applied functions -#
#---------------------#

def relink(f,place,folder,function):
	place,src,dest=a_dirs(folder,place),a_dirs(folder,f),a_dirs(a_dirs(folder,place),NAME(f))
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
	verbose_a('moving',f,place)
	relink(f,place,section,shutil.move)

def copy(f,place,section):
	verbose_a('copying',f,place)
	relink(f,place,section,shutil.copy2)

def delete(f,place,section):
	verbose_a('deleting',f)
	try:
		os.remove(a_dirs(section,f))
	except: print "Removing Failed", sys.exc_info()[1]

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

##########################
#- Recognition funtions -#
#------------------------#

def TYPE(f):
	return mimetypes.guess_type(f)
def NAME(f):
	return os.path.basename(f)	
	
