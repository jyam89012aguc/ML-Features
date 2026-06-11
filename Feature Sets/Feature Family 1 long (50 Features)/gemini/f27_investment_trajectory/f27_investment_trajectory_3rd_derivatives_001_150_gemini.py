import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f27it_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f27it_diff(a, b):
    return a - b

def _f27it_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _f27it_jerk(s, jw):
    return s.diff(jw)

def _f27it_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Jerk feature: investments smoothed by 126d, slope 63d, jerk 21d
def f27it_investments_w126_sw63_jw21_v001_jerk_signal(investments) -> pd.Series:
    """Calculates the jerk of smoothed investments."""
    base = _sma(investments, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_investments_capex_ratio_w252_sw21_jw5_v002_jerk_signal(investments, capex) -> pd.Series:
    """Calculates the jerk of the ratio of investments to capex smoothed."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_investments_revenue_ratio_w63_sw63_jw21_v003_jerk_signal(investments, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of investments to revenue smoothed."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_investments_assets_ratio_w126_sw21_jw5_v004_jerk_signal(investments, assets) -> pd.Series:
    """Calculates the jerk of the ratio of investments to assets smoothed."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_investments_cash_ratio_w252_sw63_jw21_v005_jerk_signal(investments, cash) -> pd.Series:
    """Calculates the jerk of the ratio of investments to cash smoothed."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_investments_debt_ratio_w63_sw21_jw5_v006_jerk_signal(investments, debt) -> pd.Series:
    """Calculates the jerk of the ratio of investments to debt smoothed."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_capex_investments_ratio_w126_sw63_jw21_v007_jerk_signal(capex, investments) -> pd.Series:
    """Calculates the jerk of the ratio of capex to investments smoothed."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: capex smoothed by 252d, slope 21d, jerk 5d
def f27it_capex_w252_sw21_jw5_v008_jerk_signal(capex) -> pd.Series:
    """Calculates the jerk of smoothed capex."""
    base = _sma(capex, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_capex_revenue_ratio_w63_sw63_jw21_v009_jerk_signal(capex, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of capex to revenue smoothed."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_capex_assets_ratio_w126_sw21_jw5_v010_jerk_signal(capex, assets) -> pd.Series:
    """Calculates the jerk of the ratio of capex to assets smoothed."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_capex_cash_ratio_w252_sw63_jw21_v011_jerk_signal(capex, cash) -> pd.Series:
    """Calculates the jerk of the ratio of capex to cash smoothed."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_capex_debt_ratio_w63_sw21_jw5_v012_jerk_signal(capex, debt) -> pd.Series:
    """Calculates the jerk of the ratio of capex to debt smoothed."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_revenue_investments_ratio_w126_sw63_jw21_v013_jerk_signal(revenue, investments) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to investments smoothed."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_revenue_capex_ratio_w252_sw21_jw5_v014_jerk_signal(revenue, capex) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to capex smoothed."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_revenue_w63_sw63_jw21_v015_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_revenue_assets_ratio_w126_sw21_jw5_v016_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_revenue_cash_ratio_w252_sw63_jw21_v017_jerk_signal(revenue, cash) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to cash smoothed."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_revenue_debt_ratio_w63_sw21_jw5_v018_jerk_signal(revenue, debt) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to debt smoothed."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_assets_investments_ratio_w126_sw63_jw21_v019_jerk_signal(assets, investments) -> pd.Series:
    """Calculates the jerk of the ratio of assets to investments smoothed."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_assets_capex_ratio_w252_sw21_jw5_v020_jerk_signal(assets, capex) -> pd.Series:
    """Calculates the jerk of the ratio of assets to capex smoothed."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_assets_revenue_ratio_w63_sw63_jw21_v021_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 126d, slope 21d, jerk 5d
def f27it_assets_w126_sw21_jw5_v022_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_assets_cash_ratio_w252_sw63_jw21_v023_jerk_signal(assets, cash) -> pd.Series:
    """Calculates the jerk of the ratio of assets to cash smoothed."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_assets_debt_ratio_w63_sw21_jw5_v024_jerk_signal(assets, debt) -> pd.Series:
    """Calculates the jerk of the ratio of assets to debt smoothed."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_cash_investments_ratio_w126_sw63_jw21_v025_jerk_signal(cash, investments) -> pd.Series:
    """Calculates the jerk of the ratio of cash to investments smoothed."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_cash_capex_ratio_w252_sw21_jw5_v026_jerk_signal(cash, capex) -> pd.Series:
    """Calculates the jerk of the ratio of cash to capex smoothed."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_cash_revenue_ratio_w63_sw63_jw21_v027_jerk_signal(cash, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of cash to revenue smoothed."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_cash_assets_ratio_w126_sw21_jw5_v028_jerk_signal(cash, assets) -> pd.Series:
    """Calculates the jerk of the ratio of cash to assets smoothed."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: cash smoothed by 252d, slope 63d, jerk 21d
def f27it_cash_w252_sw63_jw21_v029_jerk_signal(cash) -> pd.Series:
    """Calculates the jerk of smoothed cash."""
    base = _sma(cash, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_cash_debt_ratio_w63_sw21_jw5_v030_jerk_signal(cash, debt) -> pd.Series:
    """Calculates the jerk of the ratio of cash to debt smoothed."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_debt_investments_ratio_w126_sw63_jw21_v031_jerk_signal(debt, investments) -> pd.Series:
    """Calculates the jerk of the ratio of debt to investments smoothed."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_debt_capex_ratio_w252_sw21_jw5_v032_jerk_signal(debt, capex) -> pd.Series:
    """Calculates the jerk of the ratio of debt to capex smoothed."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_debt_revenue_ratio_w63_sw63_jw21_v033_jerk_signal(debt, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of debt to revenue smoothed."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_debt_assets_ratio_w126_sw21_jw5_v034_jerk_signal(debt, assets) -> pd.Series:
    """Calculates the jerk of the ratio of debt to assets smoothed."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_debt_cash_ratio_w252_sw63_jw21_v035_jerk_signal(debt, cash) -> pd.Series:
    """Calculates the jerk of the ratio of debt to cash smoothed."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: debt smoothed by 63d, slope 21d, jerk 5d
def f27it_debt_w63_sw21_jw5_v036_jerk_signal(debt) -> pd.Series:
    """Calculates the jerk of smoothed debt."""
    base = _sma(debt, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: investments smoothed by 126d, slope 63d, jerk 21d
def f27it_investments_w126_sw63_jw21_v037_jerk_signal(investments) -> pd.Series:
    """Calculates the jerk of smoothed investments."""
    base = _sma(investments, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_investments_capex_ratio_w252_sw21_jw5_v038_jerk_signal(investments, capex) -> pd.Series:
    """Calculates the jerk of the ratio of investments to capex smoothed."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_investments_revenue_ratio_w63_sw63_jw21_v039_jerk_signal(investments, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of investments to revenue smoothed."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_investments_assets_ratio_w126_sw21_jw5_v040_jerk_signal(investments, assets) -> pd.Series:
    """Calculates the jerk of the ratio of investments to assets smoothed."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_investments_cash_ratio_w252_sw63_jw21_v041_jerk_signal(investments, cash) -> pd.Series:
    """Calculates the jerk of the ratio of investments to cash smoothed."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_investments_debt_ratio_w63_sw21_jw5_v042_jerk_signal(investments, debt) -> pd.Series:
    """Calculates the jerk of the ratio of investments to debt smoothed."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_capex_investments_ratio_w126_sw63_jw21_v043_jerk_signal(capex, investments) -> pd.Series:
    """Calculates the jerk of the ratio of capex to investments smoothed."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: capex smoothed by 252d, slope 21d, jerk 5d
def f27it_capex_w252_sw21_jw5_v044_jerk_signal(capex) -> pd.Series:
    """Calculates the jerk of smoothed capex."""
    base = _sma(capex, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_capex_revenue_ratio_w63_sw63_jw21_v045_jerk_signal(capex, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of capex to revenue smoothed."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_capex_assets_ratio_w126_sw21_jw5_v046_jerk_signal(capex, assets) -> pd.Series:
    """Calculates the jerk of the ratio of capex to assets smoothed."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_capex_cash_ratio_w252_sw63_jw21_v047_jerk_signal(capex, cash) -> pd.Series:
    """Calculates the jerk of the ratio of capex to cash smoothed."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_capex_debt_ratio_w63_sw21_jw5_v048_jerk_signal(capex, debt) -> pd.Series:
    """Calculates the jerk of the ratio of capex to debt smoothed."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_revenue_investments_ratio_w126_sw63_jw21_v049_jerk_signal(revenue, investments) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to investments smoothed."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_revenue_capex_ratio_w252_sw21_jw5_v050_jerk_signal(revenue, capex) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to capex smoothed."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_revenue_w63_sw63_jw21_v051_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_revenue_assets_ratio_w126_sw21_jw5_v052_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_revenue_cash_ratio_w252_sw63_jw21_v053_jerk_signal(revenue, cash) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to cash smoothed."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_revenue_debt_ratio_w63_sw21_jw5_v054_jerk_signal(revenue, debt) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to debt smoothed."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_assets_investments_ratio_w126_sw63_jw21_v055_jerk_signal(assets, investments) -> pd.Series:
    """Calculates the jerk of the ratio of assets to investments smoothed."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_assets_capex_ratio_w252_sw21_jw5_v056_jerk_signal(assets, capex) -> pd.Series:
    """Calculates the jerk of the ratio of assets to capex smoothed."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_assets_revenue_ratio_w63_sw63_jw21_v057_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 126d, slope 21d, jerk 5d
def f27it_assets_w126_sw21_jw5_v058_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_assets_cash_ratio_w252_sw63_jw21_v059_jerk_signal(assets, cash) -> pd.Series:
    """Calculates the jerk of the ratio of assets to cash smoothed."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_assets_debt_ratio_w63_sw21_jw5_v060_jerk_signal(assets, debt) -> pd.Series:
    """Calculates the jerk of the ratio of assets to debt smoothed."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_cash_investments_ratio_w126_sw63_jw21_v061_jerk_signal(cash, investments) -> pd.Series:
    """Calculates the jerk of the ratio of cash to investments smoothed."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_cash_capex_ratio_w252_sw21_jw5_v062_jerk_signal(cash, capex) -> pd.Series:
    """Calculates the jerk of the ratio of cash to capex smoothed."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_cash_revenue_ratio_w63_sw63_jw21_v063_jerk_signal(cash, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of cash to revenue smoothed."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_cash_assets_ratio_w126_sw21_jw5_v064_jerk_signal(cash, assets) -> pd.Series:
    """Calculates the jerk of the ratio of cash to assets smoothed."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: cash smoothed by 252d, slope 63d, jerk 21d
def f27it_cash_w252_sw63_jw21_v065_jerk_signal(cash) -> pd.Series:
    """Calculates the jerk of smoothed cash."""
    base = _sma(cash, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_cash_debt_ratio_w63_sw21_jw5_v066_jerk_signal(cash, debt) -> pd.Series:
    """Calculates the jerk of the ratio of cash to debt smoothed."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_debt_investments_ratio_w126_sw63_jw21_v067_jerk_signal(debt, investments) -> pd.Series:
    """Calculates the jerk of the ratio of debt to investments smoothed."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_debt_capex_ratio_w252_sw21_jw5_v068_jerk_signal(debt, capex) -> pd.Series:
    """Calculates the jerk of the ratio of debt to capex smoothed."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_debt_revenue_ratio_w63_sw63_jw21_v069_jerk_signal(debt, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of debt to revenue smoothed."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_debt_assets_ratio_w126_sw21_jw5_v070_jerk_signal(debt, assets) -> pd.Series:
    """Calculates the jerk of the ratio of debt to assets smoothed."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_debt_cash_ratio_w252_sw63_jw21_v071_jerk_signal(debt, cash) -> pd.Series:
    """Calculates the jerk of the ratio of debt to cash smoothed."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: debt smoothed by 63d, slope 21d, jerk 5d
def f27it_debt_w63_sw21_jw5_v072_jerk_signal(debt) -> pd.Series:
    """Calculates the jerk of smoothed debt."""
    base = _sma(debt, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: investments smoothed by 126d, slope 63d, jerk 21d
def f27it_investments_w126_sw63_jw21_v073_jerk_signal(investments) -> pd.Series:
    """Calculates the jerk of smoothed investments."""
    base = _sma(investments, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_investments_capex_ratio_w252_sw21_jw5_v074_jerk_signal(investments, capex) -> pd.Series:
    """Calculates the jerk of the ratio of investments to capex smoothed."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_investments_revenue_ratio_w63_sw63_jw21_v075_jerk_signal(investments, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of investments to revenue smoothed."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_investments_assets_ratio_w126_sw21_jw5_v076_jerk_signal(investments, assets) -> pd.Series:
    """Calculates the jerk of the ratio of investments to assets smoothed."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_investments_cash_ratio_w252_sw63_jw21_v077_jerk_signal(investments, cash) -> pd.Series:
    """Calculates the jerk of the ratio of investments to cash smoothed."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_investments_debt_ratio_w63_sw21_jw5_v078_jerk_signal(investments, debt) -> pd.Series:
    """Calculates the jerk of the ratio of investments to debt smoothed."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_capex_investments_ratio_w126_sw63_jw21_v079_jerk_signal(capex, investments) -> pd.Series:
    """Calculates the jerk of the ratio of capex to investments smoothed."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: capex smoothed by 252d, slope 21d, jerk 5d
def f27it_capex_w252_sw21_jw5_v080_jerk_signal(capex) -> pd.Series:
    """Calculates the jerk of smoothed capex."""
    base = _sma(capex, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_capex_revenue_ratio_w63_sw63_jw21_v081_jerk_signal(capex, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of capex to revenue smoothed."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_capex_assets_ratio_w126_sw21_jw5_v082_jerk_signal(capex, assets) -> pd.Series:
    """Calculates the jerk of the ratio of capex to assets smoothed."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_capex_cash_ratio_w252_sw63_jw21_v083_jerk_signal(capex, cash) -> pd.Series:
    """Calculates the jerk of the ratio of capex to cash smoothed."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_capex_debt_ratio_w63_sw21_jw5_v084_jerk_signal(capex, debt) -> pd.Series:
    """Calculates the jerk of the ratio of capex to debt smoothed."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_revenue_investments_ratio_w126_sw63_jw21_v085_jerk_signal(revenue, investments) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to investments smoothed."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_revenue_capex_ratio_w252_sw21_jw5_v086_jerk_signal(revenue, capex) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to capex smoothed."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_revenue_w63_sw63_jw21_v087_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_revenue_assets_ratio_w126_sw21_jw5_v088_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_revenue_cash_ratio_w252_sw63_jw21_v089_jerk_signal(revenue, cash) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to cash smoothed."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_revenue_debt_ratio_w63_sw21_jw5_v090_jerk_signal(revenue, debt) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to debt smoothed."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_assets_investments_ratio_w126_sw63_jw21_v091_jerk_signal(assets, investments) -> pd.Series:
    """Calculates the jerk of the ratio of assets to investments smoothed."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_assets_capex_ratio_w252_sw21_jw5_v092_jerk_signal(assets, capex) -> pd.Series:
    """Calculates the jerk of the ratio of assets to capex smoothed."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_assets_revenue_ratio_w63_sw63_jw21_v093_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 126d, slope 21d, jerk 5d
def f27it_assets_w126_sw21_jw5_v094_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_assets_cash_ratio_w252_sw63_jw21_v095_jerk_signal(assets, cash) -> pd.Series:
    """Calculates the jerk of the ratio of assets to cash smoothed."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_assets_debt_ratio_w63_sw21_jw5_v096_jerk_signal(assets, debt) -> pd.Series:
    """Calculates the jerk of the ratio of assets to debt smoothed."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_cash_investments_ratio_w126_sw63_jw21_v097_jerk_signal(cash, investments) -> pd.Series:
    """Calculates the jerk of the ratio of cash to investments smoothed."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_cash_capex_ratio_w252_sw21_jw5_v098_jerk_signal(cash, capex) -> pd.Series:
    """Calculates the jerk of the ratio of cash to capex smoothed."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_cash_revenue_ratio_w63_sw63_jw21_v099_jerk_signal(cash, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of cash to revenue smoothed."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_cash_assets_ratio_w126_sw21_jw5_v100_jerk_signal(cash, assets) -> pd.Series:
    """Calculates the jerk of the ratio of cash to assets smoothed."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: cash smoothed by 252d, slope 63d, jerk 21d
def f27it_cash_w252_sw63_jw21_v101_jerk_signal(cash) -> pd.Series:
    """Calculates the jerk of smoothed cash."""
    base = _sma(cash, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_cash_debt_ratio_w63_sw21_jw5_v102_jerk_signal(cash, debt) -> pd.Series:
    """Calculates the jerk of the ratio of cash to debt smoothed."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_debt_investments_ratio_w126_sw63_jw21_v103_jerk_signal(debt, investments) -> pd.Series:
    """Calculates the jerk of the ratio of debt to investments smoothed."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_debt_capex_ratio_w252_sw21_jw5_v104_jerk_signal(debt, capex) -> pd.Series:
    """Calculates the jerk of the ratio of debt to capex smoothed."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_debt_revenue_ratio_w63_sw63_jw21_v105_jerk_signal(debt, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of debt to revenue smoothed."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_debt_assets_ratio_w126_sw21_jw5_v106_jerk_signal(debt, assets) -> pd.Series:
    """Calculates the jerk of the ratio of debt to assets smoothed."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_debt_cash_ratio_w252_sw63_jw21_v107_jerk_signal(debt, cash) -> pd.Series:
    """Calculates the jerk of the ratio of debt to cash smoothed."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: debt smoothed by 63d, slope 21d, jerk 5d
def f27it_debt_w63_sw21_jw5_v108_jerk_signal(debt) -> pd.Series:
    """Calculates the jerk of smoothed debt."""
    base = _sma(debt, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: investments smoothed by 126d, slope 63d, jerk 21d
def f27it_investments_w126_sw63_jw21_v109_jerk_signal(investments) -> pd.Series:
    """Calculates the jerk of smoothed investments."""
    base = _sma(investments, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_investments_capex_ratio_w252_sw21_jw5_v110_jerk_signal(investments, capex) -> pd.Series:
    """Calculates the jerk of the ratio of investments to capex smoothed."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_investments_revenue_ratio_w63_sw63_jw21_v111_jerk_signal(investments, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of investments to revenue smoothed."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_investments_assets_ratio_w126_sw21_jw5_v112_jerk_signal(investments, assets) -> pd.Series:
    """Calculates the jerk of the ratio of investments to assets smoothed."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_investments_cash_ratio_w252_sw63_jw21_v113_jerk_signal(investments, cash) -> pd.Series:
    """Calculates the jerk of the ratio of investments to cash smoothed."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_investments_debt_ratio_w63_sw21_jw5_v114_jerk_signal(investments, debt) -> pd.Series:
    """Calculates the jerk of the ratio of investments to debt smoothed."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_capex_investments_ratio_w126_sw63_jw21_v115_jerk_signal(capex, investments) -> pd.Series:
    """Calculates the jerk of the ratio of capex to investments smoothed."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: capex smoothed by 252d, slope 21d, jerk 5d
def f27it_capex_w252_sw21_jw5_v116_jerk_signal(capex) -> pd.Series:
    """Calculates the jerk of smoothed capex."""
    base = _sma(capex, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_capex_revenue_ratio_w63_sw63_jw21_v117_jerk_signal(capex, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of capex to revenue smoothed."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_capex_assets_ratio_w126_sw21_jw5_v118_jerk_signal(capex, assets) -> pd.Series:
    """Calculates the jerk of the ratio of capex to assets smoothed."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_capex_cash_ratio_w252_sw63_jw21_v119_jerk_signal(capex, cash) -> pd.Series:
    """Calculates the jerk of the ratio of capex to cash smoothed."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of capex to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_capex_debt_ratio_w63_sw21_jw5_v120_jerk_signal(capex, debt) -> pd.Series:
    """Calculates the jerk of the ratio of capex to debt smoothed."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_revenue_investments_ratio_w126_sw63_jw21_v121_jerk_signal(revenue, investments) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to investments smoothed."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_revenue_capex_ratio_w252_sw21_jw5_v122_jerk_signal(revenue, capex) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to capex smoothed."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_revenue_w63_sw63_jw21_v123_jerk_signal(revenue) -> pd.Series:
    """Calculates the jerk of smoothed revenue."""
    base = _sma(revenue, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_revenue_assets_ratio_w126_sw21_jw5_v124_jerk_signal(revenue, assets) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to assets smoothed."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_revenue_cash_ratio_w252_sw63_jw21_v125_jerk_signal(revenue, cash) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to cash smoothed."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of revenue to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_revenue_debt_ratio_w63_sw21_jw5_v126_jerk_signal(revenue, debt) -> pd.Series:
    """Calculates the jerk of the ratio of revenue to debt smoothed."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_assets_investments_ratio_w126_sw63_jw21_v127_jerk_signal(assets, investments) -> pd.Series:
    """Calculates the jerk of the ratio of assets to investments smoothed."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_assets_capex_ratio_w252_sw21_jw5_v128_jerk_signal(assets, capex) -> pd.Series:
    """Calculates the jerk of the ratio of assets to capex smoothed."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_assets_revenue_ratio_w63_sw63_jw21_v129_jerk_signal(assets, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of assets to revenue smoothed."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: assets smoothed by 126d, slope 21d, jerk 5d
def f27it_assets_w126_sw21_jw5_v130_jerk_signal(assets) -> pd.Series:
    """Calculates the jerk of smoothed assets."""
    base = _sma(assets, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_assets_cash_ratio_w252_sw63_jw21_v131_jerk_signal(assets, cash) -> pd.Series:
    """Calculates the jerk of the ratio of assets to cash smoothed."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of assets to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_assets_debt_ratio_w63_sw21_jw5_v132_jerk_signal(assets, debt) -> pd.Series:
    """Calculates the jerk of the ratio of assets to debt smoothed."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_cash_investments_ratio_w126_sw63_jw21_v133_jerk_signal(cash, investments) -> pd.Series:
    """Calculates the jerk of the ratio of cash to investments smoothed."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_cash_capex_ratio_w252_sw21_jw5_v134_jerk_signal(cash, capex) -> pd.Series:
    """Calculates the jerk of the ratio of cash to capex smoothed."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_cash_revenue_ratio_w63_sw63_jw21_v135_jerk_signal(cash, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of cash to revenue smoothed."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_cash_assets_ratio_w126_sw21_jw5_v136_jerk_signal(cash, assets) -> pd.Series:
    """Calculates the jerk of the ratio of cash to assets smoothed."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: cash smoothed by 252d, slope 63d, jerk 21d
def f27it_cash_w252_sw63_jw21_v137_jerk_signal(cash) -> pd.Series:
    """Calculates the jerk of smoothed cash."""
    base = _sma(cash, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of cash to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_cash_debt_ratio_w63_sw21_jw5_v138_jerk_signal(cash, debt) -> pd.Series:
    """Calculates the jerk of the ratio of cash to debt smoothed."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to investments smoothed by 126d, slope 63d, jerk 21d
def f27it_debt_investments_ratio_w126_sw63_jw21_v139_jerk_signal(debt, investments) -> pd.Series:
    """Calculates the jerk of the ratio of debt to investments smoothed."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_debt_capex_ratio_w252_sw21_jw5_v140_jerk_signal(debt, capex) -> pd.Series:
    """Calculates the jerk of the ratio of debt to capex smoothed."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_debt_revenue_ratio_w63_sw63_jw21_v141_jerk_signal(debt, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of debt to revenue smoothed."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_debt_assets_ratio_w126_sw21_jw5_v142_jerk_signal(debt, assets) -> pd.Series:
    """Calculates the jerk of the ratio of debt to assets smoothed."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of debt to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_debt_cash_ratio_w252_sw63_jw21_v143_jerk_signal(debt, cash) -> pd.Series:
    """Calculates the jerk of the ratio of debt to cash smoothed."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: debt smoothed by 63d, slope 21d, jerk 5d
def f27it_debt_w63_sw21_jw5_v144_jerk_signal(debt) -> pd.Series:
    """Calculates the jerk of smoothed debt."""
    base = _sma(debt, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: investments smoothed by 126d, slope 63d, jerk 21d
def f27it_investments_w126_sw63_jw21_v145_jerk_signal(investments) -> pd.Series:
    """Calculates the jerk of smoothed investments."""
    base = _sma(investments, 126)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to capex smoothed by 252d, slope 21d, jerk 5d
def f27it_investments_capex_ratio_w252_sw21_jw5_v146_jerk_signal(investments, capex) -> pd.Series:
    """Calculates the jerk of the ratio of investments to capex smoothed."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to revenue smoothed by 63d, slope 63d, jerk 21d
def f27it_investments_revenue_ratio_w63_sw63_jw21_v147_jerk_signal(investments, revenue) -> pd.Series:
    """Calculates the jerk of the ratio of investments to revenue smoothed."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to assets smoothed by 126d, slope 21d, jerk 5d
def f27it_investments_assets_ratio_w126_sw21_jw5_v148_jerk_signal(investments, assets) -> pd.Series:
    """Calculates the jerk of the ratio of investments to assets smoothed."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 126)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to cash smoothed by 252d, slope 63d, jerk 21d
def f27it_investments_cash_ratio_w252_sw63_jw21_v149_jerk_signal(investments, cash) -> pd.Series:
    """Calculates the jerk of the ratio of investments to cash smoothed."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 252)
    slope = _f27it_slope(base, 63)
    res = _f27it_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk feature: ratio of investments to debt smoothed by 63d, slope 21d, jerk 5d
def f27it_investments_debt_ratio_w63_sw21_jw5_v150_jerk_signal(investments, debt) -> pd.Series:
    """Calculates the jerk of the ratio of investments to debt smoothed."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 63)
    slope = _f27it_slope(base, 21)
    res = _f27it_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.random.normal(100, 20, n) for col in ['investments', 'capex', 'revenue', 'assets', 'cash', 'debt']})
    for col in ['investments', 'capex', 'revenue', 'assets', 'cash', 'debt']:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f27it_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f27_investment_trajectory/f27it_jerk_001_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f27it_'))]}
f27it_REGISTRY_JERK = REGISTRY

