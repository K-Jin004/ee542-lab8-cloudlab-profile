#!/usr/bin/env python3

import geni.portal as portal
import geni.rspec.pg as rspec


# ============================================================
# 1. Create the request
# ============================================================

request = portal.context.makeRequestRSpec()


# ============================================================
# 2. node0
# ============================================================

node0 = request.RawPC("node0")

# Required hardware for EE542 Lab 8 Part 7
node0.hardware_type = "d7525"

# Ubuntu 24.04
node0.disk_image = (
    "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"
)

# Experiment-network interface
iface0 = node0.addInterface("if0")

iface0.addAddress(
    rspec.IPv4Address(
        "10.10.1.1",
        "255.255.255.0"
    )
)

# Extra storage mounted at /mydata
# This is used later for Docker data because the root disk is limited.
bs0 = node0.Blockstore("bs0", "/mydata")
bs0.size = "100GB"


# ============================================================
# 3. node1
# ============================================================

node1 = request.RawPC("node1")

# Required hardware for EE542 Lab 8 Part 7
node1.hardware_type = "d7525"

# Ubuntu 24.04
node1.disk_image = (
    "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"
)

# Experiment-network interface
iface1 = node1.addInterface("if1")

iface1.addAddress(
    rspec.IPv4Address(
        "10.10.1.2",
        "255.255.255.0"
    )
)

# Extra storage mounted at /mydata
bs1 = node1.Blockstore("bs1", "/mydata")
bs1.size = "100GB"


# ============================================================
# 4. LAN connecting node0 and node1
# ============================================================

lan = request.LAN("lan")

lan.addInterface(iface0)
lan.addInterface(iface1)


# ============================================================
# 5. Output the RSpec
# ============================================================

portal.context.printRequestRSpec()
