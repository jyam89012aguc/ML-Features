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

# Base feature: sharesbas smoothed by 756d
def f26_dilution_rate_sharesbas_w756_v076_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 756 days."""
    res = _sma(sharesbas, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 1260d
def f26_dilution_rate_sharesbas_revenue_ratio_w1260_v077_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 63d
def f26_dilution_rate_sharesbas_netinc_ratio_w63_v078_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to assets smoothed by 126d
def f26_dilution_rate_sharesbas_assets_ratio_w126_v079_base_signal(sharesbas, assets) -> pd.Series:
    """Calculates the ratio of sharesbas to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to equity smoothed by 252d
def f26_dilution_rate_sharesbas_equity_ratio_w252_v080_base_signal(sharesbas, equity) -> pd.Series:
    """Calculates the ratio of sharesbas to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to fcf smoothed by 504d
def f26_dilution_rate_sharesbas_fcf_ratio_w504_v081_base_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the ratio of sharesbas to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to sharesbas smoothed by 756d
def f26_dilution_rate_revenue_sharesbas_ratio_w756_v082_base_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the ratio of revenue to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 1260d
def f26_dilution_rate_revenue_w1260_v083_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 1260 days."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 63d
def f26_dilution_rate_revenue_netinc_ratio_w63_v084_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 126d
def f26_dilution_rate_revenue_assets_ratio_w126_v085_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to equity smoothed by 252d
def f26_dilution_rate_revenue_equity_ratio_w252_v086_base_signal(revenue, equity) -> pd.Series:
    """Calculates the ratio of revenue to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to fcf smoothed by 504d
def f26_dilution_rate_revenue_fcf_ratio_w504_v087_base_signal(revenue, fcf) -> pd.Series:
    """Calculates the ratio of revenue to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to sharesbas smoothed by 756d
def f26_dilution_rate_netinc_sharesbas_ratio_w756_v088_base_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the ratio of netinc to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 1260d
def f26_dilution_rate_netinc_revenue_ratio_w1260_v089_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 63d
def f26_dilution_rate_netinc_w63_v090_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 63 days."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 126d
def f26_dilution_rate_netinc_assets_ratio_w126_v091_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to equity smoothed by 252d
def f26_dilution_rate_netinc_equity_ratio_w252_v092_base_signal(netinc, equity) -> pd.Series:
    """Calculates the ratio of netinc to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to fcf smoothed by 504d
def f26_dilution_rate_netinc_fcf_ratio_w504_v093_base_signal(netinc, fcf) -> pd.Series:
    """Calculates the ratio of netinc to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to sharesbas smoothed by 756d
def f26_dilution_rate_assets_sharesbas_ratio_w756_v094_base_signal(assets, sharesbas) -> pd.Series:
    """Calculates the ratio of assets to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 1260d
def f26_dilution_rate_assets_revenue_ratio_w1260_v095_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 63d
def f26_dilution_rate_assets_netinc_ratio_w63_v096_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 126d
def f26_dilution_rate_assets_w126_v097_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 126 days."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to equity smoothed by 252d
def f26_dilution_rate_assets_equity_ratio_w252_v098_base_signal(assets, equity) -> pd.Series:
    """Calculates the ratio of assets to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to fcf smoothed by 504d
def f26_dilution_rate_assets_fcf_ratio_w504_v099_base_signal(assets, fcf) -> pd.Series:
    """Calculates the ratio of assets to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to sharesbas smoothed by 756d
def f26_dilution_rate_equity_sharesbas_ratio_w756_v100_base_signal(equity, sharesbas) -> pd.Series:
    """Calculates the ratio of equity to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to revenue smoothed by 1260d
def f26_dilution_rate_equity_revenue_ratio_w1260_v101_base_signal(equity, revenue) -> pd.Series:
    """Calculates the ratio of equity to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to netinc smoothed by 63d
def f26_dilution_rate_equity_netinc_ratio_w63_v102_base_signal(equity, netinc) -> pd.Series:
    """Calculates the ratio of equity to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to assets smoothed by 126d
def f26_dilution_rate_equity_assets_ratio_w126_v103_base_signal(equity, assets) -> pd.Series:
    """Calculates the ratio of equity to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: equity smoothed by 252d
def f26_dilution_rate_equity_w252_v104_base_signal(equity) -> pd.Series:
    """Calculates the smoothed equity over 252 days."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to fcf smoothed by 504d
def f26_dilution_rate_equity_fcf_ratio_w504_v105_base_signal(equity, fcf) -> pd.Series:
    """Calculates the ratio of equity to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to sharesbas smoothed by 756d
def f26_dilution_rate_fcf_sharesbas_ratio_w756_v106_base_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the ratio of fcf to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to revenue smoothed by 1260d
def f26_dilution_rate_fcf_revenue_ratio_w1260_v107_base_signal(fcf, revenue) -> pd.Series:
    """Calculates the ratio of fcf to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to netinc smoothed by 63d
def f26_dilution_rate_fcf_netinc_ratio_w63_v108_base_signal(fcf, netinc) -> pd.Series:
    """Calculates the ratio of fcf to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to assets smoothed by 126d
def f26_dilution_rate_fcf_assets_ratio_w126_v109_base_signal(fcf, assets) -> pd.Series:
    """Calculates the ratio of fcf to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to equity smoothed by 252d
def f26_dilution_rate_fcf_equity_ratio_w252_v110_base_signal(fcf, equity) -> pd.Series:
    """Calculates the ratio of fcf to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: fcf smoothed by 504d
def f26_dilution_rate_fcf_w504_v111_base_signal(fcf) -> pd.Series:
    """Calculates the smoothed fcf over 504 days."""
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: sharesbas smoothed by 756d
def f26_dilution_rate_sharesbas_w756_v112_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 756 days."""
    res = _sma(sharesbas, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 1260d
def f26_dilution_rate_sharesbas_revenue_ratio_w1260_v113_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 63d
def f26_dilution_rate_sharesbas_netinc_ratio_w63_v114_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to assets smoothed by 126d
def f26_dilution_rate_sharesbas_assets_ratio_w126_v115_base_signal(sharesbas, assets) -> pd.Series:
    """Calculates the ratio of sharesbas to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to equity smoothed by 252d
def f26_dilution_rate_sharesbas_equity_ratio_w252_v116_base_signal(sharesbas, equity) -> pd.Series:
    """Calculates the ratio of sharesbas to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to fcf smoothed by 504d
def f26_dilution_rate_sharesbas_fcf_ratio_w504_v117_base_signal(sharesbas, fcf) -> pd.Series:
    """Calculates the ratio of sharesbas to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to sharesbas smoothed by 756d
def f26_dilution_rate_revenue_sharesbas_ratio_w756_v118_base_signal(revenue, sharesbas) -> pd.Series:
    """Calculates the ratio of revenue to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(revenue, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 1260d
def f26_dilution_rate_revenue_w1260_v119_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 1260 days."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 63d
def f26_dilution_rate_revenue_netinc_ratio_w63_v120_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(revenue, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 126d
def f26_dilution_rate_revenue_assets_ratio_w126_v121_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(revenue, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to equity smoothed by 252d
def f26_dilution_rate_revenue_equity_ratio_w252_v122_base_signal(revenue, equity) -> pd.Series:
    """Calculates the ratio of revenue to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(revenue, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to fcf smoothed by 504d
def f26_dilution_rate_revenue_fcf_ratio_w504_v123_base_signal(revenue, fcf) -> pd.Series:
    """Calculates the ratio of revenue to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(revenue, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to sharesbas smoothed by 756d
def f26_dilution_rate_netinc_sharesbas_ratio_w756_v124_base_signal(netinc, sharesbas) -> pd.Series:
    """Calculates the ratio of netinc to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(netinc, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 1260d
def f26_dilution_rate_netinc_revenue_ratio_w1260_v125_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(netinc, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 63d
def f26_dilution_rate_netinc_w63_v126_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 63 days."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 126d
def f26_dilution_rate_netinc_assets_ratio_w126_v127_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(netinc, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to equity smoothed by 252d
def f26_dilution_rate_netinc_equity_ratio_w252_v128_base_signal(netinc, equity) -> pd.Series:
    """Calculates the ratio of netinc to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(netinc, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to fcf smoothed by 504d
def f26_dilution_rate_netinc_fcf_ratio_w504_v129_base_signal(netinc, fcf) -> pd.Series:
    """Calculates the ratio of netinc to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(netinc, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to sharesbas smoothed by 756d
def f26_dilution_rate_assets_sharesbas_ratio_w756_v130_base_signal(assets, sharesbas) -> pd.Series:
    """Calculates the ratio of assets to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(assets, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 1260d
def f26_dilution_rate_assets_revenue_ratio_w1260_v131_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(assets, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 63d
def f26_dilution_rate_assets_netinc_ratio_w63_v132_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(assets, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 126d
def f26_dilution_rate_assets_w126_v133_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 126 days."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to equity smoothed by 252d
def f26_dilution_rate_assets_equity_ratio_w252_v134_base_signal(assets, equity) -> pd.Series:
    """Calculates the ratio of assets to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(assets, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to fcf smoothed by 504d
def f26_dilution_rate_assets_fcf_ratio_w504_v135_base_signal(assets, fcf) -> pd.Series:
    """Calculates the ratio of assets to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(assets, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to sharesbas smoothed by 756d
def f26_dilution_rate_equity_sharesbas_ratio_w756_v136_base_signal(equity, sharesbas) -> pd.Series:
    """Calculates the ratio of equity to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(equity, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to revenue smoothed by 1260d
def f26_dilution_rate_equity_revenue_ratio_w1260_v137_base_signal(equity, revenue) -> pd.Series:
    """Calculates the ratio of equity to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(equity, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to netinc smoothed by 63d
def f26_dilution_rate_equity_netinc_ratio_w63_v138_base_signal(equity, netinc) -> pd.Series:
    """Calculates the ratio of equity to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(equity, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to assets smoothed by 126d
def f26_dilution_rate_equity_assets_ratio_w126_v139_base_signal(equity, assets) -> pd.Series:
    """Calculates the ratio of equity to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(equity, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: equity smoothed by 252d
def f26_dilution_rate_equity_w252_v140_base_signal(equity) -> pd.Series:
    """Calculates the smoothed equity over 252 days."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of equity to fcf smoothed by 504d
def f26_dilution_rate_equity_fcf_ratio_w504_v141_base_signal(equity, fcf) -> pd.Series:
    """Calculates the ratio of equity to fcf smoothed over 504 days."""
    ratio = _f26_dilution_rate_ratio(equity, fcf)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to sharesbas smoothed by 756d
def f26_dilution_rate_fcf_sharesbas_ratio_w756_v142_base_signal(fcf, sharesbas) -> pd.Series:
    """Calculates the ratio of fcf to sharesbas smoothed over 756 days."""
    ratio = _f26_dilution_rate_ratio(fcf, sharesbas)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to revenue smoothed by 1260d
def f26_dilution_rate_fcf_revenue_ratio_w1260_v143_base_signal(fcf, revenue) -> pd.Series:
    """Calculates the ratio of fcf to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(fcf, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to netinc smoothed by 63d
def f26_dilution_rate_fcf_netinc_ratio_w63_v144_base_signal(fcf, netinc) -> pd.Series:
    """Calculates the ratio of fcf to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(fcf, netinc)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to assets smoothed by 126d
def f26_dilution_rate_fcf_assets_ratio_w126_v145_base_signal(fcf, assets) -> pd.Series:
    """Calculates the ratio of fcf to assets smoothed over 126 days."""
    ratio = _f26_dilution_rate_ratio(fcf, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of fcf to equity smoothed by 252d
def f26_dilution_rate_fcf_equity_ratio_w252_v146_base_signal(fcf, equity) -> pd.Series:
    """Calculates the ratio of fcf to equity smoothed over 252 days."""
    ratio = _f26_dilution_rate_ratio(fcf, equity)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: fcf smoothed by 504d
def f26_dilution_rate_fcf_w504_v147_base_signal(fcf) -> pd.Series:
    """Calculates the smoothed fcf over 504 days."""
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: sharesbas smoothed by 756d
def f26_dilution_rate_sharesbas_w756_v148_base_signal(sharesbas) -> pd.Series:
    """Calculates the smoothed sharesbas over 756 days."""
    res = _sma(sharesbas, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to revenue smoothed by 1260d
def f26_dilution_rate_sharesbas_revenue_ratio_w1260_v149_base_signal(sharesbas, revenue) -> pd.Series:
    """Calculates the ratio of sharesbas to revenue smoothed over 1260 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, revenue)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of sharesbas to netinc smoothed by 63d
def f26_dilution_rate_sharesbas_netinc_ratio_w63_v150_base_signal(sharesbas, netinc) -> pd.Series:
    """Calculates the ratio of sharesbas to netinc smoothed over 63 days."""
    ratio = _f26_dilution_rate_ratio(sharesbas, netinc)
    res = _sma(ratio, 63)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f26_dilution_rate/f26_dilution_rate_base_076_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f26_dilution_rate_'))]}
F26_DILUTION_RATE_REGISTRY_BASE = REGISTRY
