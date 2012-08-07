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
#----- Modules ------#
######################

#---- Importation ---#

import ConfigParser,mimetypes,argparse
import sys,os,shutil

#------ Ajouts ------#
#sys.path.append('Modules')
#from functions import exec_conf
execfile('Modules/functions.py')
######################
#     Functions      #
######################

FUNCTIONS={'':move,'!':delete,':':copy}

INFOS={'type':TYPE,'name':NAME}

PATTERNS={'is':IS,'is_not':IS_NOT,'contains':CONTAINS,'contains_not':CONTAINS_NOT}


def exec_conf(config):
	try:
		parser=ConfigParser.SafeConfigParser()
		parser.read(config)
	except:
		print "Your config file is weird",config
		return

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
					if seek(value.lower(),str(infos(a_dirs(section,f))).lower()):
						FUNCTIONS[t_action](f,action,section)
				except:
					print "Unexpected error:", sys.exc_info(), sys.exit()

#######################
#---- Main Program ---#
#######################

#######################
#------- Init --------#
#---------------------#

mimetypes.init()

#---------------------#
#------ Parser -------#

parser=argparse.ArgumentParser(description="Read a config file and apply it's rules")
parser.add_argument('conf', metavar='config', nargs='+', type=str,help='a config file to apply')
parser.add_argument('-v','--verbose', dest='VV', action='store_const', const=True, help='be verbose')
parser.add_argument('-f','--force', dest='OVERWRITE', action='store_const', const=True, default=False, help='overwrite destination data')
args = parser.parse_args()

VV,OVERWRITE,conf=args.VV,args.OVERWRITE,args.conf

for config in conf:
	exec_conf(config)
					
