import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f29ra_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f29ra_diff(a, b):
    return a - b

def _f29ra_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _f29ra_jerk(s, jw):
    return s.diff(jw)

def _f29ra_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Jerk feature: revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_revenue_w126_sw63_jw21_v001_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_revenue_gp_ratio_w252_sw21_jw5_v002_jerk_signal(revenue, gp) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to gp smoothed."""
    ratio = _f29ra_ratio(revenue, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_revenue_opinc_ratio_w63_sw63_jw21_v003_jerk_signal(revenue, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to opinc smoothed."""
    ratio = _f29ra_ratio(revenue, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_revenue_ebitda_ratio_w126_sw21_jw5_v004_jerk_signal(revenue, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to ebitda smoothed."""
    ratio = _f29ra_ratio(revenue, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_revenue_netinc_ratio_w252_sw63_jw21_v005_jerk_signal(revenue, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to netinc smoothed."""
    ratio = _f29ra_ratio(revenue, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_revenue_assets_ratio_w63_sw21_jw5_v006_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f29ra_ratio(revenue, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_gp_revenue_ratio_w126_sw63_jw21_v007_jerk_signal(gp, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of gp to revenue smoothed."""
    ratio = _f29ra_ratio(gp, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_gp_w252_sw21_jw5_v008_jerk_signal(gp) -> pd.Series:
    """Calculates the jerk of smoothed gp."""
    base = _sma(gp, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_gp_opinc_ratio_w63_sw63_jw21_v009_jerk_signal(gp, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to opinc smoothed."""
    ratio = _f29ra_ratio(gp, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_gp_ebitda_ratio_w126_sw21_jw5_v010_jerk_signal(gp, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of gp to ebitda smoothed."""
    ratio = _f29ra_ratio(gp, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_gp_netinc_ratio_w252_sw63_jw21_v011_jerk_signal(gp, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to netinc smoothed."""
    ratio = _f29ra_ratio(gp, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_gp_assets_ratio_w63_sw21_jw5_v012_jerk_signal(gp, assets) -> pd.Series:
    """Calculates the jerk of the ratio of gp to assets smoothed."""
    ratio = _f29ra_ratio(gp, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_opinc_revenue_ratio_w126_sw63_jw21_v013_jerk_signal(opinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to revenue smoothed."""
    ratio = _f29ra_ratio(opinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_opinc_gp_ratio_w252_sw21_jw5_v014_jerk_signal(opinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to gp smoothed."""
    ratio = _f29ra_ratio(opinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_opinc_w63_sw63_jw21_v015_jerk_signal(opinc) -> pd.Series:
    """Calculates the jerk of smoothed opinc."""
    base = _sma(opinc, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_opinc_ebitda_ratio_w126_sw21_jw5_v016_jerk_signal(opinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to ebitda smoothed."""
    ratio = _f29ra_ratio(opinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_opinc_netinc_ratio_w252_sw63_jw21_v017_jerk_signal(opinc, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to netinc smoothed."""
    ratio = _f29ra_ratio(opinc, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_opinc_assets_ratio_w63_sw21_jw5_v018_jerk_signal(opinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to assets smoothed."""
    ratio = _f29ra_ratio(opinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_ebitda_revenue_ratio_w126_sw63_jw21_v019_jerk_signal(ebitda, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to revenue smoothed."""
    ratio = _f29ra_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_ebitda_gp_ratio_w252_sw21_jw5_v020_jerk_signal(ebitda, gp) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to gp smoothed."""
    ratio = _f29ra_ratio(ebitda, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_ebitda_opinc_ratio_w63_sw63_jw21_v021_jerk_signal(ebitda, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to opinc smoothed."""
    ratio = _f29ra_ratio(ebitda, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_ebitda_w126_sw21_jw5_v022_jerk_signal(ebitda) -> pd.Series:
    """Calculates the jerk of smoothed ebitda."""
    base = _sma(ebitda, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_ebitda_netinc_ratio_w252_sw63_jw21_v023_jerk_signal(ebitda, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to netinc smoothed."""
    ratio = _f29ra_ratio(ebitda, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_ebitda_assets_ratio_w63_sw21_jw5_v024_jerk_signal(ebitda, assets) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to assets smoothed."""
    ratio = _f29ra_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_netinc_revenue_ratio_w126_sw63_jw21_v025_jerk_signal(netinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to revenue smoothed."""
    ratio = _f29ra_ratio(netinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_netinc_gp_ratio_w252_sw21_jw5_v026_jerk_signal(netinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to gp smoothed."""
    ratio = _f29ra_ratio(netinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_netinc_opinc_ratio_w63_sw63_jw21_v027_jerk_signal(netinc, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to opinc smoothed."""
    ratio = _f29ra_ratio(netinc, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_netinc_ebitda_ratio_w126_sw21_jw5_v028_jerk_signal(netinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to ebitda smoothed."""
    ratio = _f29ra_ratio(netinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_netinc_w252_sw63_jw21_v029_jerk_signal(netinc) -> pd.Series:
    """Calculates the jerk of smoothed netinc."""
    base = _sma(netinc, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_netinc_assets_ratio_w63_sw21_jw5_v030_jerk_signal(netinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to assets smoothed."""
    ratio = _f29ra_ratio(netinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_assets_revenue_ratio_w126_sw63_jw21_v031_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f29ra_ratio(assets, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_assets_gp_ratio_w252_sw21_jw5_v032_jerk_signal(assets, gp) -> pd.Series:
    """Calculates the jerk of the ratio of assets to gp smoothed."""
    ratio = _f29ra_ratio(assets, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_assets_opinc_ratio_w63_sw63_jw21_v033_jerk_signal(assets, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to opinc smoothed."""
    ratio = _f29ra_ratio(assets, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_assets_ebitda_ratio_w126_sw21_jw5_v034_jerk_signal(assets, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of assets to ebitda smoothed."""
    ratio = _f29ra_ratio(assets, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_assets_netinc_ratio_w252_sw63_jw21_v035_jerk_signal(assets, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to netinc smoothed."""
    ratio = _f29ra_ratio(assets, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_assets_w63_sw21_jw5_v036_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_revenue_w126_sw63_jw21_v037_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_revenue_gp_ratio_w252_sw21_jw5_v038_jerk_signal(revenue, gp) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to gp smoothed."""
    ratio = _f29ra_ratio(revenue, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_revenue_opinc_ratio_w63_sw63_jw21_v039_jerk_signal(revenue, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to opinc smoothed."""
    ratio = _f29ra_ratio(revenue, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_revenue_ebitda_ratio_w126_sw21_jw5_v040_jerk_signal(revenue, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to ebitda smoothed."""
    ratio = _f29ra_ratio(revenue, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_revenue_netinc_ratio_w252_sw63_jw21_v041_jerk_signal(revenue, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to netinc smoothed."""
    ratio = _f29ra_ratio(revenue, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_revenue_assets_ratio_w63_sw21_jw5_v042_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f29ra_ratio(revenue, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_gp_revenue_ratio_w126_sw63_jw21_v043_jerk_signal(gp, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of gp to revenue smoothed."""
    ratio = _f29ra_ratio(gp, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_gp_w252_sw21_jw5_v044_jerk_signal(gp) -> pd.Series:
    """Calculates the jerk of smoothed gp."""
    base = _sma(gp, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_gp_opinc_ratio_w63_sw63_jw21_v045_jerk_signal(gp, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to opinc smoothed."""
    ratio = _f29ra_ratio(gp, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_gp_ebitda_ratio_w126_sw21_jw5_v046_jerk_signal(gp, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of gp to ebitda smoothed."""
    ratio = _f29ra_ratio(gp, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_gp_netinc_ratio_w252_sw63_jw21_v047_jerk_signal(gp, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to netinc smoothed."""
    ratio = _f29ra_ratio(gp, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_gp_assets_ratio_w63_sw21_jw5_v048_jerk_signal(gp, assets) -> pd.Series:
    """Calculates the jerk of the ratio of gp to assets smoothed."""
    ratio = _f29ra_ratio(gp, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_opinc_revenue_ratio_w126_sw63_jw21_v049_jerk_signal(opinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to revenue smoothed."""
    ratio = _f29ra_ratio(opinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_opinc_gp_ratio_w252_sw21_jw5_v050_jerk_signal(opinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to gp smoothed."""
    ratio = _f29ra_ratio(opinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_opinc_w63_sw63_jw21_v051_jerk_signal(opinc) -> pd.Series:
    """Calculates the jerk of smoothed opinc."""
    base = _sma(opinc, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_opinc_ebitda_ratio_w126_sw21_jw5_v052_jerk_signal(opinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to ebitda smoothed."""
    ratio = _f29ra_ratio(opinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_opinc_netinc_ratio_w252_sw63_jw21_v053_jerk_signal(opinc, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to netinc smoothed."""
    ratio = _f29ra_ratio(opinc, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_opinc_assets_ratio_w63_sw21_jw5_v054_jerk_signal(opinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to assets smoothed."""
    ratio = _f29ra_ratio(opinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_ebitda_revenue_ratio_w126_sw63_jw21_v055_jerk_signal(ebitda, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to revenue smoothed."""
    ratio = _f29ra_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_ebitda_gp_ratio_w252_sw21_jw5_v056_jerk_signal(ebitda, gp) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to gp smoothed."""
    ratio = _f29ra_ratio(ebitda, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_ebitda_opinc_ratio_w63_sw63_jw21_v057_jerk_signal(ebitda, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to opinc smoothed."""
    ratio = _f29ra_ratio(ebitda, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_ebitda_w126_sw21_jw5_v058_jerk_signal(ebitda) -> pd.Series:
    """Calculates the jerk of smoothed ebitda."""
    base = _sma(ebitda, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_ebitda_netinc_ratio_w252_sw63_jw21_v059_jerk_signal(ebitda, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to netinc smoothed."""
    ratio = _f29ra_ratio(ebitda, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_ebitda_assets_ratio_w63_sw21_jw5_v060_jerk_signal(ebitda, assets) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to assets smoothed."""
    ratio = _f29ra_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_netinc_revenue_ratio_w126_sw63_jw21_v061_jerk_signal(netinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to revenue smoothed."""
    ratio = _f29ra_ratio(netinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_netinc_gp_ratio_w252_sw21_jw5_v062_jerk_signal(netinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to gp smoothed."""
    ratio = _f29ra_ratio(netinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_netinc_opinc_ratio_w63_sw63_jw21_v063_jerk_signal(netinc, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to opinc smoothed."""
    ratio = _f29ra_ratio(netinc, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_netinc_ebitda_ratio_w126_sw21_jw5_v064_jerk_signal(netinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to ebitda smoothed."""
    ratio = _f29ra_ratio(netinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_netinc_w252_sw63_jw21_v065_jerk_signal(netinc) -> pd.Series:
    """Calculates the jerk of smoothed netinc."""
    base = _sma(netinc, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_netinc_assets_ratio_w63_sw21_jw5_v066_jerk_signal(netinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to assets smoothed."""
    ratio = _f29ra_ratio(netinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_assets_revenue_ratio_w126_sw63_jw21_v067_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f29ra_ratio(assets, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_assets_gp_ratio_w252_sw21_jw5_v068_jerk_signal(assets, gp) -> pd.Series:
    """Calculates the jerk of the ratio of assets to gp smoothed."""
    ratio = _f29ra_ratio(assets, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_assets_opinc_ratio_w63_sw63_jw21_v069_jerk_signal(assets, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to opinc smoothed."""
    ratio = _f29ra_ratio(assets, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_assets_ebitda_ratio_w126_sw21_jw5_v070_jerk_signal(assets, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of assets to ebitda smoothed."""
    ratio = _f29ra_ratio(assets, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_assets_netinc_ratio_w252_sw63_jw21_v071_jerk_signal(assets, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to netinc smoothed."""
    ratio = _f29ra_ratio(assets, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_assets_w63_sw21_jw5_v072_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_revenue_w126_sw63_jw21_v073_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_revenue_gp_ratio_w252_sw21_jw5_v074_jerk_signal(revenue, gp) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to gp smoothed."""
    ratio = _f29ra_ratio(revenue, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_revenue_opinc_ratio_w63_sw63_jw21_v075_jerk_signal(revenue, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to opinc smoothed."""
    ratio = _f29ra_ratio(revenue, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_revenue_ebitda_ratio_w126_sw21_jw5_v076_jerk_signal(revenue, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to ebitda smoothed."""
    ratio = _f29ra_ratio(revenue, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_revenue_netinc_ratio_w252_sw63_jw21_v077_jerk_signal(revenue, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to netinc smoothed."""
    ratio = _f29ra_ratio(revenue, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_revenue_assets_ratio_w63_sw21_jw5_v078_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f29ra_ratio(revenue, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_gp_revenue_ratio_w126_sw63_jw21_v079_jerk_signal(gp, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of gp to revenue smoothed."""
    ratio = _f29ra_ratio(gp, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_gp_w252_sw21_jw5_v080_jerk_signal(gp) -> pd.Series:
    """Calculates the jerk of smoothed gp."""
    base = _sma(gp, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_gp_opinc_ratio_w63_sw63_jw21_v081_jerk_signal(gp, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to opinc smoothed."""
    ratio = _f29ra_ratio(gp, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_gp_ebitda_ratio_w126_sw21_jw5_v082_jerk_signal(gp, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of gp to ebitda smoothed."""
    ratio = _f29ra_ratio(gp, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_gp_netinc_ratio_w252_sw63_jw21_v083_jerk_signal(gp, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to netinc smoothed."""
    ratio = _f29ra_ratio(gp, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_gp_assets_ratio_w63_sw21_jw5_v084_jerk_signal(gp, assets) -> pd.Series:
    """Calculates the jerk of the ratio of gp to assets smoothed."""
    ratio = _f29ra_ratio(gp, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_opinc_revenue_ratio_w126_sw63_jw21_v085_jerk_signal(opinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to revenue smoothed."""
    ratio = _f29ra_ratio(opinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_opinc_gp_ratio_w252_sw21_jw5_v086_jerk_signal(opinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to gp smoothed."""
    ratio = _f29ra_ratio(opinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_opinc_w63_sw63_jw21_v087_jerk_signal(opinc) -> pd.Series:
    """Calculates the jerk of smoothed opinc."""
    base = _sma(opinc, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_opinc_ebitda_ratio_w126_sw21_jw5_v088_jerk_signal(opinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to ebitda smoothed."""
    ratio = _f29ra_ratio(opinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_opinc_netinc_ratio_w252_sw63_jw21_v089_jerk_signal(opinc, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to netinc smoothed."""
    ratio = _f29ra_ratio(opinc, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_opinc_assets_ratio_w63_sw21_jw5_v090_jerk_signal(opinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to assets smoothed."""
    ratio = _f29ra_ratio(opinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_ebitda_revenue_ratio_w126_sw63_jw21_v091_jerk_signal(ebitda, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to revenue smoothed."""
    ratio = _f29ra_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_ebitda_gp_ratio_w252_sw21_jw5_v092_jerk_signal(ebitda, gp) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to gp smoothed."""
    ratio = _f29ra_ratio(ebitda, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_ebitda_opinc_ratio_w63_sw63_jw21_v093_jerk_signal(ebitda, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to opinc smoothed."""
    ratio = _f29ra_ratio(ebitda, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_ebitda_w126_sw21_jw5_v094_jerk_signal(ebitda) -> pd.Series:
    """Calculates the jerk of smoothed ebitda."""
    base = _sma(ebitda, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_ebitda_netinc_ratio_w252_sw63_jw21_v095_jerk_signal(ebitda, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to netinc smoothed."""
    ratio = _f29ra_ratio(ebitda, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_ebitda_assets_ratio_w63_sw21_jw5_v096_jerk_signal(ebitda, assets) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to assets smoothed."""
    ratio = _f29ra_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_netinc_revenue_ratio_w126_sw63_jw21_v097_jerk_signal(netinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to revenue smoothed."""
    ratio = _f29ra_ratio(netinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_netinc_gp_ratio_w252_sw21_jw5_v098_jerk_signal(netinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to gp smoothed."""
    ratio = _f29ra_ratio(netinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_netinc_opinc_ratio_w63_sw63_jw21_v099_jerk_signal(netinc, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to opinc smoothed."""
    ratio = _f29ra_ratio(netinc, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_netinc_ebitda_ratio_w126_sw21_jw5_v100_jerk_signal(netinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to ebitda smoothed."""
    ratio = _f29ra_ratio(netinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_netinc_w252_sw63_jw21_v101_jerk_signal(netinc) -> pd.Series:
    """Calculates the jerk of smoothed netinc."""
    base = _sma(netinc, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_netinc_assets_ratio_w63_sw21_jw5_v102_jerk_signal(netinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to assets smoothed."""
    ratio = _f29ra_ratio(netinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_assets_revenue_ratio_w126_sw63_jw21_v103_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f29ra_ratio(assets, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_assets_gp_ratio_w252_sw21_jw5_v104_jerk_signal(assets, gp) -> pd.Series:
    """Calculates the jerk of the ratio of assets to gp smoothed."""
    ratio = _f29ra_ratio(assets, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_assets_opinc_ratio_w63_sw63_jw21_v105_jerk_signal(assets, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to opinc smoothed."""
    ratio = _f29ra_ratio(assets, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_assets_ebitda_ratio_w126_sw21_jw5_v106_jerk_signal(assets, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of assets to ebitda smoothed."""
    ratio = _f29ra_ratio(assets, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_assets_netinc_ratio_w252_sw63_jw21_v107_jerk_signal(assets, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to netinc smoothed."""
    ratio = _f29ra_ratio(assets, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_assets_w63_sw21_jw5_v108_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_revenue_w126_sw63_jw21_v109_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_revenue_gp_ratio_w252_sw21_jw5_v110_jerk_signal(revenue, gp) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to gp smoothed."""
    ratio = _f29ra_ratio(revenue, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_revenue_opinc_ratio_w63_sw63_jw21_v111_jerk_signal(revenue, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to opinc smoothed."""
    ratio = _f29ra_ratio(revenue, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_revenue_ebitda_ratio_w126_sw21_jw5_v112_jerk_signal(revenue, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to ebitda smoothed."""
    ratio = _f29ra_ratio(revenue, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_revenue_netinc_ratio_w252_sw63_jw21_v113_jerk_signal(revenue, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to netinc smoothed."""
    ratio = _f29ra_ratio(revenue, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_revenue_assets_ratio_w63_sw21_jw5_v114_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f29ra_ratio(revenue, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_gp_revenue_ratio_w126_sw63_jw21_v115_jerk_signal(gp, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of gp to revenue smoothed."""
    ratio = _f29ra_ratio(gp, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_gp_w252_sw21_jw5_v116_jerk_signal(gp) -> pd.Series:
    """Calculates the jerk of smoothed gp."""
    base = _sma(gp, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_gp_opinc_ratio_w63_sw63_jw21_v117_jerk_signal(gp, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to opinc smoothed."""
    ratio = _f29ra_ratio(gp, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_gp_ebitda_ratio_w126_sw21_jw5_v118_jerk_signal(gp, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of gp to ebitda smoothed."""
    ratio = _f29ra_ratio(gp, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_gp_netinc_ratio_w252_sw63_jw21_v119_jerk_signal(gp, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of gp to netinc smoothed."""
    ratio = _f29ra_ratio(gp, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of gp to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_gp_assets_ratio_w63_sw21_jw5_v120_jerk_signal(gp, assets) -> pd.Series:
    """Calculates the jerk of the ratio of gp to assets smoothed."""
    ratio = _f29ra_ratio(gp, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_opinc_revenue_ratio_w126_sw63_jw21_v121_jerk_signal(opinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to revenue smoothed."""
    ratio = _f29ra_ratio(opinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_opinc_gp_ratio_w252_sw21_jw5_v122_jerk_signal(opinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to gp smoothed."""
    ratio = _f29ra_ratio(opinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_opinc_w63_sw63_jw21_v123_jerk_signal(opinc) -> pd.Series:
    """Calculates the jerk of smoothed opinc."""
    base = _sma(opinc, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_opinc_ebitda_ratio_w126_sw21_jw5_v124_jerk_signal(opinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to ebitda smoothed."""
    ratio = _f29ra_ratio(opinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_opinc_netinc_ratio_w252_sw63_jw21_v125_jerk_signal(opinc, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to netinc smoothed."""
    ratio = _f29ra_ratio(opinc, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of opinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_opinc_assets_ratio_w63_sw21_jw5_v126_jerk_signal(opinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of opinc to assets smoothed."""
    ratio = _f29ra_ratio(opinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_ebitda_revenue_ratio_w126_sw63_jw21_v127_jerk_signal(ebitda, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to revenue smoothed."""
    ratio = _f29ra_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_ebitda_gp_ratio_w252_sw21_jw5_v128_jerk_signal(ebitda, gp) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to gp smoothed."""
    ratio = _f29ra_ratio(ebitda, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_ebitda_opinc_ratio_w63_sw63_jw21_v129_jerk_signal(ebitda, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to opinc smoothed."""
    ratio = _f29ra_ratio(ebitda, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_ebitda_w126_sw21_jw5_v130_jerk_signal(ebitda) -> pd.Series:
    """Calculates the jerk of smoothed ebitda."""
    base = _sma(ebitda, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_ebitda_netinc_ratio_w252_sw63_jw21_v131_jerk_signal(ebitda, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to netinc smoothed."""
    ratio = _f29ra_ratio(ebitda, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of ebitda to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_ebitda_assets_ratio_w63_sw21_jw5_v132_jerk_signal(ebitda, assets) -> pd.Series:
    """Calculates the jerk of the ratio of ebitda to assets smoothed."""
    ratio = _f29ra_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_netinc_revenue_ratio_w126_sw63_jw21_v133_jerk_signal(netinc, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to revenue smoothed."""
    ratio = _f29ra_ratio(netinc, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_netinc_gp_ratio_w252_sw21_jw5_v134_jerk_signal(netinc, gp) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to gp smoothed."""
    ratio = _f29ra_ratio(netinc, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_netinc_opinc_ratio_w63_sw63_jw21_v135_jerk_signal(netinc, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to opinc smoothed."""
    ratio = _f29ra_ratio(netinc, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_netinc_ebitda_ratio_w126_sw21_jw5_v136_jerk_signal(netinc, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to ebitda smoothed."""
    ratio = _f29ra_ratio(netinc, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_netinc_w252_sw63_jw21_v137_jerk_signal(netinc) -> pd.Series:
    """Calculates the jerk of smoothed netinc."""
    base = _sma(netinc, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of netinc to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_netinc_assets_ratio_w63_sw21_jw5_v138_jerk_signal(netinc, assets) -> pd.Series:
    """Calculates the jerk of the ratio of netinc to assets smoothed."""
    ratio = _f29ra_ratio(netinc, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_assets_revenue_ratio_w126_sw63_jw21_v139_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f29ra_ratio(assets, revenue)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_assets_gp_ratio_w252_sw21_jw5_v140_jerk_signal(assets, gp) -> pd.Series:
    """Calculates the jerk of the ratio of assets to gp smoothed."""
    ratio = _f29ra_ratio(assets, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_assets_opinc_ratio_w63_sw63_jw21_v141_jerk_signal(assets, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to opinc smoothed."""
    ratio = _f29ra_ratio(assets, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_assets_ebitda_ratio_w126_sw21_jw5_v142_jerk_signal(assets, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of assets to ebitda smoothed."""
    ratio = _f29ra_ratio(assets, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_assets_netinc_ratio_w252_sw63_jw21_v143_jerk_signal(assets, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of assets to netinc smoothed."""
    ratio = _f29ra_ratio(assets, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_assets_w63_sw21_jw5_v144_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 126d, slope 63d, jerk 21d
def f29ra_revenue_w126_sw63_jw21_v145_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 126)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to gp smoothed by 252d, slope 21d, jerk 5d
def f29ra_revenue_gp_ratio_w252_sw21_jw5_v146_jerk_signal(revenue, gp) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to gp smoothed."""
    ratio = _f29ra_ratio(revenue, gp)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to opinc smoothed by 63d, slope 63d, jerk 21d
def f29ra_revenue_opinc_ratio_w63_sw63_jw21_v147_jerk_signal(revenue, opinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to opinc smoothed."""
    ratio = _f29ra_ratio(revenue, opinc)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to ebitda smoothed by 126d, slope 21d, jerk 5d
def f29ra_revenue_ebitda_ratio_w126_sw21_jw5_v148_jerk_signal(revenue, ebitda) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to ebitda smoothed."""
    ratio = _f29ra_ratio(revenue, ebitda)
    base = _sma(ratio, 126)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to netinc smoothed by 252d, slope 63d, jerk 21d
def f29ra_revenue_netinc_ratio_w252_sw63_jw21_v149_jerk_signal(revenue, netinc) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to netinc smoothed."""
    ratio = _f29ra_ratio(revenue, netinc)
    base = _sma(ratio, 252)
    slope = _f29ra_slope(base, 63)
    res = _f29ra_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 63d, slope 21d, jerk 5d
def f29ra_revenue_assets_ratio_w63_sw21_jw5_v150_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f29ra_ratio(revenue, assets)
    base = _sma(ratio, 63)
    slope = _f29ra_slope(base, 21)
    res = _f29ra_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.random.normal(100, 20, n) for col in ['revenue', 'gp', 'opinc', 'ebitda', 'netinc', 'assets']})
    for col in ['revenue', 'gp', 'opinc', 'ebitda', 'netinc', 'assets']:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f29ra_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f29_revenue_acceleration/f29ra_jerk_001_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f29ra_'))]}
f29ra_REGISTRY_JERK = REGISTRY

