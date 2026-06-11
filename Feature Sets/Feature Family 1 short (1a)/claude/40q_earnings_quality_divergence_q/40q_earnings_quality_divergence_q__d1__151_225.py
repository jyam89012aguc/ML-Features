"""earnings_quality_divergence_q d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20
QQTRS_4Y = 16


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def f40q_eqdgq_151_conditional_accrual_shock_z_post_calm_d1(workingcapital: pd.Series, depamor: pd.Series, assets: pd.Series) -> pd.Series:
    delta_wc = workingcapital.diff()
    accr = _safe_div(delta_wc - depamor, assets)
    z16 = _rolling_zscore(accr, QQTRS_4Y)
    std4_prior = accr.shift(1).rolling(QQTRS, min_periods=max(QQTRS // 2, 2)).std()
    std16 = accr.rolling(QQTRS_4Y, min_periods=max(QQTRS_4Y // 3, 2)).std()
    calm = std4_prior < (0.5 * std16)
    return z16.where(calm).diff()


def f40q_eqdgq_152_sloan_bs_vs_cf_method_gap_d1(workingcapital: pd.Series, depamor: pd.Series, netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    bs = _safe_div(workingcapital.diff() - depamor, assets)
    cf = _safe_div(netinc - ncfo, assets)
    return (bs - cf).abs().diff()


def f40q_eqdgq_153_cashconv_dispersion_regime_change_d1(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    ratio = _safe_div(ncfo, netinc)
    var_recent = ratio.rolling(QQTRS_2Y, min_periods=max(QQTRS_2Y // 2, 3)).var()
    var_prior = ratio.shift(QQTRS_2Y).rolling(QQTRS_2Y, min_periods=max(QQTRS_2Y // 2, 3)).var()
    return _safe_div(var_recent, var_prior).diff()


EARNINGS_QUALITY_DIVERGENCE_Q_D1_REGISTRY_151_225 = {
    "f40q_eqdgq_151_conditional_accrual_shock_z_post_calm_d1": {"inputs": ["workingcapital", "depamor", "assets"], "func": f40q_eqdgq_151_conditional_accrual_shock_z_post_calm_d1},
    "f40q_eqdgq_152_sloan_bs_vs_cf_method_gap_d1": {"inputs": ["workingcapital", "depamor", "netinc", "ncfo", "assets"], "func": f40q_eqdgq_152_sloan_bs_vs_cf_method_gap_d1},
    "f40q_eqdgq_153_cashconv_dispersion_regime_change_d1": {"inputs": ["ncfo", "netinc"], "func": f40q_eqdgq_153_cashconv_dispersion_regime_change_d1},
}
