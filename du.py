from sh import du


def ducmd():
    comannds = du("-d 1 -h")
    return comannds


nowdu = ducmd()

print(nowdu)
