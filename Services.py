from motor.motor_asyncio import AsyncIOMotorClient

Client = AsyncIOMotorClient('mongodb://localhost:27017')
Database = Client['GeneralData']
Users = Database['Users']
Posts = Database['Posts']
Tokens = Database['Tokens']
