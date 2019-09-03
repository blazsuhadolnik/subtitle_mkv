#i have 22 episode in one telenovel so i repet code from 1 to 23 without number 23
for j in range(1, 23):
	#for every line in file (like 1.srt) save just lines with word Dialogue in array lines
	lines = [line.rstrip('\n') for line in open(str(j)+'.srt') if line.find('Dialogue:') != -1]
	#for array pod we just cut some start caracter in each line 
	pod = []
	for i in lines:
		pod.append(i[12:])
	#array times is changing in shape with text and time seqence.
	times = []
	for i in pod:
		times.append(i.split(",", 8))
	f=open('episode'+str(j)+'.srt', 'a')
	for i in range(1,len(times)+1):
		#writing in file
		f.write(str(i))
		f.write('\n')
		#writing time
		f.write(times[i-1][0] + "0 --> " + times[i-1][1])
		#removing some sequence in text before writing in file.
		times[i-1][-1] = times[i-1][-1].replace('{\i1}', ' ')
		times[i-1][-1] = times[i-1][-1].replace('{\i0}', ' ')
		times[i-1][-1] = times[i-1][-1].replace('\\N', '\n')
		#writting text in file
		f.write('\n')
		f.write(times[i-1][-1])
		f.write('\n\n')
	#close file
	f.close()
