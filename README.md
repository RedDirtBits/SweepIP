# SweepIP

A ping sweep utility using Python.  

The name is a play on words of sort.  Instead of sweep it, it's sweep ip.  Get it?  Okay, so that's not going to win any awards.  Call it my lame attempt at creativity. 

SweepIP is a python utility built to replicate some of the functionality found in applications such as [Angry IP Scanner](https://angryip.org/) but do so using Python.  It will allow the user to enter an IP address and a subnet mask or CIDR and ping each IP in the subnet and report whether the address is reachable or not.

It's not intended to be a faithful replication, in Python, of Angry IP Scanner, rather a replication, as best I can achieve with my current python skills, the more common features I use personally and at work.

As with any of my _projects_ that I add a GUI front end to, this one also uses [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) as the framework used for that.  As far as GUI frameworks go, it is by far the best to use for quick stand-ups of a GUI front end to python applications.  My only complaint with it has been the ability to make elements and fields symmetrical, but it's such a small issue in the light of the ease to generate good looking GUI's, it remains my goto framework for such things.

# Modules Used

While both [netaddr](https://netaddr.readthedocs.io/en/latest/) and [ipaddress](https://docs.python.org/3/library/ipaddress.html) do very similar things I decided to include them both here as a way to test them both and see which is easier to work with or if there is enough difference between them to be able to make valid use of both.

In the past I have used `ipaddress` primarily as a very good IP address validator, but it can do much more and is part of the Python standard library.  I have never used `netaddr` before and may remove this if it does not prove useful or any functionality that cannot be provided by the `ipaddress` module.

## Third Party Modules

- [icmplib](https://pypi.org/project/icmplib/)

## Standard Library Modules

- [ipaddress](https://docs.python.org/3/library/ipaddress.html)

# Acknowledgements

I first have to give thanks and a shout out to [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/).  As a Linux user, I am no stranger to the command line but I know that is not common, particularly in shops dominated by MS Windows and related products.  As such I heavily gravitate to creating GUI interfaces for most python based projects I work on.  [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) makes this process about as painless and simple as it can be, even for this Python novice.

I also have to give a big shout out to [Valentin BELYN](https://github.com/ValentinBELYN) for [icmplib](https://pypi.org/project/icmplib/).  It should come as no surprise, as a network technician, that tools such as ping, traceroute, nslookup, etc. are invaluable tools that are used on a near daily basis.  I cannot fully articulate the frustration of trying to parse terminal/command line output for such tools in Python, at least for me.  I think I'd rather coat myself in the scent of a Gazelle and sit in the den of hungry lions than try and do that.  That is where [Valentin BELYN's](https://github.com/ValentinBELYN) [icmplib](https://pypi.org/project/icmplib/) comes into play.  If you are tasked with writing Python for network testing or automation purposes, do yourself a favor and check out his library.  Trust me, you can put the bottle of aspirin away now.

I like to think that someday my Python skills will grow to such an extent that I too will be able to contribute to the Python commmuity in the way that [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) and [Valentin BELYN](https://github.com/ValentinBELYN) have.  Hey, I can dream, right?

# Conclusion

This is **very** much a work in progress.  When I looked at all that would be involved in just replicating some of the functionality of AngryIP Scanner, I quickly realized I was going have to make a plan on stepping through this one chunk at a time and that it was going to be longer than a weekend project.

If you have ideas on how I could do something I have mentioned I am trying to get done or how to better do what I have already uploaded **please** reach out to me via email at `reddirtplace at protonmail dot com`.  I don't pretend to be any kind of guru at Python (looking at my code alone should tell you that) and one way I can improve is to learn what I am doing wrong or could do better, best practices, etc.  So please, feel free to contribute to my education.

This is likely going to be the biggest project I have undertaken to date.  I seem to never come up with good ideas from common things I do at home or from general computing, so I draw the bulk of my inspiration from work and mostly re-inventing the wheel by way of thinking can I do _this_ in Python and use it to learn and get better.  Perhaps at some point the lightning will strike and I will come up with some novel idea.  For now, it's looking at that wheel and concieving of ways to make it just as round in Python.

