def roomfinder(roomtype):
  if roomtype==1:
    b,c=1,21
  elif roomtype==2:
    b,c=21,41
  elif roomtype==3:
    b,c=41,61
  elif roomtype==4:
    b,c=61,81
  elif roomtype==5:
    b,c=81,101 
  for i in range(b,c):
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    query="select roomno from roominfo where roomno={} and status='{}'".format(i,'available')
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
      print("Your Room No. is {}".format(i))
      return i
    
def roomassigner (room_no,c_id,checkout):
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    query="update roominfo set c_id={} where roomno={} ".format(c_id,room_no)
    cursor.execute(query)
    con.commit()
    query="update roominfo set status='booked' where roomno={} and c_id={}".format(room_no,c_id)
    cursor.execute(query)
    con.commit()
    query="update roominfo set checkout='{}' where roomno={} and c_id={}".format(checkout,room_no,c_id)
    cursor.execute(query)
    con.commit()

    
