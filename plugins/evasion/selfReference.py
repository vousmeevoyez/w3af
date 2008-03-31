'''
selfReference.py

Copyright 2006 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''

from core.controllers.basePlugin.baseEvasionPlugin import baseEvasionPlugin
from core.controllers.w3afException import w3afException
import core.data.parsers.urlParser as urlParser
import urllib2
# options
from core.data.options.option import option
from core.data.options.optionList import optionList

class selfReference(baseEvasionPlugin):
    '''
    Add a directory self reference.
    @author: Andres Riancho ( andres.riancho@gmail.com )
    '''

    def __init__(self):
        baseEvasionPlugin.__init__(self)

    def modifyRequest(self, request ):
        '''
        Mangles the request
        
        @parameter request: urllib2.Request instance that is going to be modified by the evasion plugin
        '''
        # We mangle the URL
        path = urlParser.getPathQs( request.get_full_url() )
        path = path.replace('/','/./' )
        
        # Finally, we set all the mutants to the request in order to return it
        url = urlParser.getProtocol( request.get_full_url() )
        url += '://' + urlParser.getDomain( request.get_full_url() ) + path        
        new_req = urllib2.Request( url , request.get_data(), request.headers, request.get_origin_req_host() )
        
        return request
    
    def getOptions( self ):
        '''
        @return: A list of option objects for this plugin.
        '''    
        ol = optionList()
        return ol

    def setOptions( self, OptionList ):
        '''
        This method sets all the options that are configured using the user interface 
        generated by the framework using the result of getOptions().
        
        @parameter OptionList: A dictionary with the options for the plugin.
        @return: No value is returned.
        ''' 
        pass
        
    def getPluginDeps( self ):
        return []

    def getPriority( self ):
        '''
        This function is called when sorting evasion plugins.
        Each evasion plugin should implement this.
        
        @return: An integer specifying the priority. 0 is runned first, 100 last.
        '''
        return 0

    def getLongDesc( self ):
        '''
        @return: A DETAILED description of the plugin functions and features.
        '''
        return '''
        This evasion plugin adds a directory self reference.
        
        Example:
            Input:      '/bar/foo.asp'
            Output :    '/bar/./foo.asp'
        '''
