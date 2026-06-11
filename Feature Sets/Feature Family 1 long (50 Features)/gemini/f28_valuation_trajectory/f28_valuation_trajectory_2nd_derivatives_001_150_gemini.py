import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f28vt_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f28vt_diff(a, b):
    return a - b

def _f28vt_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _f28vt_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Slope feature: marketcap smoothed by 126d, slope over 21d
def f28vt_marketcap_w126_sw21_v001_slope_signal(marketcap) -> pd.Series:
    """Calculates the slope of smoothed marketcap over 21 days."""
    base = _sma(marketcap, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ev smoothed by 252d, slope over 63d
def f28vt_marketcap_ev_ratio_w252_sw63_v002_slope_signal(marketcap, ev) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to revenue smoothed by 504d, slope over 5d
def f28vt_marketcap_revenue_ratio_w504_sw5_v003_slope_signal(marketcap, revenue) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ebitda smoothed by 63d, slope over 21d
def f28vt_marketcap_ebitda_ratio_w63_sw21_v004_slope_signal(marketcap, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(marketcap, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to netinc smoothed by 126d, slope over 63d
def f28vt_marketcap_netinc_ratio_w126_sw63_v005_slope_signal(marketcap, netinc) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to assets smoothed by 252d, slope over 5d
def f28vt_marketcap_assets_ratio_w252_sw5_v006_slope_signal(marketcap, assets) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to marketcap smoothed by 504d, slope over 21d
def f28vt_ev_marketcap_ratio_w504_sw21_v007_slope_signal(ev, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ev to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ev smoothed by 63d, slope over 63d
def f28vt_ev_w63_sw63_v008_slope_signal(ev) -> pd.Series:
    """Calculates the slope of smoothed ev over 63 days."""
    base = _sma(ev, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to revenue smoothed by 126d, slope over 5d
def f28vt_ev_revenue_ratio_w126_sw5_v009_slope_signal(ev, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ev to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to ebitda smoothed by 252d, slope over 21d
def f28vt_ev_ebitda_ratio_w252_sw21_v010_slope_signal(ev, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of ev to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to netinc smoothed by 504d, slope over 63d
def f28vt_ev_netinc_ratio_w504_sw63_v011_slope_signal(ev, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ev to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ev, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to assets smoothed by 63d, slope over 5d
def f28vt_ev_assets_ratio_w63_sw5_v012_slope_signal(ev, assets) -> pd.Series:
    """Calculates the slope of the ratio of ev to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to marketcap smoothed by 126d, slope over 21d
def f28vt_revenue_marketcap_ratio_w126_sw21_v013_slope_signal(revenue, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of revenue to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ev smoothed by 252d, slope over 63d
def f28vt_revenue_ev_ratio_w252_sw63_v014_slope_signal(revenue, ev) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f28vt_revenue_w504_sw5_v015_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ebitda smoothed by 63d, slope over 21d
def f28vt_revenue_ebitda_ratio_w63_sw21_v016_slope_signal(revenue, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 63d
def f28vt_revenue_netinc_ratio_w126_sw63_v017_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 5d
def f28vt_revenue_assets_ratio_w252_sw5_v018_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to marketcap smoothed by 504d, slope over 21d
def f28vt_ebitda_marketcap_ratio_w504_sw21_v019_slope_signal(ebitda, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ebitda, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to ev smoothed by 63d, slope over 63d
def f28vt_ebitda_ev_ratio_w63_sw63_v020_slope_signal(ebitda, ev) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to revenue smoothed by 126d, slope over 5d
def f28vt_ebitda_revenue_ratio_w126_sw5_v021_slope_signal(ebitda, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ebitda smoothed by 252d, slope over 21d
def f28vt_ebitda_w252_sw21_v022_slope_signal(ebitda) -> pd.Series:
    """Calculates the slope of smoothed ebitda over 21 days."""
    base = _sma(ebitda, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to netinc smoothed by 504d, slope over 63d
def f28vt_ebitda_netinc_ratio_w504_sw63_v023_slope_signal(ebitda, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to assets smoothed by 63d, slope over 5d
def f28vt_ebitda_assets_ratio_w63_sw5_v024_slope_signal(ebitda, assets) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to marketcap smoothed by 126d, slope over 21d
def f28vt_netinc_marketcap_ratio_w126_sw21_v025_slope_signal(netinc, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of netinc to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ev smoothed by 252d, slope over 63d
def f28vt_netinc_ev_ratio_w252_sw63_v026_slope_signal(netinc, ev) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(netinc, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 504d, slope over 5d
def f28vt_netinc_revenue_ratio_w504_sw5_v027_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ebitda smoothed by 63d, slope over 21d
def f28vt_netinc_ebitda_ratio_w63_sw21_v028_slope_signal(netinc, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 126d, slope over 63d
def f28vt_netinc_w126_sw63_v029_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 63 days."""
    base = _sma(netinc, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 252d, slope over 5d
def f28vt_netinc_assets_ratio_w252_sw5_v030_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to marketcap smoothed by 504d, slope over 21d
def f28vt_assets_marketcap_ratio_w504_sw21_v031_slope_signal(assets, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of assets to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ev smoothed by 63d, slope over 63d
def f28vt_assets_ev_ratio_w63_sw63_v032_slope_signal(assets, ev) -> pd.Series:
    """Calculates the slope of the ratio of assets to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f28vt_assets_revenue_ratio_w126_sw5_v033_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ebitda smoothed by 252d, slope over 21d
def f28vt_assets_ebitda_ratio_w252_sw21_v034_slope_signal(assets, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of assets to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 504d, slope over 63d
def f28vt_assets_netinc_ratio_w504_sw63_v035_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 63d, slope over 5d
def f28vt_assets_w63_sw5_v036_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 5 days."""
    base = _sma(assets, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: marketcap smoothed by 126d, slope over 21d
def f28vt_marketcap_w126_sw21_v037_slope_signal(marketcap) -> pd.Series:
    """Calculates the slope of smoothed marketcap over 21 days."""
    base = _sma(marketcap, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ev smoothed by 252d, slope over 63d
def f28vt_marketcap_ev_ratio_w252_sw63_v038_slope_signal(marketcap, ev) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to revenue smoothed by 504d, slope over 5d
def f28vt_marketcap_revenue_ratio_w504_sw5_v039_slope_signal(marketcap, revenue) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ebitda smoothed by 63d, slope over 21d
def f28vt_marketcap_ebitda_ratio_w63_sw21_v040_slope_signal(marketcap, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(marketcap, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to netinc smoothed by 126d, slope over 63d
def f28vt_marketcap_netinc_ratio_w126_sw63_v041_slope_signal(marketcap, netinc) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to assets smoothed by 252d, slope over 5d
def f28vt_marketcap_assets_ratio_w252_sw5_v042_slope_signal(marketcap, assets) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to marketcap smoothed by 504d, slope over 21d
def f28vt_ev_marketcap_ratio_w504_sw21_v043_slope_signal(ev, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ev to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ev smoothed by 63d, slope over 63d
def f28vt_ev_w63_sw63_v044_slope_signal(ev) -> pd.Series:
    """Calculates the slope of smoothed ev over 63 days."""
    base = _sma(ev, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to revenue smoothed by 126d, slope over 5d
def f28vt_ev_revenue_ratio_w126_sw5_v045_slope_signal(ev, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ev to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to ebitda smoothed by 252d, slope over 21d
def f28vt_ev_ebitda_ratio_w252_sw21_v046_slope_signal(ev, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of ev to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to netinc smoothed by 504d, slope over 63d
def f28vt_ev_netinc_ratio_w504_sw63_v047_slope_signal(ev, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ev to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ev, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to assets smoothed by 63d, slope over 5d
def f28vt_ev_assets_ratio_w63_sw5_v048_slope_signal(ev, assets) -> pd.Series:
    """Calculates the slope of the ratio of ev to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to marketcap smoothed by 126d, slope over 21d
def f28vt_revenue_marketcap_ratio_w126_sw21_v049_slope_signal(revenue, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of revenue to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ev smoothed by 252d, slope over 63d
def f28vt_revenue_ev_ratio_w252_sw63_v050_slope_signal(revenue, ev) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f28vt_revenue_w504_sw5_v051_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ebitda smoothed by 63d, slope over 21d
def f28vt_revenue_ebitda_ratio_w63_sw21_v052_slope_signal(revenue, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 63d
def f28vt_revenue_netinc_ratio_w126_sw63_v053_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 5d
def f28vt_revenue_assets_ratio_w252_sw5_v054_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to marketcap smoothed by 504d, slope over 21d
def f28vt_ebitda_marketcap_ratio_w504_sw21_v055_slope_signal(ebitda, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ebitda, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to ev smoothed by 63d, slope over 63d
def f28vt_ebitda_ev_ratio_w63_sw63_v056_slope_signal(ebitda, ev) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to revenue smoothed by 126d, slope over 5d
def f28vt_ebitda_revenue_ratio_w126_sw5_v057_slope_signal(ebitda, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ebitda smoothed by 252d, slope over 21d
def f28vt_ebitda_w252_sw21_v058_slope_signal(ebitda) -> pd.Series:
    """Calculates the slope of smoothed ebitda over 21 days."""
    base = _sma(ebitda, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to netinc smoothed by 504d, slope over 63d
def f28vt_ebitda_netinc_ratio_w504_sw63_v059_slope_signal(ebitda, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to assets smoothed by 63d, slope over 5d
def f28vt_ebitda_assets_ratio_w63_sw5_v060_slope_signal(ebitda, assets) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to marketcap smoothed by 126d, slope over 21d
def f28vt_netinc_marketcap_ratio_w126_sw21_v061_slope_signal(netinc, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of netinc to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ev smoothed by 252d, slope over 63d
def f28vt_netinc_ev_ratio_w252_sw63_v062_slope_signal(netinc, ev) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(netinc, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 504d, slope over 5d
def f28vt_netinc_revenue_ratio_w504_sw5_v063_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ebitda smoothed by 63d, slope over 21d
def f28vt_netinc_ebitda_ratio_w63_sw21_v064_slope_signal(netinc, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 126d, slope over 63d
def f28vt_netinc_w126_sw63_v065_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 63 days."""
    base = _sma(netinc, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 252d, slope over 5d
def f28vt_netinc_assets_ratio_w252_sw5_v066_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to marketcap smoothed by 504d, slope over 21d
def f28vt_assets_marketcap_ratio_w504_sw21_v067_slope_signal(assets, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of assets to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ev smoothed by 63d, slope over 63d
def f28vt_assets_ev_ratio_w63_sw63_v068_slope_signal(assets, ev) -> pd.Series:
    """Calculates the slope of the ratio of assets to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f28vt_assets_revenue_ratio_w126_sw5_v069_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ebitda smoothed by 252d, slope over 21d
def f28vt_assets_ebitda_ratio_w252_sw21_v070_slope_signal(assets, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of assets to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 504d, slope over 63d
def f28vt_assets_netinc_ratio_w504_sw63_v071_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 63d, slope over 5d
def f28vt_assets_w63_sw5_v072_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 5 days."""
    base = _sma(assets, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: marketcap smoothed by 126d, slope over 21d
def f28vt_marketcap_w126_sw21_v073_slope_signal(marketcap) -> pd.Series:
    """Calculates the slope of smoothed marketcap over 21 days."""
    base = _sma(marketcap, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ev smoothed by 252d, slope over 63d
def f28vt_marketcap_ev_ratio_w252_sw63_v074_slope_signal(marketcap, ev) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to revenue smoothed by 504d, slope over 5d
def f28vt_marketcap_revenue_ratio_w504_sw5_v075_slope_signal(marketcap, revenue) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ebitda smoothed by 63d, slope over 21d
def f28vt_marketcap_ebitda_ratio_w63_sw21_v076_slope_signal(marketcap, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(marketcap, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to netinc smoothed by 126d, slope over 63d
def f28vt_marketcap_netinc_ratio_w126_sw63_v077_slope_signal(marketcap, netinc) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to assets smoothed by 252d, slope over 5d
def f28vt_marketcap_assets_ratio_w252_sw5_v078_slope_signal(marketcap, assets) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to marketcap smoothed by 504d, slope over 21d
def f28vt_ev_marketcap_ratio_w504_sw21_v079_slope_signal(ev, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ev to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ev smoothed by 63d, slope over 63d
def f28vt_ev_w63_sw63_v080_slope_signal(ev) -> pd.Series:
    """Calculates the slope of smoothed ev over 63 days."""
    base = _sma(ev, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to revenue smoothed by 126d, slope over 5d
def f28vt_ev_revenue_ratio_w126_sw5_v081_slope_signal(ev, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ev to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to ebitda smoothed by 252d, slope over 21d
def f28vt_ev_ebitda_ratio_w252_sw21_v082_slope_signal(ev, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of ev to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to netinc smoothed by 504d, slope over 63d
def f28vt_ev_netinc_ratio_w504_sw63_v083_slope_signal(ev, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ev to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ev, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to assets smoothed by 63d, slope over 5d
def f28vt_ev_assets_ratio_w63_sw5_v084_slope_signal(ev, assets) -> pd.Series:
    """Calculates the slope of the ratio of ev to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to marketcap smoothed by 126d, slope over 21d
def f28vt_revenue_marketcap_ratio_w126_sw21_v085_slope_signal(revenue, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of revenue to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ev smoothed by 252d, slope over 63d
def f28vt_revenue_ev_ratio_w252_sw63_v086_slope_signal(revenue, ev) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f28vt_revenue_w504_sw5_v087_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ebitda smoothed by 63d, slope over 21d
def f28vt_revenue_ebitda_ratio_w63_sw21_v088_slope_signal(revenue, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 63d
def f28vt_revenue_netinc_ratio_w126_sw63_v089_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 5d
def f28vt_revenue_assets_ratio_w252_sw5_v090_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to marketcap smoothed by 504d, slope over 21d
def f28vt_ebitda_marketcap_ratio_w504_sw21_v091_slope_signal(ebitda, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ebitda, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to ev smoothed by 63d, slope over 63d
def f28vt_ebitda_ev_ratio_w63_sw63_v092_slope_signal(ebitda, ev) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to revenue smoothed by 126d, slope over 5d
def f28vt_ebitda_revenue_ratio_w126_sw5_v093_slope_signal(ebitda, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ebitda smoothed by 252d, slope over 21d
def f28vt_ebitda_w252_sw21_v094_slope_signal(ebitda) -> pd.Series:
    """Calculates the slope of smoothed ebitda over 21 days."""
    base = _sma(ebitda, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to netinc smoothed by 504d, slope over 63d
def f28vt_ebitda_netinc_ratio_w504_sw63_v095_slope_signal(ebitda, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to assets smoothed by 63d, slope over 5d
def f28vt_ebitda_assets_ratio_w63_sw5_v096_slope_signal(ebitda, assets) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to marketcap smoothed by 126d, slope over 21d
def f28vt_netinc_marketcap_ratio_w126_sw21_v097_slope_signal(netinc, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of netinc to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ev smoothed by 252d, slope over 63d
def f28vt_netinc_ev_ratio_w252_sw63_v098_slope_signal(netinc, ev) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(netinc, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 504d, slope over 5d
def f28vt_netinc_revenue_ratio_w504_sw5_v099_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ebitda smoothed by 63d, slope over 21d
def f28vt_netinc_ebitda_ratio_w63_sw21_v100_slope_signal(netinc, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 126d, slope over 63d
def f28vt_netinc_w126_sw63_v101_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 63 days."""
    base = _sma(netinc, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 252d, slope over 5d
def f28vt_netinc_assets_ratio_w252_sw5_v102_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to marketcap smoothed by 504d, slope over 21d
def f28vt_assets_marketcap_ratio_w504_sw21_v103_slope_signal(assets, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of assets to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ev smoothed by 63d, slope over 63d
def f28vt_assets_ev_ratio_w63_sw63_v104_slope_signal(assets, ev) -> pd.Series:
    """Calculates the slope of the ratio of assets to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f28vt_assets_revenue_ratio_w126_sw5_v105_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ebitda smoothed by 252d, slope over 21d
def f28vt_assets_ebitda_ratio_w252_sw21_v106_slope_signal(assets, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of assets to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 504d, slope over 63d
def f28vt_assets_netinc_ratio_w504_sw63_v107_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 63d, slope over 5d
def f28vt_assets_w63_sw5_v108_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 5 days."""
    base = _sma(assets, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: marketcap smoothed by 126d, slope over 21d
def f28vt_marketcap_w126_sw21_v109_slope_signal(marketcap) -> pd.Series:
    """Calculates the slope of smoothed marketcap over 21 days."""
    base = _sma(marketcap, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ev smoothed by 252d, slope over 63d
def f28vt_marketcap_ev_ratio_w252_sw63_v110_slope_signal(marketcap, ev) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to revenue smoothed by 504d, slope over 5d
def f28vt_marketcap_revenue_ratio_w504_sw5_v111_slope_signal(marketcap, revenue) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ebitda smoothed by 63d, slope over 21d
def f28vt_marketcap_ebitda_ratio_w63_sw21_v112_slope_signal(marketcap, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(marketcap, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to netinc smoothed by 126d, slope over 63d
def f28vt_marketcap_netinc_ratio_w126_sw63_v113_slope_signal(marketcap, netinc) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to assets smoothed by 252d, slope over 5d
def f28vt_marketcap_assets_ratio_w252_sw5_v114_slope_signal(marketcap, assets) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to marketcap smoothed by 504d, slope over 21d
def f28vt_ev_marketcap_ratio_w504_sw21_v115_slope_signal(ev, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ev to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ev smoothed by 63d, slope over 63d
def f28vt_ev_w63_sw63_v116_slope_signal(ev) -> pd.Series:
    """Calculates the slope of smoothed ev over 63 days."""
    base = _sma(ev, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to revenue smoothed by 126d, slope over 5d
def f28vt_ev_revenue_ratio_w126_sw5_v117_slope_signal(ev, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ev to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to ebitda smoothed by 252d, slope over 21d
def f28vt_ev_ebitda_ratio_w252_sw21_v118_slope_signal(ev, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of ev to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(ev, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to netinc smoothed by 504d, slope over 63d
def f28vt_ev_netinc_ratio_w504_sw63_v119_slope_signal(ev, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ev to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ev, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ev to assets smoothed by 63d, slope over 5d
def f28vt_ev_assets_ratio_w63_sw5_v120_slope_signal(ev, assets) -> pd.Series:
    """Calculates the slope of the ratio of ev to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ev, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to marketcap smoothed by 126d, slope over 21d
def f28vt_revenue_marketcap_ratio_w126_sw21_v121_slope_signal(revenue, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of revenue to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ev smoothed by 252d, slope over 63d
def f28vt_revenue_ev_ratio_w252_sw63_v122_slope_signal(revenue, ev) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f28vt_revenue_w504_sw5_v123_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to ebitda smoothed by 63d, slope over 21d
def f28vt_revenue_ebitda_ratio_w63_sw21_v124_slope_signal(revenue, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of revenue to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(revenue, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 63d
def f28vt_revenue_netinc_ratio_w126_sw63_v125_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 5d
def f28vt_revenue_assets_ratio_w252_sw5_v126_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to marketcap smoothed by 504d, slope over 21d
def f28vt_ebitda_marketcap_ratio_w504_sw21_v127_slope_signal(ebitda, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(ebitda, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to ev smoothed by 63d, slope over 63d
def f28vt_ebitda_ev_ratio_w63_sw63_v128_slope_signal(ebitda, ev) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to revenue smoothed by 126d, slope over 5d
def f28vt_ebitda_revenue_ratio_w126_sw5_v129_slope_signal(ebitda, revenue) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ebitda smoothed by 252d, slope over 21d
def f28vt_ebitda_w252_sw21_v130_slope_signal(ebitda) -> pd.Series:
    """Calculates the slope of smoothed ebitda over 21 days."""
    base = _sma(ebitda, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to netinc smoothed by 504d, slope over 63d
def f28vt_ebitda_netinc_ratio_w504_sw63_v131_slope_signal(ebitda, netinc) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(ebitda, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of ebitda to assets smoothed by 63d, slope over 5d
def f28vt_ebitda_assets_ratio_w63_sw5_v132_slope_signal(ebitda, assets) -> pd.Series:
    """Calculates the slope of the ratio of ebitda to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(ebitda, assets)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to marketcap smoothed by 126d, slope over 21d
def f28vt_netinc_marketcap_ratio_w126_sw21_v133_slope_signal(netinc, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of netinc to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, marketcap)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ev smoothed by 252d, slope over 63d
def f28vt_netinc_ev_ratio_w252_sw63_v134_slope_signal(netinc, ev) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(netinc, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 504d, slope over 5d
def f28vt_netinc_revenue_ratio_w504_sw5_v135_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to ebitda smoothed by 63d, slope over 21d
def f28vt_netinc_ebitda_ratio_w63_sw21_v136_slope_signal(netinc, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of netinc to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(netinc, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 126d, slope over 63d
def f28vt_netinc_w126_sw63_v137_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 63 days."""
    base = _sma(netinc, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 252d, slope over 5d
def f28vt_netinc_assets_ratio_w252_sw5_v138_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(netinc, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to marketcap smoothed by 504d, slope over 21d
def f28vt_assets_marketcap_ratio_w504_sw21_v139_slope_signal(assets, marketcap) -> pd.Series:
    """Calculates the slope of the ratio of assets to marketcap smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, marketcap)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ev smoothed by 63d, slope over 63d
def f28vt_assets_ev_ratio_w63_sw63_v140_slope_signal(assets, ev) -> pd.Series:
    """Calculates the slope of the ratio of assets to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, ev)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f28vt_assets_revenue_ratio_w126_sw5_v141_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to ebitda smoothed by 252d, slope over 21d
def f28vt_assets_ebitda_ratio_w252_sw21_v142_slope_signal(assets, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of assets to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(assets, ebitda)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 504d, slope over 63d
def f28vt_assets_netinc_ratio_w504_sw63_v143_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(assets, netinc)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 63d, slope over 5d
def f28vt_assets_w63_sw5_v144_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 5 days."""
    base = _sma(assets, 63)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: marketcap smoothed by 126d, slope over 21d
def f28vt_marketcap_w126_sw21_v145_slope_signal(marketcap) -> pd.Series:
    """Calculates the slope of smoothed marketcap over 21 days."""
    base = _sma(marketcap, 126)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ev smoothed by 252d, slope over 63d
def f28vt_marketcap_ev_ratio_w252_sw63_v146_slope_signal(marketcap, ev) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ev smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, ev)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to revenue smoothed by 504d, slope over 5d
def f28vt_marketcap_revenue_ratio_w504_sw5_v147_slope_signal(marketcap, revenue) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to revenue smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, revenue)
    base = _sma(ratio, 504)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to ebitda smoothed by 63d, slope over 21d
def f28vt_marketcap_ebitda_ratio_w63_sw21_v148_slope_signal(marketcap, ebitda) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to ebitda smoothed over 21 days."""
    ratio = _f28vt_ratio(marketcap, ebitda)
    base = _sma(ratio, 63)
    res = _f28vt_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to netinc smoothed by 126d, slope over 63d
def f28vt_marketcap_netinc_ratio_w126_sw63_v149_slope_signal(marketcap, netinc) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to netinc smoothed over 63 days."""
    ratio = _f28vt_ratio(marketcap, netinc)
    base = _sma(ratio, 126)
    res = _f28vt_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of marketcap to assets smoothed by 252d, slope over 5d
def f28vt_marketcap_assets_ratio_w252_sw5_v150_slope_signal(marketcap, assets) -> pd.Series:
    """Calculates the slope of the ratio of marketcap to assets smoothed over 5 days."""
    ratio = _f28vt_ratio(marketcap, assets)
    base = _sma(ratio, 252)
    res = _f28vt_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.random.normal(100, 20, n) for col in ['marketcap', 'ev', 'revenue', 'ebitda', 'netinc', 'assets']})
    for col in ['marketcap', 'ev', 'revenue', 'ebitda', 'netinc', 'assets']:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f28vt_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f28_valuation_trajectory/f28vt_slope_001_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f28vt_'))]}
f28vt_REGISTRY_SLOPE = REGISTRY

