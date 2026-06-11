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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== f16 illiquidity / trading-cost RATIO primitives =====
# Domain: cost-of-trading and price-impact RATIOS only.
#   - Amihud illiquidity = |ret| / dollar-volume   (impact PER DOLLAR)
#   - Corwin-Schultz high-low SPREAD estimator      (the spread formula)
#   - Roll effective-spread from serial covariance
#   - turnover (volume vs its OWN average, a ratio)
#   - zero/thin-volume dry-up streaks
# NOT raw high-low range, NOT raw up/down volume, NOT dollar-volume LEVEL.

def _f16_dollar_vol(closeadj, volume):
    # dollar-volume = closeadj * volume; used only inside RATIO denominators.
    return (closeadj * volume).replace(0, np.nan)


def _f16_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))


def _f16_amihud_daily(closeadj, volume):
    # daily Amihud illiquidity ratio: |ret| per $million traded, scaled
    dv = _f16_dollar_vol(closeadj, volume)
    r = _f16_logret(closeadj).abs()
    return (r / dv) * 1e9


def _f16_amihud(closeadj, volume, w):
    d = _f16_amihud_daily(closeadj, volume)
    return d.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_amihud_med(closeadj, volume, w):
    d = _f16_amihud_daily(closeadj, volume)
    return d.rolling(w, min_periods=max(1, w // 2)).median()


def _f16_turnover(volume, w):
    # turnover proxy: volume relative to its own trailing average (a ratio)
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_cs_spread(high, low):
    # Corwin-Schultz high-low SPREAD estimator (effective bid-ask spread).
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    beta = hl + hl.shift(1)
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = np.log(h2.replace(0, np.nan) / l2.replace(0, np.nan)) ** 2
    k = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    alpha = alpha.clip(lower=0)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread


def _f16_roll_spread(closeadj, w):
    # Roll effective spread = 2*sqrt(-cov(dP, dP_lag)) / price
    dp = closeadj.diff()
    cov = dp.rolling(w, min_periods=max(1, w // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0)) / closeadj.replace(0, np.nan)


def _f16_kyle(closeadj, volume, w):
    # Kyle-lambda style price impact: |ret| / sqrt(dollar-volume)
    r = _f16_logret(closeadj).abs()
    dv = _f16_dollar_vol(closeadj, volume)
    lam = (r / np.sqrt(dv)) * 1e4
    return lam.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_thin_flag(volume, w, q):
    thresh = volume.rolling(w, min_periods=max(1, w // 2)).quantile(q)
    return (volume <= thresh).astype(float)


def _f16_streak(flag):
    grp = (flag != flag.shift(1)).cumsum()
    run = flag.groupby(grp).cumcount() + 1
    return (run * flag).astype(float)


# ============================================================
# === Amihud illiquidity ratio (impact per dollar) — level / windows ===
# 21d short robust illiquidity: median daily impact ratio (recent cost floor)
def f16lq_f16_liquidity_profile_amihud_21d_base_v001_signal(closeadj, volume):
    b = np.log1p(_f16_amihud_med(closeadj, volume, 21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihud_63d_base_v002_signal(closeadj, volume):
    b = np.log1p(_f16_amihud(closeadj, volume, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust illiquidity: median daily impact ratio (outlier-resistant cost level)
def f16lq_f16_liquidity_profile_amihud_126d_base_v003_signal(closeadj, volume):
    b = np.log1p(_f16_amihud_med(closeadj, volume, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihud_252d_base_v004_signal(closeadj, volume):
    b = np.log1p(_f16_amihud(closeadj, volume, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud EWMA displacement: fast vs slow recency-weighted illiquidity ratio
def f16lq_f16_liquidity_profile_amihudewma_63d_base_v005_signal(closeadj, volume):
    daily = np.log1p(_f16_amihud_daily(closeadj, volume))
    fast = daily.ewm(span=21, min_periods=10).mean()
    slow = daily.ewm(span=126, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud up/down asymmetry: illiquidity ratio on down days minus up days
def f16lq_f16_liquidity_profile_amihudasym_252d_base_v006_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    r = _f16_logret(closeadj)
    dn = daily.where(r < 0).rolling(252, min_periods=126).mean()
    up = daily.where(r > 0).rolling(252, min_periods=126).mean()
    b = np.log1p(dn) - np.log1p(up)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud z-score (de-trended illiquidity ratio)
def f16lq_f16_liquidity_profile_amihudz_63d_base_v007_signal(closeadj, volume):
    b = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihudz_126d_base_v008_signal(closeadj, volume):
    b = _z(np.log1p(_f16_amihud(closeadj, volume, 126)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud percentile rank
def f16lq_f16_liquidity_profile_amihudrank_63d_base_v009_signal(closeadj, volume):
    b = _rank(_f16_amihud(closeadj, volume, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihudrank_252d_base_v010_signal(closeadj, volume):
    b = _rank(_f16_amihud(closeadj, volume, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud mean-minus-median (tail skew of the daily impact ratio)
def f16lq_f16_liquidity_profile_amihudtailskew_63d_base_v011_signal(closeadj, volume):
    mean = _f16_amihud(closeadj, volume, 63)
    med = _f16_amihud_med(closeadj, volume, 63)
    b = (mean - med) / (mean + med).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud short/long ratio (illiquidity term structure)
def f16lq_f16_liquidity_profile_amihudratio_21v126_base_v012_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 21)
    l = _f16_amihud(closeadj, volume, 126)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihudratio_63v252_base_v013_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 63)
    l = _f16_amihud(closeadj, volume, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud trend (illiquidity ratio worsening/improving)
def f16lq_f16_liquidity_profile_amihudtrend_63d_base_v014_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_amihudtrend_126d_base_v015_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 126))
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud dispersion (CV of the daily impact ratio = instability of trading cost)
def f16lq_f16_liquidity_profile_amihuddisp_63d_base_v016_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    m = daily.rolling(63, min_periods=31).mean()
    sd = daily.rolling(63, min_periods=31).std()
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud spike prevalence (excess impact days above the median ratio)
def f16lq_f16_liquidity_profile_amihudspike_63d_base_v017_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    med = daily.rolling(126, min_periods=63).median().replace(0, np.nan)
    excess = (daily / med - 1.0).clip(lower=0)
    b = excess.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Inverse-Amihud depth ratio (dollar traded per unit of move) z-scored
def f16lq_f16_liquidity_profile_depthratioz_126d_base_v018_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    depth = dv / (_f16_logret(closeadj).abs() * 1e9 + 1.0)
    b = _z(np.log1p(depth.rolling(21, min_periods=10).mean()), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Turnover RATIO (volume vs own average) facets ===
# relative-volume depth level: log of monthly-avg turnover vs its 126d baseline
def f16lq_f16_liquidity_profile_turnover_21d_base_v019_signal(volume):
    fast = _mean(volume, 21)
    base = _mean(volume, 126)
    b = np.log(fast.replace(0, np.nan) / base.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio persistence (autocorrelation of the relative-volume ratio)
def f16lq_f16_liquidity_profile_turnac1_63d_base_v020_signal(volume):
    t = _f16_turnover(volume, 63)
    b = t.rolling(63, min_periods=31).corr(t.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# where the smoothed turnover ratio sits in its own 126d range (regime position)
def f16lq_f16_liquidity_profile_turnrangepos_126d_base_v021_signal(volume):
    t = _f16_turnover(volume, 21).rolling(21, min_periods=10).mean()
    hi = _rmax(t, 126)
    lo = _rmin(t, 126)
    b = (t - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio asymmetry: median-to-mean gap of relative volume (burst skew)
def f16lq_f16_liquidity_profile_turnburstskew_63d_base_v022_signal(volume):
    t = _f16_turnover(volume, 252)
    m = t.rolling(63, min_periods=31).mean()
    med = t.rolling(63, min_periods=31).median()
    b = (m - med) / (m + med).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio z-score on the slow (63d) relative-volume drift: regime distance
def f16lq_f16_liquidity_profile_turnz_252d_base_v023_signal(volume):
    slow = _f16_turnover(volume, 21).rolling(63, min_periods=31).mean()
    b = _z(slow, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio percentile rank (smoothed relative-volume regime)
def f16lq_f16_liquidity_profile_turnrank_252d_base_v024_signal(volume):
    t = _f16_turnover(volume, 21).rolling(10, min_periods=5).mean()
    b = _rank(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# chronic thinness depth: average shortfall of relative volume below 1 (illiquidity prevalence)
def f16lq_f16_liquidity_profile_turnthintime_63d_base_v025_signal(volume):
    t = _f16_turnover(volume, 21)
    deficit = (1.0 - t).clip(lower=0)
    b = (deficit ** 1.5).rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio inter-quantile span (relative-volume dispersion, robust)
def f16lq_f16_liquidity_profile_turnspan_252d_base_v026_signal(volume):
    t = _f16_turnover(volume, 5)
    hi = t.rolling(252, min_periods=126).quantile(0.9)
    lo = t.rolling(252, min_periods=126).quantile(0.1)
    b = np.log1p(hi) - np.log1p(lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio trend: relative-volume drift over a half year
def f16lq_f16_liquidity_profile_turntrend_126d_base_v027_signal(volume):
    t = np.log1p(_f16_turnover(volume, 63))
    b = t - t.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio acceleration: fast vs slow relative-volume
def f16lq_f16_liquidity_profile_turnfastslow_base_v028_signal(volume):
    f = _f16_turnover(volume, 21)
    s = _f16_turnover(volume, 126)
    b = np.log1p(f) - np.log1p(s)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio rebound off its trough (relative-volume recovery)
def f16lq_f16_liquidity_profile_turnrebound_63d_base_v029_signal(volume):
    t = _f16_turnover(volume, 5)
    trough = _rmin(t, 63)
    b = np.log1p(t) - np.log1p(trough)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio weekly rhythm: lag-5 autocorrelation of relative volume
def f16lq_f16_liquidity_profile_turndisp_63d_base_v030_signal(volume):
    t = np.log1p(_f16_turnover(volume, 63))
    b = t.rolling(126, min_periods=63).corr(t.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-vs-turnover divergence: high impact while turnover is high (fragile depth)
def f16lq_f16_liquidity_profile_fragiledepth_63d_base_v031_signal(closeadj, volume):
    illiq = _rank(_f16_amihud(closeadj, volume, 63), 252)
    turn = _rank(_f16_turnover(volume, 21), 252)
    b = illiq + turn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Thin / zero-volume dry-up facets (counts/streaks/depth) ===
# thin-day prevalence: depth below the 25th-pct volume floor
def f16lq_f16_liquidity_profile_thinfrac_63d_base_v032_signal(volume):
    thresh = volume.rolling(126, min_periods=63).quantile(0.25)
    deficit = ((thresh - volume) / thresh.replace(0, np.nan)).clip(lower=0)
    b = deficit.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_thinfrac_126d_base_v033_signal(volume):
    thresh = volume.rolling(252, min_periods=126).quantile(0.20)
    deficit = ((thresh - volume) / thresh.replace(0, np.nan)).clip(lower=0)
    b = deficit.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current thin-volume streak (consecutive thin days), depth-weighted
def f16lq_f16_liquidity_profile_thinstreak_base_v034_signal(volume):
    avg = _mean(volume, 126)
    flag = (volume < 0.7 * avg).astype(float)
    st = _f16_streak(flag)
    deficit = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0)
    b = st + deficit
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max thin streak over the last quarter blended with avg thin depth
def f16lq_f16_liquidity_profile_maxthinstreak_63d_base_v035_signal(volume):
    avg = _mean(volume, 126)
    flag = (volume < 0.7 * avg).astype(float)
    st = _f16_streak(flag)
    deficit = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0)
    b = _rmax(st, 63) + 5.0 * deficit.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-day relative-volume drought, smoothed
def f16lq_f16_liquidity_profile_worstvol_126d_base_v036_signal(volume):
    avg = _mean(volume, 252)
    rel = volume / avg.replace(0, np.nan)
    worst = _rmin(rel, 21)
    b = (1.0 - worst).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-volume-day count over the year, depth-weighted
def f16lq_f16_liquidity_profile_lowvolcount_252d_base_v037_signal(volume):
    avg = _mean(volume, 252)
    low = (volume < 0.5 * avg).astype(float)
    deficit = (0.5 - volume / avg.replace(0, np.nan)).clip(lower=0)
    b = _rsum(low, 252) + 10.0 * _rsum(deficit, 252) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-drought entries: how often relative volume dips into a drought regime
def f16lq_f16_liquidity_profile_droughtentry_252d_base_v038_signal(volume):
    ratio = _mean(volume, 21) / volume.rolling(252, min_periods=126).median().replace(0, np.nan)
    below = (ratio < 0.9).astype(float)
    entries = ((below == 1) & (below.shift(1) == 0)).astype(float)
    sev = (0.9 - ratio).clip(lower=0)
    b = _rsum(entries, 252) + 30.0 * sev.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-freeze depth: how far below normal volume sits when thin
def f16lq_f16_liquidity_profile_freezedepth_63d_base_v039_signal(volume):
    avg = _mean(volume, 252)
    deficit = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0)
    b = deficit.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Corwin-Schultz SPREAD estimator facets (the spread, not range) ===
def f16lq_f16_liquidity_profile_csspread_21d_base_v040_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_csspread_63d_base_v041_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_csspread_126d_base_v042_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread expansion vs its own trailing minimum (squeeze release)
def f16lq_f16_liquidity_profile_csspreadexp_63d_base_v043_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    floor = _rmin(s, 252)
    b = s / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread percentile rank
def f16lq_f16_liquidity_profile_csspreadrank_252d_base_v044_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread trend (transaction-cost drift)
def f16lq_f16_liquidity_profile_csspreadtrend_126d_base_v045_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread short/long ratio
def f16lq_f16_liquidity_profile_csspreadratio_21v126_base_v046_signal(high, low):
    s = _f16_cs_spread(high, low)
    short = s.rolling(21, min_periods=10).mean()
    long = s.rolling(126, min_periods=63).mean()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread dispersion (instability of the spread estimator)
def f16lq_f16_liquidity_profile_csspreaddisp_63d_base_v047_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(63, min_periods=31).std() / s.rolling(63, min_periods=31).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread acceleration: spread trend now vs a quarter ago (cost curvature)
def f16lq_f16_liquidity_profile_csspreadz_252d_base_v048_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    tr = s - s.shift(63)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread squeeze-time: fraction of quarter the spread sits below its median (cheap regime)
def f16lq_f16_liquidity_profile_csspreadcheaptime_63d_base_v049_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(5, min_periods=3).mean()
    med = s.rolling(252, min_periods=126).median()
    below = (s < med).astype(float)
    b = below.rolling(63, min_periods=31).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread per unit volatility: cost paid above what risk alone implies
def f16lq_f16_liquidity_profile_csspreadpervol_252d_base_v050_signal(high, low, closeadj):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    b = _z(s / vol.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-per-dollar-traded: CS spread carried per unit of relative turnover (cost intensity)
def f16lq_f16_liquidity_profile_spreadperturn_63d_base_v051_signal(high, low, volume):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    turn = _f16_turnover(volume, 252).rolling(21, min_periods=10).mean()
    b = _z(np.log1p(s / turn.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Roll effective-spread (serial-covariance) facets ===
def f16lq_f16_liquidity_profile_rollspread_63d_base_v052_signal(closeadj):
    b = _f16_roll_spread(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_rollspread_126d_base_v053_signal(closeadj):
    b = _f16_roll_spread(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread z-score
def f16lq_f16_liquidity_profile_rollspreadz_252d_base_v054_signal(closeadj):
    sp = _f16_roll_spread(closeadj, 63)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Illiquidity regime / interaction RATIO facets ===
# illiquidity stress: short vs long Amihud ratio (acute cost spike)
def f16lq_f16_liquidity_profile_illiqstress_21v252_base_v055_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 21)
    l = _f16_amihud(closeadj, volume, 252)
    b = np.log1p(s) - np.log1p(l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity acceleration-as-level: fast vs slow Amihud ratio
def f16lq_f16_liquidity_profile_illiqfastslow_base_v056_signal(closeadj, volume):
    f = np.log1p(_f16_amihud(closeadj, volume, 21))
    s = np.log1p(_f16_amihud(closeadj, volume, 126))
    b = f - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity persistence: fraction of quarter Amihud above its 252d median
def f16lq_f16_liquidity_profile_illiqpersist_63d_base_v057_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(252, min_periods=126).median()
    above = (a > med).astype(float)
    high = (a / med.replace(0, np.nan) - 1.0).clip(lower=0)
    b = above.rolling(63, min_periods=31).mean() + 0.2 * high.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-improvement streak (consecutive days Amihud below its MA), depth weighted
def f16lq_f16_liquidity_profile_illiqdownstreak_base_v058_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    ma = a.rolling(63, min_periods=31).mean()
    flag = (a < ma).astype(float)
    st = _f16_streak(flag)
    gap = (1.0 - a / ma.replace(0, np.nan)).clip(lower=0)
    b = st + gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-momentum interaction: impact ratio x signed drift
def f16lq_f16_liquidity_profile_illiqret_63d_base_v059_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = a * np.sign(ret) * ret.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-per-volatility ratio, percentile-ranked (cost-vs-risk regime)
def f16lq_f16_liquidity_profile_illiqvol_63d_base_v060_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    b = _rank(a / vol.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity x drawdown: thin names that crash (gaming-miss fragility)
def f16lq_f16_liquidity_profile_illiqcrash_63d_base_v061_signal(closeadj, volume):
    a = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    peak = _rmax(closeadj, 252)
    dd = (closeadj / peak.replace(0, np.nan) - 1.0)
    b = a * (-dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-drift correlation: do illiquid periods coincide with negative drift
def f16lq_f16_liquidity_profile_illiqdrift_126d_base_v062_signal(closeadj, volume):
    a = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    drift = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    b = a.rolling(126, min_periods=63).corr(drift)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Kyle price-impact RATIO facets ===
# Kyle impact term structure: short vs long price-impact ratio
def f16lq_f16_liquidity_profile_kyle_63d_base_v063_signal(closeadj, volume):
    s = _f16_kyle(closeadj, volume, 21)
    l = _f16_kyle(closeadj, volume, 252)
    b = np.log1p(s) - np.log1p(l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f16lq_f16_liquidity_profile_kylerank_63d_base_v064_signal(closeadj, volume):
    b = _rank(_f16_kyle(closeadj, volume, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle up/down impact asymmetry: price-impact ratio on down vs up days (cost direction)
def f16lq_f16_liquidity_profile_kylesigned_63d_base_v065_signal(closeadj, volume):
    r = _f16_logret(closeadj)
    dv = _f16_dollar_vol(closeadj, volume)
    lam = (r.abs() / np.sqrt(dv)) * 1e4
    dn = lam.where(r < 0).rolling(63, min_periods=20).mean()
    up = lam.where(r > 0).rolling(63, min_periods=20).mean()
    b = (dn - up) / (dn + up).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Microstructure / stale-price illiquidity facets ===
# bid-ask-bounce signature: negative lag-1 return autocorrelation
def f16lq_f16_liquidity_profile_retac1_63d_base_v066_signal(closeadj):
    r = _f16_logret(closeadj)
    b = -r.rolling(63, min_periods=31).corr(r.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stale-price / no-information days: prevalence of unusually small moves
def f16lq_f16_liquidity_profile_staleret_63d_base_v067_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    quiet = (1.0 - r / typ).clip(lower=0)
    b = quiet.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio deviation (1d vs 5d): non-random-walk illiquidity drag
def f16lq_f16_liquidity_profile_varratio_126d_base_v068_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(126, min_periods=63).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(126, min_periods=63).var()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Composite / cross-estimator RATIO facets ===
# Amihud convexity: signed-sqrt of de-meaned illiquidity ratio (tail emphasis)
def f16lq_f16_liquidity_profile_illiqsignmag_126d_base_v069_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    typ = a.rolling(126, min_periods=63).mean()
    d = a - typ
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-cost composite: blended CS spread + Amihud rank
def f16lq_f16_liquidity_profile_costcomposite_63d_base_v070_signal(closeadj, volume, high, low):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    s = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    b = 0.5 * (a + s)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triad cost: average rank of Amihud, CS spread, Roll spread
def f16lq_f16_liquidity_profile_costtriad_63d_base_v071_signal(closeadj, volume, high, low):
    ra = _rank(_f16_amihud(closeadj, volume, 63), 252)
    rc = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rr = _rank(_f16_roll_spread(closeadj, 63), 252)
    b = (ra + rc + rr) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud / CS-spread disagreement (impact vs quoted-spread divergence)
def f16lq_f16_liquidity_profile_impactspreadspr_63d_base_v072_signal(closeadj, volume, high, low):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    s = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    b = a - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity term-structure dispersion (cross-window cost disagreement)
def f16lq_f16_liquidity_profile_illiqtermdisp_base_v073_signal(closeadj, volume):
    a1 = np.log1p(_f16_amihud(closeadj, volume, 21))
    a2 = np.log1p(_f16_amihud(closeadj, volume, 63))
    a3 = np.log1p(_f16_amihud(closeadj, volume, 252))
    b = pd.concat([a1, a2, a3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS-vs-Roll spread disagreement: percentile-rank gap of two spread estimators
def f16lq_f16_liquidity_profile_spreadpervol_63d_base_v074_signal(high, low, closeadj):
    cs = _rank(_f16_cs_spread(high, low).rolling(63, min_periods=31).mean(), 252)
    roll = _rank(_f16_roll_spread(closeadj, 63), 252)
    b = cs - roll
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# master composite illiquidity score: Amihud z + spread z + thin-fraction
def f16lq_f16_liquidity_profile_illiqscore_base_v075_signal(closeadj, volume, high, low):
    az = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    sz = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    thin = _f16_thin_flag(volume, 126, 0.25).rolling(63, min_periods=31).mean()
    b = az + sz + 2.0 * (thin - 0.25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16lq_f16_liquidity_profile_amihud_21d_base_v001_signal,
    f16lq_f16_liquidity_profile_amihud_63d_base_v002_signal,
    f16lq_f16_liquidity_profile_amihud_126d_base_v003_signal,
    f16lq_f16_liquidity_profile_amihud_252d_base_v004_signal,
    f16lq_f16_liquidity_profile_amihudewma_63d_base_v005_signal,
    f16lq_f16_liquidity_profile_amihudasym_252d_base_v006_signal,
    f16lq_f16_liquidity_profile_amihudz_63d_base_v007_signal,
    f16lq_f16_liquidity_profile_amihudz_126d_base_v008_signal,
    f16lq_f16_liquidity_profile_amihudrank_63d_base_v009_signal,
    f16lq_f16_liquidity_profile_amihudrank_252d_base_v010_signal,
    f16lq_f16_liquidity_profile_amihudtailskew_63d_base_v011_signal,
    f16lq_f16_liquidity_profile_amihudratio_21v126_base_v012_signal,
    f16lq_f16_liquidity_profile_amihudratio_63v252_base_v013_signal,
    f16lq_f16_liquidity_profile_amihudtrend_63d_base_v014_signal,
    f16lq_f16_liquidity_profile_amihudtrend_126d_base_v015_signal,
    f16lq_f16_liquidity_profile_amihuddisp_63d_base_v016_signal,
    f16lq_f16_liquidity_profile_amihudspike_63d_base_v017_signal,
    f16lq_f16_liquidity_profile_depthratioz_126d_base_v018_signal,
    f16lq_f16_liquidity_profile_turnover_21d_base_v019_signal,
    f16lq_f16_liquidity_profile_turnac1_63d_base_v020_signal,
    f16lq_f16_liquidity_profile_turnrangepos_126d_base_v021_signal,
    f16lq_f16_liquidity_profile_turnburstskew_63d_base_v022_signal,
    f16lq_f16_liquidity_profile_turnz_252d_base_v023_signal,
    f16lq_f16_liquidity_profile_turnrank_252d_base_v024_signal,
    f16lq_f16_liquidity_profile_turnthintime_63d_base_v025_signal,
    f16lq_f16_liquidity_profile_turnspan_252d_base_v026_signal,
    f16lq_f16_liquidity_profile_turntrend_126d_base_v027_signal,
    f16lq_f16_liquidity_profile_turnfastslow_base_v028_signal,
    f16lq_f16_liquidity_profile_turnrebound_63d_base_v029_signal,
    f16lq_f16_liquidity_profile_turndisp_63d_base_v030_signal,
    f16lq_f16_liquidity_profile_fragiledepth_63d_base_v031_signal,
    f16lq_f16_liquidity_profile_thinfrac_63d_base_v032_signal,
    f16lq_f16_liquidity_profile_thinfrac_126d_base_v033_signal,
    f16lq_f16_liquidity_profile_thinstreak_base_v034_signal,
    f16lq_f16_liquidity_profile_maxthinstreak_63d_base_v035_signal,
    f16lq_f16_liquidity_profile_worstvol_126d_base_v036_signal,
    f16lq_f16_liquidity_profile_lowvolcount_252d_base_v037_signal,
    f16lq_f16_liquidity_profile_droughtentry_252d_base_v038_signal,
    f16lq_f16_liquidity_profile_freezedepth_63d_base_v039_signal,
    f16lq_f16_liquidity_profile_csspread_21d_base_v040_signal,
    f16lq_f16_liquidity_profile_csspread_63d_base_v041_signal,
    f16lq_f16_liquidity_profile_csspread_126d_base_v042_signal,
    f16lq_f16_liquidity_profile_csspreadexp_63d_base_v043_signal,
    f16lq_f16_liquidity_profile_csspreadrank_252d_base_v044_signal,
    f16lq_f16_liquidity_profile_csspreadtrend_126d_base_v045_signal,
    f16lq_f16_liquidity_profile_csspreadratio_21v126_base_v046_signal,
    f16lq_f16_liquidity_profile_csspreaddisp_63d_base_v047_signal,
    f16lq_f16_liquidity_profile_csspreadz_252d_base_v048_signal,
    f16lq_f16_liquidity_profile_csspreadcheaptime_63d_base_v049_signal,
    f16lq_f16_liquidity_profile_csspreadpervol_252d_base_v050_signal,
    f16lq_f16_liquidity_profile_spreadperturn_63d_base_v051_signal,
    f16lq_f16_liquidity_profile_rollspread_63d_base_v052_signal,
    f16lq_f16_liquidity_profile_rollspread_126d_base_v053_signal,
    f16lq_f16_liquidity_profile_rollspreadz_252d_base_v054_signal,
    f16lq_f16_liquidity_profile_illiqstress_21v252_base_v055_signal,
    f16lq_f16_liquidity_profile_illiqfastslow_base_v056_signal,
    f16lq_f16_liquidity_profile_illiqpersist_63d_base_v057_signal,
    f16lq_f16_liquidity_profile_illiqdownstreak_base_v058_signal,
    f16lq_f16_liquidity_profile_illiqret_63d_base_v059_signal,
    f16lq_f16_liquidity_profile_illiqvol_63d_base_v060_signal,
    f16lq_f16_liquidity_profile_illiqcrash_63d_base_v061_signal,
    f16lq_f16_liquidity_profile_illiqdrift_126d_base_v062_signal,
    f16lq_f16_liquidity_profile_kyle_63d_base_v063_signal,
    f16lq_f16_liquidity_profile_kylerank_63d_base_v064_signal,
    f16lq_f16_liquidity_profile_kylesigned_63d_base_v065_signal,
    f16lq_f16_liquidity_profile_retac1_63d_base_v066_signal,
    f16lq_f16_liquidity_profile_staleret_63d_base_v067_signal,
    f16lq_f16_liquidity_profile_varratio_126d_base_v068_signal,
    f16lq_f16_liquidity_profile_illiqsignmag_126d_base_v069_signal,
    f16lq_f16_liquidity_profile_costcomposite_63d_base_v070_signal,
    f16lq_f16_liquidity_profile_costtriad_63d_base_v071_signal,
    f16lq_f16_liquidity_profile_impactspreadspr_63d_base_v072_signal,
    f16lq_f16_liquidity_profile_illiqtermdisp_base_v073_signal,
    f16lq_f16_liquidity_profile_spreadpervol_63d_base_v074_signal,
    f16lq_f16_liquidity_profile_illiqscore_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_PROFILE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f16_liquidity_profile_base_001_075_claude: %d features pass" % n_features)
