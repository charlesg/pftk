'''
(c) 2018, charlesg@unixrealm.com - Fork from QSTK
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license. Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on Apr 22, 2011

@author: shreyas
@contact: dbratcher@gatech.edu
@summary: This is intended to be a collection of helper routines used by different pftk modules
'''

import os

global_cache = {}

def cached_listdir(path):
    '''
    @summary: Replacement for Python2 dircache compatible with Python3
    '''
    res = global_cache.get(path)
    if res is None:
        res = os.listdir(path)
        global_cache[path] = res
    return res

def clean_paths (paths_to_clean):
    '''
    @summary: Removes any previous files in the list of paths.
    '''

    if (type(paths_to_clean) is str):
        temp= paths_to_clean
        paths_to_clean= list()
        paths_to_clean.append(temp)
    #endif
    
    for path in paths_to_clean:
        files_at_this_path = cached_listdir(str(path))
        for _file in files_at_this_path:
            if (os.path.isfile(path + _file)):
                os.remove(path + _file)
                #if ends 
        #for ends
    #outer for ends   



#clean_output_paths  ends
