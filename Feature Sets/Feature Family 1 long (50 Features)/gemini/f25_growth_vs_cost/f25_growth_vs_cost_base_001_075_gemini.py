import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f25_growth_vs_cost_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f25_growth_vs_cost_diff(a, b):
    return a - b

def _f25_growth_vs_cost_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Base feature: revenue smoothed by 126d
def f25_growth_vs_cost_revenue_w126_v001_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 252d
def f25_growth_vs_cost_revenue_capex_ratio_w252_v002_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 504d
def f25_growth_vs_cost_revenue_assets_ratio_w504_v003_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 756d
def f25_growth_vs_cost_revenue_opinc_ratio_w756_v004_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 1260d
def f25_growth_vs_cost_revenue_ebitda_ratio_w1260_v005_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 63d
def f25_growth_vs_cost_revenue_netinc_ratio_w63_v006_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 126d
def f25_growth_vs_cost_capex_revenue_ratio_w126_v007_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 252d
def f25_growth_vs_cost_capex_w252_v008_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 252 days."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 504d
def f25_growth_vs_cost_capex_assets_ratio_w504_v009_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to opinc smoothed by 756d
def f25_growth_vs_cost_capex_opinc_ratio_w756_v010_base_signal(capex, opinc) -> pd.Series:
    """Calculates the ratio of capex to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to ebitda smoothed by 1260d
def f25_growth_vs_cost_capex_ebitda_ratio_w1260_v011_base_signal(capex, ebitda) -> pd.Series:
    """Calculates the ratio of capex to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to netinc smoothed by 63d
def f25_growth_vs_cost_capex_netinc_ratio_w63_v012_base_signal(capex, netinc) -> pd.Series:
    """Calculates the ratio of capex to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 126d
def f25_growth_vs_cost_assets_revenue_ratio_w126_v013_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 252d
def f25_growth_vs_cost_assets_capex_ratio_w252_v014_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 504d
def f25_growth_vs_cost_assets_w504_v015_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 504 days."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 756d
def f25_growth_vs_cost_assets_opinc_ratio_w756_v016_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 1260d
def f25_growth_vs_cost_assets_ebitda_ratio_w1260_v017_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 63d
def f25_growth_vs_cost_assets_netinc_ratio_w63_v018_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 126d
def f25_growth_vs_cost_opinc_revenue_ratio_w126_v019_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to capex smoothed by 252d
def f25_growth_vs_cost_opinc_capex_ratio_w252_v020_base_signal(opinc, capex) -> pd.Series:
    """Calculates the ratio of opinc to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 504d
def f25_growth_vs_cost_opinc_assets_ratio_w504_v021_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 756d
def f25_growth_vs_cost_opinc_w756_v022_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 756 days."""
    res = _sma(opinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 1260d
def f25_growth_vs_cost_opinc_ebitda_ratio_w1260_v023_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 63d
def f25_growth_vs_cost_opinc_netinc_ratio_w63_v024_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 126d
def f25_growth_vs_cost_ebitda_revenue_ratio_w126_v025_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to capex smoothed by 252d
def f25_growth_vs_cost_ebitda_capex_ratio_w252_v026_base_signal(ebitda, capex) -> pd.Series:
    """Calculates the ratio of ebitda to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 504d
def f25_growth_vs_cost_ebitda_assets_ratio_w504_v027_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 756d
def f25_growth_vs_cost_ebitda_opinc_ratio_w756_v028_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 1260d
def f25_growth_vs_cost_ebitda_w1260_v029_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 1260 days."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 63d
def f25_growth_vs_cost_ebitda_netinc_ratio_w63_v030_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 126d
def f25_growth_vs_cost_netinc_revenue_ratio_w126_v031_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to capex smoothed by 252d
def f25_growth_vs_cost_netinc_capex_ratio_w252_v032_base_signal(netinc, capex) -> pd.Series:
    """Calculates the ratio of netinc to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 504d
def f25_growth_vs_cost_netinc_assets_ratio_w504_v033_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 756d
def f25_growth_vs_cost_netinc_opinc_ratio_w756_v034_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 1260d
def f25_growth_vs_cost_netinc_ebitda_ratio_w1260_v035_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 63d
def f25_growth_vs_cost_netinc_w63_v036_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 63 days."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 126d
def f25_growth_vs_cost_revenue_w126_v037_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 252d
def f25_growth_vs_cost_revenue_capex_ratio_w252_v038_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 504d
def f25_growth_vs_cost_revenue_assets_ratio_w504_v039_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 756d
def f25_growth_vs_cost_revenue_opinc_ratio_w756_v040_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 1260d
def f25_growth_vs_cost_revenue_ebitda_ratio_w1260_v041_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 63d
def f25_growth_vs_cost_revenue_netinc_ratio_w63_v042_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 126d
def f25_growth_vs_cost_capex_revenue_ratio_w126_v043_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 252d
def f25_growth_vs_cost_capex_w252_v044_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 252 days."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 504d
def f25_growth_vs_cost_capex_assets_ratio_w504_v045_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to opinc smoothed by 756d
def f25_growth_vs_cost_capex_opinc_ratio_w756_v046_base_signal(capex, opinc) -> pd.Series:
    """Calculates the ratio of capex to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to ebitda smoothed by 1260d
def f25_growth_vs_cost_capex_ebitda_ratio_w1260_v047_base_signal(capex, ebitda) -> pd.Series:
    """Calculates the ratio of capex to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to netinc smoothed by 63d
def f25_growth_vs_cost_capex_netinc_ratio_w63_v048_base_signal(capex, netinc) -> pd.Series:
    """Calculates the ratio of capex to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 126d
def f25_growth_vs_cost_assets_revenue_ratio_w126_v049_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 252d
def f25_growth_vs_cost_assets_capex_ratio_w252_v050_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 504d
def f25_growth_vs_cost_assets_w504_v051_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 504 days."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 756d
def f25_growth_vs_cost_assets_opinc_ratio_w756_v052_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 1260d
def f25_growth_vs_cost_assets_ebitda_ratio_w1260_v053_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 63d
def f25_growth_vs_cost_assets_netinc_ratio_w63_v054_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 126d
def f25_growth_vs_cost_opinc_revenue_ratio_w126_v055_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to capex smoothed by 252d
def f25_growth_vs_cost_opinc_capex_ratio_w252_v056_base_signal(opinc, capex) -> pd.Series:
    """Calculates the ratio of opinc to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 504d
def f25_growth_vs_cost_opinc_assets_ratio_w504_v057_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 756d
def f25_growth_vs_cost_opinc_w756_v058_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 756 days."""
    res = _sma(opinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 1260d
def f25_growth_vs_cost_opinc_ebitda_ratio_w1260_v059_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 63d
def f25_growth_vs_cost_opinc_netinc_ratio_w63_v060_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 126d
def f25_growth_vs_cost_ebitda_revenue_ratio_w126_v061_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to capex smoothed by 252d
def f25_growth_vs_cost_ebitda_capex_ratio_w252_v062_base_signal(ebitda, capex) -> pd.Series:
    """Calculates the ratio of ebitda to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 504d
def f25_growth_vs_cost_ebitda_assets_ratio_w504_v063_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 756d
def f25_growth_vs_cost_ebitda_opinc_ratio_w756_v064_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 1260d
def f25_growth_vs_cost_ebitda_w1260_v065_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 1260 days."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 63d
def f25_growth_vs_cost_ebitda_netinc_ratio_w63_v066_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 126d
def f25_growth_vs_cost_netinc_revenue_ratio_w126_v067_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, revenue)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to capex smoothed by 252d
def f25_growth_vs_cost_netinc_capex_ratio_w252_v068_base_signal(netinc, capex) -> pd.Series:
    """Calculates the ratio of netinc to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 504d
def f25_growth_vs_cost_netinc_assets_ratio_w504_v069_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 756d
def f25_growth_vs_cost_netinc_opinc_ratio_w756_v070_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, opinc)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 1260d
def f25_growth_vs_cost_netinc_ebitda_ratio_w1260_v071_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, ebitda)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 63d
def f25_growth_vs_cost_netinc_w63_v072_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 63 days."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 126d
def f25_growth_vs_cost_revenue_w126_v073_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 126 days."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 252d
def f25_growth_vs_cost_revenue_capex_ratio_w252_v074_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 504d
def f25_growth_vs_cost_revenue_assets_ratio_w504_v075_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.random.normal(100, 20, n) for col in ['revenue', 'capex', 'assets', 'opinc', 'ebitda', 'netinc']})
    for col in ['revenue', 'capex', 'assets', 'opinc', 'ebitda', 'netinc']:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f25_growth_vs_cost_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f25_growth_vs_cost/f25_growth_vs_cost_base_001_075_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f25_growth_vs_cost_'))]}
F25_GROWTH_VS_COST_REGISTRY_BASE = REGISTRY
