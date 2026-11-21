#!/usr/bin/env python3
import os
import shutil
import hashlib
import sys

def main():
    # Resolve entry.png relative to main.py's own directory with a CWD fallback
    script_dir = os.path.dirname(os.path.abspath(__file__))
    entry_filename = "entry.png"
    src_path = os.path.join(script_dir, entry_filename)
    if not os.path.exists(src_path):
        src_path = entry_filename # fallback to CWD
    
    if not os.path.exists(src_path):
        print(f"Error: {entry_filename} not found at {src_path}", file=sys.stderr)
        sys.exit(1)
        
    # Read output directory from MAKEFUN_OUTPUT_DIR environment variable (default /output)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Create the output directory if needed
    os.makedirs(output_dir, exist_ok=True)
    
    dest_path = os.path.join(output_dir, entry_filename)
    
    # Copy the image bytes exactly
    shutil.copyfile(src_path, dest_path)

    # Check that the output file exists and its size in bytes equals the source file's size
    if not os.path.exists(dest_path) or os.path.getsize(dest_path) != os.path.getsize(src_path):
        print(f"Error: Output file {dest_path} missing or size mismatch", file=sys.stderr)
        sys.exit(1)
    
    # Compute SHA-256 of the copied file
    sha256_hash = hashlib.sha256()
    with open(dest_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    file_hash = sha256_hash.hexdigest()
    
    file_size = os.path.getsize(dest_path)
    
    print(f"Copied {entry_filename} to {dest_path}")
    print(f"SHA-256: {file_hash}")
    print(f"Size: {file_size} bytes")

if __name__ == "__main__":
    main()
