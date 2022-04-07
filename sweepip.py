import icmplib
import ipaddress

"""
    A ping sweep utility using Python

    SweepIP is a python utility built to replicate some of the
    functionality found in applications such as Angry IP Scanner but
    do so using Python.

    It will allow the user to enter an IP address and a subnet mask or
    CIDR and ping each IP in the subnet and report whether the address
    is reachable or not
"""