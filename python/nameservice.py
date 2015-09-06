# the name service must has a table in a database as follow
# OBJ_ID VARCHAR(45)
# NAME VARCHAR(45)
# HOST VARCAHR(15)
# PORT INT

import MySQLdb
import uuid

class IRef:
  def __init__(self, data):
    self.id = data[0]
    self.name = data[1]
    self.host = data[2]
    self.port = data[3]

class NameService:
    def __init__(self):
      self.conn = MySQLdb.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  passwd="root",
                                  db="mw_nameservice"
                                  )
      self.cursor = self.conn.cursor()
      #self.reset()

    def __createIRef(self, data):
      result = []
      for x in data:
        result.append(IRef(x))
      return result

    def lookupAll(self):
      self.cursor.execute("SELECT * FROM remoteobject")
      data = self.cursor.fetchall()

      result = self.__createIRef(data)
      return result
      

    def lookupId(self, id):
      sql = "SELECT * FROM remoteobject WHERE obj_id = '%s'" % (id)
      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      result = self.__createIRef(data)
      return result

    def lookupName(self, name):
      sql = "SELECT * FROM remoteobject WHERE name = '%s'" % (name)
      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      result = self.__createIRef(data)
      return result

    def register(self, obj_id, name, host, port):
      sql = "INSERT INTO remoteobject(OBJ_ID, NAME, HOST, PORT) \
      VALUES ('%s', '%s', '%s', '%s')" % \
      (obj_id.hex, name, host, port)

      try:
        self.cursor.execute(sql)
        self.conn.commit()
      except:
        self.conn.rollback()

    def reset(self):
      self.cursor.execute("truncate remoteobject")      

    def __del__(self):
      self.conn.close()

def main():
    ns = NameService()
    
    ns.register(uuid.uuid1(), "obj", "localhost", 5000)
    iRef = ns.lookupName("obj")[0]
    print iRef.name
    #ns.reset()
    

if __name__ == "__main__":
    main()  
