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
# jerk = second math derivative (discrete 2nd difference) of a dollar-volume base.
# jerk(k) = base - 2*base.shift(k) + base.shift(2k), with k matched to the base window.
# Each function expands its base inline; no factories / loops / exec.


# jerk of 21d log-dv level (k=5) — liquidity-level acceleration
def f17dv_f17_dollar_volume_dynamics_dvlevel21_5d_jerk_v001_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 21)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d log-dv level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvlevel63_21d_jerk_v002_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d log-dv level (k=63)
def f17dv_f17_dollar_volume_dynamics_dvlevel252_63d_jerk_v003_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 126d log-dv level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvlevel126_21d_jerk_v004_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 126)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d log-dv dispersion (k=21) — instability acceleration
def f17dv_f17_dollar_volume_dynamics_dvdisp63_21d_jerk_v005_signal(closeadj, volume):
    b = _std(_ldv(closeadj, volume), 63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d up/down dollar-volume balance (k=21) — directional-liquidity acceleration
def f17dv_f17_dollar_volume_dynamics_dvupdown63_21d_jerk_v006_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d log-dv kurtosis (k=21) — tail-shape acceleration
def f17dv_f17_dollar_volume_dynamics_dvkurt63_21d_jerk_v007_signal(closeadj, volume):
    b = _ldv(closeadj, volume).rolling(63, min_periods=21).kurt()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume rank (k=21) — tier-position acceleration
def f17dv_f17_dollar_volume_dynamics_dvrank252_21d_jerk_v008_signal(closeadj, volume):
    b = _rank(_ldv(closeadj, volume), 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 504d dollar-volume rank (k=63)
def f17dv_f17_dollar_volume_dynamics_dvrank504_63d_jerk_v009_signal(closeadj, volume):
    b = _rank(_ldv(closeadj, volume), 504)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike persistence (2x band) (k=5)
def f17dv_f17_dollar_volume_dynamics_dvspkpersist_5d_jerk_v010_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    b = (dv / avg.replace(0, np.nan) - 2.0).clip(lower=0).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume Herfindahl (k=21)
def f17dv_f17_dollar_volume_dynamics_dvherf252_21d_jerk_v011_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = (share ** 2).rolling(252, min_periods=126).sum()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume drawdown (k=21) — dry-up acceleration
def f17dv_f17_dollar_volume_dynamics_dvdd252_21d_jerk_v012_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 126d dollar-volume ulcer (drawdown RMS) (k=21)
def f17dv_f17_dollar_volume_dynamics_dvulcer126_21d_jerk_v013_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(126, min_periods=63).max().replace(0, np.nan) - 1.0
    b = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 21d dollar-volume spike ratio (k=5) — surge acceleration
def f17dv_f17_dollar_volume_dynamics_dvspike21_5d_jerk_v014_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(dv.replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dollar-volume spike ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspike63_21d_jerk_v015_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 5).replace(0, np.nan) / _mean(dv, 63).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d up/down dollar-volume balance (k=63)
def f17dv_f17_dollar_volume_dynamics_dvupdown252_63d_jerk_v016_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=126).sum()
    dn = dv.where(ret < 0, 0.0).rolling(252, min_periods=126).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dollar-volume Herfindahl (k=21) — concentration acceleration
def f17dv_f17_dollar_volume_dynamics_dvherf63_21d_jerk_v017_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (share ** 2).rolling(63, min_periods=21).sum()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume z (k=63)
def f17dv_f17_dollar_volume_dynamics_dvz252_63d_jerk_v018_signal(closeadj, volume):
    b = _z(_ldv(closeadj, volume), 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume drawdown duration (k=21)
def f17dv_f17_dollar_volume_dynamics_dvddur252_21d_jerk_v019_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    b = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dollar-volume skew (k=21)
def f17dv_f17_dollar_volume_dynamics_dvskew63_21d_jerk_v020_signal(closeadj, volume):
    b = _dv(closeadj, volume).rolling(63, min_periods=21).skew()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs price-size proxy (k=21) — turnover-of-value acceleration
def f17dv_f17_dollar_volume_dynamics_dvsize63_21d_jerk_v021_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lp = np.log(closeadj.replace(0, np.nan))
    b = _mean(ldv - lp, 63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume per-move depth (k=21) — depth-of-market acceleration
def f17dv_f17_dollar_volume_dynamics_dvpermove21_21d_jerk_v022_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    b = _mean(np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan)), 21)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dollar-volume top5 share (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtop563_21d_jerk_v023_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    tot = dv.rolling(63, min_periods=21).sum()
    top5 = dv.rolling(63, min_periods=21).apply(lambda a: np.sort(a)[-5:].sum(), raw=True)
    b = top5 / tot.replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d/126d EMA displacement (k=21) — momentum acceleration
def f17dv_f17_dollar_volume_dynamics_dvemadisp63_21d_jerk_v024_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dollar-volume CV (k=21)
def f17dv_f17_dollar_volume_dynamics_dvcv63_21d_jerk_v025_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = _std(dv, 63) / _mean(dv, 63).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 63d IQR (k=21)
def f17dv_f17_dollar_volume_dynamics_dviqr63_21d_jerk_v026_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(63, min_periods=21).quantile(0.75) - ldv.rolling(63, min_periods=21).quantile(0.25)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max/median spike ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmaxmed63_21d_jerk_v027_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    md = dv.rolling(63, min_periods=21).median()
    b = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume min/median ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvminmed63_21d_jerk_v028_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mn = dv.rolling(63, min_periods=21).min()
    md = dv.rolling(63, min_periods=21).median()
    b = np.log(mn.replace(0, np.nan) / md.replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawdown-vs-price-drawdown gap (k=21)
def f17dv_f17_dollar_volume_dynamics_dvvspxdd252_21d_jerk_v029_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dvdd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    pxdd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    b = dvdd - pxdd
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume to-252d-mean ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtomean252_21d_jerk_v030_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 252).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume upside semi-dispersion 63d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvupsemi63_21d_jerk_v031_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    up = (ldv - _mean(ldv, 63)).clip(lower=0)
    b = (up ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume downside semi-dispersion 63d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdnsemi63_21d_jerk_v032_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    dn = (_mean(ldv, 63) - ldv).clip(lower=0)
    b = (dn ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 126d log-dv skew (k=21)
def f17dv_f17_dollar_volume_dynamics_ldvskew126_21d_jerk_v033_signal(closeadj, volume):
    b = _ldv(closeadj, volume).rolling(126, min_periods=63).skew()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume cumulative quarter/year ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvcumratio_21d_jerk_v034_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    q = dv.rolling(63, min_periods=21).sum()
    y = dv.rolling(252, min_periods=126).sum()
    b = (q * 4.0) / y.replace(0, np.nan) - 1.0
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume tier-position instability std (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtierdisp252_21d_jerk_v035_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    b = rp.rolling(63, min_periods=21).std()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume effort-to-result (k=21)
def f17dv_f17_dollar_volume_dynamics_dveffort63_21d_jerk_v036_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    cumdv = dv.rolling(63, min_periods=21).sum()
    move = (closeadj / closeadj.shift(63) - 1.0).abs()
    b = np.log(cumdv.replace(0, np.nan)) - np.log((move * 100.0).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max-day share over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmaxshare63_21d_jerk_v037_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = dv.rolling(252, min_periods=126).sum()
    b = (mx * 63.0) / tot.replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume tail spread (95-50 pct) (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtailspr126_21d_jerk_v038_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(126, min_periods=63).quantile(0.95) - ldv.rolling(126, min_periods=63).quantile(0.50)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs price co-movement (k=21)
def f17dv_f17_dollar_volume_dynamics_dvpxcorr63_21d_jerk_v039_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    b = dvchg.rolling(63, min_periods=30).corr(ret)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume sign x magnitude momentum (k=21)
def f17dv_f17_dollar_volume_dynamics_dvsignmag63_21d_jerk_v040_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    chg = m - m.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 504d log-dv level (k=63)
def f17dv_f17_dollar_volume_dynamics_dvlevel504_63d_jerk_v041_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 504)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs price co-movement over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvpxcorr252_21d_jerk_v042_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    b = dvchg.rolling(252, min_periods=126).corr(ret)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume tier spread (63d vs 252d rank) (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtierspr_21d_jerk_v043_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = _rank(ldv, 63) - _rank(ldv, 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 504d dollar-volume drawdown (k=63)
def f17dv_f17_dollar_volume_dynamics_dvdd504_63d_jerk_v044_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = dv / dv.rolling(504, min_periods=252).max().replace(0, np.nan) - 1.0
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 5d dollar-volume spike (k=5)
def f17dv_f17_dollar_volume_dynamics_dvspike5_5d_jerk_v045_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 5).replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 21d up/down dollar-volume balance (k=5)
def f17dv_f17_dollar_volume_dynamics_dvupdown21_5d_jerk_v046_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs raw-volume z divergence (k=21)
def f17dv_f17_dollar_volume_dynamics_dvvoldiv252_21d_jerk_v047_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    b = _z(ldv, 252) - _z(lv, 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume per-move depth z over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dvpermove252_63d_jerk_v048_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    b = _z(np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan)), 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 126d dollar-volume CV (k=21)
def f17dv_f17_dollar_volume_dynamics_dvcv126_21d_jerk_v049_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 63d-mean to 504d-mean ratio (k=63)
def f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_jerk_v050_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 63).replace(0, np.nan) / _mean(dv, 504).replace(0, np.nan))
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of intraday-range dollar churn level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvchurn63_21d_jerk_v051_signal(closeadj, volume, high, low):
    rangefrac = (high - low).abs() / closeadj.replace(0, np.nan)
    b = _mean(np.log(rangefrac.replace(0, np.nan)), 63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs intraday-range value ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvrangeval21_21d_jerk_v052_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    rangeval = (high - low).abs() * volume.abs()
    b = _mean(np.log((dv / rangeval.replace(0, np.nan)).replace(0, np.nan)), 21)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume Gini concentration over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvgini252_21d_jerk_v053_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _gini(a):
        a = np.sort(a)
        m = len(a)
        s = a.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, m + 1)
        return float((2.0 * np.dot(idx, a) / (m * s)) - (m + 1.0) / m)

    b = dv.rolling(252, min_periods=126).apply(_gini, raw=True)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume per-risk level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvperrisk63_21d_jerk_v054_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = _mean(ldv, 21) - np.log(vol.replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume entropy of daily shares (k=21)
def f17dv_f17_dollar_volume_dynamics_dventropy63_21d_jerk_v055_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)

    def _ent(a):
        a = a[a > 0]
        if len(a) == 0:
            return np.nan
        a = a / a.sum()
        return float(-(a * np.log(a)).sum())

    b = share.rolling(63, min_periods=30).apply(lambda a: _ent(a) if np.nansum(a) > 0 else np.nan, raw=True)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume floor spread (50-5 pct) (k=21)
def f17dv_f17_dollar_volume_dynamics_dvfloorspr126_21d_jerk_v056_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(126, min_periods=63).quantile(0.50) - ldv.rolling(126, min_periods=63).quantile(0.05)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume trend tstat (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtrendt63_21d_jerk_v057_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = (_mean(ldv, 21) - _mean(ldv, 63)) / _std(ldv, 63).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume downside quantile of change (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdownq63_21d_jerk_v058_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    b = d.rolling(63, min_periods=21).quantile(0.05)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume dispersion ratio short/long (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdispratio_21d_jerk_v059_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = _std(ldv, 21) / _std(ldv, 126).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume change-autocorrelation (k=21)
def f17dv_f17_dollar_volume_dynamics_dvchgac63_21d_jerk_v060_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    b = d.rolling(63, min_periods=30).apply(lambda a: pd.Series(a).autocorr(lag=1), raw=False)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume up-day fraction momentum (k=5)
def f17dv_f17_dollar_volume_dynamics_dvupfrac63_5d_jerk_v061_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = (ldv.diff() > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5 \
        + 5.0 * ldv.diff().rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d log-dv level (k=5)
def f17dv_f17_dollar_volume_dynamics_dvlevel63_5d_jerk_v062_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 63)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d log-dv level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvlevel252_21d_jerk_v063_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 126d log-dv kurtosis (k=63)
def f17dv_f17_dollar_volume_dynamics_ldvkurt126_63d_jerk_v064_signal(closeadj, volume):
    b = _ldv(closeadj, volume).rolling(126, min_periods=63).kurt()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 252d dollar-volume z (k=21)
def f17dv_f17_dollar_volume_dynamics_dvz252_21d_jerk_v065_signal(closeadj, volume):
    b = _z(_ldv(closeadj, volume), 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 252d skewness (k=63)
def f17dv_f17_dollar_volume_dynamics_dvskew252_63d_jerk_v066_signal(closeadj, volume):
    b = _dv(closeadj, volume).rolling(252, min_periods=126).skew()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 63d Herfindahl (k=63)
def f17dv_f17_dollar_volume_dynamics_dvherf63_63d_jerk_v067_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (share ** 2).rolling(63, min_periods=21).sum()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawup off 252d trough (k=63)
def f17dv_f17_dollar_volume_dynamics_dvdrawup252_63d_jerk_v068_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log((dv / dv.rolling(252, min_periods=126).min().replace(0, np.nan)).replace(0, np.nan))
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike tail kurtosis (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspktailk_21d_jerk_v069_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    sp = np.log(dv.replace(0, np.nan) / _mean(dv, 21).replace(0, np.nan))
    b = sp.rolling(63, min_periods=21).kurt()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max/median ratio (k=5)
def f17dv_f17_dollar_volume_dynamics_dvmaxmed63_5d_jerk_v070_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    md = dv.rolling(63, min_periods=21).median()
    b = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d up/down balance (k=5)
def f17dv_f17_dollar_volume_dynamics_dvupdown63_5d_jerk_v071_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d Herfindahl (k=5)
def f17dv_f17_dollar_volume_dynamics_dvherf63_5d_jerk_v072_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (share ** 2).rolling(63, min_periods=21).sum()
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of 63d dispersion (k=5)
def f17dv_f17_dollar_volume_dynamics_dvdisp63_5d_jerk_v073_signal(closeadj, volume):
    b = _std(_ldv(closeadj, volume), 63)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs raw-volume rank divergence (k=63)
def f17dv_f17_dollar_volume_dynamics_dvvolrankdiv252_63d_jerk_v074_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    b = _rank(ldv, 252) - _rank(lv, 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 252d ulcer (drawdown RMS) (k=63)
def f17dv_f17_dollar_volume_dynamics_dvulcer252_63d_jerk_v075_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    b = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume regime fraction-above-median (k=21)
def f17dv_f17_dollar_volume_dynamics_dvregime63_21d_jerk_v076_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    med = ldv.rolling(252, min_periods=126).median()
    b = (ldv > med).astype(float).rolling(63, min_periods=21).mean() - 0.5
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume new-252d-high frequency (k=21)
def f17dv_f17_dollar_volume_dynamics_dvnewhi252_21d_jerk_v077_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    hi = ldv.rolling(252, min_periods=126).max()
    b = (ldv >= hi - 1e-9).astype(float).rolling(63, min_periods=21).mean() \
        + 0.25 * (ldv - hi).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume thin-fraction (k=21)
def f17dv_f17_dollar_volume_dynamics_dvthinfrac63_21d_jerk_v078_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(252, min_periods=126).median()
    b = (dv < med * 0.25).astype(float).rolling(63, min_periods=21).mean() \
        + ((med * 0.25 - dv).clip(lower=0) / med.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume wave amplitude (k=21)
def f17dv_f17_dollar_volume_dynamics_dvwave63_21d_jerk_v079_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    s = dv.rolling(21, min_periods=10).sum()
    b = np.log(s.replace(0, np.nan) / s.shift(63).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume raw-level autocorrelation (k=21)
def f17dv_f17_dollar_volume_dynamics_dvautocorr63_21d_jerk_v080_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(63, min_periods=30).apply(lambda a: pd.Series(a).autocorr(lag=1), raw=False)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume top-tercile time (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtoptime252_21d_jerk_v081_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    b = (rp >= 0.6667).astype(float).rolling(63, min_periods=21).mean() \
        + 3.0 * (rp - 0.6667).clip(lower=0).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawup off 63d trough (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdrawup63_21d_jerk_v082_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log((dv / dv.rolling(63, min_periods=21).min().replace(0, np.nan)).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max/median ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmaxmed63b_21d_jerk_v083_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(126, min_periods=63).max()
    md = dv.rolling(126, min_periods=63).median()
    b = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume OLS 63d trend slope (k=21) — trend curvature
def f17dv_f17_dollar_volume_dynamics_dvolsslope63_21d_jerk_v084_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)

    def _sl(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        den = (xc ** 2).sum()
        if den <= 0:
            return np.nan
        return float(np.dot(a - a.mean(), xc) / den)

    b = ldv.rolling(63, min_periods=40).apply(_sl, raw=True)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume per-move depth over 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvpermove126_21d_jerk_v085_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    absret = closeadj.pct_change().abs()
    ratio = np.log((dv / (absret.replace(0, np.nan) * 100.0)).replace(0, np.nan))
    b = _mean(ratio, 63) - _mean(ratio, 126)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 504d EMA crossover (k=63)
def f17dv_f17_dollar_volume_dynamics_dvemadisp252_63d_jerk_v086_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.ewm(span=63, min_periods=21).mean() - ldv.ewm(span=252, min_periods=126).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume IQR over 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_dviqr126_21d_jerk_v087_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(126, min_periods=63).quantile(0.75) - ldv.rolling(126, min_periods=63).quantile(0.25)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume semi-dispersion asymmetry (k=21)
def f17dv_f17_dollar_volume_dynamics_dvsemiasym63_21d_jerk_v088_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    us = ((ldv - m).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    ds = ((m - ldv).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    b = (us - ds) / (us + ds).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 252d underwater fraction (k=63)
def f17dv_f17_dollar_volume_dynamics_dvuwfrac252_63d_jerk_v089_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    b = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume churn z (k=63)
def f17dv_f17_dollar_volume_dynamics_dvchurnz252_63d_jerk_v090_signal(closeadj, volume, high, low):
    churn = (high - low).abs() / closeadj.replace(0, np.nan) * _dv(closeadj, volume)
    b = _z(np.log(churn.replace(0, np.nan)), 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs high-low value ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvhlratio21_21d_jerk_v091_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    hlval = ((high + low) / 2.0).abs() * volume.abs()
    b = _mean(np.log((dv / hlval.replace(0, np.nan)).replace(0, np.nan)), 21)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume tier range / mobility (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtierrange252_21d_jerk_v092_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    b = rp.rolling(126, min_periods=63).max() - rp.rolling(126, min_periods=63).min()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume top1 share over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtop1252_21d_jerk_v093_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    mx = dv.rolling(252, min_periods=126).max()
    tot = dv.rolling(252, min_periods=126).sum()
    b = (mx * 252.0) / tot.replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max-min log span (k=63)
def f17dv_f17_dollar_volume_dynamics_dvmaxmin252_63d_jerk_v094_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(252, min_periods=126).max() - ldv.rolling(252, min_periods=126).min()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume momentum 63d (k=5)
def f17dv_f17_dollar_volume_dynamics_dvmom63_5d_jerk_v095_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    b = m - m.shift(63)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume momentum 252d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmom252_21d_jerk_v096_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    b = m - m.shift(252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike-frequency (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspikefreq63_21d_jerk_v097_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    b = (dv > 2.0 * med).astype(float).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume to-mean ratio over 504d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtomean504_21d_jerk_v098_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 63).replace(0, np.nan) / _mean(dv, 504).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume effort-z over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dveffortz252_63d_jerk_v099_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    cumdv = dv.rolling(21, min_periods=10).sum()
    move = (closeadj / closeadj.shift(21) - 1.0).abs()
    b = _z(np.log(cumdv.replace(0, np.nan)) - np.log((move * 100.0).replace(0, np.nan)), 252)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 126d dispersion (k=63)
def f17dv_f17_dollar_volume_dynamics_dvdisp126_63d_jerk_v100_signal(closeadj, volume):
    b = _std(_ldv(closeadj, volume), 126)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike persistence (1.5x band) (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspkpersist15_21d_jerk_v101_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    b = (dv / avg.replace(0, np.nan) - 1.5).clip(lower=0).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume Gini concentration (k=63)
def f17dv_f17_dollar_volume_dynamics_dvgini126_63d_jerk_v102_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _gini(a):
        a = np.sort(a)
        m = len(a)
        s = a.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, m + 1)
        return float((2.0 * np.dot(idx, a) / (m * s)) - (m + 1.0) / m)

    b = dv.rolling(126, min_periods=63).apply(_gini, raw=True)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume top-tercile time (k=63)
def f17dv_f17_dollar_volume_dynamics_dvtoptime252_63d_jerk_v103_signal(closeadj, volume):
    rp = _rngpos(_ldv(closeadj, volume), 252)
    b = (rp >= 0.6667).astype(float).rolling(63, min_periods=21).mean() \
        + 3.0 * (rp - 0.6667).clip(lower=0).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawdown-vs-price-drawdown gap 252d (k=63)
def f17dv_f17_dollar_volume_dynamics_dvvspxdd252_63d_jerk_v104_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dvdd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    pxdd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    b = dvdd - pxdd
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike magnitude excess (k=21) — continuous surge-excess curvature
def f17dv_f17_dollar_volume_dynamics_dvspikefreq63_5d_jerk_v105_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    b = (dv / med.replace(0, np.nan) - 2.0).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume wave amplitude (k=21) — liquidity-wave curvature
def f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_jerk_v106_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    s = dv.rolling(21, min_periods=10).sum()
    b = np.log(s.replace(0, np.nan) / s.shift(126).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume semi-asymmetry 63d (k=63)
def f17dv_f17_dollar_volume_dynamics_dvsemiasym63_63d_jerk_v107_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    us = ((ldv - m).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    ds = ((m - ldv).clip(lower=0) ** 2).rolling(63, min_periods=21).mean() ** 0.5
    b = (us - ds) / (us + ds).replace(0, np.nan)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume dispersion trend (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdisptrend63_21d_jerk_v108_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    d = _std(ldv, 63)
    b = d - d.shift(63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume change-autocorrelation (k=5)
def f17dv_f17_dollar_volume_dynamics_dvchgac63_5d_jerk_v109_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    b = d.rolling(63, min_periods=30).apply(lambda a: pd.Series(a).autocorr(lag=1), raw=False)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume up/down balance over 21d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvupdown21_21d_jerk_v110_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 126d CV (k=63)
def f17dv_f17_dollar_volume_dynamics_dvcv126_63d_jerk_v111_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike persistence (2x band) over a quarter (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspkpersist2q_21d_jerk_v112_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    avg = _mean(dv, 21)
    b = (dv / avg.replace(0, np.nan) - 2.0).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume Gini concentration over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dvgini252_63d_jerk_v113_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _gini(a):
        a = np.sort(a)
        m = len(a)
        s = a.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, m + 1)
        return float((2.0 * np.dot(idx, a) / (m * s)) - (m + 1.0) / m)

    b = dv.rolling(252, min_periods=126).apply(_gini, raw=True)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume entropy (k=5)
def f17dv_f17_dollar_volume_dynamics_dventropy63_5d_jerk_v114_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    share = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)

    def _ent(a):
        a = a[a > 0]
        if len(a) == 0:
            return np.nan
        a = a / a.sum()
        return float(-(a * np.log(a)).sum())

    b = share.rolling(63, min_periods=30).apply(lambda a: _ent(a) if np.nansum(a) > 0 else np.nan, raw=True)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume trend tstat (k=5)
def f17dv_f17_dollar_volume_dynamics_dvtrendt63_5d_jerk_v115_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = (_mean(ldv, 21) - _mean(ldv, 63)) / _std(ldv, 63).replace(0, np.nan)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs price corr over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dvpxcorr252_63d_jerk_v116_signal(closeadj, volume):
    dvchg = _ldv(closeadj, volume).diff()
    ret = closeadj.pct_change()
    b = dvchg.rolling(252, min_periods=126).corr(ret)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume rp spread 63 vs 252 (k=21)
def f17dv_f17_dollar_volume_dynamics_dvrpspr_21d_jerk_v117_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = _rngpos(ldv, 63) - _rngpos(ldv, 252)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume downside quantile of change (k=5)
def f17dv_f17_dollar_volume_dynamics_dvdownq63_5d_jerk_v118_signal(closeadj, volume):
    d = _ldv(closeadj, volume).diff()
    b = d.rolling(63, min_periods=21).quantile(0.05)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume gap-normalized level (k=21)
def f17dv_f17_dollar_volume_dynamics_dvgapnorm252_21d_jerk_v119_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    gap = ldv - _mean(ldv, 252)
    b = (gap / _std(ldv, 63).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume mid-horizon momentum 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmom126_21d_jerk_v120_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 21)
    b = m - m.shift(126)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume up/down balance over 63d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvupdown63b_21d_jerk_v121_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 63d/126d EMA displacement (k=5)
def f17dv_f17_dollar_volume_dynamics_dvemadisp126_5d_jerk_v122_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=126, min_periods=63).mean()
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 126d dispersion (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdisp126_21d_jerk_v123_signal(closeadj, volume):
    b = _std(_ldv(closeadj, volume), 126)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawup off 126d trough (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdrawup126_21d_jerk_v124_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log((dv / dv.rolling(126, min_periods=63).min().replace(0, np.nan)).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume dry-up depth (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdrydepth63_21d_jerk_v125_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    b = ((med - dv).clip(lower=0) / med.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike-count over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspikecnt252_21d_jerk_v126_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    b = (dv > 3.0 * med).astype(float).rolling(252, min_periods=126).sum() \
        + (dv / med.replace(0, np.nan) - 3.0).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs raw-volume momentum divergence (k=21)
def f17dv_f17_dollar_volume_dynamics_dvvolmomdiv63_21d_jerk_v127_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    dm = _mean(ldv, 21) - _mean(ldv, 21).shift(63)
    vm = _mean(lv, 21) - _mean(lv, 21).shift(63)
    b = dm - vm
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume max-min log span (k=21)
def f17dv_f17_dollar_volume_dynamics_dvmaxmin252_21d_jerk_v128_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(252, min_periods=126).max() - ldv.rolling(252, min_periods=126).min()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume dispersion trend (k=5)
def f17dv_f17_dollar_volume_dynamics_dvdisptrend63_5d_jerk_v129_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    d = _std(ldv, 63)
    b = d - d.shift(63)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume new-504d-high frequency (k=63)
def f17dv_f17_dollar_volume_dynamics_dvnewhi504_63d_jerk_v130_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    hi = ldv.rolling(504, min_periods=252).max()
    b = (ldv >= hi - 1e-9).astype(float).rolling(126, min_periods=63).mean() \
        + 0.25 * (ldv - hi).rolling(21, min_periods=10).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume deep-dry duration (k=63)
def f17dv_f17_dollar_volume_dynamics_dvdeepdry252_63d_jerk_v131_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    b = (dd <= -0.50).astype(float).rolling(252, min_periods=126).mean() \
        + (-dd - 0.50).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume skew 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvskew126_21d_jerk_v132_signal(closeadj, volume):
    b = _dv(closeadj, volume).rolling(126, min_periods=63).skew()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume kurtosis 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_ldvkurt126_21d_jerk_v133_signal(closeadj, volume):
    b = _ldv(closeadj, volume).rolling(126, min_periods=63).kurt()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume vs raw-volume momentum divergence (k=63)
def f17dv_f17_dollar_volume_dynamics_dvvspxdd252b_21d_jerk_v134_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    lv = np.log(volume.abs().replace(0, np.nan))
    dm = _mean(ldv, 21) - _mean(ldv, 21).shift(63)
    vm = _mean(lv, 21) - _mean(lv, 21).shift(63)
    b = dm - vm
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume signmag over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dvsignmag252_63d_jerk_v135_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    m = _mean(ldv, 63)
    chg = m - m.shift(252)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume wave amplitude over a year (k=63)
def f17dv_f17_dollar_volume_dynamics_dvwave252_63d_jerk_v136_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    s = dv.rolling(21, min_periods=10).sum()
    b = np.log(s.replace(0, np.nan) / s.shift(252).replace(0, np.nan))
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume regime-cross count over a year (k=21)
def f17dv_f17_dollar_volume_dynamics_dvcross252_21d_jerk_v137_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    med = ldv.rolling(252, min_periods=126).median()
    above = (ldv > med).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + (ldv - med).abs().rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 21d drawup off trough (k=5) — fast revival curvature
def f17dv_f17_dollar_volume_dynamics_dvdrawup63_5d_jerk_v138_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log((dv / dv.rolling(21, min_periods=10).min().replace(0, np.nan)).replace(0, np.nan))
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 504d underwater fraction (k=63)
def f17dv_f17_dollar_volume_dynamics_dvuwfrac504_63d_jerk_v139_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(504, min_periods=252).max().replace(0, np.nan) - 1.0
    b = (dd <= -0.30).astype(float).rolling(252, min_periods=126).mean()
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume time-since-peak (k=21)
def f17dv_f17_dollar_volume_dynamics_dvdsh252_21d_jerk_v140_signal(closeadj, volume):
    dv = _dv(closeadj, volume)

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = dv.rolling(252, min_periods=126).apply(_dsh, raw=True)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 126d-mean to 1260d-mean ratio (k=21)
def f17dv_f17_dollar_volume_dynamics_dvtomean1260_21d_jerk_v141_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    b = np.log(_mean(dv, 126).replace(0, np.nan) / _mean(dv, 1260).replace(0, np.nan))
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 1260d rank (k=63)
def f17dv_f17_dollar_volume_dynamics_dvrank1260_63d_jerk_v142_signal(closeadj, volume):
    b = _rank(_ldv(closeadj, volume), 1260)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume drawdown frequency (k=21)
def f17dv_f17_dollar_volume_dynamics_dvddfreq252_21d_jerk_v143_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(126, min_periods=63).max().replace(0, np.nan) - 1.0
    in_dd = (dd <= -0.40).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + dd.rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume up/down balance change (k=21)
def f17dv_f17_dollar_volume_dynamics_dvupdownchg63_21d_jerk_v144_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume range-value z over 126d (k=21)
def f17dv_f17_dollar_volume_dynamics_dvrangeval126_21d_jerk_v145_signal(closeadj, volume, high, low):
    dv = _dv(closeadj, volume)
    rangeval = (high - low).abs() * volume.abs()
    b = _z(np.log((dv / rangeval.replace(0, np.nan)).replace(0, np.nan)), 126)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 126d level (k=5)
def f17dv_f17_dollar_volume_dynamics_dvlevel126_5d_jerk_v146_signal(closeadj, volume):
    b = _mean(_ldv(closeadj, volume), 126)
    result = b - 2.0 * b.shift(5) + b.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume IQR over 126d (k=63) — robust-dispersion curvature
def f17dv_f17_dollar_volume_dynamics_dvtrenddist126_21d_jerk_v147_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(126, min_periods=63).quantile(0.75) - ldv.rolling(126, min_periods=63).quantile(0.25)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume floor-spread over 126d (k=63)
def f17dv_f17_dollar_volume_dynamics_dvfloorspr126_63d_jerk_v148_signal(closeadj, volume):
    ldv = _ldv(closeadj, volume)
    b = ldv.rolling(126, min_periods=63).quantile(0.50) - ldv.rolling(126, min_periods=63).quantile(0.05)
    result = b - 2.0 * b.shift(63) + b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume 252d underwater (40% threshold) fraction (k=21)
def f17dv_f17_dollar_volume_dynamics_dvuw40frac252_21d_jerk_v149_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    dd = dv / dv.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    b = (dd <= -0.40).astype(float).rolling(252, min_periods=126).mean() \
        + (-dd - 0.40).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dollar-volume spike-recency (k=21)
def f17dv_f17_dollar_volume_dynamics_dvspikerecency_21d_jerk_v150_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    spike = (dv > 3.0 * med).astype(float)

    def _recency(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    b = spike.rolling(126, min_periods=63).apply(_recency, raw=True)
    result = b - 2.0 * b.shift(21) + b.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_dvlevel21_5d_jerk_v001_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel63_21d_jerk_v002_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel252_63d_jerk_v003_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel126_21d_jerk_v004_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp63_21d_jerk_v005_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown63_21d_jerk_v006_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt63_21d_jerk_v007_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank252_21d_jerk_v008_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank504_63d_jerk_v009_signal,
    f17dv_f17_dollar_volume_dynamics_dvspkpersist_5d_jerk_v010_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf252_21d_jerk_v011_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd252_21d_jerk_v012_signal,
    f17dv_f17_dollar_volume_dynamics_dvulcer126_21d_jerk_v013_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike21_5d_jerk_v014_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike63_21d_jerk_v015_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown252_63d_jerk_v016_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf63_21d_jerk_v017_signal,
    f17dv_f17_dollar_volume_dynamics_dvz252_63d_jerk_v018_signal,
    f17dv_f17_dollar_volume_dynamics_dvddur252_21d_jerk_v019_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew63_21d_jerk_v020_signal,
    f17dv_f17_dollar_volume_dynamics_dvsize63_21d_jerk_v021_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove21_21d_jerk_v022_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop563_21d_jerk_v023_signal,
    f17dv_f17_dollar_volume_dynamics_dvemadisp63_21d_jerk_v024_signal,
    f17dv_f17_dollar_volume_dynamics_dvcv63_21d_jerk_v025_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr63_21d_jerk_v026_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmed63_21d_jerk_v027_signal,
    f17dv_f17_dollar_volume_dynamics_dvminmed63_21d_jerk_v028_signal,
    f17dv_f17_dollar_volume_dynamics_dvvspxdd252_21d_jerk_v029_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean252_21d_jerk_v030_signal,
    f17dv_f17_dollar_volume_dynamics_dvupsemi63_21d_jerk_v031_signal,
    f17dv_f17_dollar_volume_dynamics_dvdnsemi63_21d_jerk_v032_signal,
    f17dv_f17_dollar_volume_dynamics_ldvskew126_21d_jerk_v033_signal,
    f17dv_f17_dollar_volume_dynamics_dvcumratio_21d_jerk_v034_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierdisp252_21d_jerk_v035_signal,
    f17dv_f17_dollar_volume_dynamics_dveffort63_21d_jerk_v036_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxshare63_21d_jerk_v037_signal,
    f17dv_f17_dollar_volume_dynamics_dvtailspr126_21d_jerk_v038_signal,
    f17dv_f17_dollar_volume_dynamics_dvpxcorr63_21d_jerk_v039_signal,
    f17dv_f17_dollar_volume_dynamics_dvsignmag63_21d_jerk_v040_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel504_63d_jerk_v041_signal,
    f17dv_f17_dollar_volume_dynamics_dvpxcorr252_21d_jerk_v042_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierspr_21d_jerk_v043_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd504_63d_jerk_v044_signal,
    f17dv_f17_dollar_volume_dynamics_dvspike5_5d_jerk_v045_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown21_5d_jerk_v046_signal,
    f17dv_f17_dollar_volume_dynamics_dvvoldiv252_21d_jerk_v047_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove252_63d_jerk_v048_signal,
    f17dv_f17_dollar_volume_dynamics_dvcv126_21d_jerk_v049_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_jerk_v050_signal,
    f17dv_f17_dollar_volume_dynamics_dvchurn63_21d_jerk_v051_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangeval21_21d_jerk_v052_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini252_21d_jerk_v053_signal,
    f17dv_f17_dollar_volume_dynamics_dvperrisk63_21d_jerk_v054_signal,
    f17dv_f17_dollar_volume_dynamics_dventropy63_21d_jerk_v055_signal,
    f17dv_f17_dollar_volume_dynamics_dvfloorspr126_21d_jerk_v056_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendt63_21d_jerk_v057_signal,
    f17dv_f17_dollar_volume_dynamics_dvdownq63_21d_jerk_v058_signal,
    f17dv_f17_dollar_volume_dynamics_dvdispratio_21d_jerk_v059_signal,
    f17dv_f17_dollar_volume_dynamics_dvchgac63_21d_jerk_v060_signal,
    f17dv_f17_dollar_volume_dynamics_dvupfrac63_5d_jerk_v061_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel63_5d_jerk_v062_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel252_21d_jerk_v063_signal,
    f17dv_f17_dollar_volume_dynamics_ldvkurt126_63d_jerk_v064_signal,
    f17dv_f17_dollar_volume_dynamics_dvz252_21d_jerk_v065_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew252_63d_jerk_v066_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf63_63d_jerk_v067_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup252_63d_jerk_v068_signal,
    f17dv_f17_dollar_volume_dynamics_dvspktailk_21d_jerk_v069_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmed63_5d_jerk_v070_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown63_5d_jerk_v071_signal,
    f17dv_f17_dollar_volume_dynamics_dvherf63_5d_jerk_v072_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp63_5d_jerk_v073_signal,
    f17dv_f17_dollar_volume_dynamics_dvvolrankdiv252_63d_jerk_v074_signal,
    f17dv_f17_dollar_volume_dynamics_dvulcer252_63d_jerk_v075_signal,
    f17dv_f17_dollar_volume_dynamics_dvregime63_21d_jerk_v076_signal,
    f17dv_f17_dollar_volume_dynamics_dvnewhi252_21d_jerk_v077_signal,
    f17dv_f17_dollar_volume_dynamics_dvthinfrac63_21d_jerk_v078_signal,
    f17dv_f17_dollar_volume_dynamics_dvwave63_21d_jerk_v079_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr63_21d_jerk_v080_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoptime252_21d_jerk_v081_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup63_21d_jerk_v082_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmed63b_21d_jerk_v083_signal,
    f17dv_f17_dollar_volume_dynamics_dvolsslope63_21d_jerk_v084_signal,
    f17dv_f17_dollar_volume_dynamics_dvpermove126_21d_jerk_v085_signal,
    f17dv_f17_dollar_volume_dynamics_dvemadisp252_63d_jerk_v086_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr126_21d_jerk_v087_signal,
    f17dv_f17_dollar_volume_dynamics_dvsemiasym63_21d_jerk_v088_signal,
    f17dv_f17_dollar_volume_dynamics_dvuwfrac252_63d_jerk_v089_signal,
    f17dv_f17_dollar_volume_dynamics_dvchurnz252_63d_jerk_v090_signal,
    f17dv_f17_dollar_volume_dynamics_dvhlratio21_21d_jerk_v091_signal,
    f17dv_f17_dollar_volume_dynamics_dvtierrange252_21d_jerk_v092_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop1252_21d_jerk_v093_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmin252_63d_jerk_v094_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom63_5d_jerk_v095_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom252_21d_jerk_v096_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikefreq63_21d_jerk_v097_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean504_21d_jerk_v098_signal,
    f17dv_f17_dollar_volume_dynamics_dveffortz252_63d_jerk_v099_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp126_63d_jerk_v100_signal,
    f17dv_f17_dollar_volume_dynamics_dvspkpersist15_21d_jerk_v101_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini126_63d_jerk_v102_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoptime252_63d_jerk_v103_signal,
    f17dv_f17_dollar_volume_dynamics_dvvspxdd252_63d_jerk_v104_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikefreq63_5d_jerk_v105_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean504_63d_jerk_v106_signal,
    f17dv_f17_dollar_volume_dynamics_dvsemiasym63_63d_jerk_v107_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisptrend63_21d_jerk_v108_signal,
    f17dv_f17_dollar_volume_dynamics_dvchgac63_5d_jerk_v109_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown21_21d_jerk_v110_signal,
    f17dv_f17_dollar_volume_dynamics_dvcv126_63d_jerk_v111_signal,
    f17dv_f17_dollar_volume_dynamics_dvspkpersist2q_21d_jerk_v112_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini252_63d_jerk_v113_signal,
    f17dv_f17_dollar_volume_dynamics_dventropy63_5d_jerk_v114_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendt63_5d_jerk_v115_signal,
    f17dv_f17_dollar_volume_dynamics_dvpxcorr252_63d_jerk_v116_signal,
    f17dv_f17_dollar_volume_dynamics_dvrpspr_21d_jerk_v117_signal,
    f17dv_f17_dollar_volume_dynamics_dvdownq63_5d_jerk_v118_signal,
    f17dv_f17_dollar_volume_dynamics_dvgapnorm252_21d_jerk_v119_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom126_21d_jerk_v120_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdown63b_21d_jerk_v121_signal,
    f17dv_f17_dollar_volume_dynamics_dvemadisp126_5d_jerk_v122_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp126_21d_jerk_v123_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup126_21d_jerk_v124_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrydepth63_21d_jerk_v125_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikecnt252_21d_jerk_v126_signal,
    f17dv_f17_dollar_volume_dynamics_dvvolmomdiv63_21d_jerk_v127_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmin252_21d_jerk_v128_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisptrend63_5d_jerk_v129_signal,
    f17dv_f17_dollar_volume_dynamics_dvnewhi504_63d_jerk_v130_signal,
    f17dv_f17_dollar_volume_dynamics_dvdeepdry252_63d_jerk_v131_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew126_21d_jerk_v132_signal,
    f17dv_f17_dollar_volume_dynamics_ldvkurt126_21d_jerk_v133_signal,
    f17dv_f17_dollar_volume_dynamics_dvvspxdd252b_21d_jerk_v134_signal,
    f17dv_f17_dollar_volume_dynamics_dvsignmag252_63d_jerk_v135_signal,
    f17dv_f17_dollar_volume_dynamics_dvwave252_63d_jerk_v136_signal,
    f17dv_f17_dollar_volume_dynamics_dvcross252_21d_jerk_v137_signal,
    f17dv_f17_dollar_volume_dynamics_dvdrawup63_5d_jerk_v138_signal,
    f17dv_f17_dollar_volume_dynamics_dvuwfrac504_63d_jerk_v139_signal,
    f17dv_f17_dollar_volume_dynamics_dvdsh252_21d_jerk_v140_signal,
    f17dv_f17_dollar_volume_dynamics_dvtomean1260_21d_jerk_v141_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank1260_63d_jerk_v142_signal,
    f17dv_f17_dollar_volume_dynamics_dvddfreq252_21d_jerk_v143_signal,
    f17dv_f17_dollar_volume_dynamics_dvupdownchg63_21d_jerk_v144_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangeval126_21d_jerk_v145_signal,
    f17dv_f17_dollar_volume_dynamics_dvlevel126_5d_jerk_v146_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrenddist126_21d_jerk_v147_signal,
    f17dv_f17_dollar_volume_dynamics_dvfloorspr126_63d_jerk_v148_signal,
    f17dv_f17_dollar_volume_dynamics_dvuw40frac252_21d_jerk_v149_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikerecency_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_JERK_001_150 = REGISTRY


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

    print("OK f17_dollar_volume_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
