"""
103_multi_timeframe_oversold — Base Features 076-150
Domain: confluence of oversold / extreme readings across multiple lookback
        horizons (extended horizons, band/channel position, cross-family
        alignment composites).
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


def _pct_b(close: pd.Series, w: int) -> pd.Series:
    """Bollinger %B over window w (0 = lower band, 1 = upper band)."""
    ma = _rolling_mean(close, w)
    sd = _rolling_std(close, w)
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    return _safe_div(close - lower, upper - lower)


_RSI_EXT_TF = (7, 14, 21, 42, 63, 126, 252)
_DD_EXT_TF = (_TD_MON, 42, _TD_QTR, _TD_HALF, _TD_YEAR, 504, 756)
_MOM_TF = (_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_CHAN_TF = (14, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group A (076-090): RSI across extended horizons ---

def mto_076_rsi_10d(close: pd.Series) -> pd.Series:
    """10-day RSI."""
    return _rsi(close, 10)


def mto_077_rsi_42d(close: pd.Series) -> pd.Series:
    """42-day RSI (two-month horizon)."""
    return _rsi(close, 42)


def mto_078_rsi_126d(close: pd.Series) -> pd.Series:
    """126-day RSI (half-year horizon)."""
    return _rsi(close, _TD_HALF)


def mto_079_rsi_252d(close: pd.Series) -> pd.Series:
    """252-day RSI (annual horizon)."""
    return _rsi(close, _TD_YEAR)


def mto_080_rsi_min_extended_tf(close: pd.Series) -> pd.Series:
    """Minimum RSI across the 7-252 day extended horizon set."""
    return pd.concat([_rsi(close, w) for w in _RSI_EXT_TF], axis=1).min(axis=1)


def mto_081_rsi_oversold_count_extended(close: pd.Series) -> pd.Series:
    """Count of extended RSI horizons reading below 30."""
    return sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)


def mto_082_rsi_below_25_count(close: pd.Series) -> pd.Series:
    """Count of extended RSI horizons reading below 25."""
    return sum((_rsi(close, w) < 25).astype(float) for w in _RSI_EXT_TF)


def mto_083_rsi_slow_horizon_oversold(close: pd.Series) -> pd.Series:
    """Flag: the 63/126/252-day RSIs are all simultaneously below 40."""
    cnt = sum((_rsi(close, w) < 40).astype(float) for w in (_TD_QTR, _TD_HALF, _TD_YEAR))
    return (cnt == 3).astype(float)


def mto_084_rsi_pctile_14d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 14-day RSI within a trailing 252-day window."""
    return _rolling_rank_pct(_rsi(close, 14), _TD_YEAR)


def mto_085_rsi_at_252d_low_flag(close: pd.Series) -> pd.Series:
    """Flag: the 14-day RSI is at its lowest level of the trailing 252 days."""
    rsi = _rsi(close, 14)
    return (rsi <= _rolling_min(rsi, _TD_YEAR)).astype(float)


def mto_086_rsi_consensus_extremity(close: pd.Series) -> pd.Series:
    """Mean of (40 - RSI) clipped at 0 across extended horizons."""
    depth = sum((40.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF)
    return depth / len(_RSI_EXT_TF)


def mto_087_rsi_fast_oversold_flag(close: pd.Series) -> pd.Series:
    """Flag: both the 5-day and 14-day RSIs are below 25."""
    return ((_rsi(close, 5) < 25) & (_rsi(close, 14) < 25)).astype(float)


def mto_088_rsi_oversold_persistence(close: pd.Series) -> pd.Series:
    """Fraction of the last 63 days the 14-day RSI was below 30."""
    return _rolling_mean((_rsi(close, 14) < 30).astype(float), _TD_QTR)


def mto_089_rsi_term_structure_slope(close: pd.Series) -> pd.Series:
    """252-day RSI minus 7-day RSI (oversold term-structure slope)."""
    return _rsi(close, _TD_YEAR) - _rsi(close, 7)


def mto_090_rsi_min_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the cross-horizon minimum RSI over a trailing 252-day window."""
    mn = pd.concat([_rsi(close, w) for w in _RSI_EXT_TF], axis=1).min(axis=1)
    return _safe_div(mn - _rolling_mean(mn, _TD_YEAR), _rolling_std(mn, _TD_YEAR))


# --- Group B (091-105): Band / channel position across horizons ---

def mto_091_stoch_k_21d(close: pd.Series) -> pd.Series:
    """Stochastic %K over the 21-day horizon."""
    return _stoch_k(close, _TD_MON)


def mto_092_stoch_k_126d(close: pd.Series) -> pd.Series:
    """Stochastic %K over the 126-day horizon."""
    return _stoch_k(close, _TD_HALF)


def mto_093_stoch_k_252d(close: pd.Series) -> pd.Series:
    """Stochastic %K over the 252-day horizon."""
    return _stoch_k(close, _TD_YEAR)


def mto_094_stoch_d_63d(close: pd.Series) -> pd.Series:
    """Smoothed (%D) 3-day average of the 63-day stochastic %K."""
    return _rolling_mean(_stoch_k(close, _TD_QTR), 3)


def mto_095_williams_r_21d(close: pd.Series) -> pd.Series:
    """Williams %R over the 21-day horizon."""
    return _williams_r(close, _TD_MON)


def mto_096_williams_r_126d(close: pd.Series) -> pd.Series:
    """Williams %R over the 126-day horizon."""
    return _williams_r(close, _TD_HALF)


def mto_097_williams_r_252d(close: pd.Series) -> pd.Series:
    """Williams %R over the 252-day horizon."""
    return _williams_r(close, _TD_YEAR)


def mto_098_williams_min_across_tf(close: pd.Series) -> pd.Series:
    """Minimum Williams %R across the 14-252 day channel horizons."""
    return pd.concat([_williams_r(close, w) for w in _CHAN_TF], axis=1).min(axis=1)


def mto_099_bollinger_pctb_21d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 21-day horizon (0 = at the lower band)."""
    return _pct_b(close, _TD_MON)


def mto_100_bollinger_pctb_63d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 63-day horizon."""
    return _pct_b(close, _TD_QTR)


def mto_101_pctb_min_across_tf(close: pd.Series) -> pd.Series:
    """Minimum Bollinger %B across the 21/63/126/252-day horizons."""
    return pd.concat([_pct_b(close, w) for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)], axis=1).min(axis=1)


def mto_102_pctb_oversold_count(close: pd.Series) -> pd.Series:
    """Count of horizons where Bollinger %B is below 0.05 (band breakdown)."""
    return sum((_pct_b(close, w) < 0.05).astype(float)
               for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR))


def mto_103_donchian_position_63d(close: pd.Series) -> pd.Series:
    """Position of close within the 63-day Donchian channel (0 = low)."""
    return _stoch_k(close, _TD_QTR) / 100.0


def mto_104_donchian_position_252d(close: pd.Series) -> pd.Series:
    """Position of close within the 252-day Donchian channel (0 = low)."""
    return _stoch_k(close, _TD_YEAR) / 100.0


def mto_105_channel_oversold_confluence(close: pd.Series) -> pd.Series:
    """Count of channel horizons with the close in the bottom 10% of range."""
    return sum((_stoch_k(close, w) < 10).astype(float) for w in _CHAN_TF)


# --- Group C (106-120): Drawdown / new-low confluence (extended) ---

def mto_106_dd_42d(close: pd.Series) -> pd.Series:
    """Drawdown from the 42-day high."""
    return _drawdown(close, 42)


def mto_107_dd_756d(close: pd.Series) -> pd.Series:
    """Drawdown from the 756-day (3-year) high."""
    return _drawdown(close, 756)


def mto_108_dd_1260d(close: pd.Series) -> pd.Series:
    """Drawdown from the 1260-day (5-year) high."""
    return _drawdown(close, 1260)


def mto_109_dd_extreme_count_30pct(close: pd.Series) -> pd.Series:
    """Count of extended horizons with drawdown worse than -30%."""
    return sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_EXT_TF)


def mto_110_dd_below_median_count(close: pd.Series) -> pd.Series:
    """Count of horizons whose drawdown is below its own 252-day median."""
    cnt = pd.Series(0.0, index=close.index)
    for w in _DD_EXT_TF:
        dd = _drawdown(close, w)
        cnt = cnt + (dd < _rolling_median(dd, _TD_YEAR)).astype(float)
    return cnt


def mto_111_new_low_count_extended(close: pd.Series) -> pd.Series:
    """Count of extended horizons on which the close is at a new trailing low."""
    return sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_EXT_TF)


def mto_112_consecutive_new_low_days(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of the close setting a new 63-day low."""
    f = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    return f.groupby((f == 0).cumsum()).cumsum()


def mto_113_dd_rank_min_extended(close: pd.Series) -> pd.Series:
    """Lowest 252-day percentile rank of drawdown across extended horizons."""
    ranks = [_rolling_rank_pct(_drawdown(close, w), _TD_YEAR) for w in _DD_EXT_TF]
    return pd.concat(ranks, axis=1).min(axis=1)


def mto_114_dd_worst_zscore(close: pd.Series) -> pd.Series:
    """Most negative z-score of drawdown across extended horizons."""
    zs = []
    for w in _DD_EXT_TF:
        dd = _drawdown(close, w)
        zs.append(_safe_div(dd - _rolling_mean(dd, _TD_YEAR), _rolling_std(dd, _TD_YEAR)))
    return pd.concat(zs, axis=1).min(axis=1)


def mto_115_dd_alignment_all_negative_extended(close: pd.Series) -> pd.Series:
    """Flag: drawdown is negative on every extended horizon."""
    cnt = sum((_drawdown(close, w) < 0).astype(float) for w in _DD_EXT_TF)
    return (cnt == len(_DD_EXT_TF)).astype(float)


def mto_116_fresh_low_breadth(close: pd.Series) -> pd.Series:
    """Fraction of extended horizons within 2% of their trailing low."""
    cnt = sum((_safe_div(_rolling_min(close, w), close) > 0.98).astype(float)
              for w in _DD_EXT_TF)
    return cnt / len(_DD_EXT_TF)


def mto_117_dd_worsening_confluence(close: pd.Series) -> pd.Series:
    """Count of horizons whose drawdown deteriorated over the last 5 days."""
    cnt = pd.Series(0.0, index=close.index)
    for w in _DD_EXT_TF:
        dd = _drawdown(close, w)
        cnt = cnt + (dd.diff(5) < 0).astype(float)
    return cnt


def mto_118_dd_severity_weighted(close: pd.Series) -> pd.Series:
    """Horizon-weighted mean drawdown (longer horizons weighted more)."""
    weights = np.linspace(1.0, 2.0, len(_DD_EXT_TF))
    num = sum(weights[i] * _drawdown(close, w) for i, w in enumerate(_DD_EXT_TF))
    return num / weights.sum()


def mto_119_multi_year_low_flag(close: pd.Series) -> pd.Series:
    """Flag: the close is within 1% of its trailing 1260-day (5-year) low."""
    return (_safe_div(_rolling_min(close, 1260), close) > 0.99).astype(float)


def mto_120_dd_confluence_index(close: pd.Series) -> pd.Series:
    """Mean drawdown depth times the fraction of horizons at a new low."""
    mean_dd = pd.concat([_drawdown(close, w) for w in _DD_EXT_TF], axis=1).mean(axis=1)
    nl = sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_EXT_TF)
    return mean_dd.abs() * (nl / len(_DD_EXT_TF))


# --- Group D (121-135): Momentum / return confluence (extended) ---

def mto_121_ret_5d(close: pd.Series) -> pd.Series:
    """Trailing 5-day return."""
    return close.pct_change(_TD_WEEK)


def mto_122_ret_21d(close: pd.Series) -> pd.Series:
    """Trailing 21-day return."""
    return close.pct_change(_TD_MON)


def mto_123_ret_63d(close: pd.Series) -> pd.Series:
    """Trailing 63-day return."""
    return close.pct_change(_TD_QTR)


def mto_124_ret_126d(close: pd.Series) -> pd.Series:
    """Trailing 126-day return."""
    return close.pct_change(_TD_HALF)


def mto_125_ret_252d(close: pd.Series) -> pd.Series:
    """Trailing 252-day return."""
    return close.pct_change(_TD_YEAR)


def mto_126_negative_return_count_extended(close: pd.Series) -> pd.Series:
    """Count of trailing-return horizons that are negative."""
    return sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF)


def mto_127_worst_return_across_tf(close: pd.Series) -> pd.Series:
    """Worst trailing return across the 5-252 day horizons."""
    return pd.concat([close.pct_change(w) for w in _MOM_TF], axis=1).min(axis=1)


def mto_128_mean_return_across_tf(close: pd.Series) -> pd.Series:
    """Mean trailing return across the 5-252 day horizons."""
    return pd.concat([close.pct_change(w) for w in _MOM_TF], axis=1).mean(axis=1)


def mto_129_return_zscore_min_across_tf(close: pd.Series) -> pd.Series:
    """Most negative trailing-return z-score across horizons."""
    zs = []
    for w in _MOM_TF:
        r = close.pct_change(w)
        zs.append(_safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR)))
    return pd.concat(zs, axis=1).min(axis=1)


def mto_130_momentum_all_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: every trailing-return horizon is simultaneously negative."""
    cnt = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF)
    return (cnt == len(_MOM_TF)).astype(float)


def mto_131_deeply_negative_momentum_count(close: pd.Series) -> pd.Series:
    """Count of trailing-return horizons worse than -30%."""
    return sum((close.pct_change(w) < -0.30).astype(float) for w in _MOM_TF)


def mto_132_momentum_dispersion(close: pd.Series) -> pd.Series:
    """Cross-horizon standard deviation of the trailing returns."""
    return pd.concat([close.pct_change(w) for w in _MOM_TF], axis=1).std(axis=1)


def mto_133_return_pctile_min(close: pd.Series) -> pd.Series:
    """Lowest 252-day percentile rank of trailing returns across horizons."""
    ranks = [_rolling_rank_pct(close.pct_change(w), _TD_YEAR) for w in _MOM_TF]
    return pd.concat(ranks, axis=1).min(axis=1)


def mto_134_cumulative_negative_momentum(close: pd.Series) -> pd.Series:
    """Sum of the negative parts of trailing returns across horizons."""
    return sum(close.pct_change(w).clip(upper=0) for w in _MOM_TF)


def mto_135_momentum_confluence_index(close: pd.Series) -> pd.Series:
    """Negative-momentum breadth times the absolute mean trailing return."""
    neg = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / len(_MOM_TF)
    mean_r = pd.concat([close.pct_change(w) for w in _MOM_TF], axis=1).mean(axis=1)
    return neg * mean_r.abs()


# --- Group E (136-150): Cross-family alignment composites ---

def mto_136_oscillator_consensus(close: pd.Series) -> pd.Series:
    """Flag: RSI, stochastic and Williams %R are all oversold at 63 days."""
    rsi_os = _rsi(close, _TD_QTR) < 35
    stoch_os = _stoch_k(close, _TD_QTR) < 20
    will_os = _williams_r(close, _TD_QTR) < -80
    return (rsi_os & stoch_os & will_os).astype(float)


def mto_137_oversold_family_count(close: pd.Series) -> pd.Series:
    """Count of indicator families (RSI/MA/DD/percentile/momentum) majority-oversold."""
    rsi_f = sum((_rsi(close, w) < 30).astype(float) for w in (7, 14, 21, 63)) / 4 > 0.5
    ma_f = sum((close < _rolling_mean(close, w)).astype(float)
               for w in (10, 21, 50, 100, 200)) / 5 > 0.5
    dd_f = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF) / 7 > 0.5
    pc_f = sum((_rolling_rank_pct(close, w) < 0.10).astype(float)
               for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)) / 4 > 0.5
    mo_f = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / 5 > 0.5
    return (rsi_f.astype(float) + ma_f.astype(float) + dd_f.astype(float) +
            pc_f.astype(float) + mo_f.astype(float))


def mto_138_all_families_oversold_flag(close: pd.Series) -> pd.Series:
    """Flag: all 5 indicator families are simultaneously majority-oversold."""
    return (mto_137_oversold_family_count(close) == 5).astype(float)


def mto_139_oversold_zscore_index(close: pd.Series) -> pd.Series:
    """Z-score of the extended RSI oversold count over a trailing 252-day window."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def mto_140_cross_family_min_pctile(close: pd.Series) -> pd.Series:
    """Lowest percentile rank across RSI, price and drawdown families."""
    parts = [_rolling_rank_pct(_rsi(close, 14), _TD_YEAR),
             _rolling_rank_pct(close, _TD_YEAR),
             _rolling_rank_pct(_drawdown(close, _TD_YEAR), _TD_YEAR)]
    return pd.concat(parts, axis=1).min(axis=1)


def mto_141_oversold_depth_total(close: pd.Series) -> pd.Series:
    """Total oversold depth: summed (30 - RSI) and (-drawdown) contributions."""
    rsi_depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in (7, 14, 21, 63)) / 30.0
    dd_depth = sum((-_drawdown(close, w)).clip(lower=0) for w in _DD_EXT_TF)
    return rsi_depth + dd_depth


def mto_142_timeframe_alignment_ratio(close: pd.Series) -> pd.Series:
    """Fraction of all extended horizons (RSI + drawdown) reading oversold."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF)
    return (rsi_c + dd_c) / (len(_RSI_EXT_TF) + len(_DD_EXT_TF))


def mto_143_short_vs_long_oversold_spread(close: pd.Series) -> pd.Series:
    """Short-horizon RSI minus long-horizon RSI (oversold rotation)."""
    short = pd.concat([_rsi(close, w) for w in (5, 7, 14)], axis=1).mean(axis=1)
    long = pd.concat([_rsi(close, w) for w in (_TD_QTR, _TD_HALF, _TD_YEAR)], axis=1).mean(axis=1)
    return short - long


def mto_144_oversold_acceleration(close: pd.Series) -> pd.Series:
    """5-day change in the extended RSI oversold count (deepening confluence)."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    return cnt.diff(5)


def mto_145_capitulation_confluence_count(close: pd.Series) -> pd.Series:
    """Total extreme readings across RSI<25, %B<0.05, DD<-30%, return<-30%."""
    rsi_c = sum((_rsi(close, w) < 25).astype(float) for w in _RSI_EXT_TF)
    pctb_c = sum((_pct_b(close, w) < 0.05).astype(float)
                 for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR))
    dd_c = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_EXT_TF)
    mo_c = sum((close.pct_change(w) < -0.30).astype(float) for w in _MOM_TF)
    return rsi_c + pctb_c + dd_c + mo_c


def mto_146_weighted_multi_tf_score(close: pd.Series) -> pd.Series:
    """Horizon-weighted oversold score across RSI horizons (long = heavier)."""
    weights = {7: 1.0, 14: 1.3, 21: 1.6, 42: 2.0, 63: 2.5, 126: 3.0, 252: 3.5}
    tot = sum(weights.values())
    score = sum(weights[w] * (_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    return score / tot


def mto_147_extreme_reading_density(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with the master oversold count above 12."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF)
    master = rsi_c + dd_c
    return _rolling_mean((master > 12).astype(float), _TD_MON)


def mto_148_oversold_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days with all 4 fast RSI horizons oversold."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in (7, 14, 21, 63))
    return _rolling_mean((cnt == 4).astype(float), _TD_QTR)


def mto_149_multi_tf_distress_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the capitulation confluence count over a trailing 252 days."""
    rsi_c = sum((_rsi(close, w) < 25).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_EXT_TF)
    cnt = rsi_c + dd_c
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def mto_150_master_multi_timeframe_capitulation_index(close: pd.Series) -> pd.Series:
    """Master index: oversold breadth, depth and persistence combined (0-1+)."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF)
    mo_c = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF)
    total = len(_RSI_EXT_TF) + len(_DD_EXT_TF) + len(_MOM_TF)
    breadth = (rsi_c + dd_c + mo_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF) / (len(_RSI_EXT_TF) * 30.0)
    persistence = _rolling_mean((rsi_c > len(_RSI_EXT_TF) / 2).astype(float), _TD_MON)
    return breadth * (0.5 + depth) * (0.5 + persistence)


# ── Registry ──────────────────────────────────────────────────────────────────

MULTI_TIMEFRAME_OVERSOLD_REGISTRY_076_150 = {
    "mto_076_rsi_10d": {"inputs": ["close"], "func": mto_076_rsi_10d},
    "mto_077_rsi_42d": {"inputs": ["close"], "func": mto_077_rsi_42d},
    "mto_078_rsi_126d": {"inputs": ["close"], "func": mto_078_rsi_126d},
    "mto_079_rsi_252d": {"inputs": ["close"], "func": mto_079_rsi_252d},
    "mto_080_rsi_min_extended_tf": {"inputs": ["close"], "func": mto_080_rsi_min_extended_tf},
    "mto_081_rsi_oversold_count_extended": {"inputs": ["close"], "func": mto_081_rsi_oversold_count_extended},
    "mto_082_rsi_below_25_count": {"inputs": ["close"], "func": mto_082_rsi_below_25_count},
    "mto_083_rsi_slow_horizon_oversold": {"inputs": ["close"], "func": mto_083_rsi_slow_horizon_oversold},
    "mto_084_rsi_pctile_14d": {"inputs": ["close"], "func": mto_084_rsi_pctile_14d},
    "mto_085_rsi_at_252d_low_flag": {"inputs": ["close"], "func": mto_085_rsi_at_252d_low_flag},
    "mto_086_rsi_consensus_extremity": {"inputs": ["close"], "func": mto_086_rsi_consensus_extremity},
    "mto_087_rsi_fast_oversold_flag": {"inputs": ["close"], "func": mto_087_rsi_fast_oversold_flag},
    "mto_088_rsi_oversold_persistence": {"inputs": ["close"], "func": mto_088_rsi_oversold_persistence},
    "mto_089_rsi_term_structure_slope": {"inputs": ["close"], "func": mto_089_rsi_term_structure_slope},
    "mto_090_rsi_min_zscore": {"inputs": ["close"], "func": mto_090_rsi_min_zscore},
    "mto_091_stoch_k_21d": {"inputs": ["close"], "func": mto_091_stoch_k_21d},
    "mto_092_stoch_k_126d": {"inputs": ["close"], "func": mto_092_stoch_k_126d},
    "mto_093_stoch_k_252d": {"inputs": ["close"], "func": mto_093_stoch_k_252d},
    "mto_094_stoch_d_63d": {"inputs": ["close"], "func": mto_094_stoch_d_63d},
    "mto_095_williams_r_21d": {"inputs": ["close"], "func": mto_095_williams_r_21d},
    "mto_096_williams_r_126d": {"inputs": ["close"], "func": mto_096_williams_r_126d},
    "mto_097_williams_r_252d": {"inputs": ["close"], "func": mto_097_williams_r_252d},
    "mto_098_williams_min_across_tf": {"inputs": ["close"], "func": mto_098_williams_min_across_tf},
    "mto_099_bollinger_pctb_21d": {"inputs": ["close"], "func": mto_099_bollinger_pctb_21d},
    "mto_100_bollinger_pctb_63d": {"inputs": ["close"], "func": mto_100_bollinger_pctb_63d},
    "mto_101_pctb_min_across_tf": {"inputs": ["close"], "func": mto_101_pctb_min_across_tf},
    "mto_102_pctb_oversold_count": {"inputs": ["close"], "func": mto_102_pctb_oversold_count},
    "mto_103_donchian_position_63d": {"inputs": ["close"], "func": mto_103_donchian_position_63d},
    "mto_104_donchian_position_252d": {"inputs": ["close"], "func": mto_104_donchian_position_252d},
    "mto_105_channel_oversold_confluence": {"inputs": ["close"], "func": mto_105_channel_oversold_confluence},
    "mto_106_dd_42d": {"inputs": ["close"], "func": mto_106_dd_42d},
    "mto_107_dd_756d": {"inputs": ["close"], "func": mto_107_dd_756d},
    "mto_108_dd_1260d": {"inputs": ["close"], "func": mto_108_dd_1260d},
    "mto_109_dd_extreme_count_30pct": {"inputs": ["close"], "func": mto_109_dd_extreme_count_30pct},
    "mto_110_dd_below_median_count": {"inputs": ["close"], "func": mto_110_dd_below_median_count},
    "mto_111_new_low_count_extended": {"inputs": ["close"], "func": mto_111_new_low_count_extended},
    "mto_112_consecutive_new_low_days": {"inputs": ["close"], "func": mto_112_consecutive_new_low_days},
    "mto_113_dd_rank_min_extended": {"inputs": ["close"], "func": mto_113_dd_rank_min_extended},
    "mto_114_dd_worst_zscore": {"inputs": ["close"], "func": mto_114_dd_worst_zscore},
    "mto_115_dd_alignment_all_negative_extended": {"inputs": ["close"], "func": mto_115_dd_alignment_all_negative_extended},
    "mto_116_fresh_low_breadth": {"inputs": ["close"], "func": mto_116_fresh_low_breadth},
    "mto_117_dd_worsening_confluence": {"inputs": ["close"], "func": mto_117_dd_worsening_confluence},
    "mto_118_dd_severity_weighted": {"inputs": ["close"], "func": mto_118_dd_severity_weighted},
    "mto_119_multi_year_low_flag": {"inputs": ["close"], "func": mto_119_multi_year_low_flag},
    "mto_120_dd_confluence_index": {"inputs": ["close"], "func": mto_120_dd_confluence_index},
    "mto_121_ret_5d": {"inputs": ["close"], "func": mto_121_ret_5d},
    "mto_122_ret_21d": {"inputs": ["close"], "func": mto_122_ret_21d},
    "mto_123_ret_63d": {"inputs": ["close"], "func": mto_123_ret_63d},
    "mto_124_ret_126d": {"inputs": ["close"], "func": mto_124_ret_126d},
    "mto_125_ret_252d": {"inputs": ["close"], "func": mto_125_ret_252d},
    "mto_126_negative_return_count_extended": {"inputs": ["close"], "func": mto_126_negative_return_count_extended},
    "mto_127_worst_return_across_tf": {"inputs": ["close"], "func": mto_127_worst_return_across_tf},
    "mto_128_mean_return_across_tf": {"inputs": ["close"], "func": mto_128_mean_return_across_tf},
    "mto_129_return_zscore_min_across_tf": {"inputs": ["close"], "func": mto_129_return_zscore_min_across_tf},
    "mto_130_momentum_all_negative_flag": {"inputs": ["close"], "func": mto_130_momentum_all_negative_flag},
    "mto_131_deeply_negative_momentum_count": {"inputs": ["close"], "func": mto_131_deeply_negative_momentum_count},
    "mto_132_momentum_dispersion": {"inputs": ["close"], "func": mto_132_momentum_dispersion},
    "mto_133_return_pctile_min": {"inputs": ["close"], "func": mto_133_return_pctile_min},
    "mto_134_cumulative_negative_momentum": {"inputs": ["close"], "func": mto_134_cumulative_negative_momentum},
    "mto_135_momentum_confluence_index": {"inputs": ["close"], "func": mto_135_momentum_confluence_index},
    "mto_136_oscillator_consensus": {"inputs": ["close"], "func": mto_136_oscillator_consensus},
    "mto_137_oversold_family_count": {"inputs": ["close"], "func": mto_137_oversold_family_count},
    "mto_138_all_families_oversold_flag": {"inputs": ["close"], "func": mto_138_all_families_oversold_flag},
    "mto_139_oversold_zscore_index": {"inputs": ["close"], "func": mto_139_oversold_zscore_index},
    "mto_140_cross_family_min_pctile": {"inputs": ["close"], "func": mto_140_cross_family_min_pctile},
    "mto_141_oversold_depth_total": {"inputs": ["close"], "func": mto_141_oversold_depth_total},
    "mto_142_timeframe_alignment_ratio": {"inputs": ["close"], "func": mto_142_timeframe_alignment_ratio},
    "mto_143_short_vs_long_oversold_spread": {"inputs": ["close"], "func": mto_143_short_vs_long_oversold_spread},
    "mto_144_oversold_acceleration": {"inputs": ["close"], "func": mto_144_oversold_acceleration},
    "mto_145_capitulation_confluence_count": {"inputs": ["close"], "func": mto_145_capitulation_confluence_count},
    "mto_146_weighted_multi_tf_score": {"inputs": ["close"], "func": mto_146_weighted_multi_tf_score},
    "mto_147_extreme_reading_density": {"inputs": ["close"], "func": mto_147_extreme_reading_density},
    "mto_148_oversold_persistence_63d": {"inputs": ["close"], "func": mto_148_oversold_persistence_63d},
    "mto_149_multi_tf_distress_zscore": {"inputs": ["close"], "func": mto_149_multi_tf_distress_zscore},
    "mto_150_master_multi_timeframe_capitulation_index": {"inputs": ["close"], "func": mto_150_master_multi_timeframe_capitulation_index},
}
