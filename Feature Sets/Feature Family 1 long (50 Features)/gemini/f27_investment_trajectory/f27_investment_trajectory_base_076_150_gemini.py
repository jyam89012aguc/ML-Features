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

# Base feature: investments smoothed by 756d
def f27it_investments_w756_v076_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 756 days."""
    res = _sma(investments, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 1260d
def f27it_investments_capex_ratio_w1260_v077_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 63d
def f27it_investments_revenue_ratio_w63_v078_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to assets smoothed by 126d
def f27it_investments_assets_ratio_w126_v079_base_signal(investments, assets) -> pd.Series:
    """Calculates the ratio of investments to assets smoothed over 126 days."""
    ratio = _f27it_ratio(investments, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to cash smoothed by 252d
def f27it_investments_cash_ratio_w252_v080_base_signal(investments, cash) -> pd.Series:
    """Calculates the ratio of investments to cash smoothed over 252 days."""
    ratio = _f27it_ratio(investments, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to debt smoothed by 504d
def f27it_investments_debt_ratio_w504_v081_base_signal(investments, debt) -> pd.Series:
    """Calculates the ratio of investments to debt smoothed over 504 days."""
    ratio = _f27it_ratio(investments, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to investments smoothed by 756d
def f27it_capex_investments_ratio_w756_v082_base_signal(capex, investments) -> pd.Series:
    """Calculates the ratio of capex to investments smoothed over 756 days."""
    ratio = _f27it_ratio(capex, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 1260d
def f27it_capex_w1260_v083_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 1260 days."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 63d
def f27it_capex_revenue_ratio_w63_v084_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(capex, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 126d
def f27it_capex_assets_ratio_w126_v085_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 126 days."""
    ratio = _f27it_ratio(capex, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to cash smoothed by 252d
def f27it_capex_cash_ratio_w252_v086_base_signal(capex, cash) -> pd.Series:
    """Calculates the ratio of capex to cash smoothed over 252 days."""
    ratio = _f27it_ratio(capex, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to debt smoothed by 504d
def f27it_capex_debt_ratio_w504_v087_base_signal(capex, debt) -> pd.Series:
    """Calculates the ratio of capex to debt smoothed over 504 days."""
    ratio = _f27it_ratio(capex, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to investments smoothed by 756d
def f27it_revenue_investments_ratio_w756_v088_base_signal(revenue, investments) -> pd.Series:
    """Calculates the ratio of revenue to investments smoothed over 756 days."""
    ratio = _f27it_ratio(revenue, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 1260d
def f27it_revenue_capex_ratio_w1260_v089_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(revenue, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 63d
def f27it_revenue_w63_v090_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 63 days."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 126d
def f27it_revenue_assets_ratio_w126_v091_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 126 days."""
    ratio = _f27it_ratio(revenue, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to cash smoothed by 252d
def f27it_revenue_cash_ratio_w252_v092_base_signal(revenue, cash) -> pd.Series:
    """Calculates the ratio of revenue to cash smoothed over 252 days."""
    ratio = _f27it_ratio(revenue, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to debt smoothed by 504d
def f27it_revenue_debt_ratio_w504_v093_base_signal(revenue, debt) -> pd.Series:
    """Calculates the ratio of revenue to debt smoothed over 504 days."""
    ratio = _f27it_ratio(revenue, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to investments smoothed by 756d
def f27it_assets_investments_ratio_w756_v094_base_signal(assets, investments) -> pd.Series:
    """Calculates the ratio of assets to investments smoothed over 756 days."""
    ratio = _f27it_ratio(assets, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 1260d
def f27it_assets_capex_ratio_w1260_v095_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(assets, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 63d
def f27it_assets_revenue_ratio_w63_v096_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(assets, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 126d
def f27it_assets_w126_v097_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 126 days."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to cash smoothed by 252d
def f27it_assets_cash_ratio_w252_v098_base_signal(assets, cash) -> pd.Series:
    """Calculates the ratio of assets to cash smoothed over 252 days."""
    ratio = _f27it_ratio(assets, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to debt smoothed by 504d
def f27it_assets_debt_ratio_w504_v099_base_signal(assets, debt) -> pd.Series:
    """Calculates the ratio of assets to debt smoothed over 504 days."""
    ratio = _f27it_ratio(assets, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to investments smoothed by 756d
def f27it_cash_investments_ratio_w756_v100_base_signal(cash, investments) -> pd.Series:
    """Calculates the ratio of cash to investments smoothed over 756 days."""
    ratio = _f27it_ratio(cash, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to capex smoothed by 1260d
def f27it_cash_capex_ratio_w1260_v101_base_signal(cash, capex) -> pd.Series:
    """Calculates the ratio of cash to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(cash, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to revenue smoothed by 63d
def f27it_cash_revenue_ratio_w63_v102_base_signal(cash, revenue) -> pd.Series:
    """Calculates the ratio of cash to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(cash, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to assets smoothed by 126d
def f27it_cash_assets_ratio_w126_v103_base_signal(cash, assets) -> pd.Series:
    """Calculates the ratio of cash to assets smoothed over 126 days."""
    ratio = _f27it_ratio(cash, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: cash smoothed by 252d
def f27it_cash_w252_v104_base_signal(cash) -> pd.Series:
    """Calculates the smoothed cash over 252 days."""
    res = _sma(cash, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to debt smoothed by 504d
def f27it_cash_debt_ratio_w504_v105_base_signal(cash, debt) -> pd.Series:
    """Calculates the ratio of cash to debt smoothed over 504 days."""
    ratio = _f27it_ratio(cash, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to investments smoothed by 756d
def f27it_debt_investments_ratio_w756_v106_base_signal(debt, investments) -> pd.Series:
    """Calculates the ratio of debt to investments smoothed over 756 days."""
    ratio = _f27it_ratio(debt, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to capex smoothed by 1260d
def f27it_debt_capex_ratio_w1260_v107_base_signal(debt, capex) -> pd.Series:
    """Calculates the ratio of debt to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(debt, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to revenue smoothed by 63d
def f27it_debt_revenue_ratio_w63_v108_base_signal(debt, revenue) -> pd.Series:
    """Calculates the ratio of debt to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(debt, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to assets smoothed by 126d
def f27it_debt_assets_ratio_w126_v109_base_signal(debt, assets) -> pd.Series:
    """Calculates the ratio of debt to assets smoothed over 126 days."""
    ratio = _f27it_ratio(debt, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to cash smoothed by 252d
def f27it_debt_cash_ratio_w252_v110_base_signal(debt, cash) -> pd.Series:
    """Calculates the ratio of debt to cash smoothed over 252 days."""
    ratio = _f27it_ratio(debt, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: debt smoothed by 504d
def f27it_debt_w504_v111_base_signal(debt) -> pd.Series:
    """Calculates the smoothed debt over 504 days."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: investments smoothed by 756d
def f27it_investments_w756_v112_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 756 days."""
    res = _sma(investments, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 1260d
def f27it_investments_capex_ratio_w1260_v113_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 63d
def f27it_investments_revenue_ratio_w63_v114_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to assets smoothed by 126d
def f27it_investments_assets_ratio_w126_v115_base_signal(investments, assets) -> pd.Series:
    """Calculates the ratio of investments to assets smoothed over 126 days."""
    ratio = _f27it_ratio(investments, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to cash smoothed by 252d
def f27it_investments_cash_ratio_w252_v116_base_signal(investments, cash) -> pd.Series:
    """Calculates the ratio of investments to cash smoothed over 252 days."""
    ratio = _f27it_ratio(investments, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to debt smoothed by 504d
def f27it_investments_debt_ratio_w504_v117_base_signal(investments, debt) -> pd.Series:
    """Calculates the ratio of investments to debt smoothed over 504 days."""
    ratio = _f27it_ratio(investments, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to investments smoothed by 756d
def f27it_capex_investments_ratio_w756_v118_base_signal(capex, investments) -> pd.Series:
    """Calculates the ratio of capex to investments smoothed over 756 days."""
    ratio = _f27it_ratio(capex, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: capex smoothed by 1260d
def f27it_capex_w1260_v119_base_signal(capex) -> pd.Series:
    """Calculates the smoothed capex over 1260 days."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to revenue smoothed by 63d
def f27it_capex_revenue_ratio_w63_v120_base_signal(capex, revenue) -> pd.Series:
    """Calculates the ratio of capex to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(capex, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to assets smoothed by 126d
def f27it_capex_assets_ratio_w126_v121_base_signal(capex, assets) -> pd.Series:
    """Calculates the ratio of capex to assets smoothed over 126 days."""
    ratio = _f27it_ratio(capex, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to cash smoothed by 252d
def f27it_capex_cash_ratio_w252_v122_base_signal(capex, cash) -> pd.Series:
    """Calculates the ratio of capex to cash smoothed over 252 days."""
    ratio = _f27it_ratio(capex, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of capex to debt smoothed by 504d
def f27it_capex_debt_ratio_w504_v123_base_signal(capex, debt) -> pd.Series:
    """Calculates the ratio of capex to debt smoothed over 504 days."""
    ratio = _f27it_ratio(capex, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to investments smoothed by 756d
def f27it_revenue_investments_ratio_w756_v124_base_signal(revenue, investments) -> pd.Series:
    """Calculates the ratio of revenue to investments smoothed over 756 days."""
    ratio = _f27it_ratio(revenue, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to capex smoothed by 1260d
def f27it_revenue_capex_ratio_w1260_v125_base_signal(revenue, capex) -> pd.Series:
    """Calculates the ratio of revenue to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(revenue, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: revenue smoothed by 63d
def f27it_revenue_w63_v126_base_signal(revenue) -> pd.Series:
    """Calculates the smoothed revenue over 63 days."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to assets smoothed by 126d
def f27it_revenue_assets_ratio_w126_v127_base_signal(revenue, assets) -> pd.Series:
    """Calculates the ratio of revenue to assets smoothed over 126 days."""
    ratio = _f27it_ratio(revenue, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to cash smoothed by 252d
def f27it_revenue_cash_ratio_w252_v128_base_signal(revenue, cash) -> pd.Series:
    """Calculates the ratio of revenue to cash smoothed over 252 days."""
    ratio = _f27it_ratio(revenue, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of revenue to debt smoothed by 504d
def f27it_revenue_debt_ratio_w504_v129_base_signal(revenue, debt) -> pd.Series:
    """Calculates the ratio of revenue to debt smoothed over 504 days."""
    ratio = _f27it_ratio(revenue, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to investments smoothed by 756d
def f27it_assets_investments_ratio_w756_v130_base_signal(assets, investments) -> pd.Series:
    """Calculates the ratio of assets to investments smoothed over 756 days."""
    ratio = _f27it_ratio(assets, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to capex smoothed by 1260d
def f27it_assets_capex_ratio_w1260_v131_base_signal(assets, capex) -> pd.Series:
    """Calculates the ratio of assets to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(assets, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to revenue smoothed by 63d
def f27it_assets_revenue_ratio_w63_v132_base_signal(assets, revenue) -> pd.Series:
    """Calculates the ratio of assets to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(assets, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: assets smoothed by 126d
def f27it_assets_w126_v133_base_signal(assets) -> pd.Series:
    """Calculates the smoothed assets over 126 days."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to cash smoothed by 252d
def f27it_assets_cash_ratio_w252_v134_base_signal(assets, cash) -> pd.Series:
    """Calculates the ratio of assets to cash smoothed over 252 days."""
    ratio = _f27it_ratio(assets, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of assets to debt smoothed by 504d
def f27it_assets_debt_ratio_w504_v135_base_signal(assets, debt) -> pd.Series:
    """Calculates the ratio of assets to debt smoothed over 504 days."""
    ratio = _f27it_ratio(assets, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to investments smoothed by 756d
def f27it_cash_investments_ratio_w756_v136_base_signal(cash, investments) -> pd.Series:
    """Calculates the ratio of cash to investments smoothed over 756 days."""
    ratio = _f27it_ratio(cash, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to capex smoothed by 1260d
def f27it_cash_capex_ratio_w1260_v137_base_signal(cash, capex) -> pd.Series:
    """Calculates the ratio of cash to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(cash, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to revenue smoothed by 63d
def f27it_cash_revenue_ratio_w63_v138_base_signal(cash, revenue) -> pd.Series:
    """Calculates the ratio of cash to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(cash, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to assets smoothed by 126d
def f27it_cash_assets_ratio_w126_v139_base_signal(cash, assets) -> pd.Series:
    """Calculates the ratio of cash to assets smoothed over 126 days."""
    ratio = _f27it_ratio(cash, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: cash smoothed by 252d
def f27it_cash_w252_v140_base_signal(cash) -> pd.Series:
    """Calculates the smoothed cash over 252 days."""
    res = _sma(cash, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of cash to debt smoothed by 504d
def f27it_cash_debt_ratio_w504_v141_base_signal(cash, debt) -> pd.Series:
    """Calculates the ratio of cash to debt smoothed over 504 days."""
    ratio = _f27it_ratio(cash, debt)
    res = _sma(ratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to investments smoothed by 756d
def f27it_debt_investments_ratio_w756_v142_base_signal(debt, investments) -> pd.Series:
    """Calculates the ratio of debt to investments smoothed over 756 days."""
    ratio = _f27it_ratio(debt, investments)
    res = _sma(ratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to capex smoothed by 1260d
def f27it_debt_capex_ratio_w1260_v143_base_signal(debt, capex) -> pd.Series:
    """Calculates the ratio of debt to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(debt, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to revenue smoothed by 63d
def f27it_debt_revenue_ratio_w63_v144_base_signal(debt, revenue) -> pd.Series:
    """Calculates the ratio of debt to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(debt, revenue)
    res = _sma(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to assets smoothed by 126d
def f27it_debt_assets_ratio_w126_v145_base_signal(debt, assets) -> pd.Series:
    """Calculates the ratio of debt to assets smoothed over 126 days."""
    ratio = _f27it_ratio(debt, assets)
    res = _sma(ratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of debt to cash smoothed by 252d
def f27it_debt_cash_ratio_w252_v146_base_signal(debt, cash) -> pd.Series:
    """Calculates the ratio of debt to cash smoothed over 252 days."""
    ratio = _f27it_ratio(debt, cash)
    res = _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: debt smoothed by 504d
def f27it_debt_w504_v147_base_signal(debt) -> pd.Series:
    """Calculates the smoothed debt over 504 days."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: investments smoothed by 756d
def f27it_investments_w756_v148_base_signal(investments) -> pd.Series:
    """Calculates the smoothed investments over 756 days."""
    res = _sma(investments, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to capex smoothed by 1260d
def f27it_investments_capex_ratio_w1260_v149_base_signal(investments, capex) -> pd.Series:
    """Calculates the ratio of investments to capex smoothed over 1260 days."""
    ratio = _f27it_ratio(investments, capex)
    res = _sma(ratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Base feature: ratio of investments to revenue smoothed by 63d
def f27it_investments_revenue_ratio_w63_v150_base_signal(investments, revenue) -> pd.Series:
    """Calculates the ratio of investments to revenue smoothed over 63 days."""
    ratio = _f27it_ratio(investments, revenue)
    res = _sma(ratio, 63)
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
    print(f"All {len(funcs)} tests passed for C:/Users/jyama/Desktop/active_non audited features per AI/gemini/PENDING_20260511_152500 (50 feature family)/f27_investment_trajectory/f27it_base_076_150_gemini.py!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f27it_'))]}
f27it_REGISTRY_BASE = REGISTRY

