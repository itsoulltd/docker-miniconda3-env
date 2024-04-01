import pandas as pd
import mysql.connector
from mysql.connector import Error

class MySQLConnect:
    
    '''MySQLConnect Holds a instance var connection to exeecute multiple query.'''

    def __init__(self, host='localhost', port=3306, database='testDB', user='root', password='root@123'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        try:
            self.connection = mysql.connector.connect(host=self.host
                                                  , port=self.port
                                                  , database=self.database
                                                  , user=self.user
                                                  , password=self.password)
            if self.connection.is_connected():
                self.db_Info = self.connection.get_server_info()
                print("MySQL/MariaDB Server version ", self.db_Info)
        except Error as e:
            print(f"Error while connecting to MySQL/MariaDB: {e}")
    #end

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection is closed")
        else:
            print("DB not connected!")
    #end

    def whichDB(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.close()
        else:
            print("DB not connected!")
    #end

    def query(self, query):
        if self.connection.is_connected():
            df_mysql = pd.read_sql(query, self.connection)
            return df_mysql
        else:
            print("DB not connected!")
        return 0
    #end

#end-of-class

if __name__ == '__main__':
    #Read as Panda Df: 
    #Connect using host.docker.internal or using extra_hosts entry in docker-compose as host-machine:<machine-ip>
    connect = MySQLConnect(host='host.docker.internal', database='testDB')
    connect.whichDB()

    #pd_df = connect.query("Select * from users")
    #pd_df.info()
    #pd_df.head(5)

    connect.close()
#end