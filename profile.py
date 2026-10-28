"""EE542 Lab 8 Part 7 CloudLab profile.

Two d7525 bare-metal nodes on the Wisconsin cluster,
connected by an experiment LAN.

node0: 10.10.1.1/24
node1: 10.10.1.2/24
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# ------------------------------------------------------------
# node0
# ------------------------------------------------------------
node0 = request.RawPC("node0")
node0.hardware_type = "d7525"
node0.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"

iface0 = node0.addInterface("if0")
iface0.addAddress(
    rspec.IPv4Address("10.10.1.1", "255.255.255.0")
)

# Extra filesystem for Docker / large files
node0.addService(
    rspec.Execute(
        shell="bash",
        command="mkdir -p /mydata"
    )
)

# ------------------------------------------------------------
# node1
# ------------------------------------------------------------
node1 = request.RawPC("node1")
node1.hardware_type = "d7525"
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"

iface1 = node1.addInterface("if1")
iface1.addAddress(
    rspec.IPv4Address("10.10.1.2", "255.255.255.0")
)

node1.addService(
    rspec.Execute(
        shell="bash",
        command="mkdir -p /mydata"
    )
)

# ------------------------------------------------------------
# Experiment LAN
# ------------------------------------------------------------
lan = request.LAN("lan")
lan.addInterface(iface0)
lan.addInterface(iface1)

portal.context.printRequestRSpec()