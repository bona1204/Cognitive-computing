import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="Alonso1204",db="new_schema" )

    def read(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuarios order by nombre asc")
            else:
                cursor.execute("SELECT * FROM usuarios where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuarios(nombre,telefono,email) VALUES(%s, %s, %s)", (data['nombre'],data['telefono'],data['email'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuarios set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM usuarios where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
