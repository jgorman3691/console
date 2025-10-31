# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive tutorial repository for learning Claude AI integration and advanced AI development patterns. The codebase is organized into several educational modules covering different aspects of AI development:

- **api/**: Basic Anthropic API tutorials using Jupyter notebooks
- **claude_features/**: Advanced Claude features like thinking, citations, caching, code execution
- **mcp_cli/**: Model Control Protocol (MCP) chat application with Python CLI
- **prompt_engineering/**: Prompt engineering tutorials and data processing
- **prompts/**: Evaluation frameworks and model grading systems
- **rag/**: Retrieval-Augmented Generation implementations (chunking, embeddings, vector databases)
- **tool_use/**: Tool integration patterns and structured data handling

## Development Environment

### MCP CLI Application (mcp_cli/)

This is a Python-based chat application that demonstrates MCP (Model Control Protocol) integration.

**Setup Commands:**
```bash
cd mcp_cli
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

**Run Application:**
```bash
uv run main.py
```

**Alternative setup without uv:**
```bash
cd mcp_cli
python -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
python main.py
```

**Environment Configuration:**
- Requires `.env` file with `ANTHROPIC_API_KEY`
- Python 3.10+ required

### Jupyter Notebooks

Most tutorials are implemented as Jupyter notebooks (.ipynb files) across different directories. Each directory contains both exercise and completed versions of notebooks.

**Key notebook categories:**
- API exercises: Basic chat, structured data, temperature control
- Feature demonstrations: Thinking, caching, PDF processing, image analysis
- RAG implementations: Vector databases, BM25, hybrid search, reranking
- Tool integration: Custom tools, streaming, multi-turn conversations

## Architecture Patterns

### MCP Integration Pattern

The MCP CLI demonstrates a clean separation between:
- **Core services** (`core/`): Claude API integration, chat management, tool orchestration
- **MCP components**: Server (`mcp_server.py`) with document management tools, Client (`mcp_client.py`) for MCP communication
- **Tools system**: Dynamic tool discovery and execution via `ToolManager`

Key architectural components:
- `Chat` class handles conversation flow and tool execution loops
- `Claude` service manages API interactions and message formatting
- `ToolManager` provides centralized tool discovery across MCP clients
- FastMCP server implements document CRUD operations with validation

### Document Management System

The MCP server includes a simple document store with read/edit capabilities:
- Documents stored in-memory dictionary with string IDs
- Read tool for content retrieval
- Edit tool with find/replace functionality
- Extensible pattern for adding new document operations

## Testing and Quality

**Note**: No formal linting, testing, or type checking is configured in this repository. The README explicitly states "There are no lint or type checks implemented."

## Usage Patterns

### Interactive Chat Features
- **Document retrieval**: Use `@doc_id` to include document content
- **Commands**: Use `/command_name` for MCP server commands with tab completion
- **Tool integration**: Automatic tool discovery and execution through MCP protocol

### Development Workflow
1. Modify `mcp_server.py` to add new documents or tools
2. Implement missing functionality in `mcp_client.py` (see TODOs)
3. Use notebook exercises to experiment with different AI integration patterns
4. Reference completed notebooks for implementation examples