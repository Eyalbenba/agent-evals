import asyncio
from langgraph.pregel.remote import RemoteGraph
url = "https://tavily-people-research-agen-fa3702004ef5534d909f47857915a98b.default.us.langgraph.app"
graph_id = "agent"
#
# graph = RemoteGraph(graph_id, url=url, api_key="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")
#
query = "Eyal Ben Barouch"
include_citations = True
research_context = "General Topic"
#
# # Some input to the graph
# input = {"query": query,"include_citations": include_citations,
#         "research_context": research_context}
input = {"company": 'Tavily', "company_url": 'tavily.com'}

from langgraph_sdk import get_client, get_sync_client
from langgraph.pregel.remote import RemoteGraph
url = "https://tavily-company-research-age-aa2d819a3db35d95a53afb2d99b145ad.default.us.langgraph.app"
graph_id = "agent"
# input = {my_graph_input}
client = get_client(url=url)
sync_client = get_sync_client(url=url)
remote_graph = RemoteGraph(graph_id, client=client, sync_client=sync_client)
# Can also be a subgraph in an existing graph
name = remote_graph.get_name()
print(name)
response = remote_graph.invoke(input)
# print("Final state:", response)

# import ssl
# print(ssl.OPENSSL_VERSION)
#
# import httpx
# response = httpx.get("https://www.google.com")
# print(response.status_code)