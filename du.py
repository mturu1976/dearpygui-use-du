from sh import du
from sh import sort
from sh import pwd

def ducmd():
    comannds = sort(du("-d 1", "-h"), "-rn")
    return comannds

def pwdcmd():
    comannds = pwd()
    return comannds