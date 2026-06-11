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


def f44sm_f44_smart_money_flow_poschg_5d_slope_v001_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 5)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_21d_slope_v002_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 21)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_63d_slope_v003_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_126d_slope_v004_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschg_252d_slope_v005_signal(shrholdings):
    b = _f44_pos_change(shrholdings, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posemagap_21d_slope_v006_signal(shrholdings):
    ema = shrholdings.ewm(span=21, min_periods=10).mean()
    b = shrholdings / ema.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posimpulse_63d_slope_v007_signal(shrholdings):
    f = shrholdings.pct_change(5)
    b = f - f.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmedgap_126d_slope_v008_signal(shrholdings):
    med = shrholdings.rolling(126, min_periods=63).median()
    b = shrholdings / med.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_63d_slope_v009_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_126d_slope_v010_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convz_252d_slope_v011_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _z(conv, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrank_126d_slope_v012_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv - conv.shift(21)
    b = dc.rolling(126, min_periods=63).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrank_252d_slope_v013_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv - conv.shift(21)
    b = dc.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_21d_slope_v014_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(21)
    pc = _f44_pos_change(shrholdings, 21)
    b = np.sign(dconv) * pc.abs()
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_63d_slope_v015_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(63)
    pc = _f44_pos_change(shrholdings, 63)
    b = np.sign(dconv) * pc.abs()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_126d_slope_v016_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(126)
    pc = _f44_pos_change(shrholdings, 126)
    b = np.sign(dconv) * pc.abs()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accum_252d_slope_v017_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dconv = conv - conv.shift(252)
    pc = _f44_pos_change(shrholdings, 252)
    b = np.sign(dconv) * pc.abs()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildstreak_0d_slope_v018_signal(shrholdings):
    st = _f44_build_streak(shrholdings)
    mag = shrholdings.pct_change().clip(lower=0)
    b = st * mag.rolling(5, min_periods=1).mean()
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimstreak_0d_slope_v019_signal(shrholdings):
    st = _f44_trim_streak(shrholdings)
    mag = (-shrholdings.pct_change()).clip(lower=0)
    b = st * mag.rolling(5, min_periods=1).mean()
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_netstreak_21d_slope_v020_signal(shrholdings):
    bs = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    mag = shrholdings.pct_change().abs().rolling(5, min_periods=1).mean()
    b = (bs * mag).rolling(21, min_periods=10).mean()
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_63d_slope_v021_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(63, min_periods=31).mean()
    up = (ex.clip(lower=0) ** 2).rolling(63, min_periods=31).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(63, min_periods=31).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_126d_slope_v022_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(126, min_periods=63).mean()
    up = (ex.clip(lower=0) ** 2).rolling(126, min_periods=63).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumhit_252d_slope_v023_signal(shrholdings):
    d = shrholdings.pct_change()
    ex = d - d.rolling(252, min_periods=126).mean()
    up = (ex.clip(lower=0) ** 2).rolling(252, min_periods=126).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuz_63d_slope_v024_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuz_252d_slope_v025_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_21d_slope_v026_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 21)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_63d_slope_v027_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpumom_126d_slope_v028_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_21d_slope_v029_signal(shrvalue):
    b = _roc(shrvalue, 21)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_63d_slope_v030_signal(shrvalue):
    b = _roc(shrvalue, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_126d_slope_v031_signal(shrvalue):
    b = _roc(shrvalue, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom_252d_slope_v032_signal(shrvalue):
    b = _roc(shrvalue, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvsqty_63d_slope_v033_signal(shrvalue, shrholdings):
    b = _roc(shrvalue, 63) - _roc(shrholdings, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvsqty_126d_slope_v034_signal(shrvalue, shrholdings):
    b = _roc(shrvalue, 126) - _roc(shrholdings, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_portwtvol_126d_slope_v035_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _std(wt, 126) / _mean(wt, 126).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_portwtvol_252d_slope_v036_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _std(wt, 252) / _mean(wt, 252).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posslope_63d_slope_v037_signal(shrholdings):
    norm = shrholdings / _mean(shrholdings, 63).replace(0, np.nan)
    b = _slope(norm, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posslope_126d_slope_v038_signal(shrholdings):
    norm = shrholdings / _mean(shrholdings, 126).replace(0, np.nan)
    b = _slope(norm, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convtrend_63d_slope_v039_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convtrend_126d_slope_v040_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshbuild_126d_slope_v041_signal(shrholdings):
    lo = _rmin(shrholdings, 126)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshbuild_252d_slope_v042_signal(shrholdings):
    lo = _rmin(shrholdings, 252)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimpeak_126d_slope_v043_signal(shrholdings):
    hi = _rmax(shrholdings, 126)
    b = shrholdings / hi.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_trimpeak_252d_slope_v044_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    b = shrholdings / hi.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posrng_126d_slope_v045_signal(shrholdings):
    hi = _rmax(shrholdings, 126)
    lo = _rmin(shrholdings, 126)
    b = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posrng_252d_slope_v046_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    lo = _rmin(shrholdings, 252)
    b = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convmom_63d_slope_v047_signal(shrholdings, shrvalue, totalvalue):
    pc = _roc(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(126, min_periods=63).rank(pct=True) - 0.5
    pr = pc.rolling(126, min_periods=63).rank(pct=True) - 0.5
    b = cr * pr
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convmom_126d_slope_v048_signal(shrholdings, shrvalue, totalvalue):
    pc = _roc(shrholdings, 126)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    pr = pc.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = cr * pr
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumz_126d_slope_v049_signal(shrholdings, shrvalue, totalvalue):
    a = _f44_accum(shrholdings, shrvalue, totalvalue, 63)
    b = _z(a, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_63d_slope_v050_signal(shrunits):
    b = _roc(shrunits, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_126d_slope_v051_signal(shrunits):
    b = _roc(shrunits, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitgrow_252d_slope_v052_signal(shrunits):
    b = _roc(shrunits, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_hpuz_63d_slope_v053_signal(shrholdings, shrunits):
    r = shrholdings / shrunits.replace(0, np.nan)
    b = _z(r, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_hpuz_252d_slope_v054_signal(shrholdings, shrunits):
    r = shrholdings / shrunits.replace(0, np.nan)
    b = _z(r, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convextreme_252d_slope_v055_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    hi = _rmax(conv, 252)
    lo = _rmin(conv, 252)
    rp = (conv - lo) / (hi - lo).replace(0, np.nan)
    top = (rp >= 0.6667).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschgyoy_63d_slope_v056_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 63)
    b = pc - pc.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poschgyoy_126d_slope_v057_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 126)
    b = pc - pc.shift(126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convdownvol_126d_slope_v058_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    downsq = (dc.clip(upper=0) ** 2).rolling(126, min_periods=63).mean()
    b = np.sqrt(downsq) / _mean(conv, 126).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convdownvol_252d_slope_v059_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    downsq = (dc.clip(upper=0) ** 2).rolling(252, min_periods=126).mean()
    b = np.sqrt(downsq) / _mean(conv, 252).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowvol_126d_slope_v060_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _std(d, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowvol_252d_slope_v061_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _std(d, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_riskadjaccum_126d_slope_v062_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(126, min_periods=63).kurt()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomrank_252d_slope_v063_signal(shrvalue):
    m = _roc(shrvalue, 63)
    b = m.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posvarratio_63d_slope_v064_signal(shrholdings):
    r = np.log(shrholdings.replace(0, np.nan)).diff()
    vk = _std(r.rolling(5).sum(), 63) ** 2
    v1 = _std(r, 63) ** 2
    b = vk / (5 * v1).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posvarratio_126d_slope_v065_signal(shrholdings):
    r = np.log(shrholdings.replace(0, np.nan)).diff()
    vk = _std(r.rolling(10).sum(), 126) ** 2
    v1 = _std(r, 126) ** 2
    b = vk / (10 * v1).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreak_126d_slope_v066_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    prior = conv.shift(1).rolling(126, min_periods=63).max()
    b = conv / prior.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreak_252d_slope_v067_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    prior = conv.shift(1).rolling(252, min_periods=126).max()
    b = conv / prior.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwdrift_126d_slope_v068_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    d1 = wt - wt.shift(42)
    b = d1 - d1.shift(42)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildpersist_126d_slope_v069_signal(shrholdings):
    ns = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    sm = ns.ewm(span=21, min_periods=10).mean()
    b = sm / _std(ns, 126).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_buildpersist_252d_slope_v070_signal(shrholdings):
    ns = (_f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)).astype(float)
    sm = ns.ewm(span=42, min_periods=21).mean()
    b = sm / _std(ns, 252).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowtanh_63d_slope_v071_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    chg = conv - conv.shift(63)
    b = np.tanh(8.0 * chg / _std(conv, 126).replace(0, np.nan))
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convsize_126d_slope_v072_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(126, min_periods=63).rank(pct=True)
    sr = shrholdings.rolling(126, min_periods=63).rank(pct=True)
    b = (cr - sr).rolling(21, min_periods=10).mean()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpudiverge_126d_slope_v073_signal(shrvalue, shrunits, shrholdings):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _roc(vpu, 126) - _roc(shrholdings, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valinflect_126d_slope_v074_signal(shrvalue):
    m = _roc(shrvalue, 63)
    sm = np.sign(m) * m.abs() ** 0.5
    b = sm - sm.shift(126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumbreadth_0d_slope_v075_signal(shrholdings):
    p1 = _f44_pos_change(shrholdings, 21)
    p2 = _f44_pos_change(shrholdings, 63)
    p3 = _f44_pos_change(shrholdings, 126)
    b = pd.concat([p1, p2, p3], axis=1).mean(axis=1)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumdisp_0d_slope_v076_signal(shrholdings):
    p1 = _f44_pos_change(shrholdings, 21)
    p2 = _f44_pos_change(shrholdings, 63)
    p3 = _f44_pos_change(shrholdings, 126)
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convaccel_126d_slope_v077_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    ch = conv - conv.shift(21)
    b = ch - ch.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convramphit_63d_slope_v078_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    ex = dc - dc.rolling(63, min_periods=32).mean()
    up = (ex.clip(lower=0) ** 2).rolling(63, min_periods=32).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(63, min_periods=32).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posz_126d_slope_v079_signal(shrholdings):
    b = _z(shrholdings, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posz_252d_slope_v080_signal(shrholdings):
    b = _z(shrholdings, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtmom_63d_slope_v081_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _roc(wt, 63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtmom_126d_slope_v082_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _roc(wt, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumeff_126d_slope_v083_signal(shrholdings):
    d = shrholdings.pct_change()
    vshort = _std(d, 21)
    vlong = _std(d, 126)
    b = vshort / vlong.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumeff_252d_slope_v084_signal(shrholdings):
    d = shrholdings.pct_change()
    vshort = _std(d, 21)
    vlong = _std(d, 252)
    b = vshort / vlong.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitdiverge_126d_slope_v085_signal(shrunits, shrholdings):
    b = _roc(shrunits, 126) - _roc(shrholdings, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convregime_252d_slope_v086_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    med = conv.rolling(252, min_periods=126).median()
    above = (conv > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowskew_126d_slope_v087_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(126, min_periods=63).skew()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowskew_252d_slope_v088_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(252, min_periods=126).skew()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshconv_252d_slope_v089_signal(shrholdings, shrvalue, totalvalue):
    hi = _rmax(shrholdings, 252)
    lo = _rmin(shrholdings, 252)
    rp = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    conv = _f44_conviction(shrvalue, totalvalue)
    chi = _rmax(conv, 252)
    clo = _rmin(conv, 252)
    crp = (conv - clo) / (chi - clo).replace(0, np.nan)
    b = rp - crp
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomadj_126d_slope_v090_signal(shrvalue):
    r = shrvalue.pct_change(21)
    b = r.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posuw_252d_slope_v091_signal(shrholdings):
    peak = _rmax(shrholdings, 252)
    uw = shrholdings / peak.replace(0, np.nan) - 1.0
    deep = (uw <= -0.10).astype(float)
    b = deep.rolling(252, min_periods=126).mean()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convyoy_252d_slope_v092_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = conv - conv.shift(252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posbuildage_252d_slope_v093_signal(shrholdings):
    def _age(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = shrholdings.rolling(252, min_periods=126).apply(_age, raw=True)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom121_252d_slope_v094_signal(shrvalue):
    b = shrvalue.shift(21) / shrvalue.shift(252).replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumconsist_126d_slope_v095_signal(shrholdings):
    sub = shrholdings.pct_change(21).abs()
    mx = sub.rolling(126, min_periods=63).max()
    tot = shrholdings.pct_change().abs().rolling(126, min_periods=63).sum()
    b = mx / tot.replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwnetflow_126d_slope_v096_signal(shrholdings, shrvalue, totalvalue):
    d = shrholdings.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = (d * cr).rolling(126, min_periods=63).mean()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomrank_252d_slope_v097_signal(shrholdings):
    m = _roc(shrholdings, 63)
    b = m.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_mixshift_126d_slope_v098_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 126) - _slope(_roc(totalvalue, 21), 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpurng_126d_slope_v099_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    hi = _rmax(vpu, 126)
    lo = _rmin(vpu, 126)
    b = (vpu - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpurng_252d_slope_v100_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    hi = _rmax(vpu, 252)
    lo = _rmin(vpu, 252)
    b = (vpu - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convunit_126d_slope_v101_signal(shrunits, shrvalue, totalvalue):
    uf = shrunits.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    cf = conv.diff()
    b = uf.rolling(126, min_periods=63).corr(cf)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumspr_63d_slope_v102_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 63)
    b = s - l
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumspr_126d_slope_v103_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 126)
    b = s - l
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posanom_252d_slope_v104_signal(shrholdings):
    lm = np.log(shrholdings.replace(0, np.nan))
    b = lm - lm.rolling(252, min_periods=126).mean()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_smpressure_126d_slope_v105_signal(shrholdings, shrvalue, totalvalue):
    pc = _f44_pos_change(shrholdings, 21)
    conv = _f44_conviction(shrvalue, totalvalue)
    b = (pc * conv).ewm(span=63, min_periods=21).mean()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitrng_126d_slope_v106_signal(shrunits):
    hi = _rmax(shrunits, 126)
    lo = _rmin(shrunits, 126)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitrng_252d_slope_v107_signal(shrunits):
    hi = _rmax(shrunits, 252)
    lo = _rmin(shrunits, 252)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_velast_126d_slope_v108_signal(shrvalue, shrunits):
    dv = np.log(shrvalue.replace(0, np.nan)) - np.log(shrvalue.shift(63).replace(0, np.nan))
    du = np.log(shrunits.replace(0, np.nan)) - np.log(shrunits.shift(63).replace(0, np.nan))
    b = dv / du.replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumentries_126d_slope_v109_signal(shrholdings):
    d = shrholdings.pct_change()
    up = (d > 0).astype(float)
    entry = ((up == 1) & (up.shift(1) == 0)).astype(float)
    follow = d.clip(lower=0).rolling(5, min_periods=1).sum()
    ew = (entry * follow).rolling(126, min_periods=63).sum()
    cnt = entry.rolling(126, min_periods=63).sum()
    b = ew / cnt.replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumentries_252d_slope_v110_signal(shrholdings):
    d = shrholdings.pct_change()
    up = (d > 0).astype(float)
    entry = ((up == 1) & (up.shift(1) == 0)).astype(float)
    follow = d.clip(lower=0).rolling(5, min_periods=1).sum()
    ew = (entry * follow).rolling(252, min_periods=126).sum()
    cnt = entry.rolling(252, min_periods=126).sum()
    b = ew / cnt.replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convvssize_252d_slope_v111_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    pr = shrholdings.rolling(252, min_periods=126).rank(pct=True)
    b = cr - pr
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valaccel_126d_slope_v112_signal(shrvalue):
    m = _roc(shrvalue, 21)
    b = m - m.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posemacross_126d_slope_v113_signal(shrholdings):
    fast = shrholdings.ewm(span=21, min_periods=10).mean()
    slow = shrholdings.ewm(span=126, min_periods=42).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convimpulse_126d_slope_v114_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    f = conv.diff(5)
    b = f - f.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowz_126d_slope_v115_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _z(d, 126)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowz_252d_slope_v116_signal(shrholdings):
    d = shrholdings.pct_change(5)
    b = _z(d, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumvwbreadth_0d_slope_v117_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 126)
    b = (s - l) / (s.abs() + l.abs() + 1e-9)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_streakrank_252d_slope_v118_signal(shrholdings):
    st = _f44_build_streak(shrholdings)
    b = st.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrecov_252d_slope_v119_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    trough = _rmin(conv, 252)
    b = conv / trough.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitvalattr_126d_slope_v120_signal(shrunits, shrvalue):
    du = _roc(shrunits, 126)
    dv = _roc(shrvalue, 126)
    b = du / (du.abs() + dv.abs()).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumquality_252d_slope_v121_signal(shrholdings):
    net = (shrholdings - shrholdings.shift(252)).abs()
    path = shrholdings.diff().abs().rolling(252, min_periods=126).sum()
    er = net / path.replace(0, np.nan)
    b = er ** 2 * np.sign(shrholdings - shrholdings.shift(252))
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtconvex_126d_slope_v122_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    d1 = wt - wt.shift(21)
    b = (d1 - d1.shift(21)).rolling(21, min_periods=10).mean()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomsmooth_126d_slope_v123_signal(shrholdings):
    m = _roc(shrholdings, 63)
    b = m.ewm(span=42, min_periods=21).mean()
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshconvrank_252d_slope_v124_signal(shrholdings, shrvalue, totalvalue):
    lo = _rmin(shrholdings, 252)
    fresh = shrholdings / lo.replace(0, np.nan) - 1.0
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    b = fresh * cr
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_dollarflow_63d_slope_v125_signal(shrvalue, totalvalue):
    dv = shrvalue - shrvalue.shift(63)
    raw = dv / totalvalue.replace(0, np.nan)
    b = _z(raw, 252)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowsignmag_63d_slope_v126_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 63)
    b = np.sign(pc) * pc.abs() ** 0.5
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowsignmag_126d_slope_v127_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 126)
    b = np.sign(pc) * pc.abs() ** 0.5
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convterm_126d_slope_v128_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _mean(conv, 21) / _mean(conv, 126).replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poscv_252d_slope_v129_signal(shrholdings):
    b = _std(shrholdings, 252) / _mean(shrholdings, 252).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwhit_126d_slope_v130_signal(shrholdings, shrvalue, totalvalue):
    dh = shrholdings.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    b = dh.rolling(126, min_periods=63).corr(dc)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accummomchg_126d_slope_v131_signal(shrholdings):
    m = _roc(shrholdings, 21)
    b = m - m.shift(21)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomspr_252d_slope_v132_signal(shrvalue):
    s = _roc(shrvalue, 63)
    l = _roc(shrvalue, 252)
    b = s - l
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convunitgrow_126d_slope_v133_signal(shrunits, shrvalue, totalvalue):
    ug = _roc(shrunits, 126)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    gate = (cr >= 0.5).astype(float)
    b = ug * gate
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posnewhi_252d_slope_v134_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    prox = shrholdings / hi.replace(0, np.nan)
    b = prox.ewm(span=21, min_periods=10).mean()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convskew_252d_slope_v135_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = conv.rolling(252, min_periods=126).skew()
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuvsposz_252d_slope_v136_signal(shrvalue, shrunits, shrholdings):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 252) - _z(shrholdings, 252)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posdrawup_63d_slope_v137_signal(shrholdings):
    lo = _rmin(shrholdings, 63)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreadth_0d_slope_v138_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    r1 = conv.rolling(63, min_periods=32).rank(pct=True)
    r2 = conv.rolling(126, min_periods=63).rank(pct=True)
    r3 = conv.rolling(252, min_periods=126).rank(pct=True)
    b = pd.concat([r1, r2, r3], axis=1).mean(axis=1) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowautocorr_252d_slope_v139_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(252, min_periods=126).corr(d.shift(21))
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwnetstreak_0d_slope_v140_signal(shrholdings, shrvalue, totalvalue):
    ns = _f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = ns * wt
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomconv_252d_slope_v141_signal(shrholdings, shrvalue, totalvalue):
    m = _roc(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    disp = _std(conv, 252)
    b = m / disp.replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitaccel_126d_slope_v142_signal(shrunits):
    m = _roc(shrunits, 21)
    b = m - m.shift(63)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valoutpace_126d_slope_v143_signal(shrvalue, totalvalue):
    rel = np.log(shrvalue.replace(0, np.nan) / shrvalue.shift(63).replace(0, np.nan)) - np.log(totalvalue.replace(0, np.nan) / totalvalue.shift(63).replace(0, np.nan))
    b = rel.rolling(252, min_periods=126).rank(pct=True) - 0.5
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valqtydiv_252d_slope_v144_signal(shrholdings, shrvalue):
    vr = shrvalue.pct_change(63).rolling(252, min_periods=126).rank(pct=True)
    qr = shrholdings.pct_change(63).rolling(252, min_periods=126).rank(pct=True)
    b = vr - qr
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posqtrdrift_63d_slope_v145_signal(shrholdings):
    d = shrholdings.pct_change()
    ac = d.rolling(63, min_periods=32).corr(d.shift(1))
    b = ac
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtdisp_0d_slope_v146_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    w1 = _mean(wt, 21)
    w2 = _mean(wt, 63)
    w3 = _mean(wt, 126)
    b = pd.concat([w1, w2, w3], axis=1).std(axis=1)
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumconvsign_126d_slope_v147_signal(shrholdings, shrvalue, totalvalue):
    pc = _f44_pos_change(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    ct = _slope(conv, 126)
    b = pc * np.sign(ct)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poscum2y_504d_slope_v148_signal(shrholdings):
    b = np.log(shrholdings.replace(0, np.nan) / shrholdings.shift(504).replace(0, np.nan))
    base_val = b
    d1 = base_val - base_val.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvov_126d_slope_v149_signal(shrvalue):
    v = _std(shrvalue.pct_change(), 21)
    b = _std(v, 126) / _mean(v, 126).replace(0, np.nan)
    base_val = b
    d1 = base_val - base_val.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbuildstreak_0d_slope_v150_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    st = _streak_up(conv)
    mag = conv.diff().clip(lower=0).rolling(5, min_periods=1).mean()
    b = st * mag
    base_val = b
    d1 = base_val - base_val.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f44sm_f44_smart_money_flow_poschg_5d_slope_v001_signal,
    f44sm_f44_smart_money_flow_poschg_21d_slope_v002_signal,
    f44sm_f44_smart_money_flow_poschg_63d_slope_v003_signal,
    f44sm_f44_smart_money_flow_poschg_126d_slope_v004_signal,
    f44sm_f44_smart_money_flow_poschg_252d_slope_v005_signal,
    f44sm_f44_smart_money_flow_posemagap_21d_slope_v006_signal,
    f44sm_f44_smart_money_flow_posimpulse_63d_slope_v007_signal,
    f44sm_f44_smart_money_flow_posmedgap_126d_slope_v008_signal,
    f44sm_f44_smart_money_flow_convz_63d_slope_v009_signal,
    f44sm_f44_smart_money_flow_convz_126d_slope_v010_signal,
    f44sm_f44_smart_money_flow_convz_252d_slope_v011_signal,
    f44sm_f44_smart_money_flow_convrank_126d_slope_v012_signal,
    f44sm_f44_smart_money_flow_convrank_252d_slope_v013_signal,
    f44sm_f44_smart_money_flow_accum_21d_slope_v014_signal,
    f44sm_f44_smart_money_flow_accum_63d_slope_v015_signal,
    f44sm_f44_smart_money_flow_accum_126d_slope_v016_signal,
    f44sm_f44_smart_money_flow_accum_252d_slope_v017_signal,
    f44sm_f44_smart_money_flow_buildstreak_0d_slope_v018_signal,
    f44sm_f44_smart_money_flow_trimstreak_0d_slope_v019_signal,
    f44sm_f44_smart_money_flow_netstreak_21d_slope_v020_signal,
    f44sm_f44_smart_money_flow_accumhit_63d_slope_v021_signal,
    f44sm_f44_smart_money_flow_accumhit_126d_slope_v022_signal,
    f44sm_f44_smart_money_flow_accumhit_252d_slope_v023_signal,
    f44sm_f44_smart_money_flow_vpuz_63d_slope_v024_signal,
    f44sm_f44_smart_money_flow_vpuz_252d_slope_v025_signal,
    f44sm_f44_smart_money_flow_vpumom_21d_slope_v026_signal,
    f44sm_f44_smart_money_flow_vpumom_63d_slope_v027_signal,
    f44sm_f44_smart_money_flow_vpumom_126d_slope_v028_signal,
    f44sm_f44_smart_money_flow_valmom_21d_slope_v029_signal,
    f44sm_f44_smart_money_flow_valmom_63d_slope_v030_signal,
    f44sm_f44_smart_money_flow_valmom_126d_slope_v031_signal,
    f44sm_f44_smart_money_flow_valmom_252d_slope_v032_signal,
    f44sm_f44_smart_money_flow_valvsqty_63d_slope_v033_signal,
    f44sm_f44_smart_money_flow_valvsqty_126d_slope_v034_signal,
    f44sm_f44_smart_money_flow_portwtvol_126d_slope_v035_signal,
    f44sm_f44_smart_money_flow_portwtvol_252d_slope_v036_signal,
    f44sm_f44_smart_money_flow_posslope_63d_slope_v037_signal,
    f44sm_f44_smart_money_flow_posslope_126d_slope_v038_signal,
    f44sm_f44_smart_money_flow_convtrend_63d_slope_v039_signal,
    f44sm_f44_smart_money_flow_convtrend_126d_slope_v040_signal,
    f44sm_f44_smart_money_flow_freshbuild_126d_slope_v041_signal,
    f44sm_f44_smart_money_flow_freshbuild_252d_slope_v042_signal,
    f44sm_f44_smart_money_flow_trimpeak_126d_slope_v043_signal,
    f44sm_f44_smart_money_flow_trimpeak_252d_slope_v044_signal,
    f44sm_f44_smart_money_flow_posrng_126d_slope_v045_signal,
    f44sm_f44_smart_money_flow_posrng_252d_slope_v046_signal,
    f44sm_f44_smart_money_flow_convmom_63d_slope_v047_signal,
    f44sm_f44_smart_money_flow_convmom_126d_slope_v048_signal,
    f44sm_f44_smart_money_flow_accumz_126d_slope_v049_signal,
    f44sm_f44_smart_money_flow_unitgrow_63d_slope_v050_signal,
    f44sm_f44_smart_money_flow_unitgrow_126d_slope_v051_signal,
    f44sm_f44_smart_money_flow_unitgrow_252d_slope_v052_signal,
    f44sm_f44_smart_money_flow_hpuz_63d_slope_v053_signal,
    f44sm_f44_smart_money_flow_hpuz_252d_slope_v054_signal,
    f44sm_f44_smart_money_flow_convextreme_252d_slope_v055_signal,
    f44sm_f44_smart_money_flow_poschgyoy_63d_slope_v056_signal,
    f44sm_f44_smart_money_flow_poschgyoy_126d_slope_v057_signal,
    f44sm_f44_smart_money_flow_convdownvol_126d_slope_v058_signal,
    f44sm_f44_smart_money_flow_convdownvol_252d_slope_v059_signal,
    f44sm_f44_smart_money_flow_flowvol_126d_slope_v060_signal,
    f44sm_f44_smart_money_flow_flowvol_252d_slope_v061_signal,
    f44sm_f44_smart_money_flow_riskadjaccum_126d_slope_v062_signal,
    f44sm_f44_smart_money_flow_valmomrank_252d_slope_v063_signal,
    f44sm_f44_smart_money_flow_posvarratio_63d_slope_v064_signal,
    f44sm_f44_smart_money_flow_posvarratio_126d_slope_v065_signal,
    f44sm_f44_smart_money_flow_convbreak_126d_slope_v066_signal,
    f44sm_f44_smart_money_flow_convbreak_252d_slope_v067_signal,
    f44sm_f44_smart_money_flow_vwdrift_126d_slope_v068_signal,
    f44sm_f44_smart_money_flow_buildpersist_126d_slope_v069_signal,
    f44sm_f44_smart_money_flow_buildpersist_252d_slope_v070_signal,
    f44sm_f44_smart_money_flow_flowtanh_63d_slope_v071_signal,
    f44sm_f44_smart_money_flow_convsize_126d_slope_v072_signal,
    f44sm_f44_smart_money_flow_vpudiverge_126d_slope_v073_signal,
    f44sm_f44_smart_money_flow_valinflect_126d_slope_v074_signal,
    f44sm_f44_smart_money_flow_accumbreadth_0d_slope_v075_signal,
    f44sm_f44_smart_money_flow_accumdisp_0d_slope_v076_signal,
    f44sm_f44_smart_money_flow_convaccel_126d_slope_v077_signal,
    f44sm_f44_smart_money_flow_convramphit_63d_slope_v078_signal,
    f44sm_f44_smart_money_flow_posz_126d_slope_v079_signal,
    f44sm_f44_smart_money_flow_posz_252d_slope_v080_signal,
    f44sm_f44_smart_money_flow_wtmom_63d_slope_v081_signal,
    f44sm_f44_smart_money_flow_wtmom_126d_slope_v082_signal,
    f44sm_f44_smart_money_flow_accumeff_126d_slope_v083_signal,
    f44sm_f44_smart_money_flow_accumeff_252d_slope_v084_signal,
    f44sm_f44_smart_money_flow_unitdiverge_126d_slope_v085_signal,
    f44sm_f44_smart_money_flow_convregime_252d_slope_v086_signal,
    f44sm_f44_smart_money_flow_flowskew_126d_slope_v087_signal,
    f44sm_f44_smart_money_flow_flowskew_252d_slope_v088_signal,
    f44sm_f44_smart_money_flow_freshconv_252d_slope_v089_signal,
    f44sm_f44_smart_money_flow_valmomadj_126d_slope_v090_signal,
    f44sm_f44_smart_money_flow_posuw_252d_slope_v091_signal,
    f44sm_f44_smart_money_flow_convyoy_252d_slope_v092_signal,
    f44sm_f44_smart_money_flow_posbuildage_252d_slope_v093_signal,
    f44sm_f44_smart_money_flow_valmom121_252d_slope_v094_signal,
    f44sm_f44_smart_money_flow_accumconsist_126d_slope_v095_signal,
    f44sm_f44_smart_money_flow_vwnetflow_126d_slope_v096_signal,
    f44sm_f44_smart_money_flow_posmomrank_252d_slope_v097_signal,
    f44sm_f44_smart_money_flow_mixshift_126d_slope_v098_signal,
    f44sm_f44_smart_money_flow_vpurng_126d_slope_v099_signal,
    f44sm_f44_smart_money_flow_vpurng_252d_slope_v100_signal,
    f44sm_f44_smart_money_flow_convunit_126d_slope_v101_signal,
    f44sm_f44_smart_money_flow_accumspr_63d_slope_v102_signal,
    f44sm_f44_smart_money_flow_accumspr_126d_slope_v103_signal,
    f44sm_f44_smart_money_flow_posanom_252d_slope_v104_signal,
    f44sm_f44_smart_money_flow_smpressure_126d_slope_v105_signal,
    f44sm_f44_smart_money_flow_unitrng_126d_slope_v106_signal,
    f44sm_f44_smart_money_flow_unitrng_252d_slope_v107_signal,
    f44sm_f44_smart_money_flow_velast_126d_slope_v108_signal,
    f44sm_f44_smart_money_flow_accumentries_126d_slope_v109_signal,
    f44sm_f44_smart_money_flow_accumentries_252d_slope_v110_signal,
    f44sm_f44_smart_money_flow_convvssize_252d_slope_v111_signal,
    f44sm_f44_smart_money_flow_valaccel_126d_slope_v112_signal,
    f44sm_f44_smart_money_flow_posemacross_126d_slope_v113_signal,
    f44sm_f44_smart_money_flow_convimpulse_126d_slope_v114_signal,
    f44sm_f44_smart_money_flow_flowz_126d_slope_v115_signal,
    f44sm_f44_smart_money_flow_flowz_252d_slope_v116_signal,
    f44sm_f44_smart_money_flow_accumvwbreadth_0d_slope_v117_signal,
    f44sm_f44_smart_money_flow_streakrank_252d_slope_v118_signal,
    f44sm_f44_smart_money_flow_convrecov_252d_slope_v119_signal,
    f44sm_f44_smart_money_flow_unitvalattr_126d_slope_v120_signal,
    f44sm_f44_smart_money_flow_accumquality_252d_slope_v121_signal,
    f44sm_f44_smart_money_flow_wtconvex_126d_slope_v122_signal,
    f44sm_f44_smart_money_flow_posmomsmooth_126d_slope_v123_signal,
    f44sm_f44_smart_money_flow_freshconvrank_252d_slope_v124_signal,
    f44sm_f44_smart_money_flow_dollarflow_63d_slope_v125_signal,
    f44sm_f44_smart_money_flow_flowsignmag_63d_slope_v126_signal,
    f44sm_f44_smart_money_flow_flowsignmag_126d_slope_v127_signal,
    f44sm_f44_smart_money_flow_convterm_126d_slope_v128_signal,
    f44sm_f44_smart_money_flow_poscv_252d_slope_v129_signal,
    f44sm_f44_smart_money_flow_vwhit_126d_slope_v130_signal,
    f44sm_f44_smart_money_flow_accummomchg_126d_slope_v131_signal,
    f44sm_f44_smart_money_flow_valmomspr_252d_slope_v132_signal,
    f44sm_f44_smart_money_flow_convunitgrow_126d_slope_v133_signal,
    f44sm_f44_smart_money_flow_posnewhi_252d_slope_v134_signal,
    f44sm_f44_smart_money_flow_convskew_252d_slope_v135_signal,
    f44sm_f44_smart_money_flow_vpuvsposz_252d_slope_v136_signal,
    f44sm_f44_smart_money_flow_posdrawup_63d_slope_v137_signal,
    f44sm_f44_smart_money_flow_convbreadth_0d_slope_v138_signal,
    f44sm_f44_smart_money_flow_flowautocorr_252d_slope_v139_signal,
    f44sm_f44_smart_money_flow_vwnetstreak_0d_slope_v140_signal,
    f44sm_f44_smart_money_flow_posmomconv_252d_slope_v141_signal,
    f44sm_f44_smart_money_flow_unitaccel_126d_slope_v142_signal,
    f44sm_f44_smart_money_flow_valoutpace_126d_slope_v143_signal,
    f44sm_f44_smart_money_flow_valqtydiv_252d_slope_v144_signal,
    f44sm_f44_smart_money_flow_posqtrdrift_63d_slope_v145_signal,
    f44sm_f44_smart_money_flow_wtdisp_0d_slope_v146_signal,
    f44sm_f44_smart_money_flow_accumconvsign_126d_slope_v147_signal,
    f44sm_f44_smart_money_flow_poscum2y_504d_slope_v148_signal,
    f44sm_f44_smart_money_flow_valvov_126d_slope_v149_signal,
    f44sm_f44_smart_money_flow_convbuildstreak_0d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_SMART_MONEY_FLOW_REGISTRY_2ND_001_150 = REGISTRY


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

    print("OK f44_smart_money_flow_2nd_derivatives_001_150_claude: %d features pass" % n_features)
