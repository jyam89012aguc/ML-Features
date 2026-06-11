"""jump_detection_signature base features 451-525 — Pipeline 1b-technical batch 4.

75 NEW fine-grained signals for ML precision. Focus: conditional jump signatures at
multi-event states (jump + regime + volume), lower-high / lower-low sequence counts
after price extremes, classical candle patterns (doji-at-high, dark-cloud, evening-
star, engulfing, tweezer), close-position dynamics (persistent upper/lower close
streaks), volume-profile concentration around moves, risk-bar combinations
(Hindenburg-style new-high-and-new-low, gap-fill failure, stop-run), cumulative
move-concentration, escalating tail-event sequences (2σ → 3σ → 4σ), Bayesian
conditional probabilities (P[jump | regime]).

Inputs: SEP OHLCV only. PIT-clean. Self-contained.
"""
import math
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _log_ret(close):
    return _safe_log(close).diff()


def _sigma_prior(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)


# ============================================================
# Bucket A — Multi-event conditional jumps (451-460)
# ============================================================

def f38_jpdt_451_jump_count_after_recent_jump_252d(close: pd.Series) -> pd.Series:
    """Jump count on days where prior 5 days had ≥1 jump (clustering filter) over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    recent = j.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5
    return (j.astype(bool) & recent).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_452_jump_count_after_quiet_5d_252d(close: pd.Series) -> pd.Series:
    """Jump count on days where prior 5 days had NO jump (surprise filter) over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    quiet = j.shift(1).rolling(WDAYS, min_periods=1).max() < 0.5
    return (j.astype(bool) & quiet).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_453_jump_count_sigma_rising_volume_rising_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jump count where σ_21 rising AND volume rising over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    sig_up = sig > sig.shift(WDAYS)
    vol_up = volume.rolling(WDAYS, min_periods=2).mean() > volume.rolling(WDAYS, min_periods=2).mean().shift(WDAYS)
    return (j & sig_up & vol_up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_454_jump_count_sigma_falling_252d(close: pd.Series) -> pd.Series:
    """Jump count where σ_21 is falling over 252d (surprise jumps in a calming regime)."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    sig_dn = sig < sig.shift(WDAYS)
    return (j & sig_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_455_jump_count_after_21d_high_close_252d(close: pd.Series) -> pd.Series:
    """Jump count on days where prior bar's close was a 21d-high, over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    high_close_lag = (close.shift(1) >= close.shift(1).rolling(MDAYS, min_periods=WDAYS).max())
    return (j & high_close_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_456_jump_count_after_21d_low_close_252d(close: pd.Series) -> pd.Series:
    """Jump count on days where prior bar's close was a 21d-low, over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    low_close_lag = (close.shift(1) <= close.shift(1).rolling(MDAYS, min_periods=WDAYS).min())
    return (j & low_close_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_457_mean_abs_r_after_jump_3d_252d(close: pd.Series) -> pd.Series:
    """Mean |r| on days following any jump in past 3 days over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    recent_jump = j.shift(1).rolling(3, min_periods=1).max() > 0.5
    return r.abs().where(recent_jump, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_458_dn_jump_in_strong_uptrend_252d(close: pd.Series) -> pd.Series:
    """Down-jump count where 21d log-return > 10% (climax-detection) over 252d."""
    r = _log_ret(close)
    dn = (r < -3 * _sigma_prior(r, MDAYS))
    strong_up = (_safe_log(close) - _safe_log(close.shift(MDAYS))) > 0.10
    return (dn & strong_up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_459_up_jump_in_strong_downtrend_252d(close: pd.Series) -> pd.Series:
    """Up-jump count where 21d log-return < −10% (capitulation-bounce-detection) over 252d."""
    r = _log_ret(close)
    up = (r > 3 * _sigma_prior(r, MDAYS))
    strong_dn = (_safe_log(close) - _safe_log(close.shift(MDAYS))) < -0.10
    return (up & strong_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_460_mean_post_jump_21d_return_252d(close: pd.Series) -> pd.Series:
    """Mean 21d trailing log-return on days after a jump (regression-to-mean test) over 252d."""
    r = _log_ret(close)
    j_lag = (r.shift(MDAYS).abs() > 3 * _sigma_prior(r, MDAYS).shift(MDAYS))
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return trail.where(j_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket B — Sequence patterns after extremes (461-470)
# ============================================================

def f38_jpdt_461_lower_high_count_after_21d_high_252d(high: pd.Series) -> pd.Series:
    """Count of lower highs (high < prior bar's high) AFTER a 21d-high event, over 252d."""
    new_high_lag = (high.shift(1) >= high.shift(1).rolling(MDAYS, min_periods=WDAYS).max())
    lower_high = (high < high.shift(1))
    return (lower_high & new_high_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_462_lower_low_count_after_21d_low_252d(low: pd.Series) -> pd.Series:
    """Count of lower lows AFTER a 21d-low event over 252d."""
    new_low_lag = (low.shift(1) <= low.shift(1).rolling(MDAYS, min_periods=WDAYS).min())
    lower_low = (low < low.shift(1))
    return (lower_low & new_low_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_463_failed_bounce_count_252d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Failed bounce: low pierces 5d-low but close < open over 252d."""
    pierce = low < low.shift(1).rolling(WDAYS, min_periods=2).min()
    bearish = close < open
    return (pierce & bearish).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_464_failed_rally_count_252d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Failed rally: high pierces 5d-high but close < open over 252d."""
    pierce = high > high.shift(1).rolling(WDAYS, min_periods=2).max()
    bearish = close < open
    return (pierce & bearish).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_465_distribution_sequence_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3 consecutive down-days on high volume (vol_z>1) over 252d (distribution sequence)."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    distrib = (r < 0) & (vz > 1)
    three_seq = distrib & distrib.shift(1).fillna(False) & distrib.shift(2).fillna(False)
    return three_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_466_accumulation_sequence_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3 consecutive up-days on high volume over 252d (accumulation sequence)."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    accum = (r > 0) & (vz > 1)
    three_seq = accum & accum.shift(1).fillna(False) & accum.shift(2).fillna(False)
    return three_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_467_higher_highs_streak_count_63d(high: pd.Series) -> pd.Series:
    """Longest streak of consecutive higher-highs over 63d."""
    hh = (high > high.shift(1)).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return hh.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True)


def f38_jpdt_468_lower_lows_streak_count_63d(low: pd.Series) -> pd.Series:
    """Longest streak of consecutive lower-lows over 63d."""
    ll = (low < low.shift(1)).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return ll.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True)


def f38_jpdt_469_close_red_after_21d_high_pierce_252d(high: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars that pierce 21d-high but close red (close<open), summed 252d."""
    pierce = high > high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    red = close < open
    return (pierce & red).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_470_close_green_after_21d_low_pierce_252d(low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars that pierce 21d-low but close green (close>open), summed 252d."""
    pierce = low < low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    green = close > open
    return (pierce & green).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Classical candle patterns (471-480)
# ============================================================

def f38_jpdt_471_doji_at_21d_high_count_252d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Doji bars (|C-O|/range<0.1) at 21d-high count over 252d."""
    rng = (high - low).replace(0, np.nan)
    doji = (close - open).abs() / rng < 0.1
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max())
    return (doji & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_472_doji_at_252d_high_count_252d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Doji bars at 252d-high count over 252d (top-of-range indecision)."""
    rng = (high - low).replace(0, np.nan)
    doji = (close - open).abs() / rng < 0.1
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max())
    return (doji & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_473_dark_cloud_cover_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dark cloud cover: today's open > prior high AND close < midpoint of prior bullish body."""
    bullish_prior = close.shift(1) > open.shift(1)
    body_mid_prior = (open.shift(1) + close.shift(1)) / 2.0
    pattern = (open > high.shift(1)) & (close < body_mid_prior) & (close < open) & bullish_prior
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_474_piercing_line_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Piercing line: today's open < prior low AND close > midpoint of prior bearish body."""
    bearish_prior = close.shift(1) < open.shift(1)
    body_mid_prior = (open.shift(1) + close.shift(1)) / 2.0
    pattern = (open < low.shift(1)) & (close > body_mid_prior) & (close > open) & bearish_prior
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_475_evening_star_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Evening star: strong up bar, doji/small, strong down bar over 3 bars."""
    rng = (high - low).replace(0, np.nan)
    big_up_2 = (close.shift(2) - open.shift(2)) > (rng.shift(2) * 0.6)
    doji_1 = (close.shift(1) - open.shift(1)).abs() / rng.shift(1) < 0.2
    big_dn_0 = (open - close) > (rng * 0.6)
    return (big_up_2 & doji_1 & big_dn_0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_476_morning_star_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Morning star: strong down bar, doji/small, strong up bar over 3 bars."""
    rng = (high - low).replace(0, np.nan)
    big_dn_2 = (open.shift(2) - close.shift(2)) > (rng.shift(2) * 0.6)
    doji_1 = (close.shift(1) - open.shift(1)).abs() / rng.shift(1) < 0.2
    big_up_0 = (close - open) > (rng * 0.6)
    return (big_dn_2 & doji_1 & big_up_0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_477_bearish_engulfing_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish engulfing: today's bearish body engulfs prior bullish body."""
    bullish_prior = close.shift(1) > open.shift(1)
    bearish_now = close < open
    engulfs = (open > close.shift(1)) & (close < open.shift(1))
    return (bullish_prior & bearish_now & engulfs).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_478_bullish_engulfing_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish engulfing: today's bullish body engulfs prior bearish body."""
    bearish_prior = close.shift(1) < open.shift(1)
    bullish_now = close > open
    engulfs = (open < close.shift(1)) & (close > open.shift(1))
    return (bearish_prior & bullish_now & engulfs).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_479_tweezer_top_count_252d(high: pd.Series) -> pd.Series:
    """Tweezer top: today's high == prior high (within 0.1%) over 252d."""
    eq_high = (high - high.shift(1)).abs() / high < 0.001
    return eq_high.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_480_tweezer_bottom_count_252d(low: pd.Series) -> pd.Series:
    """Tweezer bottom: today's low == prior low (within 0.1%) over 252d."""
    eq_low = (low - low.shift(1)).abs() / low < 0.001
    return eq_low.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket D — Close-position dynamics (481-488)
# ============================================================

def f38_jpdt_481_close_upper_quartile_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days closing in upper 25% of bar's range, count over 252d."""
    pos = _safe_div(close - low, high - low)
    return (pos > 0.75).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_482_close_lower_quartile_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days closing in lower 25% of bar's range, count over 252d."""
    pos = _safe_div(close - low, high - low)
    return (pos < 0.25).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_483_close_at_high_count_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Days closing within 1% of bar's high, count over 252d."""
    return ((high - close) / high < 0.01).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_484_close_at_low_count_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Days closing within 1% of bar's low, count over 252d."""
    return ((close - low) / low < 0.01).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_485_persistent_upper_close_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 5+ consecutive days closing in top 25% of range, over 252d."""
    pos = _safe_div(close - low, high - low)
    top = (pos > 0.75)
    five_seq = top & top.shift(1).fillna(False) & top.shift(2).fillna(False) & top.shift(3).fillna(False) & top.shift(4).fillna(False)
    return five_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_486_persistent_lower_close_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 5+ consecutive days closing in bottom 25% of range, over 252d."""
    pos = _safe_div(close - low, high - low)
    bot = (pos < 0.25)
    five_seq = bot & bot.shift(1).fillna(False) & bot.shift(2).fillna(False) & bot.shift(3).fillna(False) & bot.shift(4).fillna(False)
    return five_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_487_clv_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of close-position-in-range — CLV trend."""
    pos = _safe_div(close - low, high - low)
    return _rolling_slope(pos, QDAYS)


def f38_jpdt_488_clv_regime_transitions_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CLV-rolling-mean crossings of 0.5 (regime transitions) over 252d."""
    pos = _safe_div(close - low, high - low)
    smoothed = pos.rolling(WDAYS, min_periods=2).mean()
    above = (smoothed > 0.5).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket E — Volume profile (489-495)
# ============================================================

def f38_jpdt_489_mean_volume_top_decile_r_vs_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on top-decile-|r| days / mean volume over 252d."""
    a = _log_ret(close).abs()
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    top_vol = volume.where(a > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    avg_vol = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(top_vol, avg_vol)


def f38_jpdt_490_mean_volume_bottom_decile_r_vs_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on bottom-decile-|r| days / mean volume over 252d."""
    a = _log_ret(close).abs()
    p10 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10).shift(1)
    bot_vol = volume.where(a < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    avg_vol = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(bot_vol, avg_vol)


def f38_jpdt_491_vol_zscore_neg_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume z-score on negative-r days only over 252d."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return vz.where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_492_vol_zscore_pos_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume z-score on positive-r days only over 252d."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return vz.where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_493_recent_vs_annual_volume_ratio(volume: pd.Series) -> pd.Series:
    """Σ volume last 21d / Σ volume last 252d (annualized ratio = 21/252)."""
    return _safe_div(volume.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS,
                     volume.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS)


def f38_jpdt_494_volume_concentration_top5_252d(volume: pd.Series) -> pd.Series:
    """Σ top-5 volume days / Σ all 252d volume (volume concentration)."""
    def _conc(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS or ww.sum() == 0: return np.nan
        return float(np.sort(ww)[-5:].sum() / ww.sum())
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_conc, raw=True)


def f38_jpdt_495_mean_volume_5d_after_252d_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume in 5d window after a 252d-high event, over 252d (causal lag)."""
    new_high_lag = (close.shift(WDAYS) >= close.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return volume.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket F — Risk-bar combinations (496-503)
# ============================================================

def f38_jpdt_496_hindenburg_style_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Hindenburg-style: 52w-high AND 52w-low both within trailing 21d, count over 252d."""
    new_high_21 = (high.rolling(MDAYS, min_periods=WDAYS).max() >= high.rolling(YDAYS, min_periods=QDAYS).max() * 0.999)
    new_low_21 = (low.rolling(MDAYS, min_periods=WDAYS).min() <= low.rolling(YDAYS, min_periods=QDAYS).min() * 1.001)
    return (new_high_21 & new_low_21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_497_wide_range_poor_close_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """TR > 2·ATR(21).shift(1) AND close < open, count over 252d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    wide = tr > 2 * atr_lag
    bearish = close < open
    return (wide & bearish).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_498_nr4_at_new_21d_high_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR4 (narrowest of last 4) at 21d-high, count over 252d (compression at high)."""
    rng = high - low
    nr4 = (rng == rng.rolling(4, min_periods=4).min())
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max())
    return (nr4 & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_499_doji_on_big_volume_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Doji (small body) on top-decile-volume days count over 252d (indecision with conviction)."""
    rng = (high - low).replace(0, np.nan)
    doji = (close - open).abs() / rng < 0.1
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    big_vol = vz > 2.0
    return (doji & big_vol).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_500_gap_fill_failure_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap up + close < open + close > prior_close (partial fill, bearish recovery) over 252d."""
    gap_up = open > close.shift(1) * 1.005
    bearish = close < open
    not_full_fill = close > close.shift(1)
    return (gap_up & bearish & not_full_fill).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_501_gap_fill_success_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap up + close fills entire gap (close ≤ prior_close) count over 252d."""
    gap_up = open > close.shift(1) * 1.005
    filled = close <= close.shift(1)
    return (gap_up & filled).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_502_stop_run_count_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Stop-run: low pierces 5d-low but close > 5d-low at bar close, over 252d."""
    prior_5d_low = low.shift(1).rolling(WDAYS, min_periods=2).min()
    pierce = low < prior_5d_low
    recovered = close > prior_5d_low
    return (pierce & recovered).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_503_failed_test_prior_low_count_252d(low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Low < 21d-prior-low but close > 21d-prior-low + ATR(21), count over 252d (strong-bounce-from-test)."""
    prior_21d_low = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    atr_21 = _atr(high, low, close, MDAYS)
    pierce = low < prior_21d_low
    strong_recover = close > prior_21d_low + atr_21
    return (pierce & strong_recover).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket G — Cumulative effects (504-510)
# ============================================================

def f38_jpdt_504_net_up_minus_down_days_21d(close: pd.Series) -> pd.Series:
    """Net (up days count − down days count) over 21d."""
    r = _log_ret(close)
    up = (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (r < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return up - dn


def f38_jpdt_505_top5_abs_r_sum_21d(close: pd.Series) -> pd.Series:
    """Sum of top-5 largest |r| moves within trailing 21d."""
    a = _log_ret(close).abs()
    return a.rolling(MDAYS, min_periods=WDAYS).apply(
        lambda w: float(np.sort(w[~np.isnan(w)])[-5:].sum()) if np.sum(~np.isnan(w)) >= 5 else np.nan,
        raw=True)


def f38_jpdt_506_top5_abs_r_sum_63d(close: pd.Series) -> pd.Series:
    """Sum of top-5 largest |r| moves within trailing 63d."""
    a = _log_ret(close).abs()
    return a.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: float(np.sort(w[~np.isnan(w)])[-5:].sum()) if np.sum(~np.isnan(w)) >= 5 else np.nan,
        raw=True)


def f38_jpdt_507_top3_concentration_pct_252d(close: pd.Series) -> pd.Series:
    """Top-3 |r| moves / Σ|r| over 252d (move-concentration %)."""
    a = _log_ret(close).abs()

    def _conc(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS or ww.sum() == 0: return np.nan
        return float(np.sort(ww)[-3:].sum() / ww.sum())
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_conc, raw=True)


def f38_jpdt_508_last_week_move_concentration(close: pd.Series) -> pd.Series:
    """Σ|r| last 5d / Σ|r| last 21d — recent move share."""
    a = _log_ret(close).abs()
    return _safe_div(a.rolling(WDAYS, min_periods=2).sum(), a.rolling(MDAYS, min_periods=WDAYS).sum())


def f38_jpdt_509_ret_dd_ratio_21d(close: pd.Series) -> pd.Series:
    """21d log return / max drawdown depth within 21d (recovery efficiency)."""
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))

    def _dd(w):
        ww = w[~np.isnan(w)]
        if len(ww) < WDAYS: return np.nan
        peak = np.maximum.accumulate(ww)
        return float(np.max(1.0 - ww / peak))
    dd = close.rolling(MDAYS, min_periods=WDAYS).apply(_dd, raw=True)
    return _safe_div(r21, dd + 0.01)


def f38_jpdt_510_rv_5d_annualized_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Σr² in last 5d annualized / Σr² in last 252d annualized — vol acceleration."""
    r2 = _log_ret(close) ** 2
    return _safe_div(r2.rolling(WDAYS, min_periods=2).sum() * (YDAYS / WDAYS),
                     r2.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
# Bucket H — Escalating tail-event sequences (511-517)
# ============================================================

def f38_jpdt_511_seq_2sig_then_3sig_252d(close: pd.Series) -> pd.Series:
    """2σ_21d move followed within 5 bars by a 3σ_21d move, count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    a = r.abs()
    move2 = (a > 2 * sig)
    move3 = (a > 3 * sig)
    seq = move3 & move2.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_512_seq_3sig_then_4sig_252d(close: pd.Series) -> pd.Series:
    """3σ move followed within 5 bars by a 4σ move, count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    a = r.abs()
    move3 = (a > 3 * sig)
    move4 = (a > 4 * sig)
    seq = move4 & move3.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_513_seq_4sig_then_5sig_252d(close: pd.Series) -> pd.Series:
    """4σ move followed within 5 bars by a 5σ move, count over 252d (rare extreme escalation)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    a = r.abs()
    move4 = (a > 4 * sig)
    move5 = (a > 5 * sig)
    seq = move5 & move4.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_514_dn_jump_then_bigger_dn_252d(close: pd.Series) -> pd.Series:
    """Down-jump (3σ) followed within 5 bars by a larger down-jump (|r| > prior jump), count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = r < -3 * sig
    dn_mag = r.abs().where(dn, 0.0)
    prior_dn_mag = dn_mag.shift(1).rolling(WDAYS, min_periods=1).max()
    bigger = dn & (r.abs() > prior_dn_mag) & (prior_dn_mag > 0)
    return bigger.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_515_up_jump_then_bigger_up_252d(close: pd.Series) -> pd.Series:
    """Up-jump (3σ) followed within 5 bars by a larger up-jump, count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = r > 3 * sig
    up_mag = r.abs().where(up, 0.0)
    prior_up_mag = up_mag.shift(1).rolling(WDAYS, min_periods=1).max()
    bigger = up & (r.abs() > prior_up_mag) & (prior_up_mag > 0)
    return bigger.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_516_two_consecutive_2sig_count_252d(close: pd.Series) -> pd.Series:
    """Two consecutive bars with |r| > 2σ_21d, count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    move2 = r.abs() > 2 * sig
    return (move2 & move2.shift(1).fillna(False)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_517_three_consecutive_2sig_count_252d(close: pd.Series) -> pd.Series:
    """Three consecutive bars with |r| > 2σ_21d, count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    move2 = r.abs() > 2 * sig
    return (move2 & move2.shift(1).fillna(False) & move2.shift(2).fillna(False)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket I — Bayesian conditional probabilities (518-525)
# ============================================================

def f38_jpdt_518_p_jump_given_high_sigma_252d(close: pd.Series) -> pd.Series:
    """P(jump | σ_21 in top quartile of past 252d) — conditional jump probability."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    in_regime = (sig > p75)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    joint = (in_regime & jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = in_regime.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_519_p_jump_given_low_sigma_252d(close: pd.Series) -> pd.Series:
    """P(jump | σ_21 in bottom quartile of past 252d) — surprise-jump rate."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    in_regime = (sig < p25)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    joint = (in_regime & jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = in_regime.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_520_p_jump_given_top_decile_range_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P(jump | close in top decile of 252d range) over 252d."""
    r = _log_ret(close)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    in_top = (pos >= 0.90)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    joint = (in_top & jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = in_top.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_521_p_jump_given_top_decile_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """P(jump | volume in top decile of past 252d) over 252d."""
    r = _log_ret(close)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    in_top = (volume > p90)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS))
    joint = (in_top & jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = in_top.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_522_p_down_given_3up_252d(close: pd.Series) -> pd.Series:
    """P(down-day | prior 3 days all up) over 252d."""
    r = _log_ret(close)
    three_up = (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0)
    dn = (r < 0)
    joint = (three_up & dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = three_up.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_523_p_up_given_3down_252d(close: pd.Series) -> pd.Series:
    """P(up-day | prior 3 days all down) over 252d."""
    r = _log_ret(close)
    three_dn = (r.shift(1) < 0) & (r.shift(2) < 0) & (r.shift(3) < 0)
    up = (r > 0)
    joint = (three_dn & up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = three_dn.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg)


def f38_jpdt_524_expected_abs_r_given_2sig_prior_252d(close: pd.Series) -> pd.Series:
    """E[|r_t| | r_{t-1} > 2σ_prior] — conditional expected magnitude after up-shock, 252d."""
    r = _log_ret(close)
    sig_lag = _sigma_prior(r, MDAYS).shift(1)
    big_up_prior = r.shift(1) > 2 * sig_lag
    return r.abs().where(big_up_prior, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_525_expected_abs_r_given_neg2sig_prior_252d(close: pd.Series) -> pd.Series:
    """E[|r_t| | r_{t-1} < −2σ_prior] — conditional expected magnitude after down-shock, 252d."""
    r = _log_ret(close)
    sig_lag = _sigma_prior(r, MDAYS).shift(1)
    big_dn_prior = r.shift(1) < -2 * sig_lag
    return r.abs().where(big_dn_prior, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
#                         REGISTRY 451-525
# ============================================================

JUMP_DETECTION_SIGNATURE_BASE_REGISTRY_451_525 = {
    "f38_jpdt_451_jump_count_after_recent_jump_252d": {"inputs": ["close"], "func": f38_jpdt_451_jump_count_after_recent_jump_252d},
    "f38_jpdt_452_jump_count_after_quiet_5d_252d": {"inputs": ["close"], "func": f38_jpdt_452_jump_count_after_quiet_5d_252d},
    "f38_jpdt_453_jump_count_sigma_rising_volume_rising_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_453_jump_count_sigma_rising_volume_rising_252d},
    "f38_jpdt_454_jump_count_sigma_falling_252d": {"inputs": ["close"], "func": f38_jpdt_454_jump_count_sigma_falling_252d},
    "f38_jpdt_455_jump_count_after_21d_high_close_252d": {"inputs": ["close"], "func": f38_jpdt_455_jump_count_after_21d_high_close_252d},
    "f38_jpdt_456_jump_count_after_21d_low_close_252d": {"inputs": ["close"], "func": f38_jpdt_456_jump_count_after_21d_low_close_252d},
    "f38_jpdt_457_mean_abs_r_after_jump_3d_252d": {"inputs": ["close"], "func": f38_jpdt_457_mean_abs_r_after_jump_3d_252d},
    "f38_jpdt_458_dn_jump_in_strong_uptrend_252d": {"inputs": ["close"], "func": f38_jpdt_458_dn_jump_in_strong_uptrend_252d},
    "f38_jpdt_459_up_jump_in_strong_downtrend_252d": {"inputs": ["close"], "func": f38_jpdt_459_up_jump_in_strong_downtrend_252d},
    "f38_jpdt_460_mean_post_jump_21d_return_252d": {"inputs": ["close"], "func": f38_jpdt_460_mean_post_jump_21d_return_252d},
    "f38_jpdt_461_lower_high_count_after_21d_high_252d": {"inputs": ["high"], "func": f38_jpdt_461_lower_high_count_after_21d_high_252d},
    "f38_jpdt_462_lower_low_count_after_21d_low_252d": {"inputs": ["low"], "func": f38_jpdt_462_lower_low_count_after_21d_low_252d},
    "f38_jpdt_463_failed_bounce_count_252d": {"inputs": ["high", "low", "open", "close"], "func": f38_jpdt_463_failed_bounce_count_252d},
    "f38_jpdt_464_failed_rally_count_252d": {"inputs": ["high", "low", "open", "close"], "func": f38_jpdt_464_failed_rally_count_252d},
    "f38_jpdt_465_distribution_sequence_count_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_465_distribution_sequence_count_252d},
    "f38_jpdt_466_accumulation_sequence_count_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_466_accumulation_sequence_count_252d},
    "f38_jpdt_467_higher_highs_streak_count_63d": {"inputs": ["high"], "func": f38_jpdt_467_higher_highs_streak_count_63d},
    "f38_jpdt_468_lower_lows_streak_count_63d": {"inputs": ["low"], "func": f38_jpdt_468_lower_lows_streak_count_63d},
    "f38_jpdt_469_close_red_after_21d_high_pierce_252d": {"inputs": ["high", "open", "close"], "func": f38_jpdt_469_close_red_after_21d_high_pierce_252d},
    "f38_jpdt_470_close_green_after_21d_low_pierce_252d": {"inputs": ["low", "open", "close"], "func": f38_jpdt_470_close_green_after_21d_low_pierce_252d},
    "f38_jpdt_471_doji_at_21d_high_count_252d": {"inputs": ["high", "low", "open", "close"], "func": f38_jpdt_471_doji_at_21d_high_count_252d},
    "f38_jpdt_472_doji_at_252d_high_count_252d": {"inputs": ["high", "low", "open", "close"], "func": f38_jpdt_472_doji_at_252d_high_count_252d},
    "f38_jpdt_473_dark_cloud_cover_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_473_dark_cloud_cover_count_252d},
    "f38_jpdt_474_piercing_line_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_474_piercing_line_count_252d},
    "f38_jpdt_475_evening_star_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_475_evening_star_count_252d},
    "f38_jpdt_476_morning_star_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_476_morning_star_count_252d},
    "f38_jpdt_477_bearish_engulfing_count_252d": {"inputs": ["open", "close"], "func": f38_jpdt_477_bearish_engulfing_count_252d},
    "f38_jpdt_478_bullish_engulfing_count_252d": {"inputs": ["open", "close"], "func": f38_jpdt_478_bullish_engulfing_count_252d},
    "f38_jpdt_479_tweezer_top_count_252d": {"inputs": ["high"], "func": f38_jpdt_479_tweezer_top_count_252d},
    "f38_jpdt_480_tweezer_bottom_count_252d": {"inputs": ["low"], "func": f38_jpdt_480_tweezer_bottom_count_252d},
    "f38_jpdt_481_close_upper_quartile_count_252d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_481_close_upper_quartile_count_252d},
    "f38_jpdt_482_close_lower_quartile_count_252d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_482_close_lower_quartile_count_252d},
    "f38_jpdt_483_close_at_high_count_252d": {"inputs": ["high", "close"], "func": f38_jpdt_483_close_at_high_count_252d},
    "f38_jpdt_484_close_at_low_count_252d": {"inputs": ["low", "close"], "func": f38_jpdt_484_close_at_low_count_252d},
    "f38_jpdt_485_persistent_upper_close_streak_252d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_485_persistent_upper_close_streak_252d},
    "f38_jpdt_486_persistent_lower_close_streak_252d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_486_persistent_lower_close_streak_252d},
    "f38_jpdt_487_clv_slope_63d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_487_clv_slope_63d},
    "f38_jpdt_488_clv_regime_transitions_252d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_488_clv_regime_transitions_252d},
    "f38_jpdt_489_mean_volume_top_decile_r_vs_avg_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_489_mean_volume_top_decile_r_vs_avg_252d},
    "f38_jpdt_490_mean_volume_bottom_decile_r_vs_avg_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_490_mean_volume_bottom_decile_r_vs_avg_252d},
    "f38_jpdt_491_vol_zscore_neg_days_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_491_vol_zscore_neg_days_252d},
    "f38_jpdt_492_vol_zscore_pos_days_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_492_vol_zscore_pos_days_252d},
    "f38_jpdt_493_recent_vs_annual_volume_ratio": {"inputs": ["volume"], "func": f38_jpdt_493_recent_vs_annual_volume_ratio},
    "f38_jpdt_494_volume_concentration_top5_252d": {"inputs": ["volume"], "func": f38_jpdt_494_volume_concentration_top5_252d},
    "f38_jpdt_495_mean_volume_5d_after_252d_high_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_495_mean_volume_5d_after_252d_high_252d},
    "f38_jpdt_496_hindenburg_style_count_252d": {"inputs": ["high", "low"], "func": f38_jpdt_496_hindenburg_style_count_252d},
    "f38_jpdt_497_wide_range_poor_close_count_252d": {"inputs": ["high", "low", "close", "open"], "func": f38_jpdt_497_wide_range_poor_close_count_252d},
    "f38_jpdt_498_nr4_at_new_21d_high_count_252d": {"inputs": ["high", "low"], "func": f38_jpdt_498_nr4_at_new_21d_high_count_252d},
    "f38_jpdt_499_doji_on_big_volume_count_252d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f38_jpdt_499_doji_on_big_volume_count_252d},
    "f38_jpdt_500_gap_fill_failure_count_252d": {"inputs": ["open", "close"], "func": f38_jpdt_500_gap_fill_failure_count_252d},
    "f38_jpdt_501_gap_fill_success_count_252d": {"inputs": ["open", "close"], "func": f38_jpdt_501_gap_fill_success_count_252d},
    "f38_jpdt_502_stop_run_count_252d": {"inputs": ["low", "close"], "func": f38_jpdt_502_stop_run_count_252d},
    "f38_jpdt_503_failed_test_prior_low_count_252d": {"inputs": ["low", "high", "close"], "func": f38_jpdt_503_failed_test_prior_low_count_252d},
    "f38_jpdt_504_net_up_minus_down_days_21d": {"inputs": ["close"], "func": f38_jpdt_504_net_up_minus_down_days_21d},
    "f38_jpdt_505_top5_abs_r_sum_21d": {"inputs": ["close"], "func": f38_jpdt_505_top5_abs_r_sum_21d},
    "f38_jpdt_506_top5_abs_r_sum_63d": {"inputs": ["close"], "func": f38_jpdt_506_top5_abs_r_sum_63d},
    "f38_jpdt_507_top3_concentration_pct_252d": {"inputs": ["close"], "func": f38_jpdt_507_top3_concentration_pct_252d},
    "f38_jpdt_508_last_week_move_concentration": {"inputs": ["close"], "func": f38_jpdt_508_last_week_move_concentration},
    "f38_jpdt_509_ret_dd_ratio_21d": {"inputs": ["close"], "func": f38_jpdt_509_ret_dd_ratio_21d},
    "f38_jpdt_510_rv_5d_annualized_vs_252d_ratio": {"inputs": ["close"], "func": f38_jpdt_510_rv_5d_annualized_vs_252d_ratio},
    "f38_jpdt_511_seq_2sig_then_3sig_252d": {"inputs": ["close"], "func": f38_jpdt_511_seq_2sig_then_3sig_252d},
    "f38_jpdt_512_seq_3sig_then_4sig_252d": {"inputs": ["close"], "func": f38_jpdt_512_seq_3sig_then_4sig_252d},
    "f38_jpdt_513_seq_4sig_then_5sig_252d": {"inputs": ["close"], "func": f38_jpdt_513_seq_4sig_then_5sig_252d},
    "f38_jpdt_514_dn_jump_then_bigger_dn_252d": {"inputs": ["close"], "func": f38_jpdt_514_dn_jump_then_bigger_dn_252d},
    "f38_jpdt_515_up_jump_then_bigger_up_252d": {"inputs": ["close"], "func": f38_jpdt_515_up_jump_then_bigger_up_252d},
    "f38_jpdt_516_two_consecutive_2sig_count_252d": {"inputs": ["close"], "func": f38_jpdt_516_two_consecutive_2sig_count_252d},
    "f38_jpdt_517_three_consecutive_2sig_count_252d": {"inputs": ["close"], "func": f38_jpdt_517_three_consecutive_2sig_count_252d},
    "f38_jpdt_518_p_jump_given_high_sigma_252d": {"inputs": ["close"], "func": f38_jpdt_518_p_jump_given_high_sigma_252d},
    "f38_jpdt_519_p_jump_given_low_sigma_252d": {"inputs": ["close"], "func": f38_jpdt_519_p_jump_given_low_sigma_252d},
    "f38_jpdt_520_p_jump_given_top_decile_range_252d": {"inputs": ["close", "high", "low"], "func": f38_jpdt_520_p_jump_given_top_decile_range_252d},
    "f38_jpdt_521_p_jump_given_top_decile_volume_252d": {"inputs": ["close", "volume"], "func": f38_jpdt_521_p_jump_given_top_decile_volume_252d},
    "f38_jpdt_522_p_down_given_3up_252d": {"inputs": ["close"], "func": f38_jpdt_522_p_down_given_3up_252d},
    "f38_jpdt_523_p_up_given_3down_252d": {"inputs": ["close"], "func": f38_jpdt_523_p_up_given_3down_252d},
    "f38_jpdt_524_expected_abs_r_given_2sig_prior_252d": {"inputs": ["close"], "func": f38_jpdt_524_expected_abs_r_given_2sig_prior_252d},
    "f38_jpdt_525_expected_abs_r_given_neg2sig_prior_252d": {"inputs": ["close"], "func": f38_jpdt_525_expected_abs_r_given_neg2sig_prior_252d},
}
