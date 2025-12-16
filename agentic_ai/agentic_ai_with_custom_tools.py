from langchain_core.tools import tool

# Step 1 -- create a function
def multiply(a,b):
  """Adding two numbers"""
  return a+b

# Step 2 -- adding data type hints
def multiply(a: int,b: int) -> int:
  """Multiply two numbers"""
  return a+b

# Step 3 -- adding tool decorator
@tool
def multiply(a: int,b: int) -> int:
  """This tool takes 2 integers and add them"""
  return a+b


def multiply1(a,b):
  """Adding two numbers"""
  return a*b



