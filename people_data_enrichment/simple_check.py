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
input = {"query": query,"include_citations": include_citations,
        "research_context": research_context}

from langgraph_sdk import get_client, get_sync_client
from langgraph.pregel.remote import RemoteGraph

graph_name = "agent"
client = get_client(url=url)
sync_client = get_sync_client(url=url)
remote_graph = RemoteGraph(graph_name, client=client, sync_client=sync_client)
# Can also be a subgraph in an existing graph
response = remote_graph.invoke(input)
print("Final state:", response)