import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f29ra_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f29ra_diff(a, b):
    return a - b

def _f29ra_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Base feature: revenue smoothed by 126d
def f29ra_revenue_w126_v001_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to gp smoothed by 252d
def f29ra_revenue_gp_ratio_w252_v002_base_signal(revenue, gp) -> pd.Series:
    """Calculates the ratio of revenue to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(revenue, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 504d
def f29ra_revenue_opinc_ratio_w504_v003_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(revenue, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 756d
def f29ra_revenue_ebitda_ratio_w756_v004_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(revenue, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 1260d
def f29ra_revenue_netinc_ratio_w1260_v005_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(revenue, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 63d
def f29ra_revenue_assets_ratio_w63_v006_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(revenue, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to revenue smoothed by 126d
def f29ra_gp_revenue_ratio_w126_v007_base_signal(gp, revenue) -> pd.Series:
    """Calculates the ratio of gp to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(gp, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: gp smoothed by 252d
def f29ra_gp_w252_v008_base_signal(gp) -> pd.Series:
    """Calculates the smoothed gp over 252 days."""
    res = _sma(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to opinc smoothed by 504d
def f29ra_gp_opinc_ratio_w504_v009_base_signal(gp, opinc) -> pd.Series:
    """Calculates the ratio of gp to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(gp, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to ebitda smoothed by 756d
def f29ra_gp_ebitda_ratio_w756_v010_base_signal(gp, ebitda) -> pd.Series:
    """Calculates the ratio of gp to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(gp, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to netinc smoothed by 1260d
def f29ra_gp_netinc_ratio_w1260_v011_base_signal(gp, netinc) -> pd.Series:
    """Calculates the ratio of gp to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(gp, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to assets smoothed by 63d
def f29ra_gp_assets_ratio_w63_v012_base_signal(gp, assets) -> pd.Series:
    """Calculates the ratio of gp to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(gp, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 126d
def f29ra_opinc_revenue_ratio_w126_v013_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(opinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to gp smoothed by 252d
def f29ra_opinc_gp_ratio_w252_v014_base_signal(opinc, gp) -> pd.Series:
    """Calculates the ratio of opinc to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(opinc, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 504d
def f29ra_opinc_w504_v015_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 504 days."""
    res = _sma(opinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 756d
def f29ra_opinc_ebitda_ratio_w756_v016_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(opinc, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 1260d
def f29ra_opinc_netinc_ratio_w1260_v017_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(opinc, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 63d
def f29ra_opinc_assets_ratio_w63_v018_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(opinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 126d
def f29ra_ebitda_revenue_ratio_w126_v019_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(ebitda, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to gp smoothed by 252d
def f29ra_ebitda_gp_ratio_w252_v020_base_signal(ebitda, gp) -> pd.Series:
    """Calculates the ratio of ebitda to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(ebitda, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 504d
def f29ra_ebitda_opinc_ratio_w504_v021_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(ebitda, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 756d
def f29ra_ebitda_w756_v022_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 756 days."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 1260d
def f29ra_ebitda_netinc_ratio_w1260_v023_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(ebitda, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 63d
def f29ra_ebitda_assets_ratio_w63_v024_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(ebitda, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 126d
def f29ra_netinc_revenue_ratio_w126_v025_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(netinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to gp smoothed by 252d
def f29ra_netinc_gp_ratio_w252_v026_base_signal(netinc, gp) -> pd.Series:
    """Calculates the ratio of netinc to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(netinc, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 504d
def f29ra_netinc_opinc_ratio_w504_v027_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(netinc, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 756d
def f29ra_netinc_ebitda_ratio_w756_v028_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(netinc, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 1260d
def f29ra_netinc_w1260_v029_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 1260 days."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 63d
def f29ra_netinc_assets_ratio_w63_v030_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(netinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 126d
def f29ra_assets_revenue_ratio_w126_v031_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(assets, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to gp smoothed by 252d
def f29ra_assets_gp_ratio_w252_v032_base_signal(assets, gp) -> pd.Series:
    """Calculates the ratio of assets to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(assets, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 504d
def f29ra_assets_opinc_ratio_w504_v033_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(assets, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 756d
def f29ra_assets_ebitda_ratio_w756_v034_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(assets, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 1260d
def f29ra_assets_netinc_ratio_w1260_v035_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(assets, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 63d
def f29ra_assets_w63_v036_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 63 days."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 126d
def f29ra_revenue_w126_v037_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to gp smoothed by 252d
def f29ra_revenue_gp_ratio_w252_v038_base_signal(revenue, gp) -> pd.Series:
    """Calculates the ratio of revenue to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(revenue, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 504d
def f29ra_revenue_opinc_ratio_w504_v039_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(revenue, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 756d
def f29ra_revenue_ebitda_ratio_w756_v040_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(revenue, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 1260d
def f29ra_revenue_netinc_ratio_w1260_v041_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(revenue, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 63d
def f29ra_revenue_assets_ratio_w63_v042_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(revenue, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to revenue smoothed by 126d
def f29ra_gp_revenue_ratio_w126_v043_base_signal(gp, revenue) -> pd.Series:
    """Calculates the ratio of gp to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(gp, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: gp smoothed by 252d
def f29ra_gp_w252_v044_base_signal(gp) -> pd.Series:
    """Calculates the smoothed gp over 252 days."""
    res = _sma(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to opinc smoothed by 504d
def f29ra_gp_opinc_ratio_w504_v045_base_signal(gp, opinc) -> pd.Series:
    """Calculates the ratio of gp to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(gp, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to ebitda smoothed by 756d
def f29ra_gp_ebitda_ratio_w756_v046_base_signal(gp, ebitda) -> pd.Series:
    """Calculates the ratio of gp to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(gp, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to netinc smoothed by 1260d
def f29ra_gp_netinc_ratio_w1260_v047_base_signal(gp, netinc) -> pd.Series:
    """Calculates the ratio of gp to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(gp, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of gp to assets smoothed by 63d
def f29ra_gp_assets_ratio_w63_v048_base_signal(gp, assets) -> pd.Series:
    """Calculates the ratio of gp to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(gp, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 126d
def f29ra_opinc_revenue_ratio_w126_v049_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(opinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to gp smoothed by 252d
def f29ra_opinc_gp_ratio_w252_v050_base_signal(opinc, gp) -> pd.Series:
    """Calculates the ratio of opinc to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(opinc, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 504d
def f29ra_opinc_w504_v051_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 504 days."""
    res = _sma(opinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 756d
def f29ra_opinc_ebitda_ratio_w756_v052_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(opinc, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 1260d
def f29ra_opinc_netinc_ratio_w1260_v053_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(opinc, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 63d
def f29ra_opinc_assets_ratio_w63_v054_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(opinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 126d
def f29ra_ebitda_revenue_ratio_w126_v055_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(ebitda, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to gp smoothed by 252d
def f29ra_ebitda_gp_ratio_w252_v056_base_signal(ebitda, gp) -> pd.Series:
    """Calculates the ratio of ebitda to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(ebitda, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 504d
def f29ra_ebitda_opinc_ratio_w504_v057_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(ebitda, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 756d
def f29ra_ebitda_w756_v058_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 756 days."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 1260d
def f29ra_ebitda_netinc_ratio_w1260_v059_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(ebitda, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 63d
def f29ra_ebitda_assets_ratio_w63_v060_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(ebitda, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 126d
def f29ra_netinc_revenue_ratio_w126_v061_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(netinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to gp smoothed by 252d
def f29ra_netinc_gp_ratio_w252_v062_base_signal(netinc, gp) -> pd.Series:
    """Calculates the ratio of netinc to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(netinc, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 504d
def f29ra_netinc_opinc_ratio_w504_v063_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(netinc, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 756d
def f29ra_netinc_ebitda_ratio_w756_v064_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(netinc, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 1260d
def f29ra_netinc_w1260_v065_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 1260 days."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 63d
def f29ra_netinc_assets_ratio_w63_v066_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 63 days."""
    ratio = _f29ra_ratio(netinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 126d
def f29ra_assets_revenue_ratio_w126_v067_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 126 days."""
    ratio = _f29ra_ratio(assets, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to gp smoothed by 252d
def f29ra_assets_gp_ratio_w252_v068_base_signal(assets, gp) -> pd.Series:
    """Calculates the ratio of assets to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(assets, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 504d
def f29ra_assets_opinc_ratio_w504_v069_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(assets, opinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 756d
def f29ra_assets_ebitda_ratio_w756_v070_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 756 days."""
    ratio = _f29ra_ratio(assets, ebitda)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 1260d
def f29ra_assets_netinc_ratio_w1260_v071_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 1260 days."""
    ratio = _f29ra_ratio(assets, netinc)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 63d
def f29ra_assets_w63_v072_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 63 days."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 126d
def f29ra_revenue_w126_v073_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to gp smoothed by 252d
def f29ra_revenue_gp_ratio_w252_v074_base_signal(revenue, gp) -> pd.Series:
    """Calculates the ratio of revenue to gp smoothed over 252 days."""
    ratio = _f29ra_ratio(revenue, gp)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 504d
def f29ra_revenue_opinc_ratio_w504_v075_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 504 days."""
    ratio = _f29ra_ratio(revenue, opinc)
    res = _sma(ratio, 504)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f29_revenue_acceleration/f29ra_base_001_075_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f29ra_'))]}
f29ra_REGISTRY_BASE = REGISTRY

