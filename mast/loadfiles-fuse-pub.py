#loadfiles
__version__="0.1"
from pysesame import connection
from urllib import quote_plus, urlencode, quote
import os.path, sys, os, glob
import uuid

#c=connection('http://localhost:8080/openrdf-sesame/')
#c.use_repository('testads8')
#context=None
testcodeuristart='<http://ads.harvard.edu/sem/context#'
#DATA="../fuse-rdf"

if len(sys.argv)==2:
    execfile("./default-fuse.conf")
    execfile("./mast/default-mfuse.conf")
elif len(sys.argv)==3:
    execfile(sys.argv[2])
else:
    print "Usage: python loadfiles-fuse-pub.py obsvpubmatchpattern [conffile]"
    sys.exit(-1)
#c.addnamespace('fb','http://rdf.freebase.com/ns/')
#c.addnamespace('dc','http://purl.org/dc/elements/1.1/')
c=connection(SESAME)
c.use_repository(REPOSITORY)

identifier=str(uuid.uuid4())+"-"+__file__+"-"+__version__

context=quote_plus(testcodeuristart+identifier+">")
filename=DATA+"/"+sys.argv[1]+".rdf"
if not os.path.exists(filename):
    print "Path not found: "+filename
    sys.exit(-1)


if os.path.isfile(filename):
    print filename
    c.postfile(filename, context)
else:
    "FILE not found: ", filename
