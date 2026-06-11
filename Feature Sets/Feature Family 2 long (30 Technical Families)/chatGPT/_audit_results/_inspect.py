import json
import glob
import sys
from pathlib import Path

HERE = Path(__file__).parent
target = sys.argv[1] if len(sys.argv) > 1 else "f01"

for f in sorted(HERE.glob(f"{target}*.json")):
    d = json.loads(f.read_text())
    print(f"\n=== {d['family']} ===")
    print(f"by_tier: {d.get('by_tier')}")
    print(f"\nvhash_dups ({len(d['vhash_dups'])}):")
    for g in d["vhash_dups"][:30]:
        print(" ", g["tiers"], g["members"])
    print(f"\nzcos_dups ({len(d['zcos_dups'])}):")
    for g in d["zcos_dups"][:20]:
        print(" ", g.get("tiers"), g["members"])
    print(f"\nsignflip_pairs ({len(d.get('signflip_pairs', []))}):")
    for g in d.get("signflip_pairs", [])[:20]:
        print(" ", g["members"])
    print(f"\nclass4 ({len(d.get('class4_base_deriv_pollution',[]))}):")
    for c in d.get("class4_base_deriv_pollution", [])[:35]:
        print(" ", c["name"])
