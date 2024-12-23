import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from rich import print, traceback

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')  

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set in the .env file.")


client = AsyncIOMotorClient(MONGODB_URI)

async def list_databases():
    """List all databases in the MongoDB cluster."""
    try:
        databases = await client.list_database_names()  
        print("Databases in cluster:")
        for db_name in databases:
            print(db_name)
    except Exception as e:
        print(f"An error occurred while listing databases: {e}")
    finally:
        client.close()  


if __name__ == "__main__":
    asyncio.run(list_databases())
