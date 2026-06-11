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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _dv(closeadj, volume):
    return closeadj.replace(0, np.nan).abs() * volume.abs()


def _ldv(closeadj, volume):
    return np.log(_dv(closeadj, volume).replace(0, np.nan))


def _rngpos(ldv, w):
    hi = ldv.rolling(w, min_periods=max(1, w // 2)).max()
    lo = ldv.rolling(w, min_periods=max(1, w // 2)).min()
    return (ldv - lo) / (hi - lo).replace(0, np.nan)


# ============================================================
# slope = first math derivative (ROC) of a dollar-volume base feature.
# Each function computes its base inline, then differences it over an
# ROC window matched to the base window (5d base->5d; 21d->5/21; 252d->21/63).


# slope of 21d log-dv level (5d ROC) — liquidity-level velocity
def f17dv_f17_dollar_volume_dynamics_dvlevel21_5d_slope_v001_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 21)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-dv level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel63_21d_slope_v002_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-dv level (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel252_63d_slope_v003_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d log-dv level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel126_21d_slope_v004_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 126)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 63d dispersion (63d ROC) — instability velocity
def f17dv_f17_dollar_volume_dynamics_dvz63_21d_slope_v005_signal(closeadj, volume):
    base = _std(_ldv(closeadj, volume), 63)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d up/down dollar-volume balance (63d ROC) — slow directional-liquidity velocity
def f17dv_f17_dollar_volume_dynamics_dvz252_21d_slope_v006_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-dv kurtosis (5d ROC) — fast tail-shape velocity
def f17dv_f17_dollar_volume_dynamics_dvz126_21d_slope_v007_signal(closeadj, volume):
    base = _ldv(closeadj, volume).rolling(63, min_periods=21).kurt()
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume rank (21d ROC) — tier-position velocity
def f17dv_f17_dollar_volume_dynamics_dvrank252_21d_slope_v008_signal(closeadj, volume):
    base = _rank(_ldv(closeadj, volume), 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d dollar-volume rank (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrank504_63d_slope_v009_signal(closeadj, volume):
    base = _rank(_ldv(closeadj, volume), 504)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike-persistence (excess above 2x band) (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrngpos252_21d_slope_v010_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    base = (dv / avg.replace(0, np.nan) - 2.0).clip(lower=0).rolling(21, min_periods=10).mean()
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume concentration Herfindahl (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrngpos504_63d_slope_v011_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(252, min_periods=126).sum().replace(0, np.nan)
    base = (share ** 2).rolling(252, min_periods=126).sum()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume drawdown (21d ROC) — dry-up velocity
def f17dv_f17_dollar_volume_dynamics_dvdd252_21d_slope_v012_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 126d ulcer (drawdown RMS) (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdd126_21d_slope_v013_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(126, min_periods=63).max().replace(0, np.nan) - 1.0
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume drawdown (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdd63_5d_slope_v014_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = dv / dv.rolling(63, min_periods=21).max().replace(0, np.nan) - 1.0
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d dollar-volume spike ratio (5d ROC) — surge velocity
def f17dv_f17_dollar_volume_dynamics_dvspike21_5d_slope_v015_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(dv.replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume spike ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspike63_21d_slope_v016_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 5).replace(0, np.nan) / _mean(dv, 63).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d up/down dollar-volume balance (21d ROC) — directional-liquidity velocity
def f17dv_f17_dollar_volume_dynamics_dvupdown63_21d_slope_v017_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d up/down dollar-volume balance (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupdown252_63d_slope_v018_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=126).sum()
    dn = dv.where(ret < 0, 0.0).rolling(252, min_periods=126).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume Herfindahl (21d ROC) — concentration velocity
def f17dv_f17_dollar_volume_dynamics_dvherf63_21d_slope_v019_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume Herfindahl (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvherf252_63d_slope_v020_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(252, min_periods=126).sum().replace(0, np.nan)
    base = (share ** 2).rolling(252, min_periods=126).sum()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-dv dispersion (21d ROC) — instability velocity
def f17dv_f17_dollar_volume_dynamics_dvdisp63_21d_slope_v021_signal(closeadj, volume):
    base = _std(_ldv(closeadj, volume), 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-dv dispersion (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdisp252_63d_slope_v022_signal(closeadj, volume):
    base = _std(_ldv(closeadj, volume), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume CV (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvcv63_21d_slope_v023_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _std(dv, 63) / _mean(dv, 63).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs price-size proxy (21d ROC) — turnover-of-value velocity
def f17dv_f17_dollar_volume_dynamics_dvsize63_21d_slope_v024_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lp = np.log(closeadj.replace(0, np.nan))
    base = _mean(ldv - lp, 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume top5-day share over a quarter (63d ROC)
def f17dv_f17_dollar_volume_dynamics_tierdist252_21d_slope_v025_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    tot = dv.rolling(63, min_periods=21).sum()
    top5 = dv.rolling(63, min_periods=21).apply(lambda a: np.sort(a)[-5:].sum(), raw=True)
    base = top5 / tot.replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 63d IQR (63d ROC) — robust-dispersion velocity
def f17dv_f17_dollar_volume_dynamics_tierfloor252_21d_slope_v026_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(63, min_periods=21).quantile(0.75) - ldv.rolling(63, min_periods=21).quantile(0.25)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume per-move depth (21d ROC) — depth-of-market velocity
def f17dv_f17_dollar_volume_dynamics_dvpermove21_21d_slope_v027_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    base = _mean(np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan)), 21)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume top5 share (21d ROC) — event-share velocity
def f17dv_f17_dollar_volume_dynamics_dvtop563_21d_slope_v028_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    tot = dv.rolling(63, min_periods=21).sum()
    top5 = dv.rolling(63, min_periods=21).apply(lambda a: np.sort(a)[-5:].sum(), raw=True)
    base = top5 / tot.replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max/median spike ratio over a quarter (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtrenddist252_21d_slope_v029_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    md = dv.rolling(63, min_periods=21).median()
    base = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d/126d EMA displacement (21d ROC) — liquidity-momentum velocity
def f17dv_f17_dollar_volume_dynamics_dvemadisp63_21d_slope_v030_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume drawdown duration (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvddur252_21d_slope_v031_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dollar-volume skew (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvskew63_21d_slope_v032_signal(closeadj, volume):
    base = _dv(closeadj, volume).rolling(63, min_periods=21).skew()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d log-dv skew (21d ROC)
def f17dv_f17_dollar_volume_dynamics_ldvskew126_21d_slope_v033_signal(closeadj, volume):
    base = _ldv(closeadj, volume).rolling(126, min_periods=63).skew()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-dv kurtosis (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvkurt63_21d_slope_v034_signal(closeadj, volume):
    base = _ldv(closeadj, volume).rolling(63, min_periods=21).kurt()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume cumulative quarter/year ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvcumratio_21d_slope_v035_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    q = dv.rolling(63, min_periods=21).sum()
    y = dv.rolling(252, min_periods=126).sum()
    base = (q * 4.0) / y.replace(0, np.nan) - 1.0
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume top-tercile-time tier instability (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtierdisp252_21d_slope_v036_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    base = rp.rolling(63, min_periods=21).std()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume to 252d-mean ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtomean252_21d_slope_v037_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 252).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d upside dollar-volume semi-dispersion (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupsemi63_21d_slope_v038_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    up = (ldv - _mean(ldv, 63)).clip(lower=0)
    base = (up ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d downside dollar-volume semi-dispersion (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdnsemi63_21d_slope_v039_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    dn = (_mean(ldv, 63) - ldv).clip(lower=0)
    base = (dn ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawdown vs price drawdown gap (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvvspxdd252_21d_slope_v040_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dvdd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    pxdd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    base = dvdd - pxdd
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d log-dv level (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel504_63d_slope_v041_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 504)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs price co-movement over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvz504_63d_slope_v042_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    base = dvchg.rolling(252, min_periods=126).corr(ret)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume tier spread (63d rank vs 252d rank) (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrank126_21d_slope_v043_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = _rank(ldv, 63) - _rank(ldv, 252)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d dollar-volume drawdown (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdd504_63d_slope_v044_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = dv / dv.rolling(504, min_periods=252).max().replace(0, np.nan) - 1.0
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d dollar-volume spike (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspike5_5d_slope_v045_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 5).replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d up/down dollar-volume balance (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupdown21_5d_slope_v046_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs raw-volume z divergence (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvvoldiv252_21d_slope_v047_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    base = _z(ldv, 252) - _z(lv, 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume per-move depth z over a year (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvpermove252_63d_slope_v048_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    base = _z(np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan)), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d dollar-volume CV (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvcv126_21d_slope_v049_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 21d-mean to 504d-mean ratio (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_slope_v050_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 63).replace(0, np.nan) / _mean(dv, 504).replace(0, np.nan))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intraday-range dollar churn level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvchurn63_21d_slope_v051_signal(closeadj, volume, high, low):
    rangefrac = (high - low).abs() / closeadj.replace(0, np.nan)
    base = _mean(np.log(rangefrac.replace(0, np.nan)), 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs intraday-range value ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrangeval21_21d_slope_v052_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    rangeval = (high - low).abs() * volume.abs()
    base = _mean(np.log((dv / rangeval.replace(0, np.nan)).replace(0, np.nan)), 21)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume Gini concentration over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtier252_21d_slope_v053_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _gini(a):
        a = np.sort(a)
        m = len(a)
        s = a.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, m + 1)
        return float((2.0 * np.dot(idx, a) / (m * s)) - (m + 1.0) / m)

    base = dv.rolling(126, min_periods=63).apply(_gini, raw=True)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume sign x magnitude momentum (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvsignmag63_21d_slope_v054_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    chg = m - m.shift(63)
    base = np.sign(chg) * (chg.abs() ** 0.5)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume effort-to-result (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dveffort63_21d_slope_v055_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    cumdv = dv.rolling(63, min_periods=21).sum()
    move = (closeadj / closeadj.shift(63) - 1.0).abs()
    base = np.log(cumdv.replace(0, np.nan)) - np.log((move * 100.0).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume per-risk level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvperrisk63_21d_slope_v056_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = _mean(ldv, 21) - np.log(vol.replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume IQR (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dviqr63_21d_slope_v057_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(63, min_periods=21).quantile(0.75) - ldv.rolling(63, min_periods=21).quantile(0.25)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume tail spread (95-50 pct) (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtailspr126_21d_slope_v058_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(126, min_periods=63).quantile(0.95) - ldv.rolling(126, min_periods=63).quantile(0.50)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs price co-movement (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvpxcorr63_21d_slope_v059_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    base = dvchg.rolling(63, min_periods=30).corr(ret)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max-day share over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvmaxshare63_21d_slope_v060_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = dv.rolling(252, min_periods=126).sum()
    base = (mx * 63.0) / tot.replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume up-day fraction momentum (5d ROC) — flow-consistency velocity
def f17dv_f17_dollar_volume_dynamics_dvlevel21_21d_slope_v061_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = (ldv.diff() > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5 \
        + 5.0 * ldv.diff().rolling(63, min_periods=21).mean()
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-dv level (5d ROC) — fast velocity of medium level
def f17dv_f17_dollar_volume_dynamics_dvlevel63_5d_slope_v062_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 63)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-dv level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel252_21d_slope_v063_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 126d log-dv kurtosis (63d ROC) — tail-shape velocity
def f17dv_f17_dollar_volume_dynamics_dvz63_5d_slope_v064_signal(closeadj, volume):
    base = _ldv(closeadj, volume).rolling(126, min_periods=63).kurt()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d dollar-volume z (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvz252_63d_slope_v065_signal(closeadj, volume):
    base = _z(_ldv(closeadj, volume), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 252d skewness (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrank252_63d_slope_v066_signal(closeadj, volume):
    base = _dv(closeadj, volume).rolling(252, min_periods=126).skew()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume Herfindahl over a quarter (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrngpos252_63d_slope_v067_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawup off 252d trough (63d ROC) — revival velocity
def f17dv_f17_dollar_volume_dynamics_dvdd252_63d_slope_v068_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log((dv / dv.rolling(252, min_periods=126).min().replace(0, np.nan)).replace(0, np.nan))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike tail kurtosis (21d ROC) — surge-tail velocity
def f17dv_f17_dollar_volume_dynamics_dvspike21_21d_slope_v069_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    sp = np.log(dv.replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    base = sp.rolling(63, min_periods=21).kurt()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max/median ratio over a quarter (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspike63_5d_slope_v070_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    md = dv.rolling(63, min_periods=21).median()
    base = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d up/down balance (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupdown63_5d_slope_v071_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d Herfindahl (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvherf63_5d_slope_v072_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d dispersion (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdisp63_5d_slope_v073_signal(closeadj, volume):
    base = _std(_ldv(closeadj, volume), 63)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs raw-volume rank divergence (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvsize252_63d_slope_v074_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    base = _rank(ldv, 252) - _rank(lv, 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 252d ulcer (drawdown RMS) (63d ROC)
def f17dv_f17_dollar_volume_dynamics_tierdist504_63d_slope_v075_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume regime fraction-above-median (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvregime63_21d_slope_v076_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    med = ldv.rolling(252, min_periods=126).median()
    base = (ldv > med).astype(float).rolling(63, min_periods=21).mean() - 0.5
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume new-252d-high frequency (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvnewhi252_21d_slope_v077_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    hi = ldv.rolling(252, min_periods=126).max()
    base = (ldv >= hi - 1e-9).astype(float).rolling(63, min_periods=21).mean() \
        + 0.25 * (ldv - hi).rolling(21, min_periods=10).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume thin-fraction (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvthinfrac63_21d_slope_v078_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(252, min_periods=126).median()
    base = (dv < med * 0.25).astype(float).rolling(63, min_periods=21).mean() \
        + ((med * 0.25 - dv).clip(lower=0) / med.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume wave amplitude (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvwave63_21d_slope_v079_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    s = dv.rolling(21, min_periods=10).sum()
    base = np.log(s.replace(0, np.nan) / s.shift(63).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume autocorrelation (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvautocorr63_21d_slope_v080_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(63, min_periods=30).apply(lambda a: pd.Series(a).autocorr(lag=1), raw=False)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume top-tercile time (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtoptime252_21d_slope_v081_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    base = (rp >= 0.6667).astype(float).rolling(63, min_periods=21).mean() \
        + 3.0 * (rp - 0.6667).clip(lower=0).rolling(21, min_periods=10).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawup off 63d trough (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdrawup63_21d_slope_v082_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log((dv / dv.rolling(63, min_periods=21).min().replace(0, np.nan)).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max/median ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvmaxmed63_21d_slope_v083_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    md = dv.rolling(63, min_periods=21).median()
    base = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume min/median ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvminmed63_21d_slope_v084_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mn = dv.rolling(63, min_periods=21).min()
    md = dv.rolling(63, min_periods=21).median()
    base = np.log(mn.replace(0, np.nan) / md.replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OLS 63d log-dv trend slope (21d ROC) — trend-of-trend
def f17dv_f17_dollar_volume_dynamics_dvolsslope63_21d_slope_v085_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)

    def _sl(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        den = (xc ** 2).sum()
        if den <= 0:
            return np.nan
        return float(np.dot(a - a.mean(), xc) / den)

    base = ldv.rolling(63, min_periods=40).apply(_sl, raw=True)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume per-move depth over 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvpermove126_21d_slope_v086_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    ratio = np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan))
    base = _mean(ratio, 63) - _mean(ratio, 126)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs raw-volume rank divergence (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvvolrankdiv252_21d_slope_v087_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    base = _rank(ldv, 252) - _rank(lv, 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 504d EMA crossover (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvemadisp252_63d_slope_v088_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.ewm(span=63, min_periods=21).mean() - ldv.ewm(span=252, min_periods=126).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume IQR over 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dviqr126_21d_slope_v089_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(126, min_periods=63).quantile(0.75) - ldv.rolling(126, min_periods=63).quantile(0.25)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume floor spread (50-5 pct) (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvfloorspr126_21d_slope_v090_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(126, min_periods=63).quantile(0.50) - ldv.rolling(126, min_periods=63).quantile(0.05)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume up-day fraction momentum (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupfrac63_21d_slope_v091_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = (ldv.diff() > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5 \
        + 5.0 * ldv.diff().rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume semi-dispersion asymmetry (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvsemiasym63_21d_slope_v092_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    us = ((ldv - m).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    ds = ((m - ldv).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    base = (us - ds) / (us + ds).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 252d underwater fraction (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvuwfrac252_63d_slope_v093_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume per-risk over 21d (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvperrisk21_5d_slope_v094_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    base = _mean(ldv, 21) - np.log(vol.replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume tier spread short vs long (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtierspr_21d_slope_v095_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = _rank(ldv, 63) - _rank(ldv, 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume churn z (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvchurnz252_63d_slope_v096_signal(closeadj, volume, high, low):
    churn = (high - low).abs() / closeadj.replace(0, np.nan) * _dv(closeadj, volume)
    base = _z(np.log(churn.replace(0, np.nan)), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs high-low value ratio (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvhlratio21_21d_slope_v097_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    hlval = ((high + low) / 2.0).abs() * volume.abs()
    base = _mean(np.log((dv / hlval.replace(0, np.nan)).replace(0, np.nan)), 21)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume tier range/mobility (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtierrange252_21d_slope_v098_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    base = rp.rolling(126, min_periods=63).max() - rp.rolling(126, min_periods=63).min()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume top1 share over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtop1252_21d_slope_v099_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(252, min_periods=126).max()
    tot = dv.rolling(252, min_periods=126).sum()
    base = (mx * 252.0) / tot.replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max-min log spread (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvmaxmin252_63d_slope_v100_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(252, min_periods=126).max() - ldv.rolling(252, min_periods=126).min()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume momentum 63d (5d ROC) — accel-ish of fast momentum
def f17dv_f17_dollar_volume_dynamics_dvmom63_5d_slope_v101_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    base = m - m.shift(63)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume momentum 252d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvmom252_21d_slope_v102_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    base = m - m.shift(252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume top-tercile time (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvsidemean63_21d_slope_v103_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    base = (rp >= 0.6667).astype(float).rolling(63, min_periods=21).mean() \
        + 3.0 * (rp - 0.6667).clip(lower=0).rolling(21, min_periods=10).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawdown ulcer (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvulcer252_21d_slope_v104_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike-frequency (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspikefreq63_21d_slope_v105_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    base = (dv > 2.0 * med).astype(float).rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume to-mean ratio over 504d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtomean504_21d_slope_v106_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 63).replace(0, np.nan) / _mean(dv, 504).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume semi-dispersion asymmetry 63d (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupsemi252_63d_slope_v107_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    us = ((ldv - m).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    ds = ((m - ldv).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    base = (us - ds) / (us + ds).replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume dispersion ratio short/long (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdispratio_21d_slope_v108_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = _std(ldv, 21) / _std(ldv, 126).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume change-autocorrelation (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvchgac63_21d_slope_v109_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    base = d.rolling(63, min_periods=30).apply(lambda a: pd.Series(a).autocorr(lag=1), raw=False)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume effort-z over a year (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dveffortz252_63d_slope_v110_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    cumdv = dv.rolling(21, min_periods=10).sum()
    move = (closeadj / closeadj.shift(21) - 1.0).abs()
    base = _z(np.log(cumdv.replace(0, np.nan)) - np.log((move * 100.0).replace(0, np.nan)), 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 126d CV (63d ROC) — relative-instability velocity
def f17dv_f17_dollar_volume_dynamics_dvlvl126_21d_slope_v111_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike persistence (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspikepersist21_21d_slope_v112_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    base = (dv / avg.replace(0, np.nan) - 1.5).clip(lower=0).rolling(21, min_periods=10).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume gini concentration (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvgini252_63d_slope_v113_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _gini(a):
        a = np.sort(a)
        m = len(a)
        s = a.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, m + 1)
        return float((2.0 * np.dot(idx, a) / (m * s)) - (m + 1.0) / m)

    base = dv.rolling(252, min_periods=126).apply(_gini, raw=True)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume entropy (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dventropy63_21d_slope_v114_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)

    def _ent(a):
        a = a[a > 0]
        if len(a) == 0:
            return np.nan
        a = a / a.sum()
        return float(-(a * np.log(a)).sum())

    base = share.rolling(63, min_periods=30).apply(lambda a: _ent(a) if np.nansum(a) > 0 else np.nan, raw=True)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume trend tstat (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtrendt63_21d_slope_v115_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = (_mean(ldv, 21) - _mean(ldv, 63)) / _std(ldv, 63).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs price corr over a year (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvpxcorr252_63d_slope_v116_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    base = dvchg.rolling(252, min_periods=126).corr(ret)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume rp spread 63 vs 252 (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrpspr_21d_slope_v117_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = _rngpos(ldv, 63) - _rngpos(ldv, 252)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume downside quantile of change (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdownq63_21d_slope_v118_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    base = d.rolling(63, min_periods=21).quantile(0.05)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume gap-normalized level (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvgapnorm252_21d_slope_v119_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    gap = ldv - _mean(ldv, 252)
    base = (gap / _std(ldv, 63).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume mid-horizon momentum 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvmom126_21d_slope_v120_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    base = m - m.shift(126)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume up/down balance over 21d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupdown21_21d_slope_v121_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 63d/126d EMA displacement (5d ROC) — fast momentum velocity
def f17dv_f17_dollar_volume_dynamics_tierdist252_5d_slope_v122_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=126, min_periods=63).mean()
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 126d dispersion (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvz126_63d_slope_v123_signal(closeadj, volume):
    base = _std(_ldv(closeadj, volume), 126)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawup off 126d trough (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdrawup126_21d_slope_v124_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log((dv / dv.rolling(126, min_periods=63).min().replace(0, np.nan)).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume dry-up depth (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdrydepth63_21d_slope_v125_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    base = ((med - dv).clip(lower=0) / med.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike-count over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspikecnt252_21d_slope_v126_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    base = (dv > 3.0 * med).astype(float).rolling(252, min_periods=126).sum() \
        + (dv / med.replace(0, np.nan) - 3.0).clip(lower=0).rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs raw-volume momentum divergence (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvvolmomdiv63_21d_slope_v127_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    dm = _mean(ldv, 21) - _mean(ldv, 21).shift(63)
    vm = _mean(lv, 21) - _mean(lv, 21).shift(63)
    base = dm - vm
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume max-min log span over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_tierfloor504_63d_slope_v128_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(252, min_periods=126).max() - ldv.rolling(252, min_periods=126).min()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume dispersion trend (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdisptrend63_21d_slope_v129_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    d = _std(ldv, 63)
    base = d - d.shift(63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume new-504d-high frequency (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvnewhi504_63d_slope_v130_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    hi = ldv.rolling(504, min_periods=252).max()
    base = (ldv >= hi - 1e-9).astype(float).rolling(126, min_periods=63).mean() \
        + 0.25 * (ldv - hi).rolling(21, min_periods=10).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume deep-dry duration (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdeepdry252_63d_slope_v131_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd <= -0.50).astype(float).rolling(252, min_periods=126).mean() \
        + (-dd - 0.50).clip(lower=0).rolling(63, min_periods=21).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume skew 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvskew126_21d_slope_v132_signal(closeadj, volume):
    base = _dv(closeadj, volume).rolling(126, min_periods=63).skew()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume kurtosis 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_ldvkurt126_21d_slope_v133_signal(closeadj, volume):
    base = _ldv(closeadj, volume).rolling(126, min_periods=63).kurt()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawdown-vs-price-drawdown gap at 252d (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdd63_21d_slope_v134_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dvdd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    pxdd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    base = dvdd - pxdd
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume signmag over a year (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvsignmag252_63d_slope_v135_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    chg = m - m.shift(252)
    base = np.sign(chg) * (chg.abs() ** 0.5)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume wave amplitude over a year (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvwave252_63d_slope_v136_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    s = dv.rolling(21, min_periods=10).sum()
    base = np.log(s.replace(0, np.nan) / s.shift(252).replace(0, np.nan))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume regime-cross count (with amplitude) over a year (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvcross252_21d_slope_v137_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    med = ldv.rolling(252, min_periods=126).median()
    above = (ldv > med).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    base = entries.rolling(252, min_periods=126).sum() \
        + (ldv - med).abs().rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawup off 63d trough (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdrawup63_5d_slope_v138_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log((dv / dv.rolling(63, min_periods=21).min().replace(0, np.nan)).replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 504d underwater fraction (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtier504_63d_slope_v139_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(504, min_periods=252).max().replace(0, np.nan) - 1.0
    base = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume time-since-peak (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvdsh252_21d_slope_v140_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    base = dv.rolling(252, min_periods=126).apply(_dsh, raw=True)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 504d-mean to-mean ratio shorter (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtomean1260_21d_slope_v141_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = np.log(_mean(dv, 126).replace(0, np.nan) / _mean(dv, 1260).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 1260d rank (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrank1260_63d_slope_v142_signal(closeadj, volume):
    base = _rank(_ldv(closeadj, volume), 1260)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume drawdown frequency (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvddfreq252_21d_slope_v143_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(126, min_periods=63).max().replace(0, np.nan) - 1.0
    in_dd = (dd <= -0.40).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    base = entries.rolling(252, min_periods=126).sum() + dd.rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume up/down balance change (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvupdownchg63_21d_slope_v144_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    base = bal - bal.shift(63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume range-value z over 126d (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvrangeval126_21d_slope_v145_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    rangeval = (high - low).abs() * volume.abs()
    base = _z(np.log((dv / rangeval.replace(0, np.nan)).replace(0, np.nan)), 126)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 126d level (5d ROC)
def f17dv_f17_dollar_volume_dynamics_dvlevel126_5d_slope_v146_signal(closeadj, volume):
    base = _mean(_ldv(closeadj, volume), 126)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 21d spike persistence (1.5x band) (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtrenddist126_21d_slope_v147_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    base = (dv / avg.replace(0, np.nan) - 1.5).clip(lower=0).rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume floor-spread over 126d (63d ROC)
def f17dv_f17_dollar_volume_dynamics_dvfloorspr126_63d_slope_v148_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    base = ldv.rolling(126, min_periods=63).quantile(0.50) - ldv.rolling(126, min_periods=63).quantile(0.05)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume 252d underwater-deepdry fraction (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvtierdisp252_5d_slope_v149_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    base = (dd <= -0.40).astype(float).rolling(252, min_periods=126).mean() \
        + (-dd - 0.40).clip(lower=0).rolling(63, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume spike-recency (21d ROC)
def f17dv_f17_dollar_volume_dynamics_dvspikerecency_21d_slope_v150_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    spike = (dv > 3.0 * med).astype(float)

    def _recency(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    base = spike.rolling(126, min_periods=63).apply(_recency, raw=True)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_dvlevel21_5d_slope_v001_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel63_21d_slope_v002_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel252_63d_slope_v003_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel126_21d_slope_v004_signal,
    f17dv_f17_dollar_volume_dynamics_dvz63_21d_slope_v005_signal,
    f17dv_f17_dollar_volume_dynamics_dvz252_21d_slope_v006_signal,
    f17dv_f17_dollar_volume_dynamics_dvz126_21d_slope_v007_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank252_21d_slope_v008_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank504_63d_slope_v009_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos252_21d_slope_v010_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos504_63d_slope_v011_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd252_21d_slope_v012_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd126_21d_slope_v013_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd63_5d_slope_v014_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike21_5d_slope_v015_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike63_21d_slope_v016_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown63_21d_slope_v017_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown252_63d_slope_v018_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf63_21d_slope_v019_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf252_63d_slope_v020_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp63_21d_slope_v021_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp252_63d_slope_v022_signal,
    f17dv_f17_dollar_volume_dynamics_dvcv63_21d_slope_v023_signal,
    f17dv_f17_dollar_volume_dynamics_dvsize63_21d_slope_v024_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist252_21d_slope_v025_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor252_21d_slope_v026_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove21_21d_slope_v027_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop563_21d_slope_v028_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrenddist252_21d_slope_v029_signal,
    f17dv_f17_dollar_volume_dynamics_dvemadisp63_21d_slope_v030_signal,
    f17dv_f17_dollar_volume_dynamics_dvddur252_21d_slope_v031_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew63_21d_slope_v032_signal,
    f17dv_f17_dollar_volume_dynamics_ldvskew126_21d_slope_v033_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt63_21d_slope_v034_signal,
    f17dv_f17_dollar_volume_dynamics_dvcumratio_21d_slope_v035_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierdisp252_21d_slope_v036_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean252_21d_slope_v037_signal,
    f17dv_f17_dollar_volume_dynamics_dvupsemi63_21d_slope_v038_signal,
    f17dv_f17_dollar_volume_dynamics_dvdnsemi63_21d_slope_v039_signal,
    f17dv_f17_dollar_volume_dynamics_dvvspxdd252_21d_slope_v040_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel504_63d_slope_v041_signal,
    f17dv_f17_dollar_volume_dynamics_dvz504_63d_slope_v042_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank126_21d_slope_v043_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd504_63d_slope_v044_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike5_5d_slope_v045_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown21_5d_slope_v046_signal,
    f17dv_f17_dollar_volume_dynamics_dvvoldiv252_21d_slope_v047_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove252_63d_slope_v048_signal,
    f17dv_f17_dollar_volume_dynamics_dvcv126_21d_slope_v049_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_slope_v050_signal,
    f17dv_f17_dollar_volume_dynamics_dvchurn63_21d_slope_v051_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangeval21_21d_slope_v052_signal,
    f17dv_f17_dollar_volume_dynamics_dvtier252_21d_slope_v053_signal,
    f17dv_f17_dollar_volume_dynamics_dvsignmag63_21d_slope_v054_signal,
    f17dv_f17_dollar_volume_dynamics_dveffort63_21d_slope_v055_signal,
    f17dv_f17_dollar_volume_dynamics_dvperrisk63_21d_slope_v056_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr63_21d_slope_v057_signal,
    f17dv_f17_dollar_volume_dynamics_dvtailspr126_21d_slope_v058_signal,
    f17dv_f17_dollar_volume_dynamics_dvpxcorr63_21d_slope_v059_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxshare63_21d_slope_v060_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel21_21d_slope_v061_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel63_5d_slope_v062_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel252_21d_slope_v063_signal,
    f17dv_f17_dollar_volume_dynamics_dvz63_5d_slope_v064_signal,
    f17dv_f17_dollar_volume_dynamics_dvz252_63d_slope_v065_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank252_63d_slope_v066_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos252_63d_slope_v067_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd252_63d_slope_v068_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike21_21d_slope_v069_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike63_5d_slope_v070_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown63_5d_slope_v071_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf63_5d_slope_v072_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp63_5d_slope_v073_signal,
    f17dv_f17_dollar_volume_dynamics_dvsize252_63d_slope_v074_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist504_63d_slope_v075_signal,
    f17dv_f17_dollar_volume_dynamics_dvregime63_21d_slope_v076_signal,
    f17dv_f17_dollar_volume_dynamics_dvnewhi252_21d_slope_v077_signal,
    f17dv_f17_dollar_volume_dynamics_dvthinfrac63_21d_slope_v078_signal,
    f17dv_f17_dollar_volume_dynamics_dvwave63_21d_slope_v079_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr63_21d_slope_v080_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoptime252_21d_slope_v081_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup63_21d_slope_v082_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmed63_21d_slope_v083_signal,
    f17dv_f17_dollar_volume_dynamics_dvminmed63_21d_slope_v084_signal,
    f17dv_f17_dollar_volume_dynamics_dvolsslope63_21d_slope_v085_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove126_21d_slope_v086_signal,
    f17dv_f17_dollar_volume_dynamics_dvvolrankdiv252_21d_slope_v087_signal,
    f17dv_f17_dollar_volume_dynamics_dvemadisp252_63d_slope_v088_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr126_21d_slope_v089_signal,
    f17dv_f17_dollar_volume_dynamics_dvfloorspr126_21d_slope_v090_signal,
    f17dv_f17_dollar_volume_dynamics_dvupfrac63_21d_slope_v091_signal,
    f17dv_f17_dollar_volume_dynamics_dvsemiasym63_21d_slope_v092_signal,
    f17dv_f17_dollar_volume_dynamics_dvuwfrac252_63d_slope_v093_signal,
    f17dv_f17_dollar_volume_dynamics_dvperrisk21_5d_slope_v094_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierspr_21d_slope_v095_signal,
    f17dv_f17_dollar_volume_dynamics_dvchurnz252_63d_slope_v096_signal,
    f17dv_f17_dollar_volume_dynamics_dvhlratio21_21d_slope_v097_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierrange252_21d_slope_v098_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop1252_21d_slope_v099_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmin252_63d_slope_v100_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom63_5d_slope_v101_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom252_21d_slope_v102_signal,
    f17dv_f17_dollar_volume_dynamics_dvsidemean63_21d_slope_v103_signal,
    f17dv_f17_dollar_volume_dynamics_dvulcer252_21d_slope_v104_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikefreq63_21d_slope_v105_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean504_21d_slope_v106_signal,
    f17dv_f17_dollar_volume_dynamics_dvupsemi252_63d_slope_v107_signal,
    f17dv_f17_dollar_volume_dynamics_dvdispratio_21d_slope_v108_signal,
    f17dv_f17_dollar_volume_dynamics_dvchgac63_21d_slope_v109_signal,
    f17dv_f17_dollar_volume_dynamics_dveffortz252_63d_slope_v110_signal,
    f17dv_f17_dollar_volume_dynamics_dvlvl126_21d_slope_v111_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikepersist21_21d_slope_v112_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini252_63d_slope_v113_signal,
    f17dv_f17_dollar_volume_dynamics_dventropy63_21d_slope_v114_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendt63_21d_slope_v115_signal,
    f17dv_f17_dollar_volume_dynamics_dvpxcorr252_63d_slope_v116_signal,
    f17dv_f17_dollar_volume_dynamics_dvrpspr_21d_slope_v117_signal,
    f17dv_f17_dollar_volume_dynamics_dvdownq63_21d_slope_v118_signal,
    f17dv_f17_dollar_volume_dynamics_dvgapnorm252_21d_slope_v119_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom126_21d_slope_v120_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown21_21d_slope_v121_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist252_5d_slope_v122_signal,
    f17dv_f17_dollar_volume_dynamics_dvz126_63d_slope_v123_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup126_21d_slope_v124_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrydepth63_21d_slope_v125_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikecnt252_21d_slope_v126_signal,
    f17dv_f17_dollar_volume_dynamics_dvvolmomdiv63_21d_slope_v127_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor504_63d_slope_v128_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisptrend63_21d_slope_v129_signal,
    f17dv_f17_dollar_volume_dynamics_dvnewhi504_63d_slope_v130_signal,
    f17dv_f17_dollar_volume_dynamics_dvdeepdry252_63d_slope_v131_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew126_21d_slope_v132_signal,
    f17dv_f17_dollar_volume_dynamics_ldvkurt126_21d_slope_v133_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd63_21d_slope_v134_signal,
    f17dv_f17_dollar_volume_dynamics_dvsignmag252_63d_slope_v135_signal,
    f17dv_f17_dollar_volume_dynamics_dvwave252_63d_slope_v136_signal,
    f17dv_f17_dollar_volume_dynamics_dvcross252_21d_slope_v137_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup63_5d_slope_v138_signal,
    f17dv_f17_dollar_volume_dynamics_dvtier504_63d_slope_v139_signal,
    f17dv_f17_dollar_volume_dynamics_dvdsh252_21d_slope_v140_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean1260_21d_slope_v141_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank1260_63d_slope_v142_signal,
    f17dv_f17_dollar_volume_dynamics_dvddfreq252_21d_slope_v143_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdownchg63_21d_slope_v144_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangeval126_21d_slope_v145_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel126_5d_slope_v146_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrenddist126_21d_slope_v147_signal,
    f17dv_f17_dollar_volume_dynamics_dvfloorspr126_63d_slope_v148_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierdisp252_5d_slope_v149_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikerecency_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f17_dollar_volume_dynamics_2nd_derivatives_001_150_claude: %d features pass" % n_features)
