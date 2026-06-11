"""
122_capital_access_stress — 3rd Derivatives (Features cas_drv3_001-025)
Domain: rate of change of 2nd-derivative capital-access-stress features — acceleration of
        external financing velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept.

def cas_drv3_001_ncff_qoq_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """Second QoQ diff of ncff (acceleration of external financing velocity)."""
    vel = ncff.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_002_ncff_yoy_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """QoQ diff of ncff YoY velocity (jerk in annual external-capital change)."""
    vel = ncff.diff(_TD_YEAR)
    return vel.diff(_TD_QTR)


def cas_drv3_003_ncfdebt_qoq_diff_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """Second QoQ diff of ncfdebt (acceleration of debt-issuance velocity)."""
    vel = ncfdebt.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_004_ncfcommon_qoq_diff_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """Second QoQ diff of ncfcommon (acceleration of equity-raise velocity)."""
    vel = ncfcommon.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_005_ncff_vs_ncfo_ratio_qoq_diff_qoq_diff(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Second QoQ diff of (NCFF/|NCFO|): acceleration of external-reliance ratio velocity."""
    ratio = _safe_div(ncff, ncfo.abs())
    vel   = ratio.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_006_debt_to_equity_qoq_diff_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Second QoQ diff of debt/equity (acceleration of leverage change rate)."""
    lev = _safe_div(debt, equity.abs())
    vel = lev.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_007_ncff_4q_sum_qoq_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """Second QoQ diff of TTM NCFF (acceleration of rolling external-capital velocity)."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    vel    = ncff4q.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_008_ncfdebt_4q_sum_qoq_diff_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """Second QoQ diff of TTM ncfdebt (acceleration of rolling debt-capital velocity)."""
    ncfdebt4q = _rolling_sum(ncfdebt, _TD_YEAR)
    vel       = ncfdebt4q.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_009_dividends_qoq_diff_qoq_diff(dividends: pd.Series) -> pd.Series:
    """Second QoQ diff of dividends (acceleration of dividend cut velocity)."""
    vel = dividends.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_010_debtc_qoq_diff_qoq_diff(debtc: pd.Series) -> pd.Series:
    """Second QoQ diff of current debt (acceleration of near-term refinancing pressure)."""
    vel = debtc.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_011_equity_qoq_diff_qoq_diff(equity: pd.Series) -> pd.Series:
    """Second QoQ diff of book equity (acceleration of equity erosion/recovery)."""
    vel = equity.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_012_intexp_qoq_diff_qoq_diff(intexp: pd.Series) -> pd.Series:
    """Second QoQ diff of interest expense (acceleration of debt-service cost change)."""
    vel = intexp.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_013_net_debt_qoq_diff_qoq_diff(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Second QoQ diff of net debt (acceleration of net-leverage velocity)."""
    net_debt = debt - cashnequiv
    vel      = net_debt.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_014_ncff_zscore_qoq_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """Second QoQ diff of NCFF z-score (acceleration of NCFF rank deterioration)."""
    z   = _zscore_rolling(ncff, _TD_2YR)
    vel = z.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_015_leverage_zscore_qoq_diff_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Second QoQ diff of leverage z-score (acceleration of leverage rank escalation)."""
    lev = _safe_div(debt, equity.abs())
    z   = _zscore_rolling(lev, _TD_2YR)
    vel = z.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_016_ncff_slope_qoq_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """Second QoQ diff of NCFF 4q OLS slope (acceleration of external-financing trend change)."""
    slope = _linslope(ncff, _TD_YEAR)
    vel   = slope.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_017_debtc_to_cash_ratio_qoq_diff_qoq_diff(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Second QoQ diff of debtc/cash ratio (acceleration of near-term liquidity risk)."""
    ratio = _safe_div(debtc, cashnequiv)
    vel   = ratio.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_018_intexp_coverage_qoq_diff_qoq_diff(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Second QoQ diff of interest coverage (acceleration of coverage deterioration)."""
    ncfo4q   = _rolling_sum(ncfo, _TD_YEAR)
    intexp4q = _rolling_sum(intexp.abs(), _TD_YEAR)
    cov      = _safe_div(ncfo4q, intexp4q)
    vel      = cov.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_019_capital_return_qoq_diff_qoq_diff(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """Second QoQ diff of total capital return (acceleration of return-cessation rate)."""
    buybacks = (-ncfcommon).clip(lower=0)
    total    = buybacks + dividends
    vel      = total.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_020_ncff_pct_rank_qoq_diff_qoq_diff(ncff: pd.Series) -> pd.Series:
    """Second QoQ diff of NCFF pct rank (acceleration of rank change)."""
    rank = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)
    vel  = rank.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_021_ncfdebt_slope_qoq_diff_qoq_diff(ncfdebt: pd.Series) -> pd.Series:
    """Second QoQ diff of ncfdebt 4q OLS slope (acceleration of debt-capital trend change)."""
    slope = _linslope(ncfdebt, _TD_YEAR)
    vel   = slope.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_022_ncfcommon_4q_sum_qoq_diff_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """Second QoQ diff of TTM ncfcommon (acceleration of rolling equity-raise velocity)."""
    ncfcommon4q = _rolling_sum(ncfcommon, _TD_YEAR)
    vel         = ncfcommon4q.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def cas_drv3_023_ncff_vs_ncfo_ratio_yoy_diff_qoq_diff(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ diff of ncff/ncfo ratio YoY velocity (jerk in annual external-reliance change)."""
    ratio   = _safe_div(ncff, ncfo.abs())
    vel_yoy = ratio.diff(_TD_YEAR)
    return vel_yoy.diff(_TD_QTR)


def cas_drv3_024_leverage_trend_slope_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ diff of 4q leverage OLS slope (velocity of leverage trend acceleration)."""
    lev   = _safe_div(debt, equity.abs())
    slope = _linslope(lev, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cas_drv3_025_external_stress_composite_qoq_diff_qoq_diff(ncff: pd.Series, ncfdebt: pd.Series,
                                                               ncfcommon: pd.Series, debt: pd.Series,
                                                               equity: pd.Series) -> pd.Series:
    """Second QoQ diff of composite external stress (acceleration of composite stress velocity)."""
    ncff_r    = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    lev       = _safe_div(debt, equity.abs()).fillna(0)
    lev_r     = lev.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    nd_r      = ncfdebt.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    nc_r      = ncfcommon.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    composite = 0.35 * ncff_r + 0.25 * lev_r + 0.25 * nd_r + 0.15 * nc_r
    vel       = composite.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITAL_ACCESS_STRESS_REGISTRY_3RD_DERIVATIVES = {
    "cas_drv3_001_ncff_qoq_diff_qoq_diff":                      {"inputs": ["ncff"],                                     "func": cas_drv3_001_ncff_qoq_diff_qoq_diff},
    "cas_drv3_002_ncff_yoy_diff_qoq_diff":                      {"inputs": ["ncff"],                                     "func": cas_drv3_002_ncff_yoy_diff_qoq_diff},
    "cas_drv3_003_ncfdebt_qoq_diff_qoq_diff":                   {"inputs": ["ncfdebt"],                                  "func": cas_drv3_003_ncfdebt_qoq_diff_qoq_diff},
    "cas_drv3_004_ncfcommon_qoq_diff_qoq_diff":                 {"inputs": ["ncfcommon"],                                "func": cas_drv3_004_ncfcommon_qoq_diff_qoq_diff},
    "cas_drv3_005_ncff_vs_ncfo_ratio_qoq_diff_qoq_diff":        {"inputs": ["ncff", "ncfo"],                             "func": cas_drv3_005_ncff_vs_ncfo_ratio_qoq_diff_qoq_diff},
    "cas_drv3_006_debt_to_equity_qoq_diff_qoq_diff":            {"inputs": ["debt", "equity"],                           "func": cas_drv3_006_debt_to_equity_qoq_diff_qoq_diff},
    "cas_drv3_007_ncff_4q_sum_qoq_diff_qoq_diff":               {"inputs": ["ncff"],                                     "func": cas_drv3_007_ncff_4q_sum_qoq_diff_qoq_diff},
    "cas_drv3_008_ncfdebt_4q_sum_qoq_diff_qoq_diff":            {"inputs": ["ncfdebt"],                                  "func": cas_drv3_008_ncfdebt_4q_sum_qoq_diff_qoq_diff},
    "cas_drv3_009_dividends_qoq_diff_qoq_diff":                 {"inputs": ["dividends"],                                "func": cas_drv3_009_dividends_qoq_diff_qoq_diff},
    "cas_drv3_010_debtc_qoq_diff_qoq_diff":                     {"inputs": ["debtc"],                                    "func": cas_drv3_010_debtc_qoq_diff_qoq_diff},
    "cas_drv3_011_equity_qoq_diff_qoq_diff":                    {"inputs": ["equity"],                                   "func": cas_drv3_011_equity_qoq_diff_qoq_diff},
    "cas_drv3_012_intexp_qoq_diff_qoq_diff":                    {"inputs": ["intexp"],                                   "func": cas_drv3_012_intexp_qoq_diff_qoq_diff},
    "cas_drv3_013_net_debt_qoq_diff_qoq_diff":                  {"inputs": ["debt", "cashnequiv"],                       "func": cas_drv3_013_net_debt_qoq_diff_qoq_diff},
    "cas_drv3_014_ncff_zscore_qoq_diff_qoq_diff":               {"inputs": ["ncff"],                                     "func": cas_drv3_014_ncff_zscore_qoq_diff_qoq_diff},
    "cas_drv3_015_leverage_zscore_qoq_diff_qoq_diff":           {"inputs": ["debt", "equity"],                           "func": cas_drv3_015_leverage_zscore_qoq_diff_qoq_diff},
    "cas_drv3_016_ncff_slope_qoq_diff_qoq_diff":                {"inputs": ["ncff"],                                     "func": cas_drv3_016_ncff_slope_qoq_diff_qoq_diff},
    "cas_drv3_017_debtc_to_cash_ratio_qoq_diff_qoq_diff":       {"inputs": ["debtc", "cashnequiv"],                      "func": cas_drv3_017_debtc_to_cash_ratio_qoq_diff_qoq_diff},
    "cas_drv3_018_intexp_coverage_qoq_diff_qoq_diff":           {"inputs": ["ncfo", "intexp"],                           "func": cas_drv3_018_intexp_coverage_qoq_diff_qoq_diff},
    "cas_drv3_019_capital_return_qoq_diff_qoq_diff":            {"inputs": ["ncfcommon", "dividends"],                   "func": cas_drv3_019_capital_return_qoq_diff_qoq_diff},
    "cas_drv3_020_ncff_pct_rank_qoq_diff_qoq_diff":             {"inputs": ["ncff"],                                     "func": cas_drv3_020_ncff_pct_rank_qoq_diff_qoq_diff},
    "cas_drv3_021_ncfdebt_slope_qoq_diff_qoq_diff":             {"inputs": ["ncfdebt"],                                  "func": cas_drv3_021_ncfdebt_slope_qoq_diff_qoq_diff},
    "cas_drv3_022_ncfcommon_4q_sum_qoq_diff_qoq_diff":          {"inputs": ["ncfcommon"],                                "func": cas_drv3_022_ncfcommon_4q_sum_qoq_diff_qoq_diff},
    "cas_drv3_023_ncff_vs_ncfo_ratio_yoy_diff_qoq_diff":        {"inputs": ["ncff", "ncfo"],                             "func": cas_drv3_023_ncff_vs_ncfo_ratio_yoy_diff_qoq_diff},
    "cas_drv3_024_leverage_trend_slope_qoq_diff":               {"inputs": ["debt", "equity"],                           "func": cas_drv3_024_leverage_trend_slope_qoq_diff},
    "cas_drv3_025_external_stress_composite_qoq_diff_qoq_diff": {"inputs": ["ncff", "ncfdebt", "ncfcommon", "debt", "equity"], "func": cas_drv3_025_external_stress_composite_qoq_diff_qoq_diff},
}
