"""
78_marketcap_destruction — Base Features 076-150 (registry extended to 100)
Domain: market-capitalization destruction — magnitude and speed of market-cap decline
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
  NO raw price/volume or quarterly SF1 fundamental inputs.
All features are strictly backward-looking; no forward information is used.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


# ── Feature Functions 076-150 ──────────────────────────────────────────────────

# --- Group H (076-087): Volatility-adjusted and z-score of mc destruction ---

def mcd_076_mc_dd_252d_vol_adj(marketcap: pd.Series) -> pd.Series:
    """252-day mc drawdown divided by rolling std of daily mc pct changes (vol-adj)."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), _TD_YEAR)
    return _safe_div(dd, vol)


def mcd_077_mc_dd_504d_vol_adj(marketcap: pd.Series) -> pd.Series:
    """504-day mc drawdown divided by 504-day rolling std of daily mc pct changes."""
    pk  = _rolling_max(marketcap, 504)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), 504)
    return _safe_div(dd, vol)


def mcd_078_mc_dd_ath_vol_adj(marketcap: pd.Series) -> pd.Series:
    """ATH mc drawdown divided by expanding std of daily mc pct changes."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    vol = marketcap.pct_change(1).expanding(min_periods=5).std()
    return _safe_div(dd, vol)


def mcd_079_mc_dd_zscore_252d(marketcap: pd.Series) -> pd.Series:
    """Z-score of 252-day mc drawdown over a trailing 252-day window."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _zscore_rolling(dd, _TD_YEAR)


def mcd_080_mc_dd_zscore_504d(marketcap: pd.Series) -> pd.Series:
    """Z-score of 252-day mc drawdown over a trailing 504-day window."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _zscore_rolling(dd, 504)


def mcd_081_mc_dd_zscore_1260d(marketcap: pd.Series) -> pd.Series:
    """Z-score of 1260-day mc drawdown over trailing 1260-day window."""
    pk = _rolling_max(marketcap, 1260)
    dd = _safe_div(marketcap - pk, pk)
    return _zscore_rolling(dd, 1260)


def mcd_082_mc_dd_expanding_zscore(marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of ATH mc drawdown (how extreme vs own history)."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    m  = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    return _safe_div(dd - m, sd)


def mcd_083_mc_dd_pct_rank_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of 252-day mc drawdown within trailing 252-day window."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def mcd_084_mc_dd_pct_rank_1260d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of ATH mc drawdown within trailing 1260-day window."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return dd.rolling(1260, min_periods=630).rank(pct=True)


def mcd_085_mc_dd_expanding_pct_rank(marketcap: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day mc drawdown (all-history rank)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.expanding(min_periods=5).rank(pct=True)


def mcd_086_ev_dd_zscore_252d(ev: pd.Series) -> pd.Series:
    """Z-score of 252-day EV drawdown over trailing 252-day window."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return _zscore_rolling(dd, _TD_YEAR)


def mcd_087_ev_dd_pct_rank_252d(ev: pd.Series) -> pd.Series:
    """Percentile rank of 252-day EV drawdown within trailing 252-day window."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


# --- Group I (088-098): Multi-window drawdown ratios and intensity ---

def mcd_088_mc_dd_ratio_63d_to_252d(marketcap: pd.Series) -> pd.Series:
    """Ratio of 63-day mc dd to 252-day mc dd (recent vs annual severity)."""
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    return _safe_div(dd63, dd252)


def mcd_089_mc_dd_ratio_21d_to_252d(marketcap: pd.Series) -> pd.Series:
    """Ratio of 21-day mc dd to 252-day mc dd (short vs annual severity)."""
    pk21  = _rolling_max(marketcap, _TD_MON)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd21  = _safe_div(marketcap - pk21,  pk21)
    dd252 = _safe_div(marketcap - pk252, pk252)
    return _safe_div(dd21, dd252)


def mcd_090_mc_dd_ratio_252d_to_ath(marketcap: pd.Series) -> pd.Series:
    """Ratio of 252-day mc dd to ATH mc dd (recent fraction of total destruction)."""
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    pkath = marketcap.expanding(min_periods=1).max()
    dd252 = _safe_div(marketcap - pk252, pk252)
    ddath = _safe_div(marketcap - pkath, pkath)
    return _safe_div(dd252, ddath)


def mcd_091_mc_dd_ratio_504d_to_ath(marketcap: pd.Series) -> pd.Series:
    """Ratio of 504-day mc dd to ATH mc dd."""
    pk504 = _rolling_max(marketcap, 504)
    pkath = marketcap.expanding(min_periods=1).max()
    dd504 = _safe_div(marketcap - pk504, pk504)
    ddath = _safe_div(marketcap - pkath, pkath)
    return _safe_div(dd504, ddath)


def mcd_092_mc_dd_intensity_252d(marketcap: pd.Series) -> pd.Series:
    """Current 252-day mc dd as fraction of trailing 252-day maximum drawdown."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    mdd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(dd, mdd)


def mcd_093_mc_dd_intensity_1260d(marketcap: pd.Series) -> pd.Series:
    """Current 252-day mc dd as fraction of trailing 1260-day maximum drawdown."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    mdd = _rolling_min(dd, 1260)
    return _safe_div(dd, mdd)


def mcd_094_mc_dd_intensity_ath(marketcap: pd.Series) -> pd.Series:
    """ATH mc dd as fraction of expanding maximum ATH drawdown."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    mdd = dd.expanding(min_periods=1).min()
    return _safe_div(dd, mdd)


def mcd_095_mc_ev_dd_spread_252d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Difference between 252-day EV drawdown and mc drawdown (net debt amplification)."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    return dd_ev - dd_mc


def mcd_096_mc_dd_accel_21d(marketcap: pd.Series) -> pd.Series:
    """Acceleration of 63-day mc drawdown: change in drawdown over trailing 21 days."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return dd - dd.shift(_TD_MON)


def mcd_097_mc_dd_accel_63d(marketcap: pd.Series) -> pd.Series:
    """Acceleration of 252-day mc drawdown: change in drawdown over trailing 63 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd - dd.shift(_TD_QTR)


def mcd_098_mc_dd_composite_weighted(marketcap: pd.Series) -> pd.Series:
    """Composite mc drawdown: 50% 21d + 30% 63d + 20% 252d (multi-scale severity)."""
    pk21  = _rolling_max(marketcap, _TD_MON)
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd21  = _safe_div(marketcap - pk21,  pk21)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    return 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252


# --- Group J (099-110): Drawdown area / persistence / avg depth ---

def mcd_099_mc_avg_dd_63d(marketcap: pd.Series) -> pd.Series:
    """Mean 63-day mc drawdown depth over trailing 63 days."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_mean(dd, _TD_QTR)


def mcd_100_mc_avg_dd_252d(marketcap: pd.Series) -> pd.Series:
    """Mean 252-day mc drawdown depth over trailing 252 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_mean(dd, _TD_YEAR)


def mcd_101_mc_avg_dd_504d(marketcap: pd.Series) -> pd.Series:
    """Mean 252-day mc drawdown depth over trailing 504 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_mean(dd, 504)


def mcd_102_mc_dd_area_63d(marketcap: pd.Series) -> pd.Series:
    """Sum of 63-day mc drawdown values over trailing 63 days (area under curve)."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_sum(dd, _TD_QTR)


def mcd_103_mc_dd_area_252d(marketcap: pd.Series) -> pd.Series:
    """Sum of 252-day mc drawdown values over trailing 252 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_sum(dd, _TD_YEAR)


def mcd_104_mc_underwater_fraction_63d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 63 days where mc was below its own prior 63d peak."""
    pk = _rolling_max(marketcap, _TD_QTR)
    below = (marketcap < pk).astype(float)
    return _rolling_mean(below, _TD_QTR)


def mcd_105_mc_underwater_fraction_252d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 252 days where mc was below its own prior 252d peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    below = (marketcap < pk).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def mcd_106_mc_underwater_fraction_504d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 504 days where mc was below prior 252d peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    below = (marketcap < pk).astype(float)
    return _rolling_mean(below, 504)


def mcd_107_mc_dd_vol_of_dd_63d(marketcap: pd.Series) -> pd.Series:
    """Std dev of 63-day mc drawdown series over trailing 63 days."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_std(dd, _TD_QTR)


def mcd_108_mc_dd_vol_of_dd_252d(marketcap: pd.Series) -> pd.Series:
    """Std dev of 252-day mc drawdown series over trailing 252 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_std(dd, _TD_YEAR)


def mcd_109_mc_dd_tail_q05_252d(marketcap: pd.Series) -> pd.Series:
    """5th percentile of 252-day mc drawdown over trailing 252-day window (tail risk)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def mcd_110_ev_avg_dd_252d(ev: pd.Series) -> pd.Series:
    """Mean 252-day EV drawdown depth over trailing 252 days."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return _rolling_mean(dd, _TD_YEAR)


# --- Group K (111-122): Absolute marketcap level / tier-crossing metrics ---

def mcd_111_mc_log_level(marketcap: pd.Series) -> pd.Series:
    """Log of current marketcap (raw scale indicator)."""
    return _log_safe(marketcap)


def mcd_112_mc_log_level_vs_252d_avg(marketcap: pd.Series) -> pd.Series:
    """Log marketcap minus log of 252-day avg marketcap (log-compression measure)."""
    return _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, _TD_YEAR))


def mcd_113_mc_log_level_vs_504d_avg(marketcap: pd.Series) -> pd.Series:
    """Log marketcap minus log of 504-day avg marketcap."""
    return _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, 504))


def mcd_114_mc_log_level_vs_all_time_avg(marketcap: pd.Series) -> pd.Series:
    """Log marketcap minus log of expanding-mean marketcap."""
    return _log_safe(marketcap) - _log_safe(marketcap.expanding(min_periods=1).mean())


def mcd_115_mc_is_below_300m(marketcap: pd.Series) -> pd.Series:
    """Binary: 1 if marketcap < 300M (micro-cap territory), 0 otherwise."""
    return (marketcap < 300.0).astype(float)


def mcd_116_mc_is_below_2b(marketcap: pd.Series) -> pd.Series:
    """Binary: 1 if marketcap < 2B (small-cap territory), 0 otherwise."""
    return (marketcap < 2000.0).astype(float)


def mcd_117_mc_is_below_10b(marketcap: pd.Series) -> pd.Series:
    """Binary: 1 if marketcap < 10B (mid-cap territory), 0 otherwise."""
    return (marketcap < 10000.0).astype(float)


def mcd_118_mc_days_below_252d_median(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 252d where mc was below its own 252-day rolling median."""
    med = _rolling_median(marketcap, _TD_YEAR)
    below = (marketcap < med).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def mcd_119_mc_vs_252d_median(marketcap: pd.Series) -> pd.Series:
    """Percent deviation of mc from its 252-day rolling median."""
    med = _rolling_median(marketcap, _TD_YEAR)
    return _safe_div(marketcap - med, med)


def mcd_120_mc_vs_504d_median(marketcap: pd.Series) -> pd.Series:
    """Percent deviation of mc from its 504-day rolling median."""
    med = _rolling_median(marketcap, 504)
    return _safe_div(marketcap - med, med)


def mcd_121_mc_tier_crossings_down_252d(marketcap: pd.Series) -> pd.Series:
    """Number of times mc crossed below a tier boundary (300M/2B/10B) in last 252 days."""
    tiers = [300.0, 2000.0, 10000.0]
    crosses = pd.Series(0.0, index=marketcap.index)
    for t in tiers:
        above_prev = (marketcap.shift(1) >= t).astype(float)
        below_now  = (marketcap < t).astype(float)
        cross      = (above_prev * below_now)
        crosses   += cross
    return _rolling_sum(crosses, _TD_YEAR)


def mcd_122_ev_log_level(ev: pd.Series) -> pd.Series:
    """Log of current enterprise value (raw EV scale indicator)."""
    return _log_safe(ev)


# --- Group L (123-135): EV destruction detail and combined MC/EV metrics ---

def mcd_123_ev_log_dd_from_252d_peak(ev: pd.Series) -> pd.Series:
    """Log-space EV drawdown from 252-day peak."""
    pk = _rolling_max(ev, _TD_YEAR)
    return _log_safe(ev) - _log_safe(pk)


def mcd_124_ev_log_dd_from_all_time_peak(ev: pd.Series) -> pd.Series:
    """Log-space EV drawdown from all-time peak."""
    pk = ev.expanding(min_periods=1).max()
    return _log_safe(ev) - _log_safe(pk)


def mcd_125_ev_log_dd_from_504d_peak(ev: pd.Series) -> pd.Series:
    """Log-space EV drawdown from 504-day peak."""
    pk = _rolling_max(ev, 504)
    return _log_safe(ev) - _log_safe(pk)


def mcd_126_ev_fraction_peak_remaining(ev: pd.Series) -> pd.Series:
    """Fraction of all-time peak EV still remaining."""
    pk = ev.expanding(min_periods=1).max()
    return _safe_div(ev, pk)


def mcd_127_ev_fraction_252d_peak_remaining(ev: pd.Series) -> pd.Series:
    """Fraction of 252-day peak EV still remaining."""
    pk = _rolling_max(ev, _TD_YEAR)
    return _safe_div(ev, pk)


def mcd_128_mc_ev_ratio(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Ratio of marketcap to enterprise value (leverage-adjusted cap fraction)."""
    return _safe_div(marketcap, ev)


def mcd_129_mc_ev_ratio_vs_252d_avg(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """MC/EV ratio vs its 252-day trailing average (ratio compression measure)."""
    ratio = _safe_div(marketcap, ev)
    avg   = _rolling_mean(ratio, _TD_YEAR)
    return _safe_div(ratio - avg, avg)


def mcd_130_mc_ev_ratio_zscore_252d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Z-score of MC/EV ratio over trailing 252-day window."""
    ratio = _safe_div(marketcap, ev)
    return _zscore_rolling(ratio, _TD_YEAR)


def mcd_131_ev_mc_dd_divergence_252d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Absolute difference between 252-day EV dd fraction and mc dd fraction."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    return (dd_ev - dd_mc).abs()


def mcd_132_mc_dd_skew_252d(marketcap: pd.Series) -> pd.Series:
    """Skewness of daily mc pct changes over trailing 252 days (left-tail signature)."""
    return marketcap.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def mcd_133_mc_dd_kurt_252d(marketcap: pd.Series) -> pd.Series:
    """Excess kurtosis of daily mc pct changes over trailing 252 days (fat tail)."""
    return marketcap.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).kurt()


def mcd_134_ev_worst_5d_drop_in_63d(ev: pd.Series) -> pd.Series:
    """Worst single 5-day pct drop in EV within trailing 63-day window."""
    chg = ev.pct_change(5)
    return chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()


def mcd_135_ev_down_days_fraction_63d(ev: pd.Series) -> pd.Series:
    """Fraction of days in last 63d where EV pct change was negative."""
    down = (ev.pct_change(1) < 0).astype(float)
    return _rolling_mean(down, _TD_QTR)


# --- Group M (136-150): Magnitude / speed combos, EWM, and composite signals ---

def mcd_136_mc_ewm_dd_from_peak_21d(marketcap: pd.Series) -> pd.Series:
    """EWM-smoothed (21d span) drawdown from 252-day peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _ewm_mean(dd, _TD_MON)


def mcd_137_mc_ewm_dd_from_peak_63d(marketcap: pd.Series) -> pd.Series:
    """EWM-smoothed (63d span) drawdown from 252-day peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _ewm_mean(dd, _TD_QTR)


def mcd_138_mc_ewm_log_dd_ath_21d(marketcap: pd.Series) -> pd.Series:
    """EWM-smoothed (21d span) log ATH drawdown."""
    pk   = marketcap.expanding(min_periods=1).max()
    logdd = _log_safe(marketcap) - _log_safe(pk)
    return _ewm_mean(logdd, _TD_MON)


def mcd_139_mc_daily_loss_vol_63d(marketcap: pd.Series) -> pd.Series:
    """Annualized volatility of daily mc pct changes over trailing 63 days."""
    chg = marketcap.pct_change(1)
    return _rolling_std(chg, _TD_QTR) * np.sqrt(_TD_YEAR)


def mcd_140_mc_daily_loss_vol_252d(marketcap: pd.Series) -> pd.Series:
    """Annualized volatility of daily mc pct changes over trailing 252 days."""
    chg = marketcap.pct_change(1)
    return _rolling_std(chg, _TD_YEAR) * np.sqrt(_TD_YEAR)


def mcd_141_mc_loss_vol_ratio_63_to_252(marketcap: pd.Series) -> pd.Series:
    """Ratio of 63-day annualized mc vol to 252-day annualized mc vol (vol spike)."""
    chg  = marketcap.pct_change(1)
    v63  = _rolling_std(chg, _TD_QTR)
    v252 = _rolling_std(chg, _TD_YEAR)
    return _safe_div(v63, v252)


def mcd_142_mc_dd_convexity_252d(marketcap: pd.Series) -> pd.Series:
    """Convexity of 252-day mc drawdown: avg-dd / max-dd ratio over 252 days."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    avg  = _rolling_mean(dd, _TD_YEAR)
    mxdd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(avg, mxdd)


def mcd_143_mc_dd_recovery_speed_63d(marketcap: pd.Series) -> pd.Series:
    """Ratio of 63-day mc change to absolute mc loss from 252-day peak (recovery urgency)."""
    chg63 = marketcap.pct_change(_TD_QTR)
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd252 = _safe_div(marketcap - pk, pk)
    return _safe_div(chg63, dd252.abs())


def mcd_144_mc_peak_age_days(marketcap: pd.Series) -> pd.Series:
    """Days since 252-day peak marketcap was set (peak staleness)."""
    def _days_since_max(x):
        if len(x) == 0:
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return marketcap.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_days_since_max, raw=True)


def mcd_145_mc_ath_peak_age_days(marketcap: pd.Series) -> pd.Series:
    """Days since the all-time (expanding) peak marketcap was set."""
    def _days_since_ath(x):
        if len(x) == 0:
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return marketcap.expanding(min_periods=1).apply(_days_since_ath, raw=True)


def mcd_146_mc_dd_vs_vol_ratio_expanding(marketcap: pd.Series) -> pd.Series:
    """Expanding ratio of ATH mc drawdown to expanding std of daily mc chg."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    vol = marketcap.pct_change(1).expanding(min_periods=5).std()
    return _safe_div(dd, vol)


def mcd_147_mc_rolling_sharpe_destruction_252d(marketcap: pd.Series) -> pd.Series:
    """Rolling 252-day Sharpe of daily mc pct changes (negative = net destruction)."""
    chg  = marketcap.pct_change(1)
    mu   = _rolling_mean(chg, _TD_YEAR)
    sigma = _rolling_std(chg, _TD_YEAR)
    return _safe_div(mu, sigma)


def mcd_148_ev_rolling_sharpe_destruction_252d(ev: pd.Series) -> pd.Series:
    """Rolling 252-day Sharpe of daily EV pct changes."""
    chg  = ev.pct_change(1)
    mu   = _rolling_mean(chg, _TD_YEAR)
    sigma = _rolling_std(chg, _TD_YEAR)
    return _safe_div(mu, sigma)


def mcd_149_mc_ev_combined_dd_avg(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Average of 252-day mc drawdown and 252-day EV drawdown (combined destruction)."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    return (dd_mc + dd_ev) / 2.0


def mcd_150_mc_dd_speed_index(marketcap: pd.Series) -> pd.Series:
    """Speed index: 252-day mc dd divided by days-since-peak (dd per trading day elapsed)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    def _days_since_max(x):
        if len(x) == 0:
            return np.nan
        idx = int(np.argmax(x))
        d   = float(len(x) - 1 - idx)
        return max(d, 1.0)
    age = marketcap.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_days_since_max, raw=True)
    return _safe_div(dd, age)


# --- Group N (176-185): EV persistence and combined ratio extensions ---

def mcd_176_ev_dd_from_504d_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value vs 504-day rolling peak (EV destruction fraction, 2-year)."""
    pk = _rolling_max(ev, 504)
    return _safe_div(ev - pk, pk)


def mcd_177_ev_dd_from_126d_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value vs 126-day rolling peak (EV destruction fraction, half-year)."""
    pk = _rolling_max(ev, _TD_HALF)
    return _safe_div(ev - pk, pk)


def mcd_178_ev_worst_63d_drop_in_504d(ev: pd.Series) -> pd.Series:
    """Worst single 63-day pct drop in EV within trailing 504-day window."""
    chg = ev.pct_change(_TD_QTR)
    return chg.rolling(504, min_periods=252).min()


def mcd_179_ev_pct_above_252d_low(ev: pd.Series) -> pd.Series:
    """Percent EV above 252-day low (distance from trough)."""
    lo = _rolling_min(ev, _TD_YEAR)
    return _safe_div(ev - lo, lo)


def mcd_180_ev_vs_sma252(ev: pd.Series) -> pd.Series:
    """EV deviation from its 252-day trailing average (pct)."""
    ma = _rolling_mean(ev, _TD_YEAR)
    return _safe_div(ev - ma, ma)


def mcd_181_ev_vs_sma63(ev: pd.Series) -> pd.Series:
    """EV deviation from its 63-day trailing average (pct)."""
    ma = _rolling_mean(ev, _TD_QTR)
    return _safe_div(ev - ma, ma)


def mcd_182_ev_zscore_252d(ev: pd.Series) -> pd.Series:
    """Z-score of EV relative to trailing 252-day distribution."""
    return _zscore_rolling(ev, _TD_YEAR)


def mcd_183_ev_underwater_fraction_252d(ev: pd.Series) -> pd.Series:
    """Fraction of last 252 days where EV was below its own prior 252-day peak."""
    pk = _rolling_max(ev, _TD_YEAR)
    below = (ev < pk).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def mcd_184_ev_avg_dd_504d(ev: pd.Series) -> pd.Series:
    """Mean 252-day EV drawdown depth over trailing 504 days."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return _rolling_mean(dd, 504)


def mcd_185_ev_dd_zscore_504d(ev: pd.Series) -> pd.Series:
    """Z-score of 252-day EV drawdown over trailing 504-day window."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return _zscore_rolling(dd, 504)


# --- Group O (186-195): Marketcap tail-risk and higher-moment extensions ---

def mcd_186_mc_dd_tail_q10_252d(marketcap: pd.Series) -> pd.Series:
    """10th percentile of 252-day mc drawdown over trailing 252-day window."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)


def mcd_187_mc_dd_tail_q01_252d(marketcap: pd.Series) -> pd.Series:
    """1st percentile of 252-day mc drawdown over trailing 252-day window (extreme tail)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.01)


def mcd_188_mc_dd_skew_504d(marketcap: pd.Series) -> pd.Series:
    """Skewness of daily mc pct changes over trailing 504 days."""
    return marketcap.pct_change(1).rolling(504, min_periods=_TD_QTR).skew()


def mcd_189_mc_dd_kurt_504d(marketcap: pd.Series) -> pd.Series:
    """Excess kurtosis of daily mc pct changes over trailing 504 days."""
    return marketcap.pct_change(1).rolling(504, min_periods=_TD_QTR).kurt()


def mcd_190_mc_dd_area_252d_normalized(marketcap: pd.Series) -> pd.Series:
    """Sum of 252-day mc drawdown normalized by current drawdown depth (persistence ratio)."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_YEAR)
    return _safe_div(area, dd.abs() + _EPS)


def mcd_191_mc_underwater_fraction_126d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 126 days where mc was below its own prior 126-day peak."""
    pk = _rolling_max(marketcap, _TD_HALF)
    below = (marketcap < pk).astype(float)
    return _rolling_mean(below, _TD_HALF)


def mcd_192_mc_dd_vol_of_dd_126d(marketcap: pd.Series) -> pd.Series:
    """Std dev of 126-day mc drawdown series over trailing 126 days."""
    pk = _rolling_max(marketcap, _TD_HALF)
    dd = _safe_div(marketcap - pk, pk)
    return _rolling_std(dd, _TD_HALF)


def mcd_193_mc_dd_composite_3tier(marketcap: pd.Series) -> pd.Series:
    """Composite mc drawdown: 40% 63d + 35% 252d + 25% ATH (tiered multi-scale severity)."""
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    pkath = marketcap.expanding(min_periods=1).max()
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    ddath = _safe_div(marketcap - pkath, pkath)
    return 0.40 * dd63 + 0.35 * dd252 + 0.25 * ddath


def mcd_194_mc_dd_accel_5d(marketcap: pd.Series) -> pd.Series:
    """Acceleration of 252-day mc drawdown: change in drawdown over trailing 5 days."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd - dd.shift(5)


def mcd_195_mc_dd_ratio_5d_to_252d(marketcap: pd.Series) -> pd.Series:
    """Ratio of 5-day mc dd to 252-day mc dd (weekly vs annual severity)."""
    pk5   = _rolling_max(marketcap, _TD_WEEK)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd5   = _safe_div(marketcap - pk5,   pk5)
    dd252 = _safe_div(marketcap - pk252, pk252)
    return _safe_div(dd5, dd252)


# --- Group P (196-200): Peak-age and recovery extensions ---

def mcd_196_mc_peak_age_days_504d(marketcap: pd.Series) -> pd.Series:
    """Days since 504-day peak marketcap was set (peak staleness, 2-year window)."""
    def _days_since_max(x):
        if len(x) == 0:
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return marketcap.rolling(504, min_periods=252).apply(_days_since_max, raw=True)


def mcd_197_mc_dd_recovery_speed_21d(marketcap: pd.Series) -> pd.Series:
    """Ratio of 21-day mc change to absolute mc loss from 252-day peak (short recovery urgency)."""
    chg21 = marketcap.pct_change(_TD_MON)
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd252 = _safe_div(marketcap - pk, pk)
    return _safe_div(chg21, dd252.abs())


def mcd_198_mc_rolling_sharpe_destruction_126d(marketcap: pd.Series) -> pd.Series:
    """Rolling 126-day Sharpe of daily mc pct changes (half-year net destruction ratio)."""
    chg   = marketcap.pct_change(1)
    mu    = _rolling_mean(chg, _TD_HALF)
    sigma = _rolling_std(chg, _TD_HALF)
    return _safe_div(mu, sigma)


def mcd_199_mc_ev_combined_dd_max(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Maximum (worst) of 252-day mc drawdown and 252-day EV drawdown."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    return pd.concat([dd_mc, dd_ev], axis=1).min(axis=1)


def mcd_200_mc_daily_loss_vol_126d(marketcap: pd.Series) -> pd.Series:
    """Annualized volatility of daily mc pct changes over trailing 126 days."""
    chg = marketcap.pct_change(1)
    return _rolling_std(chg, _TD_HALF) * np.sqrt(_TD_YEAR)


# ── Registry ───────────────────────────────────────────────────────────────────

MARKETCAP_DESTRUCTION_REGISTRY_076_150 = {
    "mcd_076_mc_dd_252d_vol_adj":            {"inputs": ["marketcap"], "func": mcd_076_mc_dd_252d_vol_adj},
    "mcd_077_mc_dd_504d_vol_adj":            {"inputs": ["marketcap"], "func": mcd_077_mc_dd_504d_vol_adj},
    "mcd_078_mc_dd_ath_vol_adj":             {"inputs": ["marketcap"], "func": mcd_078_mc_dd_ath_vol_adj},
    "mcd_079_mc_dd_zscore_252d":             {"inputs": ["marketcap"], "func": mcd_079_mc_dd_zscore_252d},
    "mcd_080_mc_dd_zscore_504d":             {"inputs": ["marketcap"], "func": mcd_080_mc_dd_zscore_504d},
    "mcd_081_mc_dd_zscore_1260d":            {"inputs": ["marketcap"], "func": mcd_081_mc_dd_zscore_1260d},
    "mcd_082_mc_dd_expanding_zscore":        {"inputs": ["marketcap"], "func": mcd_082_mc_dd_expanding_zscore},
    "mcd_083_mc_dd_pct_rank_252d":           {"inputs": ["marketcap"], "func": mcd_083_mc_dd_pct_rank_252d},
    "mcd_084_mc_dd_pct_rank_1260d":          {"inputs": ["marketcap"], "func": mcd_084_mc_dd_pct_rank_1260d},
    "mcd_085_mc_dd_expanding_pct_rank":      {"inputs": ["marketcap"], "func": mcd_085_mc_dd_expanding_pct_rank},
    "mcd_086_ev_dd_zscore_252d":             {"inputs": ["ev"],        "func": mcd_086_ev_dd_zscore_252d},
    "mcd_087_ev_dd_pct_rank_252d":           {"inputs": ["ev"],        "func": mcd_087_ev_dd_pct_rank_252d},
    "mcd_088_mc_dd_ratio_63d_to_252d":       {"inputs": ["marketcap"], "func": mcd_088_mc_dd_ratio_63d_to_252d},
    "mcd_089_mc_dd_ratio_21d_to_252d":       {"inputs": ["marketcap"], "func": mcd_089_mc_dd_ratio_21d_to_252d},
    "mcd_090_mc_dd_ratio_252d_to_ath":       {"inputs": ["marketcap"], "func": mcd_090_mc_dd_ratio_252d_to_ath},
    "mcd_091_mc_dd_ratio_504d_to_ath":       {"inputs": ["marketcap"], "func": mcd_091_mc_dd_ratio_504d_to_ath},
    "mcd_092_mc_dd_intensity_252d":          {"inputs": ["marketcap"], "func": mcd_092_mc_dd_intensity_252d},
    "mcd_093_mc_dd_intensity_1260d":         {"inputs": ["marketcap"], "func": mcd_093_mc_dd_intensity_1260d},
    "mcd_094_mc_dd_intensity_ath":           {"inputs": ["marketcap"], "func": mcd_094_mc_dd_intensity_ath},
    "mcd_095_mc_ev_dd_spread_252d":          {"inputs": ["marketcap", "ev"], "func": mcd_095_mc_ev_dd_spread_252d},
    "mcd_096_mc_dd_accel_21d":               {"inputs": ["marketcap"], "func": mcd_096_mc_dd_accel_21d},
    "mcd_097_mc_dd_accel_63d":               {"inputs": ["marketcap"], "func": mcd_097_mc_dd_accel_63d},
    "mcd_098_mc_dd_composite_weighted":      {"inputs": ["marketcap"], "func": mcd_098_mc_dd_composite_weighted},
    "mcd_099_mc_avg_dd_63d":                 {"inputs": ["marketcap"], "func": mcd_099_mc_avg_dd_63d},
    "mcd_100_mc_avg_dd_252d":                {"inputs": ["marketcap"], "func": mcd_100_mc_avg_dd_252d},
    "mcd_101_mc_avg_dd_504d":                {"inputs": ["marketcap"], "func": mcd_101_mc_avg_dd_504d},
    "mcd_102_mc_dd_area_63d":                {"inputs": ["marketcap"], "func": mcd_102_mc_dd_area_63d},
    "mcd_103_mc_dd_area_252d":               {"inputs": ["marketcap"], "func": mcd_103_mc_dd_area_252d},
    "mcd_104_mc_underwater_fraction_63d":    {"inputs": ["marketcap"], "func": mcd_104_mc_underwater_fraction_63d},
    "mcd_105_mc_underwater_fraction_252d":   {"inputs": ["marketcap"], "func": mcd_105_mc_underwater_fraction_252d},
    "mcd_106_mc_underwater_fraction_504d":   {"inputs": ["marketcap"], "func": mcd_106_mc_underwater_fraction_504d},
    "mcd_107_mc_dd_vol_of_dd_63d":           {"inputs": ["marketcap"], "func": mcd_107_mc_dd_vol_of_dd_63d},
    "mcd_108_mc_dd_vol_of_dd_252d":          {"inputs": ["marketcap"], "func": mcd_108_mc_dd_vol_of_dd_252d},
    "mcd_109_mc_dd_tail_q05_252d":           {"inputs": ["marketcap"], "func": mcd_109_mc_dd_tail_q05_252d},
    "mcd_110_ev_avg_dd_252d":                {"inputs": ["ev"],        "func": mcd_110_ev_avg_dd_252d},
    "mcd_111_mc_log_level":                  {"inputs": ["marketcap"], "func": mcd_111_mc_log_level},
    "mcd_112_mc_log_level_vs_252d_avg":      {"inputs": ["marketcap"], "func": mcd_112_mc_log_level_vs_252d_avg},
    "mcd_113_mc_log_level_vs_504d_avg":      {"inputs": ["marketcap"], "func": mcd_113_mc_log_level_vs_504d_avg},
    "mcd_114_mc_log_level_vs_all_time_avg":  {"inputs": ["marketcap"], "func": mcd_114_mc_log_level_vs_all_time_avg},
    "mcd_115_mc_is_below_300m":              {"inputs": ["marketcap"], "func": mcd_115_mc_is_below_300m},
    "mcd_116_mc_is_below_2b":               {"inputs": ["marketcap"], "func": mcd_116_mc_is_below_2b},
    "mcd_117_mc_is_below_10b":              {"inputs": ["marketcap"], "func": mcd_117_mc_is_below_10b},
    "mcd_118_mc_days_below_252d_median":     {"inputs": ["marketcap"], "func": mcd_118_mc_days_below_252d_median},
    "mcd_119_mc_vs_252d_median":             {"inputs": ["marketcap"], "func": mcd_119_mc_vs_252d_median},
    "mcd_120_mc_vs_504d_median":             {"inputs": ["marketcap"], "func": mcd_120_mc_vs_504d_median},
    "mcd_121_mc_tier_crossings_down_252d":   {"inputs": ["marketcap"], "func": mcd_121_mc_tier_crossings_down_252d},
    "mcd_122_ev_log_level":                  {"inputs": ["ev"],        "func": mcd_122_ev_log_level},
    "mcd_123_ev_log_dd_from_252d_peak":      {"inputs": ["ev"],        "func": mcd_123_ev_log_dd_from_252d_peak},
    "mcd_124_ev_log_dd_from_all_time_peak":  {"inputs": ["ev"],        "func": mcd_124_ev_log_dd_from_all_time_peak},
    "mcd_125_ev_log_dd_from_504d_peak":      {"inputs": ["ev"],        "func": mcd_125_ev_log_dd_from_504d_peak},
    "mcd_126_ev_fraction_peak_remaining":    {"inputs": ["ev"],        "func": mcd_126_ev_fraction_peak_remaining},
    "mcd_127_ev_fraction_252d_peak_remaining": {"inputs": ["ev"],      "func": mcd_127_ev_fraction_252d_peak_remaining},
    "mcd_128_mc_ev_ratio":                   {"inputs": ["marketcap", "ev"], "func": mcd_128_mc_ev_ratio},
    "mcd_129_mc_ev_ratio_vs_252d_avg":       {"inputs": ["marketcap", "ev"], "func": mcd_129_mc_ev_ratio_vs_252d_avg},
    "mcd_130_mc_ev_ratio_zscore_252d":       {"inputs": ["marketcap", "ev"], "func": mcd_130_mc_ev_ratio_zscore_252d},
    "mcd_131_ev_mc_dd_divergence_252d":      {"inputs": ["marketcap", "ev"], "func": mcd_131_ev_mc_dd_divergence_252d},
    "mcd_132_mc_dd_skew_252d":               {"inputs": ["marketcap"], "func": mcd_132_mc_dd_skew_252d},
    "mcd_133_mc_dd_kurt_252d":               {"inputs": ["marketcap"], "func": mcd_133_mc_dd_kurt_252d},
    "mcd_134_ev_worst_5d_drop_in_63d":       {"inputs": ["ev"],        "func": mcd_134_ev_worst_5d_drop_in_63d},
    "mcd_135_ev_down_days_fraction_63d":     {"inputs": ["ev"],        "func": mcd_135_ev_down_days_fraction_63d},
    "mcd_136_mc_ewm_dd_from_peak_21d":       {"inputs": ["marketcap"], "func": mcd_136_mc_ewm_dd_from_peak_21d},
    "mcd_137_mc_ewm_dd_from_peak_63d":       {"inputs": ["marketcap"], "func": mcd_137_mc_ewm_dd_from_peak_63d},
    "mcd_138_mc_ewm_log_dd_ath_21d":         {"inputs": ["marketcap"], "func": mcd_138_mc_ewm_log_dd_ath_21d},
    "mcd_139_mc_daily_loss_vol_63d":         {"inputs": ["marketcap"], "func": mcd_139_mc_daily_loss_vol_63d},
    "mcd_140_mc_daily_loss_vol_252d":        {"inputs": ["marketcap"], "func": mcd_140_mc_daily_loss_vol_252d},
    "mcd_141_mc_loss_vol_ratio_63_to_252":   {"inputs": ["marketcap"], "func": mcd_141_mc_loss_vol_ratio_63_to_252},
    "mcd_142_mc_dd_convexity_252d":          {"inputs": ["marketcap"], "func": mcd_142_mc_dd_convexity_252d},
    "mcd_143_mc_dd_recovery_speed_63d":      {"inputs": ["marketcap"], "func": mcd_143_mc_dd_recovery_speed_63d},
    "mcd_144_mc_peak_age_days":              {"inputs": ["marketcap"], "func": mcd_144_mc_peak_age_days},
    "mcd_145_mc_ath_peak_age_days":          {"inputs": ["marketcap"], "func": mcd_145_mc_ath_peak_age_days},
    "mcd_146_mc_dd_vs_vol_ratio_expanding":  {"inputs": ["marketcap"], "func": mcd_146_mc_dd_vs_vol_ratio_expanding},
    "mcd_147_mc_rolling_sharpe_destruction_252d": {"inputs": ["marketcap"], "func": mcd_147_mc_rolling_sharpe_destruction_252d},
    "mcd_148_ev_rolling_sharpe_destruction_252d": {"inputs": ["ev"],    "func": mcd_148_ev_rolling_sharpe_destruction_252d},
    "mcd_149_mc_ev_combined_dd_avg":         {"inputs": ["marketcap", "ev"], "func": mcd_149_mc_ev_combined_dd_avg},
    "mcd_150_mc_dd_speed_index":             {"inputs": ["marketcap"], "func": mcd_150_mc_dd_speed_index},
    "mcd_176_ev_dd_from_504d_peak":          {"inputs": ["ev"],        "func": mcd_176_ev_dd_from_504d_peak},
    "mcd_177_ev_dd_from_126d_peak":          {"inputs": ["ev"],        "func": mcd_177_ev_dd_from_126d_peak},
    "mcd_178_ev_worst_63d_drop_in_504d":     {"inputs": ["ev"],        "func": mcd_178_ev_worst_63d_drop_in_504d},
    "mcd_179_ev_pct_above_252d_low":         {"inputs": ["ev"],        "func": mcd_179_ev_pct_above_252d_low},
    "mcd_180_ev_vs_sma252":                  {"inputs": ["ev"],        "func": mcd_180_ev_vs_sma252},
    "mcd_181_ev_vs_sma63":                   {"inputs": ["ev"],        "func": mcd_181_ev_vs_sma63},
    "mcd_182_ev_zscore_252d":                {"inputs": ["ev"],        "func": mcd_182_ev_zscore_252d},
    "mcd_183_ev_underwater_fraction_252d":   {"inputs": ["ev"],        "func": mcd_183_ev_underwater_fraction_252d},
    "mcd_184_ev_avg_dd_504d":                {"inputs": ["ev"],        "func": mcd_184_ev_avg_dd_504d},
    "mcd_185_ev_dd_zscore_504d":             {"inputs": ["ev"],        "func": mcd_185_ev_dd_zscore_504d},
    "mcd_186_mc_dd_tail_q10_252d":           {"inputs": ["marketcap"], "func": mcd_186_mc_dd_tail_q10_252d},
    "mcd_187_mc_dd_tail_q01_252d":           {"inputs": ["marketcap"], "func": mcd_187_mc_dd_tail_q01_252d},
    "mcd_188_mc_dd_skew_504d":               {"inputs": ["marketcap"], "func": mcd_188_mc_dd_skew_504d},
    "mcd_189_mc_dd_kurt_504d":               {"inputs": ["marketcap"], "func": mcd_189_mc_dd_kurt_504d},
    "mcd_190_mc_dd_area_252d_normalized":    {"inputs": ["marketcap"], "func": mcd_190_mc_dd_area_252d_normalized},
    "mcd_191_mc_underwater_fraction_126d":   {"inputs": ["marketcap"], "func": mcd_191_mc_underwater_fraction_126d},
    "mcd_192_mc_dd_vol_of_dd_126d":          {"inputs": ["marketcap"], "func": mcd_192_mc_dd_vol_of_dd_126d},
    "mcd_193_mc_dd_composite_3tier":         {"inputs": ["marketcap"], "func": mcd_193_mc_dd_composite_3tier},
    "mcd_194_mc_dd_accel_5d":               {"inputs": ["marketcap"], "func": mcd_194_mc_dd_accel_5d},
    "mcd_195_mc_dd_ratio_5d_to_252d":        {"inputs": ["marketcap"], "func": mcd_195_mc_dd_ratio_5d_to_252d},
    "mcd_196_mc_peak_age_days_504d":         {"inputs": ["marketcap"], "func": mcd_196_mc_peak_age_days_504d},
    "mcd_197_mc_dd_recovery_speed_21d":      {"inputs": ["marketcap"], "func": mcd_197_mc_dd_recovery_speed_21d},
    "mcd_198_mc_rolling_sharpe_destruction_126d": {"inputs": ["marketcap"], "func": mcd_198_mc_rolling_sharpe_destruction_126d},
    "mcd_199_mc_ev_combined_dd_max":         {"inputs": ["marketcap", "ev"], "func": mcd_199_mc_ev_combined_dd_max},
    "mcd_200_mc_daily_loss_vol_126d":        {"inputs": ["marketcap"], "func": mcd_200_mc_daily_loss_vol_126d},
}
