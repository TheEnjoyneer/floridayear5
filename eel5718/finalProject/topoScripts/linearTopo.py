# Christopher Brant
# linearTopo.py
# Linear Topology Script
# - Executes Creation of Linear Topology
# - Executes data and metric collection for topological analysis

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller, Host
from mininet.util import pmonitor


class LinearTopo(Topo):
    "Linear topology by Christopher Brant."

    def __init__(self):
        # Initialize topology
        super().__init__()

        # Add hosts
        h1 = self.addHost("h1", ip="10.0.0.1/24")
        h2 = self.addHost("h2", ip="10.0.0.2/24")
        h3 = self.addHost("h3", ip="10.0.0.3/24")
        h4 = self.addHost("h4", ip="10.0.0.4/24")
        h5 = self.addHost("h5", ip="10.0.0.5/24")
        h6 = self.addHost("h6", ip="10.0.0.6/24")
        h7 = self.addHost("h7", ip="10.0.0.7/24")
        h8 = self.addHost("h8", ip="10.0.0.8/24")

        # Add switches
        s1 = self.addSwitch("s1", cls=OVSSwitch)
        s2 = self.addSwitch("s2", cls=OVSSwitch)
        s3 = self.addSwitch("s3", cls=OVSSwitch)
        s4 = self.addSwitch("s4", cls=OVSSwitch)

        # FOR TEMPLATE HERE IS WHERE YOU'LL CREATE YOUR TOPO
        # BY ADDING THE CORRECT LINKS AND CONNECTIONS BETWEENE ALL THE HOSTS
        # AND SWITCHES AS NECESSARY FOR YOUR TOPO

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s2, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(s3, s4)
        self.addLink(h7, s4)
        self.addLink(h8, s4)


topos = {"lineartopo": (lambda: LinearTopo())}


def run():
    # Configure the network with custom topology
    topo = LinearTopo()
    c0 = Controller("c0")
    net = Mininet(topo=topo, controller=c0, switch=OVSSwitch)

    # Start the network
    net.start()

    # Get necessary nodes for running commands
    h1 = net.get("h1")
    h2 = net.get("h2")
    h3 = net.get("h3")
    h4 = net.get("h4")
    h5 = net.get("h5")
    h6 = net.get("h6")
    h7 = net.get("h7")
    h8 = net.get("h8")

    hosts = [h2, h3, h5, h7]

    # Run necessary commands
    print("Running 'pingall'\n")
    # pingAllResponse = net.pingAllFull()
    iperfResponse = net.iperf([h1, h7], l4Type='UDP', udpBw='10M', seconds=5)

    '''
    popens = {}
    last = hosts[-1]
    popens[h1] = h1.popen("iperf3 -s")
    for i in range(1, len(hosts)):
        popens[hosts[i]] = hosts[i].popen("iperf3 -c 10.0.0.1 -u")
        last = hosts[i]

    for host, line in pmonitor(popens):
        #    print("in host print loop")
        # print(str(host) + " " + line)
        if host:
            # print(host.name + " " + line)
            info("<%s>: %s" % (host.name, line))
    '''

    # Run all necessary pings
    # print("Running ping between h1 and h2")

    '''
    # Run iperf commands
    print("\nRunning 'iperf' server on h1\n")
    h1.monitor()
    h1.sendCmd("iperf3 -s -u -i 1")

    print("Output from iperf udp test from h2\n")
    print(h2.cmd("iperf -c 10.0.0.1 -u"))

    print("Output from iperf udp test from h3\n")
    print(h3.cmd('iperf -c 10.0.0.1 -u'))

   
    print("Output from iperf udp test from h5\n")
    print(h5.cmd('iperf -c 10.0.0.1 -u'))

    print("Output from iperf udp test from h7\n")
    print(h7.cmd('iperf -c 10.0.0.1 -u'))

    print("Closing iperf server on h1\n")
    h1.stop()

        '''
    # Break down the network
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    run()
