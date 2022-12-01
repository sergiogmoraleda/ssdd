import Ice
Ice.loadSlice('iceFlix.ice')
import iceflix

import os
import logging

###########___SERVANT___############

class AuthServant(IceFlix.Authenticator):
    
    def loadUsers(self):
        #TODO:
        return 0
    
    def __init__(self, users_file):
        self.users_file = users_file
        if os.path.exists(users_file) == False:
            raise FileNotFoundError(' Users file does not found.\n')
        else:
            self.loadUsers()
    
    def addUser(self, user, passwordHash, adminToken):
        #TODO:
        return 0
    
    def removeUser(self, user, adminToken):
        #TODO:
        return 0
    
    def whois(self, userToken):
        #TODO:
        return 0        
    
    def isAuthorized(self, userToken):
        #TODO:
        return False
    
    def isAdmin(self, userToken):
        #TODO:
        return False
    
    def refreshAuthorization(self, user, passwordHash):
        #TODO:
        return 0
    
    
###########___SERVER___############

class AuthServer(Ice.Application):
     def run(self, args):
        """Run the application, adding the needed objects to the adapter."""
        logging.info("Running Main application")
        comm = self.communicator()
        self.adapter = comm.createObjectAdapter("MainAdapter")
        self.adapter.activate()

        self.proxy = self.adapter.addWithUUID(self.servant)

        self.shutdownOnInterrupt()
        comm.waitForShutdown()

        return 0
