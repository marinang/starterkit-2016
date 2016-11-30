import sys


input_file = sys.argv[1]


import GaudiPython as GP
from Configurables import DaVinci

dv = DaVinci()
dv.DataType = '2012'


from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([input_file])

def nodes(evt, node=None):
    """List all nodes in `evt`"""
    nodenames = []

    if node is None:
        root = evt.retrieveObject('')
        node = root.registry()

    if node.object():
        nodenames.append(node.identifier())
        for l in evt.leaves(node):
            # skip a location that takes forever to load
            # XXX How to detect these automatically??
            if 'Swum' in l.identifier():
                continue

            temp = evt[l.identifier()]
            nodenames += nodes(evt, l)

    else:
        nodenames.append(node.identifier())

    return nodenames


appMgr = GP.AppMgr()
evt = appMgr.evtsvc()
appMgr.run(1)
evt.dump()

def advance(line):
	n = 0
	while True:
		appMgr.run(1)

		if not evt['/Event/Rec/Header']:
			break

		n += 1
		# check if the line is fired
		dec = evt['/Event/Strip/Phys/DecReports']
		if dec.hasDecisionName('Stripping{}Decision'.format(line)):
			break
	return n




	
