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
    # OLS slope of s on time index over window w (handles short warm-up windows)
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
    # dollar volume (traded notional); used on windows > 21d
    return closeadj * volume


def _f14_amihud(closeadj, volume, w):
    # Amihud illiquidity: average of |return| / dollar-volume, scaled
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = ret / dv
    return illiq.rolling(w, min_periods=max(2, w // 2)).mean() * 1e9


def _f14_typical_price(high, low, closeadj):
    return (high + low + closeadj) / 3.0


def _f14_vwap_dev(high, low, closeadj, volume, w):
    # deviation of close from volume-weighted typical price over window
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(w, min_periods=max(2, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    vwap = pv / vv
    return closeadj / vwap.replace(0, np.nan) - 1.0


def _f14_turnover(volume, w):
    # turnover proxy: volume relative to its own trailing average liquidity base
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)
    return volume / base


def _f14_illiq_streak(volume, w):
    # proxy for low-liquidity persistence: fraction of days with below-median volume
    med = volume.rolling(w, min_periods=max(2, w // 2)).median()
    thin = (volume < med).astype(float)
    return thin.rolling(w, min_periods=max(2, w // 2)).mean()


# ============================================================
# --- Amihud illiquidity levels ---
# Amihud illiquidity over 21d (monthly cost-of-impact)
def f14lq_f14_liquidity_profile_amihud_21d_base_v001_signal(closeadj, volume):
    b = _f14_amihud(closeadj, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity over 63d, detrended vs its own 252d level (impact deviation, not size proxy)
def f14lq_f14_liquidity_profile_amihud_63d_base_v002_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    b = a - a.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity over 126d, z-scored vs its own 252d history
def f14lq_f14_liquidity_profile_amihud_126d_base_v003_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 126)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity over 252d, percentile-ranked vs its own 504d history
def f14lq_f14_liquidity_profile_amihud_252d_base_v004_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 252)
    b = _rank(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud short/long ratio: 21d impact vs 252d impact (illiquidity regime shift)
def f14lq_f14_liquidity_profile_amihudratio_21v252_base_v005_signal(closeadj, volume):
    s = _f14_amihud(closeadj, volume, 21)
    l = _f14_amihud(closeadj, volume, 252).replace(0, np.nan)
    b = np.log(s.clip(lower=1e-12) / l.clip(lower=1e-12))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-liquidity level ---
# log dollar-volume level over 21d (notional liquidity base)
def f14lq_f14_liquidity_profile_dollarliq_21d_base_v006_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = np.log(_mean(dv, 21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity ramp: 21d dollar-liquidity relative to 63d base (short-term liquidity expansion)
def f14lq_f14_liquidity_profile_dollarliq_63d_base_v007_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    short = _mean(dv, 21)
    base = _mean(dv, 63).replace(0, np.nan)
    b = np.log(short / base)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume level z-scored vs its own 252d history (de-trended liquidity)
def f14lq_f14_liquidity_profile_dollarliqz_126d_base_v008_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    m = _mean(dv, 126)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume percentile rank over 504d (where current liquidity sits)
def f14lq_f14_liquidity_profile_dollarliqrank_63d_base_v009_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    m = _mean(dv, 63)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tradability floor tightness: 63d min dollar-liquidity vs its 63d average (gap-down risk)
def f14lq_f14_liquidity_profile_dollarliqfloor_63d_base_v010_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    floor = dv.rolling(63, min_periods=21).min()
    avg = dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = floor / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- turnover ---
# turnover surge: 5d volume vs 63d base (short-term liquidity inflow)
def f14lq_f14_liquidity_profile_turnover_5v63_base_v011_signal(volume):
    short = _mean(volume, 5)
    base = _mean(volume, 63).replace(0, np.nan)
    b = short / base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover ratio: 21d volume vs 126d base (relative trading intensity)
def f14lq_f14_liquidity_profile_turnover_21v126_base_v012_signal(volume):
    short = _mean(volume, 21)
    base = _mean(volume, 126).replace(0, np.nan)
    b = short / base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover level z-scored vs own 252d history (de-trended participation)
def f14lq_f14_liquidity_profile_turnoverz_21d_base_v013_signal(volume):
    t = _f14_turnover(volume, 63)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover percentile rank over 252d (participation extremity)
def f14lq_f14_liquidity_profile_turnoverrank_21d_base_v014_signal(volume):
    t = _mean(volume, 21)
    b = _rank(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP deviation (typical-price-based) ---
# close vs 21d volume-weighted typical price (execution premium/discount)
def f14lq_f14_liquidity_profile_vwapdev_21d_base_v015_signal(high, low, closeadj, volume):
    b = _f14_vwap_dev(high, low, closeadj, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 63d VWAP, z-scored vs own 126d history
def f14lq_f14_liquidity_profile_vwapdev_63d_base_v016_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 126d VWAP (longer execution anchor)
def f14lq_f14_liquidity_profile_vwapdev_126d_base_v017_signal(high, low, closeadj, volume):
    b = _f14_vwap_dev(high, low, closeadj, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP-deviation spread: 21d vs 126d anchor disagreement
def f14lq_f14_liquidity_profile_vwapdevspr_21v126_base_v018_signal(high, low, closeadj, volume):
    s = _f14_vwap_dev(high, low, closeadj, volume, 21)
    l = _f14_vwap_dev(high, low, closeadj, volume, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute VWAP deviation averaged (typical execution slippage magnitude)
def f14lq_f14_liquidity_profile_vwapslip_63d_base_v019_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21).abs()
    b = d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity trend ---
# slope of log dollar-volume over 63d (liquidity trend)
def f14lq_f14_liquidity_profile_liqtrend_63d_base_v020_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _slope(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log dollar-volume over 126d (medium-term liquidity drift)
def f14lq_f14_liquidity_profile_liqtrend_126d_base_v021_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _slope(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in log dollar-volume level over a quarter (liquidity momentum)
def f14lq_f14_liquidity_profile_liqmom_63d_base_v022_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    b = dv - dv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity trend: slope of log-illiquidity over 126d (deteriorating impact)
def f14lq_f14_liquidity_profile_illiqtrend_126d_base_v023_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    b = _slope(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- illiquidity streak / thin-volume proxy ---
# depth-weighted thin-trading: avg shortfall of volume below its 63d median (illiquidity load)
def f14lq_f14_liquidity_profile_thinfrac_63d_base_v024_signal(volume):
    med = volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    shortfall = (1.0 - volume / med).clip(lower=0)
    b = shortfall.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-streak intensity: EWMA of below-average-volume signal x its depth (persistent dry spells)
def f14lq_f14_liquidity_profile_thinstreak_63d_base_v025_signal(volume):
    avg = _mean(volume, 63).replace(0, np.nan)
    rel = volume / avg
    thin_depth = (1.0 - rel).clip(lower=0)
    b = thin_depth.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dry-up severity: 10th-percentile of relative volume over 126d (how thin the quiet days get)
def f14lq_f14_liquidity_profile_dryup_126d_base_v026_signal(volume):
    base = _mean(volume, 126).replace(0, np.nan)
    rel = volume / base
    b = rel.rolling(126, min_periods=63).quantile(0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liquidity volatility ---
# volatility of log dollar-volume over 63d (liquidity instability)
def f14lq_f14_liquidity_profile_liqvol_63d_base_v027_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _std(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of dollar-volume over 126d (relative liquidity dispersion)
def f14lq_f14_liquidity_profile_liqcv_126d_base_v028_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    m = _mean(dv, 126).replace(0, np.nan)
    sd = _std(dv, 126)
    b = sd / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of Amihud illiquidity over 252d (instability of trading cost)
def f14lq_f14_liquidity_profile_illiqvol_252d_base_v029_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    b = _std(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composites / interactions ---
# illiquidity-volatility co-movement: corr of weekly Amihud changes with realized-vol changes (63d)
def f14lq_f14_liquidity_profile_amihudvol_63d_base_v030_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 5).clip(lower=0)).diff()
    vol = closeadj.pct_change().rolling(5, min_periods=3).std()
    vchg = vol.diff()
    b = a.rolling(63, min_periods=21).corr(vchg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-depth resilience: dollar-liquidity per unit intraday range, z-scored vs 252d (21d)
def f14lq_f14_liquidity_profile_resilience_21d_base_v031_signal(high, low, closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    rng = (high - low) / closeadj.replace(0, np.nan)
    depth = np.log((dv / rng.replace(0, np.nan)).replace(0, np.nan))
    b = _z(depth.rolling(21, min_periods=10).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover x VWAP-deviation magnitude (active mispricing under heavy trade)
def f14lq_f14_liquidity_profile_turnxslip_21d_base_v032_signal(high, low, closeadj, volume):
    t = _f14_turnover(volume, 63)
    slip = _f14_vwap_dev(high, low, closeadj, volume, 21).abs()
    b = t * slip
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity 21d minus its own 252d mean (illiquidity surprise)
def f14lq_f14_liquidity_profile_illiqsurprise_21d_base_v033_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 21)
    al = np.log1p(a.clip(lower=0))
    b = al - al.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity momentum balance: net of up vs down day-on-day log changes over 63d
def f14lq_f14_liquidity_profile_liqhitrate_63d_base_v034_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    up = chg.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-chg.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud asymmetry: illiquidity on down-return days vs up-return days
def f14lq_f14_liquidity_profile_illiqasym_63d_base_v035_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = ret.abs() / dv
    down = illiq.where(ret < 0)
    up = illiq.where(ret > 0)
    dn = down.rolling(63, min_periods=15).mean()
    um = up.rolling(63, min_periods=15).mean()
    b = (dn - um) / (dn + um).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle-lambda regression: slope of |return| on contemporaneous dollar-volume over 63d (impact sensitivity)
def f14lq_f14_liquidity_profile_kyle_63d_base_v036_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f14_dollar_vol(closeadj, volume) / 1e6
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    b = -(cov / var)  # more negative slope = deeper market (impact falls as volume rises)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity skew: skewness of log dollar-volume over 126d (sporadic spike profile)
def f14lq_f14_liquidity_profile_liqskew_126d_base_v037_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = dv.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP deviation persistence: fraction of 63d trading above VWAP (anchor side)
def f14lq_f14_liquidity_profile_vwapside_63d_base_v038_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    above = (d > 0).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover dispersion: std of daily relative-volume over 63d (lumpy participation)
def f14lq_f14_liquidity_profile_turndisp_63d_base_v039_signal(volume):
    rel = _f14_turnover(volume, 126)
    b = _std(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity vs price level: liquidity per unit price (share-volume tilt), log
def f14lq_f14_liquidity_profile_liqperprice_63d_base_v040_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 63)
    px = _mean(closeadj, 63).replace(0, np.nan)
    b = np.log((dv / px).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity acceleration proxy: 21d Amihud relative to 63d Amihud (impact ramp)
def f14lq_f14_liquidity_profile_illiqramp_21v63_base_v041_signal(closeadj, volume):
    s = _f14_amihud(closeadj, volume, 21).clip(lower=1e-12)
    m = _f14_amihud(closeadj, volume, 63).clip(lower=1e-12)
    b = np.log(s / m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP execution cost in path units: |close-VWAP| vs cumulative 21d range traveled (impact efficiency)
def f14lq_f14_liquidity_profile_vwapatr_21d_base_v042_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21).abs()
    path = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = d / path
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend acceleration: 63d liquidity slope minus 126d liquidity slope
def f14lq_f14_liquidity_profile_liqtrendspr_63v126_base_v043_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    s = _slope(dv, 63)
    l = _slope(dv, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover regime: log-ratio of 21d participation to 504d participation (multi-year activity shift)
def f14lq_f14_liquidity_profile_turnregime_504d_base_v044_signal(volume):
    short = _mean(volume, 21)
    long = _mean(volume, 504).replace(0, np.nan)
    b = np.log(short / long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-vs-impact composition: intraday range cost relative to Amihud return-impact (cost mix)
def f14lq_f14_liquidity_profile_spreadcost_21d_base_v045_signal(high, low, closeadj, volume):
    spr = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    aret = closeadj.pct_change().abs().rolling(21, min_periods=10).mean().replace(0, np.nan)
    b = np.log((spr / aret).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud z over 63d vs own 504d distribution (long-horizon illiquidity stress)
def f14lq_f14_liquidity_profile_illiqstress_504d_base_v046_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 63)
    b = _z(np.log1p(a.clip(lower=0)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity drawdown: current dollar-liquidity vs its trailing 252d peak (dry-up depth)
def f14lq_f14_liquidity_profile_liqdrawdown_252d_base_v047_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21)
    peak = dv.rolling(252, min_periods=126).max().replace(0, np.nan)
    b = dv / peak - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity recovery: current dollar-liquidity vs its trailing 252d trough
def f14lq_f14_liquidity_profile_liqrecovery_252d_base_v048_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21)
    trough = dv.rolling(252, min_periods=126).min().replace(0, np.nan)
    b = np.log(dv / trough)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP deviation volatility over 63d (execution-anchor instability)
def f14lq_f14_liquidity_profile_vwapvol_63d_base_v049_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = _std(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover momentum: change in log turnover-base over a month
def f14lq_f14_liquidity_profile_turnmom_21d_base_v050_signal(volume):
    base = np.log(_mean(volume, 21).replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity vs liquidity-vol interaction (costly AND unstable trading)
def f14lq_f14_liquidity_profile_costinstab_126d_base_v051_signal(closeadj, volume):
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    cv = _z(_std(dv, 63), 252)
    b = a + cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative illiquidity floor: 63d min dollar-liquidity vs its 252d median (worst-day tradability)
def f14lq_f14_liquidity_profile_illiqdays_63d_base_v052_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(252, min_periods=126).median().replace(0, np.nan)
    floor = dv.rolling(63, min_periods=21).min()
    b = floor / med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed liquidity flow: dollar-volume on up days minus down days over 63d (direction)
def f14lq_f14_liquidity_profile_liqflow_63d_base_v053_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud over 21d in absolute (untransformed) units ranked over 252d
def f14lq_f14_liquidity_profile_amihudrank_21d_base_v054_signal(closeadj, volume):
    a = _f14_amihud(closeadj, volume, 21)
    b = _rank(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity concentration: share of 63d dollar-volume on the single busiest day
def f14lq_f14_liquidity_profile_liqconc_63d_base_v055_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = mx / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP-deviation mean-reversion: 21d deviation minus its own 63d average
def f14lq_f14_liquidity_profile_vwaprev_63d_base_v056_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = d - d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-vs-illiquidity gap: high turnover but high impact (fragile liquidity)
def f14lq_f14_liquidity_profile_fragility_63d_base_v057_signal(closeadj, volume):
    t = _z(_mean(volume, 21), 252)
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    b = t + a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity trend over 252d (annual liquidity drift)
def f14lq_f14_liquidity_profile_liqtrend_252d_base_v058_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    b = _slope(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud half-life proxy: ratio of recent vs older illiquidity within 126d
def f14lq_f14_liquidity_profile_illiqdecay_126d_base_v059_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    recent = a.rolling(42, min_periods=21).mean()
    older = a.shift(63).rolling(42, min_periods=21).mean()
    b = recent - older
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-adjusted return: 21d return scaled by Amihud illiquidity (impact-aware mom)
def f14lq_f14_liquidity_profile_liqadjret_21d_base_v060_signal(closeadj, volume):
    ret = closeadj.pct_change(21)
    a = np.sqrt(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    b = ret / a.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-based illiquidity surprise: 63d high-low-per-share impact, z-scored vs its 252d norm
def f14lq_f14_liquidity_profile_rangeilliq_63d_base_v061_signal(high, low, volume):
    spr = (high - low)
    illiq = np.log1p(((spr / volume.replace(0, np.nan)) * 1e6).clip(lower=0))
    b = _z(illiq.rolling(63, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover entropy proxy: dispersion of relative volume shares over 63d (even vs spiky)
def f14lq_f14_liquidity_profile_turnentropy_63d_base_v062_signal(volume):
    tot = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    share = volume / tot
    sq = (share * share).rolling(63, min_periods=21).sum()
    b = sq  # Herfindahl of daily volume shares (concentration)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity beta to its own volatility: corr of dollar-vol changes with |return|
def f14lq_f14_liquidity_profile_volliqcorr_126d_base_v063_signal(closeadj, volume):
    dvc = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)).diff()
    aret = closeadj.pct_change().abs()
    b = dvc.rolling(126, min_periods=63).corr(aret)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity tail spread: gap between 95th and 50th pct daily Amihud over 126d (tail-impact dispersion)
def f14lq_f14_liquidity_profile_illiqtail_126d_base_v064_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = (ret / dv * 1e9)
    hi = illiq.rolling(126, min_periods=63).quantile(0.95)
    md = illiq.rolling(126, min_periods=63).quantile(0.50).replace(0, np.nan)
    b = np.log1p((hi / md).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-uptrend occupancy: fraction of last 252d that 21d liquidity sits above its 63d average
def f14lq_f14_liquidity_profile_liqupstreak_63d_base_v065_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    fast = _mean(dv, 21)
    slow = _mean(dv, 63)
    above = (fast > slow).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP deviation skew over 126d (asymmetric execution premium)
def f14lq_f14_liquidity_profile_vwapskew_126d_base_v066_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    b = d.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity coefficient of variation trend (liquidity stability improving?)
def f14lq_f14_liquidity_profile_liqcvtrend_126d_base_v067_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    cv = _std(dv, 63) / _mean(dv, 63).replace(0, np.nan)
    b = _slope(cv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud impact oscillator: fast EMA minus slow EMA of log-illiquidity (impact regime swing)
def f14lq_f14_liquidity_profile_illiqema_63d_base_v068_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = np.log1p((ret / dv * 1e9).clip(lower=0))
    fast = illiq.ewm(span=21, min_periods=10).mean()
    slow = illiq.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depth regime shift: 21d market-depth (dv per unit move) relative to its 126d depth (deepening/thinning)
def f14lq_f14_liquidity_profile_depth_63d_base_v069_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    move = closeadj.pct_change().abs()
    depth_s = dv.rolling(21, min_periods=10).sum() / move.rolling(21, min_periods=10).sum().replace(0, np.nan)
    depth_l = dv.rolling(126, min_periods=63).sum() / move.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = np.log((depth_s / depth_l.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity seasonality proxy: 21d liquidity vs same level 252d ago (YoY liquidity)
def f14lq_f14_liquidity_profile_liqyoy_252d_base_v070_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    b = dv - dv.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity convexity: squared deviation of Amihud from its own 126d mean
def f14lq_f14_liquidity_profile_illiqconvex_126d_base_v071_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    m = a.rolling(126, min_periods=63).mean()
    sd = a.rolling(126, min_periods=63).std().replace(0, np.nan)
    z = (a - m) / sd
    b = np.sign(z) * (z * z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-median liquidity-day intensity: avg excess of dollar-vol over its 126d median, when above (63d)
def f14lq_f14_liquidity_profile_liqbreadth_126d_base_v072_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(126, min_periods=63).median().replace(0, np.nan)
    excess = (dv / med - 1.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-weighted VWAP gap: signed execution premium scaled by participation
def f14lq_f14_liquidity_profile_turnvwap_21d_base_v073_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    t = _z(_mean(volume, 21), 252)
    b = d * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity regime gap: 63d Amihud rank minus 252d Amihud rank (regime divergence)
def f14lq_f14_liquidity_profile_illiqregimegap_base_v074_signal(closeadj, volume):
    a63 = _f14_amihud(closeadj, volume, 63)
    a252 = _f14_amihud(closeadj, volume, 252)
    r63 = _rank(a63, 252)
    r252 = _rank(a252, 504)
    b = r63 - r252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite tradability score: high dollar-liquidity, low Amihud, low VWAP slippage
def f14lq_f14_liquidity_profile_tradability_63d_base_v075_signal(high, low, closeadj, volume):
    liq = _z(np.log(_mean(_f14_dollar_vol(closeadj, volume), 63).replace(0, np.nan)), 252)
    illiq = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    slip = _z(_f14_vwap_dev(high, low, closeadj, volume, 21).abs().rolling(63, min_periods=21).mean(), 252)
    b = liq - illiq - slip
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14lq_f14_liquidity_profile_amihud_21d_base_v001_signal,
    f14lq_f14_liquidity_profile_amihud_63d_base_v002_signal,
    f14lq_f14_liquidity_profile_amihud_126d_base_v003_signal,
    f14lq_f14_liquidity_profile_amihud_252d_base_v004_signal,
    f14lq_f14_liquidity_profile_amihudratio_21v252_base_v005_signal,
    f14lq_f14_liquidity_profile_dollarliq_21d_base_v006_signal,
    f14lq_f14_liquidity_profile_dollarliq_63d_base_v007_signal,
    f14lq_f14_liquidity_profile_dollarliqz_126d_base_v008_signal,
    f14lq_f14_liquidity_profile_dollarliqrank_63d_base_v009_signal,
    f14lq_f14_liquidity_profile_dollarliqfloor_63d_base_v010_signal,
    f14lq_f14_liquidity_profile_turnover_5v63_base_v011_signal,
    f14lq_f14_liquidity_profile_turnover_21v126_base_v012_signal,
    f14lq_f14_liquidity_profile_turnoverz_21d_base_v013_signal,
    f14lq_f14_liquidity_profile_turnoverrank_21d_base_v014_signal,
    f14lq_f14_liquidity_profile_vwapdev_21d_base_v015_signal,
    f14lq_f14_liquidity_profile_vwapdev_63d_base_v016_signal,
    f14lq_f14_liquidity_profile_vwapdev_126d_base_v017_signal,
    f14lq_f14_liquidity_profile_vwapdevspr_21v126_base_v018_signal,
    f14lq_f14_liquidity_profile_vwapslip_63d_base_v019_signal,
    f14lq_f14_liquidity_profile_liqtrend_63d_base_v020_signal,
    f14lq_f14_liquidity_profile_liqtrend_126d_base_v021_signal,
    f14lq_f14_liquidity_profile_liqmom_63d_base_v022_signal,
    f14lq_f14_liquidity_profile_illiqtrend_126d_base_v023_signal,
    f14lq_f14_liquidity_profile_thinfrac_63d_base_v024_signal,
    f14lq_f14_liquidity_profile_thinstreak_63d_base_v025_signal,
    f14lq_f14_liquidity_profile_dryup_126d_base_v026_signal,
    f14lq_f14_liquidity_profile_liqvol_63d_base_v027_signal,
    f14lq_f14_liquidity_profile_liqcv_126d_base_v028_signal,
    f14lq_f14_liquidity_profile_illiqvol_252d_base_v029_signal,
    f14lq_f14_liquidity_profile_amihudvol_63d_base_v030_signal,
    f14lq_f14_liquidity_profile_resilience_21d_base_v031_signal,
    f14lq_f14_liquidity_profile_turnxslip_21d_base_v032_signal,
    f14lq_f14_liquidity_profile_illiqsurprise_21d_base_v033_signal,
    f14lq_f14_liquidity_profile_liqhitrate_63d_base_v034_signal,
    f14lq_f14_liquidity_profile_illiqasym_63d_base_v035_signal,
    f14lq_f14_liquidity_profile_kyle_63d_base_v036_signal,
    f14lq_f14_liquidity_profile_liqskew_126d_base_v037_signal,
    f14lq_f14_liquidity_profile_vwapside_63d_base_v038_signal,
    f14lq_f14_liquidity_profile_turndisp_63d_base_v039_signal,
    f14lq_f14_liquidity_profile_liqperprice_63d_base_v040_signal,
    f14lq_f14_liquidity_profile_illiqramp_21v63_base_v041_signal,
    f14lq_f14_liquidity_profile_vwapatr_21d_base_v042_signal,
    f14lq_f14_liquidity_profile_liqtrendspr_63v126_base_v043_signal,
    f14lq_f14_liquidity_profile_turnregime_504d_base_v044_signal,
    f14lq_f14_liquidity_profile_spreadcost_21d_base_v045_signal,
    f14lq_f14_liquidity_profile_illiqstress_504d_base_v046_signal,
    f14lq_f14_liquidity_profile_liqdrawdown_252d_base_v047_signal,
    f14lq_f14_liquidity_profile_liqrecovery_252d_base_v048_signal,
    f14lq_f14_liquidity_profile_vwapvol_63d_base_v049_signal,
    f14lq_f14_liquidity_profile_turnmom_21d_base_v050_signal,
    f14lq_f14_liquidity_profile_costinstab_126d_base_v051_signal,
    f14lq_f14_liquidity_profile_illiqdays_63d_base_v052_signal,
    f14lq_f14_liquidity_profile_liqflow_63d_base_v053_signal,
    f14lq_f14_liquidity_profile_amihudrank_21d_base_v054_signal,
    f14lq_f14_liquidity_profile_liqconc_63d_base_v055_signal,
    f14lq_f14_liquidity_profile_vwaprev_63d_base_v056_signal,
    f14lq_f14_liquidity_profile_fragility_63d_base_v057_signal,
    f14lq_f14_liquidity_profile_liqtrend_252d_base_v058_signal,
    f14lq_f14_liquidity_profile_illiqdecay_126d_base_v059_signal,
    f14lq_f14_liquidity_profile_liqadjret_21d_base_v060_signal,
    f14lq_f14_liquidity_profile_rangeilliq_63d_base_v061_signal,
    f14lq_f14_liquidity_profile_turnentropy_63d_base_v062_signal,
    f14lq_f14_liquidity_profile_volliqcorr_126d_base_v063_signal,
    f14lq_f14_liquidity_profile_illiqtail_126d_base_v064_signal,
    f14lq_f14_liquidity_profile_liqupstreak_63d_base_v065_signal,
    f14lq_f14_liquidity_profile_vwapskew_126d_base_v066_signal,
    f14lq_f14_liquidity_profile_liqcvtrend_126d_base_v067_signal,
    f14lq_f14_liquidity_profile_illiqema_63d_base_v068_signal,
    f14lq_f14_liquidity_profile_depth_63d_base_v069_signal,
    f14lq_f14_liquidity_profile_liqyoy_252d_base_v070_signal,
    f14lq_f14_liquidity_profile_illiqconvex_126d_base_v071_signal,
    f14lq_f14_liquidity_profile_liqbreadth_126d_base_v072_signal,
    f14lq_f14_liquidity_profile_turnvwap_21d_base_v073_signal,
    f14lq_f14_liquidity_profile_illiqregimegap_base_v074_signal,
    f14lq_f14_liquidity_profile_tradability_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_LIQUIDITY_PROFILE_REGISTRY_001_075 = REGISTRY


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

    print("OK f14_liquidity_profile_base_001_075_claude: %d features pass" % n_features)
