human = "Rachel"
human_age = 23
cat = "Andromeda"
if human_age > 10 and human != cat:
  print "%s is %d." % (human, human_age)

cat_names =  ["Fluffy", "Sprinkles", "Cuddley", "Banana"]
if cat_names[1] in cat_names:
  print "found %s" % (cat_names[1])
if cat in cat_names:
  print "found %s" % (cat)
else:
  print "did not find %s" % (cat)

x = None
y = None
# If x is bigger then 0, print POSITIVE
# If x is bigger then y, but not bigger then 0, print Still Going Strong!
# If x and y are the same, or x is smaller, print gotcha...
if x > 0:
  print "POSITIVE"
elif x > y:
  print "Still Going Strong!"
else:
  print "gotcha"

# For every number between 1 and 100
# If is a multiple of 3, print FIZZ
# if x is a multiple of 5, pring BUZZ
# if x is a multiple of both 3 and 5, pring FIZZBUZZ
counter = 1
maximum = 100
while counter <= maximum:
  if counter % 3 == 0 and counter % 5 == 0:
    print "FIZZBUZZ"
  elif counter % 3 == 0:
    print "FIZZ"
  elif counter % 5 == 0:
    print "BUZZ"
  else:
    print counter
  counter = counter + 1
