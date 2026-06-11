"""
30_relative_strength — Base Features 076-150
Domain: price vs its own moving averages — Hull Moving Average (HMA),
        MA ribbon (ordering, compression, flags), z-scores of MA distances,
        ATR-normalized distances, price percentile in trailing range,
        composite distress metrics.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _sma(close: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(close, w)


def _ema(close: pd.Series, span: int) -> pd.Series:
    return _ewm_mean(close, span)


def _wma(close: pd.Series, w: int) -> pd.Series:
    """Linearly-weighted moving average of period w (pure vectorised)."""
    weights = np.arange(1, w + 1, dtype=float)
    w_sum = weights.sum()
    mp = max(1, w // 2)
    def _wma_window(x):
        n = len(x)
        if n < mp:
            return np.nan
        wt = np.arange(1, n + 1, dtype=float)
        return float(np.dot(x, wt) / wt.sum())
    return close.rolling(w, min_periods=mp).apply(_wma_window, raw=True)


def _hma(close: pd.Series, n: int) -> pd.Series:
    """Hull Moving Average: WMA(2*WMA(n/2) - WMA(n), floor(sqrt(n)))."""
    half = max(2, n // 2)
    sqrtn = max(2, int(np.floor(np.sqrt(n))))
    wma_half = _wma(close, half)
    wma_full = _wma(close, n)
    raw = 2.0 * wma_half - wma_full
    return _wma(raw, sqrtn)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int = 14) -> pd.Series:
    return _rolling_mean(_tr(close, high, low), w)


# ── Helper: MA ribbon stack ────────────────────────────────────────────────────
# Ribbon periods: 5, 10, 20, 30, 40, 50, 100, 200 (8 SMAs)
_RIBBON_PERIODS = [5, 10, 20, 30, 40, 50, 100, 200]


def _ribbon_mas(close: pd.Series):
    """Return list of 8 SMA Series for ribbon periods."""
    return [_sma(close, p) for p in _RIBBON_PERIODS]


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Hull Moving Average (HMA) ---

def rst_076_close_to_hma16_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to HMA16 (short Hull MA, n=16)."""
    return _safe_div(close, _hma(close, 16))


def rst_077_close_to_hma49_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to HMA49 (medium Hull MA, n=49)."""
    return _safe_div(close, _hma(close, 49))


def rst_078_pct_dist_hma16(close: pd.Series) -> pd.Series:
    """Percent distance of close from HMA16 ((close - HMA16) / HMA16)."""
    h = _hma(close, 16)
    return _safe_div(close - h, h)


def rst_079_pct_dist_hma49(close: pd.Series) -> pd.Series:
    """Percent distance of close from HMA49."""
    h = _hma(close, 49)
    return _safe_div(close - h, h)


def rst_080_depth_below_hma16(close: pd.Series) -> pd.Series:
    """Depth below HMA16 (0 if above; negative = distress)."""
    h = _hma(close, 16)
    return _safe_div(close - h, h).clip(upper=0.0)


def rst_081_depth_below_hma49(close: pd.Series) -> pd.Series:
    """Depth below HMA49 (0 if above; negative = distress)."""
    h = _hma(close, 49)
    return _safe_div(close - h, h).clip(upper=0.0)


def rst_082_hma16_slope_5d(close: pd.Series) -> pd.Series:
    """5-day first difference of HMA16 (HMA slope / momentum)."""
    return _hma(close, 16).diff(_TD_WEEK)


def rst_083_hma49_slope_5d(close: pd.Series) -> pd.Series:
    """5-day first difference of HMA49."""
    return _hma(close, 49).diff(_TD_WEEK)


def rst_084_hma16_slope_21d(close: pd.Series) -> pd.Series:
    """21-day first difference of HMA16 (monthly trend direction)."""
    return _hma(close, 16).diff(_TD_MON)


def rst_085_hma49_slope_21d(close: pd.Series) -> pd.Series:
    """21-day first difference of HMA49."""
    return _hma(close, 49).diff(_TD_MON)


def rst_086_hma16_pct_slope_5d(close: pd.Series) -> pd.Series:
    """5-day pct change of HMA16 (normalised slope)."""
    h = _hma(close, 16)
    return _safe_div(h.diff(_TD_WEEK), h.shift(_TD_WEEK))


def rst_087_hma49_pct_slope_5d(close: pd.Series) -> pd.Series:
    """5-day pct change of HMA49."""
    h = _hma(close, 49)
    return _safe_div(h.diff(_TD_WEEK), h.shift(_TD_WEEK))


def rst_088_hma16_below_hma49_flag(close: pd.Series) -> pd.Series:
    """Flag: HMA16 < HMA49 (short Hull crossed below long Hull — bearish)."""
    return (_hma(close, 16) < _hma(close, 49)).astype(float)


def rst_089_pct_dist_hma16_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-HMA16 pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _hma(close, 16), _hma(close, 16))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_090_pct_dist_hma49_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-HMA49 pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _hma(close, 49), _hma(close, 49))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


# --- Group I (091-115): MA Ribbon features ---
# Ribbon: SMA 5, 10, 20, 30, 40, 50, 100, 200 (8 MAs)

def rst_091_ribbon_frac_below(close: pd.Series) -> pd.Series:
    """Fraction of 8 ribbon SMAs that close is currently below (0.0 – 1.0)."""
    mas = _ribbon_mas(close)
    below = sum((close < m).astype(float) for m in mas)
    return below / float(len(_RIBBON_PERIODS))


def rst_092_ribbon_count_below(close: pd.Series) -> pd.Series:
    """Count of 8 ribbon SMAs that close is currently below (0-8)."""
    mas = _ribbon_mas(close)
    return sum((close < m).astype(float) for m in mas)


def rst_093_ribbon_below_all_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below ALL 8 ribbon SMAs (extreme bearish positioning)."""
    return (rst_092_ribbon_count_below(close) >= 8).astype(float)


def rst_094_ribbon_spread_pct(close: pd.Series) -> pd.Series:
    """MA ribbon spread: (SMA200 - SMA5) / SMA5; measures ribbon width."""
    s5   = _sma(close, 5)
    s200 = _sma(close, 200)
    return _safe_div(s200 - s5, s5)


def rst_095_ribbon_std_pct(close: pd.Series) -> pd.Series:
    """Std-dev of 8 ribbon SMA values divided by their mean (ribbon compression)."""
    mas = _ribbon_mas(close)
    df  = pd.concat(mas, axis=1)
    mn  = df.mean(axis=1).replace(0, np.nan)
    sd  = df.std(axis=1)
    return _safe_div(sd, mn)


def rst_096_ribbon_all_declining_flag(close: pd.Series) -> pd.Series:
    """Flag: ALL 8 ribbon SMAs have negative 21-day slope (all declining)."""
    flags = [(m.diff(_TD_MON) < 0).astype(float) for m in _ribbon_mas(close)]
    return (sum(flags) >= 8).astype(float)


def rst_097_ribbon_majority_declining_flag(close: pd.Series) -> pd.Series:
    """Flag: majority (>=5) of 8 ribbon SMAs are declining (21-day diff < 0)."""
    flags = [(m.diff(_TD_MON) < 0).astype(float) for m in _ribbon_mas(close)]
    return (sum(flags) >= 5).astype(float)


def rst_098_ribbon_count_declining(close: pd.Series) -> pd.Series:
    """Count of ribbon SMAs with a negative 21-day slope (0-8)."""
    return sum((m.diff(_TD_MON) < 0).astype(float) for m in _ribbon_mas(close))


def rst_099_ribbon_ordered_bearish_score(close: pd.Series) -> pd.Series:
    """Score of ribbon pairs in bearish order (shorter < longer), max = 7."""
    mas = _ribbon_mas(close)
    score = sum(
        (mas[i] < mas[i + 1]).astype(float) for i in range(len(mas) - 1)
    )
    return score


def rst_100_ribbon_frac_below_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of ribbon-fraction-below vs trailing 252-day distribution."""
    frac = rst_091_ribbon_frac_below(close)
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def rst_101_ribbon_spread_pct_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of ribbon-spread vs trailing 252-day distribution."""
    sp = rst_094_ribbon_spread_pct(close)
    m = _rolling_mean(sp, _TD_YEAR)
    s = _rolling_std(sp, _TD_YEAR)
    return _safe_div(sp - m, s)


def rst_102_close_below_ribbon_bottom_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below the lowest ribbon SMA (SMA5 during declining trend)."""
    mas = _ribbon_mas(close)
    df  = pd.concat(mas, axis=1)
    mn  = df.min(axis=1)
    return (close < mn).astype(float)


def rst_103_close_above_ribbon_top_flag(close: pd.Series) -> pd.Series:
    """Flag: close is above the highest ribbon SMA (SMA200 or SMA5 in bull)."""
    mas = _ribbon_mas(close)
    df  = pd.concat(mas, axis=1)
    mx  = df.max(axis=1)
    return (close > mx).astype(float)


def rst_104_ribbon_sum_depth_below(close: pd.Series) -> pd.Series:
    """Sum of pct-depth below each of 8 ribbon SMAs (clipped at 0, summed)."""
    mas = _ribbon_mas(close)
    depths = [_safe_div(close - m, m).clip(upper=0.0) for m in mas]
    return sum(depths)


def rst_105_ribbon_mean_dist(close: pd.Series) -> pd.Series:
    """Equal-weight mean pct-distance from all 8 ribbon SMAs."""
    mas = _ribbon_mas(close)
    dists = [_safe_div(close - m, m) for m in mas]
    return sum(dists) / float(len(_RIBBON_PERIODS))


def rst_106_ribbon_mean_dist_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of mean ribbon distance vs 252-day distribution."""
    md = rst_105_ribbon_mean_dist(close)
    m = _rolling_mean(md, _TD_YEAR)
    s = _rolling_std(md, _TD_YEAR)
    return _safe_div(md - m, s)


def rst_107_ribbon_std_pct_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ribbon compression (std/mean) within trailing 252 days."""
    comp = rst_095_ribbon_std_pct(close)
    return comp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_108_ribbon_frac_below_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ribbon-fraction-below within trailing 252 days."""
    frac = rst_091_ribbon_frac_below(close)
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_109_ribbon_ordered_score_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ribbon bearish-order score within trailing 252 days."""
    sc = rst_099_ribbon_ordered_bearish_score(close)
    return sc.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_110_ribbon_sma5_vs_sma200_ratio(close: pd.Series) -> pd.Series:
    """Ratio SMA5 / SMA200 (top-to-bottom ribbon stretch)."""
    return _safe_div(_sma(close, 5), _sma(close, 200))


def rst_111_ribbon_sma20_vs_sma100_ratio(close: pd.Series) -> pd.Series:
    """Ratio SMA20 / SMA100 (mid-ribbon positioning)."""
    return _safe_div(_sma(close, 20), _sma(close, 100))


def rst_112_ribbon_sma50_vs_sma200_ratio(close: pd.Series) -> pd.Series:
    """Ratio SMA50 / SMA200 (classic death-cross metric within ribbon)."""
    return _safe_div(_sma(close, 50), _sma(close, 200))


def rst_113_ribbon_sum_depth_below_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of ribbon sum-of-depth-below vs 252-day distribution."""
    sd = rst_104_ribbon_sum_depth_below(close)
    m = _rolling_mean(sd, _TD_YEAR)
    s = _rolling_std(sd, _TD_YEAR)
    return _safe_div(sd - m, s)


def rst_114_ribbon_expansion_5d(close: pd.Series) -> pd.Series:
    """5-day change in ribbon spread (positive = expanding, negative = compressing)."""
    sp = rst_094_ribbon_spread_pct(close)
    return sp.diff(_TD_WEEK)


def rst_115_ribbon_compression_flag(close: pd.Series) -> pd.Series:
    """Flag: ribbon std/mean is in lowest 20th percentile of trailing 252-day window."""
    comp = rst_095_ribbon_std_pct(close)
    q20 = comp.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.20)
    return (comp <= q20).astype(float)


# --- Group J (116-130): Z-scores and pct-ranks of SMA/EMA MA-distances ---

def rst_116_pct_dist_sma21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-SMA21 pct-distance vs trailing 252-day distribution."""
    d = _safe_div(close - _sma(close, _TD_MON), _sma(close, _TD_MON))
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    return _safe_div(d - m, s)


def rst_117_pct_dist_sma200_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-SMA200 pct-distance vs 252-day distribution."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    return _safe_div(d - m, s)


def rst_118_pct_dist_ema200_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-EMA200 pct-distance vs 252-day distribution."""
    d = _safe_div(close - _ema(close, 200), _ema(close, 200))
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    return _safe_div(d - m, s)


def rst_119_pct_dist_sma200_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-SMA200 pct-distance vs 504-day distribution."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    m = _rolling_mean(d, 504)
    s = _rolling_std(d, 504)
    return _safe_div(d - m, s)


def rst_120_pct_dist_sma21_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of close-to-SMA21 pct-distance."""
    d = _safe_div(close - _sma(close, _TD_MON), _sma(close, _TD_MON))
    m = d.expanding(min_periods=5).mean()
    s = d.expanding(min_periods=5).std()
    return _safe_div(d - m, s)


def rst_121_pct_dist_sma200_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of close-to-SMA200 pct-distance."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    m = d.expanding(min_periods=5).mean()
    s = d.expanding(min_periods=5).std()
    return _safe_div(d - m, s)


def rst_122_pct_dist_sma21_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close-to-SMA21 distance within trailing 252 days."""
    d = _safe_div(close - _sma(close, _TD_MON), _sma(close, _TD_MON))
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_123_pct_dist_sma200_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close-to-SMA200 distance within trailing 252 days."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_124_pct_dist_sma200_pctrank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of close-to-SMA200 pct-distance in 504-day window."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def rst_125_close_vs_sma200_log_ratio(close: pd.Series) -> pd.Series:
    """Log ratio ln(close / SMA200) — symmetric measure around zero."""
    return np.log((_safe_div(close, _sma(close, 200))).clip(lower=_EPS))


def rst_126_min_pct_dist_sma200_252d(close: pd.Series) -> pd.Series:
    """Min (deepest below SMA200) pct-distance over trailing 252 days."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return _rolling_min(d, _TD_YEAR)


def rst_127_expanding_min_pct_dist_sma200(close: pd.Series) -> pd.Series:
    """All-history expanding minimum of close-to-SMA200 pct-distance."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.expanding(min_periods=1).min()


def rst_128_dist_sma200_range_ratio_252d(close: pd.Series) -> pd.Series:
    """Current SMA200 distance relative to its 252-day range (min to max)."""
    d  = _safe_div(close - _sma(close, 200), _sma(close, 200))
    mx = _rolling_max(d, _TD_YEAR)
    mn = _rolling_min(d, _TD_YEAR)
    rng = (mx - mn).replace(0, np.nan)
    return _safe_div(d - mn, rng)


def rst_129_avg_dist_all_6_smas(close: pd.Series) -> pd.Series:
    """Equal-weight average pct-distance of close from all 6 SMAs."""
    spans = [10, _TD_MON, 50, _TD_QTR, 100, 200]
    dists = [_safe_div(close - _sma(close, w), _sma(close, w)) for w in spans]
    return sum(dists) / 6.0


def rst_130_avg_dist_all_6_emas(close: pd.Series) -> pd.Series:
    """Equal-weight average pct-distance of close from all 6 EMAs."""
    spans = [10, _TD_MON, 50, _TD_QTR, 100, 200]
    dists = [_safe_div(close - _ema(close, w), _ema(close, w)) for w in spans]
    return sum(dists) / 6.0


# --- Group K (131-140): ATR-normalised distances ---

def rst_131_dist_sma21_in_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from SMA21 in 14-day ATR units ((close-SMA21)/ATR14)."""
    ma   = _sma(close, _TD_MON)
    atr14 = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr14)


def rst_132_dist_sma200_in_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from SMA200 in 14-day ATR units; deep negative = extreme distress."""
    ma   = _sma(close, 200)
    atr14 = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr14)


def rst_133_depth_below_sma200_in_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below SMA200 in ATR14 units (0 if above; large negative = extreme)."""
    return rst_132_dist_sma200_in_atr14(close, high, low).clip(upper=0.0)


def rst_134_dist_ema200_in_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from EMA200 in 14-day ATR units."""
    ma   = _ema(close, 200)
    atr14 = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr14)


def rst_135_dist_sma200_in_atr14_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR14-normalised SMA200 distance vs 252-day distribution."""
    atr14 = _atr(close, high, low, 14)
    d = _safe_div(close - _sma(close, 200), atr14)
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    return _safe_div(d - m, s)


# --- Group L (136-145): Price percentile in trailing range ---

def rst_136_price_pctile_in_21d_range(close: pd.Series) -> pd.Series:
    """Close percentile in 21-day high-low close range."""
    hi = _rolling_max(close, _TD_MON)
    lo = _rolling_min(close, _TD_MON)
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_137_price_pctile_in_63d_range(close: pd.Series) -> pd.Series:
    """Close percentile in 63-day close range."""
    hi = _rolling_max(close, _TD_QTR)
    lo = _rolling_min(close, _TD_QTR)
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_138_price_pctile_in_126d_range(close: pd.Series) -> pd.Series:
    """Close percentile in 126-day close range."""
    hi = _rolling_max(close, _TD_HALF)
    lo = _rolling_min(close, _TD_HALF)
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_139_price_pctile_in_252d_range(close: pd.Series) -> pd.Series:
    """Close percentile in 252-day close range."""
    hi = _rolling_max(close, _TD_YEAR)
    lo = _rolling_min(close, _TD_YEAR)
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_140_price_pctile_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within trailing 252-day close distribution."""
    return close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


# --- Group M (141-150): Composite distress metrics ---

def rst_141_sma200_pct_dist_pctrank_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of close-to-SMA200 pct-distance."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.expanding(min_periods=5).rank(pct=True)


def rst_142_ma_convergence_score(close: pd.Series) -> pd.Series:
    """MA convergence: 1 - (std of 4 MAs / mean of 4 MAs); higher = tighter."""
    s21  = _sma(close, _TD_MON)
    s63  = _sma(close, _TD_QTR)
    s200 = _sma(close, 200)
    e21  = _ema(close, _TD_MON)
    ma_df   = pd.concat([s21, s63, s200, e21], axis=1)
    ma_mean = ma_df.mean(axis=1).replace(0, np.nan)
    ma_std  = ma_df.std(axis=1)
    return 1.0 - _safe_div(ma_std, ma_mean)


def rst_143_ema21_vs_sma21_spread(close: pd.Series) -> pd.Series:
    """Spread EMA21 - SMA21 as pct of close (EMA leads SMA in trends)."""
    return _safe_div(_ema(close, _TD_MON) - _sma(close, _TD_MON), close)


def rst_144_ema200_vs_sma200_spread(close: pd.Series) -> pd.Series:
    """Spread EMA200 - SMA200 as pct of close (long-term trend direction)."""
    return _safe_div(_ema(close, 200) - _sma(close, 200), close)


def rst_145_close_pctile_in_21d_ma_band(close: pd.Series) -> pd.Series:
    """Close position within SMA21 ± 1 rolling-std band."""
    ma  = _sma(close, _TD_MON)
    std = _rolling_std(close, _TD_MON)
    lo  = ma - std
    hi  = ma + std
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_146_close_pctile_in_200d_ma_band(close: pd.Series) -> pd.Series:
    """Close position within SMA200 ± 1 rolling-std band."""
    ma  = _sma(close, 200)
    std = _rolling_std(close, 200)
    lo  = ma - std
    hi  = ma + std
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_147_below_ma_breadth_fraction_sma(close: pd.Series) -> pd.Series:
    """Fraction of 6 SMAs that close is below (0.0 to 1.0)."""
    cnt = (
        (close < _sma(close, 10)).astype(float)
        + (close < _sma(close, _TD_MON)).astype(float)
        + (close < _sma(close, 50)).astype(float)
        + (close < _sma(close, _TD_QTR)).astype(float)
        + (close < _sma(close, 100)).astype(float)
        + (close < _sma(close, 200)).astype(float)
    )
    return cnt / 6.0


def rst_148_below_ma_breadth_fraction_ema(close: pd.Series) -> pd.Series:
    """Fraction of 6 EMAs that close is below (0.0 to 1.0)."""
    cnt = (
        (close < _ema(close, 10)).astype(float)
        + (close < _ema(close, _TD_MON)).astype(float)
        + (close < _ema(close, 50)).astype(float)
        + (close < _ema(close, _TD_QTR)).astype(float)
        + (close < _ema(close, 100)).astype(float)
        + (close < _ema(close, 200)).astype(float)
    )
    return cnt / 6.0


def rst_149_sum_depth_12mas_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of sum-of-depth-below-12-MAs vs 252-day distribution."""
    spans  = [10, _TD_MON, 50, _TD_QTR, 100, 200]
    sma_d  = [_safe_div(close - _sma(close, w), _sma(close, w)).clip(upper=0.0) for w in spans]
    ema_d  = [_safe_div(close - _ema(close, w), _ema(close, w)).clip(upper=0.0) for w in spans]
    depth  = sum(sma_d) + sum(ema_d)
    m      = _rolling_mean(depth, _TD_YEAR)
    s      = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def rst_150_composite_distress_index(close: pd.Series) -> pd.Series:
    """Composite: ribbon-frac-below z-score × Mansfield-RS depth × MA-count-below."""
    frac   = rst_091_ribbon_frac_below(close)
    fz     = _safe_div(frac - _rolling_mean(frac, _TD_YEAR),
                       _rolling_std(frac, _TD_YEAR))
    man_d  = _safe_div(close - _sma(close, _TD_YEAR), _sma(close, _TD_YEAR)).clip(upper=0.0)
    cnt12  = (
        sum((close < _sma(close, w)).astype(float) for w in [10, _TD_MON, 50, _TD_QTR, 100, 200])
        + sum((close < _ema(close, w)).astype(float) for w in [10, _TD_MON, 50, _TD_QTR, 100, 200])
    )
    return fz * man_d.abs() * cnt12


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_REGISTRY_076_150 = {
    "rst_076_close_to_hma16_ratio": {"inputs": ["close"], "func": rst_076_close_to_hma16_ratio},
    "rst_077_close_to_hma49_ratio": {"inputs": ["close"], "func": rst_077_close_to_hma49_ratio},
    "rst_078_pct_dist_hma16": {"inputs": ["close"], "func": rst_078_pct_dist_hma16},
    "rst_079_pct_dist_hma49": {"inputs": ["close"], "func": rst_079_pct_dist_hma49},
    "rst_080_depth_below_hma16": {"inputs": ["close"], "func": rst_080_depth_below_hma16},
    "rst_081_depth_below_hma49": {"inputs": ["close"], "func": rst_081_depth_below_hma49},
    "rst_082_hma16_slope_5d": {"inputs": ["close"], "func": rst_082_hma16_slope_5d},
    "rst_083_hma49_slope_5d": {"inputs": ["close"], "func": rst_083_hma49_slope_5d},
    "rst_084_hma16_slope_21d": {"inputs": ["close"], "func": rst_084_hma16_slope_21d},
    "rst_085_hma49_slope_21d": {"inputs": ["close"], "func": rst_085_hma49_slope_21d},
    "rst_086_hma16_pct_slope_5d": {"inputs": ["close"], "func": rst_086_hma16_pct_slope_5d},
    "rst_087_hma49_pct_slope_5d": {"inputs": ["close"], "func": rst_087_hma49_pct_slope_5d},
    "rst_088_hma16_below_hma49_flag": {"inputs": ["close"], "func": rst_088_hma16_below_hma49_flag},
    "rst_089_pct_dist_hma16_zscore_252d": {"inputs": ["close"], "func": rst_089_pct_dist_hma16_zscore_252d},
    "rst_090_pct_dist_hma49_zscore_252d": {"inputs": ["close"], "func": rst_090_pct_dist_hma49_zscore_252d},
    "rst_091_ribbon_frac_below": {"inputs": ["close"], "func": rst_091_ribbon_frac_below},
    "rst_092_ribbon_count_below": {"inputs": ["close"], "func": rst_092_ribbon_count_below},
    "rst_093_ribbon_below_all_flag": {"inputs": ["close"], "func": rst_093_ribbon_below_all_flag},
    "rst_094_ribbon_spread_pct": {"inputs": ["close"], "func": rst_094_ribbon_spread_pct},
    "rst_095_ribbon_std_pct": {"inputs": ["close"], "func": rst_095_ribbon_std_pct},
    "rst_096_ribbon_all_declining_flag": {"inputs": ["close"], "func": rst_096_ribbon_all_declining_flag},
    "rst_097_ribbon_majority_declining_flag": {"inputs": ["close"], "func": rst_097_ribbon_majority_declining_flag},
    "rst_098_ribbon_count_declining": {"inputs": ["close"], "func": rst_098_ribbon_count_declining},
    "rst_099_ribbon_ordered_bearish_score": {"inputs": ["close"], "func": rst_099_ribbon_ordered_bearish_score},
    "rst_100_ribbon_frac_below_zscore_252d": {"inputs": ["close"], "func": rst_100_ribbon_frac_below_zscore_252d},
    "rst_101_ribbon_spread_pct_zscore_252d": {"inputs": ["close"], "func": rst_101_ribbon_spread_pct_zscore_252d},
    "rst_102_close_below_ribbon_bottom_flag": {"inputs": ["close"], "func": rst_102_close_below_ribbon_bottom_flag},
    "rst_103_close_above_ribbon_top_flag": {"inputs": ["close"], "func": rst_103_close_above_ribbon_top_flag},
    "rst_104_ribbon_sum_depth_below": {"inputs": ["close"], "func": rst_104_ribbon_sum_depth_below},
    "rst_105_ribbon_mean_dist": {"inputs": ["close"], "func": rst_105_ribbon_mean_dist},
    "rst_106_ribbon_mean_dist_zscore_252d": {"inputs": ["close"], "func": rst_106_ribbon_mean_dist_zscore_252d},
    "rst_107_ribbon_std_pct_pctrank_252d": {"inputs": ["close"], "func": rst_107_ribbon_std_pct_pctrank_252d},
    "rst_108_ribbon_frac_below_pctrank_252d": {"inputs": ["close"], "func": rst_108_ribbon_frac_below_pctrank_252d},
    "rst_109_ribbon_ordered_score_pctrank_252d": {"inputs": ["close"], "func": rst_109_ribbon_ordered_score_pctrank_252d},
    "rst_110_ribbon_sma5_vs_sma200_ratio": {"inputs": ["close"], "func": rst_110_ribbon_sma5_vs_sma200_ratio},
    "rst_111_ribbon_sma20_vs_sma100_ratio": {"inputs": ["close"], "func": rst_111_ribbon_sma20_vs_sma100_ratio},
    "rst_112_ribbon_sma50_vs_sma200_ratio": {"inputs": ["close"], "func": rst_112_ribbon_sma50_vs_sma200_ratio},
    "rst_113_ribbon_sum_depth_below_zscore_252d": {"inputs": ["close"], "func": rst_113_ribbon_sum_depth_below_zscore_252d},
    "rst_114_ribbon_expansion_5d": {"inputs": ["close"], "func": rst_114_ribbon_expansion_5d},
    "rst_115_ribbon_compression_flag": {"inputs": ["close"], "func": rst_115_ribbon_compression_flag},
    "rst_116_pct_dist_sma21_zscore_252d": {"inputs": ["close"], "func": rst_116_pct_dist_sma21_zscore_252d},
    "rst_117_pct_dist_sma200_zscore_252d": {"inputs": ["close"], "func": rst_117_pct_dist_sma200_zscore_252d},
    "rst_118_pct_dist_ema200_zscore_252d": {"inputs": ["close"], "func": rst_118_pct_dist_ema200_zscore_252d},
    "rst_119_pct_dist_sma200_zscore_504d": {"inputs": ["close"], "func": rst_119_pct_dist_sma200_zscore_504d},
    "rst_120_pct_dist_sma21_expanding_zscore": {"inputs": ["close"], "func": rst_120_pct_dist_sma21_expanding_zscore},
    "rst_121_pct_dist_sma200_expanding_zscore": {"inputs": ["close"], "func": rst_121_pct_dist_sma200_expanding_zscore},
    "rst_122_pct_dist_sma21_pctrank_252d": {"inputs": ["close"], "func": rst_122_pct_dist_sma21_pctrank_252d},
    "rst_123_pct_dist_sma200_pctrank_252d": {"inputs": ["close"], "func": rst_123_pct_dist_sma200_pctrank_252d},
    "rst_124_pct_dist_sma200_pctrank_504d": {"inputs": ["close"], "func": rst_124_pct_dist_sma200_pctrank_504d},
    "rst_125_close_vs_sma200_log_ratio": {"inputs": ["close"], "func": rst_125_close_vs_sma200_log_ratio},
    "rst_126_min_pct_dist_sma200_252d": {"inputs": ["close"], "func": rst_126_min_pct_dist_sma200_252d},
    "rst_127_expanding_min_pct_dist_sma200": {"inputs": ["close"], "func": rst_127_expanding_min_pct_dist_sma200},
    "rst_128_dist_sma200_range_ratio_252d": {"inputs": ["close"], "func": rst_128_dist_sma200_range_ratio_252d},
    "rst_129_avg_dist_all_6_smas": {"inputs": ["close"], "func": rst_129_avg_dist_all_6_smas},
    "rst_130_avg_dist_all_6_emas": {"inputs": ["close"], "func": rst_130_avg_dist_all_6_emas},
    "rst_131_dist_sma21_in_atr14": {"inputs": ["close", "high", "low"], "func": rst_131_dist_sma21_in_atr14},
    "rst_132_dist_sma200_in_atr14": {"inputs": ["close", "high", "low"], "func": rst_132_dist_sma200_in_atr14},
    "rst_133_depth_below_sma200_in_atr14": {"inputs": ["close", "high", "low"], "func": rst_133_depth_below_sma200_in_atr14},
    "rst_134_dist_ema200_in_atr14": {"inputs": ["close", "high", "low"], "func": rst_134_dist_ema200_in_atr14},
    "rst_135_dist_sma200_in_atr14_zscore_252d": {"inputs": ["close", "high", "low"], "func": rst_135_dist_sma200_in_atr14_zscore_252d},
    "rst_136_price_pctile_in_21d_range": {"inputs": ["close"], "func": rst_136_price_pctile_in_21d_range},
    "rst_137_price_pctile_in_63d_range": {"inputs": ["close"], "func": rst_137_price_pctile_in_63d_range},
    "rst_138_price_pctile_in_126d_range": {"inputs": ["close"], "func": rst_138_price_pctile_in_126d_range},
    "rst_139_price_pctile_in_252d_range": {"inputs": ["close"], "func": rst_139_price_pctile_in_252d_range},
    "rst_140_price_pctile_rank_252d": {"inputs": ["close"], "func": rst_140_price_pctile_rank_252d},
    "rst_141_sma200_pct_dist_pctrank_expanding": {"inputs": ["close"], "func": rst_141_sma200_pct_dist_pctrank_expanding},
    "rst_142_ma_convergence_score": {"inputs": ["close"], "func": rst_142_ma_convergence_score},
    "rst_143_ema21_vs_sma21_spread": {"inputs": ["close"], "func": rst_143_ema21_vs_sma21_spread},
    "rst_144_ema200_vs_sma200_spread": {"inputs": ["close"], "func": rst_144_ema200_vs_sma200_spread},
    "rst_145_close_pctile_in_21d_ma_band": {"inputs": ["close"], "func": rst_145_close_pctile_in_21d_ma_band},
    "rst_146_close_pctile_in_200d_ma_band": {"inputs": ["close"], "func": rst_146_close_pctile_in_200d_ma_band},
    "rst_147_below_ma_breadth_fraction_sma": {"inputs": ["close"], "func": rst_147_below_ma_breadth_fraction_sma},
    "rst_148_below_ma_breadth_fraction_ema": {"inputs": ["close"], "func": rst_148_below_ma_breadth_fraction_ema},
    "rst_149_sum_depth_12mas_zscore_252d": {"inputs": ["close"], "func": rst_149_sum_depth_12mas_zscore_252d},
    "rst_150_composite_distress_index": {"inputs": ["close"], "func": rst_150_composite_distress_index},
}
