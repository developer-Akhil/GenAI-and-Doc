from langchain_community.tools import DuckDuckGoSearchRun

'''
The DuckDuckGoSearchRun tool is a utility within the LangChain framework that integrates the privacy-focused DuckDuckGo search engine into AI applications. \
It allows language models (LLMs) to perform real-time web searches and access up-to-date information. 
'''
search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('Provide latest news from India Todays')

print(results)


'''
The ShellTool in LangChain is a built-in tool that enables a language model (LLM) agent to execute shell/powershell(window) (bash) commands on the local operating system
'''
from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke('dir')

print(results)

'''
LangChain provides a built-in YouTubeSearchTool within its langchain_community package, allowing agents to search for YouTube videos programmatically. This 
tool leverages the YouTube Data API to find relevant video information based on a query.
'''

from langchain_community.tools import YouTubeSearchTool
tool = YouTubeSearchTool()
print(tool.run("mylittlecornervideos"))
