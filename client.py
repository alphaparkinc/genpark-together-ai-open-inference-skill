import time, hashlib

class TogetherAiOpenInferenceClient:
    CATALOG = {
        "meta-llama/llama-3.3-70b":      {"price": 0.88, "base_ms": 120, "type": "text"},
        "deepseek-ai/deepseek-v4":        {"price": 1.40, "base_ms": 180, "type": "text"},
        "qwen/qwen3-235b-a22b":           {"price": 2.20, "base_ms": 340, "type": "text"},
        "mistralai/mistral-small-4":      {"price": 0.20, "base_ms": 80,  "type": "text"},
        "black-forest-labs/flux-1.1-pro": {"price": 0.04, "base_ms": 600, "type": "image"},
        "stabilityai/stable-audio-2":     {"price": 0.06, "base_ms": 400, "type": "audio"},
    }

    def infer(self, model_name: str, prompt: str, mode: str = "serverless") -> dict:
        cfg = self.CATALOG.get(model_name, {"price": 0.90, "base_ms": 150, "type": "text"})
        tokens = len(prompt.split()) * 4 // 3
        multiplier = 0.75 if mode == "dedicated" else 1.5 if mode == "batch" else 1.0
        latency = int(cfg["base_ms"] * (0.8 + tokens / 1000) * multiplier)
        rid = hashlib.md5(f"{model_name}{time.time()}".encode()).hexdigest()[:8]
        output = (
            f"[Together AI | {model_name} | {mode.upper()}] "
            f"Output generated. ID:{rid}. Tokens:{tokens}. "
            f"Type:{cfg['type']}. ATLAS speculative decoding applied."
        )
        return {"output": output, "latency_ms": latency, "price_per_1m": cfg["price"]}
