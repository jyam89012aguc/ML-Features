"""
53_liquidity_collapse — Base Features 076-150
Domain: illiquidity spikes — Amihud multi-window, high-low spread proxy,
  illiquidity vs trailing baseline, combined estimators, price-impact signals
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — liquidity drying up / price-impact spikes
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
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Rolling z-score of s over window w."""
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _amihud(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity: |ret| / dollar_volume."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c      = cond.astype(int)
    group  = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _roll_spread(close: pd.Series) -> pd.Series:
    """Roll (1984) effective spread proxy: 2*sqrt(max(-cov(dP_t, dP_{t-1}), 0))."""
    dp  = close.diff(1)
    cov = dp.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _cs_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) bid-ask spread estimator."""
    ln_hl  = _log_safe(high) - _log_safe(low)
    beta   = ln_hl ** 2 + (ln_hl.shift(1)) ** 2
    h2     = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2     = pd.concat([low,  low.shift(1)],  axis=1).min(axis=1)
    gamma  = (_log_safe(h2) - _log_safe(l2)) ** 2
    k      = 3.0 - 2.0 * np.sqrt(2.0)
    alpha  = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    spread = (2.0 * (np.exp(alpha) - 1.0)) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def _hl_spread_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High-low spread proxy: (H-L)/close — simple intraday range as illiq proxy."""
    return _safe_div(high - low, close)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Amihud across multi-window ratios and relative metrics ---

def lqc_076_amihud_5d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day Amihud mean to 252-day Amihud mean (short vs long illiq)."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_mean(ami, _TD_WEEK), _rolling_mean(ami, _TD_YEAR))


def lqc_077_amihud_21d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day Amihud mean to 252-day Amihud mean."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_mean(ami, _TD_MON), _rolling_mean(ami, _TD_YEAR))


def lqc_078_amihud_63d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day Amihud mean to 252-day Amihud mean."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_mean(ami, _TD_QTR), _rolling_mean(ami, _TD_YEAR))


def lqc_079_amihud_21d_vs_126d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day Amihud mean to 126-day Amihud mean."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_mean(ami, _TD_MON), _rolling_mean(ami, _TD_HALF))


def lqc_080_amihud_5d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day Amihud mean within trailing 252-day distribution of 5d means."""
    ami   = _amihud(close, volume)
    mean5 = _rolling_mean(ami, _TD_WEEK)
    return _zscore(mean5, _TD_YEAR)


def lqc_081_amihud_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day Amihud mean within trailing 252-day distribution."""
    ami    = _amihud(close, volume)
    mean21 = _rolling_mean(ami, _TD_MON)
    return _zscore(mean21, _TD_YEAR)


def lqc_082_amihud_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day Amihud mean within trailing 252-day distribution."""
    ami    = _amihud(close, volume)
    mean63 = _rolling_mean(ami, _TD_QTR)
    return _zscore(mean63, _TD_YEAR)


def lqc_083_amihud_median_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling median Amihud (robust central tendency of illiquidity)."""
    return _rolling_median(_amihud(close, volume), _TD_MON)


def lqc_084_amihud_median_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling median Amihud."""
    return _rolling_median(_amihud(close, volume), _TD_QTR)


def lqc_085_amihud_mean_minus_median_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean minus median Amihud over 21 days (skewness proxy for spike frequency)."""
    ami = _amihud(close, volume)
    return _rolling_mean(ami, _TD_MON) - _rolling_median(ami, _TD_MON)


def lqc_086_amihud_coef_var_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of Amihud over 63 days."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_std(ami, _TD_QTR), _rolling_mean(ami, _TD_QTR))


def lqc_087_amihud_coef_var_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of Amihud over 252 days."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_std(ami, _TD_YEAR), _rolling_mean(ami, _TD_YEAR))


def lqc_088_amihud_ewm_ratio_21_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(21) Amihud divided by EWM(63) Amihud (fast vs slow smoothed illiq)."""
    ami = _amihud(close, volume)
    return _safe_div(_ewm_mean(ami, _TD_MON), _ewm_mean(ami, _TD_QTR))


def lqc_089_amihud_ewm_ratio_5_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(5) Amihud divided by EWM(21) Amihud (very short vs monthly illiq)."""
    ami = _amihud(close, volume)
    return _safe_div(_ewm_mean(ami, _TD_WEEK), _ewm_mean(ami, _TD_MON))


def lqc_090_amihud_roll_std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling std of Amihud ratio (instability of illiquidity level)."""
    return _rolling_std(_amihud(close, volume), _TD_MON)


# --- Group I (091-105): Amihud vs baseline and trend signals ---

def lqc_091_amihud_vs_1yr_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud minus its 252-day mean (deviation from annual baseline)."""
    ami = _amihud(close, volume)
    return ami - _rolling_mean(ami, _TD_YEAR)


def lqc_092_amihud_vs_halfyr_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud minus its 126-day mean."""
    ami = _amihud(close, volume)
    return ami - _rolling_mean(ami, _TD_HALF)


def lqc_093_amihud_vs_qtr_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud minus its 63-day mean."""
    ami = _amihud(close, volume)
    return ami - _rolling_mean(ami, _TD_QTR)


def lqc_094_amihud_expanding_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding historical maximum Amihud (all-time illiquidity record)."""
    return _amihud(close, volume).expanding(min_periods=1).max()


def lqc_095_amihud_vs_expanding_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud as fraction of its expanding all-time maximum."""
    ami = _amihud(close, volume)
    return _safe_div(ami, ami.expanding(min_periods=1).max())


def lqc_096_amihud_21d_mean_vs_expanding_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day Amihud mean divided by expanding all-history mean."""
    ami = _amihud(close, volume)
    return _safe_div(_rolling_mean(ami, _TD_MON), ami.expanding(min_periods=1).mean())


def lqc_097_amihud_trend_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day difference of Amihud ratio (short-run trend in illiquidity)."""
    return _amihud(close, volume).diff(_TD_WEEK)


def lqc_098_amihud_trend_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day difference of Amihud ratio (monthly trend in illiquidity)."""
    return _amihud(close, volume).diff(_TD_MON)


def lqc_099_amihud_trend_63d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day difference of Amihud ratio (quarterly trend in illiquidity)."""
    return _amihud(close, volume).diff(_TD_QTR)


def lqc_100_amihud_5d_diff_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day Amihud change within trailing 63-day distribution."""
    return _zscore(_amihud(close, volume).diff(_TD_WEEK), _TD_QTR)


def lqc_101_amihud_21d_diff_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day Amihud change within trailing 252-day distribution."""
    return _zscore(_amihud(close, volume).diff(_TD_MON), _TD_YEAR)


def lqc_102_amihud_21d_mean_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Amihud mean within trailing 252 days."""
    mean21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    return _pct_rank(mean21, _TD_YEAR)


def lqc_103_amihud_above_prior_yr_high_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud exceeds the prior-252d maximum (new all-time illiq high)."""
    ami    = _amihud(close, volume)
    prior_max = ami.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return (ami > prior_max).astype(float)


def lqc_104_amihud_5d_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rolling sum of Amihud (accumulated illiquidity over a week)."""
    return _rolling_sum(_amihud(close, volume), _TD_WEEK)


def lqc_105_amihud_21d_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling sum of Amihud (accumulated illiquidity over a month)."""
    return _rolling_sum(_amihud(close, volume), _TD_MON)


# --- Group J (106-115): High-low spread proxy as illiquidity measure ---

def lqc_106_hl_spread_proxy_daily(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday high-low range / close (simple illiquidity proxy via price range)."""
    return _hl_spread_proxy(high, low, close)


def lqc_107_hl_spread_proxy_mean_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling mean of the high-low spread proxy."""
    return _rolling_mean(_hl_spread_proxy(high, low, close), _TD_WEEK)


def lqc_108_hl_spread_proxy_mean_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of the high-low spread proxy."""
    return _rolling_mean(_hl_spread_proxy(high, low, close), _TD_MON)


def lqc_109_hl_spread_proxy_mean_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of the high-low spread proxy."""
    return _rolling_mean(_hl_spread_proxy(high, low, close), _TD_QTR)


def lqc_110_hl_spread_proxy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of high-low spread proxy within trailing 63-day window."""
    return _zscore(_hl_spread_proxy(high, low, close), _TD_QTR)


def lqc_111_hl_spread_proxy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of high-low spread proxy within trailing 252-day window."""
    return _zscore(_hl_spread_proxy(high, low, close), _TD_YEAR)


def lqc_112_hl_spread_proxy_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of high-low spread proxy within trailing 252 days."""
    return _pct_rank(_hl_spread_proxy(high, low, close), _TD_YEAR)


def lqc_113_hl_spread_proxy_spike_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """High-low spread proxy divided by its 63-day mean (relative spike magnitude)."""
    hl = _hl_spread_proxy(high, low, close)
    return _safe_div(hl, _rolling_mean(hl, _TD_QTR))


def lqc_114_hl_spread_above_mean_streak_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where high-low spread proxy exceeds its 21-day mean."""
    hl   = _hl_spread_proxy(high, low, close)
    cond = hl > _rolling_mean(hl, _TD_MON)
    return _consec_streak(cond)


def lqc_115_hl_spread_vs_amihud_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation of high-low spread proxy with Amihud over trailing 21 days."""
    hl  = _hl_spread_proxy(high, low, close)
    ami = _amihud(close, volume)
    return hl.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).corr(ami)


# --- Group K (116-125): Combined illiquidity composite signals ---

def lqc_116_illiq_composite_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of Amihud z-score + C-S spread z-score + Roll spread z-score (21d)."""
    az = _zscore(_amihud(close, volume), _TD_MON)
    cz = _zscore(_cs_spread(high, low, close), _TD_MON)
    rz = _zscore(_roll_spread(close), _TD_MON)
    return (az + cz + rz) / 3.0


def lqc_117_illiq_composite_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of Amihud + C-S + Roll spread z-scores over 63-day window."""
    az = _zscore(_amihud(close, volume), _TD_QTR)
    cz = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz = _zscore(_roll_spread(close), _TD_QTR)
    return (az + cz + rz) / 3.0


def lqc_118_illiq_composite_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of composite (Amihud + C-S + HL proxy) within 252 days."""
    ami = _amihud(close, volume)
    cs  = _cs_spread(high, low, close)
    hl  = _hl_spread_proxy(high, low, close)
    composite = (_zscore(ami, _TD_YEAR) + _zscore(cs, _TD_YEAR) + _zscore(hl, _TD_YEAR)) / 3.0
    return _pct_rank(composite, _TD_YEAR)


def lqc_119_amihud_cs_spread_product(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of Amihud z-score and C-S spread z-score (concurrent spike amplification)."""
    az = _zscore(_amihud(close, volume), _TD_QTR)
    cz = _zscore(_cs_spread(high, low, close), _TD_QTR)
    return az * cz


def lqc_120_amihud_roll_spread_product(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of Amihud z-score and Roll spread z-score."""
    az = _zscore(_amihud(close, volume), _TD_QTR)
    rz = _zscore(_roll_spread(close), _TD_QTR)
    return az * rz


def lqc_121_illiq_all_spike_flag(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: all three estimators (Amihud, C-S, Roll) simultaneously above their 63d mean."""
    ami  = _amihud(close, volume)
    cs   = _cs_spread(high, low, close)
    rs   = _roll_spread(close)
    cond = ((ami > _rolling_mean(ami, _TD_QTR)) &
            (cs  > _rolling_mean(cs,  _TD_QTR)) &
            (rs  > _rolling_mean(rs,  _TD_QTR)))
    return cond.astype(float)


def lqc_122_illiq_all_spike_streak(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where all three illiquidity estimators exceed their 63d mean."""
    ami  = _amihud(close, volume)
    cs   = _cs_spread(high, low, close)
    rs   = _roll_spread(close)
    cond = ((ami > _rolling_mean(ami, _TD_QTR)) &
            (cs  > _rolling_mean(cs,  _TD_QTR)) &
            (rs  > _rolling_mean(rs,  _TD_QTR)))
    return _consec_streak(cond)


def lqc_123_illiq_composite_vs_1yr_baseline(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite z-score (21d) minus its 252-day mean (regime-relative illiquidity)."""
    az = _zscore(_amihud(close, volume), _TD_MON)
    cz = _zscore(_cs_spread(high, low, close), _TD_MON)
    rz = _zscore(_roll_spread(close), _TD_MON)
    comp = (az + cz + rz) / 3.0
    return comp - _rolling_mean(comp, _TD_YEAR)


def lqc_124_amihud_hl_corr_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling correlation of Amihud with high-low spread proxy."""
    ami = _amihud(close, volume)
    hl  = _hl_spread_proxy(high, low, close)
    return ami.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).corr(hl)


def lqc_125_cs_roll_spread_corr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day correlation of Corwin-Schultz spread with Roll spread."""
    cs = _cs_spread(high, low, close)
    rs = _roll_spread(close)
    return cs.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(rs)


# --- Group L (126-135): Price-impact and illiquidity percentile signals ---

def lqc_126_price_impact_per_dollar_vol_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day sum of |ret| / 5-day sum of dollar-volume (5d price-impact ratio)."""
    ret_abs = close.pct_change(1).abs()
    dolvol  = close * volume
    return _safe_div(_rolling_sum(ret_abs, _TD_WEEK), _rolling_sum(dolvol, _TD_WEEK))


def lqc_127_price_impact_per_dollar_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day accumulated price-impact ratio (sum |ret| / sum dollar-vol)."""
    ret_abs = close.pct_change(1).abs()
    dolvol  = close * volume
    return _safe_div(_rolling_sum(ret_abs, _TD_MON), _rolling_sum(dolvol, _TD_MON))


def lqc_128_price_impact_per_dollar_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day accumulated price-impact ratio."""
    ret_abs = close.pct_change(1).abs()
    dolvol  = close * volume
    return _safe_div(_rolling_sum(ret_abs, _TD_QTR), _rolling_sum(dolvol, _TD_QTR))


def lqc_129_price_impact_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily price-impact ratio within trailing 63 days."""
    ret_abs = close.pct_change(1).abs()
    dolvol  = close * volume
    pi      = _safe_div(ret_abs, dolvol)
    return _zscore(pi, _TD_QTR)


def lqc_130_price_impact_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily price-impact ratio within trailing 252 days."""
    ret_abs = close.pct_change(1).abs()
    dolvol  = close * volume
    pi      = _safe_div(ret_abs, dolvol)
    return _zscore(pi, _TD_YEAR)


def lqc_131_amihud_log_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log(1+Amihud*1e6) within trailing 252-day window."""
    log_ami = np.log1p(_amihud(close, volume) * 1e6)
    return _zscore(log_ami, _TD_YEAR)


def lqc_132_amihud_log_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of log Amihud within trailing 252 days."""
    log_ami = np.log1p(_amihud(close, volume) * 1e6)
    return _pct_rank(log_ami, _TD_YEAR)


def lqc_133_amihud_gt_90pct_consec_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive days above 90th percentile Amihud within trailing 252 days."""
    ami  = _amihud(close, volume)
    p90  = ami.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    cond = ami > p90
    return _rolling_max_streak(cond, _TD_YEAR)


def lqc_134_amihud_gt_95pct_consec_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive days above 95th percentile Amihud within trailing 252 days."""
    ami  = _amihud(close, volume)
    p95  = ami.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    cond = ami > p95
    return _rolling_max_streak(cond, _TD_YEAR)


def lqc_135_amihud_above_2x_baseline_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud more than 2x its 252-day rolling mean (doubling of illiq)."""
    ami = _amihud(close, volume)
    mu  = _rolling_mean(ami, _TD_YEAR)
    return (ami > 2.0 * mu).astype(float)


# --- Group M (136-143): Corwin-Schultz extended metrics ---

def lqc_136_cs_spread_max_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling maximum Corwin-Schultz spread (worst bid-ask in month)."""
    return _rolling_max(_cs_spread(high, low, close), _TD_MON)


def lqc_137_cs_spread_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling maximum Corwin-Schultz spread."""
    return _rolling_max(_cs_spread(high, low, close), _TD_QTR)


def lqc_138_cs_spread_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of Corwin-Schultz spread."""
    return _cs_spread(high, low, close).expanding(min_periods=5).rank(pct=True)


def lqc_139_cs_spread_ewm_ratio_5_21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM(5) C-S spread divided by EWM(21) C-S spread (fast vs monthly spread)."""
    cs = _cs_spread(high, low, close)
    return _safe_div(_ewm_mean(cs, _TD_WEEK), _ewm_mean(cs, _TD_MON))


def lqc_140_cs_spread_gt2x_252d_mean_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: C-S spread > 2x its 252-day mean (severe bid-ask widening)."""
    cs = _cs_spread(high, low, close)
    mu = _rolling_mean(cs, _TD_YEAR)
    return (cs > 2.0 * mu).astype(float)


def lqc_141_cs_spread_21d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day C-S spread mean within trailing 252-day distribution."""
    cs     = _cs_spread(high, low, close)
    mean21 = _rolling_mean(cs, _TD_MON)
    return _pct_rank(mean21, _TD_YEAR)


def lqc_142_cs_spread_price_fall_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: C-S spread above 63d mean AND close below prior close simultaneously."""
    cs   = _cs_spread(high, low, close)
    mu   = _rolling_mean(cs, _TD_QTR)
    cond = (cs > mu) & (close < close.shift(1))
    return cond.astype(float)


def lqc_143_cs_spread_price_fall_consec(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days of C-S spread above 63d mean and simultaneous price decline."""
    cs   = _cs_spread(high, low, close)
    mu   = _rolling_mean(cs, _TD_QTR)
    cond = (cs > mu) & (close < close.shift(1))
    return _consec_streak(cond)


# --- Group N (144-150): Roll spread extended + final illiquidity signals ---

def lqc_144_roll_spread_max_63d(close: pd.Series) -> pd.Series:
    """63-day rolling maximum of Roll spread estimate."""
    return _rolling_max(_roll_spread(close), _TD_QTR)


def lqc_145_roll_spread_ewm_ratio_5_63(close: pd.Series) -> pd.Series:
    """EWM(5) Roll spread divided by EWM(63) Roll spread (ultra-short vs quarterly)."""
    rs = _roll_spread(close)
    return _safe_div(_ewm_mean(rs, _TD_WEEK), _ewm_mean(rs, _TD_QTR))


def lqc_146_roll_spread_gt2x_252d_mean_flag(close: pd.Series) -> pd.Series:
    """Flag: Roll spread > 2x its 252-day mean (severe effective-spread widening)."""
    rs = _roll_spread(close)
    mu = _rolling_mean(rs, _TD_YEAR)
    return (rs > 2.0 * mu).astype(float)


def lqc_147_amihud_cs_joint_spike_flag(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: Amihud zscore(63d)>2 AND C-S spread zscore(63d)>2 simultaneously."""
    az = _zscore(_amihud(close, volume), _TD_QTR)
    cz = _zscore(_cs_spread(high, low, close), _TD_QTR)
    return ((az > 2.0) & (cz > 2.0)).astype(float)


def lqc_148_amihud_cs_joint_spike_consec(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days of joint Amihud + C-S spread spike (both z>2 over 63d)."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    cond = (az > 2.0) & (cz > 2.0)
    return _consec_streak(cond)


def lqc_149_illiq_composite_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of composite illiquidity z-score (63d)."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz   = _zscore(_roll_spread(close), _TD_QTR)
    comp = (az + cz + rz) / 3.0
    return comp.expanding(min_periods=5).rank(pct=True)


def lqc_150_amihud_log_diff_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day change in log Amihud within trailing 252-day window."""
    log_ami = np.log1p(_amihud(close, volume) * 1e6)
    return _zscore(log_ami.diff(_TD_MON), _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

def _roll_spread(close: pd.Series) -> pd.Series:
    dp  = close.diff(1)
    cov = dp.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _cs_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ln_hl  = _log_safe(high) - _log_safe(low)
    beta   = ln_hl ** 2 + (ln_hl.shift(1)) ** 2
    h2     = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2     = pd.concat([low,  low.shift(1)],  axis=1).min(axis=1)
    gamma  = (_log_safe(h2) - _log_safe(l2)) ** 2
    k      = 3.0 - 2.0 * np.sqrt(2.0)
    alpha  = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    spread = (2.0 * (np.exp(alpha) - 1.0)) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def _hl_spread_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high - low, close)


LIQUIDITY_COLLAPSE_REGISTRY_076_150 = {
    "lqc_076_amihud_5d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": lqc_076_amihud_5d_vs_252d_ratio},
    "lqc_077_amihud_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": lqc_077_amihud_21d_vs_252d_ratio},
    "lqc_078_amihud_63d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": lqc_078_amihud_63d_vs_252d_ratio},
    "lqc_079_amihud_21d_vs_126d_ratio": {"inputs": ["close", "volume"], "func": lqc_079_amihud_21d_vs_126d_ratio},
    "lqc_080_amihud_5d_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_080_amihud_5d_zscore_252d},
    "lqc_081_amihud_21d_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_081_amihud_21d_zscore_252d},
    "lqc_082_amihud_63d_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_082_amihud_63d_zscore_252d},
    "lqc_083_amihud_median_21d": {"inputs": ["close", "volume"], "func": lqc_083_amihud_median_21d},
    "lqc_084_amihud_median_63d": {"inputs": ["close", "volume"], "func": lqc_084_amihud_median_63d},
    "lqc_085_amihud_mean_minus_median_21d": {"inputs": ["close", "volume"], "func": lqc_085_amihud_mean_minus_median_21d},
    "lqc_086_amihud_coef_var_63d": {"inputs": ["close", "volume"], "func": lqc_086_amihud_coef_var_63d},
    "lqc_087_amihud_coef_var_252d": {"inputs": ["close", "volume"], "func": lqc_087_amihud_coef_var_252d},
    "lqc_088_amihud_ewm_ratio_21_63": {"inputs": ["close", "volume"], "func": lqc_088_amihud_ewm_ratio_21_63},
    "lqc_089_amihud_ewm_ratio_5_21": {"inputs": ["close", "volume"], "func": lqc_089_amihud_ewm_ratio_5_21},
    "lqc_090_amihud_roll_std_21d": {"inputs": ["close", "volume"], "func": lqc_090_amihud_roll_std_21d},
    "lqc_091_amihud_vs_1yr_baseline": {"inputs": ["close", "volume"], "func": lqc_091_amihud_vs_1yr_baseline},
    "lqc_092_amihud_vs_halfyr_baseline": {"inputs": ["close", "volume"], "func": lqc_092_amihud_vs_halfyr_baseline},
    "lqc_093_amihud_vs_qtr_baseline": {"inputs": ["close", "volume"], "func": lqc_093_amihud_vs_qtr_baseline},
    "lqc_094_amihud_expanding_max": {"inputs": ["close", "volume"], "func": lqc_094_amihud_expanding_max},
    "lqc_095_amihud_vs_expanding_max": {"inputs": ["close", "volume"], "func": lqc_095_amihud_vs_expanding_max},
    "lqc_096_amihud_21d_mean_vs_expanding_mean": {"inputs": ["close", "volume"], "func": lqc_096_amihud_21d_mean_vs_expanding_mean},
    "lqc_097_amihud_trend_5d_diff": {"inputs": ["close", "volume"], "func": lqc_097_amihud_trend_5d_diff},
    "lqc_098_amihud_trend_21d_diff": {"inputs": ["close", "volume"], "func": lqc_098_amihud_trend_21d_diff},
    "lqc_099_amihud_trend_63d_diff": {"inputs": ["close", "volume"], "func": lqc_099_amihud_trend_63d_diff},
    "lqc_100_amihud_5d_diff_zscore_63d": {"inputs": ["close", "volume"], "func": lqc_100_amihud_5d_diff_zscore_63d},
    "lqc_101_amihud_21d_diff_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_101_amihud_21d_diff_zscore_252d},
    "lqc_102_amihud_21d_mean_pct_rank_252d": {"inputs": ["close", "volume"], "func": lqc_102_amihud_21d_mean_pct_rank_252d},
    "lqc_103_amihud_above_prior_yr_high_flag": {"inputs": ["close", "volume"], "func": lqc_103_amihud_above_prior_yr_high_flag},
    "lqc_104_amihud_5d_sum": {"inputs": ["close", "volume"], "func": lqc_104_amihud_5d_sum},
    "lqc_105_amihud_21d_sum": {"inputs": ["close", "volume"], "func": lqc_105_amihud_21d_sum},
    "lqc_106_hl_spread_proxy_daily": {"inputs": ["close", "high", "low"], "func": lqc_106_hl_spread_proxy_daily},
    "lqc_107_hl_spread_proxy_mean_5d": {"inputs": ["close", "high", "low"], "func": lqc_107_hl_spread_proxy_mean_5d},
    "lqc_108_hl_spread_proxy_mean_21d": {"inputs": ["close", "high", "low"], "func": lqc_108_hl_spread_proxy_mean_21d},
    "lqc_109_hl_spread_proxy_mean_63d": {"inputs": ["close", "high", "low"], "func": lqc_109_hl_spread_proxy_mean_63d},
    "lqc_110_hl_spread_proxy_zscore_63d": {"inputs": ["close", "high", "low"], "func": lqc_110_hl_spread_proxy_zscore_63d},
    "lqc_111_hl_spread_proxy_zscore_252d": {"inputs": ["close", "high", "low"], "func": lqc_111_hl_spread_proxy_zscore_252d},
    "lqc_112_hl_spread_proxy_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": lqc_112_hl_spread_proxy_pct_rank_252d},
    "lqc_113_hl_spread_proxy_spike_ratio_63d": {"inputs": ["close", "high", "low"], "func": lqc_113_hl_spread_proxy_spike_ratio_63d},
    "lqc_114_hl_spread_above_mean_streak_21d": {"inputs": ["close", "high", "low"], "func": lqc_114_hl_spread_above_mean_streak_21d},
    "lqc_115_hl_spread_vs_amihud_21d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_115_hl_spread_vs_amihud_21d},
    "lqc_116_illiq_composite_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_116_illiq_composite_zscore_21d},
    "lqc_117_illiq_composite_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_117_illiq_composite_zscore_63d},
    "lqc_118_illiq_composite_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_118_illiq_composite_pct_rank_252d},
    "lqc_119_amihud_cs_spread_product": {"inputs": ["close", "high", "low", "volume"], "func": lqc_119_amihud_cs_spread_product},
    "lqc_120_amihud_roll_spread_product": {"inputs": ["close", "volume"], "func": lqc_120_amihud_roll_spread_product},
    "lqc_121_illiq_all_spike_flag": {"inputs": ["close", "high", "low", "volume"], "func": lqc_121_illiq_all_spike_flag},
    "lqc_122_illiq_all_spike_streak": {"inputs": ["close", "high", "low", "volume"], "func": lqc_122_illiq_all_spike_streak},
    "lqc_123_illiq_composite_vs_1yr_baseline": {"inputs": ["close", "high", "low", "volume"], "func": lqc_123_illiq_composite_vs_1yr_baseline},
    "lqc_124_amihud_hl_corr_21d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_124_amihud_hl_corr_21d},
    "lqc_125_cs_roll_spread_corr_63d": {"inputs": ["close", "high", "low"], "func": lqc_125_cs_roll_spread_corr_63d},
    "lqc_126_price_impact_per_dollar_vol_5d": {"inputs": ["close", "volume"], "func": lqc_126_price_impact_per_dollar_vol_5d},
    "lqc_127_price_impact_per_dollar_vol_21d": {"inputs": ["close", "volume"], "func": lqc_127_price_impact_per_dollar_vol_21d},
    "lqc_128_price_impact_per_dollar_vol_63d": {"inputs": ["close", "volume"], "func": lqc_128_price_impact_per_dollar_vol_63d},
    "lqc_129_price_impact_zscore_63d": {"inputs": ["close", "volume"], "func": lqc_129_price_impact_zscore_63d},
    "lqc_130_price_impact_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_130_price_impact_zscore_252d},
    "lqc_131_amihud_log_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_131_amihud_log_zscore_252d},
    "lqc_132_amihud_log_pct_rank_252d": {"inputs": ["close", "volume"], "func": lqc_132_amihud_log_pct_rank_252d},
    "lqc_133_amihud_gt_90pct_consec_252d": {"inputs": ["close", "volume"], "func": lqc_133_amihud_gt_90pct_consec_252d},
    "lqc_134_amihud_gt_95pct_consec_252d": {"inputs": ["close", "volume"], "func": lqc_134_amihud_gt_95pct_consec_252d},
    "lqc_135_amihud_above_2x_baseline_flag": {"inputs": ["close", "volume"], "func": lqc_135_amihud_above_2x_baseline_flag},
    "lqc_136_cs_spread_max_21d": {"inputs": ["close", "high", "low"], "func": lqc_136_cs_spread_max_21d},
    "lqc_137_cs_spread_max_63d": {"inputs": ["close", "high", "low"], "func": lqc_137_cs_spread_max_63d},
    "lqc_138_cs_spread_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": lqc_138_cs_spread_expanding_pct_rank},
    "lqc_139_cs_spread_ewm_ratio_5_21": {"inputs": ["close", "high", "low"], "func": lqc_139_cs_spread_ewm_ratio_5_21},
    "lqc_140_cs_spread_gt2x_252d_mean_flag": {"inputs": ["close", "high", "low"], "func": lqc_140_cs_spread_gt2x_252d_mean_flag},
    "lqc_141_cs_spread_21d_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": lqc_141_cs_spread_21d_pct_rank_252d},
    "lqc_142_cs_spread_price_fall_flag": {"inputs": ["close", "high", "low"], "func": lqc_142_cs_spread_price_fall_flag},
    "lqc_143_cs_spread_price_fall_consec": {"inputs": ["close", "high", "low"], "func": lqc_143_cs_spread_price_fall_consec},
    "lqc_144_roll_spread_max_63d": {"inputs": ["close"], "func": lqc_144_roll_spread_max_63d},
    "lqc_145_roll_spread_ewm_ratio_5_63": {"inputs": ["close"], "func": lqc_145_roll_spread_ewm_ratio_5_63},
    "lqc_146_roll_spread_gt2x_252d_mean_flag": {"inputs": ["close"], "func": lqc_146_roll_spread_gt2x_252d_mean_flag},
    "lqc_147_amihud_cs_joint_spike_flag": {"inputs": ["close", "high", "low", "volume"], "func": lqc_147_amihud_cs_joint_spike_flag},
    "lqc_148_amihud_cs_joint_spike_consec": {"inputs": ["close", "high", "low", "volume"], "func": lqc_148_amihud_cs_joint_spike_consec},
    "lqc_149_illiq_composite_expanding_rank": {"inputs": ["close", "high", "low", "volume"], "func": lqc_149_illiq_composite_expanding_rank},
    "lqc_150_amihud_log_diff_21d_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_150_amihud_log_diff_21d_zscore_252d},
}
