import subprocess
import os
import re
import ast

def run_audit():
    try:
        # Read folders from all_folders.txt
        content = ""
        for encoding in ['utf-16', 'utf-8', 'ascii']:
            try:
                with open('all_folders.txt', 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except Exception:
                continue
        
        if not content:
            print("Failed to read all_folders.txt")
            return

        folders = [line.strip() for line in content.splitlines() if line.strip()]
        if folders and folders[0].isdigit():
            folders = folders[1:]
    
        target_folders = []
        for folder in folders:
            match = re.match(r'^f(\d+)_', folder)
            if match:
                num = int(match.group(1))
                if 1 <= num <= 80:
                    target_folders.append(folder)
    
        target_folders.sort(key=lambda x: int(re.match(r'^f(\d+)_', x).group(1)))
    
        print(f"Auditing {len(target_folders)} folders...")
    
        high_correlation_reports = []
        failures = []
    
        for folder in target_folders:
            print(f"Auditing {folder}...")
            try:
                result = subprocess.run(['python', 'audit_folder.py', folder], capture_output=True, text=True)
                output = result.stdout
                
                # The output of audit_folder.py is "Auditing ...\n{...}"
                # We need to parse each line or each dict
                lines = output.splitlines()
                for line in lines:
                    if line.startswith('{') and 'high_corr' in line:
                        try:
                            # Use ast.literal_eval for safety if it's a valid python dict representation
                            # but audit_folder.py uses print(result) where result is a dict
                            audit_res = ast.literal_eval(line)
                            if audit_res.get('high_corr'):
                                high_correlation_reports.append((folder, audit_res['high_corr']))
                        except Exception as e:
                            # Maybe it's not a complete dict or has some un-evaluable parts
                            if "'high_corr': [(" in line:
                                high_correlation_reports.append((folder, line))
                
                if result.returncode != 0:
                    failures.append((folder, result.stderr))
                    
            except Exception as e:
                failures.append((folder, str(e)))

        print("\n--- Audit Summary ---")
        print(f"Total folders audited: {len(target_folders)}")
        print(f"Folders with high correlation: {len(high_correlation_reports)}")
        print(f"Failures: {len(failures)}")
        
        if high_correlation_reports:
            print("\nHigh Correlation Details:")
            for folder, detail in high_correlation_reports:
                print(f"- {folder}: {detail}")
        
        if failures:
            print("\nFailures:")
            for folder, err in failures:
                print(f"- {folder}: {err}")

    except Exception as e:
        print(f"Global audit exception: {str(e)}")

if __name__ == "__main__":
    run_audit()
