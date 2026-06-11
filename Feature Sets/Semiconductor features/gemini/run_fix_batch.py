import os
import re
import subprocess

def run_fix():
    # UTF-16 LE with BOM is common on Windows
    try:
        with open('all_folders.txt', 'r', encoding='utf-16') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading with utf-16: {e}")
        with open('all_folders.txt', 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

    target_folders = []
    for line in lines:
        line = line.strip()
        if not line: continue
        match = re.match(r'^f(\d+)_', line)
        if match:
            num = int(match.group(1))
            if 81 <= num <= 160:
                target_folders.append(line)

    target_folders.sort(key=lambda x: int(re.match(r'^f(\d+)_', x).group(1)))
    print(f"Found {len(target_folders)} folders to process.")

    results = []
    for folder in target_folders:
        print(f"Processing {folder}...")
        try:
            # Using list for subprocess.run is safer
            process = subprocess.run(['python', 'fix_folder.py', folder], capture_output=True, text=True)
            output = process.stdout + process.stderr
            if process.returncode != 0:
                results.append(f"FAILURE: {folder} (Exit code {process.returncode})")
                print(f"Failed: {folder}")
            elif "high correlation" in output.lower() or "still has high correlation" in output.lower():
                results.append(f"HIGH CORRELATION: {folder}")
                print(f"High correlation remains in {folder}")
            else:
                results.append(f"SUCCESS: {folder}")
        except Exception as e:
            results.append(f"ERROR: {folder} - {str(e)}")
            print(f"Error processing {folder}: {e}")

    with open('fix_results_81_160.txt', 'w') as f:
        f.write('\n'.join(results))

    print("\nSummary of failures or high correlation:")
    failures = [r for r in results if "SUCCESS" not in r]
    if failures:
        for r in failures:
            print(r)
    else:
        print("None. All folders processed successfully.")

if __name__ == "__main__":
    run_fix()
