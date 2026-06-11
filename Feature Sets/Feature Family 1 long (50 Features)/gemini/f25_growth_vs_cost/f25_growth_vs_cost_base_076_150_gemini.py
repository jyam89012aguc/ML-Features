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

# Base feature: revenue smoothed by 756d
def f25_growth_vs_cost_revenue_w756_v076_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 756 days."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 1260d
def f25_growth_vs_cost_revenue_capex_ratio_w1260_v077_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 63d
def f25_growth_vs_cost_revenue_assets_ratio_w63_v078_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 126d
def f25_growth_vs_cost_revenue_opinc_ratio_w126_v079_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 252d
def f25_growth_vs_cost_revenue_ebitda_ratio_w252_v080_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 504d
def f25_growth_vs_cost_revenue_netinc_ratio_w504_v081_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 756d
def f25_growth_vs_cost_capex_revenue_ratio_w756_v082_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 1260d
def f25_growth_vs_cost_capex_w1260_v083_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 1260 days."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 63d
def f25_growth_vs_cost_capex_assets_ratio_w63_v084_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to opinc smoothed by 126d
def f25_growth_vs_cost_capex_opinc_ratio_w126_v085_base_signal(capex, opinc) -> pd.Series:
    """Calculates the ratio of capex to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to ebitda smoothed by 252d
def f25_growth_vs_cost_capex_ebitda_ratio_w252_v086_base_signal(capex, ebitda) -> pd.Series:
    """Calculates the ratio of capex to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to netinc smoothed by 504d
def f25_growth_vs_cost_capex_netinc_ratio_w504_v087_base_signal(capex, netinc) -> pd.Series:
    """Calculates the ratio of capex to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 756d
def f25_growth_vs_cost_assets_revenue_ratio_w756_v088_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 1260d
def f25_growth_vs_cost_assets_capex_ratio_w1260_v089_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 63d
def f25_growth_vs_cost_assets_w63_v090_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 63 days."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 126d
def f25_growth_vs_cost_assets_opinc_ratio_w126_v091_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 252d
def f25_growth_vs_cost_assets_ebitda_ratio_w252_v092_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 504d
def f25_growth_vs_cost_assets_netinc_ratio_w504_v093_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 756d
def f25_growth_vs_cost_opinc_revenue_ratio_w756_v094_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to capex smoothed by 1260d
def f25_growth_vs_cost_opinc_capex_ratio_w1260_v095_base_signal(opinc, capex) -> pd.Series:
    """Calculates the ratio of opinc to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 63d
def f25_growth_vs_cost_opinc_assets_ratio_w63_v096_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 126d
def f25_growth_vs_cost_opinc_w126_v097_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 126 days."""
    res = _sma(opinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 252d
def f25_growth_vs_cost_opinc_ebitda_ratio_w252_v098_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 504d
def f25_growth_vs_cost_opinc_netinc_ratio_w504_v099_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 756d
def f25_growth_vs_cost_ebitda_revenue_ratio_w756_v100_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to capex smoothed by 1260d
def f25_growth_vs_cost_ebitda_capex_ratio_w1260_v101_base_signal(ebitda, capex) -> pd.Series:
    """Calculates the ratio of ebitda to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 63d
def f25_growth_vs_cost_ebitda_assets_ratio_w63_v102_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 126d
def f25_growth_vs_cost_ebitda_opinc_ratio_w126_v103_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 252d
def f25_growth_vs_cost_ebitda_w252_v104_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 252 days."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 504d
def f25_growth_vs_cost_ebitda_netinc_ratio_w504_v105_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 756d
def f25_growth_vs_cost_netinc_revenue_ratio_w756_v106_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to capex smoothed by 1260d
def f25_growth_vs_cost_netinc_capex_ratio_w1260_v107_base_signal(netinc, capex) -> pd.Series:
    """Calculates the ratio of netinc to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 63d
def f25_growth_vs_cost_netinc_assets_ratio_w63_v108_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 126d
def f25_growth_vs_cost_netinc_opinc_ratio_w126_v109_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 252d
def f25_growth_vs_cost_netinc_ebitda_ratio_w252_v110_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 504d
def f25_growth_vs_cost_netinc_w504_v111_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 504 days."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 756d
def f25_growth_vs_cost_revenue_w756_v112_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 756 days."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 1260d
def f25_growth_vs_cost_revenue_capex_ratio_w1260_v113_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 63d
def f25_growth_vs_cost_revenue_assets_ratio_w63_v114_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to opinc smoothed by 126d
def f25_growth_vs_cost_revenue_opinc_ratio_w126_v115_base_signal(revenue, opinc) -> pd.Series:
    """Calculates the ratio of revenue to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to ebitda smoothed by 252d
def f25_growth_vs_cost_revenue_ebitda_ratio_w252_v116_base_signal(revenue, ebitda) -> pd.Series:
    """Calculates the ratio of revenue to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to netinc smoothed by 504d
def f25_growth_vs_cost_revenue_netinc_ratio_w504_v117_base_signal(revenue, netinc) -> pd.Series:
    """Calculates the ratio of revenue to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 756d
def f25_growth_vs_cost_capex_revenue_ratio_w756_v118_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 1260d
def f25_growth_vs_cost_capex_w1260_v119_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 1260 days."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 63d
def f25_growth_vs_cost_capex_assets_ratio_w63_v120_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to opinc smoothed by 126d
def f25_growth_vs_cost_capex_opinc_ratio_w126_v121_base_signal(capex, opinc) -> pd.Series:
    """Calculates the ratio of capex to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to ebitda smoothed by 252d
def f25_growth_vs_cost_capex_ebitda_ratio_w252_v122_base_signal(capex, ebitda) -> pd.Series:
    """Calculates the ratio of capex to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to netinc smoothed by 504d
def f25_growth_vs_cost_capex_netinc_ratio_w504_v123_base_signal(capex, netinc) -> pd.Series:
    """Calculates the ratio of capex to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(capex, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 756d
def f25_growth_vs_cost_assets_revenue_ratio_w756_v124_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 1260d
def f25_growth_vs_cost_assets_capex_ratio_w1260_v125_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 63d
def f25_growth_vs_cost_assets_w63_v126_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 63 days."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to opinc smoothed by 126d
def f25_growth_vs_cost_assets_opinc_ratio_w126_v127_base_signal(assets, opinc) -> pd.Series:
    """Calculates the ratio of assets to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to ebitda smoothed by 252d
def f25_growth_vs_cost_assets_ebitda_ratio_w252_v128_base_signal(assets, ebitda) -> pd.Series:
    """Calculates the ratio of assets to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to netinc smoothed by 504d
def f25_growth_vs_cost_assets_netinc_ratio_w504_v129_base_signal(assets, netinc) -> pd.Series:
    """Calculates the ratio of assets to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(assets, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to revenue smoothed by 756d
def f25_growth_vs_cost_opinc_revenue_ratio_w756_v130_base_signal(opinc, revenue) -> pd.Series:
    """Calculates the ratio of opinc to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to capex smoothed by 1260d
def f25_growth_vs_cost_opinc_capex_ratio_w1260_v131_base_signal(opinc, capex) -> pd.Series:
    """Calculates the ratio of opinc to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to assets smoothed by 63d
def f25_growth_vs_cost_opinc_assets_ratio_w63_v132_base_signal(opinc, assets) -> pd.Series:
    """Calculates the ratio of opinc to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: opinc smoothed by 126d
def f25_growth_vs_cost_opinc_w126_v133_base_signal(opinc) -> pd.Series:
    """Calculates the smoothed opinc over 126 days."""
    res = _sma(opinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to ebitda smoothed by 252d
def f25_growth_vs_cost_opinc_ebitda_ratio_w252_v134_base_signal(opinc, ebitda) -> pd.Series:
    """Calculates the ratio of opinc to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of opinc to netinc smoothed by 504d
def f25_growth_vs_cost_opinc_netinc_ratio_w504_v135_base_signal(opinc, netinc) -> pd.Series:
    """Calculates the ratio of opinc to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(opinc, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to revenue smoothed by 756d
def f25_growth_vs_cost_ebitda_revenue_ratio_w756_v136_base_signal(ebitda, revenue) -> pd.Series:
    """Calculates the ratio of ebitda to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to capex smoothed by 1260d
def f25_growth_vs_cost_ebitda_capex_ratio_w1260_v137_base_signal(ebitda, capex) -> pd.Series:
    """Calculates the ratio of ebitda to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to assets smoothed by 63d
def f25_growth_vs_cost_ebitda_assets_ratio_w63_v138_base_signal(ebitda, assets) -> pd.Series:
    """Calculates the ratio of ebitda to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to opinc smoothed by 126d
def f25_growth_vs_cost_ebitda_opinc_ratio_w126_v139_base_signal(ebitda, opinc) -> pd.Series:
    """Calculates the ratio of ebitda to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ebitda smoothed by 252d
def f25_growth_vs_cost_ebitda_w252_v140_base_signal(ebitda) -> pd.Series:
    """Calculates the smoothed ebitda over 252 days."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of ebitda to netinc smoothed by 504d
def f25_growth_vs_cost_ebitda_netinc_ratio_w504_v141_base_signal(ebitda, netinc) -> pd.Series:
    """Calculates the ratio of ebitda to netinc smoothed over 504 days."""
    ratio = _f25_growth_vs_cost_ratio(ebitda, netinc)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to revenue smoothed by 756d
def f25_growth_vs_cost_netinc_revenue_ratio_w756_v142_base_signal(netinc, revenue) -> pd.Series:
    """Calculates the ratio of netinc to revenue smoothed over 756 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, revenue)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to capex smoothed by 1260d
def f25_growth_vs_cost_netinc_capex_ratio_w1260_v143_base_signal(netinc, capex) -> pd.Series:
    """Calculates the ratio of netinc to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to assets smoothed by 63d
def f25_growth_vs_cost_netinc_assets_ratio_w63_v144_base_signal(netinc, assets) -> pd.Series:
    """Calculates the ratio of netinc to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, assets)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to opinc smoothed by 126d
def f25_growth_vs_cost_netinc_opinc_ratio_w126_v145_base_signal(netinc, opinc) -> pd.Series:
    """Calculates the ratio of netinc to opinc smoothed over 126 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, opinc)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of netinc to ebitda smoothed by 252d
def f25_growth_vs_cost_netinc_ebitda_ratio_w252_v146_base_signal(netinc, ebitda) -> pd.Series:
    """Calculates the ratio of netinc to ebitda smoothed over 252 days."""
    ratio = _f25_growth_vs_cost_ratio(netinc, ebitda)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: netinc smoothed by 504d
def f25_growth_vs_cost_netinc_w504_v147_base_signal(netinc) -> pd.Series:
    """Calculates the smoothed netinc over 504 days."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 756d
def f25_growth_vs_cost_revenue_w756_v148_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 756 days."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 1260d
def f25_growth_vs_cost_revenue_capex_ratio_w1260_v149_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 1260 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 63d
def f25_growth_vs_cost_revenue_assets_ratio_w63_v150_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 63 days."""
    ratio = _f25_growth_vs_cost_ratio(revenue, assets)
    res = _sma(ratio, 63)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f25_growth_vs_cost/f25_growth_vs_cost_base_076_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f25_growth_vs_cost_'))]}
F25_GROWTH_VS_COST_REGISTRY_BASE = REGISTRY
