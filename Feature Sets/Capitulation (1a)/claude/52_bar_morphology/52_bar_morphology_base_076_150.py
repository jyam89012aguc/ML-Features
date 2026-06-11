"""
52_bar_morphology — Base Features 076-150
Domain: candlestick body/range structural statistics — rolling body skew, body momentum,
        body-size distribution quantiles, body-direction runs, range-normalized bodies,
        body acceleration, body vs average-range ratios, body asymmetry, multi-window
        body structural aggregates (aggregate statistics; no named patterns)
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
    """Element-wise division; zero denominator → NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _body_abs(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Absolute body size: |close - open|."""
    return (close - open_).abs()


def _body(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Signed body: close - open."""
    return close - open_


def _range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range: high - low."""
    return (high - low).clip(lower=0.0)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Rolling body skewness and distribution shape ---

def bmf_076_body_skew_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling skewness of absolute body size."""
    return _body_abs(close, open).rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()


def bmf_077_body_skew_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day rolling skewness of absolute body size."""
    return _body_abs(close, open).rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).skew()


def bmf_078_signed_body_skew_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling skewness of signed body (positive = bull-skewed)."""
    return _body(close, open).rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()


def bmf_079_body_q90_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """90th percentile of absolute body size over trailing 63 days."""
    return _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.90)


def bmf_080_body_q10_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """10th percentile of absolute body size over trailing 63 days."""
    return _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.10)


def bmf_081_body_q90_to_q10_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 90th to 10th percentile of body size (spread of distribution)."""
    q90 = _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.90)
    q10 = _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.10)
    return _safe_div(q90, q10.replace(0, np.nan))


def bmf_082_body_q75_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """75th percentile of absolute body over trailing 63 days."""
    return _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.75)


def bmf_083_body_q25_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """25th percentile of absolute body over trailing 63 days."""
    return _rolling_quantile(_body_abs(close, open), _TD_QTR, 0.25)


def bmf_084_body_above_q75_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's body > 63-day 75th-percentile body (outsized bar)."""
    babs = _body_abs(close, open)
    q75 = _rolling_quantile(babs.shift(1), _TD_QTR, 0.75)
    return (babs > q75).astype(float)


def bmf_085_body_below_q25_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's body < 63-day 25th-percentile body (compressed bar)."""
    babs = _body_abs(close, open)
    q25 = _rolling_quantile(babs.shift(1), _TD_QTR, 0.25)
    return (babs < q25).astype(float)


# --- Group I (086-095): Body momentum (body vs its own moving average) ---

def bmf_086_body_sma5_vs_sma21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 5-day body SMA to 21-day body SMA (short-term body momentum)."""
    babs = _body_abs(close, open)
    return _safe_div(_rolling_mean(babs, _TD_WEEK), _rolling_mean(babs, _TD_MON))


def bmf_087_body_sma21_vs_sma63(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day body SMA to 63-day body SMA."""
    babs = _body_abs(close, open)
    return _safe_div(_rolling_mean(babs, _TD_MON), _rolling_mean(babs, _TD_QTR))


def bmf_088_body_sma63_vs_sma252(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 63-day body SMA to 252-day body SMA (medium-term body trend)."""
    babs = _body_abs(close, open)
    return _safe_div(_rolling_mean(babs, _TD_QTR), _rolling_mean(babs, _TD_YEAR))


def bmf_089_body_ema5_vs_ema21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA body to 21-day EMA body."""
    babs = _body_abs(close, open)
    return _safe_div(_ewm_mean(babs, _TD_WEEK), _ewm_mean(babs, _TD_MON))


def bmf_090_body_above_sma21_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's absolute body > its 21-day SMA."""
    babs = _body_abs(close, open)
    return (babs > _rolling_mean(babs, _TD_MON)).astype(float)


def bmf_091_body_above_sma63_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's absolute body > its 63-day SMA."""
    babs = _body_abs(close, open)
    return (babs > _rolling_mean(babs, _TD_QTR)).astype(float)


def bmf_092_body_above_sma21_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days where body > 21-day body SMA in trailing 21 days."""
    flag = bmf_090_body_above_sma21_flag(close, open)
    return _rolling_sum(flag, _TD_MON)


def bmf_093_body_sma5_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of the 5-day body SMA within its trailing 252-day distribution."""
    babs = _body_abs(close, open)
    sma5 = _rolling_mean(babs, _TD_WEEK)
    return sma5.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def bmf_094_body_sma21_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 21-day body SMA over trailing 63 days."""
    babs = _body_abs(close, open)
    sma21 = _rolling_mean(babs, _TD_MON)
    return _linslope(sma21, _TD_QTR)


def bmf_095_body_ewm21_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 21-day EMA body over trailing 63 days."""
    babs = _body_abs(close, open)
    ema21 = _ewm_mean(babs, _TD_MON)
    return _linslope(ema21, _TD_QTR)


# --- Group J (096-105): Range-normalized body features ---

def bmf_096_body_to_range_ratio_ema21(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day EMA of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _ewm_mean(btr, _TD_MON)


def bmf_097_body_to_range_ratio_min21(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling min of body-to-range ratio (minimum fill in recent period)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _rolling_min(btr, _TD_MON)


def bmf_098_body_to_range_ratio_min63(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling min of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _rolling_min(btr, _TD_QTR)


def bmf_099_body_to_avg_range_21d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute body divided by 21-day average range (body relative to recent avg range)."""
    babs = _body_abs(close, open)
    avg_range = _rolling_mean(_range(high, low), _TD_MON)
    return _safe_div(babs, avg_range)


def bmf_100_body_to_avg_range_63d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute body divided by 63-day average range."""
    babs = _body_abs(close, open)
    avg_range = _rolling_mean(_range(high, low), _TD_QTR)
    return _safe_div(babs, avg_range)


def bmf_101_body_to_avg_range_252d(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute body divided by 252-day average range."""
    babs = _body_abs(close, open)
    avg_range = _rolling_mean(_range(high, low), _TD_YEAR)
    return _safe_div(babs, avg_range)


def bmf_102_range_sma21(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of bar range (average recent volatility via range)."""
    return _rolling_mean(_range(high, low), _TD_MON)


def bmf_103_range_sma63(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day SMA of bar range."""
    return _rolling_mean(_range(high, low), _TD_QTR)


def bmf_104_body_to_range_q10_63d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """10th percentile of body-to-range ratio over 63 days (how often bars are doji-like)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _rolling_quantile(btr, _TD_QTR, 0.10)


def bmf_105_body_to_range_q90_63d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """90th percentile of body-to-range ratio over 63 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _rolling_quantile(btr, _TD_QTR, 0.90)


# --- Group K (106-115): Body asymmetry — bull vs bear body size comparisons ---

def bmf_106_avg_bull_body_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average absolute body size on bull-body days in trailing 21 days."""
    babs = _body_abs(close, open)
    bull = babs.where(close > open, np.nan)
    return bull.rolling(_TD_MON, min_periods=1).mean()


def bmf_107_avg_bear_body_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average absolute body size on bear-body days in trailing 21 days."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, np.nan)
    return bear.rolling(_TD_MON, min_periods=1).mean()


def bmf_108_avg_bull_body_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average absolute body size on bull-body days in trailing 63 days."""
    babs = _body_abs(close, open)
    bull = babs.where(close > open, np.nan)
    return bull.rolling(_TD_QTR, min_periods=1).mean()


def bmf_109_avg_bear_body_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average absolute body size on bear-body days in trailing 63 days."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, np.nan)
    return bear.rolling(_TD_QTR, min_periods=1).mean()


def bmf_110_bear_to_bull_body_size_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of avg bear body to avg bull body in 21 days (bear > 1 = bears dominate size)."""
    return _safe_div(bmf_107_avg_bear_body_21d(close, open),
                     bmf_106_avg_bull_body_21d(close, open))


def bmf_111_bear_to_bull_body_size_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of avg bear body to avg bull body in 63 days."""
    return _safe_div(bmf_109_avg_bear_body_63d(close, open),
                     bmf_108_avg_bull_body_63d(close, open))


def bmf_112_bull_body_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of bull-body sizes in trailing 21 days (total bull pressure)."""
    babs = _body_abs(close, open)
    bull = babs.where(close > open, 0.0)
    return _rolling_sum(bull, _TD_MON)


def bmf_113_bear_body_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of bear-body sizes in trailing 21 days (total bear pressure)."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    return _rolling_sum(bear, _TD_MON)


def bmf_114_net_body_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Net signed body sum over 21 days (bull minus bear body pressure)."""
    return _rolling_sum(_body(close, open), _TD_MON)


def bmf_115_bear_body_dominance_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Bear body sum as fraction of total body sum in 21 days."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    return _safe_div(_rolling_sum(bear, _TD_MON), _rolling_sum(babs, _TD_MON))


# --- Group L (116-125): Body acceleration and change metrics ---

def bmf_116_body_1d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """1-day diff of absolute body size (daily body change)."""
    return _body_abs(close, open).diff(1)


def bmf_117_body_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of absolute body size (weekly body change)."""
    return _body_abs(close, open).diff(_TD_WEEK)


def bmf_118_body_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of absolute body size (monthly body change)."""
    return _body_abs(close, open).diff(_TD_MON)


def bmf_119_body_pct_change_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day percent change of absolute body size."""
    babs = _body_abs(close, open)
    return _safe_div(babs - babs.shift(_TD_WEEK), babs.shift(_TD_WEEK).replace(0, np.nan))


def bmf_120_body_pct_change_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day percent change of absolute body size."""
    babs = _body_abs(close, open)
    return _safe_div(babs - babs.shift(_TD_MON), babs.shift(_TD_MON).replace(0, np.nan))


def bmf_121_body_range_ratio_5d_diff(close: pd.Series, open: pd.Series,
                                      high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of body-to-range ratio (change in bar fullness)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return btr.diff(_TD_WEEK)


def bmf_122_body_range_ratio_21d_diff(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return btr.diff(_TD_MON)


def bmf_123_body_expanding_zscore(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding z-score of absolute body size (how extreme vs all history)."""
    babs = _body_abs(close, open)
    m = babs.expanding(min_periods=10).mean()
    s = babs.expanding(min_periods=10).std()
    return _safe_div(babs - m, s)


def bmf_124_body_sma21_vs_expanding_mean(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day body SMA relative to all-time expanding mean of body size."""
    babs = _body_abs(close, open)
    sma21 = _rolling_mean(babs, _TD_MON)
    exp_mean = babs.expanding(min_periods=5).mean()
    return _safe_div(sma21, exp_mean)


def bmf_125_body_abs_acceleration(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second difference of absolute body size (body acceleration)."""
    babs = _body_abs(close, open)
    return babs.diff(1).diff(1)


# --- Group M (126-135): Additional body-direction run and sign statistics ---

def bmf_126_bull_body_fraction_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bull-body bars in trailing 252 days."""
    cnt = _rolling_sum((close > open).astype(float), _TD_YEAR)
    return _safe_div(cnt, pd.Series(_TD_YEAR, index=close.index, dtype=float))


def bmf_127_bull_bear_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of bull-body count to bear-body count in trailing 63 days."""
    bull = _rolling_sum((close > open).astype(float), _TD_QTR)
    bear = _rolling_sum((close < open).astype(float), _TD_QTR)
    return _safe_div(bull, bear)


def bmf_128_bull_bear_ratio_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of bull to bear body count in 252 days."""
    bull = _rolling_sum((close > open).astype(float), _TD_YEAR)
    bear = _rolling_sum((close < open).astype(float), _TD_YEAR)
    return _safe_div(bull, bear)


def bmf_129_max_consec_bull_body_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive bull-body run within trailing 63 days."""
    cond = close > open
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def bmf_130_max_consec_bear_body_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive bear-body run within trailing 252 days."""
    cond = close < open
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def bmf_131_bear_body_streak_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive bear-body streak normalized by 252-day avg streak."""
    streak = _consec_streak(close < open)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def bmf_132_body_sign_change_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of body sign changes (bull-to-bear or bear-to-bull) in 21 days."""
    sign = np.sign(_body(close, open))
    changed = (sign != sign.shift(1)).astype(float)
    return _rolling_sum(changed, _TD_MON)


def bmf_133_body_sign_change_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of body sign changes in trailing 63 days."""
    sign = np.sign(_body(close, open))
    changed = (sign != sign.shift(1)).astype(float)
    return _rolling_sum(changed, _TD_QTR)


def bmf_134_bear_body_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of bear-body count in trailing 252 days (expanding)."""
    bear_cnt = _rolling_sum((close < open).astype(float), _TD_YEAR)
    return bear_cnt.expanding(min_periods=5).rank(pct=True)


def bmf_135_alternating_body_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's body direction is opposite to prior day (alternating pattern)."""
    sign = np.sign(_body(close, open))
    return (sign * sign.shift(1) < 0).astype(float)


# --- Group N (136-150): Multi-window structural aggregates and composite measures ---

def bmf_136_body_sum_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of absolute bodies over trailing 5 days."""
    return _rolling_sum(_body_abs(close, open), _TD_WEEK)


def bmf_137_body_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of absolute bodies over trailing 21 days."""
    return _rolling_sum(_body_abs(close, open), _TD_MON)


def bmf_138_body_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of absolute bodies over trailing 63 days."""
    return _rolling_sum(_body_abs(close, open), _TD_QTR)


def bmf_139_body_sum_to_range_sum_21d(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of summed bodies to summed ranges over 21 days."""
    return _safe_div(
        _rolling_sum(_body_abs(close, open), _TD_MON),
        _rolling_sum(_range(high, low), _TD_MON),
    )


def bmf_140_body_sum_to_range_sum_63d(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of summed bodies to summed ranges over 63 days."""
    return _safe_div(
        _rolling_sum(_body_abs(close, open), _TD_QTR),
        _rolling_sum(_range(high, low), _TD_QTR),
    )


def bmf_141_body_energy_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of squared absolute body sizes over 21 days (energy metric)."""
    return _rolling_sum(_body_abs(close, open) ** 2, _TD_MON)


def bmf_142_body_energy_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of squared absolute body sizes over 63 days."""
    return _rolling_sum(_body_abs(close, open) ** 2, _TD_QTR)


def bmf_143_body_range_corr_63d(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling correlation between body size and range."""
    babs = _body_abs(close, open)
    rng = _range(high, low)
    return babs.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).corr(rng)


def bmf_144_body_range_corr_252d(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling correlation between body size and range."""
    babs = _body_abs(close, open)
    rng = _range(high, low)
    return babs.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).corr(rng)


def bmf_145_bear_body_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of bear-body sizes over 63 days."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    return _rolling_sum(bear, _TD_QTR)


def bmf_146_bear_body_dominance_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Bear body sum as fraction of total body sum in 63 days."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    return _safe_div(_rolling_sum(bear, _TD_QTR), _rolling_sum(babs, _TD_QTR))


def bmf_147_net_body_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Net signed body sum over 63 days."""
    return _rolling_sum(_body(close, open), _TD_QTR)


def bmf_148_body_to_range_ratio_slope_63d(close: pd.Series, open: pd.Series,
                                           high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of body-to-range ratio over trailing 63 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _linslope(btr, _TD_QTR)


def bmf_149_body_sma21_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day body SMA within its trailing 252-day distribution."""
    sma21 = _rolling_mean(_body_abs(close, open), _TD_MON)
    return sma21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def bmf_150_body_composite_score_21d(close: pd.Series, open: pd.Series,
                                      high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite body score: z-scored body size + body-to-range ratio, 21-day window."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    body_z = _safe_div(babs - m, s)
    btr = _safe_div(babs, _range(high, low))
    btr_z = _safe_div(btr - _rolling_mean(btr, _TD_MON), _rolling_std(btr, _TD_MON))
    return (body_z.fillna(0.0) + btr_z.fillna(0.0)) / 2.0


# ── Registry ──────────────────────────────────────────────────────────────────

BAR_MORPHOLOGY_REGISTRY_076_150 = {
    "bmf_076_body_skew_63d": {"inputs": ["close", "open"], "func": bmf_076_body_skew_63d},
    "bmf_077_body_skew_252d": {"inputs": ["close", "open"], "func": bmf_077_body_skew_252d},
    "bmf_078_signed_body_skew_63d": {"inputs": ["close", "open"], "func": bmf_078_signed_body_skew_63d},
    "bmf_079_body_q90_63d": {"inputs": ["close", "open"], "func": bmf_079_body_q90_63d},
    "bmf_080_body_q10_63d": {"inputs": ["close", "open"], "func": bmf_080_body_q10_63d},
    "bmf_081_body_q90_to_q10_ratio_63d": {"inputs": ["close", "open"], "func": bmf_081_body_q90_to_q10_ratio_63d},
    "bmf_082_body_q75_63d": {"inputs": ["close", "open"], "func": bmf_082_body_q75_63d},
    "bmf_083_body_q25_63d": {"inputs": ["close", "open"], "func": bmf_083_body_q25_63d},
    "bmf_084_body_above_q75_flag": {"inputs": ["close", "open"], "func": bmf_084_body_above_q75_flag},
    "bmf_085_body_below_q25_flag": {"inputs": ["close", "open"], "func": bmf_085_body_below_q25_flag},
    "bmf_086_body_sma5_vs_sma21": {"inputs": ["close", "open"], "func": bmf_086_body_sma5_vs_sma21},
    "bmf_087_body_sma21_vs_sma63": {"inputs": ["close", "open"], "func": bmf_087_body_sma21_vs_sma63},
    "bmf_088_body_sma63_vs_sma252": {"inputs": ["close", "open"], "func": bmf_088_body_sma63_vs_sma252},
    "bmf_089_body_ema5_vs_ema21": {"inputs": ["close", "open"], "func": bmf_089_body_ema5_vs_ema21},
    "bmf_090_body_above_sma21_flag": {"inputs": ["close", "open"], "func": bmf_090_body_above_sma21_flag},
    "bmf_091_body_above_sma63_flag": {"inputs": ["close", "open"], "func": bmf_091_body_above_sma63_flag},
    "bmf_092_body_above_sma21_count_21d": {"inputs": ["close", "open"], "func": bmf_092_body_above_sma21_count_21d},
    "bmf_093_body_sma5_pct_rank_252d": {"inputs": ["close", "open"], "func": bmf_093_body_sma5_pct_rank_252d},
    "bmf_094_body_sma21_slope": {"inputs": ["close", "open"], "func": bmf_094_body_sma21_slope},
    "bmf_095_body_ewm21_slope": {"inputs": ["close", "open"], "func": bmf_095_body_ewm21_slope},
    "bmf_096_body_to_range_ratio_ema21": {"inputs": ["close", "open", "high", "low"], "func": bmf_096_body_to_range_ratio_ema21},
    "bmf_097_body_to_range_ratio_min21": {"inputs": ["close", "open", "high", "low"], "func": bmf_097_body_to_range_ratio_min21},
    "bmf_098_body_to_range_ratio_min63": {"inputs": ["close", "open", "high", "low"], "func": bmf_098_body_to_range_ratio_min63},
    "bmf_099_body_to_avg_range_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_099_body_to_avg_range_21d},
    "bmf_100_body_to_avg_range_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_100_body_to_avg_range_63d},
    "bmf_101_body_to_avg_range_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_101_body_to_avg_range_252d},
    "bmf_102_range_sma21": {"inputs": ["high", "low"], "func": bmf_102_range_sma21},
    "bmf_103_range_sma63": {"inputs": ["high", "low"], "func": bmf_103_range_sma63},
    "bmf_104_body_to_range_q10_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_104_body_to_range_q10_63d},
    "bmf_105_body_to_range_q90_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_105_body_to_range_q90_63d},
    "bmf_106_avg_bull_body_21d": {"inputs": ["close", "open"], "func": bmf_106_avg_bull_body_21d},
    "bmf_107_avg_bear_body_21d": {"inputs": ["close", "open"], "func": bmf_107_avg_bear_body_21d},
    "bmf_108_avg_bull_body_63d": {"inputs": ["close", "open"], "func": bmf_108_avg_bull_body_63d},
    "bmf_109_avg_bear_body_63d": {"inputs": ["close", "open"], "func": bmf_109_avg_bear_body_63d},
    "bmf_110_bear_to_bull_body_size_ratio_21d": {"inputs": ["close", "open"], "func": bmf_110_bear_to_bull_body_size_ratio_21d},
    "bmf_111_bear_to_bull_body_size_ratio_63d": {"inputs": ["close", "open"], "func": bmf_111_bear_to_bull_body_size_ratio_63d},
    "bmf_112_bull_body_sum_21d": {"inputs": ["close", "open"], "func": bmf_112_bull_body_sum_21d},
    "bmf_113_bear_body_sum_21d": {"inputs": ["close", "open"], "func": bmf_113_bear_body_sum_21d},
    "bmf_114_net_body_sum_21d": {"inputs": ["close", "open"], "func": bmf_114_net_body_sum_21d},
    "bmf_115_bear_body_dominance_21d": {"inputs": ["close", "open"], "func": bmf_115_bear_body_dominance_21d},
    "bmf_116_body_1d_diff": {"inputs": ["close", "open"], "func": bmf_116_body_1d_diff},
    "bmf_117_body_5d_diff": {"inputs": ["close", "open"], "func": bmf_117_body_5d_diff},
    "bmf_118_body_21d_diff": {"inputs": ["close", "open"], "func": bmf_118_body_21d_diff},
    "bmf_119_body_pct_change_5d": {"inputs": ["close", "open"], "func": bmf_119_body_pct_change_5d},
    "bmf_120_body_pct_change_21d": {"inputs": ["close", "open"], "func": bmf_120_body_pct_change_21d},
    "bmf_121_body_range_ratio_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_121_body_range_ratio_5d_diff},
    "bmf_122_body_range_ratio_21d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_122_body_range_ratio_21d_diff},
    "bmf_123_body_expanding_zscore": {"inputs": ["close", "open"], "func": bmf_123_body_expanding_zscore},
    "bmf_124_body_sma21_vs_expanding_mean": {"inputs": ["close", "open"], "func": bmf_124_body_sma21_vs_expanding_mean},
    "bmf_125_body_abs_acceleration": {"inputs": ["close", "open"], "func": bmf_125_body_abs_acceleration},
    "bmf_126_bull_body_fraction_252d": {"inputs": ["close", "open"], "func": bmf_126_bull_body_fraction_252d},
    "bmf_127_bull_bear_ratio_63d": {"inputs": ["close", "open"], "func": bmf_127_bull_bear_ratio_63d},
    "bmf_128_bull_bear_ratio_252d": {"inputs": ["close", "open"], "func": bmf_128_bull_bear_ratio_252d},
    "bmf_129_max_consec_bull_body_63d": {"inputs": ["close", "open"], "func": bmf_129_max_consec_bull_body_63d},
    "bmf_130_max_consec_bear_body_252d": {"inputs": ["close", "open"], "func": bmf_130_max_consec_bear_body_252d},
    "bmf_131_bear_body_streak_norm_252d": {"inputs": ["close", "open"], "func": bmf_131_bear_body_streak_norm_252d},
    "bmf_132_body_sign_change_count_21d": {"inputs": ["close", "open"], "func": bmf_132_body_sign_change_count_21d},
    "bmf_133_body_sign_change_count_63d": {"inputs": ["close", "open"], "func": bmf_133_body_sign_change_count_63d},
    "bmf_134_bear_body_pct_rank_252d": {"inputs": ["close", "open"], "func": bmf_134_bear_body_pct_rank_252d},
    "bmf_135_alternating_body_flag": {"inputs": ["close", "open"], "func": bmf_135_alternating_body_flag},
    "bmf_136_body_sum_5d": {"inputs": ["close", "open"], "func": bmf_136_body_sum_5d},
    "bmf_137_body_sum_21d": {"inputs": ["close", "open"], "func": bmf_137_body_sum_21d},
    "bmf_138_body_sum_63d": {"inputs": ["close", "open"], "func": bmf_138_body_sum_63d},
    "bmf_139_body_sum_to_range_sum_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_139_body_sum_to_range_sum_21d},
    "bmf_140_body_sum_to_range_sum_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_140_body_sum_to_range_sum_63d},
    "bmf_141_body_energy_21d": {"inputs": ["close", "open"], "func": bmf_141_body_energy_21d},
    "bmf_142_body_energy_63d": {"inputs": ["close", "open"], "func": bmf_142_body_energy_63d},
    "bmf_143_body_range_corr_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_143_body_range_corr_63d},
    "bmf_144_body_range_corr_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_144_body_range_corr_252d},
    "bmf_145_bear_body_sum_63d": {"inputs": ["close", "open"], "func": bmf_145_bear_body_sum_63d},
    "bmf_146_bear_body_dominance_63d": {"inputs": ["close", "open"], "func": bmf_146_bear_body_dominance_63d},
    "bmf_147_net_body_sum_63d": {"inputs": ["close", "open"], "func": bmf_147_net_body_sum_63d},
    "bmf_148_body_to_range_ratio_slope_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_148_body_to_range_ratio_slope_63d},
    "bmf_149_body_sma21_pct_rank_252d": {"inputs": ["close", "open"], "func": bmf_149_body_sma21_pct_rank_252d},
    "bmf_150_body_composite_score_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_150_body_composite_score_21d},
}
