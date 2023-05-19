from peewee import *


database = MySQLDatabase(
    'market-pos',
    user='root',password='',
    host='localhost',port=3306
)

class recordatorio(Model):
    descrip=CharField(max_length=50)
    fecha=CharField(max_length=50)
    producto=CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.descrip
    
    class Meta:
        database=database
        table_name='recordatorio'
    