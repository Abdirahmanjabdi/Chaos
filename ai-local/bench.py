"""Benchmark a local Ollama model: prompt processing and generation speed.

Usage: python bench.py qwen3:8b [runs]
"""

import json
import statistics
import sys
import urllib.request

URL = "http://127.0.0.1:11434/api/generate"
SHORT_PROMPT = "Explain how an order book works in a stock exchange, in detail."
LONG_PROMPT = ("Summarise the following text in two sentences.\n\n"
               + "The matching engine receives orders, validates them, and places them in the book. " * 150)


def generate(model, prompt, num_predict):
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": 0, "num_predict": num_predict, "seed": 42},
    }).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.load(resp)


def rate(count, duration_ns):
    return count / (duration_ns / 1e9) if duration_ns else 0.0


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "qwen3:8b"
    runs = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    print(f"model: {model}")
    warm = generate(model, "Say hi.", 8)
    print(f"cold load: {warm['load_duration'] / 1e9:.1f}s (warm-up run, not counted)")

    gen_rates, ttfts = [], []
    for i in range(runs):
        r = generate(model, SHORT_PROMPT, 400)
        gen = rate(r["eval_count"], r["eval_duration"])
        ttft = (r.get("prompt_eval_duration", 0) + r.get("load_duration", 0)) / 1e6
        gen_rates.append(gen)
        ttfts.append(ttft)
        print(f"run {i + 1}: {r['eval_count']} tokens generated at {gen:.1f} tok/s, time to first token ~{ttft:.0f} ms")

    r = generate(model, LONG_PROMPT, 64)
    pp = rate(r["prompt_eval_count"], r["prompt_eval_duration"])
    print(f"long prompt: {r['prompt_eval_count']} tokens processed at {pp:.0f} tok/s")

    print("\nsummary")
    print(f"  generation:        median {statistics.median(gen_rates):.1f} tok/s "
          f"(min {min(gen_rates):.1f}, max {max(gen_rates):.1f})")
    print(f"  prompt processing: {pp:.0f} tok/s")
    print(f"  time to first token (short prompt): median {statistics.median(ttfts):.0f} ms")


if __name__ == "__main__":
    main()
