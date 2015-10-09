#
# File Header
#
# Add your name to this

# Define a function called piggy(string) that returns a string
piggy = "string"

def piggy(word):
	
	# Magic Happens Here
	pig = word
	# Ignore previous line
	
	return pig

# Open the file *getty.txt* for reading.  
get = open("getty.txt","r")

# Open a new file *piggy.txt* for writing.  
piggyfile = open("piggy.txt","w")

# Read the getty.txt file into a string.  
getstr = get.read()

# Strip out bad characters (, - .).  
getstr = getstr.replace (',','')
getstr = getstr.replace ('-','')
getstr = getstr.replace ('.','')

# Split the string into a list of words.  
getlist = getstr.split()

# Create a new empty string.  
newstr = ""

# Loop through the list of words, pigifying each one.  
for word in getlist:
	newword = word [::-1]
	newstr = newstr + newword + " "
	

# Add the pigified word (and a space) to the new string.  
outfile = open("piggy.txt","w")

# Write the new string to piggy.txt.  
print (newstr, getlist, outfile)

# close the files.
outfile.close()
get.close()