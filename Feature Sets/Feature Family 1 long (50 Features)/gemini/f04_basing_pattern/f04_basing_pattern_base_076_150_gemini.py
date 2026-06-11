# f04_basing_pattern_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _base_range(c, w):
    return (c.rolling(w, min_periods=1).max() / c.rolling(w, min_periods=1).min().replace(0, np.nan) - 1)

def _base_tightness(c, w):
    return c.pct_change().rolling(w, min_periods=1).std()

def _base_range_ohlc(h, l, w):
    return (h.rolling(w, min_periods=1).max() / l.rolling(w, min_periods=1).min().replace(0, np.nan) - 1)

def _z_score(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

# Feature 076: Max range 5d over 63d
def f04_basing_pattern_range_max_5d_63d_base_v076_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 5)
    res = rng.rolling(63, min_periods=1).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 077: Max range 21d over 252d
def f04_basing_pattern_range_max_21d_252d_base_v077_signal(arg_close):
    rng = _base_range(arg_close, 21)
    res = rng.rolling(252, min_periods=1).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 078: Min range 5d over 63d
def f04_basing_pattern_range_min_5d_63d_base_v078_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 5)
    res = rng.rolling(63, min_periods=1).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 079: Min range 21d over 252d
def f04_basing_pattern_range_min_21d_252d_base_v079_signal(arg_close):
    rng = _base_range(arg_close, 21)
    res = rng.rolling(252, min_periods=1).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 080: Range 5d relative to its 63d mean
def f04_basing_pattern_range_rel_mean_5d_63d_base_v080_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 5)
    res = rng / _sma(rng, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 081: Range 21d relative to its 252d mean
def f04_basing_pattern_range_rel_mean_21d_252d_base_v081_signal(arg_close):
    rng = _base_range(arg_close, 21)
    res = rng / _sma(rng, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 082: Tightness 5d relative to its 63d mean
def f04_basing_pattern_tightness_rel_mean_5d_63d_base_v082_signal(arg_close):
    t = _base_tightness(arg_close, 5)
    res = t / _sma(t, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 083: Tightness 21d relative to its 252d mean
def f04_basing_pattern_tightness_rel_mean_21d_252d_base_v083_signal(arg_close):
    t = _base_tightness(arg_close, 21)
    res = t / _sma(t, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 084: Breakout strength rel median 21d
def f04_basing_pattern_breakout_rel_median_21d_base_v084_signal(arg_close):
    h = arg_close.rolling(21, min_periods=1).max()
    res = arg_close / h.rolling(252, min_periods=1).median().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 085: Breakout strength rel median 63d
def f04_basing_pattern_breakout_rel_median_63d_base_v085_signal(arg_closeadj):
    h = arg_closeadj.rolling(63, min_periods=1).max()
    res = arg_closeadj / h.rolling(252, min_periods=1).median().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 086: Days range < 1% over 10d
def f04_basing_pattern_days_tight_1pct_10d_base_v086_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.01).rolling(10, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 087: Days range < 1% over 21d
def f04_basing_pattern_days_tight_1pct_21d_base_v087_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.01).rolling(21, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 088: Days range < 3% over 10d
def f04_basing_pattern_days_tight_3pct_10d_base_v086_signal_v2(arg_close): # unique name
    rng = _base_range(arg_close, 5)
    res = (rng < 0.03).rolling(10, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 088 (v088): Days range < 3% over 10d
def f04_basing_pattern_days_tight_3pct_10d_base_v088_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.03).rolling(10, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 089: Days range < 3% over 21d
def f04_basing_pattern_days_tight_3pct_21d_base_v089_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.03).rolling(21, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 090: Z-score volume volatility 21d (252d window)
def f04_basing_pattern_vol_volatility_z_21d_base_v090_signal(arg_volume):
    vv = arg_volume.pct_change().rolling(21, min_periods=1).std()
    res = _z_score(vv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 091: Z-score volume volatility 63d (252d window)
def f04_basing_pattern_vol_volatility_z_63d_base_v091_signal(arg_volume):
    vv = arg_volume.pct_change().rolling(63, min_periods=1).std()
    res = _z_score(vv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 092: Range to Tightness ratio 5d
def f04_basing_pattern_range_tight_ratio_5d_base_v092_signal(arg_high, arg_low, arg_close):
    r = _base_range_ohlc(arg_high, arg_low, 5)
    t = _base_tightness(arg_close, 5)
    res = r / t.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 093: Range to Tightness ratio 21d
def f04_basing_pattern_range_tight_ratio_21d_base_v093_signal(arg_close):
    r = _base_range(arg_close, 21)
    t = _base_tightness(arg_close, 21)
    res = r / t.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 094: Range to Tightness ratio 63d
def f04_basing_pattern_range_tight_ratio_63d_base_v094_signal(arg_closeadj):
    r = _base_range(arg_closeadj, 63)
    t = _base_tightness(arg_closeadj, 63)
    res = r / t.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 095: Base range 180d
def f04_basing_pattern_range_180d_base_v095_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 180)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 096: Base range 378d
def f04_basing_pattern_range_378d_base_v096_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 378)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 097: Base range 756d
def f04_basing_pattern_range_756d_base_v097_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 098: Tightness 180d
def f04_basing_pattern_tightness_180d_base_v098_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 180)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 099: Tightness 378d
def f04_basing_pattern_tightness_378d_base_v099_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 378)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 100: Tightness 756d
def f04_basing_pattern_tightness_756d_base_v100_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 101-115: Range variations with different windows
for w in [8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250]:
    exec(f"""
def f04_basing_pattern_range_{w}d_ext_base_v{101 + [8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250].index(w)}_signal(arg_close, arg_closeadj):
    if {w} <= 21:
        res = _base_range(arg_close, {w})
    else:
        res = _base_range(arg_closeadj, {w})
    return res.replace([np.inf, -np.inf], np.nan)
""")

# Feature 116-130: Tightness variations with different windows
for w in [8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250]:
    exec(f"""
def f04_basing_pattern_tightness_{w}d_ext_base_v{116 + [8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250].index(w)}_signal(arg_close, arg_closeadj):
    if {w} <= 21:
        res = _base_tightness(arg_close, {w})
    else:
        res = _base_tightness(arg_closeadj, {w})
    return res.replace([np.inf, -np.inf], np.nan)
""")

# Feature 131-140: Z-score range with different windows
for w in [8, 12, 15, 30, 40, 50, 90, 126, 180, 252]:
    exec(f"""
def f04_basing_pattern_range_z_{w}d_ext_base_v{131 + [8, 12, 15, 30, 40, 50, 90, 126, 180, 252].index(w)}_signal(arg_close, arg_closeadj):
    if {w} <= 21:
        rng = _base_range(arg_close, {w})
    else:
        rng = _base_range(arg_closeadj, {w})
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)
""")

# Feature 141-150: Z-score tightness with different windows
for w in [8, 12, 15, 30, 40, 50, 90, 126, 180, 252]:
    exec(f"""
def f04_basing_pattern_tightness_z_{w}d_ext_base_v{141 + [8, 12, 15, 30, 40, 50, 90, 126, 180, 252].index(w)}_signal(arg_close, arg_closeadj):
    if {w} <= 21:
        t = _base_tightness(arg_close, {w})
    else:
        t = _base_tightness(arg_closeadj, {w})
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)
""")

# Re-defining loop-generated functions explicitly to avoid registry issues if needed, 
# but I will just build the REGISTRY dynamically for these.

REGISTRY = {
    "f04_basing_pattern_range_max_5d_63d_base_v076_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_max_5d_63d_base_v076_signal},
    "f04_basing_pattern_range_max_21d_252d_base_v077_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_max_21d_252d_base_v077_signal},
    "f04_basing_pattern_range_min_5d_63d_base_v078_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_min_5d_63d_base_v078_signal},
    "f04_basing_pattern_range_min_21d_252d_base_v079_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_min_21d_252d_base_v079_signal},
    "f04_basing_pattern_range_rel_mean_5d_63d_base_v080_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_rel_mean_5d_63d_base_v080_signal},
    "f04_basing_pattern_range_rel_mean_21d_252d_base_v081_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_rel_mean_21d_252d_base_v081_signal},
    "f04_basing_pattern_tightness_rel_mean_5d_63d_base_v082_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_rel_mean_5d_63d_base_v082_signal},
    "f04_basing_pattern_tightness_rel_mean_21d_252d_base_v083_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_rel_mean_21d_252d_base_v083_signal},
    "f04_basing_pattern_breakout_rel_median_21d_base_v084_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_breakout_rel_median_21d_base_v084_signal},
    "f04_basing_pattern_breakout_rel_median_63d_base_v085_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_breakout_rel_median_63d_base_v085_signal},
    "f04_basing_pattern_days_tight_1pct_10d_base_v086_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_1pct_10d_base_v086_signal},
    "f04_basing_pattern_days_tight_1pct_21d_base_v087_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_1pct_21d_base_v087_signal},
    "f04_basing_pattern_days_tight_3pct_10d_base_v088_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_3pct_10d_base_v088_signal},
    "f04_basing_pattern_days_tight_3pct_21d_base_v089_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_3pct_21d_base_v089_signal},
    "f04_basing_pattern_vol_volatility_z_21d_base_v090_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_z_21d_base_v090_signal},
    "f04_basing_pattern_vol_volatility_z_63d_base_v091_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_z_63d_base_v091_signal},
    "f04_basing_pattern_range_tight_ratio_5d_base_v092_signal": {"inputs": ["arg_high", "arg_low", "arg_close"], "func": f04_basing_pattern_range_tight_ratio_5d_base_v092_signal},
    "f04_basing_pattern_range_tight_ratio_21d_base_v093_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_tight_ratio_21d_base_v093_signal},
    "f04_basing_pattern_range_tight_ratio_63d_base_v094_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_tight_ratio_63d_base_v094_signal},
    "f04_basing_pattern_range_180d_base_v095_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_180d_base_v095_signal},
    "f04_basing_pattern_range_378d_base_v096_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_378d_base_v096_signal},
    "f04_basing_pattern_range_756d_base_v097_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_756d_base_v097_signal},
    "f04_basing_pattern_tightness_180d_base_v098_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_180d_base_v098_signal},
    "f04_basing_pattern_tightness_378d_base_v099_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_378d_base_v099_signal},
    "f04_basing_pattern_tightness_756d_base_v100_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_756d_base_v100_signal},
}

# Add loop-generated features to REGISTRY
for i, w in enumerate([8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250]):
    REGISTRY[f"f04_basing_pattern_range_{w}d_ext_base_v{101+i}_signal"] = {"inputs": ["arg_close", "arg_closeadj"], "func": locals()[f"f04_basing_pattern_range_{w}d_ext_base_v{101+i}_signal"]}
for i, w in enumerate([8, 12, 15, 30, 40, 50, 90, 126, 180, 252, 378, 504, 756, 1000, 1250]):
    REGISTRY[f"f04_basing_pattern_tightness_{w}d_ext_base_v{116+i}_signal"] = {"inputs": ["arg_close", "arg_closeadj"], "func": locals()[f"f04_basing_pattern_tightness_{w}d_ext_base_v{116+i}_signal"]}
for i, w in enumerate([8, 12, 15, 30, 40, 50, 90, 126, 180, 252]):
    REGISTRY[f"f04_basing_pattern_range_z_{w}d_ext_base_v{131+i}_signal"] = {"inputs": ["arg_close", "arg_closeadj"], "func": locals()[f"f04_basing_pattern_range_z_{w}d_ext_base_v{131+i}_signal"]}
for i, w in enumerate([8, 12, 15, 30, 40, 50, 90, 126, 180, 252]):
    REGISTRY[f"f04_basing_pattern_tightness_z_{w}d_ext_base_v{141+i}_signal"] = {"inputs": ["arg_close", "arg_closeadj"], "func": locals()[f"f04_basing_pattern_tightness_z_{w}d_ext_base_v{141+i}_signal"]}

F04_BASING_PATTERN_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    import inspect
    pd.set_option('display.max_columns', None)
    np.random.seed(42)
    n = 2000 # Increased for long windows
    df = pd.DataFrame({
        "arg_open": np.exp(np.random.normal(0, 0.01, n).cumsum()) * 100,
    })
    df["arg_high"] = df["arg_open"] * (1 + np.abs(np.random.normal(0, 0.01, n)))
    df["arg_low"] = df["arg_open"] * (1 - np.abs(np.random.normal(0, 0.01, n)))
    df["arg_close"] = (df["arg_high"] + df["arg_low"]) / 2 + np.random.normal(0, 0.005, n)
    df["arg_closeadj"] = df["arg_close"] * 0.98
    df["arg_volume"] = np.random.exponential(1000, n)
    
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info["inputs"]]
        y1 = info["func"](*inputs)
        y2 = info["func"](*inputs)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[1250:].dropna()
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
        assert not q.isna().all()
    print("All tests passed!")
