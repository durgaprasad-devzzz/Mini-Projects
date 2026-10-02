
# Amazon Bedrock GenAI Labs

Hands-on Python scripts built while completing the **"Building with Amazon Bedrock"** workshop on AWS Builder Center. The workshop provides the lab structure; I completed the scripts myself and adapted them where needed (for example, migrating from a retired model to Amazon Nova and updating the request and response format).

## What is covered

| Lab | Topic | What it demonstrates |
|---|---|---|
| F-2 | InvokeModel API | Model-specific request and response formats (Amazon Nova) |
| F-3 | Converse API | One unified format, multi-turn messages, image input, system prompts, token usage |
| F-4 | Inference parameters | `maxTokens`, `stopSequences` and temperature across different models |
| F-5 | Tool use | The model requests a function call, my code runs it and returns the result |
| F-6 | Streaming API | Real-time responses with `converse_stream` |
| F-7 | Embeddings | Semantic similarity using cosine similarity (foundation for RAG) |
| F-8 | Streamlit | A simple web UI in a few lines of Python |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install boto3 streamlit
```

Requires AWS credentials with access to Amazon Bedrock models in your region. Never commit credentials to this repository.

## Run

```bash
python3 bedrock_api.py
python3 converse_api.py
streamlit run simple_streamlit_app.py
```

## Tech stack

Python, boto3, Amazon Bedrock, Amazon Nova, Streamlit

## Key lessons

- A model ID and its request format go together. Switching model families with `InvokeModel` means changing the body and response parsing too.
- The Converse API removes most of that rework, because the same request shape works across text models.
- With tool use, the model only asks for a function to be called. The application code actually runs it.
- Lab content can go stale. A retired model ID (`end of its life` error) was fixed by switching to a currently available model.

## Next

Strands Agents and Amazon Bedrock AgentCore labs, followed by a larger project (resume analyzer or study assistant chatbot).

## Credits

Based on the AWS workshop "Building with Amazon Bedrock" (AWS Builder Center). All rights to the original workshop material belong to Amazon Web Services.
