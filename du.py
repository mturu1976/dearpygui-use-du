from sh import du
from sh import sort


def ducmd():
    comannds = sort(du("-d 1", "-h"), "-rn")
    return comannds
