from pymongo import MongoClient

client = MongoClient("localhost", port=27017)

products_db = client["products-db"]

products = products_db["products"]

products.delete_many({})

products.insert_many([
    {
        "name": "Moloko",
        "price": 93,
    },
    {
        "name": "Kefir",
        "price": 50,
    },
])

data = products.find({
    "price": {
        "$gt": 40
    }
})
for document in data:
    print(f"{document=}, {type(document)}")

#######


import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import Document, Indexed, init_beanie


class Product(Document):
    name: str
    price: Indexed(float)

    class Settings:
        name = "products"


async def example():
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    await init_beanie(database=client["products-db"], document_models=[Product])

    protein_bar = Product(name="Bamboo", price=5.95)
    await protein_bar.insert()

    data = await Product.find_one({"price": {"$gt": 5.55}})
    print(f"{data=}")


if __name__ == "__main__":
    asyncio.run(example())
