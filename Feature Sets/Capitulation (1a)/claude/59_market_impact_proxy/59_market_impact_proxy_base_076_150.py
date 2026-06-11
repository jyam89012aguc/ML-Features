"""
59_market_impact_proxy -- Base Features 076-150
Domain: market-impact / return-per-dollar-volume sensitivity -- Pastor-Stambaugh
  signed-volume return reversal, impact elasticity regression (|return| on log-volume),
  impact level vs trailing baseline, worst-impact days, cross-window comparisons,
  log-return impact, volume-normalized volatility, rolling OLS impact slopes.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- price-impact elasticity spiking, market depth collapsing
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# -- Constants -----------------------------------------------------------------
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9


# -- Utility helpers -----------------------------------------------------------

def _safe_div(num, den):
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s):
    return np.log(s.clip(lower=_EPS))


def _zscore(s, w):
    """Rolling z-score of s over window w."""
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _pct_rank(s, w):
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _consec_streak(cond):
    """Count consecutive True values up to each row (backward-looking)."""
    c      = cond.astype(int)
    group  = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond, w):
    """Maximum consecutive-True run over trailing w periods."""
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


def _ret_per_dolvol(close, volume):
    """Daily return-per-dollar-volume: |return| / dollar_volume."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)


def _amivest(close, volume):
    """Daily Amivest liquidity ratio: dollar_volume / |return|."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(dolvol, ret.replace(0, np.nan))


def _sqrt_impact(close, volume):
    """Square-root impact proxy: |return| / sqrt(dollar_volume)."""
    ret    = close.pct_change(1).abs()
    dolvol = (close * volume).clip(lower=_EPS)
    return ret / np.sqrt(dolvol)


def _range_per_dolvol(high, low, close, volume):
    """Intraday range per dollar volume: (H-L)/close / dollar_volume."""
    rng    = (high - low) / close.replace(0, np.nan)
    dolvol = close * volume
    return _safe_div(rng, dolvol)


def _ols_slope_xy(x_vals, y_vals, min_p):
    """OLS slope on two numpy arrays."""
    if len(x_vals) < min_p:
        return np.nan
    xm = x_vals.mean()
    ym = y_vals.mean()
    num = ((x_vals - xm) * (y_vals - ym)).sum()
    den = ((x_vals - xm) ** 2).sum()
    return num / den if abs(den) > _EPS else np.nan


def _rolling_ols_slope(x_ser, y_ser, w):
    """Rolling OLS slope of y on x over window w."""
    df     = pd.DataFrame({"x": x_ser, "y": y_ser}).dropna()
    x_vals = df["x"].values
    y_vals = df["y"].values
    idx    = df.index
    min_p  = max(2, w // 2)
    out    = pd.Series(np.nan, index=x_ser.index, dtype=float)
    for i in range(len(x_vals)):
        start = max(0, i - w + 1)
        xs = x_vals[start: i + 1]
        ys = y_vals[start: i + 1]
        out.loc[idx[i]] = _ols_slope_xy(xs, ys, min_p)
    return out


def _ps_reversal(close, volume, w):
    """Pastor-Stambaugh signed-volume return reversal coefficient (rolling OLS)."""
    ret      = close.pct_change(1)
    sign_vol = np.sign(ret) * volume
    sv_lag   = sign_vol.shift(1)
    return _rolling_ols_slope(sv_lag, ret, w)


def _impact_elasticity(close, volume, w):
    """Rolling OLS slope of |return| on log(dollar_volume)."""
    abs_ret = close.pct_change(1).abs()
    log_dv  = _log_safe(close * volume)
    return _rolling_ols_slope(log_dv, abs_ret, w)

# -- Feature functions 076-150 ------------------------------------------------

# --- Group G (076-090): Pastor-Stambaugh signed-volume reversal coefficient ---

def mip_076_ps_reversal_21d(close, volume):
    """Pastor-Stambaugh reversal coeff (21d): return regressed on lagged signed volume."""
    return _ps_reversal(close, volume, _TD_MON)


def mip_077_ps_reversal_63d(close, volume):
    """Pastor-Stambaugh reversal coeff (63d): quarterly signed-volume reversal."""
    return _ps_reversal(close, volume, _TD_QTR)


def mip_078_ps_reversal_126d(close, volume):
    """Pastor-Stambaugh reversal coeff (126d): half-year reversal sensitivity."""
    return _ps_reversal(close, volume, _TD_HALF)


def mip_079_ps_reversal_252d(close, volume):
    """Pastor-Stambaugh reversal coeff (252d): annual signed-volume reversal."""
    return _ps_reversal(close, volume, _TD_YEAR)


def mip_080_ps_reversal_21d_zscore_63d(close, volume):
    """Z-score of 21d PS reversal within trailing 63-day window."""
    return _zscore(_ps_reversal(close, volume, _TD_MON), _TD_QTR)


def mip_081_ps_reversal_21d_zscore_252d(close, volume):
    """Z-score of 21d PS reversal within trailing 252-day window."""
    return _zscore(_ps_reversal(close, volume, _TD_MON), _TD_YEAR)


def mip_082_ps_reversal_21d_pct_rank_252d(close, volume):
    """Percentile rank of 21d PS reversal within trailing 252 days."""
    return _pct_rank(_ps_reversal(close, volume, _TD_MON), _TD_YEAR)


def mip_083_ps_reversal_negative_flag(close, volume):
    """Flag: 21d PS reversal coefficient is negative (liquidity provision signal)."""
    return (_ps_reversal(close, volume, _TD_MON) < 0).astype(float)


def mip_084_ps_reversal_21d_spike_ratio_252d(close, volume):
    """21d PS reversal absolute value divided by 252d mean of absolute value."""
    ps = _ps_reversal(close, volume, _TD_MON)
    mu = _rolling_mean(ps.abs(), _TD_YEAR)
    return _safe_div(ps.abs(), mu)


def mip_085_ps_reversal_21d_roll_max_63d(close, volume):
    """63-day rolling max of absolute 21d PS reversal coeff."""
    return _rolling_max(_ps_reversal(close, volume, _TD_MON).abs(), _TD_QTR)


def mip_086_ps_reversal_21d_ewm(close, volume):
    """EWM span=21 of 21d PS reversal coeff (smoothed reversal sensitivity)."""
    return _ewm_mean(_ps_reversal(close, volume, _TD_MON), _TD_MON)


def mip_087_ps_reversal_worsening_streak(close, volume):
    """Consecutive days of increasingly negative 21d PS reversal (worsening illiquidity)."""
    ps   = _ps_reversal(close, volume, _TD_MON)
    cond = ps < ps.shift(1)
    return _consec_streak(cond)


def mip_088_ps_reversal_21d_vs_63d_ratio(close, volume):
    """Ratio of |21d PS reversal| to |63d PS reversal| (short vs medium sensitivity)."""
    return _safe_div(
        _ps_reversal(close, volume, _TD_MON).abs(),
        _ps_reversal(close, volume, _TD_QTR).abs()
    )


def mip_089_ps_reversal_spike_gt2std_252d(close, volume):
    """Flag: |21d PS reversal| > 2 std above its 252-day mean (extreme reversal spike)."""
    ps  = _ps_reversal(close, volume, _TD_MON).abs()
    mu  = _rolling_mean(ps, _TD_YEAR)
    sig = _rolling_std(ps, _TD_YEAR)
    return (ps > mu + 2.0 * sig).astype(float)


def mip_090_ps_reversal_above_mean_streak_63d(close, volume):
    """Consecutive days where |21d PS reversal| exceeds its 63-day mean."""
    ps   = _ps_reversal(close, volume, _TD_MON).abs()
    mu   = _rolling_mean(ps, _TD_QTR)
    cond = ps > mu
    return _consec_streak(cond)

# --- Group H (091-105): Impact elasticity (|return| regression on log-volume) ---

def mip_091_impact_elasticity_21d(close, volume):
    """21d impact elasticity: OLS slope of |return| on log(dollar_volume)."""
    return _impact_elasticity(close, volume, _TD_MON)


def mip_092_impact_elasticity_63d(close, volume):
    """63d impact elasticity: OLS slope of |return| on log(dollar_volume)."""
    return _impact_elasticity(close, volume, _TD_QTR)


def mip_093_impact_elasticity_126d(close, volume):
    """126d impact elasticity: half-year OLS slope of |return| on log(dollar_volume)."""
    return _impact_elasticity(close, volume, _TD_HALF)


def mip_094_impact_elasticity_252d(close, volume):
    """252d impact elasticity: annual OLS slope of |return| on log(dollar_volume)."""
    return _impact_elasticity(close, volume, _TD_YEAR)


def mip_095_impact_elasticity_21d_zscore_63d(close, volume):
    """Z-score of 21d impact elasticity within trailing 63-day window."""
    return _zscore(_impact_elasticity(close, volume, _TD_MON), _TD_QTR)


def mip_096_impact_elasticity_21d_zscore_252d(close, volume):
    """Z-score of 21d impact elasticity within trailing 252-day window."""
    return _zscore(_impact_elasticity(close, volume, _TD_MON), _TD_YEAR)


def mip_097_impact_elasticity_21d_pct_rank_252d(close, volume):
    """Percentile rank of 21d impact elasticity within trailing 252 days."""
    return _pct_rank(_impact_elasticity(close, volume, _TD_MON), _TD_YEAR)


def mip_098_impact_elasticity_21d_spike_ratio_252d(close, volume):
    """21d impact elasticity divided by its 252d rolling mean (spike ratio)."""
    el = _impact_elasticity(close, volume, _TD_MON)
    return _safe_div(el, _rolling_mean(el, _TD_YEAR))


def mip_099_impact_elasticity_21d_spike_gt2std_252d(close, volume):
    """Flag: 21d impact elasticity > 2 std above 252d mean (extreme elasticity spike)."""
    el  = _impact_elasticity(close, volume, _TD_MON)
    mu  = _rolling_mean(el, _TD_YEAR)
    sig = _rolling_std(el, _TD_YEAR)
    return (el > mu + 2.0 * sig).astype(float)


def mip_100_impact_elasticity_above_mean_streak_63d(close, volume):
    """Consecutive days where 21d impact elasticity exceeds its 63-day mean."""
    el   = _impact_elasticity(close, volume, _TD_MON)
    mu   = _rolling_mean(el, _TD_QTR)
    cond = el > mu
    return _consec_streak(cond)


def mip_101_impact_elasticity_21d_roll_max_63d(close, volume):
    """63-day rolling max of 21d impact elasticity."""
    return _rolling_max(_impact_elasticity(close, volume, _TD_MON), _TD_QTR)


def mip_102_impact_elasticity_21d_ewm(close, volume):
    """EWM span=21 of 21d impact elasticity (smoothed sensitivity)."""
    return _ewm_mean(_impact_elasticity(close, volume, _TD_MON), _TD_MON)


def mip_103_impact_elasticity_21d_vs_63d(close, volume):
    """Ratio of 21d to 63d impact elasticity (short vs medium run sensitivity)."""
    return _safe_div(
        _impact_elasticity(close, volume, _TD_MON),
        _impact_elasticity(close, volume, _TD_QTR)
    )


def mip_104_impact_elasticity_positive_flag(close, volume):
    """Flag: 21d impact elasticity is positive (|ret| rises with volume -- unusual)."""
    return (_impact_elasticity(close, volume, _TD_MON) > 0).astype(float)


def mip_105_impact_elasticity_max_streak_63d(close, volume):
    """Max consecutive days of above-mean 21d impact elasticity within 63 days."""
    el   = _impact_elasticity(close, volume, _TD_MON)
    mu   = _rolling_mean(el, _TD_QTR)
    cond = el > mu
    return _rolling_max_streak(cond, _TD_QTR)

# --- Group I (106-120): Impact level vs trailing baseline ---

def mip_106_ret_per_dolvol_vs_252d_baseline(close, volume):
    """Return-per-dolvol divided by 252-day rolling mean (current vs long-run level)."""
    r = _ret_per_dolvol(close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_YEAR))


def mip_107_amivest_vs_252d_baseline(close, volume):
    """Amivest ratio divided by its 252-day mean (depth vs long-run baseline)."""
    av = _amivest(close, volume)
    return _safe_div(av, _rolling_mean(av, _TD_YEAR))


def mip_108_sqrt_impact_vs_252d_baseline(close, volume):
    """Sqrt-impact divided by its 252-day mean (current vs long-run impact)."""
    si = _sqrt_impact(close, volume)
    return _safe_div(si, _rolling_mean(si, _TD_YEAR))


def mip_109_ret_per_dolvol_roll_max_21d(close, volume):
    """21-day rolling max of return-per-dollar-volume (worst impact in month)."""
    return _rolling_max(_ret_per_dolvol(close, volume), _TD_MON)


def mip_110_ret_per_dolvol_roll_max_63d(close, volume):
    """63-day rolling max of return-per-dollar-volume (worst impact in quarter)."""
    return _rolling_max(_ret_per_dolvol(close, volume), _TD_QTR)


def mip_111_ret_per_dolvol_roll_max_252d(close, volume):
    """252-day rolling max of return-per-dollar-volume (worst annual impact level)."""
    return _rolling_max(_ret_per_dolvol(close, volume), _TD_YEAR)


def mip_112_ret_per_dolvol_rising_streak(close, volume):
    """Consecutive days of rising return-per-dollar-volume (worsening impact)."""
    r    = _ret_per_dolvol(close, volume)
    cond = r > r.shift(1)
    return _consec_streak(cond)


def mip_113_ret_per_dolvol_max_rising_streak_21d(close, volume):
    """Max consecutive days of rising return-per-dolvol within trailing 21 days."""
    r    = _ret_per_dolvol(close, volume)
    cond = r > r.shift(1)
    return _rolling_max_streak(cond, _TD_MON)


def mip_114_ret_per_dolvol_max_rising_streak_63d(close, volume):
    """Max consecutive days of rising return-per-dolvol within trailing 63 days."""
    r    = _ret_per_dolvol(close, volume)
    cond = r > r.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def mip_115_impact_rising_price_falling_flag(close, volume):
    """Flag: return-per-dolvol above 21d mean AND close below prior close."""
    r   = _ret_per_dolvol(close, volume)
    mu  = _rolling_mean(r, _TD_MON)
    return ((r > mu) & (close < close.shift(1))).astype(float)


def mip_116_impact_rising_price_falling_streak(close, volume):
    """Consecutive days of high impact (above 21d mean) AND falling price."""
    r    = _ret_per_dolvol(close, volume)
    mu   = _rolling_mean(r, _TD_MON)
    cond = (r > mu) & (close < close.shift(1))
    return _consec_streak(cond)


def mip_117_impact_rising_price_falling_count_21d(close, volume):
    """Count of days in last 21 with high impact AND falling price."""
    r    = _ret_per_dolvol(close, volume)
    mu   = _rolling_mean(r, _TD_MON)
    flag = ((r > mu) & (close < close.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_MON)


def mip_118_impact_rising_price_falling_count_63d(close, volume):
    """Count of days in last 63 with high impact AND falling price."""
    r    = _ret_per_dolvol(close, volume)
    mu   = _rolling_mean(r, _TD_QTR)
    flag = ((r > mu) & (close < close.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def mip_119_amivest_expanding_pct_rank(close, volume):
    """Expanding all-history percentile rank of Amivest ratio."""
    return _amivest(close, volume).expanding(min_periods=5).rank(pct=True)


def mip_120_ret_per_dolvol_expanding_pct_rank(close, volume):
    """Expanding all-history percentile rank of return-per-dollar-volume."""
    return _ret_per_dolvol(close, volume).expanding(min_periods=5).rank(pct=True)


# --- Group J (121-135): Volume-normalized volatility and log-return impact ---

def mip_121_logret_per_dolvol_daily(close, volume):
    """Daily |log-return| per dollar-volume (log-return impact proxy)."""
    lret   = (_log_safe(close) - _log_safe(close.shift(1))).abs()
    dolvol = close * volume
    return _safe_div(lret, dolvol)


def mip_122_logret_per_dolvol_roll_mean_21d(close, volume):
    """21-day rolling mean of |log-return| per dollar-volume."""
    lret   = (_log_safe(close) - _log_safe(close.shift(1))).abs()
    dolvol = close * volume
    return _rolling_mean(_safe_div(lret, dolvol), _TD_MON)


def mip_123_logret_per_dolvol_zscore_63d(close, volume):
    """Z-score of |log-return| per dollar-volume within trailing 63 days."""
    lret   = (_log_safe(close) - _log_safe(close.shift(1))).abs()
    dolvol = close * volume
    return _zscore(_safe_div(lret, dolvol), _TD_QTR)


def mip_124_logret_per_dolvol_pct_rank_252d(close, volume):
    """Percentile rank of |log-return| per dollar-volume within trailing 252 days."""
    lret   = (_log_safe(close) - _log_safe(close.shift(1))).abs()
    dolvol = close * volume
    return _pct_rank(_safe_div(lret, dolvol), _TD_YEAR)


def mip_125_vol_norm_volatility_21d(close, volume):
    """Volume-normalized volatility: 21d std(return) / mean(volume) * 1e6."""
    ret = close.pct_change(1)
    std = _rolling_std(ret, _TD_MON)
    mv  = _rolling_mean(volume, _TD_MON)
    return _safe_div(std, mv) * 1e6


def mip_126_vol_norm_volatility_63d(close, volume):
    """Volume-normalized volatility: 63d std(return) / mean(volume) * 1e6."""
    ret = close.pct_change(1)
    std = _rolling_std(ret, _TD_QTR)
    mv  = _rolling_mean(volume, _TD_QTR)
    return _safe_div(std, mv) * 1e6


def mip_127_vol_norm_volatility_zscore_63d(close, volume):
    """Z-score of 21d volume-normalized volatility within 63-day window."""
    return _zscore(mip_125_vol_norm_volatility_21d(close, volume), _TD_QTR)


def mip_128_vol_norm_volatility_pct_rank_252d(close, volume):
    """Percentile rank of 21d volume-normalized volatility within 252 days."""
    return _pct_rank(mip_125_vol_norm_volatility_21d(close, volume), _TD_YEAR)


def mip_129_vol_norm_volatility_spike_ratio_252d(close, volume):
    """21d vol-norm volatility divided by its 252d mean (annual spike ratio)."""
    v = mip_125_vol_norm_volatility_21d(close, volume)
    return _safe_div(v, _rolling_mean(v, _TD_YEAR))


def mip_130_dolvol_per_abs_ret_roll_mean_21d(close, volume):
    """21-day mean of dollar-volume per unit |return| (Amivest smoothed, alias)."""
    return _rolling_mean(_amivest(close, volume), _TD_MON)


def mip_131_dolvol_per_abs_ret_roll_median_21d(close, volume):
    """21-day rolling median of Amivest ratio (robust depth estimate)."""
    return _rolling_median(_amivest(close, volume), _TD_MON)


def mip_132_dolvol_per_abs_ret_roll_median_63d(close, volume):
    """63-day rolling median of Amivest ratio (robust quarterly depth)."""
    return _rolling_median(_amivest(close, volume), _TD_QTR)


def mip_133_amivest_mean_to_median_ratio_21d(close, volume):
    """Ratio of 21d Amivest mean to median (skewness proxy, 1=symmetric)."""
    av = _amivest(close, volume)
    return _safe_div(_rolling_mean(av, _TD_MON), _rolling_median(av, _TD_MON))


def mip_134_amivest_ewm_span21(close, volume):
    """EWM span=21 of Amivest ratio (exponentially smoothed depth)."""
    return _ewm_mean(_amivest(close, volume), _TD_MON)


def mip_135_amivest_ewm_vs_mean_ratio(close, volume):
    """Ratio of EWM-21 Amivest to its 63-day rolling mean (recent vs baseline depth)."""
    av = _amivest(close, volume)
    return _safe_div(_ewm_mean(av, _TD_MON), _rolling_mean(av, _TD_QTR))


# --- Group K (136-150): Cross-measure composites and additional transforms ---

def mip_136_composite_impact_zscore_21d(close, volume):
    """Composite impact z-score (mean of ret-per-dolvol and sqrt-impact zscores, 21d)."""
    z1 = _zscore(_ret_per_dolvol(close, volume), _TD_MON)
    z2 = _zscore(_sqrt_impact(close, volume), _TD_MON)
    return (z1 + z2) / 2.0


def mip_137_composite_impact_zscore_63d(close, volume):
    """Composite impact z-score (mean of ret-per-dolvol and sqrt-impact zscores, 63d)."""
    z1 = _zscore(_ret_per_dolvol(close, volume), _TD_QTR)
    z2 = _zscore(_sqrt_impact(close, volume), _TD_QTR)
    return (z1 + z2) / 2.0


def mip_138_composite_impact_pct_rank_252d(close, volume):
    """Percentile rank of composite impact (mean of 21d and 63d composite zscores)."""
    comp = (mip_136_composite_impact_zscore_21d(close, volume) +
            mip_137_composite_impact_zscore_63d(close, volume)) / 2.0
    return _pct_rank(comp, _TD_YEAR)


def mip_139_composite_impact_spike_gt2std_252d(close, volume):
    """Flag: composite 63d impact z-score > 2 std above 252d mean."""
    comp = mip_137_composite_impact_zscore_63d(close, volume)
    mu   = _rolling_mean(comp, _TD_YEAR)
    sig  = _rolling_std(comp, _TD_YEAR)
    return (comp > mu + 2.0 * sig).astype(float)


def mip_140_amivest_spike_flag_21d(close, volume):
    """Flag: Amivest ratio below 2 std below 21d mean (depth collapse = impact spike)."""
    av  = _amivest(close, volume)
    mu  = _rolling_mean(av, _TD_MON)
    sig = _rolling_std(av, _TD_MON)
    return (av < mu - 2.0 * sig).astype(float)


def mip_141_amivest_spike_count_21d(close, volume):
    """Count of depth-collapse days (Amivest < 2std below 21d mean) in last 21 days."""
    av    = _amivest(close, volume)
    mu    = _rolling_mean(av, _TD_MON)
    sig   = _rolling_std(av, _TD_MON)
    spike = (av < mu - 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_MON)


def mip_142_amivest_spike_count_63d(close, volume):
    """Count of depth-collapse days (Amivest < 2std below 63d mean) in last 63 days."""
    av    = _amivest(close, volume)
    mu    = _rolling_mean(av, _TD_QTR)
    sig   = _rolling_std(av, _TD_QTR)
    spike = (av < mu - 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def mip_143_ret_per_dolvol_above_90pct_21d_flag(close, volume):
    """Flag: return-per-dolvol above 90th percentile of trailing 21d (impact spike)."""
    r   = _ret_per_dolvol(close, volume)
    p90 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.90)
    return (r > p90).astype(float)


def mip_144_ret_per_dolvol_above_95pct_252d_flag(close, volume):
    """Flag: return-per-dolvol above 95th percentile of trailing 252d."""
    r   = _ret_per_dolvol(close, volume)
    p95 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    return (r > p95).astype(float)


def mip_145_impact_vs_price_divergence_zscore(close, volume):
    """Z-score of (impact zscore minus return zscore): impact up + price down = extreme."""
    iz  = _zscore(_ret_per_dolvol(close, volume), _TD_QTR)
    rz  = _zscore(close.pct_change(1), _TD_QTR)
    sig = iz - rz
    return _zscore(sig, _TD_QTR)


def mip_146_range_per_dolvol_zscore_252d_spike_flag(close, high, low, volume):
    """Flag: range-per-dolvol z-score (252d) above 2 (wide intraday impact spike)."""
    z = _zscore(_range_per_dolvol(high, low, close, volume), _TD_YEAR)
    return (z > 2.0).astype(float)


def mip_147_amivest_roll_min_21d(close, volume):
    """21-day rolling min of Amivest ratio (worst depth episode in month)."""
    return _rolling_min(_amivest(close, volume), _TD_MON)


def mip_148_amivest_roll_min_63d(close, volume):
    """63-day rolling min of Amivest ratio (worst depth episode in quarter)."""
    return _rolling_min(_amivest(close, volume), _TD_QTR)


def mip_149_amivest_above_mean_streak_21d(close, volume):
    """Consecutive days where Amivest exceeds its 21-day rolling mean."""
    av   = _amivest(close, volume)
    mu   = _rolling_mean(av, _TD_MON)
    cond = av > mu
    return _consec_streak(cond)


def mip_150_ret_per_dolvol_spike_streak_count_63d(close, volume):
    """Count of impact-spike days (ret-per-dolvol > 2std above 63d mean) in last 63d."""
    r     = _ret_per_dolvol(close, volume)
    mu    = _rolling_mean(r, _TD_QTR)
    sig   = _rolling_std(r, _TD_QTR)
    spike = (r > mu + 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_QTR)

# -- Registry ------------------------------------------------------------------

MARKET_IMPACT_PROXY_REGISTRY_076_150 = {
    "mip_076_ps_reversal_21d": {"inputs": ["close", "volume"], "func": mip_076_ps_reversal_21d},
    "mip_077_ps_reversal_63d": {"inputs": ["close", "volume"], "func": mip_077_ps_reversal_63d},
    "mip_078_ps_reversal_126d": {"inputs": ["close", "volume"], "func": mip_078_ps_reversal_126d},
    "mip_079_ps_reversal_252d": {"inputs": ["close", "volume"], "func": mip_079_ps_reversal_252d},
    "mip_080_ps_reversal_21d_zscore_63d": {"inputs": ["close", "volume"], "func": mip_080_ps_reversal_21d_zscore_63d},
    "mip_081_ps_reversal_21d_zscore_252d": {"inputs": ["close", "volume"], "func": mip_081_ps_reversal_21d_zscore_252d},
    "mip_082_ps_reversal_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_082_ps_reversal_21d_pct_rank_252d},
    "mip_083_ps_reversal_negative_flag": {"inputs": ["close", "volume"], "func": mip_083_ps_reversal_negative_flag},
    "mip_084_ps_reversal_21d_spike_ratio_252d": {"inputs": ["close", "volume"], "func": mip_084_ps_reversal_21d_spike_ratio_252d},
    "mip_085_ps_reversal_21d_roll_max_63d": {"inputs": ["close", "volume"], "func": mip_085_ps_reversal_21d_roll_max_63d},
    "mip_086_ps_reversal_21d_ewm": {"inputs": ["close", "volume"], "func": mip_086_ps_reversal_21d_ewm},
    "mip_087_ps_reversal_worsening_streak": {"inputs": ["close", "volume"], "func": mip_087_ps_reversal_worsening_streak},
    "mip_088_ps_reversal_21d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": mip_088_ps_reversal_21d_vs_63d_ratio},
    "mip_089_ps_reversal_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": mip_089_ps_reversal_spike_gt2std_252d},
    "mip_090_ps_reversal_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_090_ps_reversal_above_mean_streak_63d},
    "mip_091_impact_elasticity_21d": {"inputs": ["close", "volume"], "func": mip_091_impact_elasticity_21d},
    "mip_092_impact_elasticity_63d": {"inputs": ["close", "volume"], "func": mip_092_impact_elasticity_63d},
    "mip_093_impact_elasticity_126d": {"inputs": ["close", "volume"], "func": mip_093_impact_elasticity_126d},
    "mip_094_impact_elasticity_252d": {"inputs": ["close", "volume"], "func": mip_094_impact_elasticity_252d},
    "mip_095_impact_elasticity_21d_zscore_63d": {"inputs": ["close", "volume"], "func": mip_095_impact_elasticity_21d_zscore_63d},
    "mip_096_impact_elasticity_21d_zscore_252d": {"inputs": ["close", "volume"], "func": mip_096_impact_elasticity_21d_zscore_252d},
    "mip_097_impact_elasticity_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_097_impact_elasticity_21d_pct_rank_252d},
    "mip_098_impact_elasticity_21d_spike_ratio_252d": {"inputs": ["close", "volume"], "func": mip_098_impact_elasticity_21d_spike_ratio_252d},
    "mip_099_impact_elasticity_21d_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": mip_099_impact_elasticity_21d_spike_gt2std_252d},
    "mip_100_impact_elasticity_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_100_impact_elasticity_above_mean_streak_63d},
    "mip_101_impact_elasticity_21d_roll_max_63d": {"inputs": ["close", "volume"], "func": mip_101_impact_elasticity_21d_roll_max_63d},
    "mip_102_impact_elasticity_21d_ewm": {"inputs": ["close", "volume"], "func": mip_102_impact_elasticity_21d_ewm},
    "mip_103_impact_elasticity_21d_vs_63d": {"inputs": ["close", "volume"], "func": mip_103_impact_elasticity_21d_vs_63d},
    "mip_104_impact_elasticity_positive_flag": {"inputs": ["close", "volume"], "func": mip_104_impact_elasticity_positive_flag},
    "mip_105_impact_elasticity_max_streak_63d": {"inputs": ["close", "volume"], "func": mip_105_impact_elasticity_max_streak_63d},
    "mip_106_ret_per_dolvol_vs_252d_baseline": {"inputs": ["close", "volume"], "func": mip_106_ret_per_dolvol_vs_252d_baseline},
    "mip_107_amivest_vs_252d_baseline": {"inputs": ["close", "volume"], "func": mip_107_amivest_vs_252d_baseline},
    "mip_108_sqrt_impact_vs_252d_baseline": {"inputs": ["close", "volume"], "func": mip_108_sqrt_impact_vs_252d_baseline},
    "mip_109_ret_per_dolvol_roll_max_21d": {"inputs": ["close", "volume"], "func": mip_109_ret_per_dolvol_roll_max_21d},
    "mip_110_ret_per_dolvol_roll_max_63d": {"inputs": ["close", "volume"], "func": mip_110_ret_per_dolvol_roll_max_63d},
    "mip_111_ret_per_dolvol_roll_max_252d": {"inputs": ["close", "volume"], "func": mip_111_ret_per_dolvol_roll_max_252d},
    "mip_112_ret_per_dolvol_rising_streak": {"inputs": ["close", "volume"], "func": mip_112_ret_per_dolvol_rising_streak},
    "mip_113_ret_per_dolvol_max_rising_streak_21d": {"inputs": ["close", "volume"], "func": mip_113_ret_per_dolvol_max_rising_streak_21d},
    "mip_114_ret_per_dolvol_max_rising_streak_63d": {"inputs": ["close", "volume"], "func": mip_114_ret_per_dolvol_max_rising_streak_63d},
    "mip_115_impact_rising_price_falling_flag": {"inputs": ["close", "volume"], "func": mip_115_impact_rising_price_falling_flag},
    "mip_116_impact_rising_price_falling_streak": {"inputs": ["close", "volume"], "func": mip_116_impact_rising_price_falling_streak},
    "mip_117_impact_rising_price_falling_count_21d": {"inputs": ["close", "volume"], "func": mip_117_impact_rising_price_falling_count_21d},
    "mip_118_impact_rising_price_falling_count_63d": {"inputs": ["close", "volume"], "func": mip_118_impact_rising_price_falling_count_63d},
    "mip_119_amivest_expanding_pct_rank": {"inputs": ["close", "volume"], "func": mip_119_amivest_expanding_pct_rank},
    "mip_120_ret_per_dolvol_expanding_pct_rank": {"inputs": ["close", "volume"], "func": mip_120_ret_per_dolvol_expanding_pct_rank},
    "mip_121_logret_per_dolvol_daily": {"inputs": ["close", "volume"], "func": mip_121_logret_per_dolvol_daily},
    "mip_122_logret_per_dolvol_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_122_logret_per_dolvol_roll_mean_21d},
    "mip_123_logret_per_dolvol_zscore_63d": {"inputs": ["close", "volume"], "func": mip_123_logret_per_dolvol_zscore_63d},
    "mip_124_logret_per_dolvol_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_124_logret_per_dolvol_pct_rank_252d},
    "mip_125_vol_norm_volatility_21d": {"inputs": ["close", "volume"], "func": mip_125_vol_norm_volatility_21d},
    "mip_126_vol_norm_volatility_63d": {"inputs": ["close", "volume"], "func": mip_126_vol_norm_volatility_63d},
    "mip_127_vol_norm_volatility_zscore_63d": {"inputs": ["close", "volume"], "func": mip_127_vol_norm_volatility_zscore_63d},
    "mip_128_vol_norm_volatility_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_128_vol_norm_volatility_pct_rank_252d},
    "mip_129_vol_norm_volatility_spike_ratio_252d": {"inputs": ["close", "volume"], "func": mip_129_vol_norm_volatility_spike_ratio_252d},
    "mip_130_dolvol_per_abs_ret_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_130_dolvol_per_abs_ret_roll_mean_21d},
    "mip_131_dolvol_per_abs_ret_roll_median_21d": {"inputs": ["close", "volume"], "func": mip_131_dolvol_per_abs_ret_roll_median_21d},
    "mip_132_dolvol_per_abs_ret_roll_median_63d": {"inputs": ["close", "volume"], "func": mip_132_dolvol_per_abs_ret_roll_median_63d},
    "mip_133_amivest_mean_to_median_ratio_21d": {"inputs": ["close", "volume"], "func": mip_133_amivest_mean_to_median_ratio_21d},
    "mip_134_amivest_ewm_span21": {"inputs": ["close", "volume"], "func": mip_134_amivest_ewm_span21},
    "mip_135_amivest_ewm_vs_mean_ratio": {"inputs": ["close", "volume"], "func": mip_135_amivest_ewm_vs_mean_ratio},
    "mip_136_composite_impact_zscore_21d": {"inputs": ["close", "volume"], "func": mip_136_composite_impact_zscore_21d},
    "mip_137_composite_impact_zscore_63d": {"inputs": ["close", "volume"], "func": mip_137_composite_impact_zscore_63d},
    "mip_138_composite_impact_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_138_composite_impact_pct_rank_252d},
    "mip_139_composite_impact_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": mip_139_composite_impact_spike_gt2std_252d},
    "mip_140_amivest_spike_flag_21d": {"inputs": ["close", "volume"], "func": mip_140_amivest_spike_flag_21d},
    "mip_141_amivest_spike_count_21d": {"inputs": ["close", "volume"], "func": mip_141_amivest_spike_count_21d},
    "mip_142_amivest_spike_count_63d": {"inputs": ["close", "volume"], "func": mip_142_amivest_spike_count_63d},
    "mip_143_ret_per_dolvol_above_90pct_21d_flag": {"inputs": ["close", "volume"], "func": mip_143_ret_per_dolvol_above_90pct_21d_flag},
    "mip_144_ret_per_dolvol_above_95pct_252d_flag": {"inputs": ["close", "volume"], "func": mip_144_ret_per_dolvol_above_95pct_252d_flag},
    "mip_145_impact_vs_price_divergence_zscore": {"inputs": ["close", "volume"], "func": mip_145_impact_vs_price_divergence_zscore},
    "mip_146_range_per_dolvol_zscore_252d_spike_flag": {"inputs": ["close", "high", "low", "volume"], "func": mip_146_range_per_dolvol_zscore_252d_spike_flag},
    "mip_147_amivest_roll_min_21d": {"inputs": ["close", "volume"], "func": mip_147_amivest_roll_min_21d},
    "mip_148_amivest_roll_min_63d": {"inputs": ["close", "volume"], "func": mip_148_amivest_roll_min_63d},
    "mip_149_amivest_above_mean_streak_21d": {"inputs": ["close", "volume"], "func": mip_149_amivest_above_mean_streak_21d},
    "mip_150_ret_per_dolvol_spike_streak_count_63d": {"inputs": ["close", "volume"], "func": mip_150_ret_per_dolvol_spike_streak_count_63d},
}