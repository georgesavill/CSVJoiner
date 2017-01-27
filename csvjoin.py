import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

filewriter = csv.writer(open(output_file,'wb'))
file_counter = 0

for input_file in glob.glob(os.path.join(input_path,'*.csv')):
	with open(input_file,'rU') as csv_file:
		filereader = csv.reader(csv_file)
		name, ext = os.path.splitext(input_file)
		namelong = "{:<25}".format(name)
		nameshort = name[:-1]
		temperature = namelong[+13:-9]
		nitrogen = namelong[+16:-7]
		timepoint = namelong[+18:-5]
		experimentalrep = namelong[+20:-3]
		imagerep = nameshort[+22:]
		analysisrep = name[-1]
		if file_counter < 1:
			for i, row in enumerate(filereader):
				if i==0: 
					row.append('Temperature'), 
					row.append('Nitrogen'),
					row.append('Timepoint'),
					row.append('ExperimentalRep'),
					row.append('ImageRep'),
					row.append('AnalysisRep')
				else: 
					row.append(temperature),
					row.append(nitrogen),
					row.append(timepoint),
					row.append(experimentalrep),
					row.append(imagerep),
					row.append(analysisrep)
				filewriter.writerow(row)
		else:
			header = next(filereader,None)
			for row in filereader:
				row.append(temperature),
				row.append(nitrogen),
				row.append(timepoint),
				row.append(experimentalrep),
				row.append(imagerep),
				row.append(analysisrep)
				filewriter.writerow(row)
	file_counter += 1