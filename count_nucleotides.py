seq1="CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA"

countA=0
countT=0
countC=0
countG=0

for nextCharacter in seq1:
	#print (nextCharacter)
	if nextCharacter == "A":
		countA=countA+1
	elif nextCharacter == "T":
		countT=countT+1
	elif nextCharacter == "C":
		countC=countC+1
	elif nextCharacter == "G":
		countG=countG+1
		
print ('sequence:', 'CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA') #> ncounts.txt
print ('A\'s', countA) #>> ncounts.txt
print ('C\'s', countC) #>> ncounts.txt
print ('T\'s', countT) #>> ncounts.txt
print ('G\'s', countG) #>> ncounts.txt
print ('GC content:', (countG+countC)/len(seq1)) #>> ncounts.txt need float command

seq2="CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT"

nucA=0
nucT=0
nucC=0
nucG=0

for nextCharacter in seq1:
	#print (nextCharacter)
	if nextCharacter == "A":
		nucA=nucA+1
	elif nextCharacter == "T":
		nucT=nucT+1
	elif nextCharacter == "C":
		nucC=nucC+1
	elif nextCharacter == "G":
		nucG=nucG+1
		
print ('sequence:', 'CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA') #>>ncounts.txt
print ('A\'s', nucA) #>> ncounts.txt
print ('C\'s', nucC) #>> ncounts.txt
print ('T\'s', nucT) #>> ncounts.txt
print ('G\'s', nucG) #>> ncounts.txt
print ('GC content:', (nucG+nucC)/len(seq2)) #>>ncounts.txt, need float command