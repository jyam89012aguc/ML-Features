import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _f27it_ratio(num, den):
    return num / den.replace(0, np.nan)

def _f27it_diff(a, b):
    return a - b

def _f27it_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

# Base feature: investments smoothed by 126d
def f27it_investments_w126_v001_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 126 days."""
    res = _sma(investments, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 252d
def f27it_investments_capex_ratio_w252_v002_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 252 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 504d
def f27it_investments_revenue_ratio_w504_v003_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to assets smoothed by 756d
def f27it_investments_assets_ratio_w756_v004_base_signal(investments, assets) -> pd.Series:
    """Calculates the ratio of investments to assets smoothed over 756 days."""
    ratio = _f27it_ratio(investments, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to cash smoothed by 1260d
def f27it_investments_cash_ratio_w1260_v005_base_signal(investments, cash) -> pd.Series:
    """Calculates the ratio of investments to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(investments, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to debt smoothed by 63d
def f27it_investments_debt_ratio_w63_v006_base_signal(investments, debt) -> pd.Series:
    """Calculates the ratio of investments to debt smoothed over 63 days."""
    ratio = _f27it_ratio(investments, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to investments smoothed by 126d
def f27it_capex_investments_ratio_w126_v007_base_signal(capex, investments) -> pd.Series:
    """Calculates the ratio of capex to investments smoothed over 126 days."""
    ratio = _f27it_ratio(capex, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 252d
def f27it_capex_w252_v008_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 252 days."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 504d
def f27it_capex_revenue_ratio_w504_v009_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(capex, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 756d
def f27it_capex_assets_ratio_w756_v010_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 756 days."""
    ratio = _f27it_ratio(capex, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to cash smoothed by 1260d
def f27it_capex_cash_ratio_w1260_v011_base_signal(capex, cash) -> pd.Series:
    """Calculates the ratio of capex to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(capex, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to debt smoothed by 63d
def f27it_capex_debt_ratio_w63_v012_base_signal(capex, debt) -> pd.Series:
    """Calculates the ratio of capex to debt smoothed over 63 days."""
    ratio = _f27it_ratio(capex, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to investments smoothed by 126d
def f27it_revenue_investments_ratio_w126_v013_base_signal(revenue, investments) -> pd.Series:
    """Calculates the ratio of revenue to investments smoothed over 126 days."""
    ratio = _f27it_ratio(revenue, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 252d
def f27it_revenue_capex_ratio_w252_v014_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 252 days."""
    ratio = _f27it_ratio(revenue, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 504d
def f27it_revenue_w504_v015_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 504 days."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 756d
def f27it_revenue_assets_ratio_w756_v016_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 756 days."""
    ratio = _f27it_ratio(revenue, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to cash smoothed by 1260d
def f27it_revenue_cash_ratio_w1260_v017_base_signal(revenue, cash) -> pd.Series:
    """Calculates the ratio of revenue to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(revenue, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to debt smoothed by 63d
def f27it_revenue_debt_ratio_w63_v018_base_signal(revenue, debt) -> pd.Series:
    """Calculates the ratio of revenue to debt smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to investments smoothed by 126d
def f27it_assets_investments_ratio_w126_v019_base_signal(assets, investments) -> pd.Series:
    """Calculates the ratio of assets to investments smoothed over 126 days."""
    ratio = _f27it_ratio(assets, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 252d
def f27it_assets_capex_ratio_w252_v020_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 252 days."""
    ratio = _f27it_ratio(assets, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 504d
def f27it_assets_revenue_ratio_w504_v021_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(assets, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 756d
def f27it_assets_w756_v022_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 756 days."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to cash smoothed by 1260d
def f27it_assets_cash_ratio_w1260_v023_base_signal(assets, cash) -> pd.Series:
    """Calculates the ratio of assets to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(assets, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to debt smoothed by 63d
def f27it_assets_debt_ratio_w63_v024_base_signal(assets, debt) -> pd.Series:
    """Calculates the ratio of assets to debt smoothed over 63 days."""
    ratio = _f27it_ratio(assets, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to investments smoothed by 126d
def f27it_cash_investments_ratio_w126_v025_base_signal(cash, investments) -> pd.Series:
    """Calculates the ratio of cash to investments smoothed over 126 days."""
    ratio = _f27it_ratio(cash, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to capex smoothed by 252d
def f27it_cash_capex_ratio_w252_v026_base_signal(cash, capex) -> pd.Series:
    """Calculates the ratio of cash to capex smoothed over 252 days."""
    ratio = _f27it_ratio(cash, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to revenue smoothed by 504d
def f27it_cash_revenue_ratio_w504_v027_base_signal(cash, revenue) -> pd.Series:
    """Calculates the ratio of cash to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(cash, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to assets smoothed by 756d
def f27it_cash_assets_ratio_w756_v028_base_signal(cash, assets) -> pd.Series:
    """Calculates the ratio of cash to assets smoothed over 756 days."""
    ratio = _f27it_ratio(cash, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: cash smoothed by 1260d
def f27it_cash_w1260_v029_base_signal(cash) -> pd.Series:
    """Calculates the smoothed cash over 1260 days."""
    res = _sma(cash, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to debt smoothed by 63d
def f27it_cash_debt_ratio_w63_v030_base_signal(cash, debt) -> pd.Series:
    """Calculates the ratio of cash to debt smoothed over 63 days."""
    ratio = _f27it_ratio(cash, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to investments smoothed by 126d
def f27it_debt_investments_ratio_w126_v031_base_signal(debt, investments) -> pd.Series:
    """Calculates the ratio of debt to investments smoothed over 126 days."""
    ratio = _f27it_ratio(debt, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to capex smoothed by 252d
def f27it_debt_capex_ratio_w252_v032_base_signal(debt, capex) -> pd.Series:
    """Calculates the ratio of debt to capex smoothed over 252 days."""
    ratio = _f27it_ratio(debt, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to revenue smoothed by 504d
def f27it_debt_revenue_ratio_w504_v033_base_signal(debt, revenue) -> pd.Series:
    """Calculates the ratio of debt to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(debt, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to assets smoothed by 756d
def f27it_debt_assets_ratio_w756_v034_base_signal(debt, assets) -> pd.Series:
    """Calculates the ratio of debt to assets smoothed over 756 days."""
    ratio = _f27it_ratio(debt, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to cash smoothed by 1260d
def f27it_debt_cash_ratio_w1260_v035_base_signal(debt, cash) -> pd.Series:
    """Calculates the ratio of debt to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(debt, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: debt smoothed by 63d
def f27it_debt_w63_v036_base_signal(debt) -> pd.Series:
    """Calculates the smoothed debt over 63 days."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: investments smoothed by 126d
def f27it_investments_w126_v037_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 126 days."""
    res = _sma(investments, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 252d
def f27it_investments_capex_ratio_w252_v038_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 252 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 504d
def f27it_investments_revenue_ratio_w504_v039_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to assets smoothed by 756d
def f27it_investments_assets_ratio_w756_v040_base_signal(investments, assets) -> pd.Series:
    """Calculates the ratio of investments to assets smoothed over 756 days."""
    ratio = _f27it_ratio(investments, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to cash smoothed by 1260d
def f27it_investments_cash_ratio_w1260_v041_base_signal(investments, cash) -> pd.Series:
    """Calculates the ratio of investments to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(investments, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to debt smoothed by 63d
def f27it_investments_debt_ratio_w63_v042_base_signal(investments, debt) -> pd.Series:
    """Calculates the ratio of investments to debt smoothed over 63 days."""
    ratio = _f27it_ratio(investments, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to investments smoothed by 126d
def f27it_capex_investments_ratio_w126_v043_base_signal(capex, investments) -> pd.Series:
    """Calculates the ratio of capex to investments smoothed over 126 days."""
    ratio = _f27it_ratio(capex, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 252d
def f27it_capex_w252_v044_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 252 days."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 504d
def f27it_capex_revenue_ratio_w504_v045_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(capex, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 756d
def f27it_capex_assets_ratio_w756_v046_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 756 days."""
    ratio = _f27it_ratio(capex, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to cash smoothed by 1260d
def f27it_capex_cash_ratio_w1260_v047_base_signal(capex, cash) -> pd.Series:
    """Calculates the ratio of capex to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(capex, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to debt smoothed by 63d
def f27it_capex_debt_ratio_w63_v048_base_signal(capex, debt) -> pd.Series:
    """Calculates the ratio of capex to debt smoothed over 63 days."""
    ratio = _f27it_ratio(capex, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to investments smoothed by 126d
def f27it_revenue_investments_ratio_w126_v049_base_signal(revenue, investments) -> pd.Series:
    """Calculates the ratio of revenue to investments smoothed over 126 days."""
    ratio = _f27it_ratio(revenue, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 252d
def f27it_revenue_capex_ratio_w252_v050_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 252 days."""
    ratio = _f27it_ratio(revenue, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 504d
def f27it_revenue_w504_v051_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 504 days."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 756d
def f27it_revenue_assets_ratio_w756_v052_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 756 days."""
    ratio = _f27it_ratio(revenue, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to cash smoothed by 1260d
def f27it_revenue_cash_ratio_w1260_v053_base_signal(revenue, cash) -> pd.Series:
    """Calculates the ratio of revenue to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(revenue, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to debt smoothed by 63d
def f27it_revenue_debt_ratio_w63_v054_base_signal(revenue, debt) -> pd.Series:
    """Calculates the ratio of revenue to debt smoothed over 63 days."""
    ratio = _f27it_ratio(revenue, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to investments smoothed by 126d
def f27it_assets_investments_ratio_w126_v055_base_signal(assets, investments) -> pd.Series:
    """Calculates the ratio of assets to investments smoothed over 126 days."""
    ratio = _f27it_ratio(assets, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 252d
def f27it_assets_capex_ratio_w252_v056_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 252 days."""
    ratio = _f27it_ratio(assets, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 504d
def f27it_assets_revenue_ratio_w504_v057_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(assets, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 756d
def f27it_assets_w756_v058_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 756 days."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to cash smoothed by 1260d
def f27it_assets_cash_ratio_w1260_v059_base_signal(assets, cash) -> pd.Series:
    """Calculates the ratio of assets to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(assets, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to debt smoothed by 63d
def f27it_assets_debt_ratio_w63_v060_base_signal(assets, debt) -> pd.Series:
    """Calculates the ratio of assets to debt smoothed over 63 days."""
    ratio = _f27it_ratio(assets, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to investments smoothed by 126d
def f27it_cash_investments_ratio_w126_v061_base_signal(cash, investments) -> pd.Series:
    """Calculates the ratio of cash to investments smoothed over 126 days."""
    ratio = _f27it_ratio(cash, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to capex smoothed by 252d
def f27it_cash_capex_ratio_w252_v062_base_signal(cash, capex) -> pd.Series:
    """Calculates the ratio of cash to capex smoothed over 252 days."""
    ratio = _f27it_ratio(cash, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to revenue smoothed by 504d
def f27it_cash_revenue_ratio_w504_v063_base_signal(cash, revenue) -> pd.Series:
    """Calculates the ratio of cash to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(cash, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to assets smoothed by 756d
def f27it_cash_assets_ratio_w756_v064_base_signal(cash, assets) -> pd.Series:
    """Calculates the ratio of cash to assets smoothed over 756 days."""
    ratio = _f27it_ratio(cash, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: cash smoothed by 1260d
def f27it_cash_w1260_v065_base_signal(cash) -> pd.Series:
    """Calculates the smoothed cash over 1260 days."""
    res = _sma(cash, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to debt smoothed by 63d
def f27it_cash_debt_ratio_w63_v066_base_signal(cash, debt) -> pd.Series:
    """Calculates the ratio of cash to debt smoothed over 63 days."""
    ratio = _f27it_ratio(cash, debt)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to investments smoothed by 126d
def f27it_debt_investments_ratio_w126_v067_base_signal(debt, investments) -> pd.Series:
    """Calculates the ratio of debt to investments smoothed over 126 days."""
    ratio = _f27it_ratio(debt, investments)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to capex smoothed by 252d
def f27it_debt_capex_ratio_w252_v068_base_signal(debt, capex) -> pd.Series:
    """Calculates the ratio of debt to capex smoothed over 252 days."""
    ratio = _f27it_ratio(debt, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to revenue smoothed by 504d
def f27it_debt_revenue_ratio_w504_v069_base_signal(debt, revenue) -> pd.Series:
    """Calculates the ratio of debt to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(debt, revenue)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to assets smoothed by 756d
def f27it_debt_assets_ratio_w756_v070_base_signal(debt, assets) -> pd.Series:
    """Calculates the ratio of debt to assets smoothed over 756 days."""
    ratio = _f27it_ratio(debt, assets)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to cash smoothed by 1260d
def f27it_debt_cash_ratio_w1260_v071_base_signal(debt, cash) -> pd.Series:
    """Calculates the ratio of debt to cash smoothed over 1260 days."""
    ratio = _f27it_ratio(debt, cash)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: debt smoothed by 63d
def f27it_debt_w63_v072_base_signal(debt) -> pd.Series:
    """Calculates the smoothed debt over 63 days."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: investments smoothed by 126d
def f27it_investments_w126_v073_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 126 days."""
    res = _sma(investments, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 252d
def f27it_investments_capex_ratio_w252_v074_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 252 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 504d
def f27it_investments_revenue_ratio_w504_v075_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 504 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 504)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f27_investment_trajectory/f27it_base_001_075_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f27it_'))]}
f27it_REGISTRY_BASE = REGISTRY

