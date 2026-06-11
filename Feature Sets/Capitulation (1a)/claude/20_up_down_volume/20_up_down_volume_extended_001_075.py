"""
20_up_down_volume — Extended Features 001-075
Domain: Negative Volume Index (NVI), Positive Volume Index (PVI), NVI/PVI divergence,
        extended up/down volume ratios across additional windows, down-volume streaks,
        high-volume up/down day counts, OBV variants, volume-weighted up/down pressure,
        and rate-of-change of direction-conditioned volume signals.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _compute_nvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative Volume Index: cumulative, changes only on volume-down days."""
    ret = close.pct_change(1).fillna(0.0)
    vol_down = volume < volume.shift(1)
    # On volume-down days add pct price change; on others add 0
    daily_delta = ret.where(vol_down, 0.0)
    # Start at 1000 (convention)
    nvi = (1000.0 * (1.0 + daily_delta).cumprod())
    return nvi


def _compute_pvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Positive Volume Index: cumulative, changes only on volume-up days."""
    ret = close.pct_change(1).fillna(0.0)
    vol_up = volume > volume.shift(1)
    daily_delta = ret.where(vol_up, 0.0)
    pvi = (1000.0 * (1.0 + daily_delta).cumprod())
    return pvi


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Negative Volume Index (NVI) core features ---

def udv_ext_001_nvi_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative Volume Index level: cumulative price-pct-change on volume-down days (smart money)."""
    return _compute_nvi(close, volume)


def udv_ext_002_nvi_ema255(close: pd.Series, volume: pd.Series) -> pd.Series:
    """255-day EMA of NVI (long-run smart-money trend reference)."""
    nvi = _compute_nvi(close, volume)
    return nvi.ewm(span=255, min_periods=max(1, 127)).mean()


def udv_ext_003_nvi_vs_ema255(close: pd.Series, volume: pd.Series) -> pd.Series:
    """NVI minus its 255-day EMA (above = smart money bullish; below = bearish)."""
    nvi = _compute_nvi(close, volume)
    ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return nvi - ema


def udv_ext_004_nvi_below_ema255_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: NVI is below its 255-day EMA (smart-money bearish signal)."""
    nvi = _compute_nvi(close, volume)
    ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return (nvi < ema).astype(float)


def udv_ext_005_nvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in NVI (recent smart-money momentum direction)."""
    nvi = _compute_nvi(close, volume)
    return nvi.diff(_TD_MON)


def udv_ext_006_nvi_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of NVI level relative to trailing 252-day distribution."""
    nvi = _compute_nvi(close, volume)
    m = _rolling_mean(nvi, _TD_YEAR)
    sd = _rolling_std(nvi, _TD_YEAR)
    return _safe_div(nvi - m, sd)


def udv_ext_007_nvi_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of NVI within trailing 252-day distribution."""
    nvi = _compute_nvi(close, volume)
    return nvi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_ext_008_nvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day change in NVI (medium-term smart-money trend shift)."""
    nvi = _compute_nvi(close, volume)
    return nvi.diff(_TD_QTR)


def udv_ext_009_nvi_vs_ema255_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (NVI minus EMA255) deviation over trailing 252 days."""
    nvi = _compute_nvi(close, volume)
    ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    dev = nvi - ema
    m = _rolling_mean(dev, _TD_YEAR)
    sd = _rolling_std(dev, _TD_YEAR)
    return _safe_div(dev - m, sd)


def udv_ext_010_nvi_pct_chg_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentage change in NVI over 21 days (normalized smart-money momentum)."""
    nvi = _compute_nvi(close, volume)
    prev = nvi.shift(_TD_MON)
    return _safe_div(nvi - prev, prev.abs() + _EPS)


# --- Group B (011-020): Positive Volume Index (PVI) core features ---

def udv_ext_011_pvi_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Positive Volume Index level: cumulative price-pct-change on volume-up days (crowd)."""
    return _compute_pvi(close, volume)


def udv_ext_012_pvi_ema255(close: pd.Series, volume: pd.Series) -> pd.Series:
    """255-day EMA of PVI (long-run crowd-money trend reference)."""
    pvi = _compute_pvi(close, volume)
    return pvi.ewm(span=255, min_periods=max(1, 127)).mean()


def udv_ext_013_pvi_vs_ema255(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVI minus its 255-day EMA (above = crowd bullish; below = crowd bearish)."""
    pvi = _compute_pvi(close, volume)
    ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return pvi - ema


def udv_ext_014_pvi_below_ema255_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: PVI is below its 255-day EMA (crowd bearish signal)."""
    pvi = _compute_pvi(close, volume)
    ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return (pvi < ema).astype(float)


def udv_ext_015_pvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in PVI (recent crowd momentum direction)."""
    pvi = _compute_pvi(close, volume)
    return pvi.diff(_TD_MON)


def udv_ext_016_pvi_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of PVI level relative to trailing 252-day distribution."""
    pvi = _compute_pvi(close, volume)
    m = _rolling_mean(pvi, _TD_YEAR)
    sd = _rolling_std(pvi, _TD_YEAR)
    return _safe_div(pvi - m, sd)


def udv_ext_017_pvi_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of PVI within trailing 252-day distribution."""
    pvi = _compute_pvi(close, volume)
    return pvi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_ext_018_pvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day change in PVI (medium-term crowd trend shift)."""
    pvi = _compute_pvi(close, volume)
    return pvi.diff(_TD_QTR)


def udv_ext_019_pvi_vs_ema255_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (PVI minus EMA255) deviation over trailing 252 days."""
    pvi = _compute_pvi(close, volume)
    ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    dev = pvi - ema
    m = _rolling_mean(dev, _TD_YEAR)
    sd = _rolling_std(dev, _TD_YEAR)
    return _safe_div(dev - m, sd)


def udv_ext_020_pvi_pct_chg_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentage change in PVI over 21 days (normalized crowd momentum)."""
    pvi = _compute_pvi(close, volume)
    prev = pvi.shift(_TD_MON)
    return _safe_div(pvi - prev, prev.abs() + _EPS)


# --- Group C (021-030): NVI vs PVI divergence and relative signals ---

def udv_ext_021_nvi_minus_pvi_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """NVI minus PVI, both normalized to start at 1000 (smart vs crowd divergence)."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    return nvi - pvi


def udv_ext_022_nvi_pvi_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of NVI to PVI (>1 = smart money outperforming crowd; <1 = underperforming)."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    return _safe_div(nvi, pvi)


def udv_ext_023_nvi_pvi_ratio_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of NVI/PVI ratio relative to trailing 252-day distribution."""
    ratio = udv_ext_022_nvi_pvi_ratio(close, volume)
    m = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, sd)


def udv_ext_024_both_below_ema255_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: both NVI and PVI are below their 255-day EMAs (broad bearish signal)."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    nvi_ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    pvi_ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return ((nvi < nvi_ema) & (pvi < pvi_ema)).astype(float)


def udv_ext_025_nvi_slope_minus_pvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day NVI slope minus 21-day PVI slope (smart/crowd momentum divergence)."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    return nvi.diff(_TD_MON) - pvi.diff(_TD_MON)


def udv_ext_026_nvi_ema255_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in NVI EMA255 (trend of the smart-money trend)."""
    nvi = _compute_nvi(close, volume)
    ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return ema.diff(_TD_MON)


def udv_ext_027_pvi_ema255_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in PVI EMA255 (trend of the crowd-money trend)."""
    pvi = _compute_pvi(close, volume)
    ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    return ema.diff(_TD_MON)


def udv_ext_028_nvi_below_pvi_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: NVI level is below PVI level (crowd elevated relative to smart money)."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    return (nvi < pvi).astype(float)


def udv_ext_029_nvi_pvi_spread_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of (NVI minus PVI) within 252-day distribution."""
    spread = udv_ext_021_nvi_minus_pvi_norm(close, volume)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_ext_030_nvi_vs_ema255_and_pvi_vs_ema255_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of z-scored NVI deviation and z-scored PVI deviation from their EMA255s."""
    nvi = _compute_nvi(close, volume)
    pvi = _compute_pvi(close, volume)
    nvi_ema = nvi.ewm(span=255, min_periods=max(1, 127)).mean()
    pvi_ema = pvi.ewm(span=255, min_periods=max(1, 127)).mean()
    nvi_dev = nvi - nvi_ema
    pvi_dev = pvi - pvi_ema
    nvi_z = _safe_div(nvi_dev - _rolling_mean(nvi_dev, _TD_YEAR), _rolling_std(nvi_dev, _TD_YEAR))
    pvi_z = _safe_div(pvi_dev - _rolling_mean(pvi_dev, _TD_YEAR), _rolling_std(pvi_dev, _TD_YEAR))
    return nvi_z + pvi_z


# --- Group D (031-040): Extended up/down volume ratio windows ---

def udv_ext_031_down_up_vol_ratio_10d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 10 days."""
    dv = volume.where(close < close.shift(1), np.nan).rolling(10, min_periods=1).mean()
    uv = volume.where(close > close.shift(1), np.nan).rolling(10, min_periods=1).mean()
    return _safe_div(dv, uv)


def udv_ext_032_down_up_vol_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 126 days (half-year)."""
    dv = volume.where(close < close.shift(1), np.nan).rolling(_TD_HALF, min_periods=_TD_QTR).mean()
    uv = volume.where(close > close.shift(1), np.nan).rolling(_TD_HALF, min_periods=_TD_QTR).mean()
    return _safe_div(dv, uv)


def udv_ext_033_down_vol_share_10d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 10-day total volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), 10)
    tv = _rolling_sum(volume, 10)
    return _safe_div(dv, tv)


def udv_ext_034_down_vol_share_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126-day total volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_HALF)
    tv = _rolling_sum(volume, _TD_HALF)
    return _safe_div(dv, tv)


def udv_ext_035_sum_down_up_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total 63-day down-day volume to total 63-day up-day volume."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_QTR)
    return _safe_div(dv, uv)


def udv_ext_036_sum_down_up_vol_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total 126-day down-day volume to total 126-day up-day volume."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_HALF)
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_HALF)
    return _safe_div(dv, uv)


def udv_ext_037_down_vol_share_10d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 10-day down-vol share relative to 252-day distribution."""
    s = udv_ext_033_down_vol_share_10d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def udv_ext_038_down_up_vol_ratio_10d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """10-day down/up avg-vol ratio divided by 252-day down/up avg-vol ratio (recency)."""
    r10 = udv_ext_031_down_up_vol_ratio_10d(close, volume)
    dv252 = volume.where(close < close.shift(1), np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    uv252 = volume.where(close > close.shift(1), np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    r252 = _safe_div(dv252, uv252)
    return _safe_div(r10, r252)


def udv_ext_039_down_vol_share_126d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 126-day down-vol share relative to 252-day distribution."""
    s = udv_ext_034_down_vol_share_126d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def udv_ext_040_down_up_vol_ratio_126d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day down/up avg-vol ratio divided by 252-day ratio (medium vs long-term)."""
    r126 = udv_ext_032_down_up_vol_ratio_126d(close, volume)
    dv252 = volume.where(close < close.shift(1), np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    uv252 = volume.where(close > close.shift(1), np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    r252 = _safe_div(dv252, uv252)
    return _safe_div(r126, r252)


# --- Group E (041-050): OBV variants (slope, price divergence, z-score, smoothed) ---

def udv_ext_041_obv_ema21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day EMA-smoothed OBV (exponential accumulation trend)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return _ewm_mean(obv, _TD_MON)


def udv_ext_042_obv_ema63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day EMA-smoothed OBV."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return _ewm_mean(obv, _TD_QTR)


def udv_ext_043_obv_vs_ema63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 63-day EMA (medium-term OBV deviation)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return obv - _ewm_mean(obv, _TD_QTR)


def udv_ext_044_obv_252d_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV level relative to trailing 252-day distribution."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    m = _rolling_mean(obv, _TD_YEAR)
    sd = _rolling_std(obv, _TD_YEAR)
    return _safe_div(obv - m, sd)


def udv_ext_045_obv_price_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign divergence: price 63-day direction vs OBV 63-day direction (1=diverge, 0=agree)."""
    price_dir = np.sign(close.diff(_TD_QTR))
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    obv_dir = np.sign(obv.diff(_TD_QTR))
    return (price_dir != obv_dir).astype(float)


def udv_ext_046_obv_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of OBV over 21 days, normalized by 252-day OBV std."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg = obv.diff(_TD_MON)
    sd = _rolling_std(obv, _TD_YEAR)
    return _safe_div(chg, sd + _EPS)


def udv_ext_047_obv_roc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of OBV over 63 days, normalized by 252-day OBV std."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg = obv.diff(_TD_QTR)
    sd = _rolling_std(obv, _TD_YEAR)
    return _safe_div(chg, sd + _EPS)


def udv_ext_048_obv_price_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between daily OBV changes and price returns."""
    obv_delta = (np.sign(close.diff(1)).fillna(0) * volume)
    ret = close.pct_change(1)
    return obv_delta.rolling(_TD_QTR, min_periods=_TD_QTR // 2).corr(ret)


def udv_ext_049_obv_ema21_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change of OBV EMA21 (acceleration in smoothed accumulation)."""
    return udv_ext_041_obv_ema21(close, volume).diff(_TD_MON)


def udv_ext_050_obv_ema63_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of EMA63-smoothed OBV within trailing 252-day distribution."""
    obv_ema = udv_ext_042_obv_ema63(close, volume)
    return obv_ema.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group F (051-060): Accumulation vs distribution day counts ---

def udv_ext_051_high_vol_up_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up-close days with volume > 1.5x 21-day avg volume, trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close > close.shift(1)) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_ext_052_high_vol_down_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down-close days with volume > 1.5x 21-day avg volume, trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < close.shift(1)) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_ext_053_high_vol_down_vs_up_day_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-volume down days to high-volume up days over 21 days."""
    return _safe_div(
        udv_ext_052_high_vol_down_day_count_21d(close, volume),
        udv_ext_051_high_vol_up_day_count_21d(close, volume)
    )


def udv_ext_054_high_vol_up_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume up days (vol > 1.5x avg) over trailing 63 days."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    flag = ((close > close.shift(1)) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def udv_ext_055_high_vol_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume down days (vol > 1.5x avg) over trailing 63 days."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    flag = ((close < close.shift(1)) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def udv_ext_056_high_vol_down_vs_up_day_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-volume down days to high-volume up days over 63 days."""
    return _safe_div(
        udv_ext_055_high_vol_down_day_count_63d(close, volume),
        udv_ext_054_high_vol_up_day_count_63d(close, volume)
    )


def udv_ext_057_accum_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of accumulation days: up-close with above-average volume, trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close > close.shift(1)) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_ext_058_distrib_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days: down-close with above-average volume, trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < close.shift(1)) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_ext_059_distrib_vs_accum_day_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of distribution days to accumulation days over 21 days."""
    return _safe_div(
        udv_ext_058_distrib_day_count_21d(close, volume),
        udv_ext_057_accum_day_count_21d(close, volume)
    )


def udv_ext_060_net_accum_distrib_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation day count minus distribution day count (21d net balance)."""
    return (udv_ext_057_accum_day_count_21d(close, volume)
            - udv_ext_058_distrib_day_count_21d(close, volume))


# --- Group G (061-068): Down-volume streaks ---

def udv_ext_061_current_down_vol_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-day streak where volume increased on a down-close day."""
    is_hvdown = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(int)
    streak = is_hvdown.copy().astype(float)
    arr = is_hvdown.values
    s = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        s[i] = (s[i - 1] + 1.0) * arr[i] if arr[i] else 0.0
    return pd.Series(s, index=close.index)


def udv_ext_062_down_vol_streak_max_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive down-vol-up-streak length within trailing 21 days."""
    streak = udv_ext_061_current_down_vol_streak(close, volume)
    return _rolling_max(streak, _TD_MON)


def udv_ext_063_down_vol_streak_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive down-vol-up-streak length within trailing 63 days."""
    streak = udv_ext_061_current_down_vol_streak(close, volume)
    return _rolling_max(streak, _TD_QTR)


def udv_ext_064_vol_down_day_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak of consecutive down-close days (regardless of volume level)."""
    is_down = (close < close.shift(1)).astype(int).values
    s = np.zeros(len(is_down), dtype=float)
    for i in range(1, len(is_down)):
        s[i] = (s[i - 1] + 1.0) * is_down[i] if is_down[i] else 0.0
    return pd.Series(s, index=close.index)


def udv_ext_065_vol_on_down_streak_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on days that are part of a down-streak of >= 2 days, trailing 21 days."""
    streak = udv_ext_064_vol_down_day_streak(close, volume)
    in_streak = volume.where(streak >= 2, np.nan)
    return in_streak.rolling(_TD_MON, min_periods=1).mean()


def udv_ext_066_down_vol_streak_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on down-streak days (streak>=2) as share of 21-day total volume."""
    streak = udv_ext_064_vol_down_day_streak(close, volume)
    streak_vol = _rolling_sum(volume.where(streak >= 2, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(streak_vol, total_vol)


def udv_ext_067_max_down_streak_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum length of a consecutive down-close streak over trailing 21 days."""
    streak = udv_ext_064_vol_down_day_streak(close, volume)
    return _rolling_max(streak, _TD_MON)


def udv_ext_068_max_down_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum length of a consecutive down-close streak over trailing 63 days."""
    streak = udv_ext_064_vol_down_day_streak(close, volume)
    return _rolling_max(streak, _TD_QTR)


# --- Group H (069-075): Volume-weighted up/down pressure and ROC ---

def udv_ext_069_vol_wtd_up_pressure_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted up pressure: sum of (return * volume) on up days, 21d."""
    ret = close.pct_change(1)
    pressure = (ret * volume).where(ret > 0, 0.0)
    return _rolling_sum(pressure, _TD_MON)


def udv_ext_070_vol_wtd_down_pressure_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted down pressure: sum of (|return| * volume) on down days, 21d."""
    ret = close.pct_change(1)
    pressure = (ret.abs() * volume).where(ret < 0, 0.0)
    return _rolling_sum(pressure, _TD_MON)


def udv_ext_071_down_vs_up_pressure_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume-weighted down pressure to up pressure over 21 days."""
    return _safe_div(
        udv_ext_070_vol_wtd_down_pressure_21d(close, volume),
        udv_ext_069_vol_wtd_up_pressure_21d(close, volume)
    )


def udv_ext_072_down_vs_up_pressure_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume-weighted down pressure to up pressure over 63 days."""
    ret = close.pct_change(1)
    down_p = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_QTR)
    up_p = _rolling_sum((ret * volume).where(ret > 0, 0.0), _TD_QTR)
    return _safe_div(down_p, up_p)


def udv_ext_073_down_pressure_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rate of change of volume-weighted down pressure (acceleration of selling)."""
    p = udv_ext_070_vol_wtd_down_pressure_21d(close, volume)
    prev = p.shift(_TD_MON)
    return _safe_div(p - prev, prev.abs() + _EPS)


def udv_ext_074_down_pressure_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume-weighted down pressure relative to 252-day distribution."""
    p = udv_ext_070_vol_wtd_down_pressure_21d(close, volume)
    m = _rolling_mean(p, _TD_YEAR)
    sd = _rolling_std(p, _TD_YEAR)
    return _safe_div(p - m, sd)


def udv_ext_075_nvi_pvi_both_below_and_high_distrib_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: NVI-below-EMA255 flag + PVI-below-EMA255 flag + z-scored distribution-day excess (21d)."""
    nvi_flag = udv_ext_004_nvi_below_ema255_flag(close, volume)
    pvi_flag = udv_ext_014_pvi_below_ema255_flag(close, volume)
    distrib = udv_ext_058_distrib_day_count_21d(close, volume)
    accum = udv_ext_057_accum_day_count_21d(close, volume)
    net = distrib - accum
    m = _rolling_mean(net, _TD_YEAR)
    sd = _rolling_std(net, _TD_YEAR)
    z_net = _safe_div(net - m, sd)
    return nvi_flag + pvi_flag + z_net


# ── Registry ──────────────────────────────────────────────────────────────────

UP_DOWN_VOLUME_EXTENDED_REGISTRY_001_075 = {
    "udv_ext_001_nvi_raw": {"inputs": ["close", "volume"], "func": udv_ext_001_nvi_raw},
    "udv_ext_002_nvi_ema255": {"inputs": ["close", "volume"], "func": udv_ext_002_nvi_ema255},
    "udv_ext_003_nvi_vs_ema255": {"inputs": ["close", "volume"], "func": udv_ext_003_nvi_vs_ema255},
    "udv_ext_004_nvi_below_ema255_flag": {"inputs": ["close", "volume"], "func": udv_ext_004_nvi_below_ema255_flag},
    "udv_ext_005_nvi_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_005_nvi_slope_21d},
    "udv_ext_006_nvi_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_006_nvi_zscore_252d},
    "udv_ext_007_nvi_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_ext_007_nvi_pct_rank_252d},
    "udv_ext_008_nvi_slope_63d": {"inputs": ["close", "volume"], "func": udv_ext_008_nvi_slope_63d},
    "udv_ext_009_nvi_vs_ema255_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_009_nvi_vs_ema255_zscore_252d},
    "udv_ext_010_nvi_pct_chg_21d": {"inputs": ["close", "volume"], "func": udv_ext_010_nvi_pct_chg_21d},
    "udv_ext_011_pvi_raw": {"inputs": ["close", "volume"], "func": udv_ext_011_pvi_raw},
    "udv_ext_012_pvi_ema255": {"inputs": ["close", "volume"], "func": udv_ext_012_pvi_ema255},
    "udv_ext_013_pvi_vs_ema255": {"inputs": ["close", "volume"], "func": udv_ext_013_pvi_vs_ema255},
    "udv_ext_014_pvi_below_ema255_flag": {"inputs": ["close", "volume"], "func": udv_ext_014_pvi_below_ema255_flag},
    "udv_ext_015_pvi_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_015_pvi_slope_21d},
    "udv_ext_016_pvi_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_016_pvi_zscore_252d},
    "udv_ext_017_pvi_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_ext_017_pvi_pct_rank_252d},
    "udv_ext_018_pvi_slope_63d": {"inputs": ["close", "volume"], "func": udv_ext_018_pvi_slope_63d},
    "udv_ext_019_pvi_vs_ema255_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_019_pvi_vs_ema255_zscore_252d},
    "udv_ext_020_pvi_pct_chg_21d": {"inputs": ["close", "volume"], "func": udv_ext_020_pvi_pct_chg_21d},
    "udv_ext_021_nvi_minus_pvi_norm": {"inputs": ["close", "volume"], "func": udv_ext_021_nvi_minus_pvi_norm},
    "udv_ext_022_nvi_pvi_ratio": {"inputs": ["close", "volume"], "func": udv_ext_022_nvi_pvi_ratio},
    "udv_ext_023_nvi_pvi_ratio_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_023_nvi_pvi_ratio_zscore_252d},
    "udv_ext_024_both_below_ema255_flag": {"inputs": ["close", "volume"], "func": udv_ext_024_both_below_ema255_flag},
    "udv_ext_025_nvi_slope_minus_pvi_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_025_nvi_slope_minus_pvi_slope_21d},
    "udv_ext_026_nvi_ema255_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_026_nvi_ema255_slope_21d},
    "udv_ext_027_pvi_ema255_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_027_pvi_ema255_slope_21d},
    "udv_ext_028_nvi_below_pvi_flag": {"inputs": ["close", "volume"], "func": udv_ext_028_nvi_below_pvi_flag},
    "udv_ext_029_nvi_pvi_spread_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_ext_029_nvi_pvi_spread_pct_rank_252d},
    "udv_ext_030_nvi_vs_ema255_and_pvi_vs_ema255_composite": {"inputs": ["close", "volume"], "func": udv_ext_030_nvi_vs_ema255_and_pvi_vs_ema255_composite},
    "udv_ext_031_down_up_vol_ratio_10d": {"inputs": ["close", "volume"], "func": udv_ext_031_down_up_vol_ratio_10d},
    "udv_ext_032_down_up_vol_ratio_126d": {"inputs": ["close", "volume"], "func": udv_ext_032_down_up_vol_ratio_126d},
    "udv_ext_033_down_vol_share_10d": {"inputs": ["close", "volume"], "func": udv_ext_033_down_vol_share_10d},
    "udv_ext_034_down_vol_share_126d": {"inputs": ["close", "volume"], "func": udv_ext_034_down_vol_share_126d},
    "udv_ext_035_sum_down_up_vol_ratio_63d": {"inputs": ["close", "volume"], "func": udv_ext_035_sum_down_up_vol_ratio_63d},
    "udv_ext_036_sum_down_up_vol_ratio_126d": {"inputs": ["close", "volume"], "func": udv_ext_036_sum_down_up_vol_ratio_126d},
    "udv_ext_037_down_vol_share_10d_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_037_down_vol_share_10d_zscore_252d},
    "udv_ext_038_down_up_vol_ratio_10d_vs_252d": {"inputs": ["close", "volume"], "func": udv_ext_038_down_up_vol_ratio_10d_vs_252d},
    "udv_ext_039_down_vol_share_126d_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_039_down_vol_share_126d_zscore_252d},
    "udv_ext_040_down_up_vol_ratio_126d_vs_252d": {"inputs": ["close", "volume"], "func": udv_ext_040_down_up_vol_ratio_126d_vs_252d},
    "udv_ext_041_obv_ema21": {"inputs": ["close", "volume"], "func": udv_ext_041_obv_ema21},
    "udv_ext_042_obv_ema63": {"inputs": ["close", "volume"], "func": udv_ext_042_obv_ema63},
    "udv_ext_043_obv_vs_ema63": {"inputs": ["close", "volume"], "func": udv_ext_043_obv_vs_ema63},
    "udv_ext_044_obv_252d_zscore": {"inputs": ["close", "volume"], "func": udv_ext_044_obv_252d_zscore},
    "udv_ext_045_obv_price_divergence_63d": {"inputs": ["close", "volume"], "func": udv_ext_045_obv_price_divergence_63d},
    "udv_ext_046_obv_roc_21d": {"inputs": ["close", "volume"], "func": udv_ext_046_obv_roc_21d},
    "udv_ext_047_obv_roc_63d": {"inputs": ["close", "volume"], "func": udv_ext_047_obv_roc_63d},
    "udv_ext_048_obv_price_corr_63d": {"inputs": ["close", "volume"], "func": udv_ext_048_obv_price_corr_63d},
    "udv_ext_049_obv_ema21_slope_21d": {"inputs": ["close", "volume"], "func": udv_ext_049_obv_ema21_slope_21d},
    "udv_ext_050_obv_ema63_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_ext_050_obv_ema63_pct_rank_252d},
    "udv_ext_051_high_vol_up_day_count_21d": {"inputs": ["close", "volume"], "func": udv_ext_051_high_vol_up_day_count_21d},
    "udv_ext_052_high_vol_down_day_count_21d": {"inputs": ["close", "volume"], "func": udv_ext_052_high_vol_down_day_count_21d},
    "udv_ext_053_high_vol_down_vs_up_day_ratio_21d": {"inputs": ["close", "volume"], "func": udv_ext_053_high_vol_down_vs_up_day_ratio_21d},
    "udv_ext_054_high_vol_up_day_count_63d": {"inputs": ["close", "volume"], "func": udv_ext_054_high_vol_up_day_count_63d},
    "udv_ext_055_high_vol_down_day_count_63d": {"inputs": ["close", "volume"], "func": udv_ext_055_high_vol_down_day_count_63d},
    "udv_ext_056_high_vol_down_vs_up_day_ratio_63d": {"inputs": ["close", "volume"], "func": udv_ext_056_high_vol_down_vs_up_day_ratio_63d},
    "udv_ext_057_accum_day_count_21d": {"inputs": ["close", "volume"], "func": udv_ext_057_accum_day_count_21d},
    "udv_ext_058_distrib_day_count_21d": {"inputs": ["close", "volume"], "func": udv_ext_058_distrib_day_count_21d},
    "udv_ext_059_distrib_vs_accum_day_ratio_21d": {"inputs": ["close", "volume"], "func": udv_ext_059_distrib_vs_accum_day_ratio_21d},
    "udv_ext_060_net_accum_distrib_count_21d": {"inputs": ["close", "volume"], "func": udv_ext_060_net_accum_distrib_count_21d},
    "udv_ext_061_current_down_vol_streak": {"inputs": ["close", "volume"], "func": udv_ext_061_current_down_vol_streak},
    "udv_ext_062_down_vol_streak_max_21d": {"inputs": ["close", "volume"], "func": udv_ext_062_down_vol_streak_max_21d},
    "udv_ext_063_down_vol_streak_max_63d": {"inputs": ["close", "volume"], "func": udv_ext_063_down_vol_streak_max_63d},
    "udv_ext_064_vol_down_day_streak": {"inputs": ["close", "volume"], "func": udv_ext_064_vol_down_day_streak},
    "udv_ext_065_vol_on_down_streak_days_21d": {"inputs": ["close", "volume"], "func": udv_ext_065_vol_on_down_streak_days_21d},
    "udv_ext_066_down_vol_streak_vol_share_21d": {"inputs": ["close", "volume"], "func": udv_ext_066_down_vol_streak_vol_share_21d},
    "udv_ext_067_max_down_streak_21d": {"inputs": ["close", "volume"], "func": udv_ext_067_max_down_streak_21d},
    "udv_ext_068_max_down_streak_63d": {"inputs": ["close", "volume"], "func": udv_ext_068_max_down_streak_63d},
    "udv_ext_069_vol_wtd_up_pressure_21d": {"inputs": ["close", "volume"], "func": udv_ext_069_vol_wtd_up_pressure_21d},
    "udv_ext_070_vol_wtd_down_pressure_21d": {"inputs": ["close", "volume"], "func": udv_ext_070_vol_wtd_down_pressure_21d},
    "udv_ext_071_down_vs_up_pressure_ratio_21d": {"inputs": ["close", "volume"], "func": udv_ext_071_down_vs_up_pressure_ratio_21d},
    "udv_ext_072_down_vs_up_pressure_ratio_63d": {"inputs": ["close", "volume"], "func": udv_ext_072_down_vs_up_pressure_ratio_63d},
    "udv_ext_073_down_pressure_roc_21d": {"inputs": ["close", "volume"], "func": udv_ext_073_down_pressure_roc_21d},
    "udv_ext_074_down_pressure_zscore_252d": {"inputs": ["close", "volume"], "func": udv_ext_074_down_pressure_zscore_252d},
    "udv_ext_075_nvi_pvi_both_below_and_high_distrib_composite": {"inputs": ["close", "volume"], "func": udv_ext_075_nvi_pvi_both_below_and_high_distrib_composite},
}
