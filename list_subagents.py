import json

transcript_path = "/Users/dhinakarr/.gemini/antigravity/brain/32412123-a834-4bc2-89bb-9fdfc5f5dbb1/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r") as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
            
        if entry.get("type") == "PLANNER_RESPONSE":
            for tc in entry.get("tool_calls", []):
                if tc.get("name", "").endswith("invoke_subagent"):
                    args = tc.get("args", {})
                    print(json.dumps(args, indent=2))
