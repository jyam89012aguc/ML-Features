import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f26_dilution_rate_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f26_dilution_rate_diff(a, b):
    return a - b

def _f26_dilution_rate_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _f26_dilution_rate_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Slope feature: sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_sharesbas_w126_sw21_v001_slope_signal(sharesbas) -> pd.Series:
    """Calculates the slope of smoothed sharesbas over 21 days."""
    base = _sma(sharesbas, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_sw63_v002_slope_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_sw5_v003_slope_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_sharesbas_assets_ratio_w63_sw21_v004_slope_signal(sharesbas, assets) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_sharesbas_equity_ratio_w126_sw63_v005_slope_signal(sharesbas, equity) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_sharesbas_fcf_ratio_w252_sw5_v006_slope_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_revenue_sharesbas_ratio_w504_sw21_v007_slope_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of revenue to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_revenue_w63_sw63_v008_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 63 days."""
    base = _sma(revenue, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_revenue_netinc_ratio_w126_sw5_v009_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_revenue_assets_ratio_w252_sw21_v010_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_revenue_equity_ratio_w504_sw63_v011_slope_signal(revenue, equity) -> pd.Series:
    """Calculates the slope of the ratio of revenue to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_revenue_fcf_ratio_w63_sw5_v012_slope_signal(revenue, fcf) -> pd.Series:
    """Calculates the slope of the ratio of revenue to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_sw21_v013_slope_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of netinc to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_netinc_revenue_ratio_w252_sw63_v014_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_netinc_w504_sw5_v015_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 5 days."""
    base = _sma(netinc, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_netinc_assets_ratio_w63_sw21_v016_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_netinc_equity_ratio_w126_sw63_v017_slope_signal(netinc, equity) -> pd.Series:
    """Calculates the slope of the ratio of netinc to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_netinc_fcf_ratio_w252_sw5_v018_slope_signal(netinc, fcf) -> pd.Series:
    """Calculates the slope of the ratio of netinc to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_assets_sharesbas_ratio_w504_sw21_v019_slope_signal(assets, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of assets to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_assets_revenue_ratio_w63_sw63_v020_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_assets_netinc_ratio_w126_sw5_v021_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f26_dilution_rate_assets_w252_sw21_v022_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_assets_equity_ratio_w504_sw63_v023_slope_signal(assets, equity) -> pd.Series:
    """Calculates the slope of the ratio of assets to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_assets_fcf_ratio_w63_sw5_v024_slope_signal(assets, fcf) -> pd.Series:
    """Calculates the slope of the ratio of assets to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_equity_sharesbas_ratio_w126_sw21_v025_slope_signal(equity, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of equity to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_equity_revenue_ratio_w252_sw63_v026_slope_signal(equity, revenue) -> pd.Series:
    """Calculates the slope of the ratio of equity to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_equity_netinc_ratio_w504_sw5_v027_slope_signal(equity, netinc) -> pd.Series:
    """Calculates the slope of the ratio of equity to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_equity_assets_ratio_w63_sw21_v028_slope_signal(equity, assets) -> pd.Series:
    """Calculates the slope of the ratio of equity to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: equity smoothed by 126d, slope over 63d
def f26_dilution_rate_equity_w126_sw63_v029_slope_signal(equity) -> pd.Series:
    """Calculates the slope of smoothed equity over 63 days."""
    base = _sma(equity, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_equity_fcf_ratio_w252_sw5_v030_slope_signal(equity, fcf) -> pd.Series:
    """Calculates the slope of the ratio of equity to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_fcf_sharesbas_ratio_w504_sw21_v031_slope_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of fcf to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_fcf_revenue_ratio_w63_sw63_v032_slope_signal(fcf, revenue) -> pd.Series:
    """Calculates the slope of the ratio of fcf to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_fcf_netinc_ratio_w126_sw5_v033_slope_signal(fcf, netinc) -> pd.Series:
    """Calculates the slope of the ratio of fcf to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_fcf_assets_ratio_w252_sw21_v034_slope_signal(fcf, assets) -> pd.Series:
    """Calculates the slope of the ratio of fcf to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_fcf_equity_ratio_w504_sw63_v035_slope_signal(fcf, equity) -> pd.Series:
    """Calculates the slope of the ratio of fcf to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_fcf_w63_sw5_v036_slope_signal(fcf) -> pd.Series:
    """Calculates the slope of smoothed fcf over 5 days."""
    base = _sma(fcf, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_sharesbas_w126_sw21_v037_slope_signal(sharesbas) -> pd.Series:
    """Calculates the slope of smoothed sharesbas over 21 days."""
    base = _sma(sharesbas, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_sw63_v038_slope_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_sw5_v039_slope_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_sharesbas_assets_ratio_w63_sw21_v040_slope_signal(sharesbas, assets) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_sharesbas_equity_ratio_w126_sw63_v041_slope_signal(sharesbas, equity) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_sharesbas_fcf_ratio_w252_sw5_v042_slope_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_revenue_sharesbas_ratio_w504_sw21_v043_slope_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of revenue to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_revenue_w63_sw63_v044_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 63 days."""
    base = _sma(revenue, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_revenue_netinc_ratio_w126_sw5_v045_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_revenue_assets_ratio_w252_sw21_v046_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_revenue_equity_ratio_w504_sw63_v047_slope_signal(revenue, equity) -> pd.Series:
    """Calculates the slope of the ratio of revenue to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_revenue_fcf_ratio_w63_sw5_v048_slope_signal(revenue, fcf) -> pd.Series:
    """Calculates the slope of the ratio of revenue to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_sw21_v049_slope_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of netinc to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_netinc_revenue_ratio_w252_sw63_v050_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_netinc_w504_sw5_v051_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 5 days."""
    base = _sma(netinc, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_netinc_assets_ratio_w63_sw21_v052_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_netinc_equity_ratio_w126_sw63_v053_slope_signal(netinc, equity) -> pd.Series:
    """Calculates the slope of the ratio of netinc to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_netinc_fcf_ratio_w252_sw5_v054_slope_signal(netinc, fcf) -> pd.Series:
    """Calculates the slope of the ratio of netinc to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_assets_sharesbas_ratio_w504_sw21_v055_slope_signal(assets, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of assets to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_assets_revenue_ratio_w63_sw63_v056_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_assets_netinc_ratio_w126_sw5_v057_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f26_dilution_rate_assets_w252_sw21_v058_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_assets_equity_ratio_w504_sw63_v059_slope_signal(assets, equity) -> pd.Series:
    """Calculates the slope of the ratio of assets to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_assets_fcf_ratio_w63_sw5_v060_slope_signal(assets, fcf) -> pd.Series:
    """Calculates the slope of the ratio of assets to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_equity_sharesbas_ratio_w126_sw21_v061_slope_signal(equity, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of equity to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_equity_revenue_ratio_w252_sw63_v062_slope_signal(equity, revenue) -> pd.Series:
    """Calculates the slope of the ratio of equity to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_equity_netinc_ratio_w504_sw5_v063_slope_signal(equity, netinc) -> pd.Series:
    """Calculates the slope of the ratio of equity to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_equity_assets_ratio_w63_sw21_v064_slope_signal(equity, assets) -> pd.Series:
    """Calculates the slope of the ratio of equity to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: equity smoothed by 126d, slope over 63d
def f26_dilution_rate_equity_w126_sw63_v065_slope_signal(equity) -> pd.Series:
    """Calculates the slope of smoothed equity over 63 days."""
    base = _sma(equity, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_equity_fcf_ratio_w252_sw5_v066_slope_signal(equity, fcf) -> pd.Series:
    """Calculates the slope of the ratio of equity to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_fcf_sharesbas_ratio_w504_sw21_v067_slope_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of fcf to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_fcf_revenue_ratio_w63_sw63_v068_slope_signal(fcf, revenue) -> pd.Series:
    """Calculates the slope of the ratio of fcf to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_fcf_netinc_ratio_w126_sw5_v069_slope_signal(fcf, netinc) -> pd.Series:
    """Calculates the slope of the ratio of fcf to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_fcf_assets_ratio_w252_sw21_v070_slope_signal(fcf, assets) -> pd.Series:
    """Calculates the slope of the ratio of fcf to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_fcf_equity_ratio_w504_sw63_v071_slope_signal(fcf, equity) -> pd.Series:
    """Calculates the slope of the ratio of fcf to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_fcf_w63_sw5_v072_slope_signal(fcf) -> pd.Series:
    """Calculates the slope of smoothed fcf over 5 days."""
    base = _sma(fcf, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_sharesbas_w126_sw21_v073_slope_signal(sharesbas) -> pd.Series:
    """Calculates the slope of smoothed sharesbas over 21 days."""
    base = _sma(sharesbas, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_sw63_v074_slope_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_sw5_v075_slope_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_sharesbas_assets_ratio_w63_sw21_v076_slope_signal(sharesbas, assets) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_sharesbas_equity_ratio_w126_sw63_v077_slope_signal(sharesbas, equity) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_sharesbas_fcf_ratio_w252_sw5_v078_slope_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_revenue_sharesbas_ratio_w504_sw21_v079_slope_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of revenue to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_revenue_w63_sw63_v080_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 63 days."""
    base = _sma(revenue, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_revenue_netinc_ratio_w126_sw5_v081_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_revenue_assets_ratio_w252_sw21_v082_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_revenue_equity_ratio_w504_sw63_v083_slope_signal(revenue, equity) -> pd.Series:
    """Calculates the slope of the ratio of revenue to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_revenue_fcf_ratio_w63_sw5_v084_slope_signal(revenue, fcf) -> pd.Series:
    """Calculates the slope of the ratio of revenue to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_sw21_v085_slope_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of netinc to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_netinc_revenue_ratio_w252_sw63_v086_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_netinc_w504_sw5_v087_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 5 days."""
    base = _sma(netinc, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_netinc_assets_ratio_w63_sw21_v088_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_netinc_equity_ratio_w126_sw63_v089_slope_signal(netinc, equity) -> pd.Series:
    """Calculates the slope of the ratio of netinc to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_netinc_fcf_ratio_w252_sw5_v090_slope_signal(netinc, fcf) -> pd.Series:
    """Calculates the slope of the ratio of netinc to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_assets_sharesbas_ratio_w504_sw21_v091_slope_signal(assets, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of assets to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_assets_revenue_ratio_w63_sw63_v092_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_assets_netinc_ratio_w126_sw5_v093_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f26_dilution_rate_assets_w252_sw21_v094_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_assets_equity_ratio_w504_sw63_v095_slope_signal(assets, equity) -> pd.Series:
    """Calculates the slope of the ratio of assets to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_assets_fcf_ratio_w63_sw5_v096_slope_signal(assets, fcf) -> pd.Series:
    """Calculates the slope of the ratio of assets to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_equity_sharesbas_ratio_w126_sw21_v097_slope_signal(equity, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of equity to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_equity_revenue_ratio_w252_sw63_v098_slope_signal(equity, revenue) -> pd.Series:
    """Calculates the slope of the ratio of equity to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_equity_netinc_ratio_w504_sw5_v099_slope_signal(equity, netinc) -> pd.Series:
    """Calculates the slope of the ratio of equity to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_equity_assets_ratio_w63_sw21_v100_slope_signal(equity, assets) -> pd.Series:
    """Calculates the slope of the ratio of equity to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: equity smoothed by 126d, slope over 63d
def f26_dilution_rate_equity_w126_sw63_v101_slope_signal(equity) -> pd.Series:
    """Calculates the slope of smoothed equity over 63 days."""
    base = _sma(equity, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_equity_fcf_ratio_w252_sw5_v102_slope_signal(equity, fcf) -> pd.Series:
    """Calculates the slope of the ratio of equity to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_fcf_sharesbas_ratio_w504_sw21_v103_slope_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of fcf to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_fcf_revenue_ratio_w63_sw63_v104_slope_signal(fcf, revenue) -> pd.Series:
    """Calculates the slope of the ratio of fcf to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_fcf_netinc_ratio_w126_sw5_v105_slope_signal(fcf, netinc) -> pd.Series:
    """Calculates the slope of the ratio of fcf to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_fcf_assets_ratio_w252_sw21_v106_slope_signal(fcf, assets) -> pd.Series:
    """Calculates the slope of the ratio of fcf to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_fcf_equity_ratio_w504_sw63_v107_slope_signal(fcf, equity) -> pd.Series:
    """Calculates the slope of the ratio of fcf to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_fcf_w63_sw5_v108_slope_signal(fcf) -> pd.Series:
    """Calculates the slope of smoothed fcf over 5 days."""
    base = _sma(fcf, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_sharesbas_w126_sw21_v109_slope_signal(sharesbas) -> pd.Series:
    """Calculates the slope of smoothed sharesbas over 21 days."""
    base = _sma(sharesbas, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_sw63_v110_slope_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_sw5_v111_slope_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_sharesbas_assets_ratio_w63_sw21_v112_slope_signal(sharesbas, assets) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_sharesbas_equity_ratio_w126_sw63_v113_slope_signal(sharesbas, equity) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_sharesbas_fcf_ratio_w252_sw5_v114_slope_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_revenue_sharesbas_ratio_w504_sw21_v115_slope_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of revenue to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_revenue_w63_sw63_v116_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 63 days."""
    base = _sma(revenue, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_revenue_netinc_ratio_w126_sw5_v117_slope_signal(revenue, netinc) -> pd.Series:
    """Calculates the slope of the ratio of revenue to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_revenue_assets_ratio_w252_sw21_v118_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_revenue_equity_ratio_w504_sw63_v119_slope_signal(revenue, equity) -> pd.Series:
    """Calculates the slope of the ratio of revenue to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_revenue_fcf_ratio_w63_sw5_v120_slope_signal(revenue, fcf) -> pd.Series:
    """Calculates the slope of the ratio of revenue to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_sw21_v121_slope_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of netinc to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_netinc_revenue_ratio_w252_sw63_v122_slope_signal(netinc, revenue) -> pd.Series:
    """Calculates the slope of the ratio of netinc to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_netinc_w504_sw5_v123_slope_signal(netinc) -> pd.Series:
    """Calculates the slope of smoothed netinc over 5 days."""
    base = _sma(netinc, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_netinc_assets_ratio_w63_sw21_v124_slope_signal(netinc, assets) -> pd.Series:
    """Calculates the slope of the ratio of netinc to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_netinc_equity_ratio_w126_sw63_v125_slope_signal(netinc, equity) -> pd.Series:
    """Calculates the slope of the ratio of netinc to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of netinc to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_netinc_fcf_ratio_w252_sw5_v126_slope_signal(netinc, fcf) -> pd.Series:
    """Calculates the slope of the ratio of netinc to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_assets_sharesbas_ratio_w504_sw21_v127_slope_signal(assets, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of assets to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_assets_revenue_ratio_w63_sw63_v128_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_assets_netinc_ratio_w126_sw5_v129_slope_signal(assets, netinc) -> pd.Series:
    """Calculates the slope of the ratio of assets to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f26_dilution_rate_assets_w252_sw21_v130_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_assets_equity_ratio_w504_sw63_v131_slope_signal(assets, equity) -> pd.Series:
    """Calculates the slope of the ratio of assets to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_assets_fcf_ratio_w63_sw5_v132_slope_signal(assets, fcf) -> pd.Series:
    """Calculates the slope of the ratio of assets to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_equity_sharesbas_ratio_w126_sw21_v133_slope_signal(equity, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of equity to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_equity_revenue_ratio_w252_sw63_v134_slope_signal(equity, revenue) -> pd.Series:
    """Calculates the slope of the ratio of equity to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_equity_netinc_ratio_w504_sw5_v135_slope_signal(equity, netinc) -> pd.Series:
    """Calculates the slope of the ratio of equity to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_equity_assets_ratio_w63_sw21_v136_slope_signal(equity, assets) -> pd.Series:
    """Calculates the slope of the ratio of equity to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: equity smoothed by 126d, slope over 63d
def f26_dilution_rate_equity_w126_sw63_v137_slope_signal(equity) -> pd.Series:
    """Calculates the slope of smoothed equity over 63 days."""
    base = _sma(equity, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of equity to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_equity_fcf_ratio_w252_sw5_v138_slope_signal(equity, fcf) -> pd.Series:
    """Calculates the slope of the ratio of equity to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to sharesbas smoothed by 504d, slope over 21d
def f26_dilution_rate_fcf_sharesbas_ratio_w504_sw21_v139_slope_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the slope of the ratio of fcf to sharesbas smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to revenue smoothed by 63d, slope over 63d
def f26_dilution_rate_fcf_revenue_ratio_w63_sw63_v140_slope_signal(fcf, revenue) -> pd.Series:
    """Calculates the slope of the ratio of fcf to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to netinc smoothed by 126d, slope over 5d
def f26_dilution_rate_fcf_netinc_ratio_w126_sw5_v141_slope_signal(fcf, netinc) -> pd.Series:
    """Calculates the slope of the ratio of fcf to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to assets smoothed by 252d, slope over 21d
def f26_dilution_rate_fcf_assets_ratio_w252_sw21_v142_slope_signal(fcf, assets) -> pd.Series:
    """Calculates the slope of the ratio of fcf to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of fcf to equity smoothed by 504d, slope over 63d
def f26_dilution_rate_fcf_equity_ratio_w504_sw63_v143_slope_signal(fcf, equity) -> pd.Series:
    """Calculates the slope of the ratio of fcf to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: fcf smoothed by 63d, slope over 5d
def f26_dilution_rate_fcf_w63_sw5_v144_slope_signal(fcf) -> pd.Series:
    """Calculates the slope of smoothed fcf over 5 days."""
    base = _sma(fcf, 63)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: sharesbas smoothed by 126d, slope over 21d
def f26_dilution_rate_sharesbas_w126_sw21_v145_slope_signal(sharesbas) -> pd.Series:
    """Calculates the slope of smoothed sharesbas over 21 days."""
    base = _sma(sharesbas, 126)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to revenue smoothed by 252d, slope over 63d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_sw63_v146_slope_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to revenue smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to netinc smoothed by 504d, slope over 5d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_sw5_v147_slope_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to netinc smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    base = _sma(ratio, 504)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to assets smoothed by 63d, slope over 21d
def f26_dilution_rate_sharesbas_assets_ratio_w63_sw21_v148_slope_signal(sharesbas, assets) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to assets smoothed over 21 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    base = _sma(ratio, 63)
    res = _f26_dilution_rate_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to equity smoothed by 126d, slope over 63d
def f26_dilution_rate_sharesbas_equity_ratio_w126_sw63_v149_slope_signal(sharesbas, equity) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to equity smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    base = _sma(ratio, 126)
    res = _f26_dilution_rate_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of sharesbas to fcf smoothed by 252d, slope over 5d
def f26_dilution_rate_sharesbas_fcf_ratio_w252_sw5_v150_slope_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the slope of the ratio of sharesbas to fcf smoothed over 5 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    base = _sma(ratio, 252)
    res = _f26_dilution_rate_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.random.normal(100, 20, n) for col in ['sharesbas', 'revenue', 'netinc', 'assets', 'equity', 'fcf']})
    for col in ['sharesbas', 'revenue', 'netinc', 'assets', 'equity', 'fcf']:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f26_dilution_rate_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f26_dilution_rate/f26_dilution_rate_slope_001_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f26_dilution_rate_'))]}
F26_DILUTION_RATE_REGISTRY_SLOPE = REGISTRY
