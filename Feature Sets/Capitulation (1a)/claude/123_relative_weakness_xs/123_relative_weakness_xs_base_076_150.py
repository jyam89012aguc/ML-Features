"""
123_relative_weakness_xs — Base Features 076-150
Domain: ticker price weakness relative to sector/industry/universe peer medians
        (cross-sectional comparison) — high/low relative weakness, volume-relative
        weakness, beta-adjusted residual weakness, rolling relative high/low metrics,
        peer-relative volatility, relative momentum, multi-window composite scores
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily price/volume Series AND a
    precomputed sector/industry peer-median Series of the same daily index.
    Peer-median series are named  peer_median_<field>  where <field> matches
    the own-ticker field name.  The pipeline computes sector/industry medians
    cross-sectionally and passes them in.

    Own price/volume inputs:        close, high, low, open, volume
    Peer-median series available:   peer_median_close, peer_median_high,
                                    peer_median_low, peer_median_volume
    (peer_median_open is not used — open is too noisy cross-sectionally.)

    All functions look strictly backward.  No forward leakage.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _log_return(close: pd.Series, n: int = 1) -> pd.Series:
    """n-day log return of a price series."""
    return np.log(close / close.shift(n).replace(0, np.nan))


def _drawdown_from_peak(close: pd.Series, w: int) -> pd.Series:
    """Rolling drawdown from w-day peak: (close - peak) / peak."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): High/Low relative weakness ---

def rwx_076_rel_high_return_21d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """21d return of ticker high minus 21d return of peer-median high."""
    r_own  = _log_return(high, _TD_MON)
    r_peer = _log_return(peer_median_high, _TD_MON)
    return r_own - r_peer


def rwx_077_rel_high_return_63d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """63d return of ticker high minus 63d return of peer-median high."""
    r_own  = _log_return(high, _TD_QTR)
    r_peer = _log_return(peer_median_high, _TD_QTR)
    return r_own - r_peer


def rwx_078_rel_low_return_21d(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """21d return of ticker low minus 21d return of peer-median low (low weakness)."""
    r_own  = _log_return(low, _TD_MON)
    r_peer = _log_return(peer_median_low, _TD_MON)
    return r_own - r_peer


def rwx_079_rel_low_return_63d(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """63d return of ticker low minus 63d return of peer-median low."""
    r_own  = _log_return(low, _TD_QTR)
    r_peer = _log_return(peer_median_low, _TD_QTR)
    return r_own - r_peer


def rwx_080_rel_low_to_peer_high_ratio(low: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """Log of (ticker low / peer high) — how far below the peer's high the ticker's low is."""
    ratio = _safe_div(low, peer_median_high)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_081_rel_close_to_peer_high_ratio(close: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """Log of (ticker close / peer high) — how much ticker close lags peer's peak."""
    ratio = _safe_div(close, peer_median_high)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_082_rel_high_drawdown_252d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """Ticker 252d high drawdown minus peer-median 252d high drawdown."""
    dd_own  = _drawdown_from_peak(high, _TD_YEAR)
    dd_peer = _drawdown_from_peak(peer_median_high, _TD_YEAR)
    return dd_own - dd_peer


def rwx_083_rel_low_new_low_21d_flag(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """Binary: ticker low hits new 21d relative-low-ratio low today."""
    ratio    = _safe_div(low, peer_median_low)
    prev_min = ratio.shift(1).rolling(_TD_MON, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def rwx_084_rel_low_new_low_63d_flag(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """Binary: ticker low hits new 63d relative-low-ratio low today."""
    ratio    = _safe_div(low, peer_median_low)
    prev_min = ratio.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def rwx_085_rel_high_new_low_252d_flag(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """Binary: ticker daily high hits a new 252d relative-high-ratio low (peaks eroding vs peers)."""
    ratio    = _safe_div(high, peer_median_high)
    prev_min = ratio.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (ratio < prev_min).astype(float)


# --- Group I (086-095): Volume-relative weakness ---

def rwx_086_rel_volume_ratio_21d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Ticker 21d avg volume divided by peer-median 21d avg volume (volume size relative)."""
    v_own  = _rolling_mean(volume, _TD_MON)
    v_peer = _rolling_mean(peer_median_volume, _TD_MON)
    return _safe_div(v_own, v_peer)


def rwx_087_log_volume_ratio_to_peer(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Log of (ticker volume / peer-median volume) — relative volume on log scale."""
    ratio = _safe_div(volume, peer_median_volume)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_088_volume_weighted_underperf_21d(close: pd.Series, peer_median_close: pd.Series,
                                           volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """21d sum of (relative return * ticker volume) normalized by avg volume — volume-weighted underperf."""
    rel  = _log_return(close, 1) - _log_return(peer_median_close, 1)
    vw   = rel * volume
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(_rolling_sum(vw, _TD_MON), avg_vol.clip(lower=_EPS))


def rwx_089_rel_volume_low_return_21d(close: pd.Series, peer_median_close: pd.Series,
                                       volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """21d relative return when ticker volume < peer-median volume (quiet underperformance)."""
    rel  = _log_return(close, 1) - _log_return(peer_median_close, 1)
    low_vol_flag = (volume < peer_median_volume).astype(float)
    return _rolling_mean(rel * low_vol_flag, _TD_MON)


def rwx_090_rel_volume_high_return_21d(close: pd.Series, peer_median_close: pd.Series,
                                        volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """21d relative return when ticker volume > peer-median volume (high-volume underperformance)."""
    rel  = _log_return(close, 1) - _log_return(peer_median_close, 1)
    high_vol_flag = (volume > peer_median_volume).astype(float)
    return _rolling_mean(rel * high_vol_flag, _TD_MON)


def rwx_091_rel_volume_ratio_63d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Ticker 63d avg volume divided by peer-median 63d avg volume."""
    v_own  = _rolling_mean(volume, _TD_QTR)
    v_peer = _rolling_mean(peer_median_volume, _TD_QTR)
    return _safe_div(v_own, v_peer)


def rwx_092_volume_ratio_zscore_63d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Z-score of daily volume ratio (ticker/peer) over trailing 63d."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return _zscore_rolling(ratio, _TD_QTR)


def rwx_093_rel_volume_ratio_expanding_pctrank(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of daily volume ratio (ticker/peer)."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return ratio.expanding(min_periods=21).rank(pct=True)


def rwx_094_volume_underperf_flag_21d(close: pd.Series, peer_median_close: pd.Series,
                                       volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Fraction of 21d where ticker underperforms AND volume > peer (distribution days)."""
    rel      = _log_return(close, 1) - _log_return(peer_median_close, 1)
    dist_day = ((rel < 0) & (volume > peer_median_volume)).astype(float)
    return _rolling_mean(dist_day, _TD_MON)


def rwx_095_volume_underperf_flag_63d(close: pd.Series, peer_median_close: pd.Series,
                                       volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Fraction of 63d where ticker underperforms AND volume > peer (distribution days)."""
    rel      = _log_return(close, 1) - _log_return(peer_median_close, 1)
    dist_day = ((rel < 0) & (volume > peer_median_volume)).astype(float)
    return _rolling_mean(dist_day, _TD_QTR)


# --- Group J (096-105): Beta-adjusted residual weakness ---

def rwx_096_ols_beta_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling OLS beta of ticker returns on peer-median returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    cov    = (r_own * r_peer).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() - \
             r_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * \
             r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    var_p  = r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    return _safe_div(cov, var_p)


def rwx_097_ols_beta_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling OLS beta of ticker returns on peer-median returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    cov    = (r_own * r_peer).rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean() - \
             r_own.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean() * \
             r_peer.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean()
    var_p  = r_peer.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).var()
    return _safe_div(cov, var_p)


def rwx_098_residual_return_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling alpha (intercept) of OLS regressing ticker returns on peer returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    cov    = (r_own * r_peer).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() - \
             r_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * \
             r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    var_p  = r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    beta   = _safe_div(cov, var_p)
    alpha  = r_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() - \
             beta * r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return alpha


def rwx_099_residual_return_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling alpha of OLS regressing ticker returns on peer returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    cov    = (r_own * r_peer).rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean() - \
             r_own.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean() * \
             r_peer.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean()
    var_p  = r_peer.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).var()
    beta   = _safe_div(cov, var_p)
    alpha  = r_own.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean() - \
             beta * r_peer.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean()
    return alpha


def rwx_100_beta_adj_rel_return_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d: beta-adjusted relative return = ticker_return - beta_63d * peer_return."""
    r_own  = _log_return(close, _TD_MON)
    r_peer = _log_return(peer_median_close, _TD_MON)
    r1_own  = _log_return(close, 1)
    r1_peer = _log_return(peer_median_close, 1)
    cov    = (r1_own * r1_peer).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() - \
             r1_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * \
             r1_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    var_p  = r1_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    beta   = _safe_div(cov, var_p)
    return r_own - beta * r_peer


def rwx_101_beta_gt1_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if 63d beta > 1 (amplifies peer moves — higher systematic weakness risk)."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    cov    = (r_own * r_peer).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() - \
             r_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * \
             r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    var_p  = r_peer.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    beta   = _safe_div(cov, var_p)
    return (beta > 1.0).astype(float)


def rwx_102_correlation_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling Pearson correlation between ticker and peer-median daily returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    return r_own.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).corr(r_peer)


def rwx_103_correlation_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling Pearson correlation between ticker and peer-median daily returns."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    return r_own.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).corr(r_peer)


def rwx_104_tracking_error_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling std of daily relative return (tracking error vs peer median)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_std(rel, _TD_QTR)


def rwx_105_tracking_error_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling std of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_std(rel, _TD_YEAR)


# --- Group K (106-115): Trend-slope of relative metrics ---

def rwx_106_rel_return_1d_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of daily relative return (trend in relative underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _linslope(rel, _TD_MON)


def rwx_107_rel_return_1d_slope_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 63d of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _linslope(rel, _TD_QTR)


def rwx_108_log_price_ratio_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of log(ticker/peer) (trend in relative price level)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _linslope(lr, _TD_MON)


def rwx_109_log_price_ratio_slope_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 63d of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _linslope(lr, _TD_QTR)


def rwx_110_log_price_ratio_slope_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 252d of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _linslope(lr, _TD_YEAR)


def rwx_111_rel_return_ewm21_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of EWM(21)-smoothed daily relative return."""
    rel  = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm  = _ewm_mean(rel, _TD_MON)
    return _linslope(ewm, _TD_MON)


def rwx_112_consec_underperf_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of consecutive-underperformance streak (trend in streak length)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag).astype(float)
    return _linslope(streak, _TD_MON)


def rwx_113_frac_underperf_21d_slope_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 63d of the 21d underperformance fraction (worsening trend)."""
    flag    = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21  = _rolling_mean(flag, _TD_MON)
    return _linslope(frac21, _TD_QTR)


def rwx_114_rel_drawdown_63d_slope_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 63d of 63d relative drawdown (trend in relative drawdown deepening)."""
    rel_dd = _drawdown_from_peak(close, _TD_QTR) - _drawdown_from_peak(peer_median_close, _TD_QTR)
    return _linslope(rel_dd, _TD_QTR)


def rwx_115_rel_return_1d_ewm5_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of EWM(5)-smoothed relative return (fast-trend slope)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm = _ewm_mean(rel, _TD_WEEK)
    return _linslope(ewm, _TD_MON)


# --- Group L (116-125): Multi-window composite underperformance scores ---

def rwx_116_composite_rel_return_score(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 5d/21d/63d relative returns (composite short-to-medium weakness score)."""
    r5  = _log_return(close, _TD_WEEK)  - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)   - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)   - _log_return(peer_median_close, _TD_QTR)
    return (r5 + r21 + r63) / 3.0


def rwx_117_composite_rel_return_score_wide(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 21d/63d/126d/252d relative returns (medium-to-long weakness composite)."""
    r21  = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63  = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    r126 = _log_return(close, _TD_HALF) - _log_return(peer_median_close, _TD_HALF)
    r252 = _log_return(close, _TD_YEAR) - _log_return(peer_median_close, _TD_YEAR)
    return (r21 + r63 + r126 + r252) / 4.0


def rwx_118_composite_underperf_flag_score(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of timeframes (5d/21d/63d/126d) where ticker underperforms peer (0-4 distress count)."""
    f5   = (_log_return(close, _TD_WEEK) < _log_return(peer_median_close, _TD_WEEK)).astype(float)
    f21  = (_log_return(close, _TD_MON)  < _log_return(peer_median_close, _TD_MON)).astype(float)
    f63  = (_log_return(close, _TD_QTR)  < _log_return(peer_median_close, _TD_QTR)).astype(float)
    f126 = (_log_return(close, _TD_HALF) < _log_return(peer_median_close, _TD_HALF)).astype(float)
    return f5 + f21 + f63 + f126


def rwx_119_all_windows_underperf_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if ticker underperforms peers on ALL of 5d/21d/63d/252d."""
    f5   = (_log_return(close, _TD_WEEK) < _log_return(peer_median_close, _TD_WEEK))
    f21  = (_log_return(close, _TD_MON)  < _log_return(peer_median_close, _TD_MON))
    f63  = (_log_return(close, _TD_QTR)  < _log_return(peer_median_close, _TD_QTR))
    f252 = (_log_return(close, _TD_YEAR) < _log_return(peer_median_close, _TD_YEAR))
    return (f5 & f21 & f63 & f252).astype(float)


def rwx_120_composite_zscore_3window(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 252d z-scores for 5d/21d/63d relative returns (composite extremity)."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    z5  = _zscore_rolling(r5,  _TD_YEAR)
    z21 = _zscore_rolling(r21, _TD_YEAR)
    z63 = _zscore_rolling(r63, _TD_YEAR)
    return (z5 + z21 + z63) / 3.0


def rwx_121_composite_pctrank_3window(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 252d pctrank for 5d/21d/63d relative returns (composite rank)."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    p5  = r5.rolling(_TD_YEAR,  min_periods=_TD_QTR).rank(pct=True)
    p21 = r21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    p63 = r63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (p5 + p21 + p63) / 3.0


def rwx_122_rel_vol_adj_return_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d relative return divided by 63d tracking error (risk-adjusted relative weakness)."""
    rel   = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    te63  = _rolling_std(_log_return(close, 1) - _log_return(peer_median_close, 1), _TD_QTR)
    return _safe_div(rel, te63.clip(lower=_EPS))


def rwx_123_rel_vol_adj_return_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d relative return divided by 252d tracking error (risk-adjusted)."""
    rel   = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    te252 = _rolling_std(_log_return(close, 1) - _log_return(peer_median_close, 1), _TD_YEAR)
    return _safe_div(rel, te252.clip(lower=_EPS))


def rwx_124_peer_relative_volatility_ratio(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ratio of ticker 63d return-std to peer-median 63d return-std (relative volatility)."""
    own_vol  = _rolling_std(_log_return(close, 1), _TD_QTR)
    peer_vol = _rolling_std(_log_return(peer_median_close, 1), _TD_QTR)
    return _safe_div(own_vol, peer_vol)


def rwx_125_peer_relative_volatility_ratio_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ratio of ticker 252d return-std to peer-median 252d return-std."""
    own_vol  = _rolling_std(_log_return(close, 1), _TD_YEAR)
    peer_vol = _rolling_std(_log_return(peer_median_close, 1), _TD_YEAR)
    return _safe_div(own_vol, peer_vol)


# --- Group M (126-135): Rolling relative price level metrics ---

def rwx_126_rel_close_rolling_min_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d rolling min of log(ticker/peer) — relative price at its monthly worst."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_min(lr, _TD_MON)


def rwx_127_rel_close_rolling_min_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling min of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_min(lr, _TD_QTR)


def rwx_128_rel_close_rolling_mean_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling mean of log(ticker/peer) — sustained relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_mean(lr, _TD_QTR)


def rwx_129_rel_close_rolling_mean_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling mean of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_mean(lr, _TD_YEAR)


def rwx_130_rel_close_vs_rolling_mean_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Current log(ticker/peer) minus its 63d rolling mean (deviation from recent average)."""
    lr  = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr - _rolling_mean(lr, _TD_QTR)


def rwx_131_rel_close_vs_rolling_mean_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Current log(ticker/peer) minus its 252d rolling mean."""
    lr  = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr - _rolling_mean(lr, _TD_YEAR)


def rwx_132_rel_close_drawdown_from_252d_peak(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Drawdown of log(ticker/peer) from its 252d peak (how far relative strength has fallen)."""
    lr   = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    peak = _rolling_max(lr, _TD_YEAR)
    return _safe_div(lr - peak, peak.abs().clip(lower=_EPS))


def rwx_133_rel_close_drawdown_from_expanding_peak(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Drawdown of log(ticker/peer) from its all-time expanding peak."""
    lr   = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    peak = lr.expanding(min_periods=1).max()
    return _safe_div(lr - peak, peak.abs().clip(lower=_EPS))


def rwx_134_rel_close_distance_from_252d_floor(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Current log(ticker/peer) minus its 252d rolling minimum (distance above the floor)."""
    lr    = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    floor = _rolling_min(lr, _TD_YEAR)
    return lr - floor


def rwx_135_rel_close_ewm63(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(63) of log(ticker/peer) — quarterly smoothed relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _ewm_mean(lr, _TD_QTR)


# --- Group N (136-145): Time-since-extreme and regime metrics ---

def rwx_136_time_since_rel_price_new_low_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Days elapsed since log(ticker/peer) last hit a 252d relative low."""
    lr       = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    prev_min = lr.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    new_low  = (lr < prev_min).astype(float)
    idx      = pd.Series(range(len(lr)), index=lr.index, dtype=float)
    last_idx = idx.where(new_low == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~lr.isna(), np.nan)


def rwx_137_time_since_rel_price_new_low_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Days elapsed since log(ticker/peer) last hit a 63d relative low."""
    lr       = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    prev_min = lr.shift(1).rolling(_TD_QTR, min_periods=1).min()
    new_low  = (lr < prev_min).astype(float)
    idx      = pd.Series(range(len(lr)), index=lr.index, dtype=float)
    last_idx = idx.where(new_low == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~lr.isna(), np.nan)


def rwx_138_rel_underperf_regime_flag_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if 63d underperformance fraction > 60% (persistent relative weakness regime)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac63 = _rolling_mean(flag, _TD_QTR)
    return (frac63 > 0.60).astype(float)


def rwx_139_rel_underperf_regime_flag_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if 252d underperformance fraction > 60%."""
    flag    = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac252 = _rolling_mean(flag, _TD_YEAR)
    return (frac252 > 0.60).astype(float)


def rwx_140_rel_price_at_252d_min_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if log(ticker/peer) is at or below its 252d rolling minimum today."""
    lr   = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    mn   = _rolling_min(lr, _TD_YEAR)
    return (lr <= mn).astype(float)


def rwx_141_rel_price_pctrank_252d_low_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if 252d pctrank of log(ticker/peer) is in bottom decile (<=0.10)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    pr = lr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (pr <= 0.10).astype(float)


def rwx_142_frac_underperf_21d_vs_frac_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ratio of 21d underperformance fraction to 252d fraction (recent vs long-run)."""
    flag    = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21  = _rolling_mean(flag, _TD_MON)
    frac252 = _rolling_mean(flag, _TD_YEAR)
    return _safe_div(frac21, frac252.clip(lower=_EPS))


def rwx_143_rel_return_63d_vs_126d_momentum(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d relative return minus 126d relative return (recent acceleration of weakness)."""
    r63  = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    r126 = _log_return(close, _TD_HALF) - _log_return(peer_median_close, _TD_HALF)
    return r63 - r126


def rwx_144_rel_return_21d_vs_63d_momentum(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d relative return minus 63d relative return (short-run acceleration)."""
    r21 = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return r21 - r63


def rwx_145_rel_return_1d_vs_21d_momentum(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """1d relative return minus 21d relative return (very-short-run vs monthly)."""
    r1  = _log_return(close, 1)       - _log_return(peer_median_close, 1)
    r21 = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return r1 - r21


# --- Group O (146-150): EWM smoothed relative metrics ---

def rwx_146_rel_return_ewm5(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(5) of daily relative return (ultra-short smoothed relative momentum)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_WEEK)


def rwx_147_rel_return_ewm126(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(126) of daily relative return (half-year smoothed relative trend)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_HALF)


def rwx_148_log_price_ratio_ewm21(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(21) of log(ticker/peer) — monthly smoothed relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _ewm_mean(lr, _TD_MON)


def rwx_149_log_price_ratio_ewm126(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(126) of log(ticker/peer) — half-year smoothed relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _ewm_mean(lr, _TD_HALF)


def rwx_150_rel_return_1d_rolling_median_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling median of daily relative return (robust long-run central tendency)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_median(rel, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_WEAKNESS_XS_REGISTRY_076_150 = {
    "rwx_076_rel_high_return_21d":                  {"inputs": ["high", "peer_median_high"],                                                           "func": rwx_076_rel_high_return_21d},
    "rwx_077_rel_high_return_63d":                  {"inputs": ["high", "peer_median_high"],                                                           "func": rwx_077_rel_high_return_63d},
    "rwx_078_rel_low_return_21d":                   {"inputs": ["low", "peer_median_low"],                                                             "func": rwx_078_rel_low_return_21d},
    "rwx_079_rel_low_return_63d":                   {"inputs": ["low", "peer_median_low"],                                                             "func": rwx_079_rel_low_return_63d},
    "rwx_080_rel_low_to_peer_high_ratio":           {"inputs": ["low", "peer_median_high"],                                                            "func": rwx_080_rel_low_to_peer_high_ratio},
    "rwx_081_rel_close_to_peer_high_ratio":         {"inputs": ["close", "peer_median_high"],                                                          "func": rwx_081_rel_close_to_peer_high_ratio},
    "rwx_082_rel_high_drawdown_252d":               {"inputs": ["high", "peer_median_high"],                                                           "func": rwx_082_rel_high_drawdown_252d},
    "rwx_083_rel_low_new_low_21d_flag":             {"inputs": ["low", "peer_median_low"],                                                             "func": rwx_083_rel_low_new_low_21d_flag},
    "rwx_084_rel_low_new_low_63d_flag":             {"inputs": ["low", "peer_median_low"],                                                             "func": rwx_084_rel_low_new_low_63d_flag},
    "rwx_085_rel_high_new_low_252d_flag":           {"inputs": ["high", "peer_median_high"],                                                           "func": rwx_085_rel_high_new_low_252d_flag},
    "rwx_086_rel_volume_ratio_21d":                 {"inputs": ["volume", "peer_median_volume"],                                                       "func": rwx_086_rel_volume_ratio_21d},
    "rwx_087_log_volume_ratio_to_peer":             {"inputs": ["volume", "peer_median_volume"],                                                       "func": rwx_087_log_volume_ratio_to_peer},
    "rwx_088_volume_weighted_underperf_21d":        {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                         "func": rwx_088_volume_weighted_underperf_21d},
    "rwx_089_rel_volume_low_return_21d":            {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                         "func": rwx_089_rel_volume_low_return_21d},
    "rwx_090_rel_volume_high_return_21d":           {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                         "func": rwx_090_rel_volume_high_return_21d},
    "rwx_091_rel_volume_ratio_63d":                 {"inputs": ["volume", "peer_median_volume"],                                                       "func": rwx_091_rel_volume_ratio_63d},
    "rwx_092_volume_ratio_zscore_63d":              {"inputs": ["volume", "peer_median_volume"],                                                       "func": rwx_092_volume_ratio_zscore_63d},
    "rwx_093_rel_volume_ratio_expanding_pctrank":   {"inputs": ["volume", "peer_median_volume"],                                                       "func": rwx_093_rel_volume_ratio_expanding_pctrank},
    "rwx_094_volume_underperf_flag_21d":            {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                         "func": rwx_094_volume_underperf_flag_21d},
    "rwx_095_volume_underperf_flag_63d":            {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                         "func": rwx_095_volume_underperf_flag_63d},
    "rwx_096_ols_beta_63d":                         {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_096_ols_beta_63d},
    "rwx_097_ols_beta_252d":                        {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_097_ols_beta_252d},
    "rwx_098_residual_return_63d":                  {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_098_residual_return_63d},
    "rwx_099_residual_return_252d":                 {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_099_residual_return_252d},
    "rwx_100_beta_adj_rel_return_21d":              {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_100_beta_adj_rel_return_21d},
    "rwx_101_beta_gt1_flag":                        {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_101_beta_gt1_flag},
    "rwx_102_correlation_63d":                      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_102_correlation_63d},
    "rwx_103_correlation_252d":                     {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_103_correlation_252d},
    "rwx_104_tracking_error_63d":                   {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_104_tracking_error_63d},
    "rwx_105_tracking_error_252d":                  {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_105_tracking_error_252d},
    "rwx_106_rel_return_1d_slope_21d":              {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_106_rel_return_1d_slope_21d},
    "rwx_107_rel_return_1d_slope_63d":              {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_107_rel_return_1d_slope_63d},
    "rwx_108_log_price_ratio_slope_21d":            {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_108_log_price_ratio_slope_21d},
    "rwx_109_log_price_ratio_slope_63d":            {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_109_log_price_ratio_slope_63d},
    "rwx_110_log_price_ratio_slope_252d":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_110_log_price_ratio_slope_252d},
    "rwx_111_rel_return_ewm21_slope_21d":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_111_rel_return_ewm21_slope_21d},
    "rwx_112_consec_underperf_slope_21d":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_112_consec_underperf_slope_21d},
    "rwx_113_frac_underperf_21d_slope_63d":         {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_113_frac_underperf_21d_slope_63d},
    "rwx_114_rel_drawdown_63d_slope_63d":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_114_rel_drawdown_63d_slope_63d},
    "rwx_115_rel_return_1d_ewm5_slope_21d":         {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_115_rel_return_1d_ewm5_slope_21d},
    "rwx_116_composite_rel_return_score":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_116_composite_rel_return_score},
    "rwx_117_composite_rel_return_score_wide":      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_117_composite_rel_return_score_wide},
    "rwx_118_composite_underperf_flag_score":       {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_118_composite_underperf_flag_score},
    "rwx_119_all_windows_underperf_flag":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_119_all_windows_underperf_flag},
    "rwx_120_composite_zscore_3window":             {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_120_composite_zscore_3window},
    "rwx_121_composite_pctrank_3window":            {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_121_composite_pctrank_3window},
    "rwx_122_rel_vol_adj_return_21d":               {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_122_rel_vol_adj_return_21d},
    "rwx_123_rel_vol_adj_return_63d":               {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_123_rel_vol_adj_return_63d},
    "rwx_124_peer_relative_volatility_ratio":       {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_124_peer_relative_volatility_ratio},
    "rwx_125_peer_relative_volatility_ratio_252d":  {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_125_peer_relative_volatility_ratio_252d},
    "rwx_126_rel_close_rolling_min_21d":            {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_126_rel_close_rolling_min_21d},
    "rwx_127_rel_close_rolling_min_63d":            {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_127_rel_close_rolling_min_63d},
    "rwx_128_rel_close_rolling_mean_63d":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_128_rel_close_rolling_mean_63d},
    "rwx_129_rel_close_rolling_mean_252d":          {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_129_rel_close_rolling_mean_252d},
    "rwx_130_rel_close_vs_rolling_mean_63d":        {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_130_rel_close_vs_rolling_mean_63d},
    "rwx_131_rel_close_vs_rolling_mean_252d":       {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_131_rel_close_vs_rolling_mean_252d},
    "rwx_132_rel_close_drawdown_from_252d_peak":    {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_132_rel_close_drawdown_from_252d_peak},
    "rwx_133_rel_close_drawdown_from_expanding_peak": {"inputs": ["close", "peer_median_close"],                                                       "func": rwx_133_rel_close_drawdown_from_expanding_peak},
    "rwx_134_rel_close_distance_from_252d_floor":   {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_134_rel_close_distance_from_252d_floor},
    "rwx_135_rel_close_ewm63":                      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_135_rel_close_ewm63},
    "rwx_136_time_since_rel_price_new_low_252d":    {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_136_time_since_rel_price_new_low_252d},
    "rwx_137_time_since_rel_price_new_low_63d":     {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_137_time_since_rel_price_new_low_63d},
    "rwx_138_rel_underperf_regime_flag_63d":        {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_138_rel_underperf_regime_flag_63d},
    "rwx_139_rel_underperf_regime_flag_252d":       {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_139_rel_underperf_regime_flag_252d},
    "rwx_140_rel_price_at_252d_min_flag":           {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_140_rel_price_at_252d_min_flag},
    "rwx_141_rel_price_pctrank_252d_low_flag":      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_141_rel_price_pctrank_252d_low_flag},
    "rwx_142_frac_underperf_21d_vs_frac_252d":      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_142_frac_underperf_21d_vs_frac_252d},
    "rwx_143_rel_return_63d_vs_126d_momentum":      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_143_rel_return_63d_vs_126d_momentum},
    "rwx_144_rel_return_21d_vs_63d_momentum":       {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_144_rel_return_21d_vs_63d_momentum},
    "rwx_145_rel_return_1d_vs_21d_momentum":        {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_145_rel_return_1d_vs_21d_momentum},
    "rwx_146_rel_return_ewm5":                      {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_146_rel_return_ewm5},
    "rwx_147_rel_return_ewm126":                    {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_147_rel_return_ewm126},
    "rwx_148_log_price_ratio_ewm21":                {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_148_log_price_ratio_ewm21},
    "rwx_149_log_price_ratio_ewm126":               {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_149_log_price_ratio_ewm126},
    "rwx_150_rel_return_1d_rolling_median_252d":    {"inputs": ["close", "peer_median_close"],                                                         "func": rwx_150_rel_return_1d_rolling_median_252d},
}
