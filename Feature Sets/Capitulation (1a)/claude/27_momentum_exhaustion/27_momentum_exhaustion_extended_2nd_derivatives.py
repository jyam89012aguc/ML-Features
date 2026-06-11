"""
27_momentum_exhaustion — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended-base momentum-exhaustion features — velocity of
extended exhaustion signals (ROC z-scores, Kaufman ER z-scores/pct-ranks/regime flags,
TD Sequential countdown/perfected-setup, ROC-of-ROC, deceleration confluence composites,
and exhaustion composite signals derived from the ext_001-075 extended base layer).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Self-contained: numpy/pandas only; no cross-file imports.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of Change over n periods."""
    return _safe_div(close, close.shift(n).replace(0, np.nan)) * 100.0 - 100.0


def _kaufman_er(close: pd.Series, n: int) -> pd.Series:
    """Kaufman Efficiency Ratio over n periods (0=choppy, 1=trending)."""
    direction = (close - close.shift(n)).abs()
    volatility = close.diff(1).abs().rolling(n, min_periods=max(2, n // 2)).sum()
    return _safe_div(direction, volatility)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    """TD/DeMark buy-setup running count (backward-looking); capped at 13."""
    condition = (close < close.shift(4)).astype(int).values
    n = len(condition)
    counts = np.full(n, np.nan, dtype=float)
    running = 0
    for i in range(4, n):
        if np.isnan(close.iloc[i]) or np.isnan(close.iloc[i - 4]):
            running = 0
            counts[i] = np.nan
        elif condition[i] == 1:
            running = min(running + 1, 13)
            counts[i] = float(running)
        else:
            running = 0
            counts[i] = 0.0
    return pd.Series(counts, index=close.index)


def _td_countdown_count(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """TD Sequential countdown count (0-13); backward-looking only."""
    setup = _td_buy_setup_count(close).values
    cd_cond = (close <= low.shift(2)).astype(int).values
    n = len(close)
    counts = np.full(n, np.nan, dtype=float)
    in_countdown = False
    cd_count = 0
    for i in range(n):
        if np.isnan(setup[i]):
            in_countdown = False
            cd_count = 0
            counts[i] = np.nan
            continue
        if setup[i] >= 9.0:
            in_countdown = True
            cd_count = 0
        if in_countdown:
            if cd_cond[i] == 1:
                cd_count = min(cd_count + 1, 13)
            counts[i] = float(cd_count)
        else:
            counts[i] = np.nan
    return pd.Series(counts, index=close.index)


def _td_perfected_setup_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """TD Perfected Buy Setup flag; backward-looking only."""
    setup = _td_buy_setup_count(close).values
    low_vals = low.values
    n = len(close)
    flags = np.full(n, np.nan, dtype=float)
    bar_lows = {}
    for i in range(n):
        s = setup[i]
        if np.isnan(s):
            bar_lows = {}
            flags[i] = np.nan
            continue
        bar_num = int(s)
        if bar_num == 0:
            bar_lows = {}
            flags[i] = 0.0
            continue
        bar_lows[bar_num] = low_vals[i]
        if bar_num >= 9:
            low_8 = bar_lows.get(8, np.nan)
            low_9 = bar_lows.get(9, np.nan)
            low_6 = bar_lows.get(6, np.nan)
            low_7 = bar_lows.get(7, np.nan)
            ref_low = min(v for v in [low_6, low_7] if not np.isnan(v)) if any(
                not np.isnan(v) for v in [low_6, low_7]) else np.nan
            cand_low = min(v for v in [low_8, low_9] if not np.isnan(v)) if any(
                not np.isnan(v) for v in [low_8, low_9]) else np.nan
            if np.isnan(ref_low) or np.isnan(cand_low):
                flags[i] = 0.0
            else:
                flags[i] = 1.0 if cand_low <= ref_low else 0.0
        else:
            flags[i] = 0.0
    return pd.Series(flags, index=close.index)


# ── Extended 2nd-Derivative Feature Functions (extdrv2_001-025) ───────────────

# --- Group A (extdrv2_001-005): ROC z-score and pct-rank velocity ---

def mex_extdrv2_001_roc_5d_zscore_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (z-score of 5d ROC within 126d distribution): velocity of ext_006."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_HALF)
    s = _rolling_std(roc5, _TD_HALF)
    z = _safe_div(roc5 - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_002_roc_21d_zscore_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (z-score of 21d ROC within 126d distribution): velocity of ext_007."""
    roc21 = _roc(close, _TD_MON)
    m = _rolling_mean(roc21, _TD_HALF)
    s = _rolling_std(roc21, _TD_HALF)
    z = _safe_div(roc21 - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_003_roc_63d_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (z-score of 63d ROC within 252d distribution): velocity of ext_008."""
    roc63 = _roc(close, _TD_QTR)
    m = _rolling_mean(roc63, _TD_YEAR)
    s = _rolling_std(roc63, _TD_YEAR)
    z = _safe_div(roc63 - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_004_roc_5d_pct_rank_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (percentile rank of 5d ROC within 126d distribution): velocity of ext_009."""
    roc5 = _roc(close, _TD_WEEK)
    pct = roc5.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    return pct.diff(_TD_WEEK)


def mex_extdrv2_005_roc_21d_pct_rank_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (percentile rank of 21d ROC within 126d distribution): velocity of ext_010."""
    roc21 = _roc(close, _TD_MON)
    pct = roc21.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    return pct.diff(_TD_MON)


# --- Group B (extdrv2_006-010): ROC range-position and regime-flag velocity ---

def mex_extdrv2_006_roc_21d_range_position_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21d ROC position in 252d min-max range): velocity of ext_017."""
    roc21 = _roc(close, _TD_MON)
    rmin = _rolling_min(roc21, _TD_YEAR)
    rmax = _rolling_max(roc21, _TD_YEAR)
    pos = _safe_div(roc21 - rmin, (rmax - rmin).replace(0, np.nan))
    return pos.diff(_TD_WEEK)


def mex_extdrv2_007_roc_63d_range_position_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (63d ROC position in 252d min-max range): velocity of ext_018."""
    roc63 = _roc(close, _TD_QTR)
    rmin = _rolling_min(roc63, _TD_YEAR)
    rmax = _rolling_max(roc63, _TD_YEAR)
    pos = _safe_div(roc63 - rmin, (rmax - rmin).replace(0, np.nan))
    return pos.diff(_TD_MON)


def mex_extdrv2_008_roc_42d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 42-day ROC: velocity of ext_002 (between-monthly-and-quarterly momentum change)."""
    roc42 = _roc(close, 42)
    return roc42.diff(_TD_WEEK)


def mex_extdrv2_009_roc_3d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 3-day ROC over 21 days: trend of ultra-short momentum (velocity of ext_001)."""
    roc3 = _roc(close, 3)
    return _linslope(roc3, _TD_MON)


def mex_extdrv2_010_roc_5d_neg_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (consecutive bars where 5d ROC < 0 streak count): velocity of ext_011."""
    roc5 = _roc(close, _TD_WEEK)
    is_neg = (roc5 < 0).astype(int).values
    n = len(is_neg)
    streak_arr = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc5.iloc[i]):
            streak = 0
            streak_arr[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            streak_arr[i] = float(streak)
        else:
            streak = 0
            streak_arr[i] = 0.0
    s = pd.Series(streak_arr, index=close.index)
    return s.diff(_TD_WEEK)


# --- Group C (extdrv2_011-015): Kaufman ER z-score and pct-rank velocity ---

def mex_extdrv2_011_kaufman_er_5d_zscore_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (z-score of Kaufman ER 5d within 63d distribution): velocity of ext_022."""
    er5 = _kaufman_er(close, _TD_WEEK)
    m = _rolling_mean(er5, _TD_QTR)
    s = _rolling_std(er5, _TD_QTR)
    z = _safe_div(er5 - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_012_kaufman_er_21d_zscore_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (z-score of Kaufman ER 21d within 126d distribution): velocity of ext_023."""
    er21 = _kaufman_er(close, _TD_MON)
    m = _rolling_mean(er21, _TD_HALF)
    s = _rolling_std(er21, _TD_HALF)
    z = _safe_div(er21 - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_013_kaufman_er_63d_zscore_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (z-score of Kaufman ER 63d within 252d distribution): velocity of ext_024."""
    er63 = _kaufman_er(close, _TD_QTR)
    m = _rolling_mean(er63, _TD_YEAR)
    s = _rolling_std(er63, _TD_YEAR)
    z = _safe_div(er63 - m, s)
    return z.diff(_TD_MON)


def mex_extdrv2_014_kaufman_er_5d_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (percentile rank of Kaufman ER 5d in 252d distribution): velocity of ext_025."""
    er5 = _kaufman_er(close, _TD_WEEK)
    pct = er5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def mex_extdrv2_015_kaufman_er_42d_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (percentile rank of Kaufman ER 42d in 252d distribution): velocity of ext_026."""
    er42 = _kaufman_er(close, 42)
    pct = er42.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


# --- Group D (extdrv2_016-020): TD Sequential and countdown velocity ---

def mex_extdrv2_016_td_countdown_count_5d_diff(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of TD countdown count: velocity of ext_035 progression toward 13."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    return cd.diff(_TD_WEEK)


def mex_extdrv2_017_td_countdown_zscore_63d_5d_diff(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of (z-score of TD countdown within 63d distribution): velocity of ext_038."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    m = _rolling_mean(cd, _TD_QTR)
    s = _rolling_std(cd, _TD_QTR)
    z = _safe_div(cd - m, s)
    return z.diff(_TD_WEEK)


def mex_extdrv2_018_td_countdown_pct_rank_252d_5d_diff(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of (percentile rank of TD countdown in 252d): velocity of ext_039."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    pct = cd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def mex_extdrv2_019_td_setup_count_pct_rank_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (percentile rank of TD setup count in 126d): velocity of ext_045."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    pct = counts.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    return pct.diff(_TD_WEEK)


def mex_extdrv2_020_td_perfected_setup_rate_63d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (rolling 63d rate of TD Perfected Buy Setup flags): velocity of ext_043."""
    flag = _td_perfected_setup_flag(close, low).fillna(0.0)
    rate = _rolling_mean(flag, _TD_QTR)
    return rate.diff(_TD_WEEK)


# --- Group E (extdrv2_021-025): Confluence/composite velocity ---

def mex_extdrv2_021_triple_roc_decel_confluence_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (confluence of 5d/21d/63d ROC all improving): velocity of ext_059."""
    roc5 = _roc(close, _TD_WEEK)
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    imp5 = (roc5 > roc5.shift(1)).astype(float)
    imp21 = (roc21 > roc21.shift(1)).astype(float)
    imp63 = (roc63 > roc63.shift(1)).astype(float)
    confluence = (imp5 + imp21 + imp63) / 3.0
    return confluence.diff(_TD_WEEK)


def mex_extdrv2_022_er_convergence_confluence_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (ER-5d/21d/63d all < 0.4 confluence): sustained choppiness trend from ext_060."""
    er5 = _kaufman_er(close, _TD_WEEK)
    er21 = _kaufman_er(close, _TD_MON)
    er63 = _kaufman_er(close, _TD_QTR)
    low5 = (er5 < 0.4).astype(float)
    low21 = (er21 < 0.4).astype(float)
    low63 = (er63 < 0.4).astype(float)
    confluence = (low5 + low21 + low63) / 3.0
    return _linslope(confluence, _TD_MON)


def mex_extdrv2_023_exhaustion_composite_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21d exhaustion composite z-score of ROC+ER+TD-setup): velocity of ext_064."""
    roc21 = _roc(close, _TD_MON)
    m_r = _rolling_mean(roc21, _TD_QTR)
    s_r = _rolling_std(roc21, _TD_QTR)
    z_roc = _safe_div(roc21 - m_r, s_r)

    er21 = _kaufman_er(close, _TD_MON)
    m_e = _rolling_mean(er21, _TD_QTR)
    s_e = _rolling_std(er21, _TD_QTR)
    z_er = _safe_div(er21 - m_e, s_e)

    counts = _td_buy_setup_count(close).fillna(0.0)
    m_t = _rolling_mean(counts, _TD_QTR)
    s_t = _rolling_std(counts, _TD_QTR)
    z_td = _safe_div(counts - m_t, s_t)

    composite = (z_roc.fillna(0.0) + z_er.fillna(0.0) + z_td.fillna(0.0)) / 3.0
    return composite.diff(_TD_WEEK)


def mex_extdrv2_024_exhaustion_composite_ema_smoothed_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (EMA-5 smoothed 21d exhaustion composite): trend of ext_068."""
    roc21 = _roc(close, _TD_MON)
    m_r = _rolling_mean(roc21, _TD_QTR)
    s_r = _rolling_std(roc21, _TD_QTR)
    z_roc = _safe_div(roc21 - m_r, s_r)

    er21 = _kaufman_er(close, _TD_MON)
    m_e = _rolling_mean(er21, _TD_QTR)
    s_e = _rolling_std(er21, _TD_QTR)
    z_er = _safe_div(er21 - m_e, s_e)

    counts = _td_buy_setup_count(close).fillna(0.0)
    m_t = _rolling_mean(counts, _TD_QTR)
    s_t = _rolling_std(counts, _TD_QTR)
    z_td = _safe_div(counts - m_t, s_t)

    composite = (z_roc.fillna(0.0) + z_er.fillna(0.0) + z_td.fillna(0.0)) / 3.0
    smoothed = _ewm_mean(composite, _TD_WEEK)
    return _linslope(smoothed, _TD_MON)


def mex_extdrv2_025_roc_er_divergence_score_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (ER-21d rising while 21d ROC falling divergence score): trend of ext_069."""
    roc21 = _roc(close, _TD_MON)
    er21 = _kaufman_er(close, _TD_MON)
    roc_falling = (roc21 < roc21.shift(1)).astype(float)
    er_rising = (er21 > er21.shift(1)).astype(float)
    divergence = roc_falling * er_rising
    return _linslope(divergence, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "mex_extdrv2_001_roc_5d_zscore_126d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_001_roc_5d_zscore_126d_5d_diff},
    "mex_extdrv2_002_roc_21d_zscore_126d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_002_roc_21d_zscore_126d_5d_diff},
    "mex_extdrv2_003_roc_63d_zscore_252d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_003_roc_63d_zscore_252d_5d_diff},
    "mex_extdrv2_004_roc_5d_pct_rank_126d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_004_roc_5d_pct_rank_126d_5d_diff},
    "mex_extdrv2_005_roc_21d_pct_rank_126d_21d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_005_roc_21d_pct_rank_126d_21d_diff},
    "mex_extdrv2_006_roc_21d_range_position_252d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_006_roc_21d_range_position_252d_5d_diff},
    "mex_extdrv2_007_roc_63d_range_position_252d_21d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_007_roc_63d_range_position_252d_21d_diff},
    "mex_extdrv2_008_roc_42d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_008_roc_42d_5d_diff},
    "mex_extdrv2_009_roc_3d_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv2_009_roc_3d_slope_21d},
    "mex_extdrv2_010_roc_5d_neg_streak_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_010_roc_5d_neg_streak_5d_diff},
    "mex_extdrv2_011_kaufman_er_5d_zscore_63d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_011_kaufman_er_5d_zscore_63d_5d_diff},
    "mex_extdrv2_012_kaufman_er_21d_zscore_126d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_012_kaufman_er_21d_zscore_126d_5d_diff},
    "mex_extdrv2_013_kaufman_er_63d_zscore_252d_21d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_013_kaufman_er_63d_zscore_252d_21d_diff},
    "mex_extdrv2_014_kaufman_er_5d_pct_rank_252d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_014_kaufman_er_5d_pct_rank_252d_5d_diff},
    "mex_extdrv2_015_kaufman_er_42d_pct_rank_252d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_015_kaufman_er_42d_pct_rank_252d_5d_diff},
    "mex_extdrv2_016_td_countdown_count_5d_diff": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv2_016_td_countdown_count_5d_diff},
    "mex_extdrv2_017_td_countdown_zscore_63d_5d_diff": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv2_017_td_countdown_zscore_63d_5d_diff},
    "mex_extdrv2_018_td_countdown_pct_rank_252d_5d_diff": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv2_018_td_countdown_pct_rank_252d_5d_diff},
    "mex_extdrv2_019_td_setup_count_pct_rank_126d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_019_td_setup_count_pct_rank_126d_5d_diff},
    "mex_extdrv2_020_td_perfected_setup_rate_63d_5d_diff": {
        "inputs": ["close", "low"], "func": mex_extdrv2_020_td_perfected_setup_rate_63d_5d_diff},
    "mex_extdrv2_021_triple_roc_decel_confluence_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_021_triple_roc_decel_confluence_5d_diff},
    "mex_extdrv2_022_er_convergence_confluence_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv2_022_er_convergence_confluence_slope_21d},
    "mex_extdrv2_023_exhaustion_composite_21d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv2_023_exhaustion_composite_21d_5d_diff},
    "mex_extdrv2_024_exhaustion_composite_ema_smoothed_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv2_024_exhaustion_composite_ema_smoothed_slope_21d},
    "mex_extdrv2_025_roc_er_divergence_score_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv2_025_roc_er_divergence_score_slope_21d},
}
