import json
import glob
import os

# Find all transcript_full.jsonl files
transcripts = glob.glob("/Users/dhinakarr/.gemini/antigravity/brain/*/.system_generated/logs/transcript_full.jsonl")

# To get the FIRST version chronologically, we should probably sort the tool calls by time or just collect all versions and we know the first one in the first transcript
# Actually, the earliest "created_at" in the log entry
file_versions = {}

for t_path in transcripts:
    with open(t_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except:
                continue
                
            if entry.get("type") == "PLANNER_RESPONSE":
                created_at = entry.get("created_at", "")
                for tc in entry.get("tool_calls", []):
                    if tc.get("name", "").endswith("write_to_file"):
                        args = tc.get("args", {})
                        target = args.get("TargetFile")
                        content = args.get("CodeContent")
                        
                        if target and content:
                            if target.startswith('"') and target.endswith('"'):
                                target = target[1:-1]
                            
                            if target.endswith(".astro") or target.endswith(".css") or target.endswith(".ts"):
                                if target not in file_versions:
                                    file_versions[target] = []
                                file_versions[target].append((created_at, content))

for target, versions in file_versions.items():
    # Sort by created_at to get the earliest version
    versions.sort(key=lambda x: x[0])
    first_version = versions[0][1]
    
    if first_version.startswith('"') and first_version.endswith('"'):
        first_version = json.loads(first_version)
        
    print(f"Reverting {target}")
    with open(target, "w") as out:
        out.write(first_version)

