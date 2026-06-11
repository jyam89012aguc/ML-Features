# Project Memory: Semiconductor Financial Features Library

## Overview
This project contains a comprehensive library of semiconductor-specific financial features, organized into 244 folders (`f01` to `f244`). Each folder targets a specific financial or operational theme (e.g., Revenue Stability, Capex Dynamics, Inventory Velocity).

## Library Structure
- **Total Folders:** 244 (Continuous from f01 to f244).
- **Files per Folder:** 4 standardized Python scripts:
  - `..._base_001_075_gemini.py`: First 75 base signals.
  - `..._base_076_150_gemini.py`: Next 75 base signals.
  - `..._2nd_derivative_001_150_gemini.py`: Second-order derivatives of base signals.
  - `..._3rd_derivative_001_150_gemini.py`: Third-order derivatives of base signals.

## Audit Results
### Continuity
- **Status:** PASS
- **Details:** Verified zero numerical gaps in the sequence from f01 to f244.

### Portability
- **Status:** PASS
- **Details:** All hardcoded absolute paths were replaced with dynamic paths using `os.path.dirname(__file__)` or relative paths.

### Signal Quality
- **Self-Test Reliability:** 
  - Original features (f51-f237) generally pass functional self-tests but may show high correlation (>0.95) between very similar windows.
  - Newly generated features (f01-f50, f238-f243) are structurally sound but may occasionally encounter `KeyError` in self-tests if the synthetic data generator misses specific niche columns (e.g., `gross_margin`, `current_liabilities`).
- **Correlation:** High redundancy exists in folders where windows are narrowly spaced (e.g., 62-day vs 65-day averages).

## Recent Modifications (June 2026)
- **Mass Generation:** Populated 56 folders (`f01-f50` and `f238-f243`) with 150 unique complex formulas each.
- **Path Sanitization:** Workspace-wide removal of absolute paths to `C:\Users\jyama\Desktop\...`.
- **Structural Fixes:** Standardized `if __name__ == '__main__':` blocks across the library to improve automated testing compatibility.

## Future Recommendations
1. **Signal Differentiation:** Conduct a targeted sweep to increase window spacing in highly correlated feature pairs.
2. **Data Mocking:** Standardize the synthetic data generator to include all 40+ possible financial columns used across the library to eliminate `KeyError` in self-tests.
