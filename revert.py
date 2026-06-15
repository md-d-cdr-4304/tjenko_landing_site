import json

transcript_path = "/Users/dhinakarr/.gemini/antigravity/brain/32412123-a834-4bc2-89bb-9fdfc5f5dbb1/.system_generated/logs/transcript_full.jsonl"
files_seen = {}

with open(transcript_path, "r") as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
            
        if entry.get("type") == "PLANNER_RESPONSE":
            tool_calls = entry.get("tool_calls", [])
            if not tool_calls: continue
            for tc in tool_calls:
                name = tc.get("name", "")
                if name.endswith("write_to_file"):
                    args = tc.get("args", {})
                    # Some tool calls have args inside tool_input or similar?
                    target = args.get("TargetFile")
                    content = args.get("CodeContent")
                    
                    if target and content:
                        # Clean up target string if it has literal quotes
                        if target.startswith('"') and target.endswith('"'):
                            target = target[1:-1]
                        
                        if target.endswith(".astro") or target.endswith(".css") or target.endswith(".ts"):
                            if target not in files_seen:
                                files_seen[target] = []
                            files_seen[target].append(content)

# For each file, the first version written in this conversation is the initial scaffold.
for target, versions in files_seen.items():
    if len(versions) >= 1:
        first_version = versions[0]
        if first_version.startswith('"') and first_version.endswith('"'):
            first_version = json.loads(first_version)
        print(f"Reverting {target}")
        with open(target, "w") as out:
            out.write(first_version)

