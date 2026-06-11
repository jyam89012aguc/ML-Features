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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (liquidity / illiquidity) =====
def _f16_dollar_vol(closeadj, volume):
    return (closeadj * volume).replace(0, np.nan)


def _f16_amihud(closeadj, volume, w):
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    illiq = ret / dv
    return illiq.rolling(w, min_periods=max(2, w // 2)).mean()


def _f16_amihud_raw(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f16_dollar_vol(closeadj, volume)
    return ret / dv


def _f16_turnover(volume, w):
    typ = volume.rolling(w, min_periods=max(2, w // 2)).median()
    return volume / typ.replace(0, np.nan)


def _f16_corwin_schultz(high, low, w):
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


def _f16_kyle_lambda(closeadj, volume, w):
    # Kyle's lambda proxy: |return| regressed on signed-dollar-volume ~ slope of price impact
    ret = closeadj.pct_change()
    dv = _f16_dollar_vol(closeadj, volume)
    sgn = np.sign(ret)
    signed_dv = sgn * np.sqrt(dv)
    cov = ret.rolling(w, min_periods=max(2, w // 2)).cov(signed_dv)
    var = signed_dv.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


# ============================================================
# Kyle's lambda price-impact 63d (slope of return on signed sqrt-dollar-volume)
def f16lq_f16_liquidity_illiquidity_profile_kyle_63d_base_v076_signal(closeadj, volume):
    lam = _f16_kyle_lambda(closeadj, volume, 63)
    b = np.log(lam.abs().replace(0, np.nan) * 1e6 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle's lambda 126d de-trended by its 504d mean (medium-horizon impact anomaly)
def f16lq_f16_liquidity_illiquidity_profile_kyle_126d_base_v077_signal(closeadj, volume):
    lam = np.log(_f16_kyle_lambda(closeadj, volume, 126).abs().replace(0, np.nan) * 1e6 + 1.0)
    b = lam - lam.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle's lambda 63d percentile rank vs 252d (relative price-impact regime)
def f16lq_f16_liquidity_illiquidity_profile_kylerank_base_v078_signal(closeadj, volume):
    lam = _f16_kyle_lambda(closeadj, volume, 63).abs()
    b = _rank(lam, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kyle lambda trend: change in 63d price-impact over a quarter
def f16lq_f16_liquidity_illiquidity_profile_kyletrend_base_v079_signal(closeadj, volume):
    lam = np.log(_f16_kyle_lambda(closeadj, volume, 63).abs().replace(0, np.nan) * 1e6 + 1.0)
    b = lam - lam.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Pastor-Stambaugh style reversal liquidity ----
# return reversal vs signed volume: gamma in r_t+1 = ... + gamma*sign(r)*vol (illiquidity)
def f16lq_f16_liquidity_illiquidity_profile_psgamma_63d_base_v080_signal(closeadj, volume):
    ret = closeadj.pct_change()
    excess = ret
    signed_vol = np.sign(ret) * np.log(volume.replace(0, np.nan))
    fut = ret.shift(-1)
    cov = fut.rolling(63, min_periods=21).cov(signed_vol)
    var = signed_vol.rolling(63, min_periods=21).var()
    b = -(cov / var.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Pastor-Stambaugh gamma 126d
def f16lq_f16_liquidity_illiquidity_profile_psgamma_126d_base_v081_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed_vol = np.sign(ret) * np.log(volume.replace(0, np.nan))
    fut = ret.shift(-1)
    cov = fut.rolling(126, min_periods=63).cov(signed_vol)
    var = signed_vol.rolling(126, min_periods=63).var()
    b = -(cov / var.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-horizon return reversal strength (illiquidity bounce), 21d autocorr-based
def f16lq_f16_liquidity_illiquidity_profile_reversal_21d_base_v082_signal(closeadj):
    ret = closeadj.pct_change()
    b = -ret.rolling(21, min_periods=10).corr(ret.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volume entropy / distribution shape ----
# volume distribution entropy over 21d (even = liquid, concentrated = thin/lumpy)
def f16lq_f16_liquidity_illiquidity_profile_volentropy_21d_base_v083_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    p = volume / s.replace(0, np.nan)
    ent = -(p * np.log(p.replace(0, np.nan)))
    b = ent.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume entropy over 63d
def f16lq_f16_liquidity_illiquidity_profile_dventropy_63d_base_v084_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    s = dv.rolling(63, min_periods=21).sum()
    p = dv / s.replace(0, np.nan)
    ent = -(p * np.log(p.replace(0, np.nan)))
    b = ent.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume kurtosis 126d (fat tails = sporadic liquidity events)
def f16lq_f16_liquidity_illiquidity_profile_volkurt_126d_base_v085_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = lv.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume Gini-like dispersion 63d (mean absolute deviation / mean)
def f16lq_f16_liquidity_illiquidity_profile_volgini_63d_base_v086_signal(volume):
    m = _mean(volume, 63)
    mad = (volume - m).abs().rolling(63, min_periods=21).mean()
    b = mad / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity vs volatility / range ----
# illiquidity per unit of realized volatility (impact beyond what vol explains), 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqpervol_63d_base_v087_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = lg - _z(np.log(vol.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Corwin-Schultz spread per Parkinson volatility (spread component of range), 63d
def f16lq_f16_liquidity_illiquidity_profile_csperpark_63d_base_v088_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 63)
    park = ((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(63, min_periods=21).mean()
    b = cs / np.sqrt(park).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gaplessness: close-to-close vs intraday range (gappy illiquidity), 63d
def f16lq_f16_liquidity_illiquidity_profile_gapratio_63d_base_v089_signal(close, high, low):
    cc = close.pct_change().abs()
    rng = (high - low) / close.replace(0, np.nan)
    ratio = cc / (rng + cc).replace(0, np.nan)
    b = ratio.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity timing / persistence ----
# illiquidity persistence: AR(1) of daily log-Amihud over 126d (sticky illiquidity)
def f16lq_f16_liquidity_illiquidity_profile_illiqpersist_base_v090_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    lg = np.log(raw.replace(0, np.nan) * 1e12 + 1.0)
    b = lg.rolling(126, min_periods=63).corr(lg.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover persistence: AR(1) of log-turnover over 126d
def f16lq_f16_liquidity_illiquidity_profile_turnpersist_base_v091_signal(volume):
    lt = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    b = lt.rolling(126, min_periods=63).corr(lt.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 126d where Amihud trended up day-over-day (illiquidity worsening tilt)
def f16lq_f16_liquidity_illiquidity_profile_illiqupfrac_base_v092_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    up = (illiq.diff() > 0).astype(float)
    frac = up.rolling(126, min_periods=63).mean()
    depth = illiq.diff().clip(lower=0).rolling(126, min_periods=63).mean()
    b = frac + np.log(depth.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- effective spread variants ----
# Abdi-Ranaldo close-high-low spread proxy 63d (alternative to Corwin-Schultz)
def f16lq_f16_liquidity_illiquidity_profile_arspread_63d_base_v093_signal(close, high, low):
    eta = (np.log(high.replace(0, np.nan)) + np.log(low.replace(0, np.nan))) / 2.0
    c = np.log(close.replace(0, np.nan))
    s2 = 4.0 * (c - eta) * (c - eta.shift(-1))
    s2 = (-s2).clip(lower=0)  # use negative-covariance branch as spread^2 proxy
    b = np.sqrt(s2).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Abdi-Ranaldo spread z vs 252d
def f16lq_f16_liquidity_illiquidity_profile_arspreadz_base_v094_signal(close, high, low):
    eta = (np.log(high.replace(0, np.nan)) + np.log(low.replace(0, np.nan))) / 2.0
    c = np.log(close.replace(0, np.nan))
    s2 = 4.0 * (c - eta) * (c - eta.shift(-1))
    s2 = (-s2).clip(lower=0)
    sp = np.sqrt(s2).rolling(63, min_periods=21).mean()
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low spread proxy: 2*(high-low)/(high+low) averaged 21d (simple quoted-spread)
def f16lq_f16_liquidity_illiquidity_profile_hlspread_21d_base_v095_signal(high, low):
    sp = 2.0 * (high - low) / (high + low).replace(0, np.nan)
    b = sp.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity drawdown / collapse depth ----
# turnover drawdown: current 21d turnover vs its 252d peak (activity collapse)
def f16lq_f16_liquidity_illiquidity_profile_turndrawdown_base_v096_signal(volume):
    t = _f16_turnover(volume, 63).rolling(21, min_periods=10).mean()
    peak = t.rolling(252, min_periods=126).max()
    b = np.log((t / peak.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity recovery: current dollar-vol vs its 126d trough (bounce off dry-up)
def f16lq_f16_liquidity_illiquidity_profile_liqrecovery_base_v097_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    trough = dv.rolling(126, min_periods=63).min()
    b = np.log((dv / trough.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity range: 63d Amihud max minus min over 252d (illiquidity amplitude)
def f16lq_f16_liquidity_illiquidity_profile_illiqamp_base_v098_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = lg.rolling(252, min_periods=126).max() - lg.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volume-volatility coupling ----
# correlation of volume and absolute return over 63d (informed vs noise liquidity)
def f16lq_f16_liquidity_illiquidity_profile_volretcorr_63d_base_v099_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0, np.nan))
    b = lv.rolling(63, min_periods=21).corr(ar)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-range elasticity: cov(log volume, log range)/var(log range) over 63d
def f16lq_f16_liquidity_illiquidity_profile_volrangeelast_base_v100_signal(high, low, volume):
    lr = np.log((high / low.replace(0, np.nan)).replace(0, np.nan))
    lv = np.log(volume.replace(0, np.nan))
    cov = lv.rolling(63, min_periods=21).cov(lr)
    var = lr.rolling(63, min_periods=21).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- microstructure noise ----
# variance ratio 5d/1d minus 1 over 252d (longer window; price-discovery efficiency)
def f16lq_f16_liquidity_illiquidity_profile_varratio_252d_base_v101_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=126).var()
    v5 = lr.rolling(5).sum().rolling(252, min_periods=126).var()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 10d/1d variance ratio over 126d (multi-scale microstructure noise)
def f16lq_f16_liquidity_illiquidity_profile_varratio10_base_v102_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v10 = lr.rolling(10).sum().rolling(126, min_periods=63).var()
    b = v10 / (10.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd-order return autocorrelation 63d (lag-2 staleness, illiquid price adjustment)
def f16lq_f16_liquidity_illiquidity_profile_retac2_63d_base_v103_signal(closeadj):
    ret = closeadj.pct_change()
    b = ret.rolling(63, min_periods=21).corr(ret.shift(2))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- thin-trading regime composites ----
# liquidity-quality score: low illiquidity rank + low spread rank + high turnover rank
def f16lq_f16_liquidity_illiquidity_profile_liqquality_base_v104_signal(closeadj, high, low, volume):
    illiq_r = _rank(_f16_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252)
    turn_r = _rank(_f16_turnover(volume, 63), 252)
    b = turn_r - illiq_r - cs_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard-illiquidity flag intensity: illiquid & thin & wide-spread together, 63d
def f16lq_f16_liquidity_illiquidity_profile_graveilliq_base_v105_signal(closeadj, high, low, volume):
    illiq_r = _rank(_f16_amihud(closeadj, volume, 63), 252) + 0.5
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252) + 0.5
    dv = _f16_dollar_vol(closeadj, volume).rolling(63, min_periods=21).mean()
    thin_r = 0.5 - _rank(dv, 252)
    b = illiq_r * cs_r * thin_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity stress index: weighted sum of z-scored illiquidity, spread, dry-up, 63d
def f16lq_f16_liquidity_illiquidity_profile_liqstress_base_v106_signal(closeadj, high, low, volume):
    illiq = np.log(_f16_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    cs = _f16_corwin_schultz(high, low, 63)
    dv = np.log(_f16_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    b = _z(illiq, 252) + _z(cs, 252) - _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity timing across windows ----
# illiquidity convexity: 21d Amihud vs avg of 63d & 5d (curvature in term structure)
def f16lq_f16_liquidity_illiquidity_profile_illiqcurv_base_v107_signal(closeadj, volume):
    a5 = np.log(_f16_amihud(closeadj, volume, 5).replace(0, np.nan) * 1e12 + 1.0)
    a21 = np.log(_f16_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    a63 = np.log(_f16_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    b = a21 - 0.5 * (a5 + a63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread convexity across 21/63/126 windows
def f16lq_f16_liquidity_illiquidity_profile_csconvex_base_v108_signal(high, low):
    c21 = _f16_corwin_schultz(high, low, 21)
    c63 = _f16_corwin_schultz(high, low, 63)
    c126 = _f16_corwin_schultz(high, low, 126)
    b = c63 - 0.5 * (c21 + c126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity short-vs-long crossover momentum (21d-63d log-illiq diff change)
def f16lq_f16_liquidity_illiquidity_profile_illiqcross_base_v109_signal(closeadj, volume):
    a21 = np.log(_f16_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    a63 = np.log(_f16_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    diff = a21 - a63
    b = diff - diff.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-volume structure (liquidity-tier focus, not regime) ----
# dollar-volume vs 21d EMA minus vs 63d EMA (dollar-liquidity displacement)
def f16lq_f16_liquidity_illiquidity_profile_dvdisp_base_v110_signal(closeadj, volume):
    ldv = np.log(_f16_dollar_vol(closeadj, volume))
    b = ldv.ewm(span=10, min_periods=5).mean() - ldv.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# minimum 21d dollar-vol relative to median (worst-day liquidity floor), 252d
def f16lq_f16_liquidity_illiquidity_profile_dvworst_base_v111_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    worst = dv.rolling(21, min_periods=10).min()
    med = dv.rolling(252, min_periods=126).median()
    b = np.log((worst / med.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume skew 126d (lumpy dollar-liquidity tail)
def f16lq_f16_liquidity_illiquidity_profile_dvskew_base_v112_signal(closeadj, volume):
    ldv = np.log(_f16_dollar_vol(closeadj, volume))
    b = ldv.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- amihud weighted by sign / direction ----
# net signed illiquidity: |ret|/dollarvol signed by return direction, 63d mean
def f16lq_f16_liquidity_illiquidity_profile_signilliq_base_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    raw = _f16_amihud_raw(closeadj, volume)
    signed = np.sign(ret) * np.log(raw.replace(0, np.nan) * 1e12 + 1.0)
    b = signed.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-vs-down illiquidity asymmetry (buy impact minus sell impact), 63d
def f16lq_f16_liquidity_illiquidity_profile_upilliq_base_v114_signal(closeadj, volume):
    ret = closeadj.pct_change()
    raw = _f16_amihud_raw(closeadj, volume)
    up = np.log(raw.where(ret > 0).replace(0, np.nan) * 1e12 + 1.0).rolling(63, min_periods=10).mean()
    dn = np.log(raw.where(ret < 0).replace(0, np.nan) * 1e12 + 1.0).rolling(63, min_periods=10).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-day illiquidity trend (impact when selling), change over quarter, 63d
def f16lq_f16_liquidity_illiquidity_profile_downilliqtrend_base_v115_signal(closeadj, volume):
    ret = closeadj.pct_change()
    raw = _f16_amihud_raw(closeadj, volume).where(ret < 0)
    lg = np.log(raw.replace(0, np.nan) * 1e12 + 1.0).rolling(63, min_periods=10).mean()
    b = lg - lg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- turnover-liquidity timing ----
# turnover acceleration over 126d window (2nd diff of smoothed log-turnover)
def f16lq_f16_liquidity_illiquidity_profile_turnaccel2_base_v116_signal(volume):
    lt = np.log(_f16_turnover(volume, 126).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    d = lt - lt.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover regime breadth: 63d turnover vs 252d turnover ratio
def f16lq_f16_liquidity_illiquidity_profile_turnregime_base_v117_signal(volume):
    s = np.log(_f16_turnover(volume, 63).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    l = np.log(_f16_turnover(volume, 252).replace(0, np.nan)).rolling(252, min_periods=126).mean()
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 252d in high-turnover regime (turnover > 252d median) blended w/ depth
def f16lq_f16_liquidity_illiquidity_profile_turnregtime_base_v118_signal(volume):
    t = _f16_turnover(volume, 63)
    med = t.rolling(252, min_periods=126).median()
    hot = (t > med).astype(float).rolling(252, min_periods=126).mean()
    depth = (t / med.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = hot + 0.1 * np.log(depth.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- spread-impact interactions ----
# round-trip cost proxy: CS spread plus Amihud-implied impact for a typical trade, 63d
def f16lq_f16_liquidity_illiquidity_profile_roundtrip_base_v119_signal(closeadj, high, low, volume):
    cs = _f16_corwin_schultz(high, low, 63)
    illiq = _f16_amihud(closeadj, volume, 63)
    typ_dv = _f16_dollar_vol(closeadj, volume).rolling(63, min_periods=21).median()
    impact = illiq * typ_dv  # ~ |ret| for a median-size trade
    b = cs + 2.0 * impact
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-to-impact ratio: which friction dominates (quote vs depth), 63d
def f16lq_f16_liquidity_illiquidity_profile_spreadimpact_base_v120_signal(closeadj, high, low, volume):
    cs = _f16_corwin_schultz(high, low, 63)
    illiq = _f16_amihud(closeadj, volume, 63)
    typ_dv = _f16_dollar_vol(closeadj, volume).rolling(63, min_periods=21).median()
    impact = illiq * typ_dv
    b = np.log((cs.replace(0, np.nan)) / (impact.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity volatility / risk ----
# liquidity-risk: rolling std of log-turnover over 126d (turnover instability)
def f16lq_f16_liquidity_illiquidity_profile_turnrisk_base_v121_signal(volume):
    lt = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    b = _std(lt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-of-spread: std of daily CS spread proxy over 126d (spread instability)
def f16lq_f16_liquidity_illiquidity_profile_spreadrisk_base_v122_signal(high, low):
    cs_daily = _f16_corwin_schultz(high, low, 2)
    b = _std(cs_daily, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-vol semi-deviation (downside liquidity risk), 126d
def f16lq_f16_liquidity_illiquidity_profile_dvsemidev_base_v123_signal(closeadj, volume):
    ldv = np.log(_f16_dollar_vol(closeadj, volume))
    chg = ldv.diff()
    down = chg.where(chg < 0)
    b = np.sqrt((down ** 2).rolling(126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- new amihud facets ----
# Amihud measured with high-low range as the move (range-based illiquidity), 63d
def f16lq_f16_liquidity_illiquidity_profile_rangeamihud_base_v124_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _f16_dollar_vol(closeadj, volume)
    illiq = (rng / dv).rolling(63, min_periods=21).mean()
    b = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud measured with raw volume (not dollar) as the denominator, 63d
def f16lq_f16_liquidity_illiquidity_profile_volamihud_base_v125_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    illiq = (ret / volume.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = np.log(illiq.replace(0, np.nan) * 1e9 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-minus-median daily illiquidity over 63d (right-tail illiquidity skew)
def f16lq_f16_liquidity_illiquidity_profile_medamihud_base_v126_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    mean_lg = np.log(raw.rolling(63, min_periods=21).mean().replace(0, np.nan) * 1e12 + 1.0)
    med_lg = np.log(raw.rolling(63, min_periods=21).median().replace(0, np.nan) * 1e12 + 1.0)
    b = mean_lg - med_lg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud tail: 90th-percentile daily illiquidity over 63d (worst-impact days)
def f16lq_f16_liquidity_illiquidity_profile_tailamihud_base_v127_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    q90 = raw.rolling(63, min_periods=21).quantile(0.90)
    b = np.log(q90.replace(0, np.nan) * 1e12 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud tail-to-median ratio (illiquidity spikiness), 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqspiky_base_v128_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    q90 = raw.rolling(63, min_periods=21).quantile(0.90)
    med = raw.rolling(63, min_periods=21).median()
    b = np.log((q90 / med.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity trend / momentum facets ----
# Amihud 252d trend (illiquidity drift over a year)
def f16lq_f16_liquidity_illiquidity_profile_amihudtrend252_base_v129_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 252)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    b = lg - lg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover trend 252d (year-over-year activity drift)
def f16lq_f16_liquidity_illiquidity_profile_turntrend252_base_v130_signal(volume):
    lt = np.log(_f16_turnover(volume, 252).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = lt - lt.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread trend long: change in 126d CS spread over half year
def f16lq_f16_liquidity_illiquidity_profile_csspreadtrend126_base_v131_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 126)
    b = cs - cs.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity vs price-level (size / penny-stock proxy) ----
# illiquidity sensitivity to price level: penny-stock illiquidity amplification, 63d
def f16lq_f16_liquidity_illiquidity_profile_pennyilliq_base_v132_signal(closeadj, volume):
    illiq = np.log(_f16_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    invprice = 1.0 / closeadj.replace(0, np.nan)
    b = illiq * _z(invprice, 252).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover x inverse-price (small-price churn intensity), 63d
def f16lq_f16_liquidity_illiquidity_profile_lowpriceturn_base_v133_signal(closeadj, volume):
    t = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    pr = _z(np.log(closeadj.replace(0, np.nan)), 252)
    b = t - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite liquidity scores ----
# illiquidity composite rank: mean of Amihud, Kyle, CS-spread, Roll-spread ranks, 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqcomposite_base_v134_signal(closeadj, high, low, volume):
    a_r = _rank(_f16_amihud(closeadj, volume, 63), 252)
    k_r = _rank(_f16_kyle_lambda(closeadj, volume, 63).abs(), 252)
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252)
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = 2.0 * np.sqrt((-cov).clip(lower=0))
    rs_r = _rank(rs, 252)
    b = pd.concat([a_r, k_r, cs_r, rs_r], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity dispersion across estimators: std of the four illiquidity ranks, 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqdisagree_base_v135_signal(closeadj, high, low, volume):
    a_r = _rank(_f16_amihud(closeadj, volume, 63), 252)
    k_r = _rank(_f16_kyle_lambda(closeadj, volume, 63).abs(), 252)
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252)
    t_r = _rank(_f16_turnover(volume, 63), 252)
    b = pd.concat([a_r, k_r, cs_r, t_r], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity event recency / counts (blended continuous) ----
# days since worst-illiquidity day (Amihud 252d max) blended with current level
def f16lq_f16_liquidity_illiquidity_profile_illiqrecency_base_v136_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 21)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)

    def _dsmax(a):
        return float(len(a) - 1 - int(np.argmax(a))) / float(len(a))
    dsm = lg.rolling(252, min_periods=126).apply(_dsmax, raw=True)
    b = dsm + 0.3 * _z(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 126d with widening spread (spread momentum tilt) blended with magnitude
def f16lq_f16_liquidity_illiquidity_profile_spreadwiden_base_v137_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 21)
    up = (cs.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    mag = cs.diff().clip(lower=0).rolling(126, min_periods=63).mean()
    b = up + 50.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of liquidity-improvement days (dollar-vol jumps >50%) over 252d blended depth
def f16lq_f16_liquidity_illiquidity_profile_liqimprove_base_v138_signal(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    jump = (dv / dv.shift(1).replace(0, np.nan) - 1.0)
    cnt = (jump > 0.5).astype(float).rolling(252, min_periods=126).sum()
    mag = jump.clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 20.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity smoothness / clustering ----
# Amihud autocorrelation clustering: illiquidity clustering index, 126d
def f16lq_f16_liquidity_illiquidity_profile_illiqcluster_base_v139_signal(closeadj, volume):
    raw = _f16_amihud_raw(closeadj, volume)
    lg = np.log(raw.replace(0, np.nan) * 1e12 + 1.0)
    hi = (lg > lg.rolling(126, min_periods=63).median()).astype(float)
    b = hi.rolling(126, min_periods=63).apply(lambda a: np.mean(a[1:] * a[:-1]) if len(a) > 1 else np.nan, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume run-length asymmetry: avg up-volume-run vs down-volume-run length, 63d
def f16lq_f16_liquidity_illiquidity_profile_volrunasym_base_v140_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    up = (lv.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean() - 0.5 + _z(lv, 126) * 0.05
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- liquidity-adjusted return / pricing ----
# illiquidity premium proxy: trailing return scaled by illiquidity rank, 63d
def f16lq_f16_liquidity_illiquidity_profile_illiqprem_base_v141_signal(closeadj, volume):
    ret = closeadj.pct_change().rolling(63, min_periods=21).sum()
    illiq_r = _rank(_f16_amihud(closeadj, volume, 63), 252) + 0.5
    b = ret * illiq_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-timing return: return on liquid days minus illiquid days, 126d
def f16lq_f16_liquidity_illiquidity_profile_liqtimingret_base_v142_signal(closeadj, volume):
    ret = closeadj.pct_change()
    illiq = _f16_amihud_raw(closeadj, volume)
    med = illiq.rolling(126, min_periods=63).median()
    liquid_ret = ret.where(illiq < med).rolling(126, min_periods=30).mean()
    illiquid_ret = ret.where(illiq >= med).rolling(126, min_periods=30).mean()
    b = liquid_ret - illiquid_ret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional spread proxies ----
# Roll spread using log-returns over 21d (short-horizon effective spread)
def f16lq_f16_liquidity_illiquidity_profile_rollspread_21d_base_v143_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    cov = lr.rolling(21, min_periods=10).cov(lr.shift(1))
    b = 2.0 * np.sqrt((-cov).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Roll spread trend: change in 63d Roll spread over a quarter
def f16lq_f16_liquidity_illiquidity_profile_rollspreadtrend_base_v144_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    rs = 2.0 * np.sqrt((-cov).clip(lower=0))
    b = rs - rs.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-cost per dollar traded: (CS spread)/log(dollar-vol) friction-density, 63d
def f16lq_f16_liquidity_illiquidity_profile_costdensity_base_v145_signal(closeadj, high, low, volume):
    cs = _f16_corwin_schultz(high, low, 63)
    ldv = np.log(_f16_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    b = cs * (1.0 / ldv.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- final liquidity-regime distances ----
# distance of current illiquidity from its 252d 25th pct (best-liquidity baseline)
def f16lq_f16_liquidity_illiquidity_profile_illiqbasedist_base_v146_signal(closeadj, volume):
    illiq = _f16_amihud(closeadj, volume, 63)
    lg = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    base = lg.rolling(252, min_periods=126).quantile(0.25)
    b = lg - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover distance from its 252d 75th pct (distance below peak-activity tier)
def f16lq_f16_liquidity_illiquidity_profile_turnpeakdist_base_v147_signal(volume):
    lt = np.log(_f16_turnover(volume, 63).replace(0, np.nan))
    peak = lt.rolling(252, min_periods=126).quantile(0.75)
    b = lt - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread distance from its 252d 25th pct (excess spread over tightest baseline)
def f16lq_f16_liquidity_illiquidity_profile_csbasedist_base_v148_signal(high, low):
    cs = _f16_corwin_schultz(high, low, 63)
    base = cs.rolling(252, min_periods=126).quantile(0.25)
    b = cs - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined friction momentum: change in illiquidity composite over a quarter, 63d
def f16lq_f16_liquidity_illiquidity_profile_frictionmom_base_v149_signal(closeadj, high, low, volume):
    a_r = _rank(_f16_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252)
    comp = (a_r + cs_r) / 2.0
    b = comp - comp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-quality persistence: smoothed tanh of negative illiquidity composite, 126d
def f16lq_f16_liquidity_illiquidity_profile_liqqualpersist_base_v150_signal(closeadj, high, low, volume):
    a_r = _rank(_f16_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_f16_corwin_schultz(high, low, 63), 252)
    illiq = (a_r + cs_r) / 2.0
    b = np.tanh(-illiq.rolling(126, min_periods=63).mean() * 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16lq_f16_liquidity_illiquidity_profile_kyle_63d_base_v076_signal,
    f16lq_f16_liquidity_illiquidity_profile_kyle_126d_base_v077_signal,
    f16lq_f16_liquidity_illiquidity_profile_kylerank_base_v078_signal,
    f16lq_f16_liquidity_illiquidity_profile_kyletrend_base_v079_signal,
    f16lq_f16_liquidity_illiquidity_profile_psgamma_63d_base_v080_signal,
    f16lq_f16_liquidity_illiquidity_profile_psgamma_126d_base_v081_signal,
    f16lq_f16_liquidity_illiquidity_profile_reversal_21d_base_v082_signal,
    f16lq_f16_liquidity_illiquidity_profile_volentropy_21d_base_v083_signal,
    f16lq_f16_liquidity_illiquidity_profile_dventropy_63d_base_v084_signal,
    f16lq_f16_liquidity_illiquidity_profile_volkurt_126d_base_v085_signal,
    f16lq_f16_liquidity_illiquidity_profile_volgini_63d_base_v086_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqpervol_63d_base_v087_signal,
    f16lq_f16_liquidity_illiquidity_profile_csperpark_63d_base_v088_signal,
    f16lq_f16_liquidity_illiquidity_profile_gapratio_63d_base_v089_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqpersist_base_v090_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnpersist_base_v091_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqupfrac_base_v092_signal,
    f16lq_f16_liquidity_illiquidity_profile_arspread_63d_base_v093_signal,
    f16lq_f16_liquidity_illiquidity_profile_arspreadz_base_v094_signal,
    f16lq_f16_liquidity_illiquidity_profile_hlspread_21d_base_v095_signal,
    f16lq_f16_liquidity_illiquidity_profile_turndrawdown_base_v096_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqrecovery_base_v097_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqamp_base_v098_signal,
    f16lq_f16_liquidity_illiquidity_profile_volretcorr_63d_base_v099_signal,
    f16lq_f16_liquidity_illiquidity_profile_volrangeelast_base_v100_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratio_252d_base_v101_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratio10_base_v102_signal,
    f16lq_f16_liquidity_illiquidity_profile_retac2_63d_base_v103_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqquality_base_v104_signal,
    f16lq_f16_liquidity_illiquidity_profile_graveilliq_base_v105_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqstress_base_v106_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcurv_base_v107_signal,
    f16lq_f16_liquidity_illiquidity_profile_csconvex_base_v108_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcross_base_v109_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvdisp_base_v110_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvworst_base_v111_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvskew_base_v112_signal,
    f16lq_f16_liquidity_illiquidity_profile_signilliq_base_v113_signal,
    f16lq_f16_liquidity_illiquidity_profile_upilliq_base_v114_signal,
    f16lq_f16_liquidity_illiquidity_profile_downilliqtrend_base_v115_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnaccel2_base_v116_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnregime_base_v117_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnregtime_base_v118_signal,
    f16lq_f16_liquidity_illiquidity_profile_roundtrip_base_v119_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadimpact_base_v120_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnrisk_base_v121_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadrisk_base_v122_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvsemidev_base_v123_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangeamihud_base_v124_signal,
    f16lq_f16_liquidity_illiquidity_profile_volamihud_base_v125_signal,
    f16lq_f16_liquidity_illiquidity_profile_medamihud_base_v126_signal,
    f16lq_f16_liquidity_illiquidity_profile_tailamihud_base_v127_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqspiky_base_v128_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtrend252_base_v129_signal,
    f16lq_f16_liquidity_illiquidity_profile_turntrend252_base_v130_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspreadtrend126_base_v131_signal,
    f16lq_f16_liquidity_illiquidity_profile_pennyilliq_base_v132_signal,
    f16lq_f16_liquidity_illiquidity_profile_lowpriceturn_base_v133_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcomposite_base_v134_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqdisagree_base_v135_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqrecency_base_v136_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadwiden_base_v137_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqimprove_base_v138_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcluster_base_v139_signal,
    f16lq_f16_liquidity_illiquidity_profile_volrunasym_base_v140_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqprem_base_v141_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqtimingret_base_v142_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread_21d_base_v143_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspreadtrend_base_v144_signal,
    f16lq_f16_liquidity_illiquidity_profile_costdensity_base_v145_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqbasedist_base_v146_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnpeakdist_base_v147_signal,
    f16lq_f16_liquidity_illiquidity_profile_csbasedist_base_v148_signal,
    f16lq_f16_liquidity_illiquidity_profile_frictionmom_base_v149_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqqualpersist_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_ILLIQUIDITY_PROFILE_REGISTRY_076_150 = REGISTRY


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

    print("OK f16_liquidity_illiquidity_profile_base_076_150_claude: %d features pass" % n_features)
