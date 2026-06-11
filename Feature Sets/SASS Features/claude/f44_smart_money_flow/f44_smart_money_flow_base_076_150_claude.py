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


def f44sm_f44_smart_money_flow_accumdisp_0d_base_v076_signal(shrholdings):
    p1 = _f44_pos_change(shrholdings, 21)
    p2 = _f44_pos_change(shrholdings, 63)
    p3 = _f44_pos_change(shrholdings, 126)
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convaccel_126d_base_v077_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    ch = conv - conv.shift(21)
    b = ch - ch.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convramphit_63d_base_v078_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    ex = dc - dc.rolling(63, min_periods=32).mean()
    up = (ex.clip(lower=0) ** 2).rolling(63, min_periods=32).mean()
    dn = (ex.clip(upper=0) ** 2).rolling(63, min_periods=32).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posz_126d_base_v079_signal(shrholdings):
    b = _z(shrholdings, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posz_252d_base_v080_signal(shrholdings):
    b = _z(shrholdings, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtmom_63d_base_v081_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _roc(wt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtmom_126d_base_v082_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = _roc(wt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumeff_126d_base_v083_signal(shrholdings):
    d = shrholdings.pct_change()
    vshort = _std(d, 21)
    vlong = _std(d, 126)
    b = vshort / vlong.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumeff_252d_base_v084_signal(shrholdings):
    d = shrholdings.pct_change()
    vshort = _std(d, 21)
    vlong = _std(d, 252)
    b = vshort / vlong.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitdiverge_126d_base_v085_signal(shrunits, shrholdings):
    b = _roc(shrunits, 126) - _roc(shrholdings, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convregime_252d_base_v086_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    med = conv.rolling(252, min_periods=126).median()
    above = (conv > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowskew_126d_base_v087_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowskew_252d_base_v088_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshconv_252d_base_v089_signal(shrholdings, shrvalue, totalvalue):
    hi = _rmax(shrholdings, 252)
    lo = _rmin(shrholdings, 252)
    rp = (shrholdings - lo) / (hi - lo).replace(0, np.nan)
    conv = _f44_conviction(shrvalue, totalvalue)
    chi = _rmax(conv, 252)
    clo = _rmin(conv, 252)
    crp = (conv - clo) / (chi - clo).replace(0, np.nan)
    b = rp - crp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomadj_126d_base_v090_signal(shrvalue):
    r = shrvalue.pct_change(21)
    b = r.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posuw_252d_base_v091_signal(shrholdings):
    peak = _rmax(shrholdings, 252)
    uw = shrholdings / peak.replace(0, np.nan) - 1.0
    deep = (uw <= -0.10).astype(float)
    b = deep.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convyoy_252d_base_v092_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = conv - conv.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posbuildage_252d_base_v093_signal(shrholdings):
    def _age(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = shrholdings.rolling(252, min_periods=126).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmom121_252d_base_v094_signal(shrvalue):
    b = shrvalue.shift(21) / shrvalue.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumconsist_126d_base_v095_signal(shrholdings):
    sub = shrholdings.pct_change(21).abs()
    mx = sub.rolling(126, min_periods=63).max()
    tot = shrholdings.pct_change().abs().rolling(126, min_periods=63).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwnetflow_126d_base_v096_signal(shrholdings, shrvalue, totalvalue):
    d = shrholdings.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = (d * cr).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomrank_252d_base_v097_signal(shrholdings):
    m = _roc(shrholdings, 63)
    b = m.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_mixshift_126d_base_v098_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _slope(conv, 126) - _slope(_roc(totalvalue, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpurng_126d_base_v099_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    hi = _rmax(vpu, 126)
    lo = _rmin(vpu, 126)
    b = (vpu - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpurng_252d_base_v100_signal(shrvalue, shrunits):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    hi = _rmax(vpu, 252)
    lo = _rmin(vpu, 252)
    b = (vpu - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convunit_126d_base_v101_signal(shrunits, shrvalue, totalvalue):
    uf = shrunits.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    cf = conv.diff()
    b = uf.rolling(126, min_periods=63).corr(cf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumspr_63d_base_v102_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumspr_126d_base_v103_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posanom_252d_base_v104_signal(shrholdings):
    lm = np.log(shrholdings.replace(0, np.nan))
    b = lm - lm.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_smpressure_126d_base_v105_signal(shrholdings, shrvalue, totalvalue):
    pc = _f44_pos_change(shrholdings, 21)
    conv = _f44_conviction(shrvalue, totalvalue)
    b = (pc * conv).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitrng_126d_base_v106_signal(shrunits):
    hi = _rmax(shrunits, 126)
    lo = _rmin(shrunits, 126)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitrng_252d_base_v107_signal(shrunits):
    hi = _rmax(shrunits, 252)
    lo = _rmin(shrunits, 252)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_velast_126d_base_v108_signal(shrvalue, shrunits):
    dv = np.log(shrvalue.replace(0, np.nan)) - np.log(shrvalue.shift(63).replace(0, np.nan))
    du = np.log(shrunits.replace(0, np.nan)) - np.log(shrunits.shift(63).replace(0, np.nan))
    b = dv / du.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumentries_126d_base_v109_signal(shrholdings):
    d = shrholdings.pct_change()
    up = (d > 0).astype(float)
    entry = ((up == 1) & (up.shift(1) == 0)).astype(float)
    follow = d.clip(lower=0).rolling(5, min_periods=1).sum()
    ew = (entry * follow).rolling(126, min_periods=63).sum()
    cnt = entry.rolling(126, min_periods=63).sum()
    b = ew / cnt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumentries_252d_base_v110_signal(shrholdings):
    d = shrholdings.pct_change()
    up = (d > 0).astype(float)
    entry = ((up == 1) & (up.shift(1) == 0)).astype(float)
    follow = d.clip(lower=0).rolling(5, min_periods=1).sum()
    ew = (entry * follow).rolling(252, min_periods=126).sum()
    cnt = entry.rolling(252, min_periods=126).sum()
    b = ew / cnt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convvssize_252d_base_v111_signal(shrholdings, shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    pr = shrholdings.rolling(252, min_periods=126).rank(pct=True)
    b = cr - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valaccel_126d_base_v112_signal(shrvalue):
    m = _roc(shrvalue, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posemacross_126d_base_v113_signal(shrholdings):
    fast = shrholdings.ewm(span=21, min_periods=10).mean()
    slow = shrholdings.ewm(span=126, min_periods=42).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convimpulse_126d_base_v114_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    f = conv.diff(5)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowz_126d_base_v115_signal(shrholdings):
    d = shrholdings.pct_change()
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowz_252d_base_v116_signal(shrholdings):
    d = shrholdings.pct_change(5)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumvwbreadth_0d_base_v117_signal(shrholdings):
    s = _f44_pos_change(shrholdings, 21)
    l = _f44_pos_change(shrholdings, 126)
    b = (s - l) / (s.abs() + l.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_streakrank_252d_base_v118_signal(shrholdings):
    st = _f44_build_streak(shrholdings)
    b = st.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convrecov_252d_base_v119_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    trough = _rmin(conv, 252)
    b = conv / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitvalattr_126d_base_v120_signal(shrunits, shrvalue):
    du = _roc(shrunits, 126)
    dv = _roc(shrvalue, 126)
    b = du / (du.abs() + dv.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumquality_252d_base_v121_signal(shrholdings):
    net = (shrholdings - shrholdings.shift(252)).abs()
    path = shrholdings.diff().abs().rolling(252, min_periods=126).sum()
    er = net / path.replace(0, np.nan)
    b = er ** 2 * np.sign(shrholdings - shrholdings.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtconvex_126d_base_v122_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    d1 = wt - wt.shift(21)
    b = (d1 - d1.shift(21)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomsmooth_126d_base_v123_signal(shrholdings):
    m = _roc(shrholdings, 63)
    b = m.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_freshconvrank_252d_base_v124_signal(shrholdings, shrvalue, totalvalue):
    lo = _rmin(shrholdings, 252)
    fresh = shrholdings / lo.replace(0, np.nan) - 1.0
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    b = fresh * cr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_dollarflow_63d_base_v125_signal(shrvalue, totalvalue):
    dv = shrvalue - shrvalue.shift(63)
    raw = dv / totalvalue.replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowsignmag_63d_base_v126_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 63)
    b = np.sign(pc) * pc.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowsignmag_126d_base_v127_signal(shrholdings):
    pc = _f44_pos_change(shrholdings, 126)
    b = np.sign(pc) * pc.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convterm_126d_base_v128_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = _mean(conv, 21) / _mean(conv, 126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poscv_252d_base_v129_signal(shrholdings):
    b = _std(shrholdings, 252) / _mean(shrholdings, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwhit_126d_base_v130_signal(shrholdings, shrvalue, totalvalue):
    dh = shrholdings.pct_change()
    conv = _f44_conviction(shrvalue, totalvalue)
    dc = conv.diff()
    b = dh.rolling(126, min_periods=63).corr(dc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accummomchg_126d_base_v131_signal(shrholdings):
    m = _roc(shrholdings, 21)
    b = m - m.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valmomspr_252d_base_v132_signal(shrvalue):
    s = _roc(shrvalue, 63)
    l = _roc(shrvalue, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convunitgrow_126d_base_v133_signal(shrunits, shrvalue, totalvalue):
    ug = _roc(shrunits, 126)
    conv = _f44_conviction(shrvalue, totalvalue)
    cr = conv.rolling(252, min_periods=126).rank(pct=True)
    gate = (cr >= 0.5).astype(float)
    b = ug * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posnewhi_252d_base_v134_signal(shrholdings):
    hi = _rmax(shrholdings, 252)
    prox = shrholdings / hi.replace(0, np.nan)
    b = prox.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convskew_252d_base_v135_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    b = conv.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vpuvsposz_252d_base_v136_signal(shrvalue, shrunits, shrholdings):
    vpu = _f44_value_per_unit(shrvalue, shrunits)
    b = _z(vpu, 252) - _z(shrholdings, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posdrawup_63d_base_v137_signal(shrholdings):
    lo = _rmin(shrholdings, 63)
    b = shrholdings / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbreadth_0d_base_v138_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    r1 = conv.rolling(63, min_periods=32).rank(pct=True)
    r2 = conv.rolling(126, min_periods=63).rank(pct=True)
    r3 = conv.rolling(252, min_periods=126).rank(pct=True)
    b = pd.concat([r1, r2, r3], axis=1).mean(axis=1) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_flowautocorr_252d_base_v139_signal(shrholdings):
    d = shrholdings.pct_change()
    b = d.rolling(252, min_periods=126).corr(d.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_vwnetstreak_0d_base_v140_signal(shrholdings, shrvalue, totalvalue):
    ns = _f44_build_streak(shrholdings) - _f44_trim_streak(shrholdings)
    wt = shrvalue / totalvalue.replace(0, np.nan)
    b = ns * wt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posmomconv_252d_base_v141_signal(shrholdings, shrvalue, totalvalue):
    m = _roc(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    disp = _std(conv, 252)
    b = m / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_unitaccel_126d_base_v142_signal(shrunits):
    m = _roc(shrunits, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valoutpace_126d_base_v143_signal(shrvalue, totalvalue):
    rel = np.log(shrvalue.replace(0, np.nan) / shrvalue.shift(63).replace(0, np.nan)) - np.log(totalvalue.replace(0, np.nan) / totalvalue.shift(63).replace(0, np.nan))
    b = rel.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valqtydiv_252d_base_v144_signal(shrholdings, shrvalue):
    vr = shrvalue.pct_change(63).rolling(252, min_periods=126).rank(pct=True)
    qr = shrholdings.pct_change(63).rolling(252, min_periods=126).rank(pct=True)
    b = vr - qr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_posqtrdrift_63d_base_v145_signal(shrholdings):
    d = shrholdings.pct_change()
    ac = d.rolling(63, min_periods=32).corr(d.shift(1))
    b = ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_wtdisp_0d_base_v146_signal(shrvalue, totalvalue):
    wt = shrvalue / totalvalue.replace(0, np.nan)
    w1 = _mean(wt, 21)
    w2 = _mean(wt, 63)
    w3 = _mean(wt, 126)
    b = pd.concat([w1, w2, w3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_accumconvsign_126d_base_v147_signal(shrholdings, shrvalue, totalvalue):
    pc = _f44_pos_change(shrholdings, 63)
    conv = _f44_conviction(shrvalue, totalvalue)
    ct = _slope(conv, 126)
    b = pc * np.sign(ct)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_poscum2y_504d_base_v148_signal(shrholdings):
    b = np.log(shrholdings.replace(0, np.nan) / shrholdings.shift(504).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_valvov_126d_base_v149_signal(shrvalue):
    v = _std(shrvalue.pct_change(), 21)
    b = _std(v, 126) / _mean(v, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f44sm_f44_smart_money_flow_convbuildstreak_0d_base_v150_signal(shrvalue, totalvalue):
    conv = _f44_conviction(shrvalue, totalvalue)
    st = _streak_up(conv)
    mag = conv.diff().clip(lower=0).rolling(5, min_periods=1).mean()
    b = st * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f44sm_f44_smart_money_flow_accumdisp_0d_base_v076_signal,
    f44sm_f44_smart_money_flow_convaccel_126d_base_v077_signal,
    f44sm_f44_smart_money_flow_convramphit_63d_base_v078_signal,
    f44sm_f44_smart_money_flow_posz_126d_base_v079_signal,
    f44sm_f44_smart_money_flow_posz_252d_base_v080_signal,
    f44sm_f44_smart_money_flow_wtmom_63d_base_v081_signal,
    f44sm_f44_smart_money_flow_wtmom_126d_base_v082_signal,
    f44sm_f44_smart_money_flow_accumeff_126d_base_v083_signal,
    f44sm_f44_smart_money_flow_accumeff_252d_base_v084_signal,
    f44sm_f44_smart_money_flow_unitdiverge_126d_base_v085_signal,
    f44sm_f44_smart_money_flow_convregime_252d_base_v086_signal,
    f44sm_f44_smart_money_flow_flowskew_126d_base_v087_signal,
    f44sm_f44_smart_money_flow_flowskew_252d_base_v088_signal,
    f44sm_f44_smart_money_flow_freshconv_252d_base_v089_signal,
    f44sm_f44_smart_money_flow_valmomadj_126d_base_v090_signal,
    f44sm_f44_smart_money_flow_posuw_252d_base_v091_signal,
    f44sm_f44_smart_money_flow_convyoy_252d_base_v092_signal,
    f44sm_f44_smart_money_flow_posbuildage_252d_base_v093_signal,
    f44sm_f44_smart_money_flow_valmom121_252d_base_v094_signal,
    f44sm_f44_smart_money_flow_accumconsist_126d_base_v095_signal,
    f44sm_f44_smart_money_flow_vwnetflow_126d_base_v096_signal,
    f44sm_f44_smart_money_flow_posmomrank_252d_base_v097_signal,
    f44sm_f44_smart_money_flow_mixshift_126d_base_v098_signal,
    f44sm_f44_smart_money_flow_vpurng_126d_base_v099_signal,
    f44sm_f44_smart_money_flow_vpurng_252d_base_v100_signal,
    f44sm_f44_smart_money_flow_convunit_126d_base_v101_signal,
    f44sm_f44_smart_money_flow_accumspr_63d_base_v102_signal,
    f44sm_f44_smart_money_flow_accumspr_126d_base_v103_signal,
    f44sm_f44_smart_money_flow_posanom_252d_base_v104_signal,
    f44sm_f44_smart_money_flow_smpressure_126d_base_v105_signal,
    f44sm_f44_smart_money_flow_unitrng_126d_base_v106_signal,
    f44sm_f44_smart_money_flow_unitrng_252d_base_v107_signal,
    f44sm_f44_smart_money_flow_velast_126d_base_v108_signal,
    f44sm_f44_smart_money_flow_accumentries_126d_base_v109_signal,
    f44sm_f44_smart_money_flow_accumentries_252d_base_v110_signal,
    f44sm_f44_smart_money_flow_convvssize_252d_base_v111_signal,
    f44sm_f44_smart_money_flow_valaccel_126d_base_v112_signal,
    f44sm_f44_smart_money_flow_posemacross_126d_base_v113_signal,
    f44sm_f44_smart_money_flow_convimpulse_126d_base_v114_signal,
    f44sm_f44_smart_money_flow_flowz_126d_base_v115_signal,
    f44sm_f44_smart_money_flow_flowz_252d_base_v116_signal,
    f44sm_f44_smart_money_flow_accumvwbreadth_0d_base_v117_signal,
    f44sm_f44_smart_money_flow_streakrank_252d_base_v118_signal,
    f44sm_f44_smart_money_flow_convrecov_252d_base_v119_signal,
    f44sm_f44_smart_money_flow_unitvalattr_126d_base_v120_signal,
    f44sm_f44_smart_money_flow_accumquality_252d_base_v121_signal,
    f44sm_f44_smart_money_flow_wtconvex_126d_base_v122_signal,
    f44sm_f44_smart_money_flow_posmomsmooth_126d_base_v123_signal,
    f44sm_f44_smart_money_flow_freshconvrank_252d_base_v124_signal,
    f44sm_f44_smart_money_flow_dollarflow_63d_base_v125_signal,
    f44sm_f44_smart_money_flow_flowsignmag_63d_base_v126_signal,
    f44sm_f44_smart_money_flow_flowsignmag_126d_base_v127_signal,
    f44sm_f44_smart_money_flow_convterm_126d_base_v128_signal,
    f44sm_f44_smart_money_flow_poscv_252d_base_v129_signal,
    f44sm_f44_smart_money_flow_vwhit_126d_base_v130_signal,
    f44sm_f44_smart_money_flow_accummomchg_126d_base_v131_signal,
    f44sm_f44_smart_money_flow_valmomspr_252d_base_v132_signal,
    f44sm_f44_smart_money_flow_convunitgrow_126d_base_v133_signal,
    f44sm_f44_smart_money_flow_posnewhi_252d_base_v134_signal,
    f44sm_f44_smart_money_flow_convskew_252d_base_v135_signal,
    f44sm_f44_smart_money_flow_vpuvsposz_252d_base_v136_signal,
    f44sm_f44_smart_money_flow_posdrawup_63d_base_v137_signal,
    f44sm_f44_smart_money_flow_convbreadth_0d_base_v138_signal,
    f44sm_f44_smart_money_flow_flowautocorr_252d_base_v139_signal,
    f44sm_f44_smart_money_flow_vwnetstreak_0d_base_v140_signal,
    f44sm_f44_smart_money_flow_posmomconv_252d_base_v141_signal,
    f44sm_f44_smart_money_flow_unitaccel_126d_base_v142_signal,
    f44sm_f44_smart_money_flow_valoutpace_126d_base_v143_signal,
    f44sm_f44_smart_money_flow_valqtydiv_252d_base_v144_signal,
    f44sm_f44_smart_money_flow_posqtrdrift_63d_base_v145_signal,
    f44sm_f44_smart_money_flow_wtdisp_0d_base_v146_signal,
    f44sm_f44_smart_money_flow_accumconvsign_126d_base_v147_signal,
    f44sm_f44_smart_money_flow_poscum2y_504d_base_v148_signal,
    f44sm_f44_smart_money_flow_valvov_126d_base_v149_signal,
    f44sm_f44_smart_money_flow_convbuildstreak_0d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_SMART_MONEY_FLOW_REGISTRY_076_150 = REGISTRY


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

    print("OK f44_smart_money_flow_base_076_150_claude: %d features pass" % n_features)
