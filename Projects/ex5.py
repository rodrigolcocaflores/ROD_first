# %d will format a number for display.
# %s will insert the presentation string representation of the object (i.e. str(o))
# %r will insert the canonical string representation of the object (i.e. repr(o))

my_name = 'Rodrigo L. Coca Flores'
my_age = 25 # not a lie
my_height = 70 # inches
my_weight = 185 # pounds
my_eyes = 'brown' # like poop
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "Actually that is not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are actually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it excatly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#Exercise

my_name = 'Hilary Landa'
my_age = 27
my_height 
