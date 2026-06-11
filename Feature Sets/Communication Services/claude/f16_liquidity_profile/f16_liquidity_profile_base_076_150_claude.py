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
def _f16_dollar_vol(closeadj, volume):
    return (closeadj * volume).replace(0, np.nan)


def _f16_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))


def _f16_amihud_daily(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    r = _f16_logret(closeadj).abs()
    return (r / dv) * 1e9


def _f16_amihud(closeadj, volume, w):
    d = _f16_amihud_daily(closeadj, volume)
    return d.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_turnover(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_cs_spread(high, low):
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
    dp = closeadj.diff()
    cov = dp.rolling(w, min_periods=max(1, w // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0)) / closeadj.replace(0, np.nan)


def _f16_kyle(closeadj, volume, w):
    r = _f16_logret(closeadj).abs()
    dv = _f16_dollar_vol(closeadj, volume)
    lam = (r / np.sqrt(dv)) * 1e4
    return lam.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_amivest(closeadj, volume, w):
    # Amivest liquidity ratio: dollar-volume per unit |ret| (inverse impact RATIO)
    dv = _f16_dollar_vol(closeadj, volume)
    r = _f16_logret(closeadj).abs()
    liq = dv / (r * 1e9 + 1.0)
    return liq.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_streak(flag):
    grp = (flag != flag.shift(1)).cumsum()
    run = flag.groupby(grp).cumcount() + 1
    return (run * flag).astype(float)


# ============================================================
# === Amihud illiquidity ratio — higher-frequency / long-memory facets ===
# illiquidity 5-year deep level (very long memory) log
def f16lq_f16_liquidity_profile_illiqdeep_504d_base_v076_signal(closeadj, volume):
    b = np.log1p(_f16_amihud(closeadj, volume, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity z vs a long 504d baseline (structural cost shift)
def f16lq_f16_liquidity_profile_illiqz_504d_base_v077_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity skewness over a quarter (asymmetric impact distribution)
def f16lq_f16_liquidity_profile_illiqskew_63d_base_v078_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    b = daily.rolling(63, min_periods=31).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity worst-day (max daily impact ratio vs the typical level)
def f16lq_f16_liquidity_profile_illiqworst_63d_base_v079_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    typ = daily.rolling(252, min_periods=126).median().replace(0, np.nan)
    b = np.log1p(_rmax(daily, 63) / typ)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity acceleration (trend now vs trend a quarter ago)
def f16lq_f16_liquidity_profile_illiqaccel_63d_base_v080_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    tr = a - a.shift(63)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity tail-risk: 95th-pct daily impact ratio over a half-year
def f16lq_f16_liquidity_profile_illiqtail_126d_base_v081_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    q95 = daily.rolling(126, min_periods=63).quantile(0.95)
    med = daily.rolling(126, min_periods=63).median().replace(0, np.nan)
    b = np.log1p(q95 / med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-day fraction: prevalence of impact ratio above 2x the median
def f16lq_f16_liquidity_profile_illiqdayfrac_126d_base_v082_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    med = daily.rolling(252, min_periods=126).median().replace(0, np.nan)
    excess = (daily / med - 2.0).clip(lower=0)
    b = excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity clustering: lag-1 autocorrelation of the daily impact ratio
def f16lq_f16_liquidity_profile_illiqcluster_126d_base_v083_signal(closeadj, volume):
    daily = np.log1p(_f16_amihud_daily(closeadj, volume))
    b = daily.rolling(126, min_periods=63).corr(daily.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity regime z-score change (de-trended structural cost shift)
def f16lq_f16_liquidity_profile_illiqregimez_126d_base_v084_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 126))
    z = _z(a, 504)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Amivest (inverse-impact) liquidity-ratio facets ===
# Amivest liquidity ratio level (dollar traded per unit move)
def f16lq_f16_liquidity_profile_amivest_63d_base_v085_signal(closeadj, volume):
    b = np.log1p(_f16_amivest(closeadj, volume, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest trend (liquidity-ratio improvement/erosion)
def f16lq_f16_liquidity_profile_amivesttrend_126d_base_v086_signal(closeadj, volume):
    liq = np.log1p(_f16_amivest(closeadj, volume, 21))
    b = liq - liq.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest percentile rank
def f16lq_f16_liquidity_profile_amivestrank_252d_base_v087_signal(closeadj, volume):
    b = _rank(_f16_amivest(closeadj, volume, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-vs-Amivest disagreement: impact rank minus depth rank
def f16lq_f16_liquidity_profile_impactdepthspr_63d_base_v088_signal(closeadj, volume):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    d = _rank(_f16_amivest(closeadj, volume, 63), 252)
    b = a + d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest short/long ratio (liquidity-depth term structure)
def f16lq_f16_liquidity_profile_amivestratio_21v126_base_v089_signal(closeadj, volume):
    s = _f16_amivest(closeadj, volume, 21)
    l = _f16_amivest(closeadj, volume, 126)
    b = np.log1p(s) - np.log1p(l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Kyle price-impact RATIO facets ===
# Kyle-lambda long level (252d structural impact)
def f16lq_f16_liquidity_profile_kyle_252d_base_v090_signal(closeadj, volume):
    b = np.log1p(_f16_kyle(closeadj, volume, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle-lambda trend (impact worsening/improving)
def f16lq_f16_liquidity_profile_kyletrend_126d_base_v091_signal(closeadj, volume):
    lam = np.log1p(_f16_kyle(closeadj, volume, 63))
    b = lam - lam.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle z-score (de-trended price-impact ratio)
def f16lq_f16_liquidity_profile_kylez_252d_base_v092_signal(closeadj, volume):
    lam = np.log1p(_f16_kyle(closeadj, volume, 63))
    b = _z(lam, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-adjusted impact: Amihud x relative-turnover, ranked (fragile-depth)
def f16lq_f16_liquidity_profile_impactperturn_63d_base_v093_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    turn = _f16_turnover(volume, 252)
    prod = a * turn.rolling(63, min_periods=31).mean()
    b = _rank(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity elasticity: do absolute moves consume liquidity (impact elasticity)
def f16lq_f16_liquidity_profile_liqelastic_126d_base_v094_signal(closeadj, volume):
    absr = _f16_logret(closeadj).abs()
    turn = np.log1p(_f16_turnover(volume, 21))
    b = turn.rolling(126, min_periods=63).corr(absr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Corwin-Schultz SPREAD estimator — long / higher-moment facets ===
# CS spread 252d long level
def f16lq_f16_liquidity_profile_csspread_252d_base_v095_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread z vs long 504d baseline (structural cost shift)
def f16lq_f16_liquidity_profile_csspreadz_504d_base_v096_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread skew (asymmetric transaction-cost spikes)
def f16lq_f16_liquidity_profile_csspreadskew_126d_base_v097_signal(high, low):
    s = _f16_cs_spread(high, low)
    b = s.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread spike prevalence (cost blow-up days), depth weighted
def f16lq_f16_liquidity_profile_csspreadspike_63d_base_v098_signal(high, low):
    s = _f16_cs_spread(high, low)
    med = s.rolling(252, min_periods=126).median().replace(0, np.nan)
    excess = (s / med - 1.5).clip(lower=0)
    b = excess.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread percentile vs long history
def f16lq_f16_liquidity_profile_csspreadpct_504d_base_v099_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread floor proximity: where current spread sits in its annual cost range
def f16lq_f16_liquidity_profile_csspreadfloor_252d_base_v100_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    floor = _rmin(s, 252)
    ceil = _rmax(s, 252)
    b = (s - floor) / (ceil - floor).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread mean-reversion: spread vs its own slow EMA
def f16lq_f16_liquidity_profile_csspreadmr_63d_base_v101_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(5, min_periods=3).mean()
    b = s - s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread vol-of-vol: instability of the spread estimator over a year
def f16lq_f16_liquidity_profile_csspreadvov_252d_base_v102_signal(high, low):
    s = np.log1p(_f16_cs_spread(high, low).rolling(5, min_periods=3).mean())
    b = s.diff().rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Roll effective-spread facets ===
# Roll spread 252d long level
def f16lq_f16_liquidity_profile_rollspread_252d_base_v103_signal(closeadj):
    b = _f16_roll_spread(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread rank vs 504d
def f16lq_f16_liquidity_profile_rollspreadrank_504d_base_v104_signal(closeadj):
    sp = _f16_roll_spread(closeadj, 63)
    b = _rank(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread trend (effective-cost drift)
def f16lq_f16_liquidity_profile_rollspreadtrend_126d_base_v105_signal(closeadj):
    sp = _f16_roll_spread(closeadj, 63)
    b = sp - sp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread short/long ratio (effective-cost term structure)
def f16lq_f16_liquidity_profile_rollspreadratio_63v252_base_v106_signal(closeadj):
    s = _f16_roll_spread(closeadj, 63)
    l = _f16_roll_spread(closeadj, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Microstructure / bid-ask-bounce ratio facets ===
# variance-ratio deviation (1d vs 5d) at a longer window — illiquidity drag
def f16lq_f16_liquidity_profile_varratio_252d_base_v107_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(252, min_periods=126).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(252, min_periods=126).var()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag-1 over a longer window (bounce persistence)
def f16lq_f16_liquidity_profile_retac1_126d_base_v108_signal(closeadj):
    r = _f16_logret(closeadj)
    b = -r.rolling(126, min_periods=63).corr(r.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stale-price day prevalence over a half-year (no-information illiquidity)
def f16lq_f16_liquidity_profile_staleret_126d_base_v109_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    quiet = (1.0 - r / typ).clip(lower=0)
    b = quiet.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zero-move streak: longest run of near-stale days, blended with stale-day depth
def f16lq_f16_liquidity_profile_stalestreak_63d_base_v110_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    flag = (r < 0.3 * typ).astype(float)
    st = _f16_streak(flag)
    quiet = (1.0 - r / typ).clip(lower=0)
    b = _rmax(st, 63) + 5.0 * quiet.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Thin / dry-up facets (counts, depth, recovery) ===
# liquidity drought duration: longest below-median relative-volume run
def f16lq_f16_liquidity_profile_droughtdur_126d_base_v111_signal(volume):
    t = _f16_turnover(volume, 5)
    flag = (t < 1.0).astype(float)
    st = _f16_streak(flag)
    depth = (1.0 - t).clip(lower=0)
    b = _rmax(st, 126) + 10.0 * depth.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-tail volume floor: 5th-pct relative volume vs its median (depth-of-book floor)
def f16lq_f16_liquidity_profile_volfloor_252d_base_v112_signal(volume):
    t = _f16_turnover(volume, 21)
    p05 = t.rolling(252, min_periods=126).quantile(0.05)
    med = t.rolling(252, min_periods=126).median()
    b = p05 / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover compression: recent relative-volume dispersion vs its long dispersion
def f16lq_f16_liquidity_profile_turncompress_63d_base_v113_signal(volume):
    t = _f16_turnover(volume, 252)
    near = _std(t, 21) / _mean(t, 21).replace(0, np.nan)
    far = _std(t, 252) / _mean(t, 252).replace(0, np.nan)
    b = near / far.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quiet-then-impact fragility: thin prior day followed by a price move
def f16lq_f16_liquidity_profile_quietspike_63d_base_v114_signal(closeadj, volume):
    t = _f16_turnover(volume, 252)
    quiet = (1.0 - t.shift(1)).clip(lower=0)
    move = _f16_logret(closeadj).abs()
    b = (quiet * move).rolling(63, min_periods=31).mean() * 1e2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-shock prevalence: fraction of half-year with relative volume > 1.5x (count-friendly)
def f16lq_f16_liquidity_profile_turnshock_126d_base_v115_signal(volume):
    t = _f16_turnover(volume, 252)
    shock = (t > 1.5).astype(float)
    excess = (t - 1.5).clip(lower=0)
    b = shock.rolling(126, min_periods=63).mean() + 0.05 * excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Composite / interaction RATIO facets ===
# CS spread x turnover divergence: wide spread despite active trading (fragile depth)
def f16lq_f16_liquidity_profile_spreadturndiv_63d_base_v116_signal(high, low, volume):
    sp = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    tr = _rank(_f16_turnover(volume, 21).rolling(21, min_periods=10).mean(), 252)
    b = sp + tr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-turnover elasticity: do wider spreads coincide with heavier trading (cost stickiness)
def f16lq_f16_liquidity_profile_paidcost_63d_base_v117_signal(high, low, volume):
    sp = np.log1p(_f16_cs_spread(high, low).rolling(5, min_periods=3).mean())
    turn = np.log1p(_f16_turnover(volume, 21))
    b = sp.rolling(63, min_periods=31).corr(turn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-to-volatility ratio: cost per unit risk (illiquidity premium)
def f16lq_f16_liquidity_profile_spreadpervol_63d_base_v118_signal(high, low, closeadj):
    sp = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    b = sp / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll-spread-to-volatility ratio: effective cost per unit risk
def f16lq_f16_liquidity_profile_rollpervol_63d_base_v119_signal(closeadj):
    sp = _f16_roll_spread(closeadj, 63)
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    b = _z(sp / vol.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-trend agreement: spread trend signed by impact trend (regime confirmation)
def f16lq_f16_liquidity_profile_costagree_126d_base_v120_signal(closeadj, volume, high, low):
    atr = np.log1p(_f16_amihud(closeadj, volume, 21))
    atr = atr - atr.shift(126)
    sptr = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    sptr = sptr - sptr.shift(126)
    b = np.sign(atr) * sptr * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-vs-spread term-structure dispersion across estimators
def f16lq_f16_liquidity_profile_estdisp_base_v121_signal(closeadj, volume, high, low):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    c = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    r = _rank(_f16_roll_spread(closeadj, 63), 252)
    b = pd.concat([a, c, r], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread skew-of-impact: CS spread rank x Amihud tail skew (cost asymmetry blend)
def f16lq_f16_liquidity_profile_costtailblend_63d_base_v122_signal(closeadj, volume, high, low):
    daily = _f16_amihud_daily(closeadj, volume)
    skew = daily.rolling(63, min_periods=31).skew()
    sp = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    b = np.sign(sp) * skew.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact-per-spread: Amihud rank minus Roll-spread rank (which cost dominates)
def f16lq_f16_liquidity_profile_impactperspread_63d_base_v123_signal(closeadj, volume):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    r = _rank(_f16_roll_spread(closeadj, 63), 252)
    b = a - r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-trading momentum consistency: fraction of months with rising Amihud
def f16lq_f16_liquidity_profile_illiqmomconsist_252d_base_v124_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    up = (a > a.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# === Additional distinct illiquidity-ratio facets ===
# Amihud convexity at a longer window: signed-sqrt of de-meaned impact ratio
def f16lq_f16_liquidity_profile_illiqsignmag_252d_base_v125_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 126))
    typ = a.rolling(252, min_periods=126).mean()
    d = a - typ
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity shock-and-fade: max recent impact ratio vs current (decay)
def f16lq_f16_liquidity_profile_illiqshockfade_63d_base_v126_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 5))
    spike = _rmax(a, 63)
    b = spike - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact-to-spread coherence: rolling corr of Amihud and CS spread (cost co-movement)
def f16lq_f16_liquidity_profile_costcoherence_126d_base_v127_signal(closeadj, volume, high, low):
    a = np.log1p(_f16_amihud(closeadj, volume, 21))
    s = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    b = a.rolling(126, min_periods=63).corr(s)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact half-life proxy: EWMA-decay displacement of the impact ratio
def f16lq_f16_liquidity_profile_illiqdecay_63d_base_v128_signal(closeadj, volume):
    daily = np.log1p(_f16_amihud_daily(closeadj, volume))
    fast = daily.ewm(span=10, min_periods=5).mean()
    slow = daily.ewm(span=63, min_periods=31).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity range-position: where current Amihud sits in its annual cost range
def f16lq_f16_liquidity_profile_illiqrangepos_252d_base_v129_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 21))
    hi = _rmax(a, 252)
    lo = _rmin(a, 252)
    b = (a - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-vs-Kyle disagreement: linear vs sqrt-impact rank gap
def f16lq_f16_liquidity_profile_amihudkylespr_63d_base_v130_signal(closeadj, volume):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    k = _rank(_f16_kyle(closeadj, volume, 63), 252)
    b = a - k
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-cheapening streak: consecutive days CS spread below its MA, depth weighted
def f16lq_f16_liquidity_profile_spreadcheapstreak_base_v131_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(5, min_periods=3).mean()
    ma = s.rolling(63, min_periods=31).mean()
    flag = (s < ma).astype(float)
    st = _f16_streak(flag)
    gap = (1.0 - s / ma.replace(0, np.nan)).clip(lower=0)
    b = st + gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity premium percentile: Amihud-per-vol ranked over 504d
def f16lq_f16_liquidity_profile_illiqpremrank_504d_base_v132_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    b = _rank(a / vol.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll-spread spike prevalence: effective-cost blow-up days
def f16lq_f16_liquidity_profile_rollspike_63d_base_v133_signal(closeadj):
    sp = _f16_roll_spread(closeadj, 21)
    med = sp.rolling(252, min_periods=126).median().replace(0, np.nan)
    excess = (sp / med - 1.5).clip(lower=0)
    b = excess.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-impact coherence: corr of relative-volume and impact ratio (depth response)
def f16lq_f16_liquidity_profile_turnimpactcorr_126d_base_v134_signal(closeadj, volume):
    turn = np.log1p(_f16_turnover(volume, 21))
    a = np.log1p(_f16_amihud(closeadj, volume, 21))
    b = -turn.rolling(126, min_periods=63).corr(a)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread per impact: quoted-spread rank vs realized-impact rank (which cost bites)
def f16lq_f16_liquidity_profile_spreadperimpact_63d_base_v135_signal(closeadj, volume, high, low):
    sp = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    b = (sp + 0.5) / (a + 0.5 + 1e-3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity worsening velocity (impact ratio delta over a month)
def f16lq_f16_liquidity_profile_illiqvelocity_63d_base_v136_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    b = a - a.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest drawdown: liquidity-ratio depth from its trailing peak
def f16lq_f16_liquidity_profile_amivestdd_252d_base_v137_signal(closeadj, volume):
    liq = _f16_amivest(closeadj, volume, 21)
    peak = _rmax(liq, 252)
    b = np.log(liq.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity persistence over a year: fraction above 504d median (chronic cost)
def f16lq_f16_liquidity_profile_illiqchronic_252d_base_v138_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(504, min_periods=252).median()
    above = (a > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CS spread-to-Roll-spread term-structure: short CS vs long Roll (cost curve tilt)
def f16lq_f16_liquidity_profile_spreadtilt_base_v139_signal(closeadj, high, low):
    cs = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    roll = _rank(_f16_roll_spread(closeadj, 252), 252)
    b = cs - roll
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact dispersion across estimators z-change (cost-disagreement drift)
def f16lq_f16_liquidity_profile_estdispchg_126d_base_v140_signal(closeadj, volume, high, low):
    a = _rank(_f16_amihud(closeadj, volume, 63), 252)
    c = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    disp = (a - c).abs()
    b = disp - disp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-ratio kurtosis: fat-tailed relative-volume bursts (spiky liquidity)
def f16lq_f16_liquidity_profile_turnkurt_126d_base_v141_signal(volume):
    t = _f16_turnover(volume, 252)
    b = t.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact-skew sign x spread: directionality of cost (asymmetric trading friction)
def f16lq_f16_liquidity_profile_costdirection_126d_base_v142_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    r = _f16_logret(closeadj)
    dn = daily.where(r < 0).rolling(126, min_periods=40).mean()
    up = daily.where(r > 0).rolling(126, min_periods=40).mean()
    b = (dn - up) / (dn + up).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-floor breakout: current CS spread vs its annual minimum (cost re-rating)
def f16lq_f16_liquidity_profile_spreadbreakout_252d_base_v143_signal(high, low):
    s = _f16_cs_spread(high, low).rolling(5, min_periods=3).mean()
    floor = s.shift(1).rolling(252, min_periods=126).min()
    b = s / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-cost half-year acceleration of the Amivest depth ratio
def f16lq_f16_liquidity_profile_premaccel_126d_base_v144_signal(closeadj, volume):
    liq = np.log1p(_f16_amivest(closeadj, volume, 63))
    tr = liq - liq.shift(63)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll-spread z-change: de-trended effective-cost structural shift
def f16lq_f16_liquidity_profile_rollz_change_126d_base_v145_signal(closeadj):
    z = _z(_f16_roll_spread(closeadj, 63), 252)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# impact-spike clustering: consecutive-high-impact prevalence blended with excess depth
def f16lq_f16_liquidity_profile_spikecluster_63d_base_v146_signal(closeadj, volume):
    daily = _f16_amihud_daily(closeadj, volume)
    med = daily.rolling(252, min_periods=126).median().replace(0, np.nan)
    hi = (daily > 2.0 * med).astype(float)
    both = (hi * hi.shift(1))
    excess = (daily / med - 2.0).clip(lower=0)
    b = both.rolling(63, min_periods=31).mean() + 0.1 * excess.rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest vol-of-vol: instability of the depth ratio (fragile liquidity supply)
def f16lq_f16_liquidity_profile_amivestvov_126d_base_v147_signal(closeadj, volume):
    liq = np.log1p(_f16_amivest(closeadj, volume, 5))
    b = liq.diff().rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-cost interaction: thin turnover that coincides with wide spread (trap)
def f16lq_f16_liquidity_profile_thintrap_63d_base_v148_signal(high, low, volume):
    thin = (1.0 - _f16_turnover(volume, 252)).clip(lower=0)
    sp = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252) + 0.5
    b = (thin * sp).rolling(63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-cost regime distance: Amihud rank minus its own one-year-ago rank
def f16lq_f16_liquidity_profile_illiqrankchg_252d_base_v149_signal(closeadj, volume):
    rk = _rank(_f16_amihud(closeadj, volume, 63), 252)
    b = rk - rk.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# master cost-of-trading index: weighted blend of impact, quoted, effective spreads
def f16lq_f16_liquidity_profile_costindex_base_v150_signal(closeadj, volume, high, low):
    az = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    cz = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rz = _z(_f16_roll_spread(closeadj, 63), 252)
    kz = _z(np.log1p(_f16_kyle(closeadj, volume, 63)), 252)
    b = 0.35 * az + 0.25 * cz + 0.2 * rz + 0.2 * kz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16lq_f16_liquidity_profile_illiqdeep_504d_base_v076_signal,
    f16lq_f16_liquidity_profile_illiqz_504d_base_v077_signal,
    f16lq_f16_liquidity_profile_illiqskew_63d_base_v078_signal,
    f16lq_f16_liquidity_profile_illiqworst_63d_base_v079_signal,
    f16lq_f16_liquidity_profile_illiqaccel_63d_base_v080_signal,
    f16lq_f16_liquidity_profile_illiqtail_126d_base_v081_signal,
    f16lq_f16_liquidity_profile_illiqdayfrac_126d_base_v082_signal,
    f16lq_f16_liquidity_profile_illiqcluster_126d_base_v083_signal,
    f16lq_f16_liquidity_profile_illiqregimez_126d_base_v084_signal,
    f16lq_f16_liquidity_profile_amivest_63d_base_v085_signal,
    f16lq_f16_liquidity_profile_amivesttrend_126d_base_v086_signal,
    f16lq_f16_liquidity_profile_amivestrank_252d_base_v087_signal,
    f16lq_f16_liquidity_profile_impactdepthspr_63d_base_v088_signal,
    f16lq_f16_liquidity_profile_amivestratio_21v126_base_v089_signal,
    f16lq_f16_liquidity_profile_kyle_252d_base_v090_signal,
    f16lq_f16_liquidity_profile_kyletrend_126d_base_v091_signal,
    f16lq_f16_liquidity_profile_kylez_252d_base_v092_signal,
    f16lq_f16_liquidity_profile_impactperturn_63d_base_v093_signal,
    f16lq_f16_liquidity_profile_liqelastic_126d_base_v094_signal,
    f16lq_f16_liquidity_profile_csspread_252d_base_v095_signal,
    f16lq_f16_liquidity_profile_csspreadz_504d_base_v096_signal,
    f16lq_f16_liquidity_profile_csspreadskew_126d_base_v097_signal,
    f16lq_f16_liquidity_profile_csspreadspike_63d_base_v098_signal,
    f16lq_f16_liquidity_profile_csspreadpct_504d_base_v099_signal,
    f16lq_f16_liquidity_profile_csspreadfloor_252d_base_v100_signal,
    f16lq_f16_liquidity_profile_csspreadmr_63d_base_v101_signal,
    f16lq_f16_liquidity_profile_csspreadvov_252d_base_v102_signal,
    f16lq_f16_liquidity_profile_rollspread_252d_base_v103_signal,
    f16lq_f16_liquidity_profile_rollspreadrank_504d_base_v104_signal,
    f16lq_f16_liquidity_profile_rollspreadtrend_126d_base_v105_signal,
    f16lq_f16_liquidity_profile_rollspreadratio_63v252_base_v106_signal,
    f16lq_f16_liquidity_profile_varratio_252d_base_v107_signal,
    f16lq_f16_liquidity_profile_retac1_126d_base_v108_signal,
    f16lq_f16_liquidity_profile_staleret_126d_base_v109_signal,
    f16lq_f16_liquidity_profile_stalestreak_63d_base_v110_signal,
    f16lq_f16_liquidity_profile_droughtdur_126d_base_v111_signal,
    f16lq_f16_liquidity_profile_volfloor_252d_base_v112_signal,
    f16lq_f16_liquidity_profile_turncompress_63d_base_v113_signal,
    f16lq_f16_liquidity_profile_quietspike_63d_base_v114_signal,
    f16lq_f16_liquidity_profile_turnshock_126d_base_v115_signal,
    f16lq_f16_liquidity_profile_spreadturndiv_63d_base_v116_signal,
    f16lq_f16_liquidity_profile_paidcost_63d_base_v117_signal,
    f16lq_f16_liquidity_profile_spreadpervol_63d_base_v118_signal,
    f16lq_f16_liquidity_profile_rollpervol_63d_base_v119_signal,
    f16lq_f16_liquidity_profile_costagree_126d_base_v120_signal,
    f16lq_f16_liquidity_profile_estdisp_base_v121_signal,
    f16lq_f16_liquidity_profile_costtailblend_63d_base_v122_signal,
    f16lq_f16_liquidity_profile_impactperspread_63d_base_v123_signal,
    f16lq_f16_liquidity_profile_illiqmomconsist_252d_base_v124_signal,
    f16lq_f16_liquidity_profile_illiqsignmag_252d_base_v125_signal,
    f16lq_f16_liquidity_profile_illiqshockfade_63d_base_v126_signal,
    f16lq_f16_liquidity_profile_costcoherence_126d_base_v127_signal,
    f16lq_f16_liquidity_profile_illiqdecay_63d_base_v128_signal,
    f16lq_f16_liquidity_profile_illiqrangepos_252d_base_v129_signal,
    f16lq_f16_liquidity_profile_amihudkylespr_63d_base_v130_signal,
    f16lq_f16_liquidity_profile_spreadcheapstreak_base_v131_signal,
    f16lq_f16_liquidity_profile_illiqpremrank_504d_base_v132_signal,
    f16lq_f16_liquidity_profile_rollspike_63d_base_v133_signal,
    f16lq_f16_liquidity_profile_turnimpactcorr_126d_base_v134_signal,
    f16lq_f16_liquidity_profile_spreadperimpact_63d_base_v135_signal,
    f16lq_f16_liquidity_profile_illiqvelocity_63d_base_v136_signal,
    f16lq_f16_liquidity_profile_amivestdd_252d_base_v137_signal,
    f16lq_f16_liquidity_profile_illiqchronic_252d_base_v138_signal,
    f16lq_f16_liquidity_profile_spreadtilt_base_v139_signal,
    f16lq_f16_liquidity_profile_estdispchg_126d_base_v140_signal,
    f16lq_f16_liquidity_profile_turnkurt_126d_base_v141_signal,
    f16lq_f16_liquidity_profile_costdirection_126d_base_v142_signal,
    f16lq_f16_liquidity_profile_spreadbreakout_252d_base_v143_signal,
    f16lq_f16_liquidity_profile_premaccel_126d_base_v144_signal,
    f16lq_f16_liquidity_profile_rollz_change_126d_base_v145_signal,
    f16lq_f16_liquidity_profile_spikecluster_63d_base_v146_signal,
    f16lq_f16_liquidity_profile_amivestvov_126d_base_v147_signal,
    f16lq_f16_liquidity_profile_thintrap_63d_base_v148_signal,
    f16lq_f16_liquidity_profile_illiqrankchg_252d_base_v149_signal,
    f16lq_f16_liquidity_profile_costindex_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_PROFILE_REGISTRY_076_150 = REGISTRY


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

    print("OK f16_liquidity_profile_base_076_150_claude: %d features pass" % n_features)
