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


def _logchg(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _dil(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _creep(d, b):
    return d / b.replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slopew(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# jerk operator: 2nd math derivative = central second difference over step w
def _d2(s, w):
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)


# ============================================================
# Each function computes a DISTINCT base quantity inline, then takes its
# 2nd derivative (jerk) over an ROC window appropriate to the base window.

def f28sc_f28_share_count_dynamics_dilbas252_21d_jerk_v001_signal(sharesbas):
    base = _dil(sharesbas, 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas63_5d_jerk_v002_signal(sharesbas):
    base = _dil(sharesbas, 63)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas126_21d_jerk_v003_signal(sharesbas):
    base = _dil(sharesbas, 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwa252_21d_jerk_v004_signal(shareswa):
    base = _logchg(shareswa, 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwa63_5d_jerk_v005_signal(shareswa):
    base = _logchg(shareswa, 63)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creep_21d_jerk_v006_signal(shareswadil, shareswa):
    base = _creep(shareswadil, shareswa)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creep_63d_jerk_v007_signal(shareswadil, shareswa):
    base = _creep(shareswadil, shareswa)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilspread_21d_jerk_v008_signal(shareswadil, sharesbas):
    base = _logchg(shareswadil, 252) - _logchg(sharesbas, 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintens_21d_jerk_v009_signal(ncfcommon, sharesbas):
    base = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_purity_21d_jerk_v010_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    base = net / gross.replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countrngpos_21d_jerk_v011_signal(sharesbas):
    hi = _rmax(sharesbas, 504)
    lo = _rmin(sharesbas, 504)
    base = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilz_21d_jerk_v012_signal(sharesbas):
    base = _z(_logchg(sharesbas, 252), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilrank_21d_jerk_v013_signal(sharesbas):
    base = _rank(_logchg(sharesbas, 252), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilstreak_21d_jerk_v014_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_baswadiv_21d_jerk_v015_signal(sharesbas, shareswa):
    base = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncflevel_21d_jerk_v016_signal(ncfcommon):
    q = ncfcommon.rolling(63, min_periods=21).sum()
    base = np.sign(q) * np.log1p(q.abs())
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildildtr_21d_jerk_v017_signal(shareswadil):
    g = _logchg(shareswadil, 252)
    base = g - g.ewm(span=126, min_periods=42).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepz_21d_jerk_v018_signal(shareswadil, shareswa):
    base = _z(_creep(shareswadil, shareswa), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbconsist_21d_jerk_v019_signal(ncfcommon):
    qsum = ncfcommon.rolling(63, min_periods=21).sum()
    base = (qsum < 0).astype(float).rolling(504, min_periods=252).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_belowmax_21d_jerk_v020_signal(sharesbas):
    rmax = _rmax(sharesbas, 504)
    base = sharesbas / rmax.replace(0, np.nan) - 1.0
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepz504_21d_jerk_v021_signal(shareswadil, shareswa):
    base = _z(_creep(shareswadil, shareswa), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildisp_63d_jerk_v022_signal(sharesbas):
    base = _std(_logchg(sharesbas, 63), 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintensz_21d_jerk_v023_signal(ncfcommon, shareswa):
    base = _z((-ncfcommon) / shareswa.replace(0, np.nan), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countdev_21d_jerk_v024_signal(shareswa):
    m = _mean(shareswa, 252)
    base = shareswa / m.replace(0, np.nan) - 1.0
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issrate_21d_jerk_v025_signal(ncfcommon, sharesbas):
    rate = ncfcommon.rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    base = np.sign(rate) * np.log1p(rate.abs())
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepmom_21d_jerk_v026_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = c - c.shift(63)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas21_5d_jerk_v027_signal(sharesbas):
    base = _dil(sharesbas, 21)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwadisp_63d_jerk_v028_signal(shareswa):
    base = _std(_logchg(shareswa, 63), 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildilstreak_21d_jerk_v029_signal(shareswadil):
    up = (shareswadil.diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilasym_21d_jerk_v030_signal(shareswa):
    chg = _logchg(shareswa, 21)
    up = (chg > 0).astype(float).rolling(252, min_periods=126).mean()
    dn = (chg < 0).astype(float).rolling(252, min_periods=126).mean()
    base = up - dn
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbasratiorank_21d_jerk_v031_signal(shareswadil, sharesbas):
    r = shareswadil / sharesbas.replace(0, np.nan)
    base = _rank(r, 1260)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_purity504_63d_jerk_v032_signal(ncfcommon):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    gross = ncfcommon.abs().rolling(504, min_periods=252).sum()
    base = net / gross.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_trend_21d_jerk_v033_signal(sharesbas):
    base = _slopew(np.log(sharesbas.replace(0, np.nan)), 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creeprngpos_21d_jerk_v034_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    hi = _rmax(c, 504)
    lo = _rmin(c, 504)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintens_63d_jerk_v035_signal(ncfcommon, sharesbas):
    base = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_diltanh_21d_jerk_v036_signal(sharesbas):
    base = np.tanh(20.0 * _logchg(sharesbas, 252))
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_flowtilt_21d_jerk_v037_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    base = (q / (q.abs() + 1e6)).rolling(252, min_periods=126).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_abovemin_21d_jerk_v038_signal(sharesbas):
    rmin = _rmin(sharesbas, 504)
    base = sharesbas / rmin.replace(0, np.nan) - 1.0
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepconv_21d_jerk_v039_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    dev = c - c.rolling(252, min_periods=126).mean()
    base = np.sign(dev) * (dev ** 2)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwarank_21d_jerk_v040_signal(shareswa):
    base = _rank(_logchg(shareswa, 252), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issscale_21d_jerk_v041_signal(ncfcommon, sharesbas):
    mag = ncfcommon.abs().rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    base = _rank(mag, 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_diler_63d_jerk_v042_signal(sharesbas):
    lg = np.log(sharesbas.replace(0, np.nan))
    net = (lg - lg.shift(252)).abs()
    path = lg.diff().abs().rolling(252, min_periods=126).sum()
    base = net / path.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creep_5d_jerk_v043_signal(shareswadil, shareswa):
    base = _creep(shareswadil, shareswa)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwa126_21d_jerk_v044_signal(shareswa):
    base = _dil(shareswa, 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issaccel_63d_jerk_v045_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    sm = np.sign(net) * np.log1p(net.abs())
    base = sm - sm.shift(252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_overhanglead_21d_jerk_v046_signal(shareswadil, shareswa):
    lead = (shareswadil.pct_change() > shareswa.pct_change()).astype(float)
    base = lead.rolling(252, min_periods=126).mean() - 0.5
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bblump_21d_jerk_v047_signal(ncfcommon):
    m = (-ncfcommon).rolling(21, min_periods=10).sum().clip(lower=0)
    peak = m.rolling(252, min_periods=126).max()
    avg = m.rolling(252, min_periods=126).mean()
    base = peak / avg.replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_cumdrag_63d_jerk_v048_signal(sharesbas):
    base = _logchg(sharesbas, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepema_21d_jerk_v049_signal(shareswadil, shareswa):
    base = _creep(shareswadil, shareswa).ewm(span=126, min_periods=42).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_fundmix_21d_jerk_v050_signal(shareswadil, shareswa, ncfcommon, sharesbas):
    creep = _creep(shareswadil, shareswa).abs()
    iss = (ncfcommon.rolling(504, min_periods=252).sum() / sharesbas.replace(0, np.nan)).abs()
    base = creep / (creep + iss + 1e-9) - 0.5
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas252_63d_jerk_v051_signal(sharesbas):
    base = _dil(sharesbas, 252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwa252_63d_jerk_v052_signal(shareswa):
    base = _logchg(shareswa, 252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_netstance_21d_jerk_v053_signal(ncfcommon, sharesbas):
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    dil = _logchg(sharesbas, 252)
    base = _z(bb, 504) - _z(dil, 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepmom_5d_jerk_v054_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = c - c.shift(21)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countrngpos1260_63d_jerk_v055_signal(sharesbas):
    detr = sharesbas / _mean(sharesbas, 252).replace(0, np.nan)
    base = _rank(detr, 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncfema_21d_jerk_v056_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    s = q.ewm(span=126, min_periods=42).mean()
    base = np.sign(s) * np.log1p(s.abs())
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilvol_63d_jerk_v057_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    vol = _std(_logchg(sharesbas, 21), 252)
    base = g / vol.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbrank_21d_jerk_v058_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    base = _rank(raw, 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_trenddil_21d_jerk_v059_signal(shareswadil):
    base = _slopew(np.log(shareswadil.replace(0, np.nan)), 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepdisp_63d_jerk_v060_signal(shareswadil, shareswa):
    base = _std(_creep(shareswadil, shareswa), 252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas504_21d_jerk_v061_signal(sharesbas):
    base = _logchg(sharesbas, 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_baswadivrank_21d_jerk_v062_signal(sharesbas, shareswa):
    d = sharesbas / shareswa.replace(0, np.nan) - 1.0
    base = _rank(d, 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_reductqual_63d_jerk_v063_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = -net / gross.replace(0, np.nan)
    decline = (-_dil(sharesbas, 252)).clip(lower=0)
    base = pur * np.log1p(decline)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepstd63_21d_jerk_v064_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = _std(c, 63)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwamom_21d_jerk_v065_signal(shareswa):
    g = _logchg(shareswa, 126)
    base = g - g.shift(126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_flowvol_21d_jerk_v066_signal(ncfcommon, sharesbas):
    q = ncfcommon.rolling(21, min_periods=10).sum() / sharesbas.replace(0, np.nan)
    base = _std(q, 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_leangap_63d_jerk_v067_signal(sharesbas):
    lo = _rmin(sharesbas, 1260)
    base = np.log(sharesbas.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issmag_63d_jerk_v068_signal(ncfcommon):
    qsum = ncfcommon.rolling(63, min_periods=21).sum()
    base = np.log1p(qsum.clip(lower=0).rolling(504, min_periods=252).mean())
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbasratio_5d_jerk_v069_signal(shareswadil, sharesbas):
    base = shareswadil / sharesbas.replace(0, np.nan) - 1.0
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilsignmag_21d_jerk_v070_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    base = np.sign(g) * (g.abs() ** 0.5)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintensmom_5d_jerk_v071_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    base = raw - raw.shift(63)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creeptrend_21d_jerk_v072_signal(shareswadil, shareswa):
    base = _slopew(_creep(shareswadil, shareswa), 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_warngpos_63d_jerk_v073_signal(shareswa):
    hi = _rmax(shareswa, 1260)
    lo = _rmin(shareswa, 1260)
    base = (shareswa - lo) / (hi - lo).replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_puritymom_63d_jerk_v074_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    base = pur - pur.shift(252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilpressure_21d_jerk_v075_signal(sharesbas, shareswadil, shareswa, ncfcommon):
    dilr = _rank(_logchg(sharesbas, 252), 504)
    creepr = _rank(_creep(shareswadil, shareswa), 504)
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    base = dilr + creepr + 0.5 * pur
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas21_21d_jerk_v076_signal(sharesbas):
    base = _dil(sharesbas, 21)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildil126z_21d_jerk_v077_signal(shareswadil):
    base = _z(_logchg(shareswadil, 126), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepmom126_63d_jerk_v078_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = c - c.shift(126)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbpurity252_63d_jerk_v079_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    base = (-net / gross.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncfz_63d_jerk_v080_signal(ncfcommon):
    q = ncfcommon.rolling(63, min_periods=21).sum()
    base = _z(q, 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countdev504_63d_jerk_v081_signal(sharesbas):
    m = _mean(sharesbas, 504)
    base = _rank(sharesbas / m.replace(0, np.nan), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilspread126_21d_jerk_v082_signal(shareswadil, sharesbas):
    base = _logchg(shareswadil, 126) - _logchg(sharesbas, 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_diler504_63d_jerk_v083_signal(shareswa):
    lg = np.log(shareswa.replace(0, np.nan))
    net = (lg - lg.shift(504)).abs()
    path = lg.diff().abs().rolling(504, min_periods=252).sum()
    base = net / path.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbdisp_63d_jerk_v084_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    base = _std(raw, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilaccel_21d_jerk_v085_signal(sharesbas):
    g = _logchg(sharesbas, 63)
    base = g - g.shift(63)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creeprank_21d_jerk_v086_signal(shareswadil, shareswa):
    base = _rank(_creep(shareswadil, shareswa), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildildisprank_63d_jerk_v087_signal(shareswadil):
    disp = _std(_logchg(shareswadil, 63), 252)
    base = _rank(disp, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_purity504b_21d_jerk_v088_signal(ncfcommon):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    gross = ncfcommon.abs().rolling(504, min_periods=252).sum()
    base = net / gross.replace(0, np.nan)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_belowmax1260_63d_jerk_v089_signal(sharesbas):
    rmax = _rmax(sharesbas, 1260)
    base = np.log(sharesbas.replace(0, np.nan) / rmax.replace(0, np.nan))
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_trendwa_63d_jerk_v090_signal(shareswa):
    base = _slopew(np.log(shareswa.replace(0, np.nan)), 252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbasratiorank1260_21d_jerk_v091_signal(shareswadil, sharesbas):
    r = shareswadil / sharesbas.replace(0, np.nan)
    base = _rank(r, 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_streakbal126_21d_jerk_v092_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    dn = (sharesbas.diff() < 0).astype(float).rolling(126, min_periods=63).mean()
    base = up - dn
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepmomtanh_21d_jerk_v093_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = np.tanh(50.0 * (c - c.shift(126)))
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncf252_63d_jerk_v094_signal(ncfcommon):
    q = ncfcommon.rolling(252, min_periods=126).sum()
    base = np.sign(q) * np.log1p(q.abs())
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepz1260_63d_jerk_v095_signal(shareswadil, shareswa):
    base = _std(_creep(shareswadil, shareswa), 126)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintens_5d_jerk_v096_signal(ncfcommon, shareswa):
    base = (-ncfcommon).rolling(63, min_periods=21).sum() / shareswa.replace(0, np.nan)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilz504_63d_jerk_v097_signal(sharesbas):
    base = _rank(_logchg(sharesbas, 252), 1260)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilimpulse_21d_jerk_v098_signal(shareswa):
    g = _logchg(shareswa, 63)
    base = g - g.ewm(span=252, min_periods=63).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwarank1260_63d_jerk_v099_signal(shareswa):
    base = _rank(_logchg(shareswa, 252), 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_netstance504_63d_jerk_v100_signal(ncfcommon, sharesbas):
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    dil = _logchg(sharesbas, 252)
    base = _z(bb, 504) + _z(dil, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildiltanh_21d_jerk_v101_signal(shareswadil, sharesbas):
    gap = _logchg(shareswadil, 252) - _logchg(sharesbas, 252)
    base = np.tanh(200.0 * gap)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_reductstreak_63d_jerk_v102_signal(sharesbas):
    below = (sharesbas < sharesbas.shift(63)).astype(float)
    base = below.rolling(1260, min_periods=504).mean()
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepconv1260_63d_jerk_v103_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    dev = c - c.rolling(1260, min_periods=504).mean()
    base = np.sign(dev) * (dev ** 2)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_fundmix_63d_jerk_v104_signal(shareswadil, shareswa, ncfcommon, sharesbas):
    creep = _creep(shareswadil, shareswa).abs()
    iss = (ncfcommon.rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)).abs()
    base = creep / (creep + iss + 1e-9) - 0.5
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countrank_21d_jerk_v105_signal(sharesbas):
    detr = sharesbas / _mean(sharesbas, 252).replace(0, np.nan)
    base = _rank(detr, 1260)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwadisp_21d_jerk_v106_signal(shareswa):
    base = _std(_logchg(shareswa, 63), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dualreduct_63d_jerk_v107_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    cash_rank = _rank(-net, 504)
    decline_rank = _rank(-_logchg(sharesbas, 504), 504)
    base = cash_rank * decline_rank
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncfema252_63d_jerk_v108_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    s = q.ewm(span=252, min_periods=84).mean()
    base = np.sign(s) * np.log1p(s.abs())
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_overhangdisp_63d_jerk_v109_signal(shareswadil, sharesbas):
    gap = _logchg(shareswadil, 63) - _logchg(sharesbas, 63)
    base = _std(gap, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countdevwa_63d_jerk_v110_signal(shareswa):
    m = _mean(shareswa, 1260)
    base = shareswa / m.replace(0, np.nan) - 1.0
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilvol504_63d_jerk_v111_signal(sharesbas):
    g = _logchg(sharesbas, 504)
    vol = _std(_logchg(sharesbas, 63), 504)
    base = g / vol.replace(0, np.nan)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildilrank_21d_jerk_v112_signal(shareswadil):
    base = _rank(_logchg(shareswadil, 252), 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbrank1260_63d_jerk_v113_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    base = _rank(raw, 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepchg252_21d_jerk_v114_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = c - c.shift(252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_isspershare_63d_jerk_v115_signal(ncfcommon, sharesbas):
    iss = ncfcommon.rolling(252, min_periods=126).sum()
    cnt_chg = (sharesbas - sharesbas.shift(252)).abs() + 1.0
    base = np.tanh(iss / cnt_chg / 1e3)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilsignpersist_63d_jerk_v116_signal(sharesbas):
    chg = _logchg(sharesbas, 21)
    base = np.sign(chg).rolling(504, min_periods=252).mean()
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dildilgap_5d_jerk_v117_signal(shareswadil, sharesbas):
    base = _logchg(shareswadil, 63) - _logchg(sharesbas, 63)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_purity_5d_jerk_v118_signal(ncfcommon):
    net = ncfcommon.rolling(126, min_periods=63).sum()
    gross = ncfcommon.abs().rolling(126, min_periods=63).sum()
    base = net / gross.replace(0, np.nan)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_countrngpos_5d_jerk_v119_signal(sharesbas):
    hi = _rmax(sharesbas, 504)
    lo = _rmin(sharesbas, 504)
    base = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    b = _d2(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwaz_21d_jerk_v120_signal(shareswa):
    base = _z(_logchg(shareswa, 252), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbimpulse_21d_jerk_v121_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    base = raw - raw.rolling(126, min_periods=63).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbasratio_63d_jerk_v122_signal(shareswadil, sharesbas):
    base = shareswadil / sharesbas.replace(0, np.nan) - 1.0
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilyoy_21d_jerk_v123_signal(shareswa):
    g = _logchg(shareswa, 252)
    base = g - g.rolling(504, min_periods=252).median()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepvsmin_63d_jerk_v124_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = c - c.rolling(504, min_periods=252).median()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_isslife_63d_jerk_v125_signal(ncfcommon):
    net = ncfcommon.rolling(1260, min_periods=504).sum()
    base = np.sign(net) * np.log1p(net.abs())
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilimpulse252_63d_jerk_v126_signal(shareswadil):
    g = _logchg(shareswadil, 252)
    base = np.tanh(15.0 * (g - g.ewm(span=504, min_periods=126).mean()))
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilrankspr_21d_jerk_v127_signal(shareswa, sharesbas):
    rw = _rank(_logchg(shareswa, 252), 504)
    rb = _rank(_logchg(sharesbas, 252), 504)
    base = rw - rb
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbintens63sm_21d_jerk_v128_signal(ncfcommon, sharesbas):
    base = ((-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepmomtanh126_63d_jerk_v129_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    base = np.tanh(50.0 * (c - c.shift(63)))
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_leangaprank_63d_jerk_v130_signal(sharesbas):
    lo = _rmin(sharesbas, 1260)
    gap = np.log(sharesbas.replace(0, np.nan) / lo.replace(0, np.nan))
    base = _rank(gap, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilaccel2_21d_jerk_v131_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    base = (g - g.shift(126)) - (g.shift(126) - g.shift(252))
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbeff_21d_jerk_v132_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    cash_rank = _rank(-net, 504)
    decline_rank = _rank(-_logchg(sharesbas, 504), 504)
    base = cash_rank * decline_rank
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbasratiomom_63d_jerk_v133_signal(shareswadil, sharesbas):
    r = shareswadil / sharesbas.replace(0, np.nan)
    base = r - r.shift(252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_stancetexture_63d_jerk_v134_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    sgn = np.sign(q)
    flips = (sgn != sgn.shift(5)).astype(float).rolling(252, min_periods=126).mean()
    tilt = q.rolling(252, min_periods=126).mean()
    base = flips + np.tanh(tilt / 1e7)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwaaccel_21d_jerk_v135_signal(shareswa):
    g = _logchg(shareswa, 63)
    base = g - g.shift(252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepxdil_21d_jerk_v136_signal(shareswadil, shareswa):
    creep = _creep(shareswadil, shareswa)
    gd = _logchg(shareswadil, 126)
    base = creep * np.sign(gd)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issvsmax_63d_jerk_v137_signal(ncfcommon):
    q = ncfcommon.rolling(252, min_periods=126).sum()
    qmax = _rmax(q, 1260)
    base = np.sign(q - qmax) * np.log1p((qmax - q).abs())
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilasym126_21d_jerk_v138_signal(sharesbas):
    chg = _logchg(sharesbas, 21)
    up = (chg > 0).astype(float).rolling(126, min_periods=63).mean()
    dn = (chg < 0).astype(float).rolling(126, min_periods=63).mean()
    base = up - dn
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepdisp1260_63d_jerk_v139_signal(shareswadil, shareswa):
    base = _std(_creep(shareswadil, shareswa), 1260)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_ncfz1260_21d_jerk_v140_signal(ncfcommon):
    q = ncfcommon.rolling(63, min_periods=21).sum()
    base = _rank(_z(q, 1260), 252)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_realdil_63d_jerk_v141_signal(shareswa, ncfcommon, sharesbas):
    dil = _logchg(shareswa, 252)
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    base = _z(dil, 504) + _z(bb, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_trenddiv_21d_jerk_v142_signal(shareswadil, sharesbas):
    sd = _slopew(np.log(shareswadil.replace(0, np.nan)), 126)
    sb = _slopew(np.log(sharesbas.replace(0, np.nan)), 126)
    base = sd - sb
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_issscale_63d_jerk_v143_signal(ncfcommon, sharesbas):
    mag = ncfcommon.abs().rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    base = _rank(mag, 504)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creepchgrank_21d_jerk_v144_signal(shareswadil, shareswa):
    c = _creep(shareswadil, shareswa)
    chg = c - c.shift(252)
    base = _rank(chg, 504)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_fundmixsm_63d_jerk_v145_signal(shareswadil, shareswa, ncfcommon, sharesbas):
    creep = _creep(shareswadil, shareswa).abs()
    iss = (ncfcommon.rolling(504, min_periods=252).sum() / sharesbas.replace(0, np.nan)).abs()
    base = (creep / (creep + iss + 1e-9) - 0.5).rolling(63, min_periods=21).mean()
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwamom126_63d_jerk_v146_signal(shareswa):
    g = _logchg(shareswa, 126)
    base = g - g.shift(126)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_bbdisp1260_21d_jerk_v147_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    base = _std(raw, 1260)
    b = _d2(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_creeprank252_63d_jerk_v148_signal(shareswadil, shareswa):
    base = _rank(_creep(shareswadil, shareswa), 252)
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilpressure_63d_jerk_v149_signal(sharesbas, shareswadil, shareswa, ncfcommon):
    dilr = _rank(_logchg(sharesbas, 252), 504)
    creepr = _rank(_creep(shareswadil, shareswa), 504)
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    base = dilr + creepr + 0.5 * pur
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_belowmaxsm_63d_jerk_v150_signal(sharesbas):
    rmax = _rmax(sharesbas, 504)
    base = (sharesbas / rmax.replace(0, np.nan) - 1.0).ewm(span=63, min_periods=21).mean()
    b = _d2(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sc_f28_share_count_dynamics_dilbas252_21d_jerk_v001_signal,
    f28sc_f28_share_count_dynamics_dilbas63_5d_jerk_v002_signal,
    f28sc_f28_share_count_dynamics_dilbas126_21d_jerk_v003_signal,
    f28sc_f28_share_count_dynamics_dilwa252_21d_jerk_v004_signal,
    f28sc_f28_share_count_dynamics_dilwa63_5d_jerk_v005_signal,
    f28sc_f28_share_count_dynamics_creep_21d_jerk_v006_signal,
    f28sc_f28_share_count_dynamics_creep_63d_jerk_v007_signal,
    f28sc_f28_share_count_dynamics_dilspread_21d_jerk_v008_signal,
    f28sc_f28_share_count_dynamics_bbintens_21d_jerk_v009_signal,
    f28sc_f28_share_count_dynamics_purity_21d_jerk_v010_signal,
    f28sc_f28_share_count_dynamics_countrngpos_21d_jerk_v011_signal,
    f28sc_f28_share_count_dynamics_dilz_21d_jerk_v012_signal,
    f28sc_f28_share_count_dynamics_dilrank_21d_jerk_v013_signal,
    f28sc_f28_share_count_dynamics_dilstreak_21d_jerk_v014_signal,
    f28sc_f28_share_count_dynamics_baswadiv_21d_jerk_v015_signal,
    f28sc_f28_share_count_dynamics_ncflevel_21d_jerk_v016_signal,
    f28sc_f28_share_count_dynamics_dildildtr_21d_jerk_v017_signal,
    f28sc_f28_share_count_dynamics_creepz_21d_jerk_v018_signal,
    f28sc_f28_share_count_dynamics_bbconsist_21d_jerk_v019_signal,
    f28sc_f28_share_count_dynamics_belowmax_21d_jerk_v020_signal,
    f28sc_f28_share_count_dynamics_creepz504_21d_jerk_v021_signal,
    f28sc_f28_share_count_dynamics_dildisp_63d_jerk_v022_signal,
    f28sc_f28_share_count_dynamics_bbintensz_21d_jerk_v023_signal,
    f28sc_f28_share_count_dynamics_countdev_21d_jerk_v024_signal,
    f28sc_f28_share_count_dynamics_issrate_21d_jerk_v025_signal,
    f28sc_f28_share_count_dynamics_creepmom_21d_jerk_v026_signal,
    f28sc_f28_share_count_dynamics_dilbas21_5d_jerk_v027_signal,
    f28sc_f28_share_count_dynamics_dilwadisp_63d_jerk_v028_signal,
    f28sc_f28_share_count_dynamics_dildilstreak_21d_jerk_v029_signal,
    f28sc_f28_share_count_dynamics_dilasym_21d_jerk_v030_signal,
    f28sc_f28_share_count_dynamics_dilbasratiorank_21d_jerk_v031_signal,
    f28sc_f28_share_count_dynamics_purity504_63d_jerk_v032_signal,
    f28sc_f28_share_count_dynamics_trend_21d_jerk_v033_signal,
    f28sc_f28_share_count_dynamics_creeprngpos_21d_jerk_v034_signal,
    f28sc_f28_share_count_dynamics_bbintens_63d_jerk_v035_signal,
    f28sc_f28_share_count_dynamics_diltanh_21d_jerk_v036_signal,
    f28sc_f28_share_count_dynamics_flowtilt_21d_jerk_v037_signal,
    f28sc_f28_share_count_dynamics_abovemin_21d_jerk_v038_signal,
    f28sc_f28_share_count_dynamics_creepconv_21d_jerk_v039_signal,
    f28sc_f28_share_count_dynamics_dilwarank_21d_jerk_v040_signal,
    f28sc_f28_share_count_dynamics_issscale_21d_jerk_v041_signal,
    f28sc_f28_share_count_dynamics_diler_63d_jerk_v042_signal,
    f28sc_f28_share_count_dynamics_creep_5d_jerk_v043_signal,
    f28sc_f28_share_count_dynamics_dilwa126_21d_jerk_v044_signal,
    f28sc_f28_share_count_dynamics_issaccel_63d_jerk_v045_signal,
    f28sc_f28_share_count_dynamics_overhanglead_21d_jerk_v046_signal,
    f28sc_f28_share_count_dynamics_bblump_21d_jerk_v047_signal,
    f28sc_f28_share_count_dynamics_cumdrag_63d_jerk_v048_signal,
    f28sc_f28_share_count_dynamics_creepema_21d_jerk_v049_signal,
    f28sc_f28_share_count_dynamics_fundmix_21d_jerk_v050_signal,
    f28sc_f28_share_count_dynamics_dilbas252_63d_jerk_v051_signal,
    f28sc_f28_share_count_dynamics_dilwa252_63d_jerk_v052_signal,
    f28sc_f28_share_count_dynamics_netstance_21d_jerk_v053_signal,
    f28sc_f28_share_count_dynamics_creepmom_5d_jerk_v054_signal,
    f28sc_f28_share_count_dynamics_countrngpos1260_63d_jerk_v055_signal,
    f28sc_f28_share_count_dynamics_ncfema_21d_jerk_v056_signal,
    f28sc_f28_share_count_dynamics_dilvol_63d_jerk_v057_signal,
    f28sc_f28_share_count_dynamics_bbrank_21d_jerk_v058_signal,
    f28sc_f28_share_count_dynamics_trenddil_21d_jerk_v059_signal,
    f28sc_f28_share_count_dynamics_creepdisp_63d_jerk_v060_signal,
    f28sc_f28_share_count_dynamics_dilbas504_21d_jerk_v061_signal,
    f28sc_f28_share_count_dynamics_baswadivrank_21d_jerk_v062_signal,
    f28sc_f28_share_count_dynamics_reductqual_63d_jerk_v063_signal,
    f28sc_f28_share_count_dynamics_creepstd63_21d_jerk_v064_signal,
    f28sc_f28_share_count_dynamics_dilwamom_21d_jerk_v065_signal,
    f28sc_f28_share_count_dynamics_flowvol_21d_jerk_v066_signal,
    f28sc_f28_share_count_dynamics_leangap_63d_jerk_v067_signal,
    f28sc_f28_share_count_dynamics_issmag_63d_jerk_v068_signal,
    f28sc_f28_share_count_dynamics_dilbasratio_5d_jerk_v069_signal,
    f28sc_f28_share_count_dynamics_dilsignmag_21d_jerk_v070_signal,
    f28sc_f28_share_count_dynamics_bbintensmom_5d_jerk_v071_signal,
    f28sc_f28_share_count_dynamics_creeptrend_21d_jerk_v072_signal,
    f28sc_f28_share_count_dynamics_warngpos_63d_jerk_v073_signal,
    f28sc_f28_share_count_dynamics_puritymom_63d_jerk_v074_signal,
    f28sc_f28_share_count_dynamics_dilpressure_21d_jerk_v075_signal,
    f28sc_f28_share_count_dynamics_dilbas21_21d_jerk_v076_signal,
    f28sc_f28_share_count_dynamics_dildil126z_21d_jerk_v077_signal,
    f28sc_f28_share_count_dynamics_creepmom126_63d_jerk_v078_signal,
    f28sc_f28_share_count_dynamics_bbpurity252_63d_jerk_v079_signal,
    f28sc_f28_share_count_dynamics_ncfz_63d_jerk_v080_signal,
    f28sc_f28_share_count_dynamics_countdev504_63d_jerk_v081_signal,
    f28sc_f28_share_count_dynamics_dilspread126_21d_jerk_v082_signal,
    f28sc_f28_share_count_dynamics_diler504_63d_jerk_v083_signal,
    f28sc_f28_share_count_dynamics_bbdisp_63d_jerk_v084_signal,
    f28sc_f28_share_count_dynamics_dilaccel_21d_jerk_v085_signal,
    f28sc_f28_share_count_dynamics_creeprank_21d_jerk_v086_signal,
    f28sc_f28_share_count_dynamics_dildildisprank_63d_jerk_v087_signal,
    f28sc_f28_share_count_dynamics_purity504b_21d_jerk_v088_signal,
    f28sc_f28_share_count_dynamics_belowmax1260_63d_jerk_v089_signal,
    f28sc_f28_share_count_dynamics_trendwa_63d_jerk_v090_signal,
    f28sc_f28_share_count_dynamics_dilbasratiorank1260_21d_jerk_v091_signal,
    f28sc_f28_share_count_dynamics_streakbal126_21d_jerk_v092_signal,
    f28sc_f28_share_count_dynamics_creepmomtanh_21d_jerk_v093_signal,
    f28sc_f28_share_count_dynamics_ncf252_63d_jerk_v094_signal,
    f28sc_f28_share_count_dynamics_creepz1260_63d_jerk_v095_signal,
    f28sc_f28_share_count_dynamics_bbintens_5d_jerk_v096_signal,
    f28sc_f28_share_count_dynamics_dilz504_63d_jerk_v097_signal,
    f28sc_f28_share_count_dynamics_dilimpulse_21d_jerk_v098_signal,
    f28sc_f28_share_count_dynamics_dilwarank1260_63d_jerk_v099_signal,
    f28sc_f28_share_count_dynamics_netstance504_63d_jerk_v100_signal,
    f28sc_f28_share_count_dynamics_dildiltanh_21d_jerk_v101_signal,
    f28sc_f28_share_count_dynamics_reductstreak_63d_jerk_v102_signal,
    f28sc_f28_share_count_dynamics_creepconv1260_63d_jerk_v103_signal,
    f28sc_f28_share_count_dynamics_fundmix_63d_jerk_v104_signal,
    f28sc_f28_share_count_dynamics_countrank_21d_jerk_v105_signal,
    f28sc_f28_share_count_dynamics_dilwadisp_21d_jerk_v106_signal,
    f28sc_f28_share_count_dynamics_dualreduct_63d_jerk_v107_signal,
    f28sc_f28_share_count_dynamics_ncfema252_63d_jerk_v108_signal,
    f28sc_f28_share_count_dynamics_overhangdisp_63d_jerk_v109_signal,
    f28sc_f28_share_count_dynamics_countdevwa_63d_jerk_v110_signal,
    f28sc_f28_share_count_dynamics_dilvol504_63d_jerk_v111_signal,
    f28sc_f28_share_count_dynamics_dildilrank_21d_jerk_v112_signal,
    f28sc_f28_share_count_dynamics_bbrank1260_63d_jerk_v113_signal,
    f28sc_f28_share_count_dynamics_creepchg252_21d_jerk_v114_signal,
    f28sc_f28_share_count_dynamics_isspershare_63d_jerk_v115_signal,
    f28sc_f28_share_count_dynamics_dilsignpersist_63d_jerk_v116_signal,
    f28sc_f28_share_count_dynamics_dildilgap_5d_jerk_v117_signal,
    f28sc_f28_share_count_dynamics_purity_5d_jerk_v118_signal,
    f28sc_f28_share_count_dynamics_countrngpos_5d_jerk_v119_signal,
    f28sc_f28_share_count_dynamics_dilwaz_21d_jerk_v120_signal,
    f28sc_f28_share_count_dynamics_bbimpulse_21d_jerk_v121_signal,
    f28sc_f28_share_count_dynamics_dilbasratio_63d_jerk_v122_signal,
    f28sc_f28_share_count_dynamics_dilyoy_21d_jerk_v123_signal,
    f28sc_f28_share_count_dynamics_creepvsmin_63d_jerk_v124_signal,
    f28sc_f28_share_count_dynamics_isslife_63d_jerk_v125_signal,
    f28sc_f28_share_count_dynamics_dilimpulse252_63d_jerk_v126_signal,
    f28sc_f28_share_count_dynamics_dilrankspr_21d_jerk_v127_signal,
    f28sc_f28_share_count_dynamics_bbintens63sm_21d_jerk_v128_signal,
    f28sc_f28_share_count_dynamics_creepmomtanh126_63d_jerk_v129_signal,
    f28sc_f28_share_count_dynamics_leangaprank_63d_jerk_v130_signal,
    f28sc_f28_share_count_dynamics_dilaccel2_21d_jerk_v131_signal,
    f28sc_f28_share_count_dynamics_bbeff_21d_jerk_v132_signal,
    f28sc_f28_share_count_dynamics_dilbasratiomom_63d_jerk_v133_signal,
    f28sc_f28_share_count_dynamics_stancetexture_63d_jerk_v134_signal,
    f28sc_f28_share_count_dynamics_dilwaaccel_21d_jerk_v135_signal,
    f28sc_f28_share_count_dynamics_creepxdil_21d_jerk_v136_signal,
    f28sc_f28_share_count_dynamics_issvsmax_63d_jerk_v137_signal,
    f28sc_f28_share_count_dynamics_dilasym126_21d_jerk_v138_signal,
    f28sc_f28_share_count_dynamics_creepdisp1260_63d_jerk_v139_signal,
    f28sc_f28_share_count_dynamics_ncfz1260_21d_jerk_v140_signal,
    f28sc_f28_share_count_dynamics_realdil_63d_jerk_v141_signal,
    f28sc_f28_share_count_dynamics_trenddiv_21d_jerk_v142_signal,
    f28sc_f28_share_count_dynamics_issscale_63d_jerk_v143_signal,
    f28sc_f28_share_count_dynamics_creepchgrank_21d_jerk_v144_signal,
    f28sc_f28_share_count_dynamics_fundmixsm_63d_jerk_v145_signal,
    f28sc_f28_share_count_dynamics_dilwamom126_63d_jerk_v146_signal,
    f28sc_f28_share_count_dynamics_bbdisp1260_21d_jerk_v147_signal,
    f28sc_f28_share_count_dynamics_creeprank252_63d_jerk_v148_signal,
    f28sc_f28_share_count_dynamics_dilpressure_63d_jerk_v149_signal,
    f28sc_f28_share_count_dynamics_belowmaxsm_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SHARE_COUNT_DYNAMICS_REGISTRY_3RD_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    sharesbas = _fund(101, base=5e8, drift=0.015, vol=0.04).rename("sharesbas")
    shareswa = _fund(102, base=4.9e8, drift=0.015, vol=0.04).rename("shareswa")
    _overhang = _fund(103, base=1.0, drift=0.01, vol=0.06).values
    shareswadil = (shareswa * (1.0 + 0.02 + 0.06 * np.clip(_overhang / _overhang[0] - 1.0, -0.5, None))).rename("shareswadil")
    _ncf_rng = np.random.default_rng(104)
    _ncf_steps = np.repeat(_ncf_rng.normal(0.0, 1.0, n // 63 + 1), 63)[:n]
    ncfcommon = pd.Series(_ncf_steps * 5e6 + _fund(105, base=1e6, drift=0.0, vol=0.4, allow_neg=True).values,
                          name="ncfcommon")

    cols = {"sharesbas": sharesbas, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon}

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

    print("OK f28_share_count_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
