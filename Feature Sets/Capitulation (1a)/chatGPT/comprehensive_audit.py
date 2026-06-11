import os
import subprocess
import sys
import re
from concurrent.futures import ProcessPoolExecutor

def audit_family(family_dir):
    try:
        process = subprocess.Popen(
            [sys.executable, "audit_harness.py", family_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        return family_dir, stdout, stderr, process.returncode
    except Exception as e:
        return family_dir, "", str(e), 1

def parse_output(family, stdout, stderr, returncode):
    if returncode != 0:
        return {
            "Family": family,
            "Total": 0,
            "Errors": 1,
            "NaNs": 0,
            "Constants": 0,
            "Duplicates": 0,
            "Status": "Failed"
        }

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
        dups = int(dup_match.group(1))

    return {
        "Family": family,
        "Total": total,
        "Errors": errors,
        "NaNs": nans,
        "Constants": constants,
        "Duplicates": dups,
        "Status": "Success"
    }

def main():
    root_dir = os.getcwd()
    dirs = [d for d in os.listdir(root_dir) if os.path.isdir(d) and d[0].isdigit()]
    dirs.sort()

    print(f"Starting audit for {len(dirs)} families...")

    results = []
    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(audit_family, d) for d in dirs]
        for i, future in enumerate(futures):
            family, stdout, stderr, returncode = future.result()
            res = parse_output(family, stdout, stderr, returncode)
            results.append(res)
            print(f"[{i+1}/{len(dirs)}] Completed {family}")

    # Generate Markdown Report
    report = "# Comprehensive Feature Audit Report\n\n"
    
    # Summary Table
    report += "## Summary Table\n\n"
    report += "| Family Name | Total Fns | Duplicates | Errors | Constants | Status |\n"
    report += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
    for res in results:
        report += f"| {res['Family']} | {res['Total']} | {res['Duplicates']} | {res['Errors']} | {res['Constants']} | {res['Status']} |\n"
    
    # System-Wide Findings
    total_funcs = sum(r['Total'] for r in results)
    total_errors = sum(r['Errors'] for r in results)
    total_nans = sum(r['NaNs'] for r in results)
    total_consts = sum(r['Constants'] for r in results)
    total_dups = sum(r['Duplicates'] for r in results)
    
    avg_redundancy = (total_dups / total_funcs * 100) if total_funcs > 0 else 0
    
    report += "\n## System-Wide Findings\n\n"
    report += f"- **Total Functions Audited**: {total_funcs}\n"
    report += f"- **Average Redundancy Rate**: {avg_redundancy:.2f}%\n"
    report += f"- **Total Errors**: {total_errors}\n"
    report += f"- **Total All-NaN Functions**: {total_nans}\n"
    report += f"- **Total Constant Functions**: {total_consts}\n"
    
    high_error_families = [r['Family'] for r in results if r['Errors'] > 0]
    if high_error_families:
        report += f"- **Families with Errors**: {', '.join(high_error_families)}\n"
    else:
        report += "- **Families with Errors**: None\n"

    # Actionable Recommendations
    report += "\n## Actionable Recommendations\n\n"
    
    clean_families = [r['Family'] for r in results if r['Errors'] == 0 and r['Duplicates'] == 0]
    redundant_families = [r['Family'] for r in results if r['Duplicates'] > (r['Total'] * 0.5) and r['Total'] > 0]
    surgical_families = [r['Family'] for r in results if r['Errors'] > 0]

    report += "### Clean Families (Ready for deployment)\n"
    if clean_families:
        for f in clean_families: report += f"- {f}\n"
    else:
        report += "- None\n"

    report += "\n### Mass-Bomb Redundant Families (Need consolidation)\n"
    if redundant_families:
        for f in redundant_families: report += f"- {f}\n"
    else:
        report += "- None\n"

    report += "\n### Surgical Fix Needed (Contain errors)\n"
    if surgical_families:
        for f in surgical_families: report += f"- {f}\n"
    else:
        report += "- None\n"

    with open("AUDIT_REPORT.md", "w") as f:
        f.write(report)

    print("\nAudit complete. Report saved to AUDIT_REPORT.md")

if __name__ == "__main__":
    main()
