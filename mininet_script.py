from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def simpleNetwork():
    # Set up the log level
    setLogLevel('info')

    # Create an instance of Mininet
    net = Mininet(controller=RemoteController, switch=OVSSwitch, autoSetMacs=True)

    # Add a remote controller to the network
    remote_controller = net.addController(name='floodlight', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add switches to the network
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    # Interconnect the switches (fully connected mesh topology)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s1, s5)
    net.addLink(s2, s3)
    net.addLink(s2, s4)
    net.addLink(s2, s5)
    net.addLink(s3, s4)
    net.addLink(s3, s5)
    net.addLink(s4, s5)

    # Connect 4 hosts to each switch and assign IPs in the same subnet
    h1 = net.addHost('h1', ip='10.0.1.11')
    h2 = net.addHost('h2', ip='10.0.1.12')
    h3 = net.addHost('h3', ip='10.0.1.13')
    h4 = net.addHost('h4', ip='10.0.1.14')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    h5 = net.addHost('h5', ip='10.0.2.11')
    h6 = net.addHost('h6', ip='10.0.2.12')
    h7 = net.addHost('h7', ip='10.0.2.13')
    h8 = net.addHost('h8', ip='10.0.2.14')
    net.addLink(h5, s2)
    net.addLink(h6, s2)
    net.addLink(h7, s2)
    net.addLink(h8, s2)

    h9 = net.addHost('h9', ip='10.0.3.11')
    h10 = net.addHost('h10', ip='10.0.3.12')
    h11 = net.addHost('h11', ip='10.0.3.13')
    h12 = net.addHost('h12', ip='10.0.3.14')
    net.addLink(h9, s3)
    net.addLink(h10, s3)
    net.addLink(h11, s3)
    net.addLink(h12, s3)

    h13 = net.addHost('h13', ip='10.0.4.11')
    h14 = net.addHost('h14', ip='10.0.4.12')
    h15 = net.addHost('h15', ip='10.0.4.13')
    h16 = net.addHost('h16', ip='10.0.4.14')
    net.addLink(h13, s4)
    net.addLink(h14, s4)
    net.addLink(h15, s4)
    net.addLink(h16, s4)

    h17 = net.addHost('h17', ip='10.0.5.11')
    h18 = net.addHost('h18', ip='10.0.5.12')
    h19 = net.addHost('h19', ip='10.0.5.13')
    h20 = net.addHost('h20', ip='10.0.5.14')
    net.addLink(h17, s5)
    net.addLink(h18, s5)
    net.addLink(h19, s5)
    net.addLink(h20, s5)

    # Start the network
    net.start()

    # Connect the switches to the remote controller
    s1.start([remote_controller])
    s2.start([remote_controller])
    s3.start([remote_controller])
    s4.start([remote_controller])
    s5.start([remote_controller])


    # Open the CLI to interact with the network
    CLI(net)

    # Stop the network
    net.stop()

# Run the function to set up and start the network
if __name__ == '__main__':
    simpleNetwork()
