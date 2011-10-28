#!/bin/env python

import os

# Get the model identifier from the DeployStudio environment variables
model_identifier = os.environ['DS_MODEL_IDENTIFIER']

# Map model identifiers to the versions of iLife that shipped with each
# This dictionary must be updated with new models as they are introduced
# Only Intel-based Mac models are included at this time
ilife_versions = {
# iMac
"iMac4,1"       : "06",
"iMac4,2"       : "06",
"iMac5,1"       : "06",
"iMac5,2"       : "06",
"iMac6,1"       : "06",
"iMac7,1"       : "08",
"iMac8,1"       : "08",
"iMac9,1"       : "09",
"iMac10,1"      : "09",
"iMac11,1"      : "09",
"iMac11,2"      : "09",
"iMac11,3"      : "09",
"iMac12,1"      : "11",
"iMac12,2"      : "11",
# Mac mini
"Macmini1,1"    : "06",
"Macmini2,1"    : "08",
"Macmini3,1"    : "09",
"Macmini4,1"    : "09",
"Macmini5,1"    : "11",
"Macmini5,2"    : "11",
"Macmini5,3"    : "11",
# Mac Pro
"MacPro1,1"     : "06",
"MacPro2,1"     : "06",
"MacPro3,1"     : "08",
"MacPro4,1"     : "09",
"MacPro5,1"     : "09",
# MacBook
"MacBook1,1"    : "06",
"MacBook2,1"    : "06",
"MacBook3,1"    : "08",
"MacBook4,1"    : "08",
"MacBook5,1"    : "08",
"MacBook5,2"    : "09",
"MacBook6,1"    : "09",
"MacBook7,1"    : "09",
# MacBook Pro
"MacBookPro1,1" : "06",
"MacBookPro1,2" : "06",
"MacBookPro2,1" : "06",
"MacBookPro2,2" : "06",
"MacBookPro3,1" : "06",
"MacBookPro4,1" : "08",
"MacBookPro5,1" : "08",
"MacBookPro5,2" : "09",
"MacBookPro5,3" : "09",
"MacBookPro5,4" : "09",
"MacBookPro5,5" : "09",
"MacBookPro6,1" : "09",
"MacBookPro6,2" : "09",
"MacBookPro7,1" : "09",
"MacBookPro8,1" : "11",
"MacBookPro8,2" : "11",
"MacBookPro8,3" : "11",
# MacBook Air
"MacBookAir1,1" : "08",
# There are two MacBookAir2,1 models that shipped with different iLife versions
"MacBookAir2,1" : "08",
# "MacBookAir2,1" : "09",
"MacBookAir3,1" : "11",
"MacBookAir3,2" : "11",
"MacBookAir4,1" : "11",
"MacBookAir4,2" : "11"
}

def install_ilife(ilife_version):
	"""
	Output RuntimeSelectWorkflow with the iLife version to be installed, if possible.
	"""
	if ilife_version:
		print('Model "%s" is known to ship with Apple iLife version %s.' % (model_identifier, ilife_version))
		workflow_name = 'Apple iLife %s' % (ilife_version)
		workflow_selection_output = "RuntimeSelectWorkflow: %s" % (workflow_name)
		print(workflow_selection_output)
	else:
		print('Model "%s" shipped with unknown Apple iLife version.' % (model_identifier))
		print('No iLife installation workflow was selected.')

if ilife_versions.has_key(model_identifier):
	install_ilife(ilife_versions[model_identifier])