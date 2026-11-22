import os
import shutil
import hashlib

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_dir, "entry.png")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        dest_path = os.path.join(output_dir, "entry.png")
    else:
        out_folder = os.path.join(base_dir, "out")
        os.makedirs(out_folder, exist_ok=True)
        dest_path = os.path.join(out_folder, "entry.png")
        
    shutil.copyfile(src_path, dest_path)
    
    src_size = os.path.getsize(src_path)
    dest_size = os.path.getsize(dest_path)
    if src_size != dest_size:
        print(f"Error: Size mismatch! Source: {src_size}, Destination: {dest_size}")
        exit(1)
    
    with open(dest_path, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
        
    print(f"Destination: {dest_path}")
    print(f"SHA-256: {sha256}")
    print(f"Source size: {src_size}, Destination size: {dest_size}")

if __name__ == "__main__":
    main()
