for j in range(1, 23):	
	lines = [line.rstrip('\n') for line in open(str(j)+'.srt') if line.find('Dialogue:') != -1]
	pod = []
	for i in lines:
		pod.append(i[12:])
	casi = []
	for i in pod:
		casi.append(i.split(",", 8))
	f=open('e'+str(j)+'.srt', 'a')
	for i in range(1,len(casi)+1):
		f.write(str(i))
		f.write('\n')
		f.write(casi[i-1][0] + "0 --> " + casi[i-1][1])
		casi[i-1][-1] = casi[i-1][-1].replace('{\i1}', ' ')
		casi[i-1][-1] = casi[i-1][-1].replace('{\i0}', ' ')
		casi[i-1][-1] = casi[i-1][-1].replace('\\N', '\n')
		f.write('\n')
		f.write(casi[i-1][-1])
		f.write('\n\n')
	f.close()


#for i in casi:
#	print(i)