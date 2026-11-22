#!/usr/bin/env python3
import os
import shutil
import hashlib
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output"
        
    try:
        os.makedirs(out_dir, exist_ok=True)
        dest_path = os.path.join(out_dir, "entry.png")
        shutil.copyfile(src_path, dest_path)
    except Exception:
        out_dir = os.path.join(script_dir, "out")
        os.makedirs(out_dir, exist_ok=True)
        dest_path = os.path.join(out_dir, "entry.png")
        shutil.copyfile(src_path, dest_path)
        
    src_size = os.path.getsize(src_path)
    dest_size = os.path.getsize(dest_path)
    if src_size != dest_size:
        print(f"Error: Size mismatch! Source {src_size} != Dest {dest_size}", file=sys.stderr)
        sys.exit(1)
        
    def compute_sha256(filepath):
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                h.update(byte_block)
        return h.hexdigest()

    src_hash = compute_sha256(src_path)
    dest_hash = compute_sha256(dest_path)
    if src_hash != dest_hash:
        print(f"Error: SHA-256 mismatch! Source {src_hash} != Dest {dest_hash}", file=sys.stderr)
        sys.exit(1)
        
    file_hash = dest_hash
    
    print(f"Output Path: {dest_path}")
    print(f"SHA-256: {file_hash}")

if __name__ == "__main__":
    main()
