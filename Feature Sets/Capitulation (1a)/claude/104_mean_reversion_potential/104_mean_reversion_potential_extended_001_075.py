"""
104_mean_reversion_potential — Extended Features 001-075
Domain: distance-from-equilibrium and reversion-potential metrics — additional
        angles not in the four base files: alternate-window stretch and band
        overshoot, RSI-of-stretch reversion oscillators, gap-fill / overshoot
        decay dynamics, half-life on new windows, range-compression and
        consolidation proxies, overshoot streaks, percentile/z-score variants
        and fresh snap-back composites.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Z-score of a series over a trailing w-day window."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _ar1(s: pd.Series, w: int) -> pd.Series:
    """Rolling lag-1 autocorrelation of a series over window w."""
    return s.rolling(w, min_periods=max(5, w // 2)).corr(s.shift(1))


def _half_life(phi: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by an AR(1) coefficient phi."""
    p = phi.clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(2.0) / np.log(p)


def _stretch(close: pd.Series, w: int) -> pd.Series:
    """Deviation of close from its w-day SMA in w-day-std units."""
    return _safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))


def _rsi(s: pd.Series, w: int) -> pd.Series:
    """Wilder-style RSI of a generic series over window w (0-100)."""
    delta = s.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    ad = down.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    rs = _safe_div(au, ad)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Stretch from equilibrium on alternate windows ---

def mrp_ext_001_stretch_from_sma10(close: pd.Series) -> pd.Series:
    """Deviation of close from its 10-day SMA in 10-day-std units."""
    return _stretch(close, 10)


def mrp_ext_002_stretch_from_sma42(close: pd.Series) -> pd.Series:
    """Deviation of close from its 42-day SMA in 42-day-std units."""
    return _stretch(close, 42)


def mrp_ext_003_stretch_from_sma189(close: pd.Series) -> pd.Series:
    """Deviation of close from its 189-day SMA in 189-day-std units."""
    return _stretch(close, 189)


def mrp_ext_004_stretch_from_sma504(close: pd.Series) -> pd.Series:
    """Deviation of close from its 504-day SMA in 504-day-std units."""
    return _stretch(close, 504)


def mrp_ext_005_stretch_from_ema21(close: pd.Series) -> pd.Series:
    """Deviation of close from its 21-day EMA in 21-day-std units."""
    ma = _ewm_mean(close, _TD_MON)
    return _safe_div(close - ma, _rolling_std(close, _TD_MON))


def mrp_ext_006_stretch_from_ema126(close: pd.Series) -> pd.Series:
    """Deviation of close from its 126-day EMA in 126-day-std units."""
    ma = _ewm_mean(close, _TD_HALF)
    return _safe_div(close - ma, _rolling_std(close, _TD_HALF))


def mrp_ext_007_stretch_from_median_63d(close: pd.Series) -> pd.Series:
    """Deviation of close from its 63-day rolling median in 63-day-std units."""
    med = _rolling_median(close, _TD_QTR)
    return _safe_div(close - med, _rolling_std(close, _TD_QTR))


def mrp_ext_008_distance_below_mean_42d(close: pd.Series) -> pd.Series:
    """Negative part of the percent deviation from the 42-day mean."""
    ma = _rolling_mean(close, 42)
    return _safe_div(close - ma, ma).clip(upper=0)


def mrp_ext_009_distance_below_mean_504d(close: pd.Series) -> pd.Series:
    """Negative part of the percent deviation from the 504-day mean."""
    ma = _rolling_mean(close, 504)
    return _safe_div(close - ma, ma).clip(upper=0)


def mrp_ext_010_max_stretch_below_alt(close: pd.Series) -> pd.Series:
    """Most negative stretch across the 10/42/189/504-day equilibria."""
    parts = [_stretch(close, w) for w in (10, 42, 189, 504)]
    return pd.concat(parts, axis=1).min(axis=1)


def mrp_ext_011_mean_stretch_alt(close: pd.Series) -> pd.Series:
    """Mean stretch across the 10/42/189/504-day equilibria."""
    parts = [_stretch(close, w) for w in (10, 42, 189, 504)]
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_ext_012_stretch_dispersion_alt(close: pd.Series) -> pd.Series:
    """Cross-window standard deviation of the alternate-window stretches."""
    parts = [_stretch(close, w) for w in (10, 42, 189, 504)]
    return pd.concat(parts, axis=1).std(axis=1)


# --- Group B (013-024): RSI-of-stretch and reversion oscillators ---

def mrp_ext_013_rsi_of_stretch_63d(close: pd.Series) -> pd.Series:
    """14-day RSI computed on the 63-day stretch series (reversion oscillator)."""
    return _rsi(_stretch(close, _TD_QTR), 14)


def mrp_ext_014_rsi_of_stretch_252d(close: pd.Series) -> pd.Series:
    """14-day RSI computed on the 252-day stretch series."""
    return _rsi(_stretch(close, _TD_YEAR), 14)


def mrp_ext_015_rsi_of_dev_from_mean(close: pd.Series) -> pd.Series:
    """14-day RSI of the percent deviation from the 63-day mean."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma)
    return _rsi(dev, 14)


def mrp_ext_016_stretch_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 63-day stretch (reversion velocity)."""
    return _stretch(close, _TD_QTR).diff(_TD_WEEK)


def mrp_ext_017_stretch_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63-day stretch (slower reversion velocity)."""
    return _stretch(close, _TD_QTR).diff(_TD_MON)


def mrp_ext_018_stretch_recovery_off_min(close: pd.Series) -> pd.Series:
    """Gap between the current 63-day stretch and its trailing 63-day minimum."""
    st = _stretch(close, _TD_QTR)
    return st - _rolling_min(st, _TD_QTR)


def mrp_ext_019_dev_smoothed_minus_raw(close: pd.Series) -> pd.Series:
    """5-day EMA of the 63-day deviation minus its raw value (turn signal)."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma)
    return _ewm_mean(dev, _TD_WEEK) - dev


def mrp_ext_020_stretch_oscillator_position(close: pd.Series) -> pd.Series:
    """Position of the 63-day stretch within its trailing 252-day range (0-1)."""
    st = _stretch(close, _TD_QTR)
    lo = _rolling_min(st, _TD_YEAR)
    hi = _rolling_max(st, _TD_YEAR)
    return _safe_div(st - lo, hi - lo)


def mrp_ext_021_dev_zscore_short(close: pd.Series) -> pd.Series:
    """Z-score of the 21-day deviation-from-mean over a trailing 63-day window."""
    ma = _rolling_mean(close, _TD_MON)
    dev = _safe_div(close - ma, ma)
    return _zscore(dev, _TD_QTR)


def mrp_ext_022_stretch_momentum_sign(close: pd.Series) -> pd.Series:
    """Sign of the 5-day change in the 63-day stretch (-1, 0, +1)."""
    return np.sign(_stretch(close, _TD_QTR).diff(_TD_WEEK))


def mrp_ext_023_rsi_of_stretch_oversold_flag(close: pd.Series) -> pd.Series:
    """Flag: the 14-day RSI of the 63-day stretch is below 20."""
    return (_rsi(_stretch(close, _TD_QTR), 14) < 20).astype(float)


def mrp_ext_024_stretch_turn_up_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day stretch is below -2 yet has risen over the last 3 days."""
    st = _stretch(close, _TD_QTR)
    return ((st < -2.0) & (st.diff(3) > 0)).astype(float)


# --- Group C (025-038): Gap-fill, overshoot decay and band dynamics ---

def mrp_ext_025_gap_to_sma21(close: pd.Series) -> pd.Series:
    """Percent gap between the close and its 21-day equilibrium mean."""
    ma = _rolling_mean(close, _TD_MON)
    return _safe_div(ma - close, ma)


def mrp_ext_026_gap_to_sma252(close: pd.Series) -> pd.Series:
    """Percent gap between the close and its 252-day equilibrium mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(ma - close, ma)


def mrp_ext_027_gap_to_ema63(close: pd.Series) -> pd.Series:
    """Percent gap between the close and its 63-day EMA equilibrium."""
    ma = _ewm_mean(close, _TD_QTR)
    return _safe_div(ma - close, ma)


def mrp_ext_028_overshoot_decay_5d(close: pd.Series) -> pd.Series:
    """5-day reduction in below-band overshoot (positive = decaying overshoot)."""
    z = _stretch(close, _TD_QTR)
    overshoot = (-(z + 2.0)).clip(lower=0)
    return overshoot.shift(_TD_WEEK) - overshoot


def mrp_ext_029_overshoot_decay_rate(close: pd.Series) -> pd.Series:
    """Overshoot decay over 5 days relative to its 5-day-prior level."""
    z = _stretch(close, _TD_QTR)
    overshoot = (-(z + 2.0)).clip(lower=0)
    return _safe_div(overshoot.shift(_TD_WEEK) - overshoot, overshoot.shift(_TD_WEEK))


def mrp_ext_030_below_lower_bollinger_126d(close: pd.Series) -> pd.Series:
    """Distance below the 126-day lower Bollinger band, in std units."""
    z = _stretch(close, _TD_HALF)
    return (z + 2.0).clip(upper=0)


def mrp_ext_031_below_lower_bollinger_252d(close: pd.Series) -> pd.Series:
    """Distance below the 252-day lower Bollinger band, in std units."""
    z = _stretch(close, _TD_YEAR)
    return (z + 2.0).clip(upper=0)


def mrp_ext_032_band_overshoot_1_5std_63d(close: pd.Series) -> pd.Series:
    """Magnitude of the 63-day stretch beyond the -1.5 std Bollinger band."""
    z = _stretch(close, _TD_QTR)
    return (-(z + 1.5)).clip(lower=0)


def mrp_ext_033_pct_b_126d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 126-day window (0 = lower band, 1 = upper)."""
    ma = _rolling_mean(close, _TD_HALF)
    sd = _rolling_std(close, _TD_HALF)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_ext_034_pct_b_252d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 252-day window."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_ext_035_donchian_undershoot_21d(close: pd.Series) -> pd.Series:
    """Position of close within the 21-day Donchian channel (0 = at the low)."""
    lo = _rolling_min(close, _TD_MON)
    hi = _rolling_max(close, _TD_MON)
    return _safe_div(close - lo, hi - lo)


def mrp_ext_036_donchian_undershoot_504d(close: pd.Series) -> pd.Series:
    """Position of close within the 504-day Donchian channel (0 = at the low)."""
    lo = _rolling_min(close, 504)
    hi = _rolling_max(close, 504)
    return _safe_div(close - lo, hi - lo)


def mrp_ext_037_gap_to_vwap_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent gap between the close and the 126-day volume-weighted mean price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_HALF), _rolling_sum(volume, _TD_HALF))
    return _safe_div(vwap - close, vwap)


def mrp_ext_038_keltner_lower_overshoot_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below the 126-day Keltner lower channel, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_HALF)
    pos = _safe_div(close - _rolling_mean(close, _TD_HALF), atr)
    return (-(pos + 2.0)).clip(lower=0)


# --- Group D (039-050): Half-life, AR and reversion dynamics on new windows ---

def mrp_ext_039_ar1_returns_42d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 42-day window."""
    return _ar1(_daily_ret(close), 42)


def mrp_ext_040_ar1_returns_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 126-day window."""
    return _ar1(_daily_ret(close), _TD_HALF)


def mrp_ext_041_ar1_price_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of the close level over a 126-day window."""
    return _ar1(close, _TD_HALF)


def mrp_ext_042_reversion_half_life_126d(close: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by 126-day AR(1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_HALF)
    return _half_life(_ar1(detr, _TD_HALF))


def mrp_ext_043_reversion_half_life_21d(close: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by 21-day AR(1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_MON)
    return _half_life(_ar1(detr, _TD_MON))


def mrp_ext_044_ou_theta_126d(close: pd.Series) -> pd.Series:
    """Ornstein-Uhlenbeck reversion rate theta over a 126-day window."""
    detr = close - _rolling_mean(close, _TD_HALF)
    phi = _ar1(detr, _TD_HALF).clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(phi)


def mrp_ext_045_reversion_speed_proxy_126d(close: pd.Series) -> pd.Series:
    """Reversion speed proxy: 1 minus the 126-day price AR(1) coefficient."""
    return 1.0 - _ar1(close, _TD_HALF)


def mrp_ext_046_mean_reversion_strength_126d(close: pd.Series) -> pd.Series:
    """Negative AR(1) of 126-day detrended price (positive = stronger reversion)."""
    detr = close - _rolling_mean(close, _TD_HALF)
    return -_ar1(detr, _TD_HALF)


def mrp_ext_047_half_life_normalized_126d(close: pd.Series) -> pd.Series:
    """126-day reversion half-life normalized by the 126-day window length."""
    detr = close - _rolling_mean(close, _TD_HALF)
    return _half_life(_ar1(detr, _TD_HALF)) / _TD_HALF


def mrp_ext_048_return_autocorr_negative_flag_252d(close: pd.Series) -> pd.Series:
    """Flag: 252-day return autocorrelation is negative (mean-reverting)."""
    return (_ar1(_daily_ret(close), _TD_YEAR) < 0).astype(float)


def mrp_ext_049_ar1_returns_change_63d(close: pd.Series) -> pd.Series:
    """21-day change in the 63-day return autocorrelation (regime shift)."""
    return _ar1(_daily_ret(close), _TD_QTR).diff(_TD_MON)


def mrp_ext_050_half_life_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day reversion half-life within 252 days."""
    detr = close - _rolling_mean(close, _TD_QTR)
    hl = _half_life(_ar1(detr, _TD_QTR))
    return _rolling_rank_pct(hl, _TD_YEAR)


# --- Group E (051-062): Range compression, consolidation & overshoot streaks ---

def mrp_ext_051_range_compression_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day ATR relative to 126-day ATR (low = compressed range)."""
    atr_s = _rolling_mean(_tr(close, high, low), _TD_MON)
    atr_l = _rolling_mean(_tr(close, high, low), _TD_HALF)
    return _safe_div(atr_s, atr_l)


def mrp_ext_052_range_compression_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day ATR relative to 252-day ATR (low = compressed range)."""
    atr_s = _rolling_mean(_tr(close, high, low), _TD_QTR)
    atr_l = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    return _safe_div(atr_s, atr_l)


def mrp_ext_053_realized_vol_compression(close: pd.Series) -> pd.Series:
    """21-day realized volatility relative to 252-day realized volatility."""
    ret = _daily_ret(close)
    return _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_YEAR))


def mrp_ext_054_close_range_width_63d(close: pd.Series) -> pd.Series:
    """Width of the 63-day close range relative to the close (consolidation)."""
    hi = _rolling_max(close, _TD_QTR)
    lo = _rolling_min(close, _TD_QTR)
    return _safe_div(hi - lo, close)


def mrp_ext_055_daily_range_vs_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range relative to its trailing 63-day mean range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, _TD_QTR))


def mrp_ext_056_overshoot_below_band_streak_63d(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 63-day stretch below the -2 std band."""
    return _consec_streak(_stretch(close, _TD_QTR) < -2.0)


def mrp_ext_057_overshoot_below_band_streak_21d(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 21-day stretch below the -2 std band."""
    return _consec_streak(_stretch(close, _TD_MON) < -2.0)


def mrp_ext_058_deep_undershoot_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 63-day stretch below the -3 std band."""
    return _consec_streak(_stretch(close, _TD_QTR) < -3.0)


def mrp_ext_059_below_mean_streak_252d(close: pd.Series) -> pd.Series:
    """Current consecutive-day streak of close below its 252-day mean."""
    return _consec_streak(close < _rolling_mean(close, _TD_YEAR))


def mrp_ext_060_overshoot_streak_max_252d(close: pd.Series) -> pd.Series:
    """Maximum below-band overshoot streak observed over the trailing 252 days."""
    streak = _consec_streak(_stretch(close, _TD_QTR) < -2.0)
    return _rolling_max(streak, _TD_YEAR)


def mrp_ext_061_time_below_band_126d(close: pd.Series) -> pd.Series:
    """Fraction of the last 126 days the 63-day stretch was below the -2 std band."""
    return _rolling_mean((_stretch(close, _TD_QTR) < -2.0).astype(float), _TD_HALF)


def mrp_ext_062_consolidation_at_low_flag(close: pd.Series) -> pd.Series:
    """Flag: compressed 21-day range while close sits in the bottom decile of 252d."""
    ret = _daily_ret(close)
    compressed = _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_YEAR)) < 0.8
    at_low = _rolling_rank_pct(close, _TD_YEAR) < 0.10
    return (compressed & at_low).astype(float)


# --- Group F (063-070): Percentile and z-score variants of stretch / overshoot ---

def mrp_ext_063_stretch_pctile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day stretch within a trailing 63-day window."""
    return _rolling_rank_pct(_stretch(close, _TD_QTR), _TD_QTR)


def mrp_ext_064_stretch_pctile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day stretch within a trailing 504-day window."""
    return _rolling_rank_pct(_stretch(close, _TD_QTR), 504)


def mrp_ext_065_stretch_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of the 21-day stretch over a trailing 63-day window."""
    return _zscore(_stretch(close, _TD_MON), _TD_QTR)


def mrp_ext_066_stretch_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of the 63-day stretch over a trailing 126-day window."""
    return _zscore(_stretch(close, _TD_QTR), _TD_HALF)


def mrp_ext_067_overshoot_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the below-band overshoot magnitude within 252 days."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    return _rolling_rank_pct(overshoot, _TD_YEAR)


def mrp_ext_068_gap_to_mean_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the gap to the 126-day mean within 252 days."""
    ma = _rolling_mean(close, _TD_HALF)
    gap = _safe_div(ma - close, ma)
    return _rolling_rank_pct(gap, _TD_YEAR)


def mrp_ext_069_dev_from_median_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the deviation from the 252-day median over 252 days."""
    med = _rolling_median(close, _TD_YEAR)
    dev = _safe_div(close - med, med)
    return _zscore(dev, _TD_YEAR)


def mrp_ext_070_stretch_min_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank within 252 days of the worst stretch across alt windows."""
    parts = [_stretch(close, w) for w in (10, 42, 189, 504)]
    smin = pd.concat(parts, axis=1).min(axis=1)
    return _rolling_rank_pct(smin, _TD_YEAR)


# --- Group G (071-075): Fresh snap-back composites ---

def mrp_ext_071_gap_x_reversion_speed_126d(close: pd.Series) -> pd.Series:
    """Gap to the 126-day mean scaled by the 126-day reversion speed proxy."""
    ma = _rolling_mean(close, _TD_HALF)
    gap = _safe_div(ma - close, ma).clip(lower=0)
    speed = (1.0 - _ar1(close, _TD_HALF)).clip(lower=0)
    return gap * speed


def mrp_ext_072_overshoot_x_compression(close: pd.Series) -> pd.Series:
    """Below-band overshoot magnitude scaled by range compression (coiled spring)."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    ret = _daily_ret(close)
    compression = _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_YEAR))
    return overshoot * (2.0 - compression.clip(upper=2.0))


def mrp_ext_073_stretch_recovery_potential(close: pd.Series) -> pd.Series:
    """Overshoot depth times the fraction of the last 63 days spent below band."""
    z = _stretch(close, _TD_QTR)
    overshoot = (-z).clip(lower=0) / 3.0
    persistence = _rolling_mean((z < -2.0).astype(float), _TD_QTR)
    return overshoot * (0.5 + persistence)


def mrp_ext_074_multi_window_undershoot_score(close: pd.Series) -> pd.Series:
    """Mean below-band overshoot across the 21/63/126/252-day windows."""
    parts = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR):
        z = _stretch(close, w)
        parts.append((-(z + 2.0)).clip(lower=0))
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_ext_075_mean_reversion_potential_index_ext(close: pd.Series) -> pd.Series:
    """Master index: multi-window undershoot, equilibrium gap and reversion speed.
    Higher = more stored snap-back potential at an exhausted low."""
    parts = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR):
        z = _stretch(close, w)
        parts.append((-(z + 2.0)).clip(lower=0))
    undershoot = pd.concat(parts, axis=1).mean(axis=1) / 3.0
    ma = _rolling_mean(close, _TD_HALF)
    gap = _safe_div(ma - close, ma).clip(lower=0)
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0, upper=2.0) / 2.0
    return (undershoot + gap) * (0.5 + speed)


# ── Registry ──────────────────────────────────────────────────────────────────

MEAN_REVERSION_POTENTIAL_EXTENDED_REGISTRY_001_075 = {
    "mrp_ext_001_stretch_from_sma10": {"inputs": ["close"], "func": mrp_ext_001_stretch_from_sma10},
    "mrp_ext_002_stretch_from_sma42": {"inputs": ["close"], "func": mrp_ext_002_stretch_from_sma42},
    "mrp_ext_003_stretch_from_sma189": {"inputs": ["close"], "func": mrp_ext_003_stretch_from_sma189},
    "mrp_ext_004_stretch_from_sma504": {"inputs": ["close"], "func": mrp_ext_004_stretch_from_sma504},
    "mrp_ext_005_stretch_from_ema21": {"inputs": ["close"], "func": mrp_ext_005_stretch_from_ema21},
    "mrp_ext_006_stretch_from_ema126": {"inputs": ["close"], "func": mrp_ext_006_stretch_from_ema126},
    "mrp_ext_007_stretch_from_median_63d": {"inputs": ["close"], "func": mrp_ext_007_stretch_from_median_63d},
    "mrp_ext_008_distance_below_mean_42d": {"inputs": ["close"], "func": mrp_ext_008_distance_below_mean_42d},
    "mrp_ext_009_distance_below_mean_504d": {"inputs": ["close"], "func": mrp_ext_009_distance_below_mean_504d},
    "mrp_ext_010_max_stretch_below_alt": {"inputs": ["close"], "func": mrp_ext_010_max_stretch_below_alt},
    "mrp_ext_011_mean_stretch_alt": {"inputs": ["close"], "func": mrp_ext_011_mean_stretch_alt},
    "mrp_ext_012_stretch_dispersion_alt": {"inputs": ["close"], "func": mrp_ext_012_stretch_dispersion_alt},
    "mrp_ext_013_rsi_of_stretch_63d": {"inputs": ["close"], "func": mrp_ext_013_rsi_of_stretch_63d},
    "mrp_ext_014_rsi_of_stretch_252d": {"inputs": ["close"], "func": mrp_ext_014_rsi_of_stretch_252d},
    "mrp_ext_015_rsi_of_dev_from_mean": {"inputs": ["close"], "func": mrp_ext_015_rsi_of_dev_from_mean},
    "mrp_ext_016_stretch_velocity_5d": {"inputs": ["close"], "func": mrp_ext_016_stretch_velocity_5d},
    "mrp_ext_017_stretch_velocity_21d": {"inputs": ["close"], "func": mrp_ext_017_stretch_velocity_21d},
    "mrp_ext_018_stretch_recovery_off_min": {"inputs": ["close"], "func": mrp_ext_018_stretch_recovery_off_min},
    "mrp_ext_019_dev_smoothed_minus_raw": {"inputs": ["close"], "func": mrp_ext_019_dev_smoothed_minus_raw},
    "mrp_ext_020_stretch_oscillator_position": {"inputs": ["close"], "func": mrp_ext_020_stretch_oscillator_position},
    "mrp_ext_021_dev_zscore_short": {"inputs": ["close"], "func": mrp_ext_021_dev_zscore_short},
    "mrp_ext_022_stretch_momentum_sign": {"inputs": ["close"], "func": mrp_ext_022_stretch_momentum_sign},
    "mrp_ext_023_rsi_of_stretch_oversold_flag": {"inputs": ["close"], "func": mrp_ext_023_rsi_of_stretch_oversold_flag},
    "mrp_ext_024_stretch_turn_up_flag": {"inputs": ["close"], "func": mrp_ext_024_stretch_turn_up_flag},
    "mrp_ext_025_gap_to_sma21": {"inputs": ["close"], "func": mrp_ext_025_gap_to_sma21},
    "mrp_ext_026_gap_to_sma252": {"inputs": ["close"], "func": mrp_ext_026_gap_to_sma252},
    "mrp_ext_027_gap_to_ema63": {"inputs": ["close"], "func": mrp_ext_027_gap_to_ema63},
    "mrp_ext_028_overshoot_decay_5d": {"inputs": ["close"], "func": mrp_ext_028_overshoot_decay_5d},
    "mrp_ext_029_overshoot_decay_rate": {"inputs": ["close"], "func": mrp_ext_029_overshoot_decay_rate},
    "mrp_ext_030_below_lower_bollinger_126d": {"inputs": ["close"], "func": mrp_ext_030_below_lower_bollinger_126d},
    "mrp_ext_031_below_lower_bollinger_252d": {"inputs": ["close"], "func": mrp_ext_031_below_lower_bollinger_252d},
    "mrp_ext_032_band_overshoot_1_5std_63d": {"inputs": ["close"], "func": mrp_ext_032_band_overshoot_1_5std_63d},
    "mrp_ext_033_pct_b_126d": {"inputs": ["close"], "func": mrp_ext_033_pct_b_126d},
    "mrp_ext_034_pct_b_252d": {"inputs": ["close"], "func": mrp_ext_034_pct_b_252d},
    "mrp_ext_035_donchian_undershoot_21d": {"inputs": ["close"], "func": mrp_ext_035_donchian_undershoot_21d},
    "mrp_ext_036_donchian_undershoot_504d": {"inputs": ["close"], "func": mrp_ext_036_donchian_undershoot_504d},
    "mrp_ext_037_gap_to_vwap_126d": {"inputs": ["close", "volume"], "func": mrp_ext_037_gap_to_vwap_126d},
    "mrp_ext_038_keltner_lower_overshoot_126d": {"inputs": ["close", "high", "low"], "func": mrp_ext_038_keltner_lower_overshoot_126d},
    "mrp_ext_039_ar1_returns_42d": {"inputs": ["close"], "func": mrp_ext_039_ar1_returns_42d},
    "mrp_ext_040_ar1_returns_126d": {"inputs": ["close"], "func": mrp_ext_040_ar1_returns_126d},
    "mrp_ext_041_ar1_price_126d": {"inputs": ["close"], "func": mrp_ext_041_ar1_price_126d},
    "mrp_ext_042_reversion_half_life_126d": {"inputs": ["close"], "func": mrp_ext_042_reversion_half_life_126d},
    "mrp_ext_043_reversion_half_life_21d": {"inputs": ["close"], "func": mrp_ext_043_reversion_half_life_21d},
    "mrp_ext_044_ou_theta_126d": {"inputs": ["close"], "func": mrp_ext_044_ou_theta_126d},
    "mrp_ext_045_reversion_speed_proxy_126d": {"inputs": ["close"], "func": mrp_ext_045_reversion_speed_proxy_126d},
    "mrp_ext_046_mean_reversion_strength_126d": {"inputs": ["close"], "func": mrp_ext_046_mean_reversion_strength_126d},
    "mrp_ext_047_half_life_normalized_126d": {"inputs": ["close"], "func": mrp_ext_047_half_life_normalized_126d},
    "mrp_ext_048_return_autocorr_negative_flag_252d": {"inputs": ["close"], "func": mrp_ext_048_return_autocorr_negative_flag_252d},
    "mrp_ext_049_ar1_returns_change_63d": {"inputs": ["close"], "func": mrp_ext_049_ar1_returns_change_63d},
    "mrp_ext_050_half_life_pctile_252d": {"inputs": ["close"], "func": mrp_ext_050_half_life_pctile_252d},
    "mrp_ext_051_range_compression_21d": {"inputs": ["close", "high", "low"], "func": mrp_ext_051_range_compression_21d},
    "mrp_ext_052_range_compression_63d": {"inputs": ["close", "high", "low"], "func": mrp_ext_052_range_compression_63d},
    "mrp_ext_053_realized_vol_compression": {"inputs": ["close"], "func": mrp_ext_053_realized_vol_compression},
    "mrp_ext_054_close_range_width_63d": {"inputs": ["close"], "func": mrp_ext_054_close_range_width_63d},
    "mrp_ext_055_daily_range_vs_mean": {"inputs": ["close", "high", "low"], "func": mrp_ext_055_daily_range_vs_mean},
    "mrp_ext_056_overshoot_below_band_streak_63d": {"inputs": ["close"], "func": mrp_ext_056_overshoot_below_band_streak_63d},
    "mrp_ext_057_overshoot_below_band_streak_21d": {"inputs": ["close"], "func": mrp_ext_057_overshoot_below_band_streak_21d},
    "mrp_ext_058_deep_undershoot_streak": {"inputs": ["close"], "func": mrp_ext_058_deep_undershoot_streak},
    "mrp_ext_059_below_mean_streak_252d": {"inputs": ["close"], "func": mrp_ext_059_below_mean_streak_252d},
    "mrp_ext_060_overshoot_streak_max_252d": {"inputs": ["close"], "func": mrp_ext_060_overshoot_streak_max_252d},
    "mrp_ext_061_time_below_band_126d": {"inputs": ["close"], "func": mrp_ext_061_time_below_band_126d},
    "mrp_ext_062_consolidation_at_low_flag": {"inputs": ["close"], "func": mrp_ext_062_consolidation_at_low_flag},
    "mrp_ext_063_stretch_pctile_63d": {"inputs": ["close"], "func": mrp_ext_063_stretch_pctile_63d},
    "mrp_ext_064_stretch_pctile_504d": {"inputs": ["close"], "func": mrp_ext_064_stretch_pctile_504d},
    "mrp_ext_065_stretch_zscore_63d": {"inputs": ["close"], "func": mrp_ext_065_stretch_zscore_63d},
    "mrp_ext_066_stretch_zscore_126d": {"inputs": ["close"], "func": mrp_ext_066_stretch_zscore_126d},
    "mrp_ext_067_overshoot_pctile_252d": {"inputs": ["close"], "func": mrp_ext_067_overshoot_pctile_252d},
    "mrp_ext_068_gap_to_mean_pctile_252d": {"inputs": ["close"], "func": mrp_ext_068_gap_to_mean_pctile_252d},
    "mrp_ext_069_dev_from_median_zscore_252d": {"inputs": ["close"], "func": mrp_ext_069_dev_from_median_zscore_252d},
    "mrp_ext_070_stretch_min_pctile_252d": {"inputs": ["close"], "func": mrp_ext_070_stretch_min_pctile_252d},
    "mrp_ext_071_gap_x_reversion_speed_126d": {"inputs": ["close"], "func": mrp_ext_071_gap_x_reversion_speed_126d},
    "mrp_ext_072_overshoot_x_compression": {"inputs": ["close"], "func": mrp_ext_072_overshoot_x_compression},
    "mrp_ext_073_stretch_recovery_potential": {"inputs": ["close"], "func": mrp_ext_073_stretch_recovery_potential},
    "mrp_ext_074_multi_window_undershoot_score": {"inputs": ["close"], "func": mrp_ext_074_multi_window_undershoot_score},
    "mrp_ext_075_mean_reversion_potential_index_ext": {"inputs": ["close"], "func": mrp_ext_075_mean_reversion_potential_index_ext},
}
