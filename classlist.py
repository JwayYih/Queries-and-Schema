import sys
from basicdb import *

#Load database and system arguments
course=sys.argv[1]
load_db('registrar.json')

#Combine registrar and courses by roomid
combined_roomid=join(db_from('courses'), db_from('rooms'), 'roomid')

#Pull out course info and print
course_info=where(combined_roomid, 'courseid', course)
name=select(course_info,'coursename')
times=select(course_info,'times')
roomname=select(course_info,'roomname')
print (str(name[0]) + ' meets ' + str(times[0]) + ' in ' + str(roomname[0]))

#Combine students and enrollment by studentid
combined_studentid=orderby(join(db_from('students'), db_from('enrollments'), 'studentid'),'firstname')

#Select students in the course, print their names
studentlist=where(combined_studentid, 'courseid',course)
count = 0
while count < len(studentlist):
    firstname=select(studentlist,'firstname')
    lastname=select(studentlist,'lastname')
    print (firstname[count] + ' '+ lastname[count])
    count += 1

#Print current enrollment
distinct_count=len(studentlist)
print ('Current enrollment: ' + str(distinct_count))

#Print remaining capacity
capacity=select(course_info,'capacity')
rem_cap=round(float(capacity[0]))-distinct_count
print ('Remaining capacity: ' + str(rem_cap))
