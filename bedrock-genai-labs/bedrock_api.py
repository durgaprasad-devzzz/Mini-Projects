import json
import boto3

bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")

prompt = "Write a short 2-line welcome message for an AI workshop."

body = json.dumps({
    "messages": [
        {
            "role": "user",
            "content": [{"text": prompt}]
        }
    ],
    "inferenceConfig": {"maxTokens": 200}
})

response = bedrock.invoke_model(
    body=body,
    modelId="us.amazon.nova-2-lite-v1:0",
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
print(response_body["output"]["message"]["content"][0]["text"])