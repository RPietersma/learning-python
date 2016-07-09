catname = "Andromeda"
print len(catname)

dloc = catname.index("m")
print dloc

print catname.count("d")

print catname[0:5]

# Andromeda is a cutie!
message = "Andromeda is not a cutie!"
print message[0:13] + message[17:25]
print("%s %s") % (message[0:12], message[17:25])

print message[::-1]

# I'm so happy we have her!
newmsg = "I'm so sad we have such a bad cat"
print("%s" "happy" "%s" "her!") % (newmsg[0:7], newmsg[10:19])

print catname.upper()
print "Rachel".upper()

if message.startswith("Andromeda"):
  print newmsg

splitmsg = message.split(" ")
print " ".join(splitmsg)

