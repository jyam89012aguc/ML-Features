"""f05 envelope jerk 001-150."""
from __future__ import annotations
import numpy as np
import pandas as pd

def _atr(high, low, close, n):
    pc = close.shift(1)
    tr = pd.concat([(high-low).abs(), (high-pc).abs(), (low-pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()

def _wma(s, n):
    w = np.arange(1, n+1, dtype=float)
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x,w)/w.sum()), raw=True)

def _parkinson(high, low, n):
    r = np.log(high / low.replace(0.0, np.nan))
    v = (r**2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))
    return np.sqrt(v)

def _gk(open_, high, low, close, n):
    hl = np.log(high / low.replace(0.0, np.nan)) ** 2
    co = np.log(close / open_.replace(0.0, np.nan)) ** 2
    daily = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    return np.sqrt(daily.rolling(n, min_periods=n).mean().clip(lower=0.0))

def _ds(touch_mask, idx_seq, nan_mask):
    out = idx_seq - idx_seq.where(touch_mask == 1).ffill()
    out[nan_mask] = np.nan
    return out


def f05me_f05_moving_average_envelope_bbpctb_10d_jerk_v001_signal(close):
    sma = close.rolling(10).mean(); sd = close.rolling(10).std()
    b = (close - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    k = 5
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbcross_50d_jerk_v002_signal(closeadj):
    sma = closeadj.rolling(50).mean()
    sign = np.sign(closeadj - sma); flip = (sign * sign.shift(1) < 0).astype(float)
    b = flip.rolling(50, min_periods=25).sum()
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpctb_200d_jerk_v003_signal(closeadj):
    sma = closeadj.rolling(200).mean(); sd = closeadj.rolling(200).std()
    b = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpctb1_20d_jerk_v004_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    b = (close - (sma - 1.0 * sd)) / (2.0 * sd).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwid_20d_jerk_v005_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    b = (4.0 * sd) / sma.replace(0.0, np.nan)
    k = 5
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwidrnk_120d_jerk_v006_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.rolling(120, min_periods=60).rank(pct=True)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwslp_30d_jerk_v007_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.diff(10) / w.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbsqz_120d_jerk_v008_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    rk = w.rolling(120, min_periods=60).rank(pct=True)
    b = (rk <= 0.10).astype(float); b[rk.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwcurv_40d_jerk_v009_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = (w - 2.0 * w.shift(10) + w.shift(20)) / w.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dsupper_60d_jerk_v010_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    touch = (close >= upper).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    b = _ds(touch, idx, upper.isna())
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dslower_60d_jerk_v011_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    lower = sma - 2.0 * sd
    touch = (close <= lower).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    b = _ds(touch, idx, lower.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_walkup_20d_jerk_v012_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    above = (close > upper).astype(int)
    grp = (above == 0).cumsum()
    cnt = above.groupby(grp).cumcount() + 1
    b = cnt.where(above == 1, 0).astype(float); b[upper.isna()] = np.nan
    k = 5
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_walkdn_20d_jerk_v013_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    lower = sma - 2.0 * sd
    below = (close < lower).astype(int)
    grp = (below == 0).cumsum()
    cnt = below.groupby(grp).cumcount() + 1
    b = cnt.where(below == 1, 0).astype(float); b[lower.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_touchcnt_50d_jerk_v014_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd
    flag = (closeadj >= upper).astype(float)
    b = flag.rolling(50).sum(); b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_touchasy_50d_jerk_v015_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    up = (closeadj >= upper).astype(float).rolling(50).sum()
    dn = (closeadj <= lower).astype(float).rolling(50).sum()
    b = (up - dn) / 50.0; b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_rejtop_30d_jerk_v016_signal(high, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    flag = ((high >= upper) & (close < upper)).astype(float)
    b = flag.rolling(30).sum(); b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_rejbot_30d_jerk_v017_signal(low, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    lower = sma - 2.0 * sd
    flag = ((low <= lower) & (close > lower)).astype(float)
    b = flag.rolling(30).sum(); b[lower.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcbreak_20d_jerk_v018_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr; lower = ema - 2.0 * atr
    b = (close > upper).astype(float) - (close < lower).astype(float)
    b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwid_30d_jerk_v019_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    b = (4.0 * atr) / ema.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_ttmsqz_120d_jerk_v020_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    atr = _atr(high, low, close, 14)
    up_bb = sma + 2.0 * sd; lo_bb = sma - 2.0 * sd
    up_kc = ema + 2.0 * atr; lo_kc = ema - 2.0 * atr
    b = ((up_bb < up_kc) & (lo_bb > lo_kc)).astype(float); b[up_bb.isna() | up_kc.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwidrnk_120d_jerk_v021_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    w = (4.0 * atr) / ema.replace(0.0, np.nan)
    b = w.rolling(120, min_periods=60).rank(pct=True)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcdsup_60d_jerk_v022_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14); upper = ema + 2.0 * atr
    touch = (close >= upper).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    b = _ds(touch, idx, upper.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctstreak_20d_jerk_v023_signal(close):
    sma = close.rolling(20).mean(); upper = 1.015 * sma
    above = (close > upper).astype(int)
    grp = (above == 0).cumsum()
    cnt = above.groupby(grp).cumcount() + 1
    b = cnt.where(above == 1, 0).astype(float); b[sma.isna()] = np.nan
    k = 5
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctenvstate_50d_jerk_v024_signal(closeadj):
    sma = closeadj.rolling(50).mean(); upper = 1.03 * sma; lower = 0.97 * sma
    b = (closeadj > upper).astype(float) - (closeadj < lower).astype(float); b[sma.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctenvbrk_60d_jerk_v025_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    up = (closeadj > 1.02 * sma).astype(float); dn = (closeadj < 0.98 * sma).astype(float)
    b = (up + dn).rolling(60).sum(); b[sma.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctenvst_30d_jerk_v026_signal(close):
    sma = close.rolling(30).mean()
    of = ((close > 1.02 * sma) | (close < 0.98 * sma)).astype(int)
    grp = (of == 0).cumsum()
    cnt = of.groupby(grp).cumcount() + 1
    b = cnt.where(of == 1, 0).astype(float); b[sma.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctenvfrac_60d_jerk_v027_signal(closeadj):
    sma = closeadj.rolling(60).mean(); upper = 1.03 * sma; lower = 0.97 * sma
    of = ((closeadj > upper) | (closeadj < lower)).astype(float)
    b = of.rolling(60).mean(); b[sma.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_asyp_20d_jerk_v028_signal(close):
    sma = close.rolling(20).mean(); dev = close - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev; lower = sma - 2.0 * dn_dev
    b = (close - lower) / (upper - lower).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_asyskew_30d_jerk_v029_signal(closeadj):
    sma = closeadj.rolling(20).mean(); dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).rolling(30).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).rolling(30).mean()
    b = (up_dev - dn_dev) / (up_dev + dn_dev).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_asywdrnk_30d_jerk_v030_signal(closeadj):
    sma = closeadj.rolling(30).mean(); dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=30, adjust=False, min_periods=30).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=30, adjust=False, min_periods=30).mean()
    frac = up_dev / (up_dev + dn_dev).replace(0.0, np.nan)
    b = frac.rolling(80, min_periods=40).rank(pct=True)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_asybrk_50d_jerk_v031_signal(closeadj):
    sma = closeadj.rolling(20).mean(); dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev
    flag = (closeadj > upper).astype(float)
    b = flag.rolling(50).sum(); b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_asylobrk_50d_jerk_v032_signal(closeadj):
    sma = closeadj.rolling(20).mean(); dev = closeadj - sma
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    lower = sma - 2.0 * dn_dev
    flag = (closeadj < lower).astype(float)
    b = flag.rolling(50).sum(); b[lower.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_parkrnk_120d_jerk_v033_signal(high, low):
    pk = _parkinson(high, low, 20)
    b = pk.rolling(120, min_periods=60).rank(pct=True)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_parkwid_30d_jerk_v034_signal(high, low, closeadj):
    sma = closeadj.rolling(30).mean()
    pk = _parkinson(high, low, 30)
    b = (4.0 * pk * closeadj) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_gkwidrat_20d_jerk_v035_signal(open_, high, low, close):
    gk = _gk(open_, high, low, close, 20); sd = close.rolling(20).std()
    b = (gk * close) / (2.0 * sd).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pkdays_60d_jerk_v036_signal(high, low, closeadj):
    sma = closeadj.rolling(30).mean(); pk = _parkinson(high, low, 30)
    upper = sma + 2.0 * pk * closeadj
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(touch, idx, upper.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_madenv_30d_jerk_v037_signal(closeadj):
    sma = closeadj.rolling(30).mean()
    mad = (closeadj - sma).abs().rolling(30).mean()
    upper = sma + 2.0 * mad; lower = sma - 2.0 * mad
    b = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_iqrasy_40d_jerk_v038_signal(closeadj):
    q1 = closeadj.rolling(40).quantile(0.25); med = closeadj.rolling(40).median()
    q3 = closeadj.rolling(40).quantile(0.75); iqr = q3 - q1
    b = ((q3 - med) - (med - q1)) / iqr.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_qbnd_60d_jerk_v039_signal(closeadj):
    sma = closeadj.rolling(30).mean(); q95 = closeadj.rolling(60).quantile(0.95)
    b = (q95 - sma) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_upslp_30d_jerk_v040_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd
    b = upper.diff(10) / upper.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_loslp_30d_jerk_v041_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    lower = sma - 2.0 * sd
    b = lower.diff(10) / lower.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bndsdif_30d_jerk_v042_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    b = upper.diff(10) / sma.replace(0.0, np.nan) - lower.diff(10) / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_upcurv_60d_jerk_v043_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd
    b = (upper - 2.0 * upper.shift(10) + upper.shift(20)) / upper.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_innband_20d_jerk_v044_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 1.0 * sd; lower = sma - 1.0 * sd
    inside = ((close <= upper) & (close >= lower)).astype(float)
    b = inside.rolling(20).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widrat_50d_jerk_v045_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    w20 = (4.0 * sd20) / sma20.replace(0.0, np.nan)
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    w50 = (4.0 * sd50) / sma50.replace(0.0, np.nan)
    b = w20 / w50.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbdiff_50d_jerk_v046_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    pb20 = (closeadj - (sma20 - 2.0 * sd20)) / (4.0 * sd20).replace(0.0, np.nan)
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    pb50 = (closeadj - (sma50 - 2.0 * sd50)) / (4.0 * sd50).replace(0.0, np.nan)
    b = pb20 - pb50
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widdiff_100d_jerk_v047_signal(closeadj):
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    w50 = (4.0 * sd50) / sma50.replace(0.0, np.nan)
    sma100 = closeadj.rolling(100).mean(); sd100 = closeadj.rolling(100).std()
    w100 = (4.0 * sd100) / sma100.replace(0.0, np.nan)
    b = (w50 - w100) / w100.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_signupper_20d_jerk_v048_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd; b = np.sign(close - upper)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_signlower_50d_jerk_v049_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    lower = sma - 2.0 * sd; b = np.sign(closeadj - lower)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_quad_30d_jerk_v050_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = 2.0 * np.sign(close - sma) + np.sign(w.diff(5))
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_breakdir_60d_jerk_v051_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    upn = (closeadj >= upper).astype(float).rolling(5, min_periods=5).sum()
    dnn = (closeadj <= lower).astype(float).rolling(5, min_periods=5).sum()
    b = (upn > 0).astype(float) * (dnn == 0).astype(float) - (dnn > 0).astype(float) * (upn == 0).astype(float)
    b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_sqzbrk_60d_jerk_v052_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    rk = w.rolling(60, min_periods=30).rank(pct=True)
    sqz_then = (rk.shift(5) <= 0.10).astype(float)
    outside = ((closeadj > sma + 2.0 * sd) | (closeadj < sma - 2.0 * sd)).astype(float)
    b = sqz_then * outside; b[rk.shift(5).isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_madwid_30d_jerk_v053_signal(closeadj):
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    mad = (closeadj - sma).abs().rolling(30).mean()
    b = mad / sd.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpath_60d_jerk_v054_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    flag = ((closeadj > upper) | (closeadj < lower)).astype(float)
    b = flag.rolling(60).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbex_30d_jerk_v055_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    b = excess.rolling(30).sum() / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbrank_60d_jerk_v056_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = pb.rolling(60, min_periods=30).rank(pct=True)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widdrawd_120d_jerk_v057_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); peak = w.rolling(120, min_periods=60).max()
    b = 1.0 - (w / peak.replace(0.0, np.nan))
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_walknet_60d_jerk_v058_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    up = (closeadj > upper).astype(float).rolling(60).sum()
    dn = (closeadj < lower).astype(float).rolling(60).sum()
    b = (up - dn) / 60.0; b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widnorm_30d_jerk_v059_signal(closeadj):
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    w_abs = 4.0 * sd
    atr = closeadj.diff().abs().ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    b = w_abs / (atr * 4.0).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widslp_50d_jerk_v060_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); slp = w.diff(10)
    b = slp.rolling(50, min_periods=25).rank(pct=True)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcbbwrat_30d_jerk_v061_signal(high, low, close, closeadj):
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    atr = _atr(high, low, close, 20)
    b = atr / sd.replace(0.0, np.nan); b[sma.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_donchma_50d_jerk_v062_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    hi = sma.rolling(50).max(); lo = sma.rolling(50).min()
    b = (sma - lo) / (hi - lo).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_donchmawid_50d_jerk_v063_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    hi = sma.rolling(50).max(); lo = sma.rolling(50).min()
    b = (hi - lo) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbskew_60d_jerk_v064_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = pb.rolling(60).skew()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widac_60d_jerk_v065_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.rolling(60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widkurt_60d_jerk_v066_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.rolling(60).kurt()
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbvar_30d_jerk_v067_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = pb.rolling(30).std()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_emasmadif_20d_jerk_v068_signal(close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    b = (ema - sma) / (2.0 * sd).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widema_30d_jerk_v069_signal(closeadj):
    ema = closeadj.ewm(span=30, adjust=False, min_periods=30).mean()
    var = (closeadj - ema).pow(2).ewm(span=30, adjust=False, min_periods=30).mean()
    sd = np.sqrt(var)
    b = (4.0 * sd) / ema.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_walkbeyond_30d_jerk_v070_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.5 * sd
    flag = (closeadj > upper).astype(float)
    b = flag.rolling(30).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widmad_50d_jerk_v071_signal(closeadj):
    sma = closeadj.rolling(50).mean()
    mad = (closeadj - sma).abs().rolling(50).mean()
    b = (4.0 * mad) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_envtilt_30d_jerk_v072_signal(closeadj):
    sma = closeadj.rolling(20).mean(); dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev; lower = sma - 2.0 * dn_dev
    tmp = upper.diff(10) / lower.diff(10).abs().replace(0.0, np.nan)
    b = np.sign(lower.diff(10)) * tmp
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widvol_60d_jerk_v073_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    m = w.rolling(60).mean(); s = w.rolling(60).std()
    b = s / m.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_distup_30d_jerk_v074_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd
    b = (upper - closeadj) / upper.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_distlo_50d_jerk_v075_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    lower = sma - 2.0 * sd
    b = (closeadj - lower) / lower.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpctb_30d_jerk_v076_signal(closeadj):
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    b = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpctb3_20d_jerk_v077_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 3.0 * sd; lower = sma - 3.0 * sd
    b = (close - upper).clip(lower=0.0) - (lower - close).clip(lower=0.0)
    b = b / sma.replace(0.0, np.nan)
    k = 5
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_emabbwid_50d_jerk_v078_signal(closeadj):
    ema = closeadj.ewm(span=50, adjust=False, min_periods=50).mean()
    var = (closeadj - ema).pow(2).ewm(span=50, adjust=False, min_periods=50).mean()
    sd = np.sqrt(var)
    b = (4.0 * sd) / ema.replace(0.0, np.nan)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_wmasmadif_30d_jerk_v079_signal(closeadj):
    wma = _wma(closeadj, 30)
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    b = (wma - sma) / (2.0 * sd).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_medsmadif_30d_jerk_v080_signal(closeadj):
    med = closeadj.rolling(30).median()
    sma = closeadj.rolling(30).mean()
    q1 = closeadj.rolling(30).quantile(0.25)
    q3 = closeadj.rolling(30).quantile(0.75)
    iqr = q3 - q1
    b = (med - sma) / iqr.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcpctk_40d_jerk_v081_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=40, adjust=False, min_periods=40).mean()
    atr = _atr(high, low, close, 20)
    upper = ema + 1.5 * atr; lower = ema - 1.5 * atr
    b = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwid_50d_jerk_v082_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=50, adjust=False, min_periods=50).mean()
    atr = _atr(high, low, close, 30)
    b = (4.0 * atr) / ema.replace(0.0, np.nan)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwslp_60d_jerk_v083_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    w = (4.0 * atr) / ema.replace(0.0, np.nan)
    b = w.diff(21) / w.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcdslo_60d_jerk_v084_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14); lower = ema - 2.0 * atr
    touch = (close <= lower).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    b = _ds(touch, idx, lower.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwalkup_30d_jerk_v085_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14); upper = ema + 2.0 * atr
    flag = (close > upper).astype(float)
    b = flag.rolling(30).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwalkdn_30d_jerk_v086_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14); lower = ema - 2.0 * atr
    flag = (close < lower).astype(float)
    b = flag.rolling(30).mean(); b[lower.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbtouchint_60d_jerk_v087_signal(close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    touch = (close >= upper).astype(float); cnt = touch.rolling(60).sum()
    b = 60.0 / cnt.where(cnt > 0, 1.0); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbdsmid_60d_jerk_v088_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    sign = np.sign(closeadj - sma); flip = (sign * sign.shift(1) < 0).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(flip, idx, sma.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbinside_60d_jerk_v089_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    inside = ((closeadj <= upper) & (closeadj >= lower)).astype(float)
    b = inside.rolling(60).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwidroc_60d_jerk_v090_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w / w.shift(21).replace(0.0, np.nan) - 1.0
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbwjerk_60d_jerk_v091_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = (w - 2.0 * w.shift(15) + w.shift(30)) / w.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbpathsgn_60d_jerk_v092_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    up = (closeadj > upper).astype(float).rolling(60).sum()
    dn = (closeadj < lower).astype(float).rolling(60).sum()
    b = (up - dn) / 60.0; b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbnewlow_60d_jerk_v093_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); mn = w.rolling(60).min()
    b = (w <= mn + 1e-12).astype(float); b[w.isna() | mn.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbnewhigh_60d_jerk_v094_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); mx = w.rolling(60).max()
    b = (w >= mx - 1e-12).astype(float); b[w.isna() | mx.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dnsdev_40d_jerk_v095_signal(closeadj):
    sma = closeadj.rolling(40).mean(); dev = closeadj - sma
    dn = dev.where(dev < 0, 0.0)
    rms = (dn.pow(2).rolling(40).mean()).pow(0.5)
    b = (2.0 * rms) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_upsdev_40d_jerk_v096_signal(closeadj):
    sma = closeadj.rolling(40).mean(); dev = closeadj - sma
    up = dev.where(dev > 0, 0.0)
    rms = (up.pow(2).rolling(40).mean()).pow(0.5)
    b = (2.0 * rms) / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dnsfrac_60d_jerk_v097_signal(closeadj):
    sma = closeadj.rolling(60).mean(); dev = closeadj - sma
    up = (dev.where(dev > 0, 0.0).pow(2).rolling(60).mean()).pow(0.5)
    dn = ((-dev.where(dev < 0, 0.0)).pow(2).rolling(60).mean()).pow(0.5)
    b = dn / (up + dn).replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_atrenvdays_40d_jerk_v098_signal(high, low, close, closeadj):
    sma = closeadj.rolling(40).mean(); atr = _atr(high, low, close, 20)
    upper = sma + 1.0 * atr
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(touch, idx, upper.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_atrwid_80d_jerk_v099_signal(high, low, close, closeadj):
    sma = closeadj.rolling(80).mean(); atr = _atr(high, low, close, 50)
    b = (2.0 * atr) / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_trbbwrat_40d_jerk_v100_signal(high, low, close, closeadj):
    atr = _atr(high, low, close, 40); sd = closeadj.rolling(40).std()
    b = atr / sd.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_lowanchor_50d_jerk_v101_signal(closeadj):
    sma = closeadj.rolling(50).mean(); lo = closeadj.rolling(50).min()
    anch = lo + 0.02 * sma
    b = (closeadj - anch) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_highanchor_50d_jerk_v102_signal(closeadj):
    sma = closeadj.rolling(50).mean(); hi = closeadj.rolling(50).max()
    b = (hi - closeadj) / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bandsep_50d_jerk_v103_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    up20 = sma20 + 2.0 * sd20
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    up50 = sma50 + 2.0 * sd50
    b = (up20 - up50) / sma50.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bandsep_lo_50d_jerk_v104_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    lo20 = sma20 - 2.0 * sd20
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    lo50 = sma50 - 2.0 * sd50
    b = (lo20 - lo50) / sma50.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_exrange_30d_jerk_v105_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    b = excess.rolling(30).max() / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bodyabove_30d_jerk_v106_signal(open_, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    body_min = pd.concat([open_, close], axis=1).min(axis=1)
    flag = (body_min > upper).astype(float)
    b = flag.rolling(30).mean(); b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bodybelow_30d_jerk_v107_signal(open_, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    lower = sma - 2.0 * sd
    body_max = pd.concat([open_, close], axis=1).max(axis=1)
    flag = (body_max < lower).astype(float)
    b = flag.rolling(30).mean(); b[lower.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widskew_60d_jerk_v108_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.rolling(60).skew()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbac_50d_jerk_v109_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = pb.rolling(50).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbquadcnt_50d_jerk_v110_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    flag = ((pb <= 0.2) | (pb >= 0.8)).astype(float)
    b = flag.rolling(50).sum(); b[pb.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_meanrev_60d_jerk_v111_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    dpb = pb.diff()
    b = pb.shift(1).rolling(60).corr(dpb)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_hlrange_30d_jerk_v112_signal(high, low, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    width = 4.0 * sd; rng = high - low
    b = rng / width.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_highbreach_30d_jerk_v113_signal(high, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    upper = sma + 2.0 * sd
    flag = (high > upper).astype(float)
    b = flag.rolling(30).sum(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_lowbreach_30d_jerk_v114_signal(low, close):
    sma = close.rolling(20).mean(); sd = close.rolling(20).std()
    lower = sma - 2.0 * sd
    flag = (low < lower).astype(float)
    b = flag.rolling(30).sum(); b[lower.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_donchemwid_60d_jerk_v115_signal(closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    hi = ema.rolling(60).max(); lo = ema.rolling(60).min()
    b = (hi - lo) / ema.replace(0.0, np.nan)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_donchempos_60d_jerk_v116_signal(closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    hi = ema.rolling(60).max(); lo = ema.rolling(60).min()
    b = (ema - lo) / (hi - lo).replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widatrrat_40d_jerk_v117_signal(high, low, close, closeadj):
    sd = closeadj.rolling(40).std()
    atr = _atr(high, low, close, 20)
    b = sd / atr.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widasymrat_40d_jerk_v118_signal(closeadj):
    sma = closeadj.rolling(40).mean(); dev = closeadj - sma
    up = (dev.where(dev > 0, 0.0).pow(2).rolling(40).mean()).pow(0.5)
    dn = ((-dev.where(dev < 0, 0.0)).pow(2).rolling(40).mean()).pow(0.5)
    b = up / dn.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_envcurv_60d_jerk_v119_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    lo = sma - 2.0 * sd
    b = (lo - 2.0 * lo.shift(15) + lo.shift(30)) / sma.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widmean_120d_jerk_v120_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = w.rolling(120, min_periods=60).mean()
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcpathfrac_60d_jerk_v121_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr; lower = ema - 2.0 * atr
    flag = ((close > upper) | (close < lower)).astype(float)
    b = flag.rolling(60).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctwidrnk_60d_jerk_v122_signal(closeadj):
    sma = closeadj.rolling(20).mean(); upper = 1.02 * sma; lower = 0.98 * sma
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    mag = excess / sma.replace(0.0, np.nan)
    b = mag.rolling(60, min_periods=30).rank(pct=True)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widpbcorr_60d_jerk_v123_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    pb_extr = (pb - 0.5).abs()
    b = w.rolling(60).corr(pb_extr)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widmonot_30d_jerk_v124_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); d = w.diff()
    pos = (d > 0).astype(float).rolling(30).sum()
    neg = (d < 0).astype(float).rolling(30).sum()
    b = (pos - neg) / 30.0; b[w.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widmrev_60d_jerk_v125_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan); dw = w.diff()
    b = w.shift(1).rolling(60).corr(dw)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_signmid_20d_jerk_v126_signal(close):
    sma = close.rolling(20).mean()
    b = np.sign(close - sma).astype(float); b[sma.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widthsign_30d_jerk_v127_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    b = np.sign(w.diff(21)).astype(float); b[w.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pkgkwid_30d_jerk_v128_signal(open_, high, low, close, closeadj):
    r = np.log(high / low.replace(0.0, np.nan))
    pk_var = (r ** 2).rolling(30).mean() / (4.0 * np.log(2.0))
    pk = np.sqrt(pk_var)
    hl = np.log(high / low.replace(0.0, np.nan)) ** 2
    co = np.log(close / open_.replace(0.0, np.nan)) ** 2
    daily = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    gk = np.sqrt(daily.rolling(30).mean().clip(lower=0.0))
    b = pk / gk.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcsqz_60d_jerk_v129_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    w = (4.0 * atr) / ema.replace(0.0, np.nan)
    rk = w.rolling(60, min_periods=30).rank(pct=True)
    b = (rk <= 0.10).astype(float); b[rk.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbdiff_200d_jerk_v130_signal(closeadj):
    sma50 = closeadj.rolling(50).mean(); sd50 = closeadj.rolling(50).std()
    pb50 = (closeadj - (sma50 - 2.0 * sd50)) / (4.0 * sd50).replace(0.0, np.nan)
    sma200 = closeadj.rolling(200).mean(); sd200 = closeadj.rolling(200).std()
    pb200 = (closeadj - (sma200 - 2.0 * sd200)) / (4.0 * sd200).replace(0.0, np.nan)
    b = pb50 - pb200
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dsupper_120d_jerk_v131_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    upper = sma + 2.0 * sd
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(touch, idx, upper.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dslower_120d_jerk_v132_signal(closeadj):
    sma = closeadj.rolling(50).mean(); sd = closeadj.rolling(50).std()
    lower = sma - 2.0 * sd
    touch = (closeadj <= lower).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(touch, idx, lower.isna())
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbexcsign_30d_jerk_v133_signal(closeadj):
    sma = closeadj.rolling(30).mean(); sd = closeadj.rolling(30).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    pos = (closeadj - upper).clip(lower=0.0); neg = (lower - closeadj).clip(lower=0.0)
    b = (pos - neg) / sma.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcoutfrac_30d_jerk_v134_signal(high, low, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr; lower = ema - 2.0 * atr
    flag = ((low > upper) | (high < lower)).astype(float)
    b = flag.rolling(30).mean(); b[upper.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bandgap_100d_jerk_v135_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    up20 = sma20 + 2.0 * sd20
    sma100 = closeadj.rolling(100).mean(); sd100 = closeadj.rolling(100).std()
    up100 = sma100 + 2.0 * sd100
    b = (up20 - up100) / sma100.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bandgap_lo_100d_jerk_v136_signal(closeadj):
    sma20 = closeadj.rolling(20).mean(); sd20 = closeadj.rolling(20).std()
    lo20 = sma20 - 2.0 * sd20
    sma100 = closeadj.rolling(100).mean(); sd100 = closeadj.rolling(100).std()
    lo100 = sma100 - 2.0 * sd100
    b = (lo20 - lo100) / sma100.replace(0.0, np.nan)
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbweight_60d_jerk_v137_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = pb.ewm(halflife=20, adjust=False, min_periods=60).mean()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widewmrat_60d_jerk_v138_signal(closeadj):
    ewm_var = closeadj.diff().pow(2).ewm(span=20, adjust=False, min_periods=20).mean()
    ewm_sd = np.sqrt(ewm_var)
    sd = closeadj.diff().rolling(20).std()
    b = ewm_sd / sd.replace(0.0, np.nan)
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbsamesign_30d_jerk_v139_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    flag = (closeadj > sma).astype(float)
    b = flag.rolling(30).mean(); b[sma.isna()] = np.nan
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbpeakgap_60d_jerk_v140_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    mx = pb.rolling(60).max()
    b = mx - pb
    k = 63
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pbrange_60d_jerk_v141_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    mn = pb.rolling(60).min(); mx = pb.rolling(60).max()
    b = mx - mn
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwidskew_60d_jerk_v142_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    w = (4.0 * atr) / ema.replace(0.0, np.nan)
    b = w.rolling(60).skew()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcwidkurt_60d_jerk_v143_signal(high, low, close, closeadj):
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    w = (4.0 * atr) / ema.replace(0.0, np.nan)
    b = w.rolling(60).kurt()
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_bbslprat_30d_jerk_v144_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    upper = sma + 2.0 * sd; lower = sma - 2.0 * sd
    us = upper.diff(10) / sma.replace(0.0, np.nan); ls = lower.diff(10) / sma.replace(0.0, np.nan)
    b = us / ls.abs().replace(0.0, np.nan) * np.sign(ls)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dsmidup_60d_jerk_v145_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    sign = np.sign(closeadj - sma); flip = ((sign > 0) & (sign.shift(1) <= 0)).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(flip, idx, sma.isna())
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_dsmidwn_60d_jerk_v146_signal(closeadj):
    sma = closeadj.rolling(20).mean()
    sign = np.sign(closeadj - sma); flip = ((sign < 0) & (sign.shift(1) >= 0)).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b = _ds(flip, idx, sma.isna())
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widmedrat_60d_jerk_v147_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    med = w.rolling(60, min_periods=30).median()
    b = w / med.replace(0.0, np.nan)
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_pctcombo_60d_jerk_v148_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    b = (pb - 0.5).rolling(60).mean()
    k = 10
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_widlongshort_120d_jerk_v149_signal(closeadj):
    sma = closeadj.rolling(20).mean(); sd = closeadj.rolling(20).std()
    w = (4.0 * sd) / sma.replace(0.0, np.nan)
    m120 = w.rolling(120, min_periods=60).mean(); m60 = w.rolling(60).mean()
    b = m120 - m60
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)

def f05me_f05_moving_average_envelope_kcrejtop_30d_jerk_v150_signal(high, close):
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    pc = close.shift(1)
    tr = pd.concat([(high - close).abs(), (high - pc).abs(), (close - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    upper = ema + 2.0 * atr
    flag = ((high >= upper) & (close < upper)).astype(float)
    b = flag.rolling(30).sum(); b[upper.isna()] = np.nan
    k = 21
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf], np.nan)


def _e(fn, *inp):
    return fn.__name__, {"inputs": list(inp), "func": fn}

f05_moving_average_envelope_jerk_001_150_REGISTRY = dict([
_e(f05me_f05_moving_average_envelope_bbpctb_10d_jerk_v001_signal, "close"),
_e(f05me_f05_moving_average_envelope_bbcross_50d_jerk_v002_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpctb_200d_jerk_v003_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpctb1_20d_jerk_v004_signal, "close"),
_e(f05me_f05_moving_average_envelope_bbwid_20d_jerk_v005_signal, "close"),
_e(f05me_f05_moving_average_envelope_bbwidrnk_120d_jerk_v006_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbwslp_30d_jerk_v007_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbsqz_120d_jerk_v008_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbwcurv_40d_jerk_v009_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dsupper_60d_jerk_v010_signal, "close"),
_e(f05me_f05_moving_average_envelope_dslower_60d_jerk_v011_signal, "close"),
_e(f05me_f05_moving_average_envelope_walkup_20d_jerk_v012_signal, "close"),
_e(f05me_f05_moving_average_envelope_walkdn_20d_jerk_v013_signal, "close"),
_e(f05me_f05_moving_average_envelope_touchcnt_50d_jerk_v014_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_touchasy_50d_jerk_v015_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_rejtop_30d_jerk_v016_signal, "high", "close"),
_e(f05me_f05_moving_average_envelope_rejbot_30d_jerk_v017_signal, "low", "close"),
_e(f05me_f05_moving_average_envelope_kcbreak_20d_jerk_v018_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_kcwid_30d_jerk_v019_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_ttmsqz_120d_jerk_v020_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_kcwidrnk_120d_jerk_v021_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcdsup_60d_jerk_v022_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_pctstreak_20d_jerk_v023_signal, "close"),
_e(f05me_f05_moving_average_envelope_pctenvstate_50d_jerk_v024_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pctenvbrk_60d_jerk_v025_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pctenvst_30d_jerk_v026_signal, "close"),
_e(f05me_f05_moving_average_envelope_pctenvfrac_60d_jerk_v027_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_asyp_20d_jerk_v028_signal, "close"),
_e(f05me_f05_moving_average_envelope_asyskew_30d_jerk_v029_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_asywdrnk_30d_jerk_v030_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_asybrk_50d_jerk_v031_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_asylobrk_50d_jerk_v032_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_parkrnk_120d_jerk_v033_signal, "high", "low"),
_e(f05me_f05_moving_average_envelope_parkwid_30d_jerk_v034_signal, "high", "low", "closeadj"),
_e(f05me_f05_moving_average_envelope_gkwidrat_20d_jerk_v035_signal, "open", "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_pkdays_60d_jerk_v036_signal, "high", "low", "closeadj"),
_e(f05me_f05_moving_average_envelope_madenv_30d_jerk_v037_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_iqrasy_40d_jerk_v038_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_qbnd_60d_jerk_v039_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_upslp_30d_jerk_v040_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_loslp_30d_jerk_v041_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bndsdif_30d_jerk_v042_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_upcurv_60d_jerk_v043_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_innband_20d_jerk_v044_signal, "close"),
_e(f05me_f05_moving_average_envelope_widrat_50d_jerk_v045_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbdiff_50d_jerk_v046_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widdiff_100d_jerk_v047_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_signupper_20d_jerk_v048_signal, "close"),
_e(f05me_f05_moving_average_envelope_signlower_50d_jerk_v049_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_quad_30d_jerk_v050_signal, "close"),
_e(f05me_f05_moving_average_envelope_breakdir_60d_jerk_v051_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_sqzbrk_60d_jerk_v052_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_madwid_30d_jerk_v053_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpath_60d_jerk_v054_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbex_30d_jerk_v055_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbrank_60d_jerk_v056_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widdrawd_120d_jerk_v057_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_walknet_60d_jerk_v058_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widnorm_30d_jerk_v059_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widslp_50d_jerk_v060_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcbbwrat_30d_jerk_v061_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_donchma_50d_jerk_v062_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_donchmawid_50d_jerk_v063_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbskew_60d_jerk_v064_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widac_60d_jerk_v065_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widkurt_60d_jerk_v066_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbvar_30d_jerk_v067_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_emasmadif_20d_jerk_v068_signal, "close"),
_e(f05me_f05_moving_average_envelope_widema_30d_jerk_v069_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_walkbeyond_30d_jerk_v070_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widmad_50d_jerk_v071_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_envtilt_30d_jerk_v072_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widvol_60d_jerk_v073_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_distup_30d_jerk_v074_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_distlo_50d_jerk_v075_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpctb_30d_jerk_v076_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpctb3_20d_jerk_v077_signal, "close"),
_e(f05me_f05_moving_average_envelope_emabbwid_50d_jerk_v078_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_wmasmadif_30d_jerk_v079_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_medsmadif_30d_jerk_v080_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcpctk_40d_jerk_v081_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcwid_50d_jerk_v082_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcwslp_60d_jerk_v083_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcdslo_60d_jerk_v084_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_kcwalkup_30d_jerk_v085_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_kcwalkdn_30d_jerk_v086_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_bbtouchint_60d_jerk_v087_signal, "close"),
_e(f05me_f05_moving_average_envelope_bbdsmid_60d_jerk_v088_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbinside_60d_jerk_v089_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbwidroc_60d_jerk_v090_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbwjerk_60d_jerk_v091_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbpathsgn_60d_jerk_v092_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbnewlow_60d_jerk_v093_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbnewhigh_60d_jerk_v094_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dnsdev_40d_jerk_v095_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_upsdev_40d_jerk_v096_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dnsfrac_60d_jerk_v097_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_atrenvdays_40d_jerk_v098_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_atrwid_80d_jerk_v099_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_trbbwrat_40d_jerk_v100_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_lowanchor_50d_jerk_v101_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_highanchor_50d_jerk_v102_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bandsep_50d_jerk_v103_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bandsep_lo_50d_jerk_v104_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_exrange_30d_jerk_v105_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bodyabove_30d_jerk_v106_signal, "open", "close"),
_e(f05me_f05_moving_average_envelope_bodybelow_30d_jerk_v107_signal, "open", "close"),
_e(f05me_f05_moving_average_envelope_widskew_60d_jerk_v108_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbac_50d_jerk_v109_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbquadcnt_50d_jerk_v110_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_meanrev_60d_jerk_v111_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_hlrange_30d_jerk_v112_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_highbreach_30d_jerk_v113_signal, "high", "close"),
_e(f05me_f05_moving_average_envelope_lowbreach_30d_jerk_v114_signal, "low", "close"),
_e(f05me_f05_moving_average_envelope_donchemwid_60d_jerk_v115_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_donchempos_60d_jerk_v116_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widatrrat_40d_jerk_v117_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_widasymrat_40d_jerk_v118_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_envcurv_60d_jerk_v119_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widmean_120d_jerk_v120_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcpathfrac_60d_jerk_v121_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_pctwidrnk_60d_jerk_v122_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widpbcorr_60d_jerk_v123_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widmonot_30d_jerk_v124_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widmrev_60d_jerk_v125_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_signmid_20d_jerk_v126_signal, "close"),
_e(f05me_f05_moving_average_envelope_widthsign_30d_jerk_v127_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pkgkwid_30d_jerk_v128_signal, "open", "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcsqz_60d_jerk_v129_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_pbdiff_200d_jerk_v130_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dsupper_120d_jerk_v131_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dslower_120d_jerk_v132_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbexcsign_30d_jerk_v133_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcoutfrac_30d_jerk_v134_signal, "high", "low", "close"),
_e(f05me_f05_moving_average_envelope_bandgap_100d_jerk_v135_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bandgap_lo_100d_jerk_v136_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbweight_60d_jerk_v137_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widewmrat_60d_jerk_v138_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_bbsamesign_30d_jerk_v139_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbpeakgap_60d_jerk_v140_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pbrange_60d_jerk_v141_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcwidskew_60d_jerk_v142_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_kcwidkurt_60d_jerk_v143_signal, "high", "low", "close", "closeadj"),
_e(f05me_f05_moving_average_envelope_bbslprat_30d_jerk_v144_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dsmidup_60d_jerk_v145_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_dsmidwn_60d_jerk_v146_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widmedrat_60d_jerk_v147_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_pctcombo_60d_jerk_v148_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_widlongshort_120d_jerk_v149_signal, "closeadj"),
_e(f05me_f05_moving_average_envelope_kcrejtop_30d_jerk_v150_signal, "high", "close"),
])


def _synthetic_inputs(n=800, seed=42):
    rng = np.random.default_rng(seed); seg = n // 4; rest = n - 3 * seg
    ret = np.concatenate([rng.normal(0.0012,0.011,seg), rng.normal(-0.0005,0.018,seg),
        rng.normal(-0.0010,0.014,seg), rng.normal(0.0008,0.012,rest)])
    close = 50.0 * np.exp(np.cumsum(ret))
    closeadj = close * np.exp(rng.normal(0.0,0.0003,size=n).cumsum())
    intra = rng.normal(0.0,0.008,size=n); open_ = close * np.exp(-intra*0.5)
    high = np.maximum(close,open_) * np.exp(np.abs(rng.normal(0.0,0.006,size=n)))
    low = np.minimum(close,open_) * np.exp(-np.abs(rng.normal(0.0,0.006,size=n)))
    volume = rng.lognormal(mean=13.0,sigma=0.6,size=n); idx = pd.RangeIndex(n)
    return pd.DataFrame({"open":pd.Series(open_,index=idx,dtype=float),
        "high":pd.Series(high,index=idx,dtype=float), "low":pd.Series(low,index=idx,dtype=float),
        "close":pd.Series(close,index=idx,dtype=float), "closeadj":pd.Series(closeadj,index=idx,dtype=float),
        "volume":pd.Series(volume,index=idx,dtype=float)})


def _self_test():
    df = _synthetic_inputs(800, 42); results = {}
    for name, entry in f05_moving_average_envelope_jerk_001_150_REGISTRY.items():
        out = entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out, pd.Series); assert len(out) == len(df)
        clean = out.dropna(); assert len(clean) > 0
        assert float(clean.std()) > 0.0 or clean.nunique() > 1
        results[name] = out
    warm = 252
    frac = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5) / len(results)
    assert frac >= 0.80
    A = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:].replace([np.inf,-np.inf], np.nan)
    C = A.corr(min_periods=50).abs(); np.fill_diagonal(C.values, 0.0)
    mc = float(C.max().max())
    if mc > 0.95:
        s = C.unstack().sort_values(ascending=False); s = s[s > 0.94].head(40); seen = set()
        for (a, b), v in s.items():
            if a < b and (a, b) not in seen:
                seen.add((a, b)); print(f"  {a}  vs  {b}  ->  {v:.4f}")
    assert mc <= 0.95 + 1e-9, f"max pairwise |corr|={mc:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={mc:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
