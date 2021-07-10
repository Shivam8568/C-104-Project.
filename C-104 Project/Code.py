import csv 
import statistics as st 
with open ("Data.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range (len(filedata)):
    n_num = filedata[i][1]
    newdata.append(float(n_num))
mean = st.mean(newdata)
print ("The Mean of the data is ", mean)
median = st.median(newdata)
print ("The Median of the data is ", median)
mode = st.mode(newdata)
print ("The Mode of the data is ", mode)