import httpx
response = httpx.get(
    "https://tavily-people-research-agen-fa3702004ef5534d909f47857915a98b.default.us.langgraph.app",
    verify=False,
)
print(response)