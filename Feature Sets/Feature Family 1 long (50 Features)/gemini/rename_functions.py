import os
import re
import subprocess

base_dir = r"C:\Users\jyama\Desktop\active_non audited features per AI\Test Features 05\gemini\v1"
directories = [
    "f21_revenue_growth",
    "f22_margin_trajectory",
    "f23_cash_flow_trajectory",
    "f24_debt_trajectory",
    "f25_growth_vs_cost",
    "f26_dilution_rate",
    "f27_investment_trajectory",
    "f28_valuation_trajectory",
    "f29_revenue_acceleration",
    "f30_margin_acceleration",
]

mappings = {
    "f21_revenue_growth": "f21rg_",
    "f22_margin_trajectory": "f22mt_",
    "f23_cash_flow_trajectory": "f23cft_",
    "f24_debt_trajectory": "f24dt_",
    "f25_growth_vs_cost": "f25gvc_",
    "f26_dilution_rate": "f26dr_",
    "f27_investment_trajectory": "f27it_",
    "f28_valuation_trajectory": "f28vt_",
    "f29_revenue_acceleration": "f29ra_",
    "f30_margin_acceleration": "f30ma_",
}

for folder in directories:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        print(f"Directory {folder} not found, skipping.")
        continue
    
    short_prefix = mappings[folder]
    full_prefix = folder + "_"
    
    # Replacement order: longer first
    long_to_replace = short_prefix + full_prefix
    
    print(f"Processing directory: {folder}")
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Perform replacements
            new_content = content.replace(long_to_replace, full_prefix)
            new_content = new_content.replace(short_prefix, full_prefix)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  Updated: {filename}")
            else:
                print(f"  No changes needed for: {filename}")

# Verification
print("\nVerifying changes...")
for folder in directories:
    folder_path = os.path.join(base_dir, folder)
    py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]
    if not py_files:
        continue
    
    test_file = py_files[0]
    test_path = os.path.join(folder_path, test_file)
    print(f"Running test for {folder}: {test_file}")
    try:
        result = subprocess.run(["python", test_path], capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"  OK: {result.stdout.strip()}")
        else:
            print(f"  FAILED: {result.stderr.strip()}")
    except Exception as e:
        print(f"  ERROR: {str(e)}")
