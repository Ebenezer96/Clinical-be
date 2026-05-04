from httpx import AsyncClient


async def test_root(client: AsyncClient) -> None:
	response = await client.get("/")
	assert response.status_code == 200
	assert "running" in response.json()["message"]


async def test_health(client: AsyncClient) -> None:
	response = await client.get("/health")
	assert response.status_code == 200
	assert response.json() == {"status": "ok"}
