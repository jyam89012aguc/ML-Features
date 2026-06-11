"""
27_momentum_exhaustion — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative momentum-exhaustion features —
acceleration of velocity of extended exhaustion signals. Each feature is the
second diff, slope-of-slope, or diff-of-slope of an extended 2nd-derivative concept
(ROC z-score velocity, Kaufman ER z-score velocity, TD countdown velocity,
confluence velocity, and exhaustion composite velocity from the extended base layer).
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


# ── Extended 3rd-Derivative Feature Functions (extdrv3_001-025) ───────────────

# --- Group A (extdrv3_001-005): ROC z-score velocity acceleration ---

def mex_extdrv3_001_roc_5d_zscore_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of 5d ROC within 126d): acceleration of extdrv2_001."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_HALF)
    s = _rolling_std(roc5, _TD_HALF)
    z = _safe_div(roc5 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_002_roc_21d_zscore_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of 21d ROC within 126d): acceleration of extdrv2_002."""
    roc21 = _roc(close, _TD_MON)
    m = _rolling_mean(roc21, _TD_HALF)
    s = _rolling_std(roc21, _TD_HALF)
    z = _safe_div(roc21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_003_roc_63d_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of 63d ROC within 252d): acceleration of extdrv2_003."""
    roc63 = _roc(close, _TD_QTR)
    m = _rolling_mean(roc63, _TD_YEAR)
    s = _rolling_std(roc63, _TD_YEAR)
    z = _safe_div(roc63 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_004_roc_5d_pct_rank_126d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (5d diff of 5d-ROC pct-rank 126d): slope-of-velocity of extdrv2_004."""
    roc5 = _roc(close, _TD_WEEK)
    pct = roc5.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mex_extdrv3_005_roc_21d_pct_rank_126d_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (21d diff of 21d-ROC pct-rank 126d): slope-of-velocity of extdrv2_005."""
    roc21 = _roc(close, _TD_MON)
    pct = roc21.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    vel = pct.diff(_TD_MON)
    return _linslope(vel, _TD_MON)


# --- Group B (extdrv3_006-010): ROC range-position and misc velocity acceleration ---

def mex_extdrv3_006_roc_21d_range_position_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d ROC position in 252d range): acceleration of extdrv2_006."""
    roc21 = _roc(close, _TD_MON)
    rmin = _rolling_min(roc21, _TD_YEAR)
    rmax = _rolling_max(roc21, _TD_YEAR)
    pos = _safe_div(roc21 - rmin, (rmax - rmin).replace(0, np.nan))
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_007_roc_63d_range_position_252d_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (21d diff of 63d-ROC range position): slope of extdrv2_007."""
    roc63 = _roc(close, _TD_QTR)
    rmin = _rolling_min(roc63, _TD_YEAR)
    rmax = _rolling_max(roc63, _TD_YEAR)
    pos = _safe_div(roc63 - rmin, (rmax - rmin).replace(0, np.nan))
    vel = pos.diff(_TD_MON)
    return _linslope(vel, _TD_MON)


def mex_extdrv3_008_roc_42d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 42d ROC: acceleration of extdrv2_008."""
    roc42 = _roc(close, 42)
    vel = roc42.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_009_roc_3d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (OLS slope of 3d ROC over 21d): velocity-of-slope from extdrv2_009."""
    roc3 = _roc(close, 3)
    slp = _linslope(roc3, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_extdrv3_010_roc_5d_neg_streak_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d ROC negative streak count): acceleration of extdrv2_010."""
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
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group C (extdrv3_011-015): Kaufman ER z-score velocity acceleration ---

def mex_extdrv3_011_kaufman_er_5d_zscore_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of Kaufman ER 5d in 63d): acceleration of extdrv2_011."""
    er5 = _kaufman_er(close, _TD_WEEK)
    m = _rolling_mean(er5, _TD_QTR)
    s = _rolling_std(er5, _TD_QTR)
    z = _safe_div(er5 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_012_kaufman_er_21d_zscore_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of Kaufman ER 21d in 126d): acceleration of extdrv2_012."""
    er21 = _kaufman_er(close, _TD_MON)
    m = _rolling_mean(er21, _TD_HALF)
    s = _rolling_std(er21, _TD_HALF)
    z = _safe_div(er21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_013_kaufman_er_63d_zscore_252d_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (21d diff of ER-63d z-score in 252d): slope of extdrv2_013."""
    er63 = _kaufman_er(close, _TD_QTR)
    m = _rolling_mean(er63, _TD_YEAR)
    s = _rolling_std(er63, _TD_YEAR)
    z = _safe_div(er63 - m, s)
    vel = z.diff(_TD_MON)
    return _linslope(vel, _TD_MON)


def mex_extdrv3_014_kaufman_er_5d_pct_rank_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (pct-rank of Kaufman ER 5d in 252d): acceleration of extdrv2_014."""
    er5 = _kaufman_er(close, _TD_WEEK)
    pct = er5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_015_kaufman_er_42d_pct_rank_252d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of (5d diff of ER-42d pct-rank 252d): slope of extdrv2_015."""
    er42 = _kaufman_er(close, 42)
    pct = er42.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# --- Group D (extdrv3_016-020): TD countdown velocity acceleration ---

def mex_extdrv3_016_td_countdown_count_5d_diff_5d_diff(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Second 5-day diff of TD countdown count: acceleration of extdrv2_016."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    vel = cd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_017_td_countdown_zscore_63d_5d_diff_5d_diff(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Second 5-day diff of (z-score of TD countdown in 63d): acceleration of extdrv2_017."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    m = _rolling_mean(cd, _TD_QTR)
    s = _rolling_std(cd, _TD_QTR)
    z = _safe_div(cd - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_018_td_countdown_pct_rank_252d_5d_diff_slope_21d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """OLS slope over 21d of (5d diff of TD countdown pct-rank 252d): slope of extdrv2_018."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    pct = cd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mex_extdrv3_019_td_setup_count_pct_rank_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (pct-rank of TD setup count in 126d): acceleration of extdrv2_019."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    pct = counts.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_020_td_perfected_setup_rate_63d_5d_diff_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of (5d diff of perfected-setup rate 63d): slope of extdrv2_020."""
    flag = _td_perfected_setup_flag(close, low).fillna(0.0)
    rate = _rolling_mean(flag, _TD_QTR)
    vel = rate.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# --- Group E (extdrv3_021-025): Confluence/composite velocity acceleration ---

def mex_extdrv3_021_triple_roc_decel_confluence_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (triple-ROC decel confluence score): acceleration of extdrv2_021."""
    roc5 = _roc(close, _TD_WEEK)
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    imp5 = (roc5 > roc5.shift(1)).astype(float)
    imp21 = (roc21 > roc21.shift(1)).astype(float)
    imp63 = (roc63 > roc63.shift(1)).astype(float)
    confluence = (imp5 + imp21 + imp63) / 3.0
    vel = confluence.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_022_er_convergence_confluence_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (OLS slope over 21d of ER-convergence confluence): diff-of-slope of extdrv2_022."""
    er5 = _kaufman_er(close, _TD_WEEK)
    er21 = _kaufman_er(close, _TD_MON)
    er63 = _kaufman_er(close, _TD_QTR)
    low5 = (er5 < 0.4).astype(float)
    low21 = (er21 < 0.4).astype(float)
    low63 = (er63 < 0.4).astype(float)
    confluence = (low5 + low21 + low63) / 3.0
    slp = _linslope(confluence, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_extdrv3_023_exhaustion_composite_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d exhaustion composite): acceleration of extdrv2_023."""
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
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_extdrv3_024_exhaustion_composite_ema_smoothed_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (OLS slope over 21d of EMA-5 smoothed composite): diff-of-slope of extdrv2_024."""
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
    slp = _linslope(smoothed, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_extdrv3_025_roc_er_divergence_score_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (OLS slope over 21d of ROC/ER divergence score): diff-of-slope of extdrv2_025."""
    roc21 = _roc(close, _TD_MON)
    er21 = _kaufman_er(close, _TD_MON)
    roc_falling = (roc21 < roc21.shift(1)).astype(float)
    er_rising = (er21 > er21.shift(1)).astype(float)
    divergence = roc_falling * er_rising
    slp = _linslope(divergence, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "mex_extdrv3_001_roc_5d_zscore_126d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_001_roc_5d_zscore_126d_5d_diff_5d_diff},
    "mex_extdrv3_002_roc_21d_zscore_126d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_002_roc_21d_zscore_126d_5d_diff_5d_diff},
    "mex_extdrv3_003_roc_63d_zscore_252d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_003_roc_63d_zscore_252d_5d_diff_5d_diff},
    "mex_extdrv3_004_roc_5d_pct_rank_126d_5d_diff_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv3_004_roc_5d_pct_rank_126d_5d_diff_slope_21d},
    "mex_extdrv3_005_roc_21d_pct_rank_126d_21d_diff_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv3_005_roc_21d_pct_rank_126d_21d_diff_slope_21d},
    "mex_extdrv3_006_roc_21d_range_position_252d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_006_roc_21d_range_position_252d_5d_diff_5d_diff},
    "mex_extdrv3_007_roc_63d_range_position_252d_21d_diff_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv3_007_roc_63d_range_position_252d_21d_diff_slope_21d},
    "mex_extdrv3_008_roc_42d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_008_roc_42d_5d_diff_5d_diff},
    "mex_extdrv3_009_roc_3d_slope_21d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_009_roc_3d_slope_21d_5d_diff},
    "mex_extdrv3_010_roc_5d_neg_streak_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_010_roc_5d_neg_streak_5d_diff_5d_diff},
    "mex_extdrv3_011_kaufman_er_5d_zscore_63d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_011_kaufman_er_5d_zscore_63d_5d_diff_5d_diff},
    "mex_extdrv3_012_kaufman_er_21d_zscore_126d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_012_kaufman_er_21d_zscore_126d_5d_diff_5d_diff},
    "mex_extdrv3_013_kaufman_er_63d_zscore_252d_21d_diff_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv3_013_kaufman_er_63d_zscore_252d_21d_diff_slope_21d},
    "mex_extdrv3_014_kaufman_er_5d_pct_rank_252d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_014_kaufman_er_5d_pct_rank_252d_5d_diff_5d_diff},
    "mex_extdrv3_015_kaufman_er_42d_pct_rank_252d_5d_diff_slope_21d": {
        "inputs": ["close"], "func": mex_extdrv3_015_kaufman_er_42d_pct_rank_252d_5d_diff_slope_21d},
    "mex_extdrv3_016_td_countdown_count_5d_diff_5d_diff": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv3_016_td_countdown_count_5d_diff_5d_diff},
    "mex_extdrv3_017_td_countdown_zscore_63d_5d_diff_5d_diff": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv3_017_td_countdown_zscore_63d_5d_diff_5d_diff},
    "mex_extdrv3_018_td_countdown_pct_rank_252d_5d_diff_slope_21d": {
        "inputs": ["close", "low", "high"], "func": mex_extdrv3_018_td_countdown_pct_rank_252d_5d_diff_slope_21d},
    "mex_extdrv3_019_td_setup_count_pct_rank_126d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_019_td_setup_count_pct_rank_126d_5d_diff_5d_diff},
    "mex_extdrv3_020_td_perfected_setup_rate_63d_5d_diff_slope_21d": {
        "inputs": ["close", "low"], "func": mex_extdrv3_020_td_perfected_setup_rate_63d_5d_diff_slope_21d},
    "mex_extdrv3_021_triple_roc_decel_confluence_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_021_triple_roc_decel_confluence_5d_diff_5d_diff},
    "mex_extdrv3_022_er_convergence_confluence_slope_21d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_022_er_convergence_confluence_slope_21d_5d_diff},
    "mex_extdrv3_023_exhaustion_composite_21d_5d_diff_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_023_exhaustion_composite_21d_5d_diff_5d_diff},
    "mex_extdrv3_024_exhaustion_composite_ema_smoothed_slope_21d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_024_exhaustion_composite_ema_smoothed_slope_21d_5d_diff},
    "mex_extdrv3_025_roc_er_divergence_score_slope_21d_5d_diff": {
        "inputs": ["close"], "func": mex_extdrv3_025_roc_er_divergence_score_slope_21d_5d_diff},
}
