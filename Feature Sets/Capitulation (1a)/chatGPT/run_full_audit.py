import os
import sys
import importlib
import pandas as pd
import numpy as np
from audit_harness import audit_family

def main():
    root_dir = os.getcwd()
    families = [d for d in os.listdir(root_dir) if os.path.isdir(d) and (d[0].isdigit())]
    families.sort(key=lambda x: int(x.split('_')[0]))

    report = []
    report.append("# FINAL AUDIT REPORT\n")
    report.append("| Family | Total | Errors | NaNs | Const | Dups | Status |")
    report.append("|---|---|---|---|---|---|---|")

    missing_inputs_details = []

    for family in families:
        print(f"Auditing {family}...")
        try:
            res, dups = audit_family(family)
            
            total = len(res)
            errors = {k: v for k, v in res.items() if isinstance(v, str)}
            all_nan = [k for k, v in res.items() if isinstance(v, dict) and v['is_all_nan']]
            constants = [k for k, v in res.items() if isinstance(v, dict) and v['is_constant'] and not v['is_all_nan']]
            
            error_count = len(errors)
            nan_count = len(all_nan)
            const_count = len(constants)
            dup_count = len(dups)
            
            status = "✅ CLEAN" if error_count == 0 else "❌ ERRORS"
            
            report.append(f"| {family} | {total} | {error_count} | {nan_count} | {const_count} | {dup_count} | {status} |")
            
            if error_count > 0:
                for func_name, err_msg in errors.items():
                    if "Missing inputs" in err_msg:
                        missing_inputs_details.append(f"- **{family}**: `{func_name}` -> {err_msg}")
                    elif "Error" in err_msg:
                        # Also track other errors just in case
                        missing_inputs_details.append(f"- **{family}**: `{func_name}` -> {err_msg}")
        except Exception as e:
            print(f"Failed to audit {family}: {e}")
            report.append(f"| {family} | ERROR | ERROR | ERROR | ERROR | ERROR | ❌ CRASH |")

    report.append("\n## Missing Input Errors & Other Failures\n")
    if missing_inputs_details:
        report.extend(missing_inputs_details)
    else:
        report.append("None. All functions have required inputs.")

    with open("FINAL_AUDIT_REPORT.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("\nAudit complete. Results written to FINAL_AUDIT_REPORT.md")

if __name__ == "__main__":
    main()
