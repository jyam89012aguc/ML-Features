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


# ===== folder domain primitives (liquidity / illiquidity) =====
def _f16_dollar_vol(closeadj, volume):
    # dollar-volume = closeadj * volume (price * shares), the liquidity scale
    return (closeadj * volume).replace(0, np.nan)


def _f16_amihud(closeadj, volume, w):
    # Amihud illiquidity = mean of |daily return| / dollar-volume over window
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    illiq = ret / dv
    return illiq.rolling(w, min_periods=max(2, w // 2)).mean()


def _f16_amihud_raw(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    return ret / dv


def _f16_turnover(volume, w):
    # turnover proxy = today's volume vs typical volume (junior float churn)
    typ = volume.rolling(w, min_periods=max(2, w // 2)).median()
    return volume / typ.replace(0, np.nan)


def _f16_corwin_schultz(high, low, w):
    # Corwin-Schultz high-low bid-ask spread estimator (rolling mean of daily proxy)
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    beta = hl + hl.shift(1)
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (np.log(h2.replace(0, np.nan) / l2.replace(0, np.nan))) ** 2
    den = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / den - np.sqrt(gamma / den)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    spread = spread.clip(lower=0)
    return spread.rolling(w, min_periods=max(2, w // 2)).mean()


def _f16_zero_vol_frac(volume, w, thresh_q=0.10):
    # fraction of recent days with thin/near-zero volume (dry-up)
    floor = volume.rolling(w, min_periods=max(2, w // 2)).quantile(thresh_q)
    thin = (volume <= floor).astype(float)
    return thin.rolling(w, min_periods=max(2, w // 2)).mean()


def _f16_dryup_streak(volume, w):
    # current run-length of below-median-volume days (consecutive dry-up)
    med = volume.rolling(w, min_periods=max(2, w // 2)).median()
    below = (volume < med).astype(float)

    def _streak(a):
        c = 0
        for x in a[::-1]:
            if x > 0.5:
                c += 1
            else:
                break
        return c
    return below.rolling(w, min_periods=max(2, w // 2)).apply(_streak, raw=True)


# ============================================================
# Amihud illiquidity, 21d level (junior illiquidity, log-scaled)
def f16lq_f16_liquidity_illiquidity_profile_amihud_21d_base_v001_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    b = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity, 63d level
def f16lq_f16_liquidity_illiquidity_profile_amihud_63d_base_v002_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    b = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud 126d level de-trended by its 504d mean (medium-horizon illiquidity anomaly)
def f16lq_f16_liquidity_illiquidity_profile_amihud_126d_base_v003_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 126)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = lg - lg.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity, 252d level
def f16lq_f16_liquidity_illiquidity_profile_amihud_252d_base_v004_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 252)
    b = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud 21d z-scored vs its own 252d history (illiquidity regime extremity)
def f16lq_f16_liquidity_illiquidity_profile_amihudz_21d_base_v005_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = _z(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud 63d percentile-ranked vs its own 252d history
def f16lq_f16_liquidity_illiquidity_profile_amihudrank_63d_base_v006_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    b = _rank(illiq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud term structure: short illiquidity vs long illiquidity (ratio)
def f16lq_f16_liquidity_illiquidity_profile_amihudterm_21v126_base_v007_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 21)
    l = _f16_amihud(closeadj, volume, 126)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud term structure: 63d vs 252d (illiquidity slope across horizons)
def f16lq_f16_liquidity_illiquidity_profile_amihudterm_63v252_base_v008_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 63)
    l = _f16_amihud(closeadj, volume, 252)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud trend: change in 63d log-illiquidity over a quarter (drying up vs deepening)
def f16lq_f16_liquidity_illiquidity_profile_amihudtrend_63d_base_v009_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = lg - lg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud dispersion: rolling std of daily raw illiquidity (illiquidity instability)
def f16lq_f16_liquidity_illiquidity_profile_amihuddisp_63d_base_v010_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    lg = np.log(raw.replace(0, np.nan) * 1e12 + 1.0)
    b = _std(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- turnover family ----
# turnover today vs 63d median volume (float churn intensity)
def f16lq_f16_liquidity_illiquidity_profile_turnover_63d_base_v011_signal(volume):
    b = _f16_turnover(volume, 63)
    result = np.log(b.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean turnover ratio vs 126d (turnover regime)
def f16lq_f16_liquidity_illiquidity_profile_turnover_21d_base_v012_signal(volume):
    t = _f16_turnover(volume, 126)
    b = _mean(t, 21)
    result = np.log(b.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover distribution skew over 126d (right-skew = sporadic liquidity bursts)
def f16lq_f16_liquidity_illiquidity_profile_turnoverz_63d_base_v013_signal(volume):
    lt = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    b = lt.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover percentile rank vs 252d (relative liquidity activity)
def f16lq_f16_liquidity_illiquidity_profile_turnoverrank_base_v014_signal(volume):
    t = _f16_turnover(volume, 63)
    b = _rank(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-driven dollar-turnover: dollar-churn minus share-churn (price-level effect)
def f16lq_f16_liquidity_illiquidity_profile_dollarturn_63d_base_v015_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    dmed = dv.rolling(63, min_periods=21).median()
    dollar_churn = np.log((dv / dmed.replace(0, np.nan)).replace(0, np.nan))
    vmed = volume.rolling(63, min_periods=21).median()
    share_churn = np.log((volume / vmed.replace(0, np.nan)).replace(0, np.nan))
    b = dollar_churn - share_churn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover smoothed minus its slow EMA (turnover displacement)
def f16lq_f16_liquidity_illiquidity_profile_turnovdisp_base_v016_signal(volume):
    t = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    b = t.ewm(span=10, min_periods=5).mean() - t.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- zero / thin volume streak & dry-up ----
# thinness intensity: fraction below 126d 25th-pct floor blended with depth (dry-up)
def f16lq_f16_liquidity_illiquidity_profile_thinfrac_63d_base_v017_signal(volume):
    floor = volume.rolling(126, min_periods=63).quantile(0.25)
    frac = (volume <= floor).astype(float).rolling(63, min_periods=21).mean()
    depth = (1.0 - volume / floor.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thinness intensity over 126d: fraction below 252d quintile blended with depth
def f16lq_f16_liquidity_illiquidity_profile_thinfrac_126d_base_v018_signal(volume):
    floor = volume.rolling(252, min_periods=126).quantile(0.20)
    frac = (volume <= floor).astype(float).rolling(126, min_periods=63).mean()
    depth = (1.0 - volume / floor.replace(0, np.nan)).clip(lower=0).rolling(126, min_periods=63).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current dry-up streak length blended with its recent average (smooth streak signal)
def f16lq_f16_liquidity_illiquidity_profile_dryupstreak_63d_base_v019_signal(volume):
    streak = _f16_dryup_streak(volume, 63)
    b = streak + streak.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dry-up episode frequency over 252d blended with mean below-floor depth (count-friendly)
def f16lq_f16_liquidity_illiquidity_profile_dryupcount_252d_base_v020_signal(volume):
    med = volume.rolling(63, min_periods=21).median()
    below = (volume < 0.5 * med).astype(float)
    entries = ((below == 1) & (below.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = (1.0 - volume / (0.5 * med).replace(0, np.nan)).clip(lower=0).rolling(252, min_periods=126).mean()
    b = cnt + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-volume depth: mean shortfall below 63d median when thin (how dry)
def f16lq_f16_liquidity_illiquidity_profile_thindepth_63d_base_v021_signal(volume):
    med = volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    shortfall = (1.0 - volume / med).clip(lower=0)
    b = shortfall.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest dry-up streak within trailing 126d (max consecutive thin run)
def f16lq_f16_liquidity_illiquidity_profile_maxdry_126d_base_v022_signal(volume):
    med = volume.rolling(63, min_periods=21).median()
    below = (volume < med).astype(float)

    def _maxrun(a):
        best = 0
        cur = 0
        for x in a:
            if x > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
    longest = below.rolling(126, min_periods=63).apply(_maxrun, raw=True)
    frac = below.rolling(126, min_periods=63).mean()
    b = longest + 10.0 * frac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume dry-up: fraction below 252d 25th-pct blended with shortfall depth
def f16lq_f16_liquidity_illiquidity_profile_dollardry_63d_base_v023_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    floor = dv.rolling(252, min_periods=126).quantile(0.25)
    thin = (dv <= floor).astype(float).rolling(63, min_periods=21).mean()
    depth = (1.0 - dv / floor.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = thin + 0.75 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Corwin-Schultz bid-ask spread proxy ----
# 21d Corwin-Schultz spread level
def f16lq_f16_liquidity_illiquidity_profile_csspread_21d_base_v024_signal(high, low):
    b = _f16_corwin_schultz(high, low, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Corwin-Schultz spread level
def f16lq_f16_liquidity_illiquidity_profile_csspread_63d_base_v025_signal(high, low):
    b = _f16_corwin_schultz(high, low, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Corwin-Schultz spread level
def f16lq_f16_liquidity_illiquidity_profile_csspread_126d_base_v026_signal(high, low):
    b = _f16_corwin_schultz(high, low, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread acceleration: change in 21d spread over a month (blow-out speed)
def f16lq_f16_liquidity_illiquidity_profile_csspreadz_21d_base_v027_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 21)
    chg = cs - cs.shift(21)
    b = chg - chg.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz term structure: 21d vs 126d spread (widening/tightening)
def f16lq_f16_liquidity_illiquidity_profile_csterm_21v126_base_v028_signal(high, low):
    s = _f16_corwin_schultz(high, low, 21)
    l = _f16_corwin_schultz(high, low, 126)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread trend: change in 63d spread over a quarter
def f16lq_f16_liquidity_illiquidity_profile_csspreadtrend_63d_base_v029_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 63)
    b = cs - cs.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread percentile rank vs 252d (relative spread regime)
def f16lq_f16_liquidity_illiquidity_profile_csspreadrank_63d_base_v030_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 63)
    b = _rank(cs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity (inverse-illiquidity) and trend ----
# Amihud-implied liquidity trend: negative change of 63d log-illiquidity (improving)
def f16lq_f16_liquidity_illiquidity_profile_liqtrend_63d_base_v031_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = -(lg - lg.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend long: change in 126d log-illiquidity over half year (sign flipped)
def f16lq_f16_liquidity_illiquidity_profile_liqtrend_126d_base_v032_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 126)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = -(lg - lg.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud short/long ratio change (illiquidity term-structure momentum)
def f16lq_f16_liquidity_illiquidity_profile_amihudtermmom_base_v033_signal(closeadj, volume):
    s = _f16_amihud(closeadj, volume, 21)
    l = _f16_amihud(closeadj, volume, 126)
    ratio = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend: 21d vs 126d mean dollar-volume (liquidity expansion)
def f16lq_f16_liquidity_illiquidity_profile_dvexpand_base_v034_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    s = _mean(dv, 21)
    l = _mean(dv, 126)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud relative to its own min over 252d (distance above best-liquidity floor)
def f16lq_f16_liquidity_illiquidity_profile_amihudfloor_base_v035_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lo = illiq.rolling(252, min_periods=126).min()
    b = np.log(illiq.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- impact / variance-ratio style depth proxies ----
# Amivest depth z-scored vs its own 252d history (de-trended liquidity-depth regime)
def f16lq_f16_liquidity_illiquidity_profile_amivest_63d_base_v036_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    num = dv.rolling(63, min_periods=21).sum()
    den = ret.rolling(63, min_periods=21).sum().replace(0, np.nan)
    depth = np.log((num / den).replace(0, np.nan))
    b = _z(depth, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amivest liquidity-depth trend: change in 126d log-depth over a quarter (improving depth)
def f16lq_f16_liquidity_illiquidity_profile_amivest_126d_base_v037_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    num = dv.rolling(126, min_periods=63).sum()
    den = ret.rolling(126, min_periods=63).sum().replace(0, np.nan)
    depth = np.log((num / den).replace(0, np.nan))
    b = depth - depth.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-per-turnover impact: |ret| divided by turnover (price impact of churn)
def f16lq_f16_liquidity_illiquidity_profile_retperturn_63d_base_v038_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    t = _f16_turnover(volume, 63)
    impact = ret / t.replace(0, np.nan)
    b = np.log(impact.rolling(63, min_periods=21).mean().replace(0, np.nan) * 1e4 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-range to close-move ratio (range-illiquidity vs realized impact), 21d
def f16lq_f16_liquidity_illiquidity_profile_rangedv_21d_base_v039_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    ret = closeadj.pct_change().abs()
    # how much intraday range is generated per unit of realized close-to-close move;
    # high = lots of churn/whipsaw with little net move (thin-book illiquidity)
    ratio = rng / (ret + rng).replace(0, np.nan)
    b = ratio.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range per dollar-volume z-scored vs 252d
def f16lq_f16_liquidity_illiquidity_profile_rangedvz_63d_base_v040_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _f16_dollar_vol(closeadj, volume)
    illiq = (rng / dv).rolling(63, min_periods=21).mean()
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = _z(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volume stability / concentration ----
# volume coefficient of variation 63d (liquidity instability)
def f16lq_f16_liquidity_illiquidity_profile_volcv_63d_base_v041_signal(volume):
    m = _mean(volume, 63)
    sd = _std(volume, 63)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume Herfindahl concentration over 21d (lumpy thin trading)
def f16lq_f16_liquidity_illiquidity_profile_volherf_21d_base_v042_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    share = volume / s.replace(0, np.nan)
    b = (share ** 2).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume Herfindahl over 63d (liquidity lumpiness)
def f16lq_f16_liquidity_illiquidity_profile_dvherf_63d_base_v043_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    s = dv.rolling(63, min_periods=21).sum()
    share = dv / s.replace(0, np.nan)
    b = (share ** 2).rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-volume dispersion 126d (long-horizon liquidity variability)
def f16lq_f16_liquidity_illiquidity_profile_logvoldisp_126d_base_v044_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = _std(lv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity level proxies ----
# Amihud x dollar-volume mismatch: illiquidity not explained by raw dollar-vol scale
def f16lq_f16_liquidity_illiquidity_profile_logdv_63d_base_v045_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg_illiq = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    dv = np.log(_f16_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    # standardize both then take the residual: illiquidity beyond what dollar-vol implies
    b = _z(lg_illiq, 252) + _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume vs its 252d mean (liquidity tier distance)
def f16lq_f16_liquidity_illiquidity_profile_logdvgap_252d_base_v046_signal(closeadj, volume):
    dv = np.log(_f16_dollar_vol(closeadj, volume))
    b = dv.rolling(21, min_periods=10).mean() - dv.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume drawdown: current 21d dollar-vol vs its 252d peak (liquidity collapse)
def f16lq_f16_liquidity_illiquidity_profile_dvdrawdown_base_v047_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    b = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume percentile rank vs 504d (relative liquidity tier)
def f16lq_f16_liquidity_illiquidity_profile_dvrank_504d_base_v048_signal(closeadj, volume):
    dv = np.log(_f16_dollar_vol(closeadj, volume)).rolling(21, min_periods=10).mean()
    b = _rank(dv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- effective spread / Roll-style proxies ----
# Roll's implied spread: 2*sqrt(-autocov of returns) over 63d (transaction cost)
def f16lq_f16_liquidity_illiquidity_profile_rollspread_63d_base_v049_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    b = 2.0 * np.sqrt((-cov).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll's implied spread 126d
def f16lq_f16_liquidity_illiquidity_profile_rollspread_126d_base_v050_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(126, min_periods=63).cov(ret.shift(1))
    b = 2.0 * np.sqrt((-cov).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread z-scored vs 252d (effective-cost blow-out)
def f16lq_f16_liquidity_illiquidity_profile_rollspreadz_63d_base_v051_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = 2.0 * np.sqrt((-cov).clip(lower=0))
    b = _z(rs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-location-in-range illiquidity: avg distance of close from midrange (pinning)
def f16lq_f16_liquidity_illiquidity_profile_closepin_21d_base_v052_signal(close, high, low):
    mid = (high + low) / 2.0
    pin = (close - mid).abs() / (high - low).replace(0, np.nan)
    b = pin.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- variance-ratio / autocorrelation depth proxies ----
# return autocorrelation 63d (illiquid stocks show stale-price autocorrelation)
def f16lq_f16_liquidity_illiquidity_profile_retac1_63d_base_v053_signal(closeadj):
    ret = closeadj.pct_change()
    b = ret.rolling(63, min_periods=21).corr(ret.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio: 5d var vs 5x 1d var (illiquidity => VR != 1), 126d window
def f16lq_f16_liquidity_illiquidity_profile_varratio_126d_base_v054_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# near-zero-return prevalence 63d: mean of a smooth small-move kernel (stale pricing)
def f16lq_f16_liquidity_illiquidity_profile_zeroret_63d_base_v055_signal(closeadj):
    ret = closeadj.pct_change().abs()
    scale = ret.rolling(252, min_periods=126).median().replace(0, np.nan)
    # smooth indicator: ~1 when |ret| << typical, decaying as it approaches typical
    kernel = np.exp(-(ret / scale) ** 2)
    b = kernel.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-information liquidity 63d: avg volume-share that produces little price move
def f16lq_f16_liquidity_illiquidity_profile_tinyimpact_63d_base_v056_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    rscale = ret.rolling(252, min_periods=126).median().replace(0, np.nan)
    vmed = volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    # high when volume is heavy yet the price barely moved (absorption)
    absorb = (volume / vmed) * np.exp(-(ret / rscale) ** 2)
    b = absorb.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity-risk / commonality-style ----
# illiquidity-of-illiquidity: vol of 21d Amihud over 126d (liquidity-risk)
def f16lq_f16_liquidity_illiquidity_profile_illiqofilliq_base_v057_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = _std(lg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity shock recency: days since last dollar-vol spike (>2.5x 63d median)
def f16lq_f16_liquidity_illiquidity_profile_liqshockrec_base_v058_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    spike = (dv > 2.5 * med).astype(float)

    def _dsl(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = spike.rolling(126, min_periods=63).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of illiquidity spikes (raw Amihud > 3x median) over 252d (count-friendly)
def f16lq_f16_liquidity_illiquidity_profile_illiqspikecnt_base_v059_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    med = raw.rolling(63, min_periods=21).median()
    spike = (raw > 3.0 * med).astype(float)
    b = spike.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetry: illiquidity on down days vs up days (down-side liquidity risk), 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqasym_63d_base_v060_signal(closeadj, volume):
    ret = closeadj.pct_change()
    raw = _f16_amihud_raw(closeadj, volume)
    down = raw.where(ret < 0)
    up = raw.where(ret > 0)
    dn = down.rolling(63, min_periods=10).mean()
    upm = up.rolling(63, min_periods=10).mean()
    b = np.log(dn.replace(0, np.nan) / upm.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more turnover / liquidity structure ----
# turnover dry-up 63d: fraction below 0.5 turnover blended with mean shortfall depth
def f16lq_f16_liquidity_illiquidity_profile_turndry_63d_base_v061_signal(volume):
    t = _f16_turnover(volume, 63)
    dry = (t < 0.5).astype(float).rolling(63, min_periods=21).mean()
    depth = (0.5 - t).clip(lower=0).rolling(63, min_periods=21).mean()
    b = dry + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover acceleration: 21d mean turnover vs 63d mean (activity pickup)
def f16lq_f16_liquidity_illiquidity_profile_turnaccel_base_v062_signal(volume):
    t = np.log(_f16_turnover(volume, 126).replace(0, np.nan))
    b = _mean(t, 21) - _mean(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-weighted return: signed return scaled by inverse illiquidity (clean moves)
def f16lq_f16_liquidity_illiquidity_profile_liqwret_21d_base_v063_signal(closeadj, volume):
    ret = closeadj.pct_change()
    illiq = _f16_amihud(closeadj, volume, 21)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = ret.rolling(21, min_periods=10).sum() / (1.0 + lg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread x illiquidity interaction (compound transaction cost), 63d
def f16lq_f16_liquidity_illiquidity_profile_costcompound_base_v064_signal(closeadj, high, low, volume):
    cs = _f16_corwin_schultz(high, low, 63)
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = cs * lg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity divergence: dollar-volume trend signed by spread-change (false liquidity)
def f16lq_f16_liquidity_illiquidity_profile_liqdiverge_base_v065_signal(closeadj, high, low, volume):
    dv = np.log(_f16_dollar_vol(closeadj, volume))
    dvtr = dv.rolling(21, min_periods=10).mean() - dv.rolling(63, min_periods=21).mean()
    cs = _f16_corwin_schultz(high, low, 21)
    cstr = cs - cs.shift(21)
    b = dvtr * np.sign(cstr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-day vs daily impact ratio (5d Amihud / 1d Amihud): impact horizon scaling, 63d
def f16lq_f16_liquidity_illiquidity_profile_amihud5d_63d_base_v066_signal(closeadj, volume):
    ret5 = (closeadj / closeadj.shift(5) - 1.0).abs()
    dv5 = _f16_dollar_vol(closeadj, volume).rolling(5).sum()
    illiq5 = (ret5 / dv5.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    illiq1 = _f16_amihud(closeadj, volume, 63)
    # >1 means impact compounds over multiple days (persistent illiquidity);
    # <1 means daily impact reverses (transitory thin-book noise)
    b = np.log((illiq5 * 5.0 / illiq1.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope vs price trend (liquidity confirming or fading the move), 63d
def f16lq_f16_liquidity_illiquidity_profile_volprictrend_base_v067_signal(closeadj, volume):
    vtr = np.log(volume.replace(0, np.nan)).rolling(63, min_periods=21).mean() \
        - np.log(volume.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    ptr = np.log(closeadj).rolling(63, min_periods=21).mean() \
        - np.log(closeadj).rolling(126, min_periods=63).mean()
    b = vtr - ptr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-then-spike pressure: dry-up fraction times latest volume vs baseline
def f16lq_f16_liquidity_illiquidity_profile_drypressure_base_v068_signal(volume):
    med = volume.rolling(126, min_periods=63).median()
    dryfrac = (volume < 0.5 * med).astype(float).rolling(63, min_periods=21).mean()
    latest = volume / med.replace(0, np.nan)
    b = dryfrac * np.log(latest.replace(0, np.nan) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread divided by volatility (spread-per-risk, pure friction), 63d
def f16lq_f16_liquidity_illiquidity_profile_spreadpervol_base_v069_signal(closeadj, high, low):
    cs = _f16_corwin_schultz(high, low, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = cs / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation 126d (liquidity reliability)
def f16lq_f16_liquidity_illiquidity_profile_dvcv_126d_base_v070_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    m = _mean(dv, 126)
    sd = _std(dv, 126)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity momentum vs longer baseline: 21d Amihud rank within 504d
def f16lq_f16_liquidity_illiquidity_profile_amihudrank504_base_v071_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    b = _rank(illiq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 252d in the illiquid regime (Amihud above its 252d median) — regime time
def f16lq_f16_liquidity_illiquidity_profile_illiqregtime_base_v072_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    med = illiq.rolling(252, min_periods=126).median()
    hot = (illiq > med).astype(float)
    b = hot.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity tier breach over 252d: entry count blended with time-below-floor depth
def f16lq_f16_liquidity_illiquidity_profile_tierbreach_base_v073_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    floor = dv.rolling(252, min_periods=126).quantile(0.10)
    below = (dv < floor).astype(float)
    entries = ((below == 1) & (below.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = (1.0 - dv / floor.replace(0, np.nan)).clip(lower=0).rolling(252, min_periods=126).mean()
    b = cnt + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-cost composite: average of normalized Amihud, CS-spread, Roll spread ranks
def f16lq_f16_liquidity_illiquidity_profile_costcomposite_base_v074_signal(closeadj, high, low, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    a_r = _rank(illiq, 252)
    cs = _f16_corwin_schultz(high, low, 63)
    cs_r = _rank(cs, 252)
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = 2.0 * np.sqrt((-cov).clip(lower=0))
    rs_r = _rank(rs, 252)
    b = pd.concat([a_r, cs_r, rs_r], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend persistence: smoothed sign of negative illiquidity change, 126d
def f16lq_f16_liquidity_illiquidity_profile_liqtrendpersist_base_v075_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    slope = -(lg - lg.shift(21))
    b = np.tanh(slope.rolling(63, min_periods=21).mean() * 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16lq_f16_liquidity_illiquidity_profile_amihud_21d_base_v001_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud_63d_base_v002_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud_126d_base_v003_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud_252d_base_v004_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudz_21d_base_v005_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudrank_63d_base_v006_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudterm_21v126_base_v007_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudterm_63v252_base_v008_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtrend_63d_base_v009_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihuddisp_63d_base_v010_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnover_63d_base_v011_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnover_21d_base_v012_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnoverz_63d_base_v013_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnoverrank_base_v014_signal,
    f16lq_f16_liquidity_illiquidity_profile_dollarturn_63d_base_v015_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnovdisp_base_v016_signal,
    f16lq_f16_liquidity_illiquidity_profile_thinfrac_63d_base_v017_signal,
    f16lq_f16_liquidity_illiquidity_profile_thinfrac_126d_base_v018_signal,
    f16lq_f16_liquidity_illiquidity_profile_dryupstreak_63d_base_v019_signal,
    f16lq_f16_liquidity_illiquidity_profile_dryupcount_252d_base_v020_signal,
    f16lq_f16_liquidity_illiquidity_profile_thindepth_63d_base_v021_signal,
    f16lq_f16_liquidity_illiquidity_profile_maxdry_126d_base_v022_signal,
    f16lq_f16_liquidity_illiquidity_profile_dollardry_63d_base_v023_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread_21d_base_v024_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread_63d_base_v025_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread_126d_base_v026_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspreadz_21d_base_v027_signal,
    f16lq_f16_liquidity_illiquidity_profile_csterm_21v126_base_v028_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspreadtrend_63d_base_v029_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspreadrank_63d_base_v030_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqtrend_63d_base_v031_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqtrend_126d_base_v032_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtermmom_base_v033_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvexpand_base_v034_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudfloor_base_v035_signal,
    f16lq_f16_liquidity_illiquidity_profile_amivest_63d_base_v036_signal,
    f16lq_f16_liquidity_illiquidity_profile_amivest_126d_base_v037_signal,
    f16lq_f16_liquidity_illiquidity_profile_retperturn_63d_base_v038_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangedv_21d_base_v039_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangedvz_63d_base_v040_signal,
    f16lq_f16_liquidity_illiquidity_profile_volcv_63d_base_v041_signal,
    f16lq_f16_liquidity_illiquidity_profile_volherf_21d_base_v042_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvherf_63d_base_v043_signal,
    f16lq_f16_liquidity_illiquidity_profile_logvoldisp_126d_base_v044_signal,
    f16lq_f16_liquidity_illiquidity_profile_logdv_63d_base_v045_signal,
    f16lq_f16_liquidity_illiquidity_profile_logdvgap_252d_base_v046_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvdrawdown_base_v047_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvrank_504d_base_v048_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread_63d_base_v049_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread_126d_base_v050_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspreadz_63d_base_v051_signal,
    f16lq_f16_liquidity_illiquidity_profile_closepin_21d_base_v052_signal,
    f16lq_f16_liquidity_illiquidity_profile_retac1_63d_base_v053_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratio_126d_base_v054_signal,
    f16lq_f16_liquidity_illiquidity_profile_zeroret_63d_base_v055_signal,
    f16lq_f16_liquidity_illiquidity_profile_tinyimpact_63d_base_v056_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqofilliq_base_v057_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqshockrec_base_v058_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqspikecnt_base_v059_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqasym_63d_base_v060_signal,
    f16lq_f16_liquidity_illiquidity_profile_turndry_63d_base_v061_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnaccel_base_v062_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqwret_21d_base_v063_signal,
    f16lq_f16_liquidity_illiquidity_profile_costcompound_base_v064_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqdiverge_base_v065_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud5d_63d_base_v066_signal,
    f16lq_f16_liquidity_illiquidity_profile_volprictrend_base_v067_signal,
    f16lq_f16_liquidity_illiquidity_profile_drypressure_base_v068_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadpervol_base_v069_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvcv_126d_base_v070_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudrank504_base_v071_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqregtime_base_v072_signal,
    f16lq_f16_liquidity_illiquidity_profile_tierbreach_base_v073_signal,
    f16lq_f16_liquidity_illiquidity_profile_costcomposite_base_v074_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqtrendpersist_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_ILLIQUIDITY_PROFILE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f16_liquidity_illiquidity_profile_base_001_075_claude: %d features pass" % n_features)
