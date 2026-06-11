import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f26_dilution_rate_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f26_dilution_rate_diff(a, b):
    return a - b

def _f26_dilution_rate_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Base feature: sharesbas smoothed by 126d
def f26_dilution_rate_sharesbas_w126_v001_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 126 days."""
    res = _sma(sharesbas, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 252d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_v002_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 504d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_v003_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to assets smoothed by 756d
def f26_dilution_rate_sharesbas_assets_ratio_w756_v004_base_signal(sharesbas, assets) -> pd.Series:
    """Calculates the ratio of sharesbas to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to equity smoothed by 1260d
def f26_dilution_rate_sharesbas_equity_ratio_w1260_v005_base_signal(sharesbas, equity) -> pd.Series:
    """Calculates the ratio of sharesbas to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to fcf smoothed by 63d
def f26_dilution_rate_sharesbas_fcf_ratio_w63_v006_base_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the ratio of sharesbas to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to sharesbas smoothed by 126d
def f26_dilution_rate_revenue_sharesbas_ratio_w126_v007_base_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the ratio of revenue to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 252d
def f26_dilution_rate_revenue_w252_v008_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 252 days."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 504d
def f26_dilution_rate_revenue_netinc_ratio_w504_v009_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 756d
def f26_dilution_rate_revenue_assets_ratio_w756_v010_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to equity smoothed by 1260d
def f26_dilution_rate_revenue_equity_ratio_w1260_v011_base_signal(revenue, equity) -> pd.Series:
    """Calculates the ratio of revenue to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to fcf smoothed by 63d
def f26_dilution_rate_revenue_fcf_ratio_w63_v012_base_signal(revenue, fcf) -> pd.Series:
    """Calculates the ratio of revenue to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to sharesbas smoothed by 126d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_v013_base_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the ratio of netinc to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 252d
def f26_dilution_rate_netinc_revenue_ratio_w252_v014_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 504d
def f26_dilution_rate_netinc_w504_v015_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 504 days."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 756d
def f26_dilution_rate_netinc_assets_ratio_w756_v016_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to equity smoothed by 1260d
def f26_dilution_rate_netinc_equity_ratio_w1260_v017_base_signal(netinc, equity) -> pd.Series:
    """Calculates the ratio of netinc to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to fcf smoothed by 63d
def f26_dilution_rate_netinc_fcf_ratio_w63_v018_base_signal(netinc, fcf) -> pd.Series:
    """Calculates the ratio of netinc to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to sharesbas smoothed by 126d
def f26_dilution_rate_assets_sharesbas_ratio_w126_v019_base_signal(assets, sharesbas) -> pd.Series:
    """Calculates the ratio of assets to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 252d
def f26_dilution_rate_assets_revenue_ratio_w252_v020_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 504d
def f26_dilution_rate_assets_netinc_ratio_w504_v021_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 756d
def f26_dilution_rate_assets_w756_v022_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 756 days."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to equity smoothed by 1260d
def f26_dilution_rate_assets_equity_ratio_w1260_v023_base_signal(assets, equity) -> pd.Series:
    """Calculates the ratio of assets to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to fcf smoothed by 63d
def f26_dilution_rate_assets_fcf_ratio_w63_v024_base_signal(assets, fcf) -> pd.Series:
    """Calculates the ratio of assets to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to sharesbas smoothed by 126d
def f26_dilution_rate_equity_sharesbas_ratio_w126_v025_base_signal(equity, sharesbas) -> pd.Series:
    """Calculates the ratio of equity to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to revenue smoothed by 252d
def f26_dilution_rate_equity_revenue_ratio_w252_v026_base_signal(equity, revenue) -> pd.Series:
    """Calculates the ratio of equity to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to netinc smoothed by 504d
def f26_dilution_rate_equity_netinc_ratio_w504_v027_base_signal(equity, netinc) -> pd.Series:
    """Calculates the ratio of equity to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to assets smoothed by 756d
def f26_dilution_rate_equity_assets_ratio_w756_v028_base_signal(equity, assets) -> pd.Series:
    """Calculates the ratio of equity to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: equity smoothed by 1260d
def f26_dilution_rate_equity_w1260_v029_base_signal(equity) -> pd.Series:
    """Calculates the smoothed equity over 1260 days."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to fcf smoothed by 63d
def f26_dilution_rate_equity_fcf_ratio_w63_v030_base_signal(equity, fcf) -> pd.Series:
    """Calculates the ratio of equity to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to sharesbas smoothed by 126d
def f26_dilution_rate_fcf_sharesbas_ratio_w126_v031_base_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the ratio of fcf to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to revenue smoothed by 252d
def f26_dilution_rate_fcf_revenue_ratio_w252_v032_base_signal(fcf, revenue) -> pd.Series:
    """Calculates the ratio of fcf to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to netinc smoothed by 504d
def f26_dilution_rate_fcf_netinc_ratio_w504_v033_base_signal(fcf, netinc) -> pd.Series:
    """Calculates the ratio of fcf to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to assets smoothed by 756d
def f26_dilution_rate_fcf_assets_ratio_w756_v034_base_signal(fcf, assets) -> pd.Series:
    """Calculates the ratio of fcf to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to equity smoothed by 1260d
def f26_dilution_rate_fcf_equity_ratio_w1260_v035_base_signal(fcf, equity) -> pd.Series:
    """Calculates the ratio of fcf to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: fcf smoothed by 63d
def f26_dilution_rate_fcf_w63_v036_base_signal(fcf) -> pd.Series:
    """Calculates the smoothed fcf over 63 days."""
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: sharesbas smoothed by 126d
def f26_dilution_rate_sharesbas_w126_v037_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 126 days."""
    res = _sma(sharesbas, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 252d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_v038_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 504d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_v039_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to assets smoothed by 756d
def f26_dilution_rate_sharesbas_assets_ratio_w756_v040_base_signal(sharesbas, assets) -> pd.Series:
    """Calculates the ratio of sharesbas to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to equity smoothed by 1260d
def f26_dilution_rate_sharesbas_equity_ratio_w1260_v041_base_signal(sharesbas, equity) -> pd.Series:
    """Calculates the ratio of sharesbas to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to fcf smoothed by 63d
def f26_dilution_rate_sharesbas_fcf_ratio_w63_v042_base_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the ratio of sharesbas to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to sharesbas smoothed by 126d
def f26_dilution_rate_revenue_sharesbas_ratio_w126_v043_base_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the ratio of revenue to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 252d
def f26_dilution_rate_revenue_w252_v044_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 252 days."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 504d
def f26_dilution_rate_revenue_netinc_ratio_w504_v045_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 756d
def f26_dilution_rate_revenue_assets_ratio_w756_v046_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to equity smoothed by 1260d
def f26_dilution_rate_revenue_equity_ratio_w1260_v047_base_signal(revenue, equity) -> pd.Series:
    """Calculates the ratio of revenue to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to fcf smoothed by 63d
def f26_dilution_rate_revenue_fcf_ratio_w63_v048_base_signal(revenue, fcf) -> pd.Series:
    """Calculates the ratio of revenue to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to sharesbas smoothed by 126d
def f26_dilution_rate_netinc_sharesbas_ratio_w126_v049_base_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the ratio of netinc to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 252d
def f26_dilution_rate_netinc_revenue_ratio_w252_v050_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 504d
def f26_dilution_rate_netinc_w504_v051_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 504 days."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 756d
def f26_dilution_rate_netinc_assets_ratio_w756_v052_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to equity smoothed by 1260d
def f26_dilution_rate_netinc_equity_ratio_w1260_v053_base_signal(netinc, equity) -> pd.Series:
    """Calculates the ratio of netinc to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to fcf smoothed by 63d
def f26_dilution_rate_netinc_fcf_ratio_w63_v054_base_signal(netinc, fcf) -> pd.Series:
    """Calculates the ratio of netinc to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to sharesbas smoothed by 126d
def f26_dilution_rate_assets_sharesbas_ratio_w126_v055_base_signal(assets, sharesbas) -> pd.Series:
    """Calculates the ratio of assets to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 252d
def f26_dilution_rate_assets_revenue_ratio_w252_v056_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 504d
def f26_dilution_rate_assets_netinc_ratio_w504_v057_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 756d
def f26_dilution_rate_assets_w756_v058_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 756 days."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to equity smoothed by 1260d
def f26_dilution_rate_assets_equity_ratio_w1260_v059_base_signal(assets, equity) -> pd.Series:
    """Calculates the ratio of assets to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to fcf smoothed by 63d
def f26_dilution_rate_assets_fcf_ratio_w63_v060_base_signal(assets, fcf) -> pd.Series:
    """Calculates the ratio of assets to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to sharesbas smoothed by 126d
def f26_dilution_rate_equity_sharesbas_ratio_w126_v061_base_signal(equity, sharesbas) -> pd.Series:
    """Calculates the ratio of equity to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to revenue smoothed by 252d
def f26_dilution_rate_equity_revenue_ratio_w252_v062_base_signal(equity, revenue) -> pd.Series:
    """Calculates the ratio of equity to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to netinc smoothed by 504d
def f26_dilution_rate_equity_netinc_ratio_w504_v063_base_signal(equity, netinc) -> pd.Series:
    """Calculates the ratio of equity to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to assets smoothed by 756d
def f26_dilution_rate_equity_assets_ratio_w756_v064_base_signal(equity, assets) -> pd.Series:
    """Calculates the ratio of equity to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: equity smoothed by 1260d
def f26_dilution_rate_equity_w1260_v065_base_signal(equity) -> pd.Series:
    """Calculates the smoothed equity over 1260 days."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to fcf smoothed by 63d
def f26_dilution_rate_equity_fcf_ratio_w63_v066_base_signal(equity, fcf) -> pd.Series:
    """Calculates the ratio of equity to fcf smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to sharesbas smoothed by 126d
def f26_dilution_rate_fcf_sharesbas_ratio_w126_v067_base_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the ratio of fcf to sharesbas smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to revenue smoothed by 252d
def f26_dilution_rate_fcf_revenue_ratio_w252_v068_base_signal(fcf, revenue) -> pd.Series:
    """Calculates the ratio of fcf to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to netinc smoothed by 504d
def f26_dilution_rate_fcf_netinc_ratio_w504_v069_base_signal(fcf, netinc) -> pd.Series:
    """Calculates the ratio of fcf to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to assets smoothed by 756d
def f26_dilution_rate_fcf_assets_ratio_w756_v070_base_signal(fcf, assets) -> pd.Series:
    """Calculates the ratio of fcf to assets smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to equity smoothed by 1260d
def f26_dilution_rate_fcf_equity_ratio_w1260_v071_base_signal(fcf, equity) -> pd.Series:
    """Calculates the ratio of fcf to equity smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: fcf smoothed by 63d
def f26_dilution_rate_fcf_w63_v072_base_signal(fcf) -> pd.Series:
    """Calculates the smoothed fcf over 63 days."""
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: sharesbas smoothed by 126d
def f26_dilution_rate_sharesbas_w126_v073_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 126 days."""
    res = _sma(sharesbas, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 252d
def f26_dilution_rate_sharesbas_revenue_ratio_w252_v074_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 504d
def f26_dilution_rate_sharesbas_netinc_ratio_w504_v075_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 504)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f26_dilution_rate/f26_dilution_rate_base_001_075_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f26_dilution_rate_'))]}
F26_DILUTION_RATE_REGISTRY_BASE = REGISTRY
