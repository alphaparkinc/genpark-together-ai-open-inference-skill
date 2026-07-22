from client import TogetherAiOpenInferenceClient
client = TogetherAiOpenInferenceClient()

# Serverless Llama inference
r1 = client.infer("meta-llama/llama-3.3-70b", "Explain mixture-of-experts architecture in simple terms", "serverless")
print(f"Latency: {r1['latency_ms']}ms | Price: ${r1['price_per_1m']}/1M")
print(r1["output"])

# Batch DeepSeek (cost-efficient)
r2 = client.infer("deepseek-ai/deepseek-v4", "Summarize 100 customer support tickets", "batch")
print(f"Latency: {r2['latency_ms']}ms | Price: ${r2['price_per_1m']}/1M")
