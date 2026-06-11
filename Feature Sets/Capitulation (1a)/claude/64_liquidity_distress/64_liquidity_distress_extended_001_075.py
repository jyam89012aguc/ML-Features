"""
64_liquidity_distress — Extended Features 001-075
Domain: short-term liquidity collapse — deeper variants of current/quick/cash
        ratios, additional windows, smoothings, z-scores, percentile ranks,
        streaks, composite distress signals, and cross-ratio confluence.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract: inputs are already daily-frequency
Series forward-filled from the most recent quarterly SF1 report. Functions
look strictly backward. 1 quarter = 63 trading days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_EPS     = 1e-9

# ── Alignment helper ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.abs().replace(0, np.nan)


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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Derived ratio builders ─────────────────────────────────────────────────────

def _current_ratio(assetsc, liabilitiesc):
    return _safe_div(assetsc, liabilitiesc)

def _quick_ratio(assetsc, inventory, liabilitiesc):
    return _safe_div(assetsc - inventory, liabilitiesc)

def _cash_ratio(cashnequiv, liabilitiesc):
    return _safe_div(cashnequiv, liabilitiesc)


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Additional ratio windows and smoothings ---

def lqd_ext_001_current_ratio_min_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Worst (minimum) current ratio in trailing 4-quarter (252-day) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_min(cr, _TD_YEAR)


def lqd_ext_002_current_ratio_min_8q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Worst current ratio in trailing 8-quarter window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_min(cr, _TD_2Y)


def lqd_ext_003_current_ratio_min_12q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Worst current ratio in trailing 12-quarter (3-year) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_min(cr, _TD_3Y)


def lqd_ext_004_current_ratio_expanding_min(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding minimum current ratio (worst-ever level)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr.expanding(min_periods=1).min()


def lqd_ext_005_current_ratio_median_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 4-quarter median current ratio (robust central tendency)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_median(cr, _TD_YEAR)


def lqd_ext_006_current_ratio_ewm_deviation(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its 8-quarter EWM (span=504) — slower momentum deviation."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    ewm = _ewm_mean(cr, _TD_2Y)
    return cr - ewm


def lqd_ext_007_quick_ratio_min_4q(assetsc: pd.Series, inventory: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Worst quick ratio in trailing 4-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_min(qr, _TD_YEAR)


def lqd_ext_008_quick_ratio_min_8q(assetsc: pd.Series, inventory: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Worst quick ratio in trailing 8-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_min(qr, _TD_2Y)


def lqd_ext_009_cash_ratio_min_4q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Worst cash ratio in trailing 4-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_min(cr, _TD_YEAR)


def lqd_ext_010_cash_ratio_min_8q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Worst cash ratio in trailing 8-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_min(cr, _TD_2Y)


def lqd_ext_011_cash_ratio_expanding_min(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding minimum cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr.expanding(min_periods=1).min()


def lqd_ext_012_current_ratio_range_8q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """8-quarter current ratio range: max - min (volatility of liquidity)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_max(cr, _TD_2Y) - _rolling_min(cr, _TD_2Y)


# --- Group B (013-022): Z-score and pct-rank extensions ---

def lqd_ext_013_quick_ratio_zscore_8q(assetsc: pd.Series, inventory: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of quick ratio within trailing 8-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _zscore_rolling(qr, _TD_2Y)


def lqd_ext_014_cash_ratio_zscore_8q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of cash ratio within trailing 8-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _zscore_rolling(cr, _TD_2Y)


def lqd_ext_015_current_ratio_pct_rank_12q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of current ratio within trailing 12-quarter window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_3Y)


def lqd_ext_016_current_ratio_expanding_pct_rank_v2(assetsc: pd.Series,
                                                     liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of current ratio (extended variant)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr.expanding(min_periods=2).rank(pct=True)


def lqd_ext_017_quick_ratio_pct_rank_8q(assetsc: pd.Series, inventory: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of quick ratio within trailing 8-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_rank_pct(qr, _TD_2Y)


def lqd_ext_018_quick_ratio_expanding_pct_rank(assetsc: pd.Series, inventory: pd.Series,
                                                liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of quick ratio."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr.expanding(min_periods=2).rank(pct=True)


def lqd_ext_019_cash_ratio_pct_rank_8q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of cash ratio within trailing 8-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_2Y)


def lqd_ext_020_cash_ratio_expanding_pct_rank(cashnequiv: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr.expanding(min_periods=2).rank(pct=True)


def lqd_ext_021_current_ratio_zscore_expanding(assetsc: pd.Series,
                                                liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding z-score of current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    m  = cr.expanding(min_periods=2).mean()
    sd = cr.expanding(min_periods=2).std()
    return _safe_div(cr - m, sd)


def lqd_ext_022_cash_ratio_zscore_expanding(cashnequiv: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """All-history expanding z-score of cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    m  = cr.expanding(min_periods=2).mean()
    sd = cr.expanding(min_periods=2).std()
    return _safe_div(cr - m, sd)


# --- Group C (023-033): Additional threshold breach flags and streaks ---

def lqd_ext_023_current_ratio_below_05_flag(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current ratio < 0.5 (severe liquidity collapse)."""
    return (_current_ratio(assetsc, liabilitiesc) < 0.5).astype(float)


def lqd_ext_024_cash_ratio_below_01_flag(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if cash ratio < 0.10 (extreme cash shortage)."""
    return (_cash_ratio(cashnequiv, liabilitiesc) < 0.10).astype(float)


def lqd_ext_025_quick_ratio_below_05_flag(assetsc: pd.Series, inventory: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if quick ratio < 0.5."""
    return (_quick_ratio(assetsc, inventory, liabilitiesc) < 0.5).astype(float)


def lqd_ext_026_current_ratio_below_1_fraction_2y(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Fraction of trailing 2-year (504-day) window where current ratio < 1.0."""
    flag = (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(float)
    return _rolling_mean(flag, _TD_2Y)


def lqd_ext_027_current_ratio_below_1_fraction_3y(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where current ratio < 1.0."""
    flag = (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(float)
    return _rolling_mean(flag, _TD_3Y)


def lqd_ext_028_current_ratio_consecutive_below_1_streak(assetsc: pd.Series,
                                                          liabilitiesc: pd.Series) -> pd.Series:
    """Consecutive daily observations where current ratio < 1.0 (streak length)."""
    below = (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(int)
    arr   = below.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assetsc.index)


def lqd_ext_029_quick_ratio_consecutive_below_1_streak(assetsc: pd.Series, inventory: pd.Series,
                                                        liabilitiesc: pd.Series) -> pd.Series:
    """Consecutive days where quick ratio < 1.0 (streak length)."""
    below = (_quick_ratio(assetsc, inventory, liabilitiesc) < 1.0).astype(int)
    arr   = below.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assetsc.index)


def lqd_ext_030_all_three_ratios_below_1_flag(assetsc: pd.Series, inventory: pd.Series,
                                               cashnequiv: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """1 when current, quick AND cash ratios are all < 1.0 simultaneously."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    return ((cr < 1.0) & (qr < 1.0) & (car < 1.0)).astype(float)


def lqd_ext_031_all_three_ratios_below_1_fraction_2y(assetsc: pd.Series, inventory: pd.Series,
                                                      cashnequiv: pd.Series,
                                                      liabilitiesc: pd.Series) -> pd.Series:
    """Fraction of trailing 2-year window where CR, QR, and cash ratio all < 1.0."""
    flag = lqd_ext_030_all_three_ratios_below_1_flag(assetsc, inventory, cashnequiv, liabilitiesc)
    return _rolling_mean(flag, _TD_2Y)


def lqd_ext_032_current_ratio_declining_streak(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Days current ratio has been consecutively declining vs prior day (longer streak variant)."""
    cr     = _current_ratio(assetsc, liabilitiesc)
    down   = (cr < cr.shift(1)).astype(int)
    arr    = down.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assetsc.index)


def lqd_ext_033_current_ratio_below_1_turned_below_075(assetsc: pd.Series,
                                                        liabilitiesc: pd.Series) -> pd.Series:
    """1 when CR crosses below 0.75 from >= 0.75 in prior quarter."""
    cr     = _current_ratio(assetsc, liabilitiesc)
    now    = (cr < 0.75).astype(float)
    before = (cr.shift(_TD_QTR) >= 0.75).astype(float)
    return now * before


# --- Group D (034-045): Drawdown extensions ---

def lqd_ext_034_current_ratio_pct_drawdown_8q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of current ratio from its 8-quarter peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_2Y)
    return _safe_div_abs(cr - peak, peak)


def lqd_ext_035_current_ratio_pct_drawdown_12q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of current ratio from its 12-quarter peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_3Y)
    return _safe_div_abs(cr - peak, peak)


def lqd_ext_036_quick_ratio_pct_drawdown_8q(assetsc: pd.Series, inventory: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of quick ratio from its 8-quarter peak."""
    qr   = _quick_ratio(assetsc, inventory, liabilitiesc)
    peak = _rolling_max(qr, _TD_2Y)
    return _safe_div_abs(qr - peak, peak)


def lqd_ext_037_quick_ratio_drawdown_expanding_pct(assetsc: pd.Series, inventory: pd.Series,
                                                    liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of quick ratio from its all-history expanding peak."""
    qr   = _quick_ratio(assetsc, inventory, liabilitiesc)
    peak = qr.expanding(min_periods=1).max()
    return _safe_div_abs(qr - peak, peak)


def lqd_ext_038_cash_ratio_drawdown_12q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio minus its 12-quarter trailing peak (absolute level drawdown)."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - _rolling_max(cr, _TD_3Y)


def lqd_ext_039_cash_ratio_pct_drawdown_expanding(cashnequiv: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of cash ratio from its all-history expanding peak."""
    cr   = _cash_ratio(cashnequiv, liabilitiesc)
    peak = cr.expanding(min_periods=1).max()
    return _safe_div_abs(cr - peak, peak)


def lqd_ext_040_current_ratio_range_position_8q(assetsc: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """CR position within its 8-quarter [min, max] range: (cr-min)/(max-min)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    lo = _rolling_min(cr, _TD_2Y)
    hi = _rolling_max(cr, _TD_2Y)
    return _safe_div(cr - lo, hi - lo)


def lqd_ext_041_quick_ratio_range_position_4q(assetsc: pd.Series, inventory: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio position within its 4-quarter [min, max] range."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    lo = _rolling_min(qr, _TD_YEAR)
    hi = _rolling_max(qr, _TD_YEAR)
    return _safe_div(qr - lo, hi - lo)


def lqd_ext_042_cashnequiv_pct_drawdown_from_8q_peak(cashnequiv: pd.Series) -> pd.Series:
    """Percent drawdown of cash & equivalents from its 8-quarter peak."""
    peak = _rolling_max(cashnequiv, _TD_2Y)
    return _safe_div_abs(cashnequiv - peak, peak)


def lqd_ext_043_cashnequiv_pct_drawdown_from_expanding(cashnequiv: pd.Series) -> pd.Series:
    """Percent drawdown of cash & equivalents from its all-history expanding peak."""
    peak = cashnequiv.expanding(min_periods=1).max()
    return _safe_div_abs(cashnequiv - peak, peak)


def lqd_ext_044_working_capital_pct_drawdown_4q(assetsc: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of absolute working capital from its 4-quarter peak."""
    wc   = assetsc - liabilitiesc
    peak = _rolling_max(wc, _TD_YEAR)
    return _safe_div_abs(wc - peak, peak)


def lqd_ext_045_working_capital_pct_drawdown_8q(assetsc: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of absolute working capital from its 8-quarter peak."""
    wc   = assetsc - liabilitiesc
    peak = _rolling_max(wc, _TD_2Y)
    return _safe_div_abs(wc - peak, peak)


# --- Group E (046-057): Trend-slope, acceleration, and EWM variants ---

def lqd_ext_046_current_ratio_trend_slope_4q(assetsc: pd.Series,
                                              liabilitiesc: pd.Series) -> pd.Series:
    """OLS slope of current ratio over trailing 4 quarters (252 td)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return cr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=False)


def lqd_ext_047_quick_ratio_trend_slope_4q(assetsc: pd.Series, inventory: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """OLS slope of quick ratio over trailing 4 quarters."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return qr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=False)


def lqd_ext_048_current_ratio_qoq_acceleration(assetsc: pd.Series,
                                                liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ change of current ratio (second difference = acceleration)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    d1 = cr - cr.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_ext_049_cash_ratio_trend_slope_4q(cashnequiv: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """OLS slope of cash ratio over trailing 4 quarters."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return cr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=False)


def lqd_ext_050_current_ratio_3y_change(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in current ratio over 3 years (756-day lag)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_3Y)


def lqd_ext_051_quick_ratio_2y_change(assetsc: pd.Series, inventory: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in quick ratio over 2 years (504-day lag)."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_2Y)


def lqd_ext_052_cash_ratio_2y_change(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in cash ratio over 2 years (504-day lag)."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_2Y)


def lqd_ext_053_current_ratio_ewm_8q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio EWM (span=504) — very slow-moving baseline for deviation."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _ewm_mean(cr, _TD_2Y)


def lqd_ext_054_current_ratio_below_ewm_252_flag(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """1 when current ratio is below its 1-year EWM (below trend)."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    ewm = _ewm_mean(cr, _TD_YEAR)
    return (cr < ewm).astype(float)


def lqd_ext_055_liabilitiesc_trend_slope_4q(liabilitiesc: pd.Series) -> pd.Series:
    """OLS slope of current liabilities over trailing 4 quarters (rising = pressure)."""
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return liabilitiesc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=False)


def lqd_ext_056_assetsc_trend_slope_4q(assetsc: pd.Series) -> pd.Series:
    """OLS slope of current assets over trailing 4 quarters."""
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return assetsc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=False)


def lqd_ext_057_debtc_to_liabilitiesc(debtc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Short-term debt as fraction of total current liabilities (maturing debt share)."""
    return _safe_div(debtc, liabilitiesc)


# --- Group F (058-068): Composite, multi-ratio, and cross-signal features ---

def lqd_ext_058_liquidity_composite_zscore_8q(assetsc: pd.Series, inventory: pd.Series,
                                               cashnequiv: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """Composite: equally weighted z-score sum of CR, QR, cash-ratio in 8-quarter window."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    z_cr  = _zscore_rolling(cr,  _TD_2Y)
    z_qr  = _zscore_rolling(qr,  _TD_2Y)
    z_car = _zscore_rolling(car, _TD_2Y)
    return (z_cr + z_qr + z_car) / 3.0


def lqd_ext_059_liquidity_pct_rank_composite(assetsc: pd.Series, inventory: pd.Series,
                                              cashnequiv: pd.Series,
                                              liabilitiesc: pd.Series) -> pd.Series:
    """Composite pct-rank: equally weighted (CR rank + QR rank + cash-ratio rank) / 3
    within 4-quarter window. Low = liquidity at its worst recent level."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    r_cr  = _rolling_rank_pct(cr,  _TD_YEAR)
    r_qr  = _rolling_rank_pct(qr,  _TD_YEAR)
    r_car = _rolling_rank_pct(car, _TD_YEAR)
    return (r_cr + r_qr + r_car) / 3.0


def lqd_ext_060_cr_minus_qr_spread(assetsc: pd.Series, inventory: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """CR - QR spread (widening = inventory becoming a larger fraction of current assets)."""
    return _current_ratio(assetsc, liabilitiesc) - _quick_ratio(assetsc, inventory, liabilitiesc)


def lqd_ext_061_cr_minus_qr_spread_zscore_4q(assetsc: pd.Series, inventory: pd.Series,
                                              liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of CR - QR spread within 4-quarter window."""
    spread = lqd_ext_060_cr_minus_qr_spread(assetsc, inventory, liabilitiesc)
    return _zscore_rolling(spread, _TD_YEAR)


def lqd_ext_062_qr_minus_cash_ratio_spread(assetsc: pd.Series, inventory: pd.Series,
                                            cashnequiv: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """QR - cash ratio spread (receivables-reliance signal)."""
    return _quick_ratio(assetsc, inventory, liabilitiesc) - _cash_ratio(cashnequiv, liabilitiesc)


def lqd_ext_063_payables_ratio_yoy_change(payables: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in payables/cash ratio — rising = stretched payment burden vs cash."""
    ratio = _safe_div(payables, cashnequiv)
    return ratio - ratio.shift(_TD_YEAR)


def lqd_ext_064_debtc_to_cashnequiv_yoy_change(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in short-term debt / cash (maturing debt pressure increasing)."""
    ratio = _safe_div(debtc, cashnequiv)
    return ratio - ratio.shift(_TD_YEAR)


def lqd_ext_065_debtc_to_cashnequiv_zscore_4q(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of short-term debt / cash within 4-quarter window."""
    ratio = _safe_div(debtc, cashnequiv)
    return _zscore_rolling(ratio, _TD_YEAR)


def lqd_ext_066_debtc_to_cashnequiv_pct_rank_4q(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Pct rank of short-term debt / cash within 4-quarter window."""
    ratio = _safe_div(debtc, cashnequiv)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lqd_ext_067_investmentsc_to_liabilitiesc_ratio(investmentsc: pd.Series,
                                                    liabilitiesc: pd.Series) -> pd.Series:
    """Short-term investments / current liabilities — additional liquid coverage."""
    return _safe_div(investmentsc, liabilitiesc)


def lqd_ext_068_investmentsc_to_liabilitiesc_yoy_change(investmentsc: pd.Series,
                                                         liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in short-term investments / current liabilities."""
    ratio = _safe_div(investmentsc, liabilitiesc)
    return ratio - ratio.shift(_TD_YEAR)


# --- Group G (069-075): EWM composite and final severity composites ---

def lqd_ext_069_current_ratio_below_qr_flag(assetsc: pd.Series, inventory: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """1 if CR < QR (impossible if inventory >= 0, signals data anomaly / negative inventory)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return (cr < qr).astype(float)


def lqd_ext_070_cashnequiv_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 4-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_YEAR)


def lqd_ext_071_cashnequiv_zscore_8q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 8-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_2Y)


def lqd_ext_072_cashnequiv_pct_rank_4q(cashnequiv: pd.Series) -> pd.Series:
    """Pct rank of cash & equivalents within trailing 4-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_YEAR)


def lqd_ext_073_cashnequiv_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Pct rank of cash & equivalents within trailing 8-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_2Y)


def lqd_ext_074_liquidity_stress_combined_flag(assetsc: pd.Series, inventory: pd.Series,
                                               cashnequiv: pd.Series,
                                               liabilitiesc: pd.Series,
                                               debtc: pd.Series) -> pd.Series:
    """Binary: 1 when CR < 1 AND QR < 0.75 AND cash < short-term debt (triple stress)."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    qr    = _quick_ratio(assetsc, inventory, liabilitiesc)
    below = (cashnequiv < debtc).astype(float)
    return ((cr < 1.0) & (qr < 0.75)).astype(float) * below


def lqd_ext_075_liquidity_capitulation_composite(assetsc: pd.Series, inventory: pd.Series,
                                                  cashnequiv: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """Liquidity capitulation composite: weighted sum of inverted pct-ranks in 8Q window.
    0.4*(1-CR_rank) + 0.35*(1-QR_rank) + 0.25*(1-cash_ratio_rank). Higher = more distressed."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    qr    = _quick_ratio(assetsc, inventory, liabilitiesc)
    car   = _cash_ratio(cashnequiv, liabilitiesc)
    r_cr  = _rolling_rank_pct(cr,  _TD_2Y)
    r_qr  = _rolling_rank_pct(qr,  _TD_2Y)
    r_car = _rolling_rank_pct(car, _TD_2Y)
    return 0.40 * (1.0 - r_cr) + 0.35 * (1.0 - r_qr) + 0.25 * (1.0 - r_car)


# ── Registry ───────────────────────────────────────────────────────────────────

LIQUIDITY_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "lqd_ext_001_current_ratio_min_4q":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_001_current_ratio_min_4q},
    "lqd_ext_002_current_ratio_min_8q":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_002_current_ratio_min_8q},
    "lqd_ext_003_current_ratio_min_12q":                {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_003_current_ratio_min_12q},
    "lqd_ext_004_current_ratio_expanding_min":          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_004_current_ratio_expanding_min},
    "lqd_ext_005_current_ratio_median_4q":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_005_current_ratio_median_4q},
    "lqd_ext_006_current_ratio_ewm_deviation":          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_006_current_ratio_ewm_deviation},
    "lqd_ext_007_quick_ratio_min_4q":                   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_007_quick_ratio_min_4q},
    "lqd_ext_008_quick_ratio_min_8q":                   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_008_quick_ratio_min_8q},
    "lqd_ext_009_cash_ratio_min_4q":                    {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_009_cash_ratio_min_4q},
    "lqd_ext_010_cash_ratio_min_8q":                    {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_010_cash_ratio_min_8q},
    "lqd_ext_011_cash_ratio_expanding_min":             {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_011_cash_ratio_expanding_min},
    "lqd_ext_012_current_ratio_range_8q":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_012_current_ratio_range_8q},
    "lqd_ext_013_quick_ratio_zscore_8q":                {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_013_quick_ratio_zscore_8q},
    "lqd_ext_014_cash_ratio_zscore_8q":                 {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_014_cash_ratio_zscore_8q},
    "lqd_ext_015_current_ratio_pct_rank_12q":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_015_current_ratio_pct_rank_12q},
    "lqd_ext_016_current_ratio_expanding_pct_rank_v2":  {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_016_current_ratio_expanding_pct_rank_v2},
    "lqd_ext_017_quick_ratio_pct_rank_8q":              {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_017_quick_ratio_pct_rank_8q},
    "lqd_ext_018_quick_ratio_expanding_pct_rank":       {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_018_quick_ratio_expanding_pct_rank},
    "lqd_ext_019_cash_ratio_pct_rank_8q":               {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_019_cash_ratio_pct_rank_8q},
    "lqd_ext_020_cash_ratio_expanding_pct_rank":        {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_020_cash_ratio_expanding_pct_rank},
    "lqd_ext_021_current_ratio_zscore_expanding":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_021_current_ratio_zscore_expanding},
    "lqd_ext_022_cash_ratio_zscore_expanding":          {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_022_cash_ratio_zscore_expanding},
    "lqd_ext_023_current_ratio_below_05_flag":          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_023_current_ratio_below_05_flag},
    "lqd_ext_024_cash_ratio_below_01_flag":             {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_024_cash_ratio_below_01_flag},
    "lqd_ext_025_quick_ratio_below_05_flag":            {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_025_quick_ratio_below_05_flag},
    "lqd_ext_026_current_ratio_below_1_fraction_2y":   {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_026_current_ratio_below_1_fraction_2y},
    "lqd_ext_027_current_ratio_below_1_fraction_3y":   {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_027_current_ratio_below_1_fraction_3y},
    "lqd_ext_028_current_ratio_consec_below_1_streak":  {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_028_current_ratio_consecutive_below_1_streak},
    "lqd_ext_029_quick_ratio_consec_below_1_streak":    {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_029_quick_ratio_consecutive_below_1_streak},
    "lqd_ext_030_all_three_ratios_below_1_flag":        {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_030_all_three_ratios_below_1_flag},
    "lqd_ext_031_all_three_ratios_below_1_frac_2y":    {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_031_all_three_ratios_below_1_fraction_2y},
    "lqd_ext_032_current_ratio_declining_streak":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_032_current_ratio_declining_streak},
    "lqd_ext_033_current_ratio_turned_below_075":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_033_current_ratio_below_1_turned_below_075},
    "lqd_ext_034_current_ratio_pct_drawdown_8q":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_034_current_ratio_pct_drawdown_8q},
    "lqd_ext_035_current_ratio_pct_drawdown_12q":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_035_current_ratio_pct_drawdown_12q},
    "lqd_ext_036_quick_ratio_pct_drawdown_8q":          {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_036_quick_ratio_pct_drawdown_8q},
    "lqd_ext_037_quick_ratio_drawdown_expanding_pct":   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_037_quick_ratio_drawdown_expanding_pct},
    "lqd_ext_038_cash_ratio_drawdown_12q":              {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_038_cash_ratio_drawdown_12q},
    "lqd_ext_039_cash_ratio_pct_drawdown_expanding":    {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_039_cash_ratio_pct_drawdown_expanding},
    "lqd_ext_040_current_ratio_range_position_8q":      {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_040_current_ratio_range_position_8q},
    "lqd_ext_041_quick_ratio_range_position_4q":        {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_041_quick_ratio_range_position_4q},
    "lqd_ext_042_cashnequiv_pct_drawdown_from_8q_peak": {"inputs": ["cashnequiv"],                                           "func": lqd_ext_042_cashnequiv_pct_drawdown_from_8q_peak},
    "lqd_ext_043_cashnequiv_pct_drawdown_from_expanding":{"inputs": ["cashnequiv"],                                          "func": lqd_ext_043_cashnequiv_pct_drawdown_from_expanding},
    "lqd_ext_044_working_capital_pct_drawdown_4q":      {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_044_working_capital_pct_drawdown_4q},
    "lqd_ext_045_working_capital_pct_drawdown_8q":      {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_045_working_capital_pct_drawdown_8q},
    "lqd_ext_046_current_ratio_trend_slope_4q":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_046_current_ratio_trend_slope_4q},
    "lqd_ext_047_quick_ratio_trend_slope_4q":           {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_047_quick_ratio_trend_slope_4q},
    "lqd_ext_048_current_ratio_qoq_acceleration":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_048_current_ratio_qoq_acceleration},
    "lqd_ext_049_cash_ratio_trend_slope_4q":            {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_049_cash_ratio_trend_slope_4q},
    "lqd_ext_050_current_ratio_3y_change":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_050_current_ratio_3y_change},
    "lqd_ext_051_quick_ratio_2y_change":                {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_051_quick_ratio_2y_change},
    "lqd_ext_052_cash_ratio_2y_change":                 {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_ext_052_cash_ratio_2y_change},
    "lqd_ext_053_current_ratio_ewm_8q":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_053_current_ratio_ewm_8q},
    "lqd_ext_054_current_ratio_below_ewm_252_flag":     {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_ext_054_current_ratio_below_ewm_252_flag},
    "lqd_ext_055_liabilitiesc_trend_slope_4q":          {"inputs": ["liabilitiesc"],                                         "func": lqd_ext_055_liabilitiesc_trend_slope_4q},
    "lqd_ext_056_assetsc_trend_slope_4q":               {"inputs": ["assetsc"],                                              "func": lqd_ext_056_assetsc_trend_slope_4q},
    "lqd_ext_057_debtc_to_liabilitiesc":                {"inputs": ["debtc", "liabilitiesc"],                                "func": lqd_ext_057_debtc_to_liabilitiesc},
    "lqd_ext_058_liquidity_composite_zscore_8q":        {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_058_liquidity_composite_zscore_8q},
    "lqd_ext_059_liquidity_pct_rank_composite":         {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_059_liquidity_pct_rank_composite},
    "lqd_ext_060_cr_minus_qr_spread":                   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_060_cr_minus_qr_spread},
    "lqd_ext_061_cr_minus_qr_spread_zscore_4q":         {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_061_cr_minus_qr_spread_zscore_4q},
    "lqd_ext_062_qr_minus_cash_ratio_spread":           {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_062_qr_minus_cash_ratio_spread},
    "lqd_ext_063_payables_ratio_yoy_change":            {"inputs": ["payables", "cashnequiv"],                               "func": lqd_ext_063_payables_ratio_yoy_change},
    "lqd_ext_064_debtc_to_cashnequiv_yoy_change":       {"inputs": ["debtc", "cashnequiv"],                                  "func": lqd_ext_064_debtc_to_cashnequiv_yoy_change},
    "lqd_ext_065_debtc_to_cashnequiv_zscore_4q":        {"inputs": ["debtc", "cashnequiv"],                                  "func": lqd_ext_065_debtc_to_cashnequiv_zscore_4q},
    "lqd_ext_066_debtc_to_cashnequiv_pct_rank_4q":      {"inputs": ["debtc", "cashnequiv"],                                  "func": lqd_ext_066_debtc_to_cashnequiv_pct_rank_4q},
    "lqd_ext_067_investmentsc_to_liabilitiesc_ratio":   {"inputs": ["investmentsc", "liabilitiesc"],                         "func": lqd_ext_067_investmentsc_to_liabilitiesc_ratio},
    "lqd_ext_068_investmentsc_to_liabilitiesc_yoy":     {"inputs": ["investmentsc", "liabilitiesc"],                         "func": lqd_ext_068_investmentsc_to_liabilitiesc_yoy_change},
    "lqd_ext_069_current_ratio_below_qr_flag":          {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_ext_069_current_ratio_below_qr_flag},
    "lqd_ext_070_cashnequiv_zscore_4q":                 {"inputs": ["cashnequiv"],                                           "func": lqd_ext_070_cashnequiv_zscore_4q},
    "lqd_ext_071_cashnequiv_zscore_8q":                 {"inputs": ["cashnequiv"],                                           "func": lqd_ext_071_cashnequiv_zscore_8q},
    "lqd_ext_072_cashnequiv_pct_rank_4q":               {"inputs": ["cashnequiv"],                                           "func": lqd_ext_072_cashnequiv_pct_rank_4q},
    "lqd_ext_073_cashnequiv_pct_rank_8q":               {"inputs": ["cashnequiv"],                                           "func": lqd_ext_073_cashnequiv_pct_rank_8q},
    "lqd_ext_074_liquidity_stress_combined_flag":       {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc", "debtc"], "func": lqd_ext_074_liquidity_stress_combined_flag},
    "lqd_ext_075_liquidity_capitulation_composite":     {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_ext_075_liquidity_capitulation_composite},
}
