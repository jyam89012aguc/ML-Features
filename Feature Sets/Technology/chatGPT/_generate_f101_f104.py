"""Generate technology feature families F101-F104 to fill the audit gaps.

F101 short_interest_dynamics  - short interest level/change, days-to-cover, squeeze setup
F102 estimate_revision_breadth - revision velocity, up/down breadth, PEAD drift
F103 options_implied_vol_regime - IV level/term/skew, put-call ratio
F104 macro_rates_sensitivity - beta to rates, USD, Nasdaq, semi-cycle

Mirrors the structure of F01-F100: 4 files per family (base_001_075, base_076_150,
2nd_derivatives_001_150, 3rd_derivatives_001_150), 75+75+150+150 = 450 functions.

Also patches technology_feature_manifest.csv / .json with the 4 new rows.
"""
import os, json, csv

HERE = os.path.dirname(os.path.abspath(__file__))

HEADER = (
    "import numpy as np\n"
    "import pandas as pd\n"
    "from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z\n"
    "\n\n"
)

WINDOWS = [5, 21, 63, 126, 252]
SPANS   = [5, 21, 63, 126, 252]
D2_NS   = [21, 63, 5, 126, 21, 5, 63, 126, 252, 21]   # cycling
D3_NS   = [5,  1, 21, 5, 63, 1, 21, 5, 1, 63]

# Each family defines 30 unique inner-expression templates over its input columns.
# First 15 are wrapped in _mean(.,w) -> base_001_075 (75 funcs, 15*5 windows).
# Last 15 are wrapped in _ewm(.,span) -> base_076_150 (75 funcs, 15*5 spans).

FAMILIES = [
    {
        "num": 101,
        "slug": "technology_f101_technology_short_interest_dynamics",
        "prefix": "tsi",
        "scope": "short-interest level, change, days-to-cover, squeeze setup, and price confirmation",
        "primary_column": "shortint",
        "secondary_column": "short_pct_float",
        "kind": "numeric",
        "inputs": ["shortint", "short_pct_float", "short_pct_shares", "days_to_cover",
                   "sharesbas", "volume", "closeadj"],
        "templates": [
            # base_001_075 - mean-wrapped
            "_safe_div(shortint, sharesbas.abs()+1e-9)",
            "short_pct_float",
            "short_pct_shares",
            "days_to_cover",
            "_pct_change(shortint, 21)",
            "_pct_change(shortint, 63)",
            "_pct_change(short_pct_float, 21)",
            "_pct_change(short_pct_float, 63)",
            "_diff(short_pct_shares, 21)",
            "_diff(days_to_cover, 21)",
            "_safe_div(shortint, volume.abs()+1e-9)",
            "_z(shortint, 252)",
            "_z(short_pct_float, 252)",
            "_corr(short_pct_float, _pct_change(closeadj, 21), 63)",
            "_corr(days_to_cover, _pct_change(closeadj, 5), 63)",
            # base_076_150 - ewm-wrapped
            "_safe_div(_diff(shortint, 21), shortint.abs()+1e-9)",
            "_safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)",
            "_safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)",
            "_safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)",
            "_rank(shortint, 252)",
            "_rank(short_pct_float, 252)",
            "_rank(days_to_cover, 252)",
            "_pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)",
            "_pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)",
            "_safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)",
            "_slope(_z(short_pct_float, 252), 63)",
            "_std(_diff(short_pct_float, 1), 63)",
            "_autocorr(short_pct_float, 63, 5)",
            "_skew(_diff(short_pct_float, 1), 252)",
            "-_safe_div(shortint, marketcap_proxy(closeadj, sharesbas).abs()+1e-9)".replace(
                "marketcap_proxy(closeadj, sharesbas)", "(closeadj*sharesbas)"),
        ],
    },
    {
        "num": 102,
        "slug": "technology_f102_estimate_revision_breadth",
        "prefix": "erb",
        "scope": "analyst estimate revisions: velocity, up/down breadth, dispersion, and PEAD drift",
        "primary_column": "eps_est",
        "secondary_column": "rev_est",
        "kind": "numeric",
        "inputs": ["eps_est", "rev_est", "eps_est_up", "eps_est_down",
                   "rev_est_up", "rev_est_down", "eps_disp", "rev_disp", "closeadj"],
        "templates": [
            # base_001_075
            "_pct_change(eps_est, 21)",
            "_pct_change(eps_est, 63)",
            "_pct_change(rev_est, 21)",
            "_pct_change(rev_est, 63)",
            "_safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)",
            "_safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)",
            "_diff(eps_est_up, 21) - _diff(eps_est_down, 21)",
            "_diff(rev_est_up, 21) - _diff(rev_est_down, 21)",
            "_safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)",
            "_safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)",
            "_z(_pct_change(eps_est, 21), 252)",
            "_z(_pct_change(rev_est, 21), 252)",
            "_corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)",
            "_corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)",
            "_slope(eps_est, 126)",
            # base_076_150
            "_slope(rev_est, 126)",
            "_safe_div(eps_disp, eps_est.abs()+1e-9)",
            "_safe_div(rev_disp, rev_est.abs()+1e-9)",
            "-_diff(eps_disp, 63)",
            "-_diff(rev_disp, 63)",
            "_rank(_pct_change(eps_est, 63), 252)",
            "_rank(_pct_change(rev_est, 63), 252)",
            "_safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5",
            "_safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5",
            "_pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)",
            "_pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)",
            "_autocorr(_pct_change(eps_est, 21), 252, 21)",
            "_std(_pct_change(eps_est, 21), 252)",
            "_skew(_pct_change(rev_est, 21), 252)",
            "_safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)",
        ],
    },
    {
        "num": 103,
        "slug": "technology_f103_options_implied_vol_regime",
        "prefix": "oiv",
        "scope": "options-implied volatility regime: IV level, IV-RV spread, skew, term structure, put-call",
        "primary_column": "iv",
        "secondary_column": "iv_skew",
        "kind": "numeric",
        "inputs": ["iv", "iv_skew", "iv_term", "put_call", "iv_rank", "hv", "closeadj", "volume"],
        "templates": [
            # base_001_075
            "iv",
            "iv - hv",
            "_safe_div(iv, hv.abs()+1e-9)",
            "iv_skew",
            "iv_term",
            "put_call",
            "iv_rank",
            "_diff(iv, 21)",
            "_diff(iv_skew, 21)",
            "_diff(put_call, 21)",
            "_z(iv, 252)",
            "_z(iv_skew, 252)",
            "_z(put_call, 252)",
            "_pct_change(iv, 21)",
            "_pct_change(iv_rank, 21)",
            # base_076_150
            "_corr(iv, _pct_change(closeadj, 5), 63)",
            "_corr(iv_skew, _pct_change(closeadj, 5), 63)",
            "_corr(put_call, _pct_change(closeadj, 5), 63)",
            "_corr(iv, _pct_change(volume, 5), 63)",
            "_slope(iv, 63)",
            "_slope(iv_skew, 63)",
            "_rank(iv, 252)",
            "_rank(iv_skew, 252)",
            "_rank(put_call, 252)",
            "_std(_diff(iv, 1), 63)",
            "_skew(_diff(iv, 1), 252)",
            "_autocorr(iv, 63, 5)",
            "iv_term - iv",
            "_safe_div(iv_term, iv.abs()+1e-9)",
            "_pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)",
        ],
    },
    {
        "num": 104,
        "slug": "technology_f104_macro_rates_sensitivity",
        "prefix": "mrs",
        "scope": "macro/rates sensitivity: beta to 10y rates, USD, Nasdaq, semi cycle, and risk-on/off transitions",
        "primary_column": "closeadj",
        "secondary_column": "rate_10y",
        "kind": "numeric",
        "inputs": ["closeadj", "volume", "beta1y", "beta5y",
                   "rate_10y", "dxy", "ixic", "sox", "return1y"],
        "templates": [
            # base_001_075
            "_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)",
            "_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)",
            "_corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)",
            "_corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)",
            "_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)",
            "_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)",
            "_corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)",
            "_corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)",
            "_corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)",
            "_corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)",
            "_pct_change(closeadj, 21) - _pct_change(ixic, 21)",
            "_pct_change(closeadj, 63) - _pct_change(ixic, 63)",
            "_pct_change(closeadj, 21) - _pct_change(sox, 21)",
            "_pct_change(closeadj, 63) - _pct_change(sox, 63)",
            "beta1y",
            # base_076_150
            "beta5y",
            "_diff(beta1y, 63)",
            "_diff(beta5y, 252)",
            "_pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)",
            "_pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)",
            "_pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)",
            "_pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)",
            "_pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)",
            "_z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)",
            "_z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)",
            "_slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)",
            "_slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)",
            "_safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)",
            "_safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)",
            "return1y - _pct_change(ixic, 252)",
        ],
    },
]


def make_func_prefix(fam):
    return f"cg_f{fam['num']}_technology_f{fam['num']}_{'_'.join(fam['slug'].split('_')[2:])}"


def render_family(fam):
    fp = make_func_prefix(fam)
    sig_inputs = ", ".join(fam["inputs"])
    templates = fam["templates"]
    assert len(templates) == 30, f"Family {fam['num']} needs exactly 30 templates, got {len(templates)}"

    # --- base_001_075: 15 templates (idx 0..14) x 5 windows = 75 funcs, _mean wrapper
    base1 = HEADER
    v = 1
    for t_idx in range(15):
        for w_idx, w in enumerate(WINDOWS):
            core = (v - 1) % 15
            base1 += f"# core{core:02d} mean {w}d\n"
            base1 += f"def {fp}_core{core:02d}_mean_{w}d_base_v{v:03d}_signal({sig_inputs}):\n"
            base1 += f"    series = {templates[t_idx]}\n"
            base1 += f"    result = _mean(series, {w})\n"
            base1 += f"    return _clean(result)\n\n"
            v += 1
    assert v == 76

    # --- base_076_150: 15 templates (idx 15..29) x 5 spans = 75 funcs, _ewm wrapper
    base2 = HEADER
    for t_idx in range(15, 30):
        for s_idx, s in enumerate(SPANS):
            core = (v - 1) % 15
            base2 += f"# core{core:02d} ewm {s}d\n"
            base2 += f"def {fp}_core{core:02d}_ewm_{s}d_base_v{v:03d}_signal({sig_inputs}):\n"
            base2 += f"    series = {templates[t_idx]}\n"
            base2 += f"    result = _ewm(series, {s})\n"
            base2 += f"    return _clean(result)\n\n"
            v += 1
    assert v == 151

    # --- 2nd_derivatives_001_150: 150 funcs, z-scored slope of each base inner expression
    deriv2 = HEADER
    for v2 in range(1, 151):
        t_idx = (v2 - 1) // 5
        inner = templates[t_idx]
        wrap_window = WINDOWS[(v2 - 1) % 5] if v2 <= 75 else SPANS[(v2 - 1) % 5]
        wrap_call = f"_mean(series, {wrap_window})" if v2 <= 75 else f"_ewm(series, {wrap_window})"
        n2 = D2_NS[(v2 - 1) % len(D2_NS)]
        core = (v2 - 1) % 15
        wname = wrap_window
        op_tag = "mean" if v2 <= 75 else "ewm"
        deriv2 += f"# core{core:02d} slope {op_tag} {wname}d\n"
        deriv2 += f"def {fp}_core{core:02d}_{op_tag}_{wname}d_slope_v{v2:03d}_signal({sig_inputs}):\n"
        deriv2 += f"    series = {inner}\n"
        deriv2 += f"    base = {wrap_call}\n"
        deriv2 += f"    result = _safe_div(_diff(base, {n2}), _std(base, {n2}).abs() + 1e-9)\n"
        deriv2 += f"    return _clean(result)\n\n"

    # --- 3rd_derivatives_001_150: 150 funcs, acceleration of 2nd-derivative
    deriv3 = HEADER
    for v3 in range(1, 151):
        t_idx = (v3 - 1) // 5
        inner = templates[t_idx]
        wrap_window = WINDOWS[(v3 - 1) % 5] if v3 <= 75 else SPANS[(v3 - 1) % 5]
        wrap_call = f"_mean(series, {wrap_window})" if v3 <= 75 else f"_ewm(series, {wrap_window})"
        n2 = D2_NS[(v3 - 1) % len(D2_NS)]
        n3 = D3_NS[(v3 - 1) % len(D3_NS)]
        core = (v3 - 1) % 15
        wname = wrap_window
        op_tag = "mean" if v3 <= 75 else "ewm"
        deriv3 += f"# core{core:02d} accel {op_tag} {wname}d\n"
        deriv3 += f"def {fp}_core{core:02d}_{op_tag}_{wname}d_accel_v{v3:03d}_signal({sig_inputs}):\n"
        deriv3 += f"    series = {inner}\n"
        deriv3 += f"    base = {wrap_call}\n"
        deriv3 += f"    d2 = _safe_div(_diff(base, {n2}), _std(base, {n2}).abs() + 1e-9)\n"
        deriv3 += f"    result = _diff(d2, {n3})\n"
        deriv3 += f"    return _clean(result)\n\n"

    return base1, base2, deriv2, deriv3


def write_family(fam):
    folder = os.path.join(HERE, fam["slug"])
    os.makedirs(folder, exist_ok=True)
    base1, base2, deriv2, deriv3 = render_family(fam)
    short_slug = "_".join(fam["slug"].split("_")[2:])  # drop "technology_fXXX_" prefix? no -- keep style
    # existing files: technology_f01_technology_price_momentum_base_001_075_chatgpt.py
    # i.e. <slug>_<suffix>_chatgpt.py
    files = {
        f"{fam['slug']}_base_001_075_chatgpt.py": base1,
        f"{fam['slug']}_base_076_150_chatgpt.py": base2,
        f"{fam['slug']}_2nd_derivatives_001_150_chatgpt.py": deriv2,
        f"{fam['slug']}_3rd_derivatives_001_150_chatgpt.py": deriv3,
    }
    for fname, content in files.items():
        with open(os.path.join(folder, fname), "w", encoding="utf-8") as f:
            f.write(content)


def update_manifest():
    csv_path = os.path.join(HERE, "technology_feature_manifest.csv")
    json_path = os.path.join(HERE, "technology_feature_manifest.json")

    # CSV: append 4 rows if not already present
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    existing_nums = {int(r[0]) for r in rows[1:] if r and r[0].isdigit()}
    for fam in FAMILIES:
        if fam["num"] in existing_nums:
            continue
        rows.append([
            str(fam["num"]),
            fam["slug"],
            fam["prefix"],
            make_func_prefix(fam),
            fam["scope"],
            fam["primary_column"],
            fam["secondary_column"],
            fam["kind"],
            "4",
            "450",
        ])
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerows(rows)

    # JSON: append 4 entries if not already present
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    existing_nums = {entry["number"] for entry in data}
    for fam in FAMILIES:
        if fam["num"] in existing_nums:
            continue
        data.append({
            "number": fam["num"],
            "family_slug": fam["slug"],
            "prefix": fam["prefix"],
            "function_prefix": make_func_prefix(fam),
            "scope": fam["scope"],
            "primary_column": fam["primary_column"],
            "secondary_column": fam["secondary_column"],
            "kind": fam["kind"],
            "files": 4,
            "features": 450,
        })
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    for fam in FAMILIES:
        write_family(fam)
        print(f"wrote family F{fam['num']} -> {fam['slug']}")
    update_manifest()
    print("manifest updated")
