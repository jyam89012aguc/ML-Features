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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f31_revenue_spike(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (revenue - m) / sd


def _f31_spike_signature(revenue, w):
    pk = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    tr = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - tr) / (pk - tr).replace(0, np.nan)


def _f31_mean_reversion_pulse(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (m - revenue) / m

def f31rss_f31_regime_spike_signature_p0_xcls_sp5_5d_slope_v001_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sd5_5d_slope_v002_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_dn5_5d_slope_v003_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sp21_5d_slope_v004_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sd21_5d_slope_v005_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_dn21_5d_slope_v006_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sp63_5d_slope_v007_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sd63_5d_slope_v008_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_dn63_5d_slope_v009_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sp126_5d_slope_v010_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_sd126_5d_slope_v011_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcls_dn126_5d_slope_v012_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sp5_5d_slope_v013_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sd5_5d_slope_v014_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_dn5_5d_slope_v015_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sp21_5d_slope_v016_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sd21_5d_slope_v017_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_dn21_5d_slope_v018_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sp63_5d_slope_v019_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sd63_5d_slope_v020_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_dn63_5d_slope_v021_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sp126_5d_slope_v022_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_sd126_5d_slope_v023_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsabs_dn126_5d_slope_v024_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).abs() * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sp5_5d_slope_v025_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sd5_5d_slope_v026_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_dn5_5d_slope_v027_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sp21_5d_slope_v028_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sd21_5d_slope_v029_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_dn21_5d_slope_v030_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sp63_5d_slope_v031_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sd63_5d_slope_v032_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_dn63_5d_slope_v033_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sp126_5d_slope_v034_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_sd126_5d_slope_v035_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclssq_dn126_5d_slope_v036_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * (_f31_revenue_spike(revenue, 5)).abs()
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sp5_5d_slope_v037_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sd5_5d_slope_v038_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_dn5_5d_slope_v039_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sp21_5d_slope_v040_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sd21_5d_slope_v041_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_dn21_5d_slope_v042_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sp63_5d_slope_v043_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sd63_5d_slope_v044_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_dn63_5d_slope_v045_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sp126_5d_slope_v046_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_sd126_5d_slope_v047_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xmcls_dn126_5d_slope_v048_signal(closeadj, revenue):
    base = _mean(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sp5_5d_slope_v049_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sd5_5d_slope_v050_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_dn5_5d_slope_v051_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sp21_5d_slope_v052_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sd21_5d_slope_v053_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_dn21_5d_slope_v054_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sp63_5d_slope_v055_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sd63_5d_slope_v056_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_dn63_5d_slope_v057_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sp126_5d_slope_v058_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_sd126_5d_slope_v059_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xstdcls_dn126_5d_slope_v060_signal(closeadj, revenue):
    base = _std(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sp5_5d_slope_v061_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sd5_5d_slope_v062_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_dn5_5d_slope_v063_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sp21_5d_slope_v064_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sd21_5d_slope_v065_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_dn21_5d_slope_v066_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sp63_5d_slope_v067_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sd63_5d_slope_v068_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_dn63_5d_slope_v069_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sp126_5d_slope_v070_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_sd126_5d_slope_v071_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xzcls_dn126_5d_slope_v072_signal(closeadj, revenue):
    base = _z(_f31_revenue_spike(revenue, 5), 26) * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sp5_5d_slope_v073_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sd5_5d_slope_v074_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_dn5_5d_slope_v075_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sp21_5d_slope_v076_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sd21_5d_slope_v077_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_dn21_5d_slope_v078_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sp63_5d_slope_v079_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sd63_5d_slope_v080_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_dn63_5d_slope_v081_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sp126_5d_slope_v082_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_sd126_5d_slope_v083_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xemacls_dn126_5d_slope_v084_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).ewm(span=26, adjust=False).mean() * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sp5_5d_slope_v085_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sd5_5d_slope_v086_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_dn5_5d_slope_v087_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sp21_5d_slope_v088_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sd21_5d_slope_v089_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_dn21_5d_slope_v090_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sp63_5d_slope_v091_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sd63_5d_slope_v092_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_dn63_5d_slope_v093_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sp126_5d_slope_v094_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_sd126_5d_slope_v095_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xlogcls_dn126_5d_slope_v096_signal(closeadj, revenue):
    base = np.log((_f31_revenue_spike(revenue, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sp5_5d_slope_v097_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sd5_5d_slope_v098_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_dn5_5d_slope_v099_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sp21_5d_slope_v100_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sd21_5d_slope_v101_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_dn21_5d_slope_v102_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sp63_5d_slope_v103_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sd63_5d_slope_v104_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_dn63_5d_slope_v105_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sp126_5d_slope_v106_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_sd126_5d_slope_v107_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xsgncls_dn126_5d_slope_v108_signal(closeadj, revenue):
    base = np.sign(_f31_revenue_spike(revenue, 5)) * closeadj * (1.0 + (_f31_revenue_spike(revenue, 5)).abs())
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sp5_5d_slope_v109_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sd5_5d_slope_v110_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_dn5_5d_slope_v111_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sp21_5d_slope_v112_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sd21_5d_slope_v113_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_dn21_5d_slope_v114_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sp63_5d_slope_v115_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sd63_5d_slope_v116_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_dn63_5d_slope_v117_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sp126_5d_slope_v118_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_sd126_5d_slope_v119_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsret_dn126_5d_slope_v120_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj * closeadj.pct_change(5)
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sp5_5d_slope_v121_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sd5_5d_slope_v122_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_dn5_5d_slope_v123_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sp21_5d_slope_v124_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sd21_5d_slope_v125_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_dn21_5d_slope_v126_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sp63_5d_slope_v127_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sd63_5d_slope_v128_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_dn63_5d_slope_v129_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sp126_5d_slope_v130_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_sd126_5d_slope_v131_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsema21_dn126_5d_slope_v132_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sp5_5d_slope_v133_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sd5_5d_slope_v134_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_dn5_5d_slope_v135_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sp21_5d_slope_v136_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sd21_5d_slope_v137_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_dn21_5d_slope_v138_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sp63_5d_slope_v139_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sd63_5d_slope_v140_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_dn63_5d_slope_v141_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _diff(base, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sp126_5d_slope_v142_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_sd126_5d_slope_v143_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xclsma63_dn126_5d_slope_v144_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _diff(base, 126) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_sp5_5d_slope_v145_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_sd5_5d_slope_v146_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_dn5_5d_slope_v147_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _diff(base, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_sp21_5d_slope_v148_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_sd21_5d_slope_v149_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31rss_f31_regime_spike_signature_p0_xcumcls_dn21_5d_slope_v150_signal(closeadj, revenue):
    base = (_f31_revenue_spike(revenue, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    result = _diff(base, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31rss_f31_regime_spike_signature_p0_xcls_sp5_5d_slope_v001_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sd5_5d_slope_v002_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_dn5_5d_slope_v003_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sp21_5d_slope_v004_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sd21_5d_slope_v005_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_dn21_5d_slope_v006_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sp63_5d_slope_v007_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sd63_5d_slope_v008_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_dn63_5d_slope_v009_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sp126_5d_slope_v010_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_sd126_5d_slope_v011_signal,
    f31rss_f31_regime_spike_signature_p0_xcls_dn126_5d_slope_v012_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sp5_5d_slope_v013_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sd5_5d_slope_v014_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_dn5_5d_slope_v015_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sp21_5d_slope_v016_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sd21_5d_slope_v017_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_dn21_5d_slope_v018_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sp63_5d_slope_v019_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sd63_5d_slope_v020_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_dn63_5d_slope_v021_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sp126_5d_slope_v022_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_sd126_5d_slope_v023_signal,
    f31rss_f31_regime_spike_signature_p0_xclsabs_dn126_5d_slope_v024_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sp5_5d_slope_v025_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sd5_5d_slope_v026_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_dn5_5d_slope_v027_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sp21_5d_slope_v028_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sd21_5d_slope_v029_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_dn21_5d_slope_v030_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sp63_5d_slope_v031_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sd63_5d_slope_v032_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_dn63_5d_slope_v033_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sp126_5d_slope_v034_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_sd126_5d_slope_v035_signal,
    f31rss_f31_regime_spike_signature_p0_xclssq_dn126_5d_slope_v036_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sp5_5d_slope_v037_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sd5_5d_slope_v038_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_dn5_5d_slope_v039_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sp21_5d_slope_v040_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sd21_5d_slope_v041_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_dn21_5d_slope_v042_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sp63_5d_slope_v043_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sd63_5d_slope_v044_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_dn63_5d_slope_v045_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sp126_5d_slope_v046_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_sd126_5d_slope_v047_signal,
    f31rss_f31_regime_spike_signature_p0_xmcls_dn126_5d_slope_v048_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sp5_5d_slope_v049_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sd5_5d_slope_v050_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_dn5_5d_slope_v051_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sp21_5d_slope_v052_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sd21_5d_slope_v053_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_dn21_5d_slope_v054_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sp63_5d_slope_v055_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sd63_5d_slope_v056_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_dn63_5d_slope_v057_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sp126_5d_slope_v058_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_sd126_5d_slope_v059_signal,
    f31rss_f31_regime_spike_signature_p0_xstdcls_dn126_5d_slope_v060_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sp5_5d_slope_v061_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sd5_5d_slope_v062_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_dn5_5d_slope_v063_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sp21_5d_slope_v064_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sd21_5d_slope_v065_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_dn21_5d_slope_v066_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sp63_5d_slope_v067_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sd63_5d_slope_v068_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_dn63_5d_slope_v069_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sp126_5d_slope_v070_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_sd126_5d_slope_v071_signal,
    f31rss_f31_regime_spike_signature_p0_xzcls_dn126_5d_slope_v072_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sp5_5d_slope_v073_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sd5_5d_slope_v074_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_dn5_5d_slope_v075_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sp21_5d_slope_v076_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sd21_5d_slope_v077_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_dn21_5d_slope_v078_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sp63_5d_slope_v079_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sd63_5d_slope_v080_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_dn63_5d_slope_v081_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sp126_5d_slope_v082_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_sd126_5d_slope_v083_signal,
    f31rss_f31_regime_spike_signature_p0_xemacls_dn126_5d_slope_v084_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sp5_5d_slope_v085_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sd5_5d_slope_v086_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_dn5_5d_slope_v087_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sp21_5d_slope_v088_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sd21_5d_slope_v089_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_dn21_5d_slope_v090_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sp63_5d_slope_v091_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sd63_5d_slope_v092_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_dn63_5d_slope_v093_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sp126_5d_slope_v094_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_sd126_5d_slope_v095_signal,
    f31rss_f31_regime_spike_signature_p0_xlogcls_dn126_5d_slope_v096_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sp5_5d_slope_v097_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sd5_5d_slope_v098_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_dn5_5d_slope_v099_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sp21_5d_slope_v100_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sd21_5d_slope_v101_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_dn21_5d_slope_v102_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sp63_5d_slope_v103_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sd63_5d_slope_v104_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_dn63_5d_slope_v105_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sp126_5d_slope_v106_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_sd126_5d_slope_v107_signal,
    f31rss_f31_regime_spike_signature_p0_xsgncls_dn126_5d_slope_v108_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sp5_5d_slope_v109_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sd5_5d_slope_v110_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_dn5_5d_slope_v111_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sp21_5d_slope_v112_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sd21_5d_slope_v113_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_dn21_5d_slope_v114_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sp63_5d_slope_v115_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sd63_5d_slope_v116_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_dn63_5d_slope_v117_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sp126_5d_slope_v118_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_sd126_5d_slope_v119_signal,
    f31rss_f31_regime_spike_signature_p0_xclsret_dn126_5d_slope_v120_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sp5_5d_slope_v121_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sd5_5d_slope_v122_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_dn5_5d_slope_v123_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sp21_5d_slope_v124_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sd21_5d_slope_v125_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_dn21_5d_slope_v126_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sp63_5d_slope_v127_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sd63_5d_slope_v128_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_dn63_5d_slope_v129_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sp126_5d_slope_v130_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_sd126_5d_slope_v131_signal,
    f31rss_f31_regime_spike_signature_p0_xclsema21_dn126_5d_slope_v132_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sp5_5d_slope_v133_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sd5_5d_slope_v134_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_dn5_5d_slope_v135_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sp21_5d_slope_v136_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sd21_5d_slope_v137_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_dn21_5d_slope_v138_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sp63_5d_slope_v139_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sd63_5d_slope_v140_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_dn63_5d_slope_v141_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sp126_5d_slope_v142_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_sd126_5d_slope_v143_signal,
    f31rss_f31_regime_spike_signature_p0_xclsma63_dn126_5d_slope_v144_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_sp5_5d_slope_v145_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_sd5_5d_slope_v146_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_dn5_5d_slope_v147_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_sp21_5d_slope_v148_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_sd21_5d_slope_v149_signal,
    f31rss_f31_regime_spike_signature_p0_xcumcls_dn21_5d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_REGIME_SPIKE_SIGNATURE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f31_revenue_spike', '_f31_spike_signature', '_f31_mean_reversion_pulse')
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
    print(f"OK f31_regime_spike_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
