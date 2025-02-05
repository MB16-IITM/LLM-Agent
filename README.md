# LLM-Agent
# DataWorks Automation Agent

## Overview
Intelligent automation agent for processing data tasks using LLM-powered task parsing.

## Features
- Flexible task execution
- Secure file handling
- LLM-powered task interpretation

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set AIPROXY_TOKEN: `export AIPROXY_TOKEN=your_token`
3. Run API: `uvicorn src.main:app`

## Docker
Build: `docker build -t dataworks-agent .`
Run: `docker run -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN dataworks-agent`

## License
MIT License
