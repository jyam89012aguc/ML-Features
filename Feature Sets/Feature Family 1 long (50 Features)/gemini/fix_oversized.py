
import os
import re

files_to_fix = [
    r"f32_leverage_acceleration\f32_leverage_acceleration_jerk_001_150_gemini.py",
    r"f31_cash_flow_acceleration\f31_cash_flow_acceleration_jerk_001_150_gemini.py",
    r"f30_margin_acceleration\f30_margin_acceleration_jerk_001_150_gemini.py",
    r"f34_revenue_jerk\f34_revenue_jerk_jerk_001_150_gemini.py",
    r"f32_leverage_acceleration\f32_leverage_acceleration_slope_001_150_gemini.py",
    r"f31_cash_flow_acceleration\f31_cash_flow_acceleration_slope_001_150_gemini.py",
    r"f30_margin_acceleration\f30_margin_acceleration_slope_001_150_gemini.py",
    r"f34_revenue_jerk\f34_revenue_jerk_slope_001_150_gemini.py"
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    v076_line = -1
    for i, line in enumerate(lines):
        if 'v076_signal' in line and line.strip().startswith('def '):
            v076_line = i
            break
            
    main_line = -1
    for i, line in enumerate(lines):
        if 'if __name__ == "__main__":' in line:
            main_line = i
            break
            
    if v076_line != -1 and main_line != -1:
        new_lines = lines[:v076_line] + lines[main_line:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Fixed {file_path}: kept lines 0-{v076_line} and {main_line}-end")
    else:
        print(f"Could not find boundaries in {file_path}: v076={v076_line}, main={main_line}")
