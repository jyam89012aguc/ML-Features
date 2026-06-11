import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd * xd).sum()
        if denom == 0:
            return np.nan
        return float((xd * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (liquidity / cost-of-trading) =====
def _f14_dollar_vol(closeadj, volume):
    return closeadj * volume


def _f14_amihud(closeadj, volume, w):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = ret / dv
    return illiq.rolling(w, min_periods=max(2, w // 2)).mean() * 1e9


def _f14_amihud_daily(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    return (ret / dv) * 1e9


def _f14_vwap_dev(high, low, closeadj, volume, w):
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(w, min_periods=max(2, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    vwap = pv / vv
    return closeadj / vwap.replace(0, np.nan) - 1.0


def _f14_turnover(volume, w):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)
    return volume / base


# ============================================================
# --- Amihud variants on different horizons/transforms ---
# Amihud illiquidity over 5d (weekly impact spikes), log
def f14lq_f14_liquidity_profile_amihudwk_5d_base_v076_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 5)
    b = np.log1p(a.clip(lower=0))
    b = b - b.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity 21d z-scored vs 504d (long-horizon illiquidity standardization)
def f14lq_f14_liquidity_profile_amihudz_504d_base_v077_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud 126d vs 504d ratio (medium vs long impact regime)
def f14lq_f14_liquidity_profile_amihudratio_126v504_base_v078_signal(closeadj, volume):
    s = _f14_amihud(closeadj, volume, 126).clip(lower=1e-12)
    l = _f14_amihud(closeadj, volume, 504).clip(lower=1e-12)
    b = np.log(s / l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud momentum: change in log-illiquidity over a quarter (impact trend)
def f14lq_f14_liquidity_profile_amihudmom_63d_base_v079_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud rank-of-change: percentile of 21d illiquidity change vs its 252d history
def f14lq_f14_liquidity_profile_amihudchgrank_base_v080_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    chg = a - a.shift(21)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-liquidity dynamics ---
# log dollar-liquidity level over 252d (annual liquidity size)
def f14lq_f14_liquidity_profile_dollarliq_252d_base_v081_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = np.log(_mean(dv, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity 63d vs 252d ratio (liquidity expansion/contraction regime)
def f14lq_f14_liquidity_profile_liqexpand_63v252_base_v082_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    s = _mean(dv, 63)
    l = _mean(dv, 252).replace(0, np.nan)
    b = np.log(s / l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity acceleration: 63d slope minus its own value a quarter ago
def f14lq_f14_liquidity_profile_liqaccel_63d_base_v083_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    sl = _slope(dv, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity drawdown depth from 504d peak (long dry-up severity)
def f14lq_f14_liquidity_profile_liqdd_504d_base_v084_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21)
    peak = dv.rolling(504, min_periods=252).max().replace(0, np.nan)
    b = np.log(dv / peak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d that dollar-liquidity is within 10% of its 252d peak (sustained-liquidity)
def f14lq_f14_liquidity_profile_liqathfrac_252d_base_v085_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21)
    peak = dv.rolling(252, min_periods=126).max().replace(0, np.nan)
    near = (dv / peak > 0.9).astype(float)
    b = near.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- turnover dynamics ---
# turnover 5d vs 21d ratio (very-short liquidity inflow)
def f14lq_f14_liquidity_profile_turnover_5v21_base_v086_signal(volume):
    s = _mean(volume, 5)
    l = _mean(volume, 21).replace(0, np.nan)
    b = s / l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover acceleration: change in 21d/63d turnover ratio over a month
def f14lq_f14_liquidity_profile_turnaccel_21d_base_v087_signal(volume):
    r = _mean(volume, 21) / _mean(volume, 63).replace(0, np.nan)
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover volatility: std of daily volume over 63d, normalized by mean (lumpiness)
def f14lq_f14_liquidity_profile_turnvol_63d_base_v088_signal(volume):
    m = _mean(volume, 63).replace(0, np.nan)
    sd = _std(volume, 63)
    b = sd / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover skew over 126d (sporadic-spike vs steady participation)
def f14lq_f14_liquidity_profile_turnskew_126d_base_v089_signal(volume):
    b = volume.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover autocorrelation lag-1 over 63d (persistence of participation)
def f14lq_f14_liquidity_profile_turnac1_63d_base_v090_signal(volume):
    v = np.log(volume.replace(0, np.nan))
    b = v.rolling(63, min_periods=21).corr(v.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP / typical-price dynamics ---
# VWAP deviation 252d (long execution anchor)
def f14lq_f14_liquidity_profile_vwapdev_252d_base_v091_signal(high, low, closeadj, volume):
    b = _f14_vwap_dev(high, low, closeadj, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP deviation momentum: change in 63d VWAP-dev over a month
def f14lq_f14_liquidity_profile_vwapdevmom_63d_base_v092_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 63)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# typical-price vs close gap: (H+L+C)/3 vs C, smoothed (intraday positioning bias)
def f14lq_f14_liquidity_profile_tpgap_21d_base_v093_signal(high, low, closeadj):
    tp = (high + low + closeadj) / 3.0
    gap = tp / closeadj.replace(0, np.nan) - 1.0
    b = gap.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP-deviation z-scored vs 252d (standardized execution premium)
def f14lq_f14_liquidity_profile_vwapdevz_252d_base_v094_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP deviation 5d minus 63d (very-short vs medium execution-anchor disagreement)
def f14lq_f14_liquidity_profile_vwapdevspr_63v252_base_v095_signal(high, low, closeadj, volume):
    s = _f14_vwap_dev(high, low, closeadj, volume, 5)
    l = _f14_vwap_dev(high, low, closeadj, volume, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity-risk / volatility ---
# vol-of-liquidity: std of log dollar-volume over 126d (liquidity uncertainty)
def f14lq_f14_liquidity_profile_liqvol_126d_base_v096_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _std(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol-of-liquidity: std of 21d liquidity-vol over 126d (regime instability)
def f14lq_f14_liquidity_profile_liqvov_126d_base_v097_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    v21 = _std(dv, 21)
    b = _std(v21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-vol ratio: 21d vs 126d liquidity volatility (vol term-structure of liquidity)
def f14lq_f14_liquidity_profile_liqvolratio_21v126_base_v098_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    s = _std(dv, 21).replace(0, np.nan)
    l = _std(dv, 126).replace(0, np.nan)
    b = np.log(s / l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside liquidity vol: std of negative log-liquidity changes over 63d (dry-up risk)
def f14lq_f14_liquidity_profile_liqdownvol_63d_base_v099_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    neg = chg.where(chg < 0)
    b = neg.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-vol trend: slope of 21d liquidity-vol over 126d (is liquidity stabilizing?)
def f14lq_f14_liquidity_profile_liqvoltrend_126d_base_v100_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    v21 = _std(dv, 21)
    b = _slope(v21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- impact / cost composites ---
# Amihud-to-turnover interaction: illiquid AND thinly-traded (z-sum)
def f14lq_f14_liquidity_profile_illiqthin_63d_base_v101_signal(closeadj, volume):
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    t = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    b = a - t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized impact per traded notional: |21d return| / 21d dollar-liquidity, z-scored
def f14lq_f14_liquidity_profile_realimpact_21d_base_v102_signal(closeadj, volume):
    ret21 = closeadj.pct_change(21).abs()
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan)
    impact = ret21 / dv
    b = _z(np.log1p((impact * 1e9).clip(lower=0)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz-style spread proxy from high-low (bid-ask cost), 21d
def f14lq_f14_liquidity_profile_hlspread_21d_base_v103_signal(high, low):
    beta = (np.log(high / low.replace(0, np.nan)) ** 2)
    beta2 = beta.rolling(2, min_periods=2).sum()
    hl2 = (np.maximum(high, high.shift(1)) / np.minimum(low, low.shift(1)).replace(0, np.nan))
    gamma = np.log(hl2) ** 2
    alpha = (np.sqrt(2 * beta2) - np.sqrt(beta2)) / (3 - 2 * np.sqrt(2)) \
        - np.sqrt(gamma / (3 - 2 * np.sqrt(2)))
    spread = 2 * (np.exp(alpha) - 1) / (1 + np.exp(alpha))
    b = spread.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread trend: slope of effective-spread over 126d (cost rising/falling)
def f14lq_f14_liquidity_profile_hlspreadz_252d_base_v104_signal(high, low):
    beta = (np.log(high / low.replace(0, np.nan)) ** 2)
    beta2 = beta.rolling(2, min_periods=2).sum()
    hl2 = (np.maximum(high, high.shift(1)) / np.minimum(low, low.shift(1)).replace(0, np.nan))
    gamma = np.log(hl2) ** 2
    alpha = (np.sqrt(2 * beta2) - np.sqrt(beta2)) / (3 - 2 * np.sqrt(2)) \
        - np.sqrt(gamma / (3 - 2 * np.sqrt(2)))
    spread = 2 * (np.exp(alpha) - 1) / (1 + np.exp(alpha))
    b = _slope(spread.rolling(21, min_periods=10).mean(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll effective-spread proxy: sqrt of negative autocovariance of returns, 63d
def f14lq_f14_liquidity_profile_rollspread_63d_base_v105_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    b = np.sqrt((-cov).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread z-scored vs 252d (relative microstructure cost)
def f14lq_f14_liquidity_profile_rollspreadz_252d_base_v106_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = np.sqrt((-cov).clip(lower=0))
    b = _z(rs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity-flow / direction ---
# signed dollar-flow imbalance over 21d (buy vs sell pressure proxy)
def f14lq_f14_liquidity_profile_flowimb_21d_base_v107_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    b = signed.rolling(21, min_periods=10).sum() / dv.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flow-imbalance persistence: 63d net signed-flow ratio (directional liquidity bias)
def f14lq_f14_liquidity_profile_flowimb_63d_base_v108_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    b = signed.rolling(63, min_periods=21).sum() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-weighted return: 21d return contribution weighted by relative dollar-vol
def f14lq_f14_liquidity_profile_liqwret_21d_base_v109_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    w = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = (ret * w).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-return elasticity: regression slope of |return| on log dollar-vol over 63d
def f14lq_f14_liquidity_profile_volretelast_63d_base_v110_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    b = cov / var
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- typical-price / VWAP cost dispersion ---
# VWAP-deviation dispersion over 63d (execution-anchor instability)
def f14lq_f14_liquidity_profile_vwapdisp_63d_base_v111_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = _std(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-VWAP intensity: avg positive VWAP deviation over 63d (premium-side cost)
def f14lq_f14_liquidity_profile_vwapprem_63d_base_v112_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = d.clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# below-VWAP intensity: avg negative VWAP deviation over 63d (discount-side cost)
def f14lq_f14_liquidity_profile_vwapdisc_63d_base_v113_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = (-d.clip(upper=0)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP premium/discount asymmetry over 63d (which side execution favors)
def f14lq_f14_liquidity_profile_vwapasym_63d_base_v114_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    up = d.clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- illiquidity persistence / streak (continuous forms) ---
# below-average-liquidity occupancy: fraction of 126d below 252d-median dollar-vol
def f14lq_f14_liquidity_profile_thinoccupancy_126d_base_v115_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(252, min_periods=126).median()
    below = (dv < med).astype(float)
    b = below.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-persistence: lag-1 autocorrelation of daily Amihud over 126d
def f14lq_f14_liquidity_profile_illiqac1_126d_base_v116_signal(closeadj, volume):
    a = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    b = a.rolling(126, min_periods=63).corr(a.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dry-spell depth: avg shortfall of dollar-vol below its 63d-EMA when below (continuous streak)
def f14lq_f14_liquidity_profile_dryspell_63d_base_v117_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    ema = dv.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    shortfall = (1.0 - dv / ema).clip(lower=0)
    b = shortfall.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since last liquidity surge: bars since dollar-vol last exceeded 2x its 63d median
def f14lq_f14_liquidity_profile_sincesurge_126d_base_v118_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    surge = (dv > 2.0 * med).astype(float)

    def _since(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = surge.rolling(126, min_periods=63).apply(_since, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-window liquidity composites ---
# liquidity term-structure slope: 21/63/252 dollar-liquidity regression across horizons
def f14lq_f14_liquidity_profile_liqterm_base_v119_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    l21 = np.log(_mean(dv, 21).replace(0, np.nan))
    l63 = np.log(_mean(dv, 63).replace(0, np.nan))
    l252 = np.log(_mean(dv, 252).replace(0, np.nan))
    b = (l21 - l252) - (l63 - l252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud term-structure: 21d vs 126d illiquidity slope across horizons
def f14lq_f14_liquidity_profile_illiqterm_base_v120_signal(closeadj, volume):
    a21 = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    a63 = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    a126 = np.log1p(_f14_amihud(closeadj, volume, 126).clip(lower=0))
    b = (a21 - a126) - (a63 - a126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-cost composite: turnover-adjusted Amihud (impact net of activity), z
def f14lq_f14_liquidity_profile_costcomposite_63d_base_v121_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    t = np.log(_mean(volume, 63).replace(0, np.nan))
    raw = a + 0.5 * t  # impact level partially offset by participation
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP / price-position liquidity ---
# close position within volume-weighted band: where close sits vs 21d VWAP +/- dispersion
def f14lq_f14_liquidity_profile_vwapband_21d_base_v122_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(21, min_periods=10).sum()
    vv = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    vwap = pv / vv
    disp = (closeadj - vwap).rolling(21, min_periods=10).std().replace(0, np.nan)
    b = (closeadj - vwap) / disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-weighted price drift vs simple price drift over 63d (liquidity-tilted move)
def f14lq_f14_liquidity_profile_liqdrift_63d_base_v123_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    w = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    wret = (ret * w).rolling(63, min_periods=21).sum()
    sret = ret.rolling(63, min_periods=21).mean()
    b = wret - sret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity-risk regime ---
# illiquidity-vol regime: ratio of 21d to 126d Amihud volatility (impact instability)
def f14lq_f14_liquidity_profile_illiqvolratio_base_v124_signal(closeadj, volume):
    a = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    s = a.rolling(21, min_periods=10).std().replace(0, np.nan)
    l = a.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = np.log(s / l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity peak-to-typical: 126d max dollar-volume vs its median (event-day lumpiness), log
def f14lq_f14_liquidity_profile_liqherf_126d_base_v125_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    mx = dv.rolling(126, min_periods=63).max()
    md = dv.rolling(126, min_periods=63).median().replace(0, np.nan)
    b = np.log(mx / md)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-5-day liquidity share over 63d (event-driven liquidity concentration)
def f14lq_f14_liquidity_profile_top5share_63d_base_v126_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)

    def _top5(a):
        s = np.sort(a)[-5:].sum()
        tot = a.sum()
        if tot <= 0:
            return np.nan
        return float(s / tot)
    b = dv.rolling(63, min_periods=21).apply(_top5, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity-adjusted momentum / value ---
# illiquidity-scaled momentum: 63d return divided by sqrt Amihud (impact-aware momentum)
def f14lq_f14_liquidity_profile_liqmom63_base_v127_signal(closeadj, volume):
    ret = closeadj.pct_change(63)
    a = np.sqrt(_f14_amihud(closeadj, volume, 63).clip(lower=0)).replace(0, np.nan)
    b = ret / a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity per unit volatility (tradable-risk capacity), 63d, log
def f14lq_f14_liquidity_profile_liqpervol_63d_base_v128_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std().replace(0, np.nan)
    b = np.log((dv * vol).replace(0, np.nan))
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-momentum interaction: turnover surge x recent return sign (informed flow)
def f14lq_f14_liquidity_profile_turnmomint_21d_base_v129_signal(closeadj, volume):
    surge = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    rsign = np.sign(closeadj.pct_change(21))
    b = surge * rsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-vs-price-trend divergence: rising price on falling liquidity (distribution proxy)
def f14lq_f14_liquidity_profile_liqpxdiv_63d_base_v130_signal(closeadj, volume):
    px = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    liq = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    b = np.sign(px) * (px - liq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional Amihud / cost variants ---
# Amihud over 252d detrended vs 504d (long impact deviation)
def f14lq_f14_liquidity_profile_amihud252det_base_v131_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 252).clip(lower=0))
    b = a - a.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity volatility 126d (instability of trading cost, medium horizon)
def f14lq_f14_liquidity_profile_illiqvol_126d_base_v132_signal(closeadj, volume):
    a = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    b = a.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-skew over 126d (tail-heavy impact profile)
def f14lq_f14_liquidity_profile_illiqskew_126d_base_v133_signal(closeadj, volume):
    a = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    b = a.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-spike intensity: avg excess of daily Amihud above its 63d 90th percentile (126d)
def f14lq_f14_liquidity_profile_illiqkurt_126d_base_v134_signal(closeadj, volume):
    a = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    p90 = a.rolling(63, min_periods=21).quantile(0.90)
    excess = (a - p90).clip(lower=0)
    b = excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-recovery rate: log liquidity gain since 126d trough divided by time since trough
def f14lq_f14_liquidity_profile_liqrecovrate_126d_base_v135_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21)
    trough = dv.rolling(126, min_periods=63).min().replace(0, np.nan)

    def _since_min(a):
        return float(len(a) - 1 - int(np.argmin(a)))
    dst = dv.rolling(126, min_periods=63).apply(_since_min, raw=True).replace(0, np.nan)
    b = np.log(dv / trough) / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- price-range-based liquidity ---
# high-low range per dollar-volume z-scored 252d (no-info impact, relative)
def f14lq_f14_liquidity_profile_rngperliq_63d_base_v136_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _f14_dollar_vol(closeadj, volume).replace(0, np.nan)
    raw = (rng / dv * 1e9)
    b = _z(np.log1p(raw.clip(lower=0)).rolling(63, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-per-range depth: volume needed per unit intraday range, z-scored (depth in shares)
def f14lq_f14_liquidity_profile_volperrange_63d_base_v137_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    depth = np.log((volume / rng.replace(0, np.nan)).replace(0, np.nan))
    b = _z(depth.rolling(63, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion vs liquidity: do wide-range days come with thin liquidity? corr 126d
def f14lq_f14_liquidity_profile_rngliqcorr_126d_base_v138_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = rng.rolling(126, min_periods=63).corr(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity flow timing ---
# liquidity-led return: corr of dollar-vol change with next-day |return| over 126d (impact lead)
def f14lq_f14_liquidity_profile_liqlead_126d_base_v139_signal(closeadj, volume):
    dvc = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)).diff()
    fut = closeadj.pct_change().abs().shift(-1)
    b = dvc.rolling(126, min_periods=63).corr(fut)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-return contemporaneous corr over 63d (volume confirming moves)
def f14lq_f14_liquidity_profile_turnretcorr_63d_base_v140_signal(closeadj, volume):
    v = np.log(volume.replace(0, np.nan)).diff()
    r = closeadj.pct_change().abs()
    b = v.rolling(63, min_periods=21).corr(r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite tradability / fragility ---
# liquidity fragility: high turnover but rising Amihud (volume without depth), 63d
def f14lq_f14_liquidity_profile_fragility2_63d_base_v141_signal(closeadj, volume):
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    b = tz * az  # interaction: simultaneous high-volume / high-impact
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tradability trend: slope of composite (liquidity up, impact down) over 126d
def f14lq_f14_liquidity_profile_tradetrend_126d_base_v142_signal(closeadj, volume):
    liq = _z(np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan)), 252)
    illiq = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    comp = liq - illiq
    b = _slope(comp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity stress index: z-sum of high Amihud, high liquidity-vol, low turnover (126d)
def f14lq_f14_liquidity_profile_stressidx_126d_base_v143_signal(closeadj, volume):
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    lvz = _z(_std(dv, 63), 252)
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    b = az + lvz - tz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-improvement breadth: fraction of 126d with 21d-liq above 63d-liq, detrended
def f14lq_f14_liquidity_profile_liqimprov_126d_base_v144_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    fast = _mean(dv, 21)
    slow = _mean(dv, 63)
    above = (fast > slow).astype(float)
    raw = above.rolling(126, min_periods=63).mean()
    b = raw - raw.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- final distinct liquidity signals ---
# Amihud-vs-spread composition: how much impact is permanent (Amihud) vs transient (Roll), 63d
def f14lq_f14_liquidity_profile_permtrans_63d_base_v145_signal(closeadj, volume):
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = np.sqrt((-cov).clip(lower=0))
    rz = _z(rs, 252)
    b = a - rz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity 5-year percentile (multi-year liquidity standing)
def f14lq_f14_liquidity_profile_liqpct_1260d_base_v146_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 63)
    b = _rank(dv, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud 5-year percentile (multi-year impact standing)
def f14lq_f14_liquidity_profile_illiqpct_1260d_base_v147_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 63)
    b = _rank(a, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-vol normalized turnover: turnover divided by its own volatility (clean activity), z
def f14lq_f14_liquidity_profile_cleanturn_63d_base_v148_signal(volume):
    t = _mean(volume, 21)
    sd = _std(volume, 63).replace(0, np.nan)
    b = _z(t / sd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity acceleration via second difference of log dollar-liquidity, 63d window mean
def f14lq_f14_liquidity_profile_liqsecdiff_63d_base_v149_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    acc = dv.diff(21) - dv.diff(21).shift(21)
    b = acc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP reversion half-life proxy: lag-1 autocorr of 21d VWAP deviation over 126d
def f14lq_f14_liquidity_profile_vwaprevac_126d_base_v150_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = d.rolling(126, min_periods=63).corr(d.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14lq_f14_liquidity_profile_amihudwk_5d_base_v076_signal,
    f14lq_f14_liquidity_profile_amihudz_504d_base_v077_signal,
    f14lq_f14_liquidity_profile_amihudratio_126v504_base_v078_signal,
    f14lq_f14_liquidity_profile_amihudmom_63d_base_v079_signal,
    f14lq_f14_liquidity_profile_amihudchgrank_base_v080_signal,
    f14lq_f14_liquidity_profile_dollarliq_252d_base_v081_signal,
    f14lq_f14_liquidity_profile_liqexpand_63v252_base_v082_signal,
    f14lq_f14_liquidity_profile_liqaccel_63d_base_v083_signal,
    f14lq_f14_liquidity_profile_liqdd_504d_base_v084_signal,
    f14lq_f14_liquidity_profile_liqathfrac_252d_base_v085_signal,
    f14lq_f14_liquidity_profile_turnover_5v21_base_v086_signal,
    f14lq_f14_liquidity_profile_turnaccel_21d_base_v087_signal,
    f14lq_f14_liquidity_profile_turnvol_63d_base_v088_signal,
    f14lq_f14_liquidity_profile_turnskew_126d_base_v089_signal,
    f14lq_f14_liquidity_profile_turnac1_63d_base_v090_signal,
    f14lq_f14_liquidity_profile_vwapdev_252d_base_v091_signal,
    f14lq_f14_liquidity_profile_vwapdevmom_63d_base_v092_signal,
    f14lq_f14_liquidity_profile_tpgap_21d_base_v093_signal,
    f14lq_f14_liquidity_profile_vwapdevz_252d_base_v094_signal,
    f14lq_f14_liquidity_profile_vwapdevspr_63v252_base_v095_signal,
    f14lq_f14_liquidity_profile_liqvol_126d_base_v096_signal,
    f14lq_f14_liquidity_profile_liqvov_126d_base_v097_signal,
    f14lq_f14_liquidity_profile_liqvolratio_21v126_base_v098_signal,
    f14lq_f14_liquidity_profile_liqdownvol_63d_base_v099_signal,
    f14lq_f14_liquidity_profile_liqvoltrend_126d_base_v100_signal,
    f14lq_f14_liquidity_profile_illiqthin_63d_base_v101_signal,
    f14lq_f14_liquidity_profile_realimpact_21d_base_v102_signal,
    f14lq_f14_liquidity_profile_hlspread_21d_base_v103_signal,
    f14lq_f14_liquidity_profile_hlspreadz_252d_base_v104_signal,
    f14lq_f14_liquidity_profile_rollspread_63d_base_v105_signal,
    f14lq_f14_liquidity_profile_rollspreadz_252d_base_v106_signal,
    f14lq_f14_liquidity_profile_flowimb_21d_base_v107_signal,
    f14lq_f14_liquidity_profile_flowimb_63d_base_v108_signal,
    f14lq_f14_liquidity_profile_liqwret_21d_base_v109_signal,
    f14lq_f14_liquidity_profile_volretelast_63d_base_v110_signal,
    f14lq_f14_liquidity_profile_vwapdisp_63d_base_v111_signal,
    f14lq_f14_liquidity_profile_vwapprem_63d_base_v112_signal,
    f14lq_f14_liquidity_profile_vwapdisc_63d_base_v113_signal,
    f14lq_f14_liquidity_profile_vwapasym_63d_base_v114_signal,
    f14lq_f14_liquidity_profile_thinoccupancy_126d_base_v115_signal,
    f14lq_f14_liquidity_profile_illiqac1_126d_base_v116_signal,
    f14lq_f14_liquidity_profile_dryspell_63d_base_v117_signal,
    f14lq_f14_liquidity_profile_sincesurge_126d_base_v118_signal,
    f14lq_f14_liquidity_profile_liqterm_base_v119_signal,
    f14lq_f14_liquidity_profile_illiqterm_base_v120_signal,
    f14lq_f14_liquidity_profile_costcomposite_63d_base_v121_signal,
    f14lq_f14_liquidity_profile_vwapband_21d_base_v122_signal,
    f14lq_f14_liquidity_profile_liqdrift_63d_base_v123_signal,
    f14lq_f14_liquidity_profile_illiqvolratio_base_v124_signal,
    f14lq_f14_liquidity_profile_liqherf_126d_base_v125_signal,
    f14lq_f14_liquidity_profile_top5share_63d_base_v126_signal,
    f14lq_f14_liquidity_profile_liqmom63_base_v127_signal,
    f14lq_f14_liquidity_profile_liqpervol_63d_base_v128_signal,
    f14lq_f14_liquidity_profile_turnmomint_21d_base_v129_signal,
    f14lq_f14_liquidity_profile_liqpxdiv_63d_base_v130_signal,
    f14lq_f14_liquidity_profile_amihud252det_base_v131_signal,
    f14lq_f14_liquidity_profile_illiqvol_126d_base_v132_signal,
    f14lq_f14_liquidity_profile_illiqskew_126d_base_v133_signal,
    f14lq_f14_liquidity_profile_illiqkurt_126d_base_v134_signal,
    f14lq_f14_liquidity_profile_liqrecovrate_126d_base_v135_signal,
    f14lq_f14_liquidity_profile_rngperliq_63d_base_v136_signal,
    f14lq_f14_liquidity_profile_volperrange_63d_base_v137_signal,
    f14lq_f14_liquidity_profile_rngliqcorr_126d_base_v138_signal,
    f14lq_f14_liquidity_profile_liqlead_126d_base_v139_signal,
    f14lq_f14_liquidity_profile_turnretcorr_63d_base_v140_signal,
    f14lq_f14_liquidity_profile_fragility2_63d_base_v141_signal,
    f14lq_f14_liquidity_profile_tradetrend_126d_base_v142_signal,
    f14lq_f14_liquidity_profile_stressidx_126d_base_v143_signal,
    f14lq_f14_liquidity_profile_liqimprov_126d_base_v144_signal,
    f14lq_f14_liquidity_profile_permtrans_63d_base_v145_signal,
    f14lq_f14_liquidity_profile_liqpct_1260d_base_v146_signal,
    f14lq_f14_liquidity_profile_illiqpct_1260d_base_v147_signal,
    f14lq_f14_liquidity_profile_cleanturn_63d_base_v148_signal,
    f14lq_f14_liquidity_profile_liqsecdiff_63d_base_v149_signal,
    f14lq_f14_liquidity_profile_vwaprevac_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_LIQUIDITY_PROFILE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f14_liquidity_profile_base_076_150_claude: %d features pass" % n_features)
