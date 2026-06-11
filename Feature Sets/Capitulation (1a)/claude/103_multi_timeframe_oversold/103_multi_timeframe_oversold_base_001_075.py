"""
103_multi_timeframe_oversold — Base Features 001-075
Domain: confluence of oversold / extreme readings measured SIMULTANEOUSLY
        across multiple lookback horizons (5/10/21/42/63/126/252/504 days).
        Captures the multi-timeframe alignment that marks a true capitulation
        low — every horizon oversold at once, not just one.
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


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


def _williams_r(close: pd.Series, w: int) -> pd.Series:
    """Williams %R over window w using the close series (-100 to 0)."""
    lo = _rolling_min(close, w)
    hi = _rolling_max(close, w)
    return -100.0 * _safe_div(hi - close, hi - lo)


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    """Drawdown of close from its trailing w-day high."""
    h = _rolling_max(close, w)
    return _safe_div(close - h, h)


def _price_zscore(close: pd.Series, w: int) -> pd.Series:
    """Z-score of close over a trailing w-day window."""
    return _safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))


# Standard horizon sets used for confluence counting.
_RSI_TF = (7, 14, 21, 63)
_MA_TF = (10, 21, 50, 100, 200)
_DD_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR, 504)
_PCTILE_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_MOM_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): RSI across horizons + confluence ---

def mto_001_rsi_5d(close: pd.Series) -> pd.Series:
    """5-day RSI (fast-horizon oversold reading)."""
    return _rsi(close, 5)


def mto_002_rsi_14d(close: pd.Series) -> pd.Series:
    """14-day RSI (standard oversold reading)."""
    return _rsi(close, 14)


def mto_003_rsi_21d(close: pd.Series) -> pd.Series:
    """21-day RSI (monthly-horizon oversold reading)."""
    return _rsi(close, _TD_MON)


def mto_004_rsi_63d(close: pd.Series) -> pd.Series:
    """63-day RSI (quarterly-horizon oversold reading)."""
    return _rsi(close, _TD_QTR)


def mto_005_rsi_min_across_tf(close: pd.Series) -> pd.Series:
    """Minimum RSI across the 7/14/21/63-day horizons (worst oversold)."""
    rsis = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1)
    return rsis.min(axis=1)


def mto_006_rsi_mean_across_tf(close: pd.Series) -> pd.Series:
    """Mean RSI across the 7/14/21/63-day horizons."""
    rsis = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1)
    return rsis.mean(axis=1)


def mto_007_rsi_oversold_count(close: pd.Series) -> pd.Series:
    """Count of RSI horizons reading below 30 (oversold confluence)."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return cnt


def mto_008_rsi_deeply_oversold_count(close: pd.Series) -> pd.Series:
    """Count of RSI horizons reading below 20 (deep-oversold confluence)."""
    cnt = sum((_rsi(close, w) < 20).astype(float) for w in _RSI_TF)
    return cnt


def mto_009_rsi_oversold_fraction(close: pd.Series) -> pd.Series:
    """Fraction of RSI horizons reading below 30."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return cnt / len(_RSI_TF)


def mto_010_rsi_spread_fast_slow(close: pd.Series) -> pd.Series:
    """14-day RSI minus 63-day RSI (fast-vs-slow oversold spread)."""
    return _rsi(close, 14) - _rsi(close, _TD_QTR)


def mto_011_rsi_all_oversold_flag(close: pd.Series) -> pd.Series:
    """Flag: every RSI horizon is simultaneously below 30."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return (cnt == len(_RSI_TF)).astype(float)


def mto_012_rsi_dispersion(close: pd.Series) -> pd.Series:
    """Cross-horizon standard deviation of RSI readings."""
    rsis = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1)
    return rsis.std(axis=1)


def mto_013_rsi_63d_oversold_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 63-day RSI below 35."""
    f = (_rsi(close, _TD_QTR) < 35).astype(float)
    return f.groupby((f == 0).cumsum()).cumsum()


def mto_014_rsi_composite_extremity(close: pd.Series) -> pd.Series:
    """Mean of (30 - RSI) clipped at 0 across horizons (oversold depth)."""
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF)
    return depth / len(_RSI_TF)


def mto_015_rsi_weighted_oversold(close: pd.Series) -> pd.Series:
    """Horizon-weighted oversold score (longer horizons weighted more)."""
    weights = {7: 1.0, 14: 1.5, 21: 2.0, 63: 3.0}
    tot = sum(weights.values())
    score = sum(weights[w] * (_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return score / tot


# --- Group B (016-030): Price vs moving averages across horizons ---

def mto_016_close_vs_sma10(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 10-day SMA."""
    ma = _rolling_mean(close, 10)
    return _safe_div(close - ma, ma)


def mto_017_close_vs_sma21(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 21-day SMA."""
    ma = _rolling_mean(close, _TD_MON)
    return _safe_div(close - ma, ma)


def mto_018_close_vs_sma50(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 50-day SMA."""
    ma = _rolling_mean(close, 50)
    return _safe_div(close - ma, ma)


def mto_019_close_vs_sma100(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 100-day SMA."""
    ma = _rolling_mean(close, 100)
    return _safe_div(close - ma, ma)


def mto_020_close_vs_sma200(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 200-day SMA."""
    ma = _rolling_mean(close, 200)
    return _safe_div(close - ma, ma)


def mto_021_below_ma_count(close: pd.Series) -> pd.Series:
    """Count of moving averages (10/21/50/100/200) the close sits below."""
    return sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)


def mto_022_below_all_ma_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below every one of the 5 moving averages."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return (cnt == len(_MA_TF)).astype(float)


def mto_023_mean_ma_deviation(close: pd.Series) -> pd.Series:
    """Mean percent deviation of close from the 5 moving averages."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF]
    return pd.concat(devs, axis=1).mean(axis=1)


def mto_024_min_ma_deviation(close: pd.Series) -> pd.Series:
    """Most negative percent deviation of close across the 5 moving averages."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF]
    return pd.concat(devs, axis=1).min(axis=1)


def mto_025_ma_deviation_dispersion(close: pd.Series) -> pd.Series:
    """Cross-horizon std of the close-vs-MA deviations."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF]
    return pd.concat(devs, axis=1).std(axis=1)


def mto_026_ma_cascade_alignment(close: pd.Series) -> pd.Series:
    """Fraction of the 5 moving averages the close sits below (0-1)."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return cnt / len(_MA_TF)


def mto_027_ma_confluence_score(close: pd.Series) -> pd.Series:
    """Mean negative MA deviation across horizons that are below price."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF]
    stacked = pd.concat(devs, axis=1)
    return stacked.clip(upper=0).mean(axis=1)


def mto_028_days_below_sma200(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of close below its 200-day SMA."""
    f = (close < _rolling_mean(close, 200)).astype(float)
    return f.groupby((f == 0).cumsum()).cumsum()


def mto_029_below_ma_count_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the below-MA count over a trailing 252-day window."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def mto_030_ma_stretch_worst(close: pd.Series) -> pd.Series:
    """Worst (most negative) close-vs-MA deviation in ATR-free percent terms."""
    devs = [_safe_div(close - _rolling_mean(close, w), _rolling_mean(close, w)) for w in _MA_TF]
    return pd.concat(devs, axis=1).min(axis=1).clip(upper=0)


# --- Group C (031-045): Drawdown across horizons confluence ---

def mto_031_dd_21d(close: pd.Series) -> pd.Series:
    """Drawdown from the 21-day high."""
    return _drawdown(close, _TD_MON)


def mto_032_dd_63d(close: pd.Series) -> pd.Series:
    """Drawdown from the 63-day high."""
    return _drawdown(close, _TD_QTR)


def mto_033_dd_126d(close: pd.Series) -> pd.Series:
    """Drawdown from the 126-day high."""
    return _drawdown(close, _TD_HALF)


def mto_034_dd_252d(close: pd.Series) -> pd.Series:
    """Drawdown from the 252-day high."""
    return _drawdown(close, _TD_YEAR)


def mto_035_dd_504d(close: pd.Series) -> pd.Series:
    """Drawdown from the 504-day high."""
    return _drawdown(close, 504)


def mto_036_dd_min_across_tf(close: pd.Series) -> pd.Series:
    """Deepest drawdown across the 21/63/126/252/504-day horizons."""
    dds = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1)
    return dds.min(axis=1)


def mto_037_dd_mean_across_tf(close: pd.Series) -> pd.Series:
    """Mean drawdown across the 21/63/126/252/504-day horizons."""
    dds = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1)
    return dds.mean(axis=1)


def mto_038_dd_extreme_count(close: pd.Series) -> pd.Series:
    """Count of horizons with drawdown worse than -20%."""
    return sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)


def mto_039_dd_all_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: drawdown is negative on every one of the 5 horizons."""
    cnt = sum((_drawdown(close, w) < 0).astype(float) for w in _DD_TF)
    return (cnt == len(_DD_TF)).astype(float)


def mto_040_dd_confluence_score(close: pd.Series) -> pd.Series:
    """Fraction of horizons with drawdown worse than -20%."""
    return sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF) / len(_DD_TF)


def mto_041_dd_dispersion(close: pd.Series) -> pd.Series:
    """Cross-horizon standard deviation of the drawdown readings."""
    dds = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1)
    return dds.std(axis=1)


def mto_042_multi_horizon_new_low_count(close: pd.Series) -> pd.Series:
    """Count of horizons on which the close is at a new trailing low."""
    return sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_TF)


def mto_043_new_low_confluence(close: pd.Series) -> pd.Series:
    """Fraction of horizons on which the close is at a new trailing low."""
    return sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_TF) / len(_DD_TF)


def mto_044_dd_severity_rank_mean(close: pd.Series) -> pd.Series:
    """Mean percentile rank of each horizon's drawdown within 252 days."""
    ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_TF]
    return pd.concat(ranks, axis=1).mean(axis=1)


def mto_045_dd_pctile_min_across_tf(close: pd.Series) -> pd.Series:
    """Lowest percentile rank of drawdown across the 5 horizons."""
    ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_TF]
    return pd.concat(ranks, axis=1).min(axis=1)


# --- Group D (046-060): Oscillator / channel position across horizons ---

def mto_046_stoch_k_14d(close: pd.Series) -> pd.Series:
    """Stochastic %K over the 14-day horizon."""
    return _stoch_k(close, 14)


def mto_047_stoch_k_63d(close: pd.Series) -> pd.Series:
    """Stochastic %K over the 63-day horizon."""
    return _stoch_k(close, _TD_QTR)


def mto_048_stoch_k_min_across_tf(close: pd.Series) -> pd.Series:
    """Minimum stochastic %K across the 14/21/63/126-day horizons."""
    ks = pd.concat([_stoch_k(close, w) for w in (14, _TD_MON, _TD_QTR, _TD_HALF)], axis=1)
    return ks.min(axis=1)


def mto_049_stoch_oversold_count(close: pd.Series) -> pd.Series:
    """Count of stochastic %K horizons reading below 20."""
    return sum((_stoch_k(close, w) < 20).astype(float)
               for w in (14, _TD_MON, _TD_QTR, _TD_HALF))


def mto_050_williams_r_14d(close: pd.Series) -> pd.Series:
    """Williams %R over the 14-day horizon."""
    return _williams_r(close, 14)


def mto_051_williams_r_63d(close: pd.Series) -> pd.Series:
    """Williams %R over the 63-day horizon."""
    return _williams_r(close, _TD_QTR)


def mto_052_williams_oversold_count(close: pd.Series) -> pd.Series:
    """Count of Williams %R horizons reading below -80 (oversold)."""
    return sum((_williams_r(close, w) < -80).astype(float)
               for w in (14, _TD_MON, _TD_QTR, _TD_HALF))


def mto_053_price_pctile_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of the close within its trailing 21-day range."""
    return _rolling_rank_pct(close, _TD_MON)


def mto_054_price_pctile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of the close within its trailing 63-day range."""
    return _rolling_rank_pct(close, _TD_QTR)


def mto_055_price_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the close within its trailing 252-day range."""
    return _rolling_rank_pct(close, _TD_YEAR)


def mto_056_price_pctile_min_across_tf(close: pd.Series) -> pd.Series:
    """Lowest close percentile rank across the 21/63/126/252-day horizons."""
    ranks = pd.concat([_rolling_rank_pct(close, w) for w in _PCTILE_TF], axis=1)
    return ranks.min(axis=1)


def mto_057_price_pctile_mean_across_tf(close: pd.Series) -> pd.Series:
    """Mean close percentile rank across the 21/63/126/252-day horizons."""
    ranks = pd.concat([_rolling_rank_pct(close, w) for w in _PCTILE_TF], axis=1)
    return ranks.mean(axis=1)


def mto_058_pctile_oversold_count(close: pd.Series) -> pd.Series:
    """Count of horizons where the close percentile rank is below 0.10."""
    return sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)


def mto_059_channel_position_confluence(close: pd.Series) -> pd.Series:
    """Mean stochastic %K across horizons (0 = at multi-horizon low)."""
    ks = pd.concat([_stoch_k(close, w) for w in (14, _TD_MON, _TD_QTR, _TD_HALF)], axis=1)
    return ks.mean(axis=1)


def mto_060_bottom_decile_count(close: pd.Series) -> pd.Series:
    """Count of horizons where stochastic %K is in the bottom decile (<10)."""
    return sum((_stoch_k(close, w) < 10).astype(float)
               for w in (14, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR))


# --- Group E (061-075): Z-score / momentum confluence & master composites ---

def mto_061_ret_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of daily return over a trailing 21-day window."""
    ret = _daily_ret(close)
    return _safe_div(ret - _rolling_mean(ret, _TD_MON), _rolling_std(ret, _TD_MON))


def mto_062_ret_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of daily return over a trailing 63-day window."""
    ret = _daily_ret(close)
    return _safe_div(ret - _rolling_mean(ret, _TD_QTR), _rolling_std(ret, _TD_QTR))


def mto_063_ret_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of daily return over a trailing 252-day window."""
    ret = _daily_ret(close)
    return _safe_div(ret - _rolling_mean(ret, _TD_YEAR), _rolling_std(ret, _TD_YEAR))


def mto_064_zscore_extreme_count(close: pd.Series) -> pd.Series:
    """Count of price z-score horizons reading below -1.5."""
    return sum((_price_zscore(close, w) < -1.5).astype(float) for w in _PCTILE_TF)


def mto_065_price_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of the close over a trailing 21-day window."""
    return _price_zscore(close, _TD_MON)


def mto_066_price_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of the close over a trailing 63-day window."""
    return _price_zscore(close, _TD_QTR)


def mto_067_price_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the close over a trailing 252-day window."""
    return _price_zscore(close, _TD_YEAR)


def mto_068_price_zscore_min_across_tf(close: pd.Series) -> pd.Series:
    """Most negative close z-score across the 21/63/126/252-day horizons."""
    zs = pd.concat([_price_zscore(close, w) for w in _PCTILE_TF], axis=1)
    return zs.min(axis=1)


def mto_069_momentum_oversold_count(close: pd.Series) -> pd.Series:
    """Count of trailing-return horizons worse than -15%."""
    return sum((close.pct_change(w) < -0.15).astype(float) for w in _MOM_TF)


def mto_070_negative_momentum_confluence(close: pd.Series) -> pd.Series:
    """Fraction of trailing-return horizons that are negative."""
    return sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / len(_MOM_TF)


def mto_071_multi_tf_oversold_master_count(close: pd.Series) -> pd.Series:
    """Total oversold signals across RSI, MA, drawdown and percentile families."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    return rsi_c + ma_c + dd_c + pc_c


def mto_072_oversold_breadth_index(close: pd.Series) -> pd.Series:
    """Master oversold count normalized by the total number of indicators."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    return (rsi_c + ma_c + dd_c + pc_c) / total


def mto_073_oversold_alignment_score(close: pd.Series) -> pd.Series:
    """Product of RSI, MA and percentile oversold fractions (joint alignment)."""
    rsi_f = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF) / len(_RSI_TF)
    ma_f = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF) / len(_MA_TF)
    pc_f = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF) / len(_PCTILE_TF)
    return rsi_f * ma_f * pc_f


def mto_074_deepest_timeframe_extremity(close: pd.Series) -> pd.Series:
    """Minimum percentile rank across drawdown and price-percentile families."""
    dd_ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_TF]
    pc_ranks = [_rolling_rank_pct(close, w) for w in _PCTILE_TF]
    return pd.concat(dd_ranks + pc_ranks, axis=1).min(axis=1)


def mto_075_multi_timeframe_capitulation_index(close: pd.Series) -> pd.Series:
    """Master index: breadth of oversold signals times mean oversold depth."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    breadth = (rsi_c + ma_c + dd_c + pc_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF) / (len(_RSI_TF) * 30.0)
    return breadth * (0.5 + depth)


# ── Registry ──────────────────────────────────────────────────────────────────

MULTI_TIMEFRAME_OVERSOLD_REGISTRY_001_075 = {
    "mto_001_rsi_5d": {"inputs": ["close"], "func": mto_001_rsi_5d},
    "mto_002_rsi_14d": {"inputs": ["close"], "func": mto_002_rsi_14d},
    "mto_003_rsi_21d": {"inputs": ["close"], "func": mto_003_rsi_21d},
    "mto_004_rsi_63d": {"inputs": ["close"], "func": mto_004_rsi_63d},
    "mto_005_rsi_min_across_tf": {"inputs": ["close"], "func": mto_005_rsi_min_across_tf},
    "mto_006_rsi_mean_across_tf": {"inputs": ["close"], "func": mto_006_rsi_mean_across_tf},
    "mto_007_rsi_oversold_count": {"inputs": ["close"], "func": mto_007_rsi_oversold_count},
    "mto_008_rsi_deeply_oversold_count": {"inputs": ["close"], "func": mto_008_rsi_deeply_oversold_count},
    "mto_009_rsi_oversold_fraction": {"inputs": ["close"], "func": mto_009_rsi_oversold_fraction},
    "mto_010_rsi_spread_fast_slow": {"inputs": ["close"], "func": mto_010_rsi_spread_fast_slow},
    "mto_011_rsi_all_oversold_flag": {"inputs": ["close"], "func": mto_011_rsi_all_oversold_flag},
    "mto_012_rsi_dispersion": {"inputs": ["close"], "func": mto_012_rsi_dispersion},
    "mto_013_rsi_63d_oversold_streak": {"inputs": ["close"], "func": mto_013_rsi_63d_oversold_streak},
    "mto_014_rsi_composite_extremity": {"inputs": ["close"], "func": mto_014_rsi_composite_extremity},
    "mto_015_rsi_weighted_oversold": {"inputs": ["close"], "func": mto_015_rsi_weighted_oversold},
    "mto_016_close_vs_sma10": {"inputs": ["close"], "func": mto_016_close_vs_sma10},
    "mto_017_close_vs_sma21": {"inputs": ["close"], "func": mto_017_close_vs_sma21},
    "mto_018_close_vs_sma50": {"inputs": ["close"], "func": mto_018_close_vs_sma50},
    "mto_019_close_vs_sma100": {"inputs": ["close"], "func": mto_019_close_vs_sma100},
    "mto_020_close_vs_sma200": {"inputs": ["close"], "func": mto_020_close_vs_sma200},
    "mto_021_below_ma_count": {"inputs": ["close"], "func": mto_021_below_ma_count},
    "mto_022_below_all_ma_flag": {"inputs": ["close"], "func": mto_022_below_all_ma_flag},
    "mto_023_mean_ma_deviation": {"inputs": ["close"], "func": mto_023_mean_ma_deviation},
    "mto_024_min_ma_deviation": {"inputs": ["close"], "func": mto_024_min_ma_deviation},
    "mto_025_ma_deviation_dispersion": {"inputs": ["close"], "func": mto_025_ma_deviation_dispersion},
    "mto_026_ma_cascade_alignment": {"inputs": ["close"], "func": mto_026_ma_cascade_alignment},
    "mto_027_ma_confluence_score": {"inputs": ["close"], "func": mto_027_ma_confluence_score},
    "mto_028_days_below_sma200": {"inputs": ["close"], "func": mto_028_days_below_sma200},
    "mto_029_below_ma_count_zscore": {"inputs": ["close"], "func": mto_029_below_ma_count_zscore},
    "mto_030_ma_stretch_worst": {"inputs": ["close"], "func": mto_030_ma_stretch_worst},
    "mto_031_dd_21d": {"inputs": ["close"], "func": mto_031_dd_21d},
    "mto_032_dd_63d": {"inputs": ["close"], "func": mto_032_dd_63d},
    "mto_033_dd_126d": {"inputs": ["close"], "func": mto_033_dd_126d},
    "mto_034_dd_252d": {"inputs": ["close"], "func": mto_034_dd_252d},
    "mto_035_dd_504d": {"inputs": ["close"], "func": mto_035_dd_504d},
    "mto_036_dd_min_across_tf": {"inputs": ["close"], "func": mto_036_dd_min_across_tf},
    "mto_037_dd_mean_across_tf": {"inputs": ["close"], "func": mto_037_dd_mean_across_tf},
    "mto_038_dd_extreme_count": {"inputs": ["close"], "func": mto_038_dd_extreme_count},
    "mto_039_dd_all_negative_flag": {"inputs": ["close"], "func": mto_039_dd_all_negative_flag},
    "mto_040_dd_confluence_score": {"inputs": ["close"], "func": mto_040_dd_confluence_score},
    "mto_041_dd_dispersion": {"inputs": ["close"], "func": mto_041_dd_dispersion},
    "mto_042_multi_horizon_new_low_count": {"inputs": ["close"], "func": mto_042_multi_horizon_new_low_count},
    "mto_043_new_low_confluence": {"inputs": ["close"], "func": mto_043_new_low_confluence},
    "mto_044_dd_severity_rank_mean": {"inputs": ["close"], "func": mto_044_dd_severity_rank_mean},
    "mto_045_dd_pctile_min_across_tf": {"inputs": ["close"], "func": mto_045_dd_pctile_min_across_tf},
    "mto_046_stoch_k_14d": {"inputs": ["close"], "func": mto_046_stoch_k_14d},
    "mto_047_stoch_k_63d": {"inputs": ["close"], "func": mto_047_stoch_k_63d},
    "mto_048_stoch_k_min_across_tf": {"inputs": ["close"], "func": mto_048_stoch_k_min_across_tf},
    "mto_049_stoch_oversold_count": {"inputs": ["close"], "func": mto_049_stoch_oversold_count},
    "mto_050_williams_r_14d": {"inputs": ["close"], "func": mto_050_williams_r_14d},
    "mto_051_williams_r_63d": {"inputs": ["close"], "func": mto_051_williams_r_63d},
    "mto_052_williams_oversold_count": {"inputs": ["close"], "func": mto_052_williams_oversold_count},
    "mto_053_price_pctile_21d": {"inputs": ["close"], "func": mto_053_price_pctile_21d},
    "mto_054_price_pctile_63d": {"inputs": ["close"], "func": mto_054_price_pctile_63d},
    "mto_055_price_pctile_252d": {"inputs": ["close"], "func": mto_055_price_pctile_252d},
    "mto_056_price_pctile_min_across_tf": {"inputs": ["close"], "func": mto_056_price_pctile_min_across_tf},
    "mto_057_price_pctile_mean_across_tf": {"inputs": ["close"], "func": mto_057_price_pctile_mean_across_tf},
    "mto_058_pctile_oversold_count": {"inputs": ["close"], "func": mto_058_pctile_oversold_count},
    "mto_059_channel_position_confluence": {"inputs": ["close"], "func": mto_059_channel_position_confluence},
    "mto_060_bottom_decile_count": {"inputs": ["close"], "func": mto_060_bottom_decile_count},
    "mto_061_ret_zscore_21d": {"inputs": ["close"], "func": mto_061_ret_zscore_21d},
    "mto_062_ret_zscore_63d": {"inputs": ["close"], "func": mto_062_ret_zscore_63d},
    "mto_063_ret_zscore_252d": {"inputs": ["close"], "func": mto_063_ret_zscore_252d},
    "mto_064_zscore_extreme_count": {"inputs": ["close"], "func": mto_064_zscore_extreme_count},
    "mto_065_price_zscore_21d": {"inputs": ["close"], "func": mto_065_price_zscore_21d},
    "mto_066_price_zscore_63d": {"inputs": ["close"], "func": mto_066_price_zscore_63d},
    "mto_067_price_zscore_252d": {"inputs": ["close"], "func": mto_067_price_zscore_252d},
    "mto_068_price_zscore_min_across_tf": {"inputs": ["close"], "func": mto_068_price_zscore_min_across_tf},
    "mto_069_momentum_oversold_count": {"inputs": ["close"], "func": mto_069_momentum_oversold_count},
    "mto_070_negative_momentum_confluence": {"inputs": ["close"], "func": mto_070_negative_momentum_confluence},
    "mto_071_multi_tf_oversold_master_count": {"inputs": ["close"], "func": mto_071_multi_tf_oversold_master_count},
    "mto_072_oversold_breadth_index": {"inputs": ["close"], "func": mto_072_oversold_breadth_index},
    "mto_073_oversold_alignment_score": {"inputs": ["close"], "func": mto_073_oversold_alignment_score},
    "mto_074_deepest_timeframe_extremity": {"inputs": ["close"], "func": mto_074_deepest_timeframe_extremity},
    "mto_075_multi_timeframe_capitulation_index": {"inputs": ["close"], "func": mto_075_multi_timeframe_capitulation_index},
}
