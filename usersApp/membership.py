import random
from random import randint
import datetime
from datetime import timedelta



def createNumberMembership():
    numbreCard = random.randint(0,9999_9999_9999_9999)
    print(numbreCard)

    traspast = str(numbreCard)


    separator = '{} {} {} {}'.format(traspast[:4],traspast[4:8],traspast[8:12],traspast[12:])
    print(separator)


createNumberMembership()