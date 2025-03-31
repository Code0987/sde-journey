import asyncio
import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/items/", json={"name": "test", "price": 100}
        )
        response.raise_for_status()
        print(response.json())

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8000/items/2",
            headers={"x-custom-key": "1234"},
            timeout=10,
        )
        response.raise_for_status()
        print(response.json())


asyncio.run(main())
