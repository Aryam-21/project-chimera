"""
Spec Alignment Checker for Project Chimera

Purpose:
- Enforce spec-first development
- Prevent implementation drift
"""

from pathlib import Path
import sys

SPECS_DIR = Path('specs')
REQUIRED_SPECS = [
    'functional.md',
    'meta.md',
    'technical.md'
]
def main():
    missing = []
    for spec in REQUIRED_SPECS:
        if not (SPECS_DIR/spec).exists():
            missing.append(spec)
    if  missing:
        print("❌ Spec check failed. Missing specs:")
        for m in missing:
            print(f"- {m}")
            sys.exit(1)
    print("✅ Spec check passed. All required specs present.")
if __name__ == "__main__":
    main()