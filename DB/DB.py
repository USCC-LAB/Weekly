class DB:
	def __init__(self,db):
		# Declaration
        self.__db = None

        # Initialization
        self.__db = db


	def CreateTable(self):
		self.__db.createTable()

	def insertStudent(self,dbname,table,sid,name,cardId):
		self.__db.insertStudent(dbname,table,sid,name,cardId)

	def checkIn(self,cardId): 
		self.__db.checkIn(cardId)
	
	def checkOut(self,cardId): 
		self.__db.checkOut(cardId)

