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

def _f27it_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Slope feature: investments smoothed by 126d, slope over 21d
def f27it_investments_w126_sw21_v001_slope_signal(investments) -> pd.Series:
    """Calculates the slope of smoothed investments over 21 days."""
    base = _sma(investments, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to capex smoothed by 252d, slope over 63d
def f27it_investments_capex_ratio_w252_sw63_v002_slope_signal(investments, capex) -> pd.Series:
    """Calculates the slope of the ratio of investments to capex smoothed over 63 days."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to revenue smoothed by 504d, slope over 5d
def f27it_investments_revenue_ratio_w504_sw5_v003_slope_signal(investments, revenue) -> pd.Series:
    """Calculates the slope of the ratio of investments to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to assets smoothed by 63d, slope over 21d
def f27it_investments_assets_ratio_w63_sw21_v004_slope_signal(investments, assets) -> pd.Series:
    """Calculates the slope of the ratio of investments to assets smoothed over 21 days."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to cash smoothed by 126d, slope over 63d
def f27it_investments_cash_ratio_w126_sw63_v005_slope_signal(investments, cash) -> pd.Series:
    """Calculates the slope of the ratio of investments to cash smoothed over 63 days."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to debt smoothed by 252d, slope over 5d
def f27it_investments_debt_ratio_w252_sw5_v006_slope_signal(investments, debt) -> pd.Series:
    """Calculates the slope of the ratio of investments to debt smoothed over 5 days."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to investments smoothed by 504d, slope over 21d
def f27it_capex_investments_ratio_w504_sw21_v007_slope_signal(capex, investments) -> pd.Series:
    """Calculates the slope of the ratio of capex to investments smoothed over 21 days."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: capex smoothed by 63d, slope over 63d
def f27it_capex_w63_sw63_v008_slope_signal(capex) -> pd.Series:
    """Calculates the slope of smoothed capex over 63 days."""
    base = _sma(capex, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to revenue smoothed by 126d, slope over 5d
def f27it_capex_revenue_ratio_w126_sw5_v009_slope_signal(capex, revenue) -> pd.Series:
    """Calculates the slope of the ratio of capex to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to assets smoothed by 252d, slope over 21d
def f27it_capex_assets_ratio_w252_sw21_v010_slope_signal(capex, assets) -> pd.Series:
    """Calculates the slope of the ratio of capex to assets smoothed over 21 days."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to cash smoothed by 504d, slope over 63d
def f27it_capex_cash_ratio_w504_sw63_v011_slope_signal(capex, cash) -> pd.Series:
    """Calculates the slope of the ratio of capex to cash smoothed over 63 days."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to debt smoothed by 63d, slope over 5d
def f27it_capex_debt_ratio_w63_sw5_v012_slope_signal(capex, debt) -> pd.Series:
    """Calculates the slope of the ratio of capex to debt smoothed over 5 days."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to investments smoothed by 126d, slope over 21d
def f27it_revenue_investments_ratio_w126_sw21_v013_slope_signal(revenue, investments) -> pd.Series:
    """Calculates the slope of the ratio of revenue to investments smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to capex smoothed by 252d, slope over 63d
def f27it_revenue_capex_ratio_w252_sw63_v014_slope_signal(revenue, capex) -> pd.Series:
    """Calculates the slope of the ratio of revenue to capex smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f27it_revenue_w504_sw5_v015_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 63d, slope over 21d
def f27it_revenue_assets_ratio_w63_sw21_v016_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to cash smoothed by 126d, slope over 63d
def f27it_revenue_cash_ratio_w126_sw63_v017_slope_signal(revenue, cash) -> pd.Series:
    """Calculates the slope of the ratio of revenue to cash smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to debt smoothed by 252d, slope over 5d
def f27it_revenue_debt_ratio_w252_sw5_v018_slope_signal(revenue, debt) -> pd.Series:
    """Calculates the slope of the ratio of revenue to debt smoothed over 5 days."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to investments smoothed by 504d, slope over 21d
def f27it_assets_investments_ratio_w504_sw21_v019_slope_signal(assets, investments) -> pd.Series:
    """Calculates the slope of the ratio of assets to investments smoothed over 21 days."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to capex smoothed by 63d, slope over 63d
def f27it_assets_capex_ratio_w63_sw63_v020_slope_signal(assets, capex) -> pd.Series:
    """Calculates the slope of the ratio of assets to capex smoothed over 63 days."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f27it_assets_revenue_ratio_w126_sw5_v021_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f27it_assets_w252_sw21_v022_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to cash smoothed by 504d, slope over 63d
def f27it_assets_cash_ratio_w504_sw63_v023_slope_signal(assets, cash) -> pd.Series:
    """Calculates the slope of the ratio of assets to cash smoothed over 63 days."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to debt smoothed by 63d, slope over 5d
def f27it_assets_debt_ratio_w63_sw5_v024_slope_signal(assets, debt) -> pd.Series:
    """Calculates the slope of the ratio of assets to debt smoothed over 5 days."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to investments smoothed by 126d, slope over 21d
def f27it_cash_investments_ratio_w126_sw21_v025_slope_signal(cash, investments) -> pd.Series:
    """Calculates the slope of the ratio of cash to investments smoothed over 21 days."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to capex smoothed by 252d, slope over 63d
def f27it_cash_capex_ratio_w252_sw63_v026_slope_signal(cash, capex) -> pd.Series:
    """Calculates the slope of the ratio of cash to capex smoothed over 63 days."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to revenue smoothed by 504d, slope over 5d
def f27it_cash_revenue_ratio_w504_sw5_v027_slope_signal(cash, revenue) -> pd.Series:
    """Calculates the slope of the ratio of cash to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to assets smoothed by 63d, slope over 21d
def f27it_cash_assets_ratio_w63_sw21_v028_slope_signal(cash, assets) -> pd.Series:
    """Calculates the slope of the ratio of cash to assets smoothed over 21 days."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: cash smoothed by 126d, slope over 63d
def f27it_cash_w126_sw63_v029_slope_signal(cash) -> pd.Series:
    """Calculates the slope of smoothed cash over 63 days."""
    base = _sma(cash, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to debt smoothed by 252d, slope over 5d
def f27it_cash_debt_ratio_w252_sw5_v030_slope_signal(cash, debt) -> pd.Series:
    """Calculates the slope of the ratio of cash to debt smoothed over 5 days."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to investments smoothed by 504d, slope over 21d
def f27it_debt_investments_ratio_w504_sw21_v031_slope_signal(debt, investments) -> pd.Series:
    """Calculates the slope of the ratio of debt to investments smoothed over 21 days."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to capex smoothed by 63d, slope over 63d
def f27it_debt_capex_ratio_w63_sw63_v032_slope_signal(debt, capex) -> pd.Series:
    """Calculates the slope of the ratio of debt to capex smoothed over 63 days."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to revenue smoothed by 126d, slope over 5d
def f27it_debt_revenue_ratio_w126_sw5_v033_slope_signal(debt, revenue) -> pd.Series:
    """Calculates the slope of the ratio of debt to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to assets smoothed by 252d, slope over 21d
def f27it_debt_assets_ratio_w252_sw21_v034_slope_signal(debt, assets) -> pd.Series:
    """Calculates the slope of the ratio of debt to assets smoothed over 21 days."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to cash smoothed by 504d, slope over 63d
def f27it_debt_cash_ratio_w504_sw63_v035_slope_signal(debt, cash) -> pd.Series:
    """Calculates the slope of the ratio of debt to cash smoothed over 63 days."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: debt smoothed by 63d, slope over 5d
def f27it_debt_w63_sw5_v036_slope_signal(debt) -> pd.Series:
    """Calculates the slope of smoothed debt over 5 days."""
    base = _sma(debt, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: investments smoothed by 126d, slope over 21d
def f27it_investments_w126_sw21_v037_slope_signal(investments) -> pd.Series:
    """Calculates the slope of smoothed investments over 21 days."""
    base = _sma(investments, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to capex smoothed by 252d, slope over 63d
def f27it_investments_capex_ratio_w252_sw63_v038_slope_signal(investments, capex) -> pd.Series:
    """Calculates the slope of the ratio of investments to capex smoothed over 63 days."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to revenue smoothed by 504d, slope over 5d
def f27it_investments_revenue_ratio_w504_sw5_v039_slope_signal(investments, revenue) -> pd.Series:
    """Calculates the slope of the ratio of investments to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to assets smoothed by 63d, slope over 21d
def f27it_investments_assets_ratio_w63_sw21_v040_slope_signal(investments, assets) -> pd.Series:
    """Calculates the slope of the ratio of investments to assets smoothed over 21 days."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to cash smoothed by 126d, slope over 63d
def f27it_investments_cash_ratio_w126_sw63_v041_slope_signal(investments, cash) -> pd.Series:
    """Calculates the slope of the ratio of investments to cash smoothed over 63 days."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to debt smoothed by 252d, slope over 5d
def f27it_investments_debt_ratio_w252_sw5_v042_slope_signal(investments, debt) -> pd.Series:
    """Calculates the slope of the ratio of investments to debt smoothed over 5 days."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to investments smoothed by 504d, slope over 21d
def f27it_capex_investments_ratio_w504_sw21_v043_slope_signal(capex, investments) -> pd.Series:
    """Calculates the slope of the ratio of capex to investments smoothed over 21 days."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: capex smoothed by 63d, slope over 63d
def f27it_capex_w63_sw63_v044_slope_signal(capex) -> pd.Series:
    """Calculates the slope of smoothed capex over 63 days."""
    base = _sma(capex, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to revenue smoothed by 126d, slope over 5d
def f27it_capex_revenue_ratio_w126_sw5_v045_slope_signal(capex, revenue) -> pd.Series:
    """Calculates the slope of the ratio of capex to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to assets smoothed by 252d, slope over 21d
def f27it_capex_assets_ratio_w252_sw21_v046_slope_signal(capex, assets) -> pd.Series:
    """Calculates the slope of the ratio of capex to assets smoothed over 21 days."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to cash smoothed by 504d, slope over 63d
def f27it_capex_cash_ratio_w504_sw63_v047_slope_signal(capex, cash) -> pd.Series:
    """Calculates the slope of the ratio of capex to cash smoothed over 63 days."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to debt smoothed by 63d, slope over 5d
def f27it_capex_debt_ratio_w63_sw5_v048_slope_signal(capex, debt) -> pd.Series:
    """Calculates the slope of the ratio of capex to debt smoothed over 5 days."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to investments smoothed by 126d, slope over 21d
def f27it_revenue_investments_ratio_w126_sw21_v049_slope_signal(revenue, investments) -> pd.Series:
    """Calculates the slope of the ratio of revenue to investments smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to capex smoothed by 252d, slope over 63d
def f27it_revenue_capex_ratio_w252_sw63_v050_slope_signal(revenue, capex) -> pd.Series:
    """Calculates the slope of the ratio of revenue to capex smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f27it_revenue_w504_sw5_v051_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 63d, slope over 21d
def f27it_revenue_assets_ratio_w63_sw21_v052_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to cash smoothed by 126d, slope over 63d
def f27it_revenue_cash_ratio_w126_sw63_v053_slope_signal(revenue, cash) -> pd.Series:
    """Calculates the slope of the ratio of revenue to cash smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to debt smoothed by 252d, slope over 5d
def f27it_revenue_debt_ratio_w252_sw5_v054_slope_signal(revenue, debt) -> pd.Series:
    """Calculates the slope of the ratio of revenue to debt smoothed over 5 days."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to investments smoothed by 504d, slope over 21d
def f27it_assets_investments_ratio_w504_sw21_v055_slope_signal(assets, investments) -> pd.Series:
    """Calculates the slope of the ratio of assets to investments smoothed over 21 days."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to capex smoothed by 63d, slope over 63d
def f27it_assets_capex_ratio_w63_sw63_v056_slope_signal(assets, capex) -> pd.Series:
    """Calculates the slope of the ratio of assets to capex smoothed over 63 days."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f27it_assets_revenue_ratio_w126_sw5_v057_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f27it_assets_w252_sw21_v058_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to cash smoothed by 504d, slope over 63d
def f27it_assets_cash_ratio_w504_sw63_v059_slope_signal(assets, cash) -> pd.Series:
    """Calculates the slope of the ratio of assets to cash smoothed over 63 days."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to debt smoothed by 63d, slope over 5d
def f27it_assets_debt_ratio_w63_sw5_v060_slope_signal(assets, debt) -> pd.Series:
    """Calculates the slope of the ratio of assets to debt smoothed over 5 days."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to investments smoothed by 126d, slope over 21d
def f27it_cash_investments_ratio_w126_sw21_v061_slope_signal(cash, investments) -> pd.Series:
    """Calculates the slope of the ratio of cash to investments smoothed over 21 days."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to capex smoothed by 252d, slope over 63d
def f27it_cash_capex_ratio_w252_sw63_v062_slope_signal(cash, capex) -> pd.Series:
    """Calculates the slope of the ratio of cash to capex smoothed over 63 days."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to revenue smoothed by 504d, slope over 5d
def f27it_cash_revenue_ratio_w504_sw5_v063_slope_signal(cash, revenue) -> pd.Series:
    """Calculates the slope of the ratio of cash to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to assets smoothed by 63d, slope over 21d
def f27it_cash_assets_ratio_w63_sw21_v064_slope_signal(cash, assets) -> pd.Series:
    """Calculates the slope of the ratio of cash to assets smoothed over 21 days."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: cash smoothed by 126d, slope over 63d
def f27it_cash_w126_sw63_v065_slope_signal(cash) -> pd.Series:
    """Calculates the slope of smoothed cash over 63 days."""
    base = _sma(cash, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to debt smoothed by 252d, slope over 5d
def f27it_cash_debt_ratio_w252_sw5_v066_slope_signal(cash, debt) -> pd.Series:
    """Calculates the slope of the ratio of cash to debt smoothed over 5 days."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to investments smoothed by 504d, slope over 21d
def f27it_debt_investments_ratio_w504_sw21_v067_slope_signal(debt, investments) -> pd.Series:
    """Calculates the slope of the ratio of debt to investments smoothed over 21 days."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to capex smoothed by 63d, slope over 63d
def f27it_debt_capex_ratio_w63_sw63_v068_slope_signal(debt, capex) -> pd.Series:
    """Calculates the slope of the ratio of debt to capex smoothed over 63 days."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to revenue smoothed by 126d, slope over 5d
def f27it_debt_revenue_ratio_w126_sw5_v069_slope_signal(debt, revenue) -> pd.Series:
    """Calculates the slope of the ratio of debt to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to assets smoothed by 252d, slope over 21d
def f27it_debt_assets_ratio_w252_sw21_v070_slope_signal(debt, assets) -> pd.Series:
    """Calculates the slope of the ratio of debt to assets smoothed over 21 days."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to cash smoothed by 504d, slope over 63d
def f27it_debt_cash_ratio_w504_sw63_v071_slope_signal(debt, cash) -> pd.Series:
    """Calculates the slope of the ratio of debt to cash smoothed over 63 days."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: debt smoothed by 63d, slope over 5d
def f27it_debt_w63_sw5_v072_slope_signal(debt) -> pd.Series:
    """Calculates the slope of smoothed debt over 5 days."""
    base = _sma(debt, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: investments smoothed by 126d, slope over 21d
def f27it_investments_w126_sw21_v073_slope_signal(investments) -> pd.Series:
    """Calculates the slope of smoothed investments over 21 days."""
    base = _sma(investments, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to capex smoothed by 252d, slope over 63d
def f27it_investments_capex_ratio_w252_sw63_v074_slope_signal(investments, capex) -> pd.Series:
    """Calculates the slope of the ratio of investments to capex smoothed over 63 days."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to revenue smoothed by 504d, slope over 5d
def f27it_investments_revenue_ratio_w504_sw5_v075_slope_signal(investments, revenue) -> pd.Series:
    """Calculates the slope of the ratio of investments to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to assets smoothed by 63d, slope over 21d
def f27it_investments_assets_ratio_w63_sw21_v076_slope_signal(investments, assets) -> pd.Series:
    """Calculates the slope of the ratio of investments to assets smoothed over 21 days."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to cash smoothed by 126d, slope over 63d
def f27it_investments_cash_ratio_w126_sw63_v077_slope_signal(investments, cash) -> pd.Series:
    """Calculates the slope of the ratio of investments to cash smoothed over 63 days."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to debt smoothed by 252d, slope over 5d
def f27it_investments_debt_ratio_w252_sw5_v078_slope_signal(investments, debt) -> pd.Series:
    """Calculates the slope of the ratio of investments to debt smoothed over 5 days."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to investments smoothed by 504d, slope over 21d
def f27it_capex_investments_ratio_w504_sw21_v079_slope_signal(capex, investments) -> pd.Series:
    """Calculates the slope of the ratio of capex to investments smoothed over 21 days."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: capex smoothed by 63d, slope over 63d
def f27it_capex_w63_sw63_v080_slope_signal(capex) -> pd.Series:
    """Calculates the slope of smoothed capex over 63 days."""
    base = _sma(capex, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to revenue smoothed by 126d, slope over 5d
def f27it_capex_revenue_ratio_w126_sw5_v081_slope_signal(capex, revenue) -> pd.Series:
    """Calculates the slope of the ratio of capex to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to assets smoothed by 252d, slope over 21d
def f27it_capex_assets_ratio_w252_sw21_v082_slope_signal(capex, assets) -> pd.Series:
    """Calculates the slope of the ratio of capex to assets smoothed over 21 days."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to cash smoothed by 504d, slope over 63d
def f27it_capex_cash_ratio_w504_sw63_v083_slope_signal(capex, cash) -> pd.Series:
    """Calculates the slope of the ratio of capex to cash smoothed over 63 days."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to debt smoothed by 63d, slope over 5d
def f27it_capex_debt_ratio_w63_sw5_v084_slope_signal(capex, debt) -> pd.Series:
    """Calculates the slope of the ratio of capex to debt smoothed over 5 days."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to investments smoothed by 126d, slope over 21d
def f27it_revenue_investments_ratio_w126_sw21_v085_slope_signal(revenue, investments) -> pd.Series:
    """Calculates the slope of the ratio of revenue to investments smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to capex smoothed by 252d, slope over 63d
def f27it_revenue_capex_ratio_w252_sw63_v086_slope_signal(revenue, capex) -> pd.Series:
    """Calculates the slope of the ratio of revenue to capex smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f27it_revenue_w504_sw5_v087_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 63d, slope over 21d
def f27it_revenue_assets_ratio_w63_sw21_v088_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to cash smoothed by 126d, slope over 63d
def f27it_revenue_cash_ratio_w126_sw63_v089_slope_signal(revenue, cash) -> pd.Series:
    """Calculates the slope of the ratio of revenue to cash smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to debt smoothed by 252d, slope over 5d
def f27it_revenue_debt_ratio_w252_sw5_v090_slope_signal(revenue, debt) -> pd.Series:
    """Calculates the slope of the ratio of revenue to debt smoothed over 5 days."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to investments smoothed by 504d, slope over 21d
def f27it_assets_investments_ratio_w504_sw21_v091_slope_signal(assets, investments) -> pd.Series:
    """Calculates the slope of the ratio of assets to investments smoothed over 21 days."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to capex smoothed by 63d, slope over 63d
def f27it_assets_capex_ratio_w63_sw63_v092_slope_signal(assets, capex) -> pd.Series:
    """Calculates the slope of the ratio of assets to capex smoothed over 63 days."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f27it_assets_revenue_ratio_w126_sw5_v093_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f27it_assets_w252_sw21_v094_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to cash smoothed by 504d, slope over 63d
def f27it_assets_cash_ratio_w504_sw63_v095_slope_signal(assets, cash) -> pd.Series:
    """Calculates the slope of the ratio of assets to cash smoothed over 63 days."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to debt smoothed by 63d, slope over 5d
def f27it_assets_debt_ratio_w63_sw5_v096_slope_signal(assets, debt) -> pd.Series:
    """Calculates the slope of the ratio of assets to debt smoothed over 5 days."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to investments smoothed by 126d, slope over 21d
def f27it_cash_investments_ratio_w126_sw21_v097_slope_signal(cash, investments) -> pd.Series:
    """Calculates the slope of the ratio of cash to investments smoothed over 21 days."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to capex smoothed by 252d, slope over 63d
def f27it_cash_capex_ratio_w252_sw63_v098_slope_signal(cash, capex) -> pd.Series:
    """Calculates the slope of the ratio of cash to capex smoothed over 63 days."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to revenue smoothed by 504d, slope over 5d
def f27it_cash_revenue_ratio_w504_sw5_v099_slope_signal(cash, revenue) -> pd.Series:
    """Calculates the slope of the ratio of cash to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to assets smoothed by 63d, slope over 21d
def f27it_cash_assets_ratio_w63_sw21_v100_slope_signal(cash, assets) -> pd.Series:
    """Calculates the slope of the ratio of cash to assets smoothed over 21 days."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: cash smoothed by 126d, slope over 63d
def f27it_cash_w126_sw63_v101_slope_signal(cash) -> pd.Series:
    """Calculates the slope of smoothed cash over 63 days."""
    base = _sma(cash, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to debt smoothed by 252d, slope over 5d
def f27it_cash_debt_ratio_w252_sw5_v102_slope_signal(cash, debt) -> pd.Series:
    """Calculates the slope of the ratio of cash to debt smoothed over 5 days."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to investments smoothed by 504d, slope over 21d
def f27it_debt_investments_ratio_w504_sw21_v103_slope_signal(debt, investments) -> pd.Series:
    """Calculates the slope of the ratio of debt to investments smoothed over 21 days."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to capex smoothed by 63d, slope over 63d
def f27it_debt_capex_ratio_w63_sw63_v104_slope_signal(debt, capex) -> pd.Series:
    """Calculates the slope of the ratio of debt to capex smoothed over 63 days."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to revenue smoothed by 126d, slope over 5d
def f27it_debt_revenue_ratio_w126_sw5_v105_slope_signal(debt, revenue) -> pd.Series:
    """Calculates the slope of the ratio of debt to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to assets smoothed by 252d, slope over 21d
def f27it_debt_assets_ratio_w252_sw21_v106_slope_signal(debt, assets) -> pd.Series:
    """Calculates the slope of the ratio of debt to assets smoothed over 21 days."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to cash smoothed by 504d, slope over 63d
def f27it_debt_cash_ratio_w504_sw63_v107_slope_signal(debt, cash) -> pd.Series:
    """Calculates the slope of the ratio of debt to cash smoothed over 63 days."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: debt smoothed by 63d, slope over 5d
def f27it_debt_w63_sw5_v108_slope_signal(debt) -> pd.Series:
    """Calculates the slope of smoothed debt over 5 days."""
    base = _sma(debt, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: investments smoothed by 126d, slope over 21d
def f27it_investments_w126_sw21_v109_slope_signal(investments) -> pd.Series:
    """Calculates the slope of smoothed investments over 21 days."""
    base = _sma(investments, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to capex smoothed by 252d, slope over 63d
def f27it_investments_capex_ratio_w252_sw63_v110_slope_signal(investments, capex) -> pd.Series:
    """Calculates the slope of the ratio of investments to capex smoothed over 63 days."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to revenue smoothed by 504d, slope over 5d
def f27it_investments_revenue_ratio_w504_sw5_v111_slope_signal(investments, revenue) -> pd.Series:
    """Calculates the slope of the ratio of investments to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to assets smoothed by 63d, slope over 21d
def f27it_investments_assets_ratio_w63_sw21_v112_slope_signal(investments, assets) -> pd.Series:
    """Calculates the slope of the ratio of investments to assets smoothed over 21 days."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to cash smoothed by 126d, slope over 63d
def f27it_investments_cash_ratio_w126_sw63_v113_slope_signal(investments, cash) -> pd.Series:
    """Calculates the slope of the ratio of investments to cash smoothed over 63 days."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to debt smoothed by 252d, slope over 5d
def f27it_investments_debt_ratio_w252_sw5_v114_slope_signal(investments, debt) -> pd.Series:
    """Calculates the slope of the ratio of investments to debt smoothed over 5 days."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to investments smoothed by 504d, slope over 21d
def f27it_capex_investments_ratio_w504_sw21_v115_slope_signal(capex, investments) -> pd.Series:
    """Calculates the slope of the ratio of capex to investments smoothed over 21 days."""
    ratio = _f27it_ratio(capex, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: capex smoothed by 63d, slope over 63d
def f27it_capex_w63_sw63_v116_slope_signal(capex) -> pd.Series:
    """Calculates the slope of smoothed capex over 63 days."""
    base = _sma(capex, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to revenue smoothed by 126d, slope over 5d
def f27it_capex_revenue_ratio_w126_sw5_v117_slope_signal(capex, revenue) -> pd.Series:
    """Calculates the slope of the ratio of capex to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(capex, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to assets smoothed by 252d, slope over 21d
def f27it_capex_assets_ratio_w252_sw21_v118_slope_signal(capex, assets) -> pd.Series:
    """Calculates the slope of the ratio of capex to assets smoothed over 21 days."""
    ratio = _f27it_ratio(capex, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to cash smoothed by 504d, slope over 63d
def f27it_capex_cash_ratio_w504_sw63_v119_slope_signal(capex, cash) -> pd.Series:
    """Calculates the slope of the ratio of capex to cash smoothed over 63 days."""
    ratio = _f27it_ratio(capex, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of capex to debt smoothed by 63d, slope over 5d
def f27it_capex_debt_ratio_w63_sw5_v120_slope_signal(capex, debt) -> pd.Series:
    """Calculates the slope of the ratio of capex to debt smoothed over 5 days."""
    ratio = _f27it_ratio(capex, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to investments smoothed by 126d, slope over 21d
def f27it_revenue_investments_ratio_w126_sw21_v121_slope_signal(revenue, investments) -> pd.Series:
    """Calculates the slope of the ratio of revenue to investments smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to capex smoothed by 252d, slope over 63d
def f27it_revenue_capex_ratio_w252_sw63_v122_slope_signal(revenue, capex) -> pd.Series:
    """Calculates the slope of the ratio of revenue to capex smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: revenue smoothed by 504d, slope over 5d
def f27it_revenue_w504_sw5_v123_slope_signal(revenue) -> pd.Series:
    """Calculates the slope of smoothed revenue over 5 days."""
    base = _sma(revenue, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to assets smoothed by 63d, slope over 21d
def f27it_revenue_assets_ratio_w63_sw21_v124_slope_signal(revenue, assets) -> pd.Series:
    """Calculates the slope of the ratio of revenue to assets smoothed over 21 days."""
    ratio = _f27it_ratio(revenue, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to cash smoothed by 126d, slope over 63d
def f27it_revenue_cash_ratio_w126_sw63_v125_slope_signal(revenue, cash) -> pd.Series:
    """Calculates the slope of the ratio of revenue to cash smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of revenue to debt smoothed by 252d, slope over 5d
def f27it_revenue_debt_ratio_w252_sw5_v126_slope_signal(revenue, debt) -> pd.Series:
    """Calculates the slope of the ratio of revenue to debt smoothed over 5 days."""
    ratio = _f27it_ratio(revenue, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to investments smoothed by 504d, slope over 21d
def f27it_assets_investments_ratio_w504_sw21_v127_slope_signal(assets, investments) -> pd.Series:
    """Calculates the slope of the ratio of assets to investments smoothed over 21 days."""
    ratio = _f27it_ratio(assets, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to capex smoothed by 63d, slope over 63d
def f27it_assets_capex_ratio_w63_sw63_v128_slope_signal(assets, capex) -> pd.Series:
    """Calculates the slope of the ratio of assets to capex smoothed over 63 days."""
    ratio = _f27it_ratio(assets, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to revenue smoothed by 126d, slope over 5d
def f27it_assets_revenue_ratio_w126_sw5_v129_slope_signal(assets, revenue) -> pd.Series:
    """Calculates the slope of the ratio of assets to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(assets, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: assets smoothed by 252d, slope over 21d
def f27it_assets_w252_sw21_v130_slope_signal(assets) -> pd.Series:
    """Calculates the slope of smoothed assets over 21 days."""
    base = _sma(assets, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to cash smoothed by 504d, slope over 63d
def f27it_assets_cash_ratio_w504_sw63_v131_slope_signal(assets, cash) -> pd.Series:
    """Calculates the slope of the ratio of assets to cash smoothed over 63 days."""
    ratio = _f27it_ratio(assets, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of assets to debt smoothed by 63d, slope over 5d
def f27it_assets_debt_ratio_w63_sw5_v132_slope_signal(assets, debt) -> pd.Series:
    """Calculates the slope of the ratio of assets to debt smoothed over 5 days."""
    ratio = _f27it_ratio(assets, debt)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to investments smoothed by 126d, slope over 21d
def f27it_cash_investments_ratio_w126_sw21_v133_slope_signal(cash, investments) -> pd.Series:
    """Calculates the slope of the ratio of cash to investments smoothed over 21 days."""
    ratio = _f27it_ratio(cash, investments)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to capex smoothed by 252d, slope over 63d
def f27it_cash_capex_ratio_w252_sw63_v134_slope_signal(cash, capex) -> pd.Series:
    """Calculates the slope of the ratio of cash to capex smoothed over 63 days."""
    ratio = _f27it_ratio(cash, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to revenue smoothed by 504d, slope over 5d
def f27it_cash_revenue_ratio_w504_sw5_v135_slope_signal(cash, revenue) -> pd.Series:
    """Calculates the slope of the ratio of cash to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(cash, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to assets smoothed by 63d, slope over 21d
def f27it_cash_assets_ratio_w63_sw21_v136_slope_signal(cash, assets) -> pd.Series:
    """Calculates the slope of the ratio of cash to assets smoothed over 21 days."""
    ratio = _f27it_ratio(cash, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: cash smoothed by 126d, slope over 63d
def f27it_cash_w126_sw63_v137_slope_signal(cash) -> pd.Series:
    """Calculates the slope of smoothed cash over 63 days."""
    base = _sma(cash, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of cash to debt smoothed by 252d, slope over 5d
def f27it_cash_debt_ratio_w252_sw5_v138_slope_signal(cash, debt) -> pd.Series:
    """Calculates the slope of the ratio of cash to debt smoothed over 5 days."""
    ratio = _f27it_ratio(cash, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to investments smoothed by 504d, slope over 21d
def f27it_debt_investments_ratio_w504_sw21_v139_slope_signal(debt, investments) -> pd.Series:
    """Calculates the slope of the ratio of debt to investments smoothed over 21 days."""
    ratio = _f27it_ratio(debt, investments)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to capex smoothed by 63d, slope over 63d
def f27it_debt_capex_ratio_w63_sw63_v140_slope_signal(debt, capex) -> pd.Series:
    """Calculates the slope of the ratio of debt to capex smoothed over 63 days."""
    ratio = _f27it_ratio(debt, capex)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to revenue smoothed by 126d, slope over 5d
def f27it_debt_revenue_ratio_w126_sw5_v141_slope_signal(debt, revenue) -> pd.Series:
    """Calculates the slope of the ratio of debt to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(debt, revenue)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to assets smoothed by 252d, slope over 21d
def f27it_debt_assets_ratio_w252_sw21_v142_slope_signal(debt, assets) -> pd.Series:
    """Calculates the slope of the ratio of debt to assets smoothed over 21 days."""
    ratio = _f27it_ratio(debt, assets)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of debt to cash smoothed by 504d, slope over 63d
def f27it_debt_cash_ratio_w504_sw63_v143_slope_signal(debt, cash) -> pd.Series:
    """Calculates the slope of the ratio of debt to cash smoothed over 63 days."""
    ratio = _f27it_ratio(debt, cash)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: debt smoothed by 63d, slope over 5d
def f27it_debt_w63_sw5_v144_slope_signal(debt) -> pd.Series:
    """Calculates the slope of smoothed debt over 5 days."""
    base = _sma(debt, 63)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: investments smoothed by 126d, slope over 21d
def f27it_investments_w126_sw21_v145_slope_signal(investments) -> pd.Series:
    """Calculates the slope of smoothed investments over 21 days."""
    base = _sma(investments, 126)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to capex smoothed by 252d, slope over 63d
def f27it_investments_capex_ratio_w252_sw63_v146_slope_signal(investments, capex) -> pd.Series:
    """Calculates the slope of the ratio of investments to capex smoothed over 63 days."""
    ratio = _f27it_ratio(investments, capex)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to revenue smoothed by 504d, slope over 5d
def f27it_investments_revenue_ratio_w504_sw5_v147_slope_signal(investments, revenue) -> pd.Series:
    """Calculates the slope of the ratio of investments to revenue smoothed over 5 days."""
    ratio = _f27it_ratio(investments, revenue)
    base = _sma(ratio, 504)
    res = _f27it_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to assets smoothed by 63d, slope over 21d
def f27it_investments_assets_ratio_w63_sw21_v148_slope_signal(investments, assets) -> pd.Series:
    """Calculates the slope of the ratio of investments to assets smoothed over 21 days."""
    ratio = _f27it_ratio(investments, assets)
    base = _sma(ratio, 63)
    res = _f27it_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to cash smoothed by 126d, slope over 63d
def f27it_investments_cash_ratio_w126_sw63_v149_slope_signal(investments, cash) -> pd.Series:
    """Calculates the slope of the ratio of investments to cash smoothed over 63 days."""
    ratio = _f27it_ratio(investments, cash)
    base = _sma(ratio, 126)
    res = _f27it_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope feature: ratio of investments to debt smoothed by 252d, slope over 5d
def f27it_investments_debt_ratio_w252_sw5_v150_slope_signal(investments, debt) -> pd.Series:
    """Calculates the slope of the ratio of investments to debt smoothed over 5 days."""
    ratio = _f27it_ratio(investments, debt)
    base = _sma(ratio, 252)
    res = _f27it_slope(base, 5)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f27_investment_trajectory/f27it_slope_001_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f27it_'))]}
f27it_REGISTRY_SLOPE = REGISTRY

