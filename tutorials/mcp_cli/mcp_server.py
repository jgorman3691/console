from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base 
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(
    name="Read document contents",
    description="Read the contents of the document and return the result as a string."
)
def read_document(
    doc_id: str = Field(description="ID of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID {doc_id} not found.")
    return docs[doc_id]

# TODO: Write a tool to edit a doc
@mcp.tool(
    name="Edit Document",
    description="Edit a document by replacing the current string with a new string."
)
#def edit_document(
#    doc_id: str = Field(description="ID of the document to be edited")
#):
#    if doc_id not in docs:
#        raise ValueError(f"Document with ID {doc_id} not found.")
#    docs[doc_id] = input(f"Please input the edits to replace the contents of {doc_id}:")
#    return docs[doc_id]
def edit_document(
    doc_id: str = Field(description="The ID of the document to be edited"),
    old_str: str = Field("The text to be replaced.  Must match exactly, including whitespace"),
    new_str: str = Field(description="The new text to insert in place of the old text")
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID {doc_id} not found.")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)


# TODO: Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with ID {doc_id} not found")
    return docs[doc_id]

# TODO: Write a prompt to rewrite a doc in markdown format
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="ID of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The ID of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary.  Please feel free to add in extra formatting.
Use the 'edit_document' tool to edit the document.  After the document has been reformatted...
"""
    
    return [
        base.UserMessage(prompt)
    ]

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
