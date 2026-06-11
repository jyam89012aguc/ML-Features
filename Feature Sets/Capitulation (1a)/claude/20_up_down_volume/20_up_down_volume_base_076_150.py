"""
20_up_down_volume — Base Features 076-150
Domain: direction-conditioned volume balance — down-day vs up-day volume asymmetry,
        return-weighted volume, intraday direction volume, volume concentration,
        distribution/accumulation line variants, multi-timeframe balance comparisons.
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


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Return-weighted volume and price-volume divergence ---

def udv_076_ret_wtd_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|return| * volume) on down days over 21 days (severity-weighted down pressure)."""
    ret = close.pct_change(1)
    val = (ret.abs() * volume).where(ret < 0, 0.0)
    return _rolling_sum(val, _TD_MON)


def udv_077_ret_wtd_up_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|return| * volume) on up days over 21 days."""
    ret = close.pct_change(1)
    val = (ret.abs() * volume).where(ret > 0, 0.0)
    return _rolling_sum(val, _TD_MON)


def udv_078_ret_wtd_down_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|return| * volume) on down days over 63 days."""
    ret = close.pct_change(1)
    val = (ret.abs() * volume).where(ret < 0, 0.0)
    return _rolling_sum(val, _TD_QTR)


def udv_079_ret_wtd_up_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|return| * volume) on up days over 63 days."""
    ret = close.pct_change(1)
    val = (ret.abs() * volume).where(ret > 0, 0.0)
    return _rolling_sum(val, _TD_QTR)


def udv_080_ret_wtd_down_up_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of return-weighted down volume to return-weighted up volume (21d)."""
    return _safe_div(udv_076_ret_wtd_down_vol_21d(close, volume),
                     udv_077_ret_wtd_up_vol_21d(close, volume))


def udv_081_ret_wtd_down_up_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of return-weighted down volume to return-weighted up volume (63d)."""
    return _safe_div(udv_078_ret_wtd_down_vol_63d(close, volume),
                     udv_079_ret_wtd_up_vol_63d(close, volume))


def udv_082_price_vol_divergence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price trend sign vs OBV change sign divergence count over 21 days."""
    price_sign = np.sign(close.diff(_TD_MON))
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    obv_sign = np.sign(obv.diff(_TD_MON))
    diverge = (price_sign != obv_sign).astype(float)
    return _rolling_sum(diverge, _TD_MON)


def udv_083_cum_ret_wtd_vol_balance_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net return-weighted volume (down minus up) over 21 days; positive = distribution."""
    ret = close.pct_change(1)
    signed_rv = ret.abs() * volume * np.sign(-ret).fillna(0)
    return _rolling_sum(signed_rv, _TD_MON)


def udv_084_cum_ret_wtd_vol_balance_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net return-weighted volume (down minus up) over 63 days."""
    ret = close.pct_change(1)
    signed_rv = ret.abs() * volume * np.sign(-ret).fillna(0)
    return _rolling_sum(signed_rv, _TD_QTR)


def udv_085_ret_wtd_vol_balance_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day net return-weighted vol balance in 252-day distribution."""
    s = udv_083_cum_ret_wtd_vol_balance_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group I (086-095): Intraday direction-conditioned volume ---

def udv_086_avg_down_intraday_vol_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on bearish candle days (close < open) over 21 days."""
    bear = volume.where(close < open, np.nan)
    return bear.rolling(_TD_MON, min_periods=1).mean()


def udv_087_avg_up_intraday_vol_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on bullish candle days (close > open) over 21 days."""
    bull = volume.where(close > open, np.nan)
    return bull.rolling(_TD_MON, min_periods=1).mean()


def udv_088_bear_bull_intraday_vol_ratio_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg bear-candle volume to avg bull-candle volume over 21 days."""
    return _safe_div(udv_086_avg_down_intraday_vol_21d(close, open, volume),
                     udv_087_avg_up_intraday_vol_21d(close, open, volume))


def udv_089_bear_candle_vol_share_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume on bearish candle days."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(bv, tv)


def udv_090_bear_candle_vol_share_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume on bearish candle days."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(bv, tv)


def udv_091_gap_down_vol_share_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume on gap-down open days (open < prior close)."""
    gd = _rolling_sum(volume.where(open < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(gd, tv)


def udv_092_gap_down_vol_share_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume on gap-down open days."""
    gd = _rolling_sum(volume.where(open < close.shift(1), 0.0), _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(gd, tv)


def udv_093_bear_candle_vol_ratio_vs_total_avg_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg bear-candle volume divided by avg total volume (21d)."""
    avg_bear = udv_086_avg_down_intraday_vol_21d(close, open, volume)
    avg_all = _rolling_mean(volume, _TD_MON)
    return _safe_div(avg_bear, avg_all)


def udv_094_gap_up_vol_share_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume on gap-up open days (open > prior close)."""
    gu = _rolling_sum(volume.where(open > close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(gu, tv)


def udv_095_bear_candle_vol_share_pct_rank_252d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day bear-candle vol share in 252-day distribution."""
    s = udv_089_bear_candle_vol_share_21d(close, open, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group J (096-105): Chaikin Money Flow and A/D line variants ---

def udv_096_money_flow_multiplier(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Chaikin money flow multiplier: ((close-low)-(high-close)) / (high-low)."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div((close - low) - (high - close), rng)


def udv_097_money_flow_volume(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Money flow volume: multiplier * volume (daily)."""
    mfm = udv_096_money_flow_multiplier(close, high, low)
    return mfm * volume


def udv_098_chaikin_mf_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 21 days: sum(MFV) / sum(volume)."""
    mfv = udv_097_money_flow_volume(close, high, low, volume)
    return _safe_div(_rolling_sum(mfv, _TD_MON), _rolling_sum(volume, _TD_MON))


def udv_099_chaikin_mf_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 63 days."""
    mfv = udv_097_money_flow_volume(close, high, low, volume)
    return _safe_div(_rolling_sum(mfv, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def udv_100_ad_line(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation/Distribution line: cumulative sum of money flow volume."""
    mfv = udv_097_money_flow_volume(close, high, low, volume)
    return mfv.cumsum()


def udv_101_ad_line_21d_change(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in A/D line."""
    return udv_100_ad_line(close, high, low, volume).diff(_TD_MON)


def udv_102_ad_line_63d_change(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day change in A/D line."""
    return udv_100_ad_line(close, high, low, volume).diff(_TD_QTR)


def udv_103_cmf_21d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day CMF within trailing 252-day distribution."""
    cmf = udv_098_chaikin_mf_21d(close, high, low, volume)
    return cmf.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_104_cmf_21d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day CMF relative to 252-day distribution."""
    cmf = udv_098_chaikin_mf_21d(close, high, low, volume)
    m = _rolling_mean(cmf, _TD_YEAR)
    sd = _rolling_std(cmf, _TD_YEAR)
    return _safe_div(cmf - m, sd)


def udv_105_mfv_negative_share_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume with negative money flow multiplier (close in lower half)."""
    mfm = udv_096_money_flow_multiplier(close, high, low)
    neg_vol = _rolling_sum(volume.where(mfm < 0, 0.0), _TD_MON)
    tot_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(neg_vol, tot_vol)


# --- Group K (106-115): Volume concentration on down days, std and skew ---

def udv_106_down_vol_std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard deviation of volume on down-price days over 21 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_MON, min_periods=1).std()


def udv_107_up_vol_std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard deviation of volume on up-price days over 21 days."""
    uv = volume.where(close > close.shift(1), np.nan)
    return uv.rolling(_TD_MON, min_periods=1).std()


def udv_108_down_vol_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of down-day volume (std/mean) over 21 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    m = dv.rolling(_TD_MON, min_periods=1).mean()
    sd = dv.rolling(_TD_MON, min_periods=1).std()
    return _safe_div(sd, m)


def udv_109_down_vol_cv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of down-day volume over 63 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    m = dv.rolling(_TD_QTR, min_periods=1).mean()
    sd = dv.rolling(_TD_QTR, min_periods=1).std()
    return _safe_div(sd, m)


def udv_110_max_single_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum single down-day volume over trailing 21 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return _rolling_max(dv, _TD_MON)


def udv_111_max_single_down_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum single down-day volume over trailing 63 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return _rolling_max(dv, _TD_QTR)


def udv_112_max_down_vol_share_of_total_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max single down-day volume as share of 21-day total volume."""
    max_dv = udv_110_max_single_down_vol_21d(close, volume)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(max_dv, tv)


def udv_113_down_vol_range_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max minus min down-day volume divided by avg down-day volume (21d spread)."""
    dv = volume.where(close < close.shift(1), np.nan)
    mx = dv.rolling(_TD_MON, min_periods=1).max()
    mn = dv.rolling(_TD_MON, min_periods=1).min()
    avg = dv.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(mx - mn, avg)


def udv_114_down_day_vol_above_2x_avg_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days where volume > 2x the 21-day avg volume, in trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < close.shift(1)) & (volume > 2 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_115_down_day_vol_above_2x_avg_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days where volume > 2x avg over trailing 63 days."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    flag = ((close < close.shift(1)) & (volume > 2 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


# --- Group L (116-125): Median-based and quantile volume comparisons ---

def udv_116_median_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on down-price days over trailing 21 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_MON, min_periods=1).median()


def udv_117_median_up_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on up-price days over trailing 21 days."""
    uv = volume.where(close > close.shift(1), np.nan)
    return uv.rolling(_TD_MON, min_periods=1).median()


def udv_118_median_down_up_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of median down-day volume to median up-day volume (21d)."""
    return _safe_div(udv_116_median_down_vol_21d(close, volume),
                     udv_117_median_up_vol_21d(close, volume))


def udv_119_median_down_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on down-price days over trailing 63 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_QTR, min_periods=1).median()


def udv_120_median_up_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on up-price days over trailing 63 days."""
    uv = volume.where(close > close.shift(1), np.nan)
    return uv.rolling(_TD_QTR, min_periods=1).median()


def udv_121_median_down_up_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of median down-day volume to median up-day volume (63d)."""
    return _safe_div(udv_119_median_down_vol_63d(close, volume),
                     udv_120_median_up_vol_63d(close, volume))


def udv_122_down_vol_75th_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """75th percentile of down-day volume over trailing 21 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_MON, min_periods=1).quantile(0.75)


def udv_123_up_vol_25th_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """25th percentile of up-day volume over trailing 21 days."""
    uv = volume.where(close > close.shift(1), np.nan)
    return uv.rolling(_TD_MON, min_periods=1).quantile(0.25)


def udv_124_down_vol_q75_vs_up_vol_q25_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 75th-pct down-vol to 25th-pct up-vol (pessimistic comparison, 21d)."""
    return _safe_div(udv_122_down_vol_75th_pct_21d(close, volume),
                     udv_123_up_vol_25th_pct_21d(close, volume))


def udv_125_down_vol_median_vs_avg_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of median to mean down-day volume (21d); <1 suggests outlier spikes."""
    return _safe_div(udv_116_median_down_vol_21d(close, volume),
                     udv_001_avg_down_vol_21d(close, volume))


def udv_001_avg_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over trailing 21 days (local helper)."""
    return volume.where(close < close.shift(1), np.nan).rolling(_TD_MON, min_periods=1).mean()


# --- Group M (126-135): Cross-timeframe volume balance comparisons ---

def udv_126_down_vol_share_21d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day down-vol share minus 252-day down-vol share (recent vs long-run)."""
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv21 = _rolling_sum(volume, _TD_MON)
    s21 = _safe_div(dv21, tv21)
    dv252 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_YEAR)
    tv252 = _rolling_sum(volume, _TD_YEAR)
    s252 = _safe_div(dv252, tv252)
    return s21 - s252


def udv_127_net_vol_21d_vs_63d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day net volume to 63-day net volume (short vs medium term balance)."""
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    uv21 = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    net21 = uv21 - dv21
    dv63 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    uv63 = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_QTR)
    net63 = uv63 - dv63
    return _safe_div(net21, net63.abs() + _EPS)


def udv_128_vol_wtd_down_frac_21d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day vol-weighted down fraction minus 63-day vol-weighted down fraction."""
    avg21 = _rolling_mean(volume, _TD_MON)
    wt21_d = _safe_div(volume, avg21).where(close < close.shift(1), 0.0)
    wt21_u = _safe_div(volume, avg21).where(close > close.shift(1), 0.0)
    d21 = _rolling_sum(wt21_d, _TD_MON)
    u21 = _rolling_sum(wt21_u, _TD_MON)
    f21 = _safe_div(d21, d21 + u21)
    avg63 = _rolling_mean(volume, _TD_QTR)
    wt63_d = _safe_div(volume, avg63).where(close < close.shift(1), 0.0)
    wt63_u = _safe_div(volume, avg63).where(close > close.shift(1), 0.0)
    d63 = _rolling_sum(wt63_d, _TD_QTR)
    u63 = _rolling_sum(wt63_u, _TD_QTR)
    f63 = _safe_div(d63, d63 + u63)
    return f21 - f63


def udv_129_obv_21d_vs_63d_change_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day OBV change to 63-day OBV change (short vs medium term flow)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg21 = obv.diff(_TD_MON)
    chg63 = obv.diff(_TD_QTR)
    return _safe_div(chg21, chg63.abs() + _EPS)


def udv_130_down_vol_share_expanding_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day down-vol share (all-history extremity)."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    s = _safe_div(dv, tv)
    m = s.expanding(min_periods=5).mean()
    sd = s.expanding(min_periods=5).std()
    return _safe_div(s - m, sd)


def udv_131_down_vol_share_252d_expanding_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day down-vol share."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_YEAR)
    tv = _rolling_sum(volume, _TD_YEAR)
    s = _safe_div(dv, tv)
    return s.expanding(min_periods=10).rank(pct=True)


def udv_132_net_vol_252d_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day net volume relative to 252-day distribution."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    net = uv - dv
    m = _rolling_mean(net, _TD_YEAR)
    sd = _rolling_std(net, _TD_YEAR)
    return _safe_div(net - m, sd)


def udv_133_down_up_vol_ratio_5wk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-week (25-day) rolling ratio of down-day to up-day avg volume."""
    dv = volume.where(close < close.shift(1), np.nan).rolling(25, min_periods=1).mean()
    uv = volume.where(close > close.shift(1), np.nan).rolling(25, min_periods=1).mean()
    return _safe_div(dv, uv)


def udv_134_down_vol_share_5wk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 25-day total volume occurring on down days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), 25)
    tv = _rolling_sum(volume, 25)
    return _safe_div(dv, tv)


def udv_135_vol_balance_composite_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: avg of z-scored (21d down_vol_share, 63d down_vol_share, 21d net_vol_zscore)."""
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv21 = _rolling_sum(volume, _TD_MON)
    s21 = _safe_div(dv21, tv21)
    m21 = _rolling_mean(s21, _TD_YEAR)
    sd21 = _rolling_std(s21, _TD_YEAR)
    z21 = _safe_div(s21 - m21, sd21)
    dv63 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    tv63 = _rolling_sum(volume, _TD_QTR)
    s63 = _safe_div(dv63, tv63)
    m63 = _rolling_mean(s63, _TD_YEAR)
    sd63 = _rolling_std(s63, _TD_YEAR)
    z63 = _safe_div(s63 - m63, sd63)
    dv_n = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    uv_n = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    net = uv_n - dv_n
    mn = _rolling_mean(net, _TD_YEAR)
    sdn = _rolling_std(net, _TD_YEAR)
    zn = _safe_div(net - mn, sdn)
    return (z21 + z63 + zn) / 3.0


# --- Group N (136-145): High/low day volume and directional intensity ---

def udv_136_vol_on_new_low_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on days that set a new 21-day closing low, trailing 21 days."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    new_low = close < roll_min
    nv = volume.where(new_low, np.nan)
    return nv.rolling(_TD_MON, min_periods=1).mean()


def udv_137_vol_on_new_low_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on days that set a new 63-day closing low, trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    nv = volume.where(new_low, np.nan)
    return nv.rolling(_TD_QTR, min_periods=1).mean()


def udv_138_new_low_vol_vs_avg_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on new-21d-low days divided by total avg volume (21d)."""
    return _safe_div(udv_136_vol_on_new_low_days_21d(close, volume),
                     _rolling_mean(volume, _TD_MON))


def udv_139_new_low_vol_vs_avg_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on new-63d-low days divided by total avg volume (63d)."""
    return _safe_div(udv_137_vol_on_new_low_days_63d(close, volume),
                     _rolling_mean(volume, _TD_QTR))


def udv_140_vol_on_down_open_to_close_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on days where open > close AND close < prior close, trailing 21 days."""
    cond = (close < open) & (close < close.shift(1))
    return volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()


def udv_141_vol_share_double_down_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume share on days with bear candle AND down close, trailing 21 days."""
    cond = (close < open) & (close < close.shift(1))
    dv = _rolling_sum(volume.where(cond, 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(dv, tv)


def udv_142_up_vol_on_down_close_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on days with gap-up open but down close (failed rally volume), 21d."""
    cond = (open > close.shift(1)) & (close < close.shift(1))
    return volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()


def udv_143_down_vol_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (down-return * volume) as a directional intensity measure (21d)."""
    ret = close.pct_change(1)
    intensity = (ret * volume).where(ret < 0, 0.0).abs()
    return _rolling_sum(intensity, _TD_MON)


def udv_144_down_vol_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (down-return * volume) intensity over 63 days."""
    ret = close.pct_change(1)
    intensity = (ret * volume).where(ret < 0, 0.0).abs()
    return _rolling_sum(intensity, _TD_QTR)


def udv_145_down_up_intensity_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down intensity (ret*vol on down days) to up intensity (ret*vol on up days), 21d."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    return _safe_div(d_int, u_int)


# --- Group O (146-150): Composite distress and final balance indicators ---

def udv_146_down_up_intensity_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down intensity to up intensity over 63 days."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_QTR)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_QTR)
    return _safe_div(d_int, u_int)


def udv_147_down_vol_share_and_intensity_composite_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of down-vol-share and down-intensity-ratio (21d combined distress score)."""
    share = _safe_div(
        _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    return share * ratio


def udv_148_net_vol_21d_norm_by_total_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day net volume (up-down) normalized by 252-day total volume."""
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    uv21 = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    net21 = uv21 - dv21
    tv252 = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(net21, tv252)


def udv_149_down_vol_share_21d_gt_expanding_mean_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21-day down-vol share exceeds its expanding historical mean."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    s = _safe_div(dv, tv)
    exp_mean = s.expanding(min_periods=5).mean()
    return (s > exp_mean).astype(float)


def udv_150_vol_direction_balance_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distress index: z-scored down-vol-share * down-intensity-ratio, 21d, scaled by 252d rank."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    share = _safe_div(dv, tv)
    m = _rolling_mean(share, _TD_YEAR)
    sd = _rolling_std(share, _TD_YEAR)
    z_share = _safe_div(share - m, sd)
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int + _EPS)
    rank = share.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return z_share * ratio * rank


# --- Group P (176-200): Extended windows, CMF variants, additional composites ---

def udv_176_down_vol_share_5wk_vs_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-week down-vol share minus 21-day down-vol share (ultra-short vs short-term shift)."""
    dv5 = _rolling_sum(volume.where(close < close.shift(1), 0.0), 25)
    tv5 = _rolling_sum(volume, 25)
    s5 = _safe_div(dv5, tv5)
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv21 = _rolling_sum(volume, _TD_MON)
    s21 = _safe_div(dv21, tv21)
    return s5 - s21


def udv_177_down_vol_share_21d_vs_63d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day down-vol share to 63-day down-vol share (recency factor)."""
    dv21 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv21 = _rolling_sum(volume, _TD_MON)
    s21 = _safe_div(dv21, tv21)
    dv63 = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    tv63 = _rolling_sum(volume, _TD_QTR)
    s63 = _safe_div(dv63, tv63)
    return _safe_div(s21, s63)


def udv_178_obv_sma63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day SMA of OBV (medium-term smoothed accumulation trend)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return _rolling_mean(obv, _TD_QTR)


def udv_179_obv_vs_sma63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 63-day SMA (OBV deviation from medium-term trend)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return obv - _rolling_mean(obv, _TD_QTR)


def udv_180_cmf_63d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day CMF within trailing 252-day distribution."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf63 = _safe_div(_rolling_sum(mfv, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return cmf63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_181_cmf_63d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day CMF relative to 252-day distribution."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf63 = _safe_div(_rolling_sum(mfv, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    m = _rolling_mean(cmf63, _TD_YEAR)
    sd = _rolling_std(cmf63, _TD_YEAR)
    return _safe_div(cmf63 - m, sd)


def udv_182_mfv_negative_share_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume with negative money flow multiplier."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    neg_vol = _rolling_sum(volume.where(mfm < 0, 0.0), _TD_QTR)
    tot_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(neg_vol, tot_vol)


def udv_183_ad_line_126d_change(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day change in the Accumulation/Distribution line."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    ad = (mfm * volume).cumsum()
    return ad.diff(_TD_HALF)


def udv_184_ad_line_norm_by_avg_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day A/D line change normalized by 21-day avg total volume."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    ad = (mfm * volume).cumsum()
    chg21 = ad.diff(_TD_MON)
    avg_tv = _rolling_mean(volume, _TD_MON)
    return _safe_div(chg21, avg_tv * _TD_MON)


def udv_185_down_vol_cv_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of down-day volume over 126 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    m = dv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean()
    sd = dv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).std()
    return _safe_div(sd, m)


def udv_186_max_single_down_vol_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum single down-day volume over trailing 126 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return dv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).max()


def udv_187_max_down_vol_share_of_total_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max single down-day volume as share of 63-day total volume."""
    dv = volume.where(close < close.shift(1), 0.0)
    max_dv = _rolling_max(dv, _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(max_dv, tv)


def udv_188_down_day_vol_above_15x_avg_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days where volume >1.5x the 21-day avg volume, trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < close.shift(1)) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_189_median_down_vol_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on down-price days over trailing 126 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).median()


def udv_190_median_down_up_vol_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of median down-day volume to median up-day volume over 126 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    uv = volume.where(close > close.shift(1), np.nan)
    med_d = dv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).median()
    med_u = uv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).median()
    return _safe_div(med_d, med_u)


def udv_191_down_vol_25th_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """25th percentile of down-day volume over trailing 21 days."""
    dv = volume.where(close < close.shift(1), np.nan)
    return dv.rolling(_TD_MON, min_periods=1).quantile(0.25)


def udv_192_up_vol_75th_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """75th percentile of up-day volume over trailing 21 days."""
    uv = volume.where(close > close.shift(1), np.nan)
    return uv.rolling(_TD_MON, min_periods=1).quantile(0.75)


def udv_193_new_low_vol_share_63d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on 63d new-low days divided by avg vol on 252d new-low days (recency of panic)."""
    roll_min63 = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    nl63 = volume.where(close < roll_min63, np.nan)
    avg63 = nl63.rolling(_TD_QTR, min_periods=1).mean()
    roll_min252 = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    nl252 = volume.where(close < roll_min252, np.nan)
    avg252 = nl252.rolling(_TD_YEAR, min_periods=1).mean()
    return _safe_div(avg63, avg252)


def udv_194_vol_on_down_open_to_close_days_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on days where open > close AND close < prior close, trailing 63 days."""
    cond = (close < open) & (close < close.shift(1))
    return volume.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def udv_195_bear_candle_vol_share_126d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126-day total volume on bearish candle days."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_HALF)
    tv = _rolling_sum(volume, _TD_HALF)
    return _safe_div(bv, tv)


def udv_196_gap_down_vol_share_126d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126-day volume on gap-down open days."""
    gd = _rolling_sum(volume.where(open < close.shift(1), 0.0), _TD_HALF)
    tv = _rolling_sum(volume, _TD_HALF)
    return _safe_div(gd, tv)


def udv_197_vol_on_new_low_days_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on days that set a new 126-day closing low, trailing 126 days."""
    roll_min = close.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()
    new_low = close < roll_min
    nv = volume.where(new_low, np.nan)
    return nv.rolling(_TD_HALF, min_periods=1).mean()


def udv_198_down_up_intensity_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down intensity (|ret|*vol on down) to up intensity over 126 days."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_HALF)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_HALF)
    return _safe_div(d_int, u_int)


def udv_199_distress_composite_cmf_intensity_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: avg z-score of 21d CMF and 21d down/up intensity ratio (distress signal)."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    cmf = _safe_div(_rolling_sum(mfm * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    cmf_z = _safe_div(cmf - _rolling_mean(cmf, _TD_YEAR), _rolling_std(cmf, _TD_YEAR))
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    ratio_z = _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR), _rolling_std(ratio, _TD_YEAR))
    return (-cmf_z + ratio_z) / 2.0


def udv_200_vol_direction_extremity_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite extremity: avg of expanding ranks of 21d down-vol share, net vol, and OBV change."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    share = _safe_div(dv, tv)
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    net = uv - dv
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg21 = obv.diff(_TD_MON)
    r1 = share.expanding(min_periods=5).rank(pct=True)
    r2 = (-net).expanding(min_periods=5).rank(pct=True)
    r3 = (-chg21).expanding(min_periods=5).rank(pct=True)
    return (r1 + r2 + r3) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

UP_DOWN_VOLUME_REGISTRY_076_150 = {
    "udv_076_ret_wtd_down_vol_21d": {"inputs": ["close", "volume"], "func": udv_076_ret_wtd_down_vol_21d},
    "udv_077_ret_wtd_up_vol_21d": {"inputs": ["close", "volume"], "func": udv_077_ret_wtd_up_vol_21d},
    "udv_078_ret_wtd_down_vol_63d": {"inputs": ["close", "volume"], "func": udv_078_ret_wtd_down_vol_63d},
    "udv_079_ret_wtd_up_vol_63d": {"inputs": ["close", "volume"], "func": udv_079_ret_wtd_up_vol_63d},
    "udv_080_ret_wtd_down_up_vol_ratio_21d": {"inputs": ["close", "volume"], "func": udv_080_ret_wtd_down_up_vol_ratio_21d},
    "udv_081_ret_wtd_down_up_vol_ratio_63d": {"inputs": ["close", "volume"], "func": udv_081_ret_wtd_down_up_vol_ratio_63d},
    "udv_082_price_vol_divergence_21d": {"inputs": ["close", "volume"], "func": udv_082_price_vol_divergence_21d},
    "udv_083_cum_ret_wtd_vol_balance_21d": {"inputs": ["close", "volume"], "func": udv_083_cum_ret_wtd_vol_balance_21d},
    "udv_084_cum_ret_wtd_vol_balance_63d": {"inputs": ["close", "volume"], "func": udv_084_cum_ret_wtd_vol_balance_63d},
    "udv_085_ret_wtd_vol_balance_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_085_ret_wtd_vol_balance_pct_rank_252d},
    "udv_086_avg_down_intraday_vol_21d": {"inputs": ["close", "open", "volume"], "func": udv_086_avg_down_intraday_vol_21d},
    "udv_087_avg_up_intraday_vol_21d": {"inputs": ["close", "open", "volume"], "func": udv_087_avg_up_intraday_vol_21d},
    "udv_088_bear_bull_intraday_vol_ratio_21d": {"inputs": ["close", "open", "volume"], "func": udv_088_bear_bull_intraday_vol_ratio_21d},
    "udv_089_bear_candle_vol_share_21d": {"inputs": ["close", "open", "volume"], "func": udv_089_bear_candle_vol_share_21d},
    "udv_090_bear_candle_vol_share_63d": {"inputs": ["close", "open", "volume"], "func": udv_090_bear_candle_vol_share_63d},
    "udv_091_gap_down_vol_share_21d": {"inputs": ["close", "open", "volume"], "func": udv_091_gap_down_vol_share_21d},
    "udv_092_gap_down_vol_share_63d": {"inputs": ["close", "open", "volume"], "func": udv_092_gap_down_vol_share_63d},
    "udv_093_bear_candle_vol_ratio_vs_total_avg_21d": {"inputs": ["close", "open", "volume"], "func": udv_093_bear_candle_vol_ratio_vs_total_avg_21d},
    "udv_094_gap_up_vol_share_21d": {"inputs": ["close", "open", "volume"], "func": udv_094_gap_up_vol_share_21d},
    "udv_095_bear_candle_vol_share_pct_rank_252d": {"inputs": ["close", "open", "volume"], "func": udv_095_bear_candle_vol_share_pct_rank_252d},
    "udv_096_money_flow_multiplier": {"inputs": ["close", "high", "low"], "func": udv_096_money_flow_multiplier},
    "udv_097_money_flow_volume": {"inputs": ["close", "high", "low", "volume"], "func": udv_097_money_flow_volume},
    "udv_098_chaikin_mf_21d": {"inputs": ["close", "high", "low", "volume"], "func": udv_098_chaikin_mf_21d},
    "udv_099_chaikin_mf_63d": {"inputs": ["close", "high", "low", "volume"], "func": udv_099_chaikin_mf_63d},
    "udv_100_ad_line": {"inputs": ["close", "high", "low", "volume"], "func": udv_100_ad_line},
    "udv_101_ad_line_21d_change": {"inputs": ["close", "high", "low", "volume"], "func": udv_101_ad_line_21d_change},
    "udv_102_ad_line_63d_change": {"inputs": ["close", "high", "low", "volume"], "func": udv_102_ad_line_63d_change},
    "udv_103_cmf_21d_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": udv_103_cmf_21d_pct_rank_252d},
    "udv_104_cmf_21d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": udv_104_cmf_21d_zscore_252d},
    "udv_105_mfv_negative_share_21d": {"inputs": ["close", "high", "low", "volume"], "func": udv_105_mfv_negative_share_21d},
    "udv_106_down_vol_std_21d": {"inputs": ["close", "volume"], "func": udv_106_down_vol_std_21d},
    "udv_107_up_vol_std_21d": {"inputs": ["close", "volume"], "func": udv_107_up_vol_std_21d},
    "udv_108_down_vol_cv_21d": {"inputs": ["close", "volume"], "func": udv_108_down_vol_cv_21d},
    "udv_109_down_vol_cv_63d": {"inputs": ["close", "volume"], "func": udv_109_down_vol_cv_63d},
    "udv_110_max_single_down_vol_21d": {"inputs": ["close", "volume"], "func": udv_110_max_single_down_vol_21d},
    "udv_111_max_single_down_vol_63d": {"inputs": ["close", "volume"], "func": udv_111_max_single_down_vol_63d},
    "udv_112_max_down_vol_share_of_total_21d": {"inputs": ["close", "volume"], "func": udv_112_max_down_vol_share_of_total_21d},
    "udv_113_down_vol_range_ratio_21d": {"inputs": ["close", "volume"], "func": udv_113_down_vol_range_ratio_21d},
    "udv_114_down_day_vol_above_2x_avg_count_21d": {"inputs": ["close", "volume"], "func": udv_114_down_day_vol_above_2x_avg_count_21d},
    "udv_115_down_day_vol_above_2x_avg_count_63d": {"inputs": ["close", "volume"], "func": udv_115_down_day_vol_above_2x_avg_count_63d},
    "udv_116_median_down_vol_21d": {"inputs": ["close", "volume"], "func": udv_116_median_down_vol_21d},
    "udv_117_median_up_vol_21d": {"inputs": ["close", "volume"], "func": udv_117_median_up_vol_21d},
    "udv_118_median_down_up_vol_ratio_21d": {"inputs": ["close", "volume"], "func": udv_118_median_down_up_vol_ratio_21d},
    "udv_119_median_down_vol_63d": {"inputs": ["close", "volume"], "func": udv_119_median_down_vol_63d},
    "udv_120_median_up_vol_63d": {"inputs": ["close", "volume"], "func": udv_120_median_up_vol_63d},
    "udv_121_median_down_up_vol_ratio_63d": {"inputs": ["close", "volume"], "func": udv_121_median_down_up_vol_ratio_63d},
    "udv_122_down_vol_75th_pct_21d": {"inputs": ["close", "volume"], "func": udv_122_down_vol_75th_pct_21d},
    "udv_123_up_vol_25th_pct_21d": {"inputs": ["close", "volume"], "func": udv_123_up_vol_25th_pct_21d},
    "udv_124_down_vol_q75_vs_up_vol_q25_ratio_21d": {"inputs": ["close", "volume"], "func": udv_124_down_vol_q75_vs_up_vol_q25_ratio_21d},
    "udv_125_down_vol_median_vs_avg_ratio_21d": {"inputs": ["close", "volume"], "func": udv_125_down_vol_median_vs_avg_ratio_21d},
    "udv_126_down_vol_share_21d_vs_252d": {"inputs": ["close", "volume"], "func": udv_126_down_vol_share_21d_vs_252d},
    "udv_127_net_vol_21d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": udv_127_net_vol_21d_vs_63d_ratio},
    "udv_128_vol_wtd_down_frac_21d_vs_63d": {"inputs": ["close", "volume"], "func": udv_128_vol_wtd_down_frac_21d_vs_63d},
    "udv_129_obv_21d_vs_63d_change_ratio": {"inputs": ["close", "volume"], "func": udv_129_obv_21d_vs_63d_change_ratio},
    "udv_130_down_vol_share_expanding_zscore": {"inputs": ["close", "volume"], "func": udv_130_down_vol_share_expanding_zscore},
    "udv_131_down_vol_share_252d_expanding_rank": {"inputs": ["close", "volume"], "func": udv_131_down_vol_share_252d_expanding_rank},
    "udv_132_net_vol_252d_zscore": {"inputs": ["close", "volume"], "func": udv_132_net_vol_252d_zscore},
    "udv_133_down_up_vol_ratio_5wk": {"inputs": ["close", "volume"], "func": udv_133_down_up_vol_ratio_5wk},
    "udv_134_down_vol_share_5wk": {"inputs": ["close", "volume"], "func": udv_134_down_vol_share_5wk},
    "udv_135_vol_balance_composite_score": {"inputs": ["close", "volume"], "func": udv_135_vol_balance_composite_score},
    "udv_136_vol_on_new_low_days_21d": {"inputs": ["close", "volume"], "func": udv_136_vol_on_new_low_days_21d},
    "udv_137_vol_on_new_low_days_63d": {"inputs": ["close", "volume"], "func": udv_137_vol_on_new_low_days_63d},
    "udv_138_new_low_vol_vs_avg_ratio_21d": {"inputs": ["close", "volume"], "func": udv_138_new_low_vol_vs_avg_ratio_21d},
    "udv_139_new_low_vol_vs_avg_ratio_63d": {"inputs": ["close", "volume"], "func": udv_139_new_low_vol_vs_avg_ratio_63d},
    "udv_140_vol_on_down_open_to_close_days_21d": {"inputs": ["close", "open", "volume"], "func": udv_140_vol_on_down_open_to_close_days_21d},
    "udv_141_vol_share_double_down_days_21d": {"inputs": ["close", "open", "volume"], "func": udv_141_vol_share_double_down_days_21d},
    "udv_142_up_vol_on_down_close_days_21d": {"inputs": ["close", "open", "volume"], "func": udv_142_up_vol_on_down_close_days_21d},
    "udv_143_down_vol_intensity_21d": {"inputs": ["close", "volume"], "func": udv_143_down_vol_intensity_21d},
    "udv_144_down_vol_intensity_63d": {"inputs": ["close", "volume"], "func": udv_144_down_vol_intensity_63d},
    "udv_145_down_up_intensity_ratio_21d": {"inputs": ["close", "volume"], "func": udv_145_down_up_intensity_ratio_21d},
    "udv_146_down_up_intensity_ratio_63d": {"inputs": ["close", "volume"], "func": udv_146_down_up_intensity_ratio_63d},
    "udv_147_down_vol_share_and_intensity_composite_21d": {"inputs": ["close", "volume"], "func": udv_147_down_vol_share_and_intensity_composite_21d},
    "udv_148_net_vol_21d_norm_by_total_vol_252d": {"inputs": ["close", "volume"], "func": udv_148_net_vol_21d_norm_by_total_vol_252d},
    "udv_149_down_vol_share_21d_gt_expanding_mean_flag": {"inputs": ["close", "volume"], "func": udv_149_down_vol_share_21d_gt_expanding_mean_flag},
    "udv_150_vol_direction_balance_distress_index": {"inputs": ["close", "volume"], "func": udv_150_vol_direction_balance_distress_index},
    "udv_176_down_vol_share_5wk_vs_21d": {"inputs": ["close", "volume"], "func": udv_176_down_vol_share_5wk_vs_21d},
    "udv_177_down_vol_share_21d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": udv_177_down_vol_share_21d_vs_63d_ratio},
    "udv_178_obv_sma63": {"inputs": ["close", "volume"], "func": udv_178_obv_sma63},
    "udv_179_obv_vs_sma63": {"inputs": ["close", "volume"], "func": udv_179_obv_vs_sma63},
    "udv_180_cmf_63d_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": udv_180_cmf_63d_pct_rank_252d},
    "udv_181_cmf_63d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": udv_181_cmf_63d_zscore_252d},
    "udv_182_mfv_negative_share_63d": {"inputs": ["close", "high", "low", "volume"], "func": udv_182_mfv_negative_share_63d},
    "udv_183_ad_line_126d_change": {"inputs": ["close", "high", "low", "volume"], "func": udv_183_ad_line_126d_change},
    "udv_184_ad_line_norm_by_avg_vol_21d": {"inputs": ["close", "high", "low", "volume"], "func": udv_184_ad_line_norm_by_avg_vol_21d},
    "udv_185_down_vol_cv_126d": {"inputs": ["close", "volume"], "func": udv_185_down_vol_cv_126d},
    "udv_186_max_single_down_vol_126d": {"inputs": ["close", "volume"], "func": udv_186_max_single_down_vol_126d},
    "udv_187_max_down_vol_share_of_total_63d": {"inputs": ["close", "volume"], "func": udv_187_max_down_vol_share_of_total_63d},
    "udv_188_down_day_vol_above_15x_avg_count_21d": {"inputs": ["close", "volume"], "func": udv_188_down_day_vol_above_15x_avg_count_21d},
    "udv_189_median_down_vol_126d": {"inputs": ["close", "volume"], "func": udv_189_median_down_vol_126d},
    "udv_190_median_down_up_vol_ratio_126d": {"inputs": ["close", "volume"], "func": udv_190_median_down_up_vol_ratio_126d},
    "udv_191_down_vol_25th_pct_21d": {"inputs": ["close", "volume"], "func": udv_191_down_vol_25th_pct_21d},
    "udv_192_up_vol_75th_pct_21d": {"inputs": ["close", "volume"], "func": udv_192_up_vol_75th_pct_21d},
    "udv_193_new_low_vol_share_63d_vs_252d": {"inputs": ["close", "volume"], "func": udv_193_new_low_vol_share_63d_vs_252d},
    "udv_194_vol_on_down_open_to_close_days_63d": {"inputs": ["close", "open", "volume"], "func": udv_194_vol_on_down_open_to_close_days_63d},
    "udv_195_bear_candle_vol_share_126d": {"inputs": ["close", "open", "volume"], "func": udv_195_bear_candle_vol_share_126d},
    "udv_196_gap_down_vol_share_126d": {"inputs": ["close", "open", "volume"], "func": udv_196_gap_down_vol_share_126d},
    "udv_197_vol_on_new_low_days_126d": {"inputs": ["close", "volume"], "func": udv_197_vol_on_new_low_days_126d},
    "udv_198_down_up_intensity_ratio_126d": {"inputs": ["close", "volume"], "func": udv_198_down_up_intensity_ratio_126d},
    "udv_199_distress_composite_cmf_intensity_21d": {"inputs": ["close", "high", "low", "volume"], "func": udv_199_distress_composite_cmf_intensity_21d},
    "udv_200_vol_direction_extremity_score": {"inputs": ["close", "volume"], "func": udv_200_vol_direction_extremity_score},
}
