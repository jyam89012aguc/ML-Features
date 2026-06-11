import os
import subprocess
import sys
import re

def main():
    root_dir = os.getcwd()
    dirs = [d for d in os.listdir(root_dir) if os.path.isdir(d) and d[0].isdigit()]
    dirs.sort()

    results = []

    for d in dirs:
        print(f"Auditing {d}...")
        try:
            process = subprocess.Popen(
                [sys.executable, "audit_harness.py", d],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                results.append({
                    "Family": d,
                    "Total": 0,
                    "Errors": 1,
                    "NaNs": 0,
                    "Constants": 0,
                    "Duplicates": 0,
                    "Status": "Failed to run"
                })
                continue

            # Parse stdout
            total = 0
            errors = 0
            nans = 0
            constants = 0
            dups = 0

            total_match = re.search(r"Total functions: (\d+)", stdout)
            if total_match:
                total = int(total_match.group(1))

            error_match = re.search(r"Errors \((\d+)\):", stdout)
            if error_match:
                errors = int(error_match.group(1))

            nan_match = re.search(r"All-NaN functions \((\d+)\):", stdout)
            if nan_match:
                nans = int(nan_match.group(1))

            const_match = re.search(r"Constant functions \((\d+)\):", stdout)
            if const_match:
                constants = int(const_match.group(1))

            dup_match = re.search(r"Duplicates \((\d+)\):", stdout)
            if dup_match:
                # The output says "Duplicates (N):", but then lists pairs/groups.
                # Let's count the number of duplicates reported.
                dups = int(dup_match.group(1))

            results.append({
                "Family": d,
                "Total": total,
                "Errors": errors,
                "NaNs": nans,
                "Constants": constants,
                "Duplicates": dups,
                "Status": "Success"
            })

        except Exception as e:
            results.append({
                "Family": d,
                "Total": 0,
                "Errors": 1,
                "NaNs": 0,
                "Constants": 0,
                "Duplicates": 0,
                "Status": f"Exception: {str(e)}"
            })

    # Print Summary Table
    print("\n" + "="*80)
    print(f"{'Family':<40} | {'Total':<6} | {'Err':<4} | {'NaN':<4} | {'Const':<6} | {'Dup':<4}")
    print("-" * 80)
    for res in results:
        print(f"{res['Family']:<40} | {res['Total']:<6} | {res['Errors']:<4} | {res['NaNs']:<4} | {res['Constants']:<6} | {res['Duplicates']:<4}")
    
    # Global stats
    total_funcs = sum(r['Total'] for r in results)
    total_errors = sum(r['Errors'] for r in results)
    total_nans = sum(r['NaNs'] for r in results)
    total_consts = sum(r['Constants'] for r in results)
    total_dups = sum(r['Duplicates'] for r in results)

    print("\n" + "="*80)
    print("GLOBAL SUMMARY")
    print(f"Total Families: {len(results)}")
    print(f"Total Functions: {total_funcs}")
    print(f"Total Errors: {total_errors}")
    print(f"Total All-NaNs: {total_nans}")
    print(f"Total Constants: {total_consts}")
    print(f"Total Duplicates: {total_dups}")

if __name__ == "__main__":
    main()
