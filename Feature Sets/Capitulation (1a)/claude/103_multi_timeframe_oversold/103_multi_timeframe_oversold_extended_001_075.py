"""
103_multi_timeframe_oversold — Extended Features 001-075
Domain: multi-horizon oversold confluence — additional angles not in the four
        base files: alternate horizon sets (3/42/189/378), ROC / momentum
        confluence, CCI and MFI oscillator families across horizons, range and
        volume oversold breadth, oversold streaks and persistence, cross-family
        z-scores and percentile ranks, and fresh composite indices.
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


def _rsi(close: pd.Series, w: int) -> pd.Series:
    """Wilder-style RSI over window w (0-100; <30 oversold)."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    ad = down.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    rs = _safe_div(au, ad)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def _stoch_k(close: pd.Series, w: int) -> pd.Series:
    """Stochastic %K over window w using the close series (0-100)."""
    lo = _rolling_min(close, w)
    hi = _rolling_max(close, w)
    return 100.0 * _safe_div(close - lo, hi - lo)


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    """Drawdown of close from its trailing w-day high."""
    h = _rolling_max(close, w)
    return _safe_div(close - h, h)


def _roc(close: pd.Series, w: int) -> pd.Series:
    """Rate of change (percent return) over window w."""
    return close.pct_change(w)


def _cci(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Commodity Channel Index over window w using the typical price."""
    tp = (high + low + close) / 3.0
    ma = _rolling_mean(tp, w)
    md = (tp - ma).abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return _safe_div(tp - ma, 0.015 * md)


def _mfi(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Money Flow Index over window w (0-100; <20 oversold)."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff(1)
    pos = rmf.where(delta > 0, 0.0)
    neg = rmf.where(delta < 0, 0.0)
    pos_sum = _rolling_sum(pos, w)
    neg_sum = _rolling_sum(neg, w)
    mr = _safe_div(pos_sum, neg_sum)
    return 100.0 - _safe_div(100.0, 1.0 + mr)


# Alternate horizon sets used for confluence counting (distinct from base file).
_RSI_TF_ALT = (3, 9, 42, 126)
_MA_TF_ALT = (5, 30, 75, 150, 252)
_DD_TF_ALT = (10, 42, 189, 378, 756)
_ROC_TF = (_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_OSC_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): RSI on alternate horizon set + confluence ---

def mto_ext_001_rsi_3d(close: pd.Series) -> pd.Series:
    """3-day RSI (ultra-fast oversold reading)."""
    return _rsi(close, 3)


def mto_ext_002_rsi_9d(close: pd.Series) -> pd.Series:
    """9-day RSI (between weekly and standard horizon)."""
    return _rsi(close, 9)


def mto_ext_003_rsi_42d(close: pd.Series) -> pd.Series:
    """42-day RSI (two-month horizon oversold reading)."""
    return _rsi(close, 42)


def mto_ext_004_rsi_126d(close: pd.Series) -> pd.Series:
    """126-day RSI (semi-annual horizon oversold reading)."""
    return _rsi(close, _TD_HALF)


def mto_ext_005_rsi_min_alt_tf(close: pd.Series) -> pd.Series:
    """Minimum RSI across the 3/9/42/126-day alternate horizons."""
    rsis = pd.concat([_rsi(close, w) for w in _RSI_TF_ALT], axis=1)
    return rsis.min(axis=1)


def mto_ext_006_rsi_oversold_count_alt_tf(close: pd.Series) -> pd.Series:
    """Count of alternate-horizon RSIs reading below 30."""
    return sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)


def mto_ext_007_rsi_deep_oversold_count_alt_tf(close: pd.Series) -> pd.Series:
    """Count of alternate-horizon RSIs reading below 25."""
    return sum((_rsi(close, w) < 25).astype(float) for w in _RSI_TF_ALT)


def mto_ext_008_rsi_oversold_fraction_alt_tf(close: pd.Series) -> pd.Series:
    """Fraction of alternate-horizon RSIs reading below 30."""
    return sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT) / len(_RSI_TF_ALT)


def mto_ext_009_rsi_range_alt_tf(close: pd.Series) -> pd.Series:
    """Max minus min RSI across the alternate horizons (cross-horizon range)."""
    rsis = pd.concat([_rsi(close, w) for w in _RSI_TF_ALT], axis=1)
    return rsis.max(axis=1) - rsis.min(axis=1)


def mto_ext_010_rsi_spread_3d_126d(close: pd.Series) -> pd.Series:
    """3-day RSI minus 126-day RSI (ultra-fast vs semi-annual spread)."""
    return _rsi(close, 3) - _rsi(close, _TD_HALF)


def mto_ext_011_rsi_all_oversold_flag_alt_tf(close: pd.Series) -> pd.Series:
    """Flag: every alternate-horizon RSI is simultaneously below 30."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    return (cnt == len(_RSI_TF_ALT)).astype(float)


def mto_ext_012_rsi_depth_alt_tf(close: pd.Series) -> pd.Series:
    """Mean depth below 30 across the alternate-horizon RSIs."""
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF_ALT)
    return depth / len(_RSI_TF_ALT)


# --- Group B (013-024): Rate-of-change / momentum confluence ---

def mto_ext_013_roc_5d(close: pd.Series) -> pd.Series:
    """5-day rate of change (weekly momentum)."""
    return _roc(close, _TD_WEEK)


def mto_ext_014_roc_21d(close: pd.Series) -> pd.Series:
    """21-day rate of change (monthly momentum)."""
    return _roc(close, _TD_MON)


def mto_ext_015_roc_63d(close: pd.Series) -> pd.Series:
    """63-day rate of change (quarterly momentum)."""
    return _roc(close, _TD_QTR)


def mto_ext_016_roc_252d(close: pd.Series) -> pd.Series:
    """252-day rate of change (annual momentum)."""
    return _roc(close, _TD_YEAR)


def mto_ext_017_roc_min_across_tf(close: pd.Series) -> pd.Series:
    """Most negative rate of change across the 5/21/63/126/252-day horizons."""
    rocs = pd.concat([_roc(close, w) for w in _ROC_TF], axis=1)
    return rocs.min(axis=1)


def mto_ext_018_roc_mean_across_tf(close: pd.Series) -> pd.Series:
    """Mean rate of change across the 5/21/63/126/252-day horizons."""
    rocs = pd.concat([_roc(close, w) for w in _ROC_TF], axis=1)
    return rocs.mean(axis=1)


def mto_ext_019_roc_negative_count(close: pd.Series) -> pd.Series:
    """Count of rate-of-change horizons reading negative."""
    return sum((_roc(close, w) < 0).astype(float) for w in _ROC_TF)


def mto_ext_020_roc_severe_count(close: pd.Series) -> pd.Series:
    """Count of rate-of-change horizons worse than -25%."""
    return sum((_roc(close, w) < -0.25).astype(float) for w in _ROC_TF)


def mto_ext_021_roc_all_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: rate of change is negative on every one of the 5 horizons."""
    cnt = sum((_roc(close, w) < 0).astype(float) for w in _ROC_TF)
    return (cnt == len(_ROC_TF)).astype(float)


def mto_ext_022_roc_dispersion(close: pd.Series) -> pd.Series:
    """Cross-horizon standard deviation of the rate-of-change readings."""
    rocs = pd.concat([_roc(close, w) for w in _ROC_TF], axis=1)
    return rocs.std(axis=1)


def mto_ext_023_roc_acceleration_confluence(close: pd.Series) -> pd.Series:
    """Count of horizons where short ROC is below long ROC (decelerating)."""
    short = _roc(close, _TD_MON)
    return sum((short < _roc(close, w)).astype(float) for w in (_TD_QTR, _TD_HALF, _TD_YEAR))


def mto_ext_024_roc_severity_rank_mean(close: pd.Series) -> pd.Series:
    """Mean percentile rank of each horizon's ROC within 252 days."""
    ranks = [_rolling_rank_pct(_roc(close, w), _TD_YEAR) for w in _ROC_TF]
    return pd.concat(ranks, axis=1).mean(axis=1)


# --- Group C (025-036): CCI and MFI oscillator families across horizons ---

def mto_ext_025_cci_20d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Commodity Channel Index over the 20-day horizon."""
    return _cci(close, high, low, 20)


def mto_ext_026_cci_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Commodity Channel Index over the 63-day horizon."""
    return _cci(close, high, low, _TD_QTR)


def mto_ext_027_cci_min_across_tf(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative CCI across the 21/63/126/252-day horizons."""
    ccis = pd.concat([_cci(close, high, low, w) for w in _OSC_TF], axis=1)
    return ccis.min(axis=1)


def mto_ext_028_cci_oversold_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of CCI horizons reading below -100 (oversold)."""
    return sum((_cci(close, high, low, w) < -100).astype(float) for w in _OSC_TF)


def mto_ext_029_cci_deep_oversold_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of CCI horizons reading below -200 (deeply oversold)."""
    return sum((_cci(close, high, low, w) < -200).astype(float) for w in _OSC_TF)


def mto_ext_030_cci_mean_across_tf(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean CCI across the 21/63/126/252-day horizons."""
    ccis = pd.concat([_cci(close, high, low, w) for w in _OSC_TF], axis=1)
    return ccis.mean(axis=1)


def mto_ext_031_mfi_14d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index over the 14-day horizon."""
    return _mfi(close, high, low, volume, 14)


def mto_ext_032_mfi_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index over the 63-day horizon."""
    return _mfi(close, high, low, volume, _TD_QTR)


def mto_ext_033_mfi_min_across_tf(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Minimum Money Flow Index across the 21/63/126/252-day horizons."""
    mfis = pd.concat([_mfi(close, high, low, volume, w) for w in _OSC_TF], axis=1)
    return mfis.min(axis=1)


def mto_ext_034_mfi_oversold_count(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Money Flow Index horizons reading below 20 (oversold)."""
    return sum((_mfi(close, high, low, volume, w) < 20).astype(float) for w in _OSC_TF)


def mto_ext_035_mfi_deep_oversold_count(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Money Flow Index horizons reading below 10 (deeply oversold)."""
    return sum((_mfi(close, high, low, volume, w) < 10).astype(float) for w in _OSC_TF)


def mto_ext_036_mfi_mean_across_tf(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean Money Flow Index across the 21/63/126/252-day horizons."""
    mfis = pd.concat([_mfi(close, high, low, volume, w) for w in _OSC_TF], axis=1)
    return mfis.mean(axis=1)


# --- Group D (037-050): Drawdown / MA on alternate horizons + range breadth ---

def mto_ext_037_dd_10d(close: pd.Series) -> pd.Series:
    """Drawdown from the 10-day high (fast-horizon drawdown)."""
    return _drawdown(close, 10)


def mto_ext_038_dd_42d(close: pd.Series) -> pd.Series:
    """Drawdown from the 42-day high (two-month drawdown)."""
    return _drawdown(close, 42)


def mto_ext_039_dd_189d(close: pd.Series) -> pd.Series:
    """Drawdown from the 189-day high (nine-month drawdown)."""
    return _drawdown(close, 189)


def mto_ext_040_dd_756d(close: pd.Series) -> pd.Series:
    """Drawdown from the 756-day high (three-year drawdown)."""
    return _drawdown(close, 756)


def mto_ext_041_dd_min_alt_tf(close: pd.Series) -> pd.Series:
    """Deepest drawdown across the 10/42/189/378/756-day alternate horizons."""
    dds = pd.concat([_drawdown(close, w) for w in _DD_TF_ALT], axis=1)
    return dds.min(axis=1)


def mto_ext_042_dd_severe_count_alt_tf(close: pd.Series) -> pd.Series:
    """Count of alternate-horizon drawdowns worse than -30%."""
    return sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_TF_ALT)


def mto_ext_043_below_ma_count_alt_tf(close: pd.Series) -> pd.Series:
    """Count of alternate moving averages (5/30/75/150/252) the close sits below."""
    return sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF_ALT)


def mto_ext_044_below_all_ma_flag_alt_tf(close: pd.Series) -> pd.Series:
    """Flag: close is below every one of the 5 alternate moving averages."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF_ALT)
    return (cnt == len(_MA_TF_ALT)).astype(float)


def mto_ext_045_mean_ma_deviation_alt_tf(close: pd.Series) -> pd.Series:
    """Mean percent deviation of close from the 5 alternate moving averages."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF_ALT]
    return pd.concat(devs, axis=1).mean(axis=1)


def mto_ext_046_min_ma_deviation_alt_tf(close: pd.Series) -> pd.Series:
    """Most negative percent deviation of close across the 5 alternate MAs."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF_ALT]
    return pd.concat(devs, axis=1).min(axis=1)


def mto_ext_047_range_position_min_across_tf(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lowest close position within the high-low range across 21/63/126/252-day horizons."""
    parts = []
    for w in _OSC_TF:
        lo = _rolling_min(low, w)
        hi = _rolling_max(high, w)
        parts.append(_safe_div(close - lo, hi - lo))
    return pd.concat(parts, axis=1).min(axis=1)


def mto_ext_048_at_period_low_count(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of horizons on which today's low is at/below the trailing range low."""
    return sum((low <= _rolling_min(low, w)).astype(float) for w in _DD_TF_ALT)


def mto_ext_049_dd_pctile_min_alt_tf(close: pd.Series) -> pd.Series:
    """Lowest percentile rank of alternate-horizon drawdowns within 252 days."""
    ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_TF_ALT]
    return pd.concat(ranks, axis=1).min(axis=1)


def mto_ext_050_dd_mean_alt_tf(close: pd.Series) -> pd.Series:
    """Mean drawdown across the 10/42/189/378/756-day alternate horizons."""
    dds = pd.concat([_drawdown(close, w) for w in _DD_TF_ALT], axis=1)
    return dds.mean(axis=1)


# --- Group E (051-062): Volume / oversold streaks & persistence ---

def mto_ext_051_volume_pctile_min_across_tf(volume: pd.Series) -> pd.Series:
    """Lowest volume percentile rank across the 21/63/126/252-day horizons (dry-up)."""
    ranks = pd.concat([_rolling_rank_pct(volume, w) for w in _OSC_TF], axis=1)
    return ranks.min(axis=1)


def mto_ext_052_down_volume_share_min_across_tf(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max down-day volume share across the 21/63/126-day horizons (selling breadth)."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    parts = [_safe_div(_rolling_sum(dv, w), _rolling_sum(volume, w)) for w in (_TD_MON, _TD_QTR, _TD_HALF)]
    return pd.concat(parts, axis=1).max(axis=1)


def mto_ext_053_rsi14_oversold_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 14-day RSI below 30."""
    return _consec_streak(_rsi(close, 14) < 30)


def mto_ext_054_rsi21_oversold_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 21-day RSI below 30."""
    return _consec_streak(_rsi(close, _TD_MON) < 30)


def mto_ext_055_stoch_oversold_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 14-day stochastic %K below 20."""
    return _consec_streak(_stoch_k(close, 14) < 20)


def mto_ext_056_multi_tf_oversold_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of at least 3 alternate-horizon RSIs below 30."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    return _consec_streak(cnt >= 3)


def mto_ext_057_oversold_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of the last 63 days the 14-day RSI was below 30."""
    return _rolling_mean((_rsi(close, 14) < 30).astype(float), _TD_QTR)


def mto_ext_058_deep_oversold_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of the last 63 days the 14-day RSI was below 20."""
    return _rolling_mean((_rsi(close, 14) < 20).astype(float), _TD_QTR)


def mto_ext_059_below_all_ma_persistence_126d(close: pd.Series) -> pd.Series:
    """Fraction of the last 126 days the close sat below all 5 alternate MAs."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF_ALT)
    return _rolling_mean((cnt == len(_MA_TF_ALT)).astype(float), _TD_HALF)


def mto_ext_060_new_low_persistence_126d(close: pd.Series) -> pd.Series:
    """Fraction of the last 126 days the close was at a new 252-day low."""
    new_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return _rolling_mean(new_low, _TD_HALF)


def mto_ext_061_oversold_count_streak_max_63d(close: pd.Series) -> pd.Series:
    """Maximum 14-day-RSI oversold streak observed over the trailing 63 days."""
    streak = _consec_streak(_rsi(close, 14) < 30)
    return _rolling_max(streak, _TD_QTR)


def mto_ext_062_stoch_bottom_decile_persistence(close: pd.Series) -> pd.Series:
    """Fraction of the last 63 days the 63-day stochastic %K was below 10."""
    return _rolling_mean((_stoch_k(close, _TD_QTR) < 10).astype(float), _TD_QTR)


# --- Group F (063-070): Cross-family z-scores and percentile ranks ---

def mto_ext_063_oversold_count_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the alternate-horizon RSI oversold count within 252 days."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    return _rolling_rank_pct(cnt, _TD_YEAR)


def mto_ext_064_dd_count_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the alternate-horizon severe-drawdown count over 252 days."""
    cnt = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_TF_ALT)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def mto_ext_065_roc_min_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the worst cross-horizon ROC over a trailing 252-day window."""
    rmin = pd.concat([_roc(close, w) for w in _ROC_TF], axis=1).min(axis=1)
    return _safe_div(rmin - _rolling_mean(rmin, _TD_YEAR), _rolling_std(rmin, _TD_YEAR))


def mto_ext_066_rsi_mean_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the mean alternate-horizon RSI within 252 days."""
    rmean = pd.concat([_rsi(close, w) for w in _RSI_TF_ALT], axis=1).mean(axis=1)
    return _rolling_rank_pct(rmean, _TD_YEAR)


def mto_ext_067_cci_min_pctile_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of the worst cross-horizon CCI within 252 days."""
    cmin = pd.concat([_cci(close, high, low, w) for w in _OSC_TF], axis=1).min(axis=1)
    return _rolling_rank_pct(cmin, _TD_YEAR)


def mto_ext_068_below_ma_count_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the alternate below-MA count within 252 days."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF_ALT)
    return _rolling_rank_pct(cnt, _TD_YEAR)


def mto_ext_069_mfi_min_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of the worst cross-horizon MFI over a trailing 252-day window."""
    mmin = pd.concat([_mfi(close, high, low, volume, w) for w in _OSC_TF], axis=1).min(axis=1)
    return _safe_div(mmin - _rolling_mean(mmin, _TD_YEAR), _rolling_std(mmin, _TD_YEAR))


def mto_ext_070_dd_min_pctile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of the worst alternate-horizon drawdown within 504 days."""
    dmin = pd.concat([_drawdown(close, w) for w in _DD_TF_ALT], axis=1).min(axis=1)
    return _rolling_rank_pct(dmin, 504)


# --- Group G (071-075): Fresh composite oversold indices ---

def mto_ext_071_oscillator_oversold_master_count(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Total oversold signals across RSI, CCI, MFI and stochastic families."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    cci_c = sum((_cci(close, high, low, w) < -100).astype(float) for w in _OSC_TF)
    mfi_c = sum((_mfi(close, high, low, volume, w) < 20).astype(float) for w in _OSC_TF)
    stoch_c = sum((_stoch_k(close, w) < 20).astype(float) for w in _OSC_TF)
    return rsi_c + cci_c + mfi_c + stoch_c


def mto_ext_072_oscillator_oversold_breadth(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Oscillator oversold master count normalized by the indicator total."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    cci_c = sum((_cci(close, high, low, w) < -100).astype(float) for w in _OSC_TF)
    mfi_c = sum((_mfi(close, high, low, volume, w) < 20).astype(float) for w in _OSC_TF)
    stoch_c = sum((_stoch_k(close, w) < 20).astype(float) for w in _OSC_TF)
    total = len(_RSI_TF_ALT) + 3 * len(_OSC_TF)
    return (rsi_c + cci_c + mfi_c + stoch_c) / total


def mto_ext_073_momentum_drawdown_alignment(close: pd.Series) -> pd.Series:
    """Product of negative-ROC and severe-drawdown confluence fractions."""
    roc_f = sum((_roc(close, w) < 0).astype(float) for w in _ROC_TF) / len(_ROC_TF)
    dd_f = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_TF_ALT) / len(_DD_TF_ALT)
    return roc_f * dd_f


def mto_ext_074_deep_extremity_alt_tf(close: pd.Series) -> pd.Series:
    """Minimum percentile rank across alternate drawdown and ROC families."""
    dd_ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_TF_ALT]
    roc_ranks = [_rolling_rank_pct(_roc(close, w), _TD_YEAR) for w in _ROC_TF]
    return pd.concat(dd_ranks + roc_ranks, axis=1).min(axis=1)


def mto_ext_075_multi_timeframe_oversold_index_ext(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Master index: oscillator oversold breadth times mean RSI/MFI depth.
    Higher = broader and deeper multi-horizon oversold confluence."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF_ALT)
    cci_c = sum((_cci(close, high, low, w) < -100).astype(float) for w in _OSC_TF)
    mfi_c = sum((_mfi(close, high, low, volume, w) < 20).astype(float) for w in _OSC_TF)
    stoch_c = sum((_stoch_k(close, w) < 20).astype(float) for w in _OSC_TF)
    total = len(_RSI_TF_ALT) + 3 * len(_OSC_TF)
    breadth = (rsi_c + cci_c + mfi_c + stoch_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF_ALT) / (len(_RSI_TF_ALT) * 30.0)
    return breadth * (0.5 + depth)


# ── Registry ──────────────────────────────────────────────────────────────────

MULTI_TIMEFRAME_OVERSOLD_EXTENDED_REGISTRY_001_075 = {
    "mto_ext_001_rsi_3d": {"inputs": ["close"], "func": mto_ext_001_rsi_3d},
    "mto_ext_002_rsi_9d": {"inputs": ["close"], "func": mto_ext_002_rsi_9d},
    "mto_ext_003_rsi_42d": {"inputs": ["close"], "func": mto_ext_003_rsi_42d},
    "mto_ext_004_rsi_126d": {"inputs": ["close"], "func": mto_ext_004_rsi_126d},
    "mto_ext_005_rsi_min_alt_tf": {"inputs": ["close"], "func": mto_ext_005_rsi_min_alt_tf},
    "mto_ext_006_rsi_oversold_count_alt_tf": {"inputs": ["close"], "func": mto_ext_006_rsi_oversold_count_alt_tf},
    "mto_ext_007_rsi_deep_oversold_count_alt_tf": {"inputs": ["close"], "func": mto_ext_007_rsi_deep_oversold_count_alt_tf},
    "mto_ext_008_rsi_oversold_fraction_alt_tf": {"inputs": ["close"], "func": mto_ext_008_rsi_oversold_fraction_alt_tf},
    "mto_ext_009_rsi_range_alt_tf": {"inputs": ["close"], "func": mto_ext_009_rsi_range_alt_tf},
    "mto_ext_010_rsi_spread_3d_126d": {"inputs": ["close"], "func": mto_ext_010_rsi_spread_3d_126d},
    "mto_ext_011_rsi_all_oversold_flag_alt_tf": {"inputs": ["close"], "func": mto_ext_011_rsi_all_oversold_flag_alt_tf},
    "mto_ext_012_rsi_depth_alt_tf": {"inputs": ["close"], "func": mto_ext_012_rsi_depth_alt_tf},
    "mto_ext_013_roc_5d": {"inputs": ["close"], "func": mto_ext_013_roc_5d},
    "mto_ext_014_roc_21d": {"inputs": ["close"], "func": mto_ext_014_roc_21d},
    "mto_ext_015_roc_63d": {"inputs": ["close"], "func": mto_ext_015_roc_63d},
    "mto_ext_016_roc_252d": {"inputs": ["close"], "func": mto_ext_016_roc_252d},
    "mto_ext_017_roc_min_across_tf": {"inputs": ["close"], "func": mto_ext_017_roc_min_across_tf},
    "mto_ext_018_roc_mean_across_tf": {"inputs": ["close"], "func": mto_ext_018_roc_mean_across_tf},
    "mto_ext_019_roc_negative_count": {"inputs": ["close"], "func": mto_ext_019_roc_negative_count},
    "mto_ext_020_roc_severe_count": {"inputs": ["close"], "func": mto_ext_020_roc_severe_count},
    "mto_ext_021_roc_all_negative_flag": {"inputs": ["close"], "func": mto_ext_021_roc_all_negative_flag},
    "mto_ext_022_roc_dispersion": {"inputs": ["close"], "func": mto_ext_022_roc_dispersion},
    "mto_ext_023_roc_acceleration_confluence": {"inputs": ["close"], "func": mto_ext_023_roc_acceleration_confluence},
    "mto_ext_024_roc_severity_rank_mean": {"inputs": ["close"], "func": mto_ext_024_roc_severity_rank_mean},
    "mto_ext_025_cci_20d": {"inputs": ["close", "high", "low"], "func": mto_ext_025_cci_20d},
    "mto_ext_026_cci_63d": {"inputs": ["close", "high", "low"], "func": mto_ext_026_cci_63d},
    "mto_ext_027_cci_min_across_tf": {"inputs": ["close", "high", "low"], "func": mto_ext_027_cci_min_across_tf},
    "mto_ext_028_cci_oversold_count": {"inputs": ["close", "high", "low"], "func": mto_ext_028_cci_oversold_count},
    "mto_ext_029_cci_deep_oversold_count": {"inputs": ["close", "high", "low"], "func": mto_ext_029_cci_deep_oversold_count},
    "mto_ext_030_cci_mean_across_tf": {"inputs": ["close", "high", "low"], "func": mto_ext_030_cci_mean_across_tf},
    "mto_ext_031_mfi_14d": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_031_mfi_14d},
    "mto_ext_032_mfi_63d": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_032_mfi_63d},
    "mto_ext_033_mfi_min_across_tf": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_033_mfi_min_across_tf},
    "mto_ext_034_mfi_oversold_count": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_034_mfi_oversold_count},
    "mto_ext_035_mfi_deep_oversold_count": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_035_mfi_deep_oversold_count},
    "mto_ext_036_mfi_mean_across_tf": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_036_mfi_mean_across_tf},
    "mto_ext_037_dd_10d": {"inputs": ["close"], "func": mto_ext_037_dd_10d},
    "mto_ext_038_dd_42d": {"inputs": ["close"], "func": mto_ext_038_dd_42d},
    "mto_ext_039_dd_189d": {"inputs": ["close"], "func": mto_ext_039_dd_189d},
    "mto_ext_040_dd_756d": {"inputs": ["close"], "func": mto_ext_040_dd_756d},
    "mto_ext_041_dd_min_alt_tf": {"inputs": ["close"], "func": mto_ext_041_dd_min_alt_tf},
    "mto_ext_042_dd_severe_count_alt_tf": {"inputs": ["close"], "func": mto_ext_042_dd_severe_count_alt_tf},
    "mto_ext_043_below_ma_count_alt_tf": {"inputs": ["close"], "func": mto_ext_043_below_ma_count_alt_tf},
    "mto_ext_044_below_all_ma_flag_alt_tf": {"inputs": ["close"], "func": mto_ext_044_below_all_ma_flag_alt_tf},
    "mto_ext_045_mean_ma_deviation_alt_tf": {"inputs": ["close"], "func": mto_ext_045_mean_ma_deviation_alt_tf},
    "mto_ext_046_min_ma_deviation_alt_tf": {"inputs": ["close"], "func": mto_ext_046_min_ma_deviation_alt_tf},
    "mto_ext_047_range_position_min_across_tf": {"inputs": ["close", "high", "low"], "func": mto_ext_047_range_position_min_across_tf},
    "mto_ext_048_at_period_low_count": {"inputs": ["close", "low"], "func": mto_ext_048_at_period_low_count},
    "mto_ext_049_dd_pctile_min_alt_tf": {"inputs": ["close"], "func": mto_ext_049_dd_pctile_min_alt_tf},
    "mto_ext_050_dd_mean_alt_tf": {"inputs": ["close"], "func": mto_ext_050_dd_mean_alt_tf},
    "mto_ext_051_volume_pctile_min_across_tf": {"inputs": ["volume"], "func": mto_ext_051_volume_pctile_min_across_tf},
    "mto_ext_052_down_volume_share_min_across_tf": {"inputs": ["close", "volume"], "func": mto_ext_052_down_volume_share_min_across_tf},
    "mto_ext_053_rsi14_oversold_streak": {"inputs": ["close"], "func": mto_ext_053_rsi14_oversold_streak},
    "mto_ext_054_rsi21_oversold_streak": {"inputs": ["close"], "func": mto_ext_054_rsi21_oversold_streak},
    "mto_ext_055_stoch_oversold_streak": {"inputs": ["close"], "func": mto_ext_055_stoch_oversold_streak},
    "mto_ext_056_multi_tf_oversold_streak": {"inputs": ["close"], "func": mto_ext_056_multi_tf_oversold_streak},
    "mto_ext_057_oversold_persistence_63d": {"inputs": ["close"], "func": mto_ext_057_oversold_persistence_63d},
    "mto_ext_058_deep_oversold_persistence_63d": {"inputs": ["close"], "func": mto_ext_058_deep_oversold_persistence_63d},
    "mto_ext_059_below_all_ma_persistence_126d": {"inputs": ["close"], "func": mto_ext_059_below_all_ma_persistence_126d},
    "mto_ext_060_new_low_persistence_126d": {"inputs": ["close"], "func": mto_ext_060_new_low_persistence_126d},
    "mto_ext_061_oversold_count_streak_max_63d": {"inputs": ["close"], "func": mto_ext_061_oversold_count_streak_max_63d},
    "mto_ext_062_stoch_bottom_decile_persistence": {"inputs": ["close"], "func": mto_ext_062_stoch_bottom_decile_persistence},
    "mto_ext_063_oversold_count_pctile_252d": {"inputs": ["close"], "func": mto_ext_063_oversold_count_pctile_252d},
    "mto_ext_064_dd_count_zscore_252d": {"inputs": ["close"], "func": mto_ext_064_dd_count_zscore_252d},
    "mto_ext_065_roc_min_zscore_252d": {"inputs": ["close"], "func": mto_ext_065_roc_min_zscore_252d},
    "mto_ext_066_rsi_mean_pctile_252d": {"inputs": ["close"], "func": mto_ext_066_rsi_mean_pctile_252d},
    "mto_ext_067_cci_min_pctile_252d": {"inputs": ["close", "high", "low"], "func": mto_ext_067_cci_min_pctile_252d},
    "mto_ext_068_below_ma_count_pctile_252d": {"inputs": ["close"], "func": mto_ext_068_below_ma_count_pctile_252d},
    "mto_ext_069_mfi_min_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_069_mfi_min_zscore_252d},
    "mto_ext_070_dd_min_pctile_504d": {"inputs": ["close"], "func": mto_ext_070_dd_min_pctile_504d},
    "mto_ext_071_oscillator_oversold_master_count": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_071_oscillator_oversold_master_count},
    "mto_ext_072_oscillator_oversold_breadth": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_072_oscillator_oversold_breadth},
    "mto_ext_073_momentum_drawdown_alignment": {"inputs": ["close"], "func": mto_ext_073_momentum_drawdown_alignment},
    "mto_ext_074_deep_extremity_alt_tf": {"inputs": ["close"], "func": mto_ext_074_deep_extremity_alt_tf},
    "mto_ext_075_multi_timeframe_oversold_index_ext": {"inputs": ["close", "high", "low", "volume"], "func": mto_ext_075_multi_timeframe_oversold_index_ext},
}
