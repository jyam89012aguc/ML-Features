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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _slope(s, w):
    # ordinary-least-squares slope of s over a trailing window, per step
    def _f(a):
        n = len(a)
        x = np.arange(n, dtype=float)
        xm = x.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        ym = a.mean()
        return ((x - xm) * (a - ym)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _streak_up(s):
    # length of current consecutive positive-change run, vectorized
    d = (s.diff() > 0).astype(float)
    grp = (d == 0).cumsum()
    return d.groupby(grp).cumsum()


def _streak_dn(s):
    d = (s.diff() < 0).astype(float)
    grp = (d == 0).cumsum()
    return d.groupby(grp).cumsum()


# ===== ownership / smart-money domain primitives (sf3b investor-level) =====
def _f44_conviction(shrvalue, totalvalue):
    # share of the investor's portfolio value in this position
    return shrvalue / totalvalue.replace(0, np.nan)


def _f44_pos_change(shrholdings, w):
    # fractional change in reported share holdings (13F position delta)
    return shrholdings / shrholdings.shift(w).replace(0, np.nan) - 1.0


def _f44_value_per_unit(shrvalue, shrunits):
    # implied price/value per reported unit
    return shrvalue / shrunits.replace(0, np.nan)


def _f44_accum(shrholdings, shrvalue, totalvalue, w):
    # value-weighted accumulation: position growth weighted by conviction
    pc = shrholdings / shrholdings.shift(w).replace(0, np.nan) - 1.0
    conv = shrvalue / totalvalue.replace(0, np.nan)
    return pc * conv


def _f44_build_streak(shrholdings):
    return _streak_up(shrholdings)


def _f44_trim_streak(shrholdings):
    return _streak_dn(shrholdings)


def f44sm_f44_smart_money_flow_poschg_5d_base_v001_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_21d_base_v002_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_63d_base_v003_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_126d_base_v004_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_252d_base_v005_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posemagap_21d_base_v006_signal(shrholdings):
    ema = shrholdings.ewm(span=21, min_periods=10).mean()
    b = shrholdings / ema.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posimpulse_63d_base_v007_signal(shrholdings):
    f = shrholdings.pct_change(5)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmedgap_126d_base_v008_signal(shrholdings):
    med = shrholdings.rolling(126, min_periods=63).median()
    b = shrholdings / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_63d_base_v009_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_126d_base_v010_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_252d_base_v011_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrank_126d_base_v012_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv - conv.shift(21)
    b = dc.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrank_252d_base_v013_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv - conv.shift(21)
    b = dc.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_21d_base_v014_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(21)
    pc = _f44_pos_change(shrholdings, 21)
    b = np.sign(dconv) * pc.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_63d_base_v015_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(63)
    pc = _f44_pos_change(shrholdings, 63)
    b = np.sign(dconv) * pc.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_126d_base_v016_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(126)
    pc = _f44_pos_change(shrholdings, 126)
    b = np.sign(dconv) * pc.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_252d_base_v017_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(252)
    pc = _f44_pos_change(shrholdings, 252)
    b = np.sign(dconv) * pc.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildstreak_0d_base_v018_signal(shrholdings):
    st = _f44_build_streak(shrholdings)
    mag = shrholdings.pct_change().clip(lower=0)
    b = st * mag.rolling(5, min_periods=1).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimstreak_0d_base_v019_signal(shrholdings):
    st = _f44_trim_streak(shrholdings)
    mag = (-shrholdings.pct_change()).clip(lower=0)
    b = st * mag.rolling(5, min_periods=1).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_netstreak_21d_base_v020_signal(shrholdings):
    bs = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    mag = shrholdings.pct_change().abs().rolling(5, min_periods=1).mean()
    b = (bs * mag).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_63d_base_v021_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(63, min_periods=31).mean()
    up = (ex.clip(lower=0) ** 2).rolling(63, min_periods=31).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(63, min_periods=31).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_126d_base_v022_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(126, min_periods=63).mean()
    up = (ex.clip(lower=0) ** 2).rolling(126, min_periods=63).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_252d_base_v023_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(252, min_periods=126).mean()
    up = (ex.clip(lower=0) ** 2).rolling(252, min_periods=126).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuz_63d_base_v024_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuz_252d_base_v025_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_21d_base_v026_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_63d_base_v027_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_126d_base_v028_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_21d_base_v029_signal(shrvalue):
    b = _roc(shrvalue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_63d_base_v030_signal(shrvalue):
    b = _roc(shrvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_126d_base_v031_signal(shrvalue):
    b = _roc(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_252d_base_v032_signal(shrvalue):
    b = _roc(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvsqty_63d_base_v033_signal(shrvalue, shrholdings):
    b = _roc(shrvalue, 63) - _roc(shrholdings, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvsqty_126d_base_v034_signal(shrvalue, shrholdings):
    b = _roc(shrvalue, 126) - _roc(shrholdings, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_portwtvol_126d_base_v035_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _std(wt, 126) / _mean(wt, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_portwtvol_252d_base_v036_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _std(wt, 252) / _mean(wt, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posslope_63d_base_v037_signal(shrholdings):
    norm = shrholdings / _mean(shrholdings, 63).replace(0, np.nan)
    b = _slope(norm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posslope_126d_base_v038_signal(shrholdings):
    norm = shrholdings / _mean(shrholdings, 126).replace(0, np.nan)
    b = _slope(norm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convtrend_63d_base_v039_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convtrend_126d_base_v040_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshbuild_126d_base_v041_signal(shrholdings):
    lo = _rmin(shrholdings, 126)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshbuild_252d_base_v042_signal(shrholdings):
    lo = _rmin(shrholdings, 252)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimpeak_126d_base_v043_signal(shrholdings):
    hi = _rmax(shrholdings, 126)
    b = shrholdings / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimpeak_252d_base_v044_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    b = shrholdings / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posrng_126d_base_v045_signal(shrholdings):
    hi = _rmax(shrholdings, 126)
    lo = _rmin(shrholdings, 126)
    b = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posrng_252d_base_v046_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    lo = _rmin(shrholdings, 252)
    b = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convmom_63d_base_v047_signal(shrholdings, shrvalue, totalvalue):
    pc = _roc(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(126, min_periods=63).rank(pct=True) - 0.5
    pr = pc.rolling(126, min_periods=63).rank(pct=True) - 0.5
    b = cr * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convmom_126d_base_v048_signal(shrholdings, shrvalue, totalvalue):
    pc = _roc(shrholdings, 126)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    pr = pc.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = cr * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumz_126d_base_v049_signal(shrholdings, shrvalue, totalvalue):
    a = _f44_accum(shrholdings, shrvalue, totalvalue, 63)
    b = _z(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_63d_base_v050_signal(shrunits):
    b = _roc(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_126d_base_v051_signal(shrunits):
    b = _roc(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_252d_base_v052_signal(shrunits):
    b = _roc(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_hpuz_63d_base_v053_signal(shrholdings, shrunits):
    r = shrholdings / shrunits.replace(0, np.nan)
    b = _z(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_hpuz_252d_base_v054_signal(shrholdings, shrunits):
    r = shrholdings / shrunits.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convextreme_252d_base_v055_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    hi = _rmax(conv, 252)
    lo = _rmin(conv, 252)
    rp = (conv - lo) / (hi - lo).replace(0, np.nan)
    top = (rp >= 0.6667).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschgyoy_63d_base_v056_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 63)
    b = pc - pc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschgyoy_126d_base_v057_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 126)
    b = pc - pc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convdownvol_126d_base_v058_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    downsq = (dc.clip(upper=0) ** 2).rolling(126, min_periods=63).mean()
    b = np.sqrt(downsq) / _mean(conv, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convdownvol_252d_base_v059_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    downsq = (dc.clip(upper=0) ** 2).rolling(252, min_periods=126).mean()
    b = np.sqrt(downsq) / _mean(conv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowvol_126d_base_v060_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _std(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowvol_252d_base_v061_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _std(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_riskadjaccum_126d_base_v062_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomrank_252d_base_v063_signal(shrvalue):
    m = _roc(shrvalue, 63)
    b = m.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posvarratio_63d_base_v064_signal(shrholdings):
    r = np.log(shrholdings.replace(0, np.nan)).diff()
    vk = _std(r.rolling(5).sum(), 63) ** 2
    v1 = _std(r, 63) ** 2
    b = vk / (5 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posvarratio_126d_base_v065_signal(shrholdings):
    r = np.log(shrholdings.replace(0, np.nan)).diff()
    vk = _std(r.rolling(10).sum(), 126) ** 2
    v1 = _std(r, 126) ** 2
    b = vk / (10 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreak_126d_base_v066_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    prior = conv.shift(1).rolling(126, min_periods=63).max()
    b = conv / prior.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreak_252d_base_v067_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    prior = conv.shift(1).rolling(252, min_periods=126).max()
    b = conv / prior.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwdrift_126d_base_v068_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    d1 = wt - wt.shift(42)
    b = d1 - d1.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildpersist_126d_base_v069_signal(shrholdings):
    ns = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    sm = ns.ewm(span=21, min_periods=10).mean()
    b = sm / _std(ns, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildpersist_252d_base_v070_signal(shrholdings):
    ns = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    sm = ns.ewm(span=42, min_periods=21).mean()
    b = sm / _std(ns, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowtanh_63d_base_v071_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    chg = conv - conv.shift(63)
    b = np.tanh(8.0 * chg / _std(conv, 126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convsize_126d_base_v072_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(126, min_periods=63).rank(pct=True)
    sr = shrholdings.rolling(126, min_periods=63).rank(pct=True)
    b = (cr - sr).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpudiverge_126d_base_v073_signal(shrvalue, shrunits, shrholdings):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 126) - _roc(shrholdings, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valinflect_126d_base_v074_signal(shrvalue):
    m = _roc(shrvalue, 63)
    sm = np.sign(m) * m.abs() ** 0.5
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumbreadth_0d_base_v075_signal(shrholdings):
    p1 = _f44_pos_change(shrholdings, 21)
    p2 = _f44_pos_change(shrholdings, 63)
    p3 = _f44_pos_change(shrholdings, 126)
    b = pd.concat([p1, p2, p3], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f44sm_f44_smart_money_flow_poschg_5d_base_v001_signal,
    f44sm_f44_smart_money_flow_poschg_21d_base_v002_signal,
    f44sm_f44_smart_money_flow_poschg_63d_base_v003_signal,
    f44sm_f44_smart_money_flow_poschg_126d_base_v004_signal,
    f44sm_f44_smart_money_flow_poschg_252d_base_v005_signal,
    f44sm_f44_smart_money_flow_posemagap_21d_base_v006_signal,
    f44sm_f44_smart_money_flow_posimpulse_63d_base_v007_signal,
    f44sm_f44_smart_money_flow_posmedgap_126d_base_v008_signal,
    f44sm_f44_smart_money_flow_convz_63d_base_v009_signal,
    f44sm_f44_smart_money_flow_convz_126d_base_v010_signal,
    f44sm_f44_smart_money_flow_convz_252d_base_v011_signal,
    f44sm_f44_smart_money_flow_convrank_126d_base_v012_signal,
    f44sm_f44_smart_money_flow_convrank_252d_base_v013_signal,
    f44sm_f44_smart_money_flow_accum_21d_base_v014_signal,
    f44sm_f44_smart_money_flow_accum_63d_base_v015_signal,
    f44sm_f44_smart_money_flow_accum_126d_base_v016_signal,
    f44sm_f44_smart_money_flow_accum_252d_base_v017_signal,
    f44sm_f44_smart_money_flow_buildstreak_0d_base_v018_signal,
    f44sm_f44_smart_money_flow_trimstreak_0d_base_v019_signal,
    f44sm_f44_smart_money_flow_netstreak_21d_base_v020_signal,
    f44sm_f44_smart_money_flow_accumhit_63d_base_v021_signal,
    f44sm_f44_smart_money_flow_accumhit_126d_base_v022_signal,
    f44sm_f44_smart_money_flow_accumhit_252d_base_v023_signal,
    f44sm_f44_smart_money_flow_vpuz_63d_base_v024_signal,
    f44sm_f44_smart_money_flow_vpuz_252d_base_v025_signal,
    f44sm_f44_smart_money_flow_vpumom_21d_base_v026_signal,
    f44sm_f44_smart_money_flow_vpumom_63d_base_v027_signal,
    f44sm_f44_smart_money_flow_vpumom_126d_base_v028_signal,
    f44sm_f44_smart_money_flow_valmom_21d_base_v029_signal,
    f44sm_f44_smart_money_flow_valmom_63d_base_v030_signal,
    f44sm_f44_smart_money_flow_valmom_126d_base_v031_signal,
    f44sm_f44_smart_money_flow_valmom_252d_base_v032_signal,
    f44sm_f44_smart_money_flow_valvsqty_63d_base_v033_signal,
    f44sm_f44_smart_money_flow_valvsqty_126d_base_v034_signal,
    f44sm_f44_smart_money_flow_portwtvol_126d_base_v035_signal,
    f44sm_f44_smart_money_flow_portwtvol_252d_base_v036_signal,
    f44sm_f44_smart_money_flow_posslope_63d_base_v037_signal,
    f44sm_f44_smart_money_flow_posslope_126d_base_v038_signal,
    f44sm_f44_smart_money_flow_convtrend_63d_base_v039_signal,
    f44sm_f44_smart_money_flow_convtrend_126d_base_v040_signal,
    f44sm_f44_smart_money_flow_freshbuild_126d_base_v041_signal,
    f44sm_f44_smart_money_flow_freshbuild_252d_base_v042_signal,
    f44sm_f44_smart_money_flow_trimpeak_126d_base_v043_signal,
    f44sm_f44_smart_money_flow_trimpeak_252d_base_v044_signal,
    f44sm_f44_smart_money_flow_posrng_126d_base_v045_signal,
    f44sm_f44_smart_money_flow_posrng_252d_base_v046_signal,
    f44sm_f44_smart_money_flow_convmom_63d_base_v047_signal,
    f44sm_f44_smart_money_flow_convmom_126d_base_v048_signal,
    f44sm_f44_smart_money_flow_accumz_126d_base_v049_signal,
    f44sm_f44_smart_money_flow_unitgrow_63d_base_v050_signal,
    f44sm_f44_smart_money_flow_unitgrow_126d_base_v051_signal,
    f44sm_f44_smart_money_flow_unitgrow_252d_base_v052_signal,
    f44sm_f44_smart_money_flow_hpuz_63d_base_v053_signal,
    f44sm_f44_smart_money_flow_hpuz_252d_base_v054_signal,
    f44sm_f44_smart_money_flow_convextreme_252d_base_v055_signal,
    f44sm_f44_smart_money_flow_poschgyoy_63d_base_v056_signal,
    f44sm_f44_smart_money_flow_poschgyoy_126d_base_v057_signal,
    f44sm_f44_smart_money_flow_convdownvol_126d_base_v058_signal,
    f44sm_f44_smart_money_flow_convdownvol_252d_base_v059_signal,
    f44sm_f44_smart_money_flow_flowvol_126d_base_v060_signal,
    f44sm_f44_smart_money_flow_flowvol_252d_base_v061_signal,
    f44sm_f44_smart_money_flow_riskadjaccum_126d_base_v062_signal,
    f44sm_f44_smart_money_flow_valmomrank_252d_base_v063_signal,
    f44sm_f44_smart_money_flow_posvarratio_63d_base_v064_signal,
    f44sm_f44_smart_money_flow_posvarratio_126d_base_v065_signal,
    f44sm_f44_smart_money_flow_convbreak_126d_base_v066_signal,
    f44sm_f44_smart_money_flow_convbreak_252d_base_v067_signal,
    f44sm_f44_smart_money_flow_vwdrift_126d_base_v068_signal,
    f44sm_f44_smart_money_flow_buildpersist_126d_base_v069_signal,
    f44sm_f44_smart_money_flow_buildpersist_252d_base_v070_signal,
    f44sm_f44_smart_money_flow_flowtanh_63d_base_v071_signal,
    f44sm_f44_smart_money_flow_convsize_126d_base_v072_signal,
    f44sm_f44_smart_money_flow_vpudiverge_126d_base_v073_signal,
    f44sm_f44_smart_money_flow_valinflect_126d_base_v074_signal,
    f44sm_f44_smart_money_flow_accumbreadth_0d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_SMART_MONEY_FLOW_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, daily=0.0):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if daily > 0:
            # mild positive-preserving daily wobble so within-quarter flow,
            # streak and rank features carry independent structure.
            s = s * np.exp(g.normal(0.0, daily, n))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    # ownership columns (sf3b investor-level) -- all positive, with trend so
    # position-change / streak features vary across the series.
    shrholdings = _fund(101, base=5.0e5, drift=0.03, vol=0.06, daily=0.020).rename("shrholdings")
    shrunits = _fund(202, base=5.0e5, drift=0.03, vol=0.05, daily=0.016).rename("shrunits")
    shrvalue = _fund(303, base=2.0e7, drift=0.025, vol=0.07, daily=0.028).rename("shrvalue")
    totalvalue = _fund(404, base=5.0e8, drift=0.02, vol=0.04, daily=0.022).rename("totalvalue")

    cols = {
        "shrholdings": shrholdings,
        "shrunits": shrunits,
        "shrvalue": shrvalue,
        "totalvalue": totalvalue,
    }

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

    print("OK f44_smart_money_flow_base_001_075_claude: %d features pass" % n_features)
