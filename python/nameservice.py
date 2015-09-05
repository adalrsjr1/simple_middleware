'''
ID
NAME
HOST
PORT
'''
import MySQLdb
import uuid

class NameService:
    def __init__(self):
      self.conn = MySQLdb.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  passwd="root",
                                  db="mw_nameservice"
                                  )
      self.cursor = self.conn.cursor()
      self.reset()

    def lookupAll(self):
      self.cursor.execute("SELECT * FROM remoteobject")
      return self.cursor.fetchall()

    def lookupId(self, id):
      sql = "SELECT * FROM remoteobject WHERE obj_id = '%s'" % (id)
      self.cursor.execute(sql)
      return self.cursor.fetchall()

    def lookupName(self, name):
      sql = "SELECT * FROM remoteobject WHERE name = '%s'" % (name)
      self.cursor.execute(sql)
      return self.cursor.fetchall()

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
    
    #ns.register(uuid.uuid1(), "obj", "localhost", 5000)
    #print ns.lookupName("obj")
    #ns.reset()
    print uuid.uuid1().int

if __name__ == "__main__":
    main()  
