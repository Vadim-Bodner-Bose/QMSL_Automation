import argparse

##################################################################################

#this defines a method, which is called every tyme an argument is added by the call type = encodeString
#this method turns a regular string to a byteobject expected by the QMSL dll
def encodeString(myString):
    # myString = str.encode()
    newString = myString.encode()
    return newString

##################################################################################
# string = encodeString("vadik")
# print (string)

parser = argparse.ArgumentParser(description='Input the parameters for TX test WCN3999 component')

parser.add_argument('phyRFMode', type=encodeString, help='parameter value for phyRFMode')
parser.add_argument('phyId', type=encodeString, help='parameter value for phyId')
parser.add_argument('channel', type=encodeString, help='parameter value for channel')
parser.add_argument('txMode', type=encodeString, help='parameter value for txMode')
parser.add_argument('wlanMode', type=encodeString, help='parameter value for wlanMode')
parser.add_argument('bandwidth', type=encodeString, help='parameter value for bandwidth')
parser.add_argument('txPower0', type=encodeString, help='parameter value for txPower0')
parser.add_argument('tpcm', type=encodeString, help='parameter value for tpcm')
parser.add_argument('rateBitIndex0', type=encodeString, help='parameter value for rateBitIndex0')
parser.add_argument('enANI', type=encodeString, help='parameter value for enANI')
parser.add_argument('scramblerOff', type=encodeString, help='parameter value for scramblerOff')
parser.add_argument('aifsn', type=encodeString, help='parameter value for aifsn')
parser.add_argument('agg', type=encodeString, help='parameter value for agg')
parser.add_argument('dutyCycle', type=encodeString, help='parameter value for dutyCycle')
parser.add_argument('pktLen0', type=encodeString, help='parameter value for pktLen0')
parser.add_argument('antenna', type=encodeString, help='parameter value for antenna')
parser.add_argument('txChain0', type=encodeString, help='parameter value for txChain0')
parser.add_argument('broadcast', type=encodeString, help='parameter value for broadcast')
parser.add_argument('shortGuard', type=encodeString, help='parameter value for shortGuard')
parser.add_argument('numPackets', type=encodeString, help='parameter value for numPackets')
parser.add_argument('txPattern', type=encodeString, help='parameter value for txPattern')
parser.add_argument('flags', type=encodeString, help='parameter value for flags')

# args = parser.parse_args()

print(args.txPattern, args.flags)