"""
122_capital_access_stress — 2nd Derivatives (Features cas_drv2_001-025)
Domain: rate of change of base capital-access-stress features — velocity of external financing reliance
Asset class: US equities | Sharadar SF1 fundamentals (FUNDAMENTAL folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2YR  = 504
_TD_3YR  = 756
_TD_5YR  = 1260
_EPS     = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """Forward-fill a quarterly SF1 field onto a daily trading-day index."""
    return q_series.reindex(daily_index).ffill()


# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────
# Each 2nd-derivative = QoQ diff (63 td) or 1-quarter velocity of a base feature.

def cas_drv2_001_ncff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of ncff (velocity of external financing inflow change)."""
    return ncff.diff(_TD_QTR)


def cas_drv2_002_ncff_yoy_diff(ncff: pd.Series) -> pd.Series:
    """YoY diff of ncff (annual velocity of external financing)."""
    return ncff.diff(_TD_YEAR)


def cas_drv2_003_ncfdebt_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """QoQ diff of ncfdebt (velocity of debt issuance/repayment change)."""
    return ncfdebt.diff(_TD_QTR)


def cas_drv2_004_ncfcommon_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """QoQ diff of ncfcommon (velocity of equity-raise change)."""
    return ncfcommon.diff(_TD_QTR)


def cas_drv2_005_ncff_vs_ncfo_ratio_qoq_diff(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ diff of (NCFF / |NCFO|): velocity of external-reliance ratio."""
    ratio = _safe_div(ncff, ncfo.abs())
    return ratio.diff(_TD_QTR)


def cas_drv2_006_debt_to_equity_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ diff of debt/equity ratio (velocity of leverage change)."""
    lev = _safe_div(debt, equity.abs())
    return lev.diff(_TD_QTR)


def cas_drv2_007_ncff_4q_sum_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of TTM NCFF (velocity of rolling external-capital inflow)."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return ncff4q.diff(_TD_QTR)


def cas_drv2_008_ncfdebt_4q_sum_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """QoQ diff of TTM ncfdebt (velocity of rolling debt-capital reliance)."""
    ncfdebt4q = _rolling_sum(ncfdebt, _TD_YEAR)
    return ncfdebt4q.diff(_TD_QTR)


def cas_drv2_009_ncfcommon_4q_sum_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """QoQ diff of TTM ncfcommon (velocity of rolling equity-raise)."""
    ncfcommon4q = _rolling_sum(ncfcommon, _TD_YEAR)
    return ncfcommon4q.diff(_TD_QTR)


def cas_drv2_010_dividends_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ diff of dividends (velocity of capital-return change — cut signal speed)."""
    return dividends.diff(_TD_QTR)


def cas_drv2_011_debtc_qoq_diff(debtc: pd.Series) -> pd.Series:
    """QoQ diff of current debt (velocity of near-term refinancing pressure)."""
    return debtc.diff(_TD_QTR)


def cas_drv2_012_equity_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ diff of book equity (velocity of equity base erosion/recovery)."""
    return equity.diff(_TD_QTR)


def cas_drv2_013_intexp_qoq_diff(intexp: pd.Series) -> pd.Series:
    """QoQ diff of interest expense (velocity of debt-service cost change)."""
    return intexp.diff(_TD_QTR)


def cas_drv2_014_net_debt_qoq_diff(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ diff of net debt (debt - cash): velocity of net leverage change."""
    net_debt = debt - cashnequiv
    return net_debt.diff(_TD_QTR)


def cas_drv2_015_ncff_zscore_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of NCFF z-score (velocity of NCFF relative to 8q distribution)."""
    z = _zscore_rolling(ncff, _TD_2YR)
    return z.diff(_TD_QTR)


def cas_drv2_016_leverage_zscore_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ diff of leverage z-score (velocity of leverage relative to 8q distribution)."""
    lev = _safe_div(debt, equity.abs())
    z   = _zscore_rolling(lev, _TD_2YR)
    return z.diff(_TD_QTR)


def cas_drv2_017_ncff_slope_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of NCFF 4-quarter OLS slope (acceleration of external financing trend)."""
    slope = _linslope(ncff, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cas_drv2_018_ncfdebt_slope_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """QoQ diff of ncfdebt 4-quarter OLS slope."""
    slope = _linslope(ncfdebt, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cas_drv2_019_debtc_to_cash_ratio_qoq_diff(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ diff of debtc/cash ratio (velocity of near-term liquidity risk)."""
    ratio = _safe_div(debtc, cashnequiv)
    return ratio.diff(_TD_QTR)


def cas_drv2_020_intexp_coverage_qoq_diff(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of interest coverage ratio NCFO/|intexp| (velocity of coverage deterioration)."""
    ncfo4q   = _rolling_sum(ncfo, _TD_YEAR)
    intexp4q = _rolling_sum(intexp.abs(), _TD_YEAR)
    cov      = _safe_div(ncfo4q, intexp4q)
    return cov.diff(_TD_QTR)


def cas_drv2_021_capital_return_qoq_diff(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """QoQ diff of total capital return (buybacks + dividends): velocity of return cessation."""
    buybacks = (-ncfcommon).clip(lower=0)
    total    = buybacks + dividends
    return total.diff(_TD_QTR)


def cas_drv2_022_ncff_pct_rank_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of NCFF percentile rank (velocity of rank deterioration)."""
    rank = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)
    return rank.diff(_TD_QTR)


def cas_drv2_023_equity_replace_debt_flag_sum_4q(ncfcommon: pd.Series, ncfdebt: pd.Series) -> pd.Series:
    """Count of quarters in trailing year where equity replaced debt (dual-stress frequency)."""
    flag = ((ncfcommon > 0) & (ncfdebt < 0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def cas_drv2_024_ncfdebt_to_debt_ratio_qoq_diff(ncfdebt: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ diff of (ncfdebt / debt): velocity of debt-rollover intensity."""
    ratio = _safe_div(ncfdebt, debt)
    return ratio.diff(_TD_QTR)


def cas_drv2_025_external_stress_composite_qoq_diff(ncff: pd.Series, ncfdebt: pd.Series,
                                                      ncfcommon: pd.Series, debt: pd.Series,
                                                      equity: pd.Series) -> pd.Series:
    """QoQ diff of the external financing composite (velocity of composite stress change)."""
    ncff_r     = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    lev        = _safe_div(debt, equity.abs()).fillna(0)
    lev_r      = lev.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    nd_r       = ncfdebt.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    nc_r       = ncfcommon.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    composite  = 0.35 * ncff_r + 0.25 * lev_r + 0.25 * nd_r + 0.15 * nc_r
    return composite.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITAL_ACCESS_STRESS_REGISTRY_2ND_DERIVATIVES = {
    "cas_drv2_001_ncff_qoq_diff":                      {"inputs": ["ncff"],                                    "func": cas_drv2_001_ncff_qoq_diff},
    "cas_drv2_002_ncff_yoy_diff":                      {"inputs": ["ncff"],                                    "func": cas_drv2_002_ncff_yoy_diff},
    "cas_drv2_003_ncfdebt_qoq_diff":                   {"inputs": ["ncfdebt"],                                 "func": cas_drv2_003_ncfdebt_qoq_diff},
    "cas_drv2_004_ncfcommon_qoq_diff":                 {"inputs": ["ncfcommon"],                               "func": cas_drv2_004_ncfcommon_qoq_diff},
    "cas_drv2_005_ncff_vs_ncfo_ratio_qoq_diff":        {"inputs": ["ncff", "ncfo"],                            "func": cas_drv2_005_ncff_vs_ncfo_ratio_qoq_diff},
    "cas_drv2_006_debt_to_equity_qoq_diff":            {"inputs": ["debt", "equity"],                          "func": cas_drv2_006_debt_to_equity_qoq_diff},
    "cas_drv2_007_ncff_4q_sum_qoq_diff":               {"inputs": ["ncff"],                                    "func": cas_drv2_007_ncff_4q_sum_qoq_diff},
    "cas_drv2_008_ncfdebt_4q_sum_qoq_diff":            {"inputs": ["ncfdebt"],                                 "func": cas_drv2_008_ncfdebt_4q_sum_qoq_diff},
    "cas_drv2_009_ncfcommon_4q_sum_qoq_diff":          {"inputs": ["ncfcommon"],                               "func": cas_drv2_009_ncfcommon_4q_sum_qoq_diff},
    "cas_drv2_010_dividends_qoq_diff":                 {"inputs": ["dividends"],                               "func": cas_drv2_010_dividends_qoq_diff},
    "cas_drv2_011_debtc_qoq_diff":                     {"inputs": ["debtc"],                                   "func": cas_drv2_011_debtc_qoq_diff},
    "cas_drv2_012_equity_qoq_diff":                    {"inputs": ["equity"],                                  "func": cas_drv2_012_equity_qoq_diff},
    "cas_drv2_013_intexp_qoq_diff":                    {"inputs": ["intexp"],                                  "func": cas_drv2_013_intexp_qoq_diff},
    "cas_drv2_014_net_debt_qoq_diff":                  {"inputs": ["debt", "cashnequiv"],                      "func": cas_drv2_014_net_debt_qoq_diff},
    "cas_drv2_015_ncff_zscore_qoq_diff":               {"inputs": ["ncff"],                                    "func": cas_drv2_015_ncff_zscore_qoq_diff},
    "cas_drv2_016_leverage_zscore_qoq_diff":           {"inputs": ["debt", "equity"],                          "func": cas_drv2_016_leverage_zscore_qoq_diff},
    "cas_drv2_017_ncff_slope_qoq_diff":                {"inputs": ["ncff"],                                    "func": cas_drv2_017_ncff_slope_qoq_diff},
    "cas_drv2_018_ncfdebt_slope_qoq_diff":             {"inputs": ["ncfdebt"],                                 "func": cas_drv2_018_ncfdebt_slope_qoq_diff},
    "cas_drv2_019_debtc_to_cash_ratio_qoq_diff":       {"inputs": ["debtc", "cashnequiv"],                     "func": cas_drv2_019_debtc_to_cash_ratio_qoq_diff},
    "cas_drv2_020_intexp_coverage_qoq_diff":           {"inputs": ["ncfo", "intexp"],                          "func": cas_drv2_020_intexp_coverage_qoq_diff},
    "cas_drv2_021_capital_return_qoq_diff":            {"inputs": ["ncfcommon", "dividends"],                  "func": cas_drv2_021_capital_return_qoq_diff},
    "cas_drv2_022_ncff_pct_rank_qoq_diff":             {"inputs": ["ncff"],                                    "func": cas_drv2_022_ncff_pct_rank_qoq_diff},
    "cas_drv2_023_equity_replace_debt_flag_sum_4q":    {"inputs": ["ncfcommon", "ncfdebt"],                    "func": cas_drv2_023_equity_replace_debt_flag_sum_4q},
    "cas_drv2_024_ncfdebt_to_debt_ratio_qoq_diff":     {"inputs": ["ncfdebt", "debt"],                         "func": cas_drv2_024_ncfdebt_to_debt_ratio_qoq_diff},
    "cas_drv2_025_external_stress_composite_qoq_diff": {"inputs": ["ncff", "ncfdebt", "ncfcommon", "debt", "equity"], "func": cas_drv2_025_external_stress_composite_qoq_diff},
}
