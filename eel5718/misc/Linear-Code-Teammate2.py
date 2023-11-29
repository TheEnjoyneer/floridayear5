from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller

class LinearTopo(Topo):
    "Linear topology by Teammate2 (Christopher Brant)."

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

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, h5)
        self.addLink(s4, h6)
        self.addLink(s4, h7)
        self.addLink(s4, h8)


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

    # Run necessary commands
    print("Running 'pingall'\n")
    print(net.pingAll())

    print("\nRunning 'qperf' server on h1\n")
    h1.sendCmd("qperf")

    print("Output from qperf tcp latency test from h2\n")
    print(h2.cmd("qperf -vvs 10.0.0.1 tcp_lat"))
    print("Output from qperf udp latency test from h2\n")
    print(h2.cmd("qperf -vvs 10.0.0.1 udp_lat"))

    print("Output from qperf tcp latency test from h3\n")
    print(h3.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h3\n")
    print(h3.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Output from qperf tcp latency test from h4\n")
    print(h4.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h4\n")
    print(h4.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Output from qperf tcp latency test from h5\n")
    print(h5.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h5\n")
    print(h5.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Output from qperf tcp latency test from h6\n")
    print(h6.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h6\n")
    print(h6.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Output from qperf tcp latency test from h7\n")
    print(h7.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h7\n")
    print(h7.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Output from qperf tcp latency test from h8\n")
    print(h8.cmd('qperf -vvs 10.0.0.1 tcp_lat'))
    print("Output from qperf udp latency test from h8\n")
    print(h8.cmd('qperf -vvs 10.0.0.1 udp_lat'))

    print("Closing qperf server on h1\n")
    h1.stop()
    # Break down the network
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    run()
