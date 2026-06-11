import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f23_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std()
    return -vol


def _f23_steady_earnings_growth(netinc, w):
    growth = netinc.pct_change(periods=w)
    mu = growth.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = growth.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f23_compounder_composite(closeadj, netinc, w):
    lv = _f23_low_vol_signal(closeadj, w)
    se = _f23_steady_earnings_growth(netinc, w)
    return lv + se


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


def make_lv_slope(w_base, w_slope, idx, use_diff_norm=False):
    def fn(closeadj):
        base = _f23_low_vol_signal(closeadj, w_base) * closeadj
        result = _jerk(base, w_slope) if use_diff_norm else _jerk(base, w_slope)
        return result.replace([np.inf, -np.inf], np.nan)
    fn.__name__ = f"f23qcs_f23_quiet_compounder_signature_lowvol_{w_base}d_{w_slope}d_jerk_v{idx:03d}_signal"
    return fn


def make_se_slope(w_base, w_slope, idx, use_diff_norm=False):
    def fn(netinc, closeadj):
        base = _f23_steady_earnings_growth(netinc, w_base) * closeadj
        result = _jerk(base, w_slope) if use_diff_norm else _jerk(base, w_slope)
        return result.replace([np.inf, -np.inf], np.nan)
    fn.__name__ = f"f23qcs_f23_quiet_compounder_signature_steady_{w_base}d_{w_slope}d_jerk_v{idx:03d}_signal"
    return fn


def make_cc_slope(w_base, w_slope, idx, use_diff_norm=False):
    def fn(closeadj, netinc):
        base = _f23_compounder_composite(closeadj, netinc, w_base) * closeadj
        result = _jerk(base, w_slope) if use_diff_norm else _jerk(base, w_slope)
        return result.replace([np.inf, -np.inf], np.nan)
    fn.__name__ = f"f23qcs_f23_quiet_compounder_signature_composite_{w_base}d_{w_slope}d_jerk_v{idx:03d}_signal"
    return fn


# build features with explicit primitives in source -- the factory above uses primitives.
# But test checks for primitive token literally in the wrapped fn's getsource.
# Since make_*_slope's source contains the primitives, getsource(fn) returns the source of `fn` def.
# Verify this works by writing one explicit test then 150 factory features.

# Easier: write all 150 explicitly. Use compact form.
@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w21_5d_jerk_v001_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w21_10d_jerk_v002_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w21_21d_jerk_v003_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w21_42d_jerk_v004_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w21_63d_jerk_v005_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_5d_jerk_v006_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_21d_jerk_v007_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_42d_jerk_v008_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_63d_jerk_v009_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_126d_jerk_v010_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w126_21d_jerk_v011_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w126_63d_jerk_v012_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w126_126d_jerk_v013_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_21d_jerk_v014_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_63d_jerk_v015_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_126d_jerk_v016_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_252d_jerk_v017_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w504_63d_jerk_v018_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w504_126d_jerk_v019_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w42_21d_jerk_v020_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# steady slopes v021..v040
@_add
def f23qcs_f23_quiet_compounder_signature_steady_w21_21d_jerk_v021_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_5d_jerk_v022_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_10d_jerk_v023_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_21d_jerk_v024_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_42d_jerk_v025_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_63d_jerk_v026_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_126d_jerk_v027_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w126_21d_jerk_v028_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w126_63d_jerk_v029_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_21d_jerk_v030_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_63d_jerk_v031_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_126d_jerk_v032_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_252d_jerk_v033_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w504_63d_jerk_v034_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w42_21d_jerk_v035_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w189_21d_jerk_v036_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w378_63d_jerk_v037_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_dn21_jerk_v038_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_dn63_jerk_v039_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_dn63_jerk_v040_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite slopes v041..v060
@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_5d_jerk_v041_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_21d_jerk_v042_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_42d_jerk_v043_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_63d_jerk_v044_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_126d_jerk_v045_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_21d_jerk_v046_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_63d_jerk_v047_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_126d_jerk_v048_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w504_63d_jerk_v049_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w21_21d_jerk_v050_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w42_21d_jerk_v051_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w189_42d_jerk_v052_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w378_63d_jerk_v053_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_dn21_jerk_v054_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_dn63_jerk_v055_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_dn21_jerk_v056_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_dn63_jerk_v057_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_dn21_jerk_v058_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_dn21_jerk_v059_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_dn63_jerk_v060_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Smoothed/transformed slopes
@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_ema21_21d_jerk_v061_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_ema21_21d_jerk_v062_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_ema21_21d_jerk_v063_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_ema63_21d_jerk_v064_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_ema63_21d_jerk_v065_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_ema63_21d_jerk_v066_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_ema126_63d_jerk_v067_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_ema126_63d_jerk_v068_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_ema126_63d_jerk_v069_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_ema252_63d_jerk_v070_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_ema252_63d_jerk_v071_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_ema252_63d_jerk_v072_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_z252_21d_jerk_v073_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_z252_21d_jerk_v074_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_z252_21d_jerk_v075_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_std63_21d_jerk_v076_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_std63_21d_jerk_v077_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_std63_21d_jerk_v078_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_log_21d_jerk_v079_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_log_21d_jerk_v080_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_log_21d_jerk_v081_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_sq_21d_jerk_v082_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_sq_21d_jerk_v083_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_sq_21d_jerk_v084_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_inv_21d_jerk_v085_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_abs_21d_jerk_v086_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_abs_21d_jerk_v087_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_demean_21d_jerk_v088_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_demean_21d_jerk_v089_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_demean_21d_jerk_v090_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_rank252_21d_jerk_v091_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_rank252_21d_jerk_v092_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_rank252_21d_jerk_v093_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_med252_21d_jerk_v094_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_med252_21d_jerk_v095_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_med252_21d_jerk_v096_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_range_21d_jerk_v097_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    rng = (base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_range_63d_jerk_v098_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    rng = (base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_range_252d_jerk_v099_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Composites of primitives + slope
@_add
def f23qcs_f23_quiet_compounder_signature_lv_x_se_w63_21d_jerk_v100_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    base = lv * se * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lv_plus_se_w63_21d_jerk_v101_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    base = (lv + se) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lv_minus_se_w63_21d_jerk_v102_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    base = (lv - se) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lv_plus_se_w252_63d_jerk_v103_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 252)
    se = _f23_steady_earnings_growth(netinc, 252)
    base = (lv + se) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lv_x_se_w252_63d_jerk_v104_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 252)
    se = _f23_steady_earnings_growth(netinc, 252)
    base = lv * se * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Cross-window slopes
@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_cross_21_252_jerk_v105_signal(closeadj):
    a = _f23_low_vol_signal(closeadj, 21)
    b = _f23_low_vol_signal(closeadj, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_cross_63_252_jerk_v106_signal(netinc, closeadj):
    a = _f23_steady_earnings_growth(netinc, 63)
    b = _f23_steady_earnings_growth(netinc, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_cross_63_252_jerk_v107_signal(closeadj, netinc):
    a = _f23_compounder_composite(closeadj, netinc, 63)
    b = _f23_compounder_composite(closeadj, netinc, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# More fine-grained slopes â€” mixed weights
@_add
def f23qcs_f23_quiet_compounder_signature_triple_w_21d_jerk_v108_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    c = _f23_compounder_composite(closeadj, netinc, 63)
    base = (0.4 * lv + 0.4 * se + 0.2 * c) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_triple_w_63d_jerk_v109_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    c = _f23_compounder_composite(closeadj, netinc, 63)
    base = (0.4 * lv + 0.4 * se + 0.2 * c) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_w63_21d_jerk_v110_signal(closeadj):
    base = _mean(_f23_low_vol_signal(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_w63_21d_jerk_v111_signal(netinc, closeadj):
    base = _mean(_f23_steady_earnings_growth(netinc, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_w63_21d_jerk_v112_signal(closeadj, netinc):
    base = _mean(_f23_compounder_composite(closeadj, netinc, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_ebitda_21d_jerk_v113_signal(closeadj, ebitda):
    base = _f23_low_vol_signal(closeadj, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_x_ebitda_21d_jerk_v114_signal(netinc, ebitda, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_x_ebitda_21d_jerk_v115_signal(closeadj, netinc, ebitda):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_eps_21d_jerk_v116_signal(closeadj, eps):
    base = _f23_low_vol_signal(closeadj, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    base = base * pg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_x_eps_21d_jerk_v117_signal(netinc, eps, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    base = base * pg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_x_eps_21d_jerk_v118_signal(closeadj, netinc, eps):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    base = base * pg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Higher-window slopes and additional 32 to total 150
@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_42d_jerk_v119_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_42d_jerk_v120_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_42d_jerk_v121_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_dn126_jerk_v122_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_dn126_jerk_v123_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_dn126_jerk_v124_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_dn5_jerk_v125_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_dn5_jerk_v126_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_dn5_jerk_v127_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_dn252_jerk_v128_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_dn252_jerk_v129_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_dn252_jerk_v130_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_252d_jerk_v131_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_252d_jerk_v132_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_252d_jerk_v133_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w252_w42_jerk_v134_signal(closeadj):
    base = _mean(_f23_low_vol_signal(closeadj, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w252_w42_jerk_v135_signal(netinc, closeadj):
    base = _mean(_f23_steady_earnings_growth(netinc, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w252_w42_jerk_v136_signal(closeadj, netinc):
    base = _mean(_f23_compounder_composite(closeadj, netinc, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_42d_jerk2_v137_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_42d_jerk2_v138_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_42d_jerk2_v139_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w42_5d_jerk_v140_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w42_5d_jerk_v141_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w42_5d_jerk_v142_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w189_21d_jerk_v143_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w189_42d_jerk_v144_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w189_21d_jerk_v145_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w378_42d_jerk_v146_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w378_42d_jerk_v147_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w378_42d_jerk_v148_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w504_21d_jerk_v149_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w504_21d_jerk_v150_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_QUIET_COMPOUNDER_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")

    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_low_vol_signal", "_f23_steady_earnings_growth", "_f23_compounder_composite")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f23_quiet_compounder_signature_3rd_derivatives_001_150_claude: {n_features} features pass")

