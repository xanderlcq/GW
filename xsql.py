__author__ = 'x'
import pymysql
import pymysql.cursors


class Xsql(object):
    def __init__(self):
        self.connection = None
        self.connection_status = False

    def start_connection(self, host,database,user, password=None):
        try:
            self.connection = pymysql.connect(host=host,
                                 user=user, passwd=password,
                                 db=database)
            self.connection_status = True
            return 'Connection Succeed'
        except pymysql.MySQLError:
            return 'Connection Failed! Check your database name'

    def close_connection(self):
        assert self.connection_status, 'The connection is not set up yet!'
        self.connection.close()
        self.connection_status = False
        return 'Mysql database connection closed.'

    def write_data(self,table_name,keys,values):
        assert type(table_name) is str, 'Table name must be a string'
        assert type(keys) is list, 'keys must be a list of keys'
        assert type(values) is list, 'values must be a list of values'
        assert (len(keys) > 0) & (len(values) > 0), 'keys and values can not be emtpy lists'
        assert len(keys) == len(values), 'keys and values must match up'
    # INSERT INTO `plant1`(`moisture`, `light`, `addWater`, `temperature`, `note`) VALUES (123,321,123,321,'abc')
        sql_first = "INSERT INTO `"+table_name+"`("
        sql_second = ") VALUES ("
        sql_third = ")"
        for x in range(len(keys)):
            keys_append = "`"+keys[x]+"`, "
            values_append = ""+values[x]+","
            sql_first += keys_append
            sql_second += values_append
        sql_first = sql_first[0:len(sql_first)-2]
        sql_second = sql_second[0:len(sql_second)-1]
        sql = sql_first+sql_second+sql_third
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            print 'Data writing succeed'
        except pymysql.ProgrammingError:
            print 'Data writing failed, Check Table Name'
        except pymysql.InternalError:
            print 'Data writing failed, check column key word'

    def is_valid_key(self,key):
        assert self.connection_status, 'You must connect to a database first!'
        with self.connection.cursor() as cursor:
            sql = "SHOW COLUMNS FROM `plant1` LIKE '"+key+"'"
            return cursor.execute(sql) == 1
