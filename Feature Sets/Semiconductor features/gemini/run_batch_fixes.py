import subprocess
import os
import re

def run_fix():
    try:
        # Try different encodings
        content = ""
        for encoding in ['utf-8', 'utf-16', 'ascii']:
            try:
                with open('all_folders.txt', 'r', encoding=encoding) as f:
                    content = f.read()
                print(f"Successfully read with {encoding}")
                break
            except Exception:
                continue
        
        if not content:
            print("Failed to read all_folders.txt with any common encoding")
            return

        folders = [line.strip() for line in content.splitlines() if line.strip()]
        print(f"Read {len(folders)} lines from all_folders.txt")
        if folders:
            print(f"First line: '{folders[0]}'")
    
        # Skip the first line if it's just a count
        if folders and folders[0].isdigit():
            folders = folders[1:]
    
        target_folders = []
        for folder in folders:
            # Match fXX_ or fXXX_
            match = re.match(r'^f(\d+)_', folder)
            if match:
                num = int(match.group(1))
                if 1 <= num <= 80:
                    target_folders.append(folder)
            else:
                # print(f"Skipping {folder} - no match")
                pass
    
        # Sort folders numerically
        target_folders.sort(key=lambda x: int(re.match(r'^f(\d+)_', x).group(1)))
    
        print(f"Found {len(target_folders)} folders to process.")
        if target_folders:
            print(f"Example target: {target_folders[0]}")
    
        failures = []
        high_correlation = []
    
        for folder in target_folders:
            print(f"Processing {folder}...")
            try:
                # Ensure we run in the right directory
                result = subprocess.run(['python', 'fix_folder.py', folder], capture_output=True, text=True)
                output = result.stdout + result.stderr
                if result.returncode != 0:
                    print(f"Error processing {folder}")
                    failures.append((folder, output))
                else:
                    # Check for indicators of remaining high correlation
                    if "high correlation" in output.lower() or "still high" in output.lower() or "failed to fix correlation" in output.lower():
                        high_correlation.append((folder, output))
                    print(f"Finished {folder}")
            except Exception as e:
                print(f"Exception processing {folder}: {str(e)}")
                failures.append((folder, str(e)))

        print("\n--- Summary ---")
        print(f"Total processed: {len(target_folders)}")
        print(f"Failures: {len(failures)}")
        print(f"Still high correlation: {len(high_correlation)}")
    
        if failures:
            print("\nFailures:")
            for folder, error in failures:
                print(f"- {folder}")
            
        if high_correlation:
            print("\nStill high correlation:")
            for folder, out in high_correlation:
                print(f"- {folder}")

    except Exception as e:
        print(f"Global exception: {str(e)}")

if __name__ == "__main__":
    run_fix()
