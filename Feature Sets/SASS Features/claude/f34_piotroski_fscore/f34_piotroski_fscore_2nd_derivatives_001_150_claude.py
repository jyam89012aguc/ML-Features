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


def _chg(s, w):
    return s - s.shift(w)


def _pctchg(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f34_soft_pos(s, scale):
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(s / sc.replace(0, np.nan))


def _f34_soft_gt(a, b, scale):
    diff = a - b
    sc = (a.abs() + b.abs()).rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(diff / sc.replace(0, np.nan))


def _f34_soft_up(s, w, scale):
    d = s - s.shift(w)
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_soft_down(s, w, scale):
    d = s.shift(w) - s
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_leverage(debt, assets):
    return _safe_div(debt, assets)


def _rollslope(s, w, mp):
    def _slope(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xm = x.mean()
        xden = ((x - xm) ** 2).sum()
        if xden == 0:
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / xden
    return s.rolling(w, min_periods=mp).apply(_slope, raw=True)


def _roc(s, w):
    # math 1st derivative: rate of change over w (difference of the base feature)
    return s - s.shift(w)


def _jerk(s, w):
    # math 2nd derivative: difference of the difference over w
    d = s - s.shift(w)
    return d - d.shift(w)



def f34pf_f34_piotroski_fscore_posni_252d_slope_v001_signal(netinc):
    bse = _f34_soft_pos(netinc, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_posnism_63d_slope_v002_signal(netinc):
    bse = _f34_soft_pos(netinc, 126).ewm(span=63, min_periods=21).mean()
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_nivol_252d_slope_v003_signal(netinc, assets):
    r = _safe_div(netinc, assets)
    vol = r.rolling(126, min_periods=63).std()
    sc = r.abs().rolling(252, min_periods=126).mean()
    bse = -np.tanh(vol / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_posocf_252d_slope_v004_signal(ncfo):
    bse = _f34_soft_pos(ncfo, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_posocfa_252d_slope_v005_signal(ncfo, assets):
    r = _safe_div(ncfo, assets)
    bse = r.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_posocffrac_252d_slope_v006_signal(ncfo):
    bse = _f34_soft_pos(ncfo, 126).clip(lower=0).rolling(252, min_periods=126).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_droa_252d_slope_v007_signal(roa):
    bse = _f34_soft_up(roa, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_droah_126d_slope_v008_signal(roa):
    bse = _f34_soft_up(roa, 126, 252)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_droasyn_252d_slope_v009_signal(netinc, assets):
    bse = _f34_soft_up(_safe_div(netinc, assets), 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accr_252d_slope_v010_signal(ncfo, netinc):
    bse = _f34_soft_gt(ncfo, netinc, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accra_252d_slope_v011_signal(ncfo, netinc, assets):
    accr = _safe_div(ncfo - netinc, assets)
    sc = accr.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(accr / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrsm_63d_slope_v012_signal(ncfo, netinc):
    soft = _f34_soft_gt(ncfo, netinc, 126)
    bse = (soft > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5 + 0.05 * soft
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dlev_252d_slope_v013_signal(debt, assets):
    bse = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dlevh_126d_slope_v014_signal(debt, assets):
    bse = _f34_soft_down(_f34_leverage(debt, assets), 126, 252)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_paydownstreak_252d_slope_v015_signal(debt):
    falling = (debt < debt.shift(63)).astype(float)
    streak = falling.rolling(252, min_periods=126).mean()
    depth = (-_pctchg(debt, 63)).clip(lower=0).rolling(63, min_periods=21).mean()
    bse = streak + 5.0 * depth
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dcurr_252d_slope_v016_signal(currentratio):
    bse = _f34_soft_up(currentratio, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dcurrq_63d_slope_v017_signal(currentratio):
    bse = _f34_soft_up(currentratio, 63, 126)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currlvl_252d_slope_v018_signal(currentratio):
    bse = np.tanh(_z(currentratio, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_nodil_252d_slope_v019_signal(sharesbas):
    bse = _f34_soft_down(sharesbas, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_nodilh_126d_slope_v020_signal(sharesbas):
    bse = _f34_soft_down(sharesbas, 126, 252)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_buybackcons_252d_slope_v021_signal(sharesbas):
    bse = (sharesbas < sharesbas.shift(63)).astype(float).rolling(504, min_periods=252).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dgm_252d_slope_v022_signal(grossmargin):
    bse = _f34_soft_up(grossmargin, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dgmq_63d_slope_v023_signal(grossmargin):
    bse = _f34_soft_up(grossmargin, 63, 126)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmlvl_252d_slope_v024_signal(grossmargin):
    bse = np.tanh(_z(grossmargin, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dato_252d_slope_v025_signal(assetturnover):
    bse = _f34_soft_up(assetturnover, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_datoh_126d_slope_v026_signal(assetturnover):
    bse = _f34_soft_up(assetturnover, 126, 252)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_atolvl_252d_slope_v027_signal(assetturnover):
    bse = np.tanh(_z(assetturnover, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fscore9_252d_slope_v028_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252); c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    bse = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fscorehard_252d_slope_v029_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    lev = _f34_leverage(debt, assets)
    s = ((netinc > 0).astype(float) + (ncfo > 0).astype(float) + (_chg(roa, 252) > 0).astype(float)
         + (ncfo > netinc).astype(float) + (_chg(lev, 252) < 0).astype(float)
         + (_chg(currentratio, 252) > 0).astype(float) + (_chg(sharesbas, 252) <= 0).astype(float)
         + (_chg(grossmargin, 252) > 0).astype(float) + (_chg(assetturnover, 252) > 0).astype(float))
    mag = _z(_safe_div(ncfo, assets), 252) * 0.001
    bse = (s + mag).rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fscore9h_126d_slope_v030_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126); c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252); c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 126, 252)
    c6 = _f34_soft_up(currentratio, 126, 252); c7 = _f34_soft_down(sharesbas, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252); c9 = _f34_soft_up(assetturnover, 126, 252)
    bse = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_profsub_252d_slope_v031_signal(netinc, ncfo, roa, assets):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    bse = (c1 + c2 + c3 + c4) / 4.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levsub_252d_slope_v032_signal(debt, assets, currentratio, sharesbas):
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252); c7 = _f34_soft_down(sharesbas, 252, 252)
    bse = (c5 + c6 + c7) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_effsub_252d_slope_v033_signal(grossmargin, assetturnover):
    bse = (_f34_soft_up(grossmargin, 252, 252) + _f34_soft_up(assetturnover, 252, 252)) / 2.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_qualcore_252d_slope_v034_signal(ncfo, netinc, debt, assets):
    c2 = _f34_soft_pos(ncfo, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    bse = (c2 + c4 + c5) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_imptrio_63d_slope_v035_signal(roa, grossmargin, assetturnover):
    c3 = (_f34_soft_up(roa, 63, 126) + 1) / 2
    c8 = (_f34_soft_up(grossmargin, 63, 126) + 1) / 2
    c9 = (_f34_soft_up(assetturnover, 63, 126) + 1) / 2
    bse = (c3 * c8 * c9) ** (1.0 / 3.0) - 0.5
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_wmag_252d_slope_v036_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin):
    c1 = np.tanh(2.0 * _safe_div(netinc, assets)); c2 = np.tanh(2.0 * _safe_div(ncfo, assets))
    c3 = np.tanh(50.0 * _chg(roa, 252)); c4 = np.tanh(5.0 * _safe_div(ncfo - netinc, assets))
    c5 = np.tanh(-10.0 * _chg(_f34_leverage(debt, assets), 252)); c6 = np.tanh(2.0 * _chg(currentratio, 252))
    c8 = np.tanh(20.0 * _chg(grossmargin, 252))
    bse = (c1 + c2 + c3 + c4 + c5 + c6 + c8) / 7.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_wprof_252d_slope_v037_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252); c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    bse = (c1 + c2 + c3 + c4) / 4.0 - (c5 + c6 + c7 + c8 + c9) / 5.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_weff_252d_slope_v038_signal(netinc, ncfo, debt, assets, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    bse = np.tanh(2.0 * ((c8 + c9) / 2.0 - (c1 + c2 + c5 + c6) / 4.0))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_wrecency_63d_slope_v039_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    def comp(w, sc):
        c3 = _f34_soft_up(roa, w, sc); c4 = _f34_soft_gt(ncfo, netinc, sc)
        c5 = _f34_soft_down(_f34_leverage(debt, assets), w, sc); c6 = _f34_soft_up(currentratio, w, sc)
        c8 = _f34_soft_up(grossmargin, w, sc); c9 = _f34_soft_up(assetturnover, w, sc)
        return (c3 + c4 + c5 + c6 + c8 + c9) / 6.0
    bse = comp(63, 126) - comp(252, 252)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_rollmean_252d_slope_v040_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126); c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252); c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 126, 252)
    c6 = _f34_soft_up(currentratio, 126, 252); c7 = _f34_soft_down(sharesbas, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252); c9 = _f34_soft_up(assetturnover, 126, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    bse = fs.rolling(252, min_periods=126).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fschg_252d_slope_v041_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252); c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    bse = fs - fs.shift(252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsrank_504d_slope_v042_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    bse = fs.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_strongcnt_252d_slope_v043_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [_f34_soft_pos(netinc, 252), _f34_soft_pos(ncfo, 252), _f34_soft_up(roa, 252, 252),
             _f34_soft_gt(ncfo, netinc, 252), _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
             _f34_soft_up(currentratio, 252, 252), _f34_soft_down(sharesbas, 252, 252),
             _f34_soft_up(grossmargin, 252, 252), _f34_soft_up(assetturnover, 252, 252)]
    tally = sum((c > 0.3).astype(float) for c in comps)
    mag = sum(c.clip(lower=0) for c in comps) * 0.01
    bse = (tally + mag).rolling(21, min_periods=10).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_compdisp_252d_slope_v044_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [_f34_soft_pos(netinc, 252), _f34_soft_pos(ncfo, 252), _f34_soft_up(roa, 252, 252),
             _f34_soft_gt(ncfo, netinc, 252), _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
             _f34_soft_up(currentratio, 252, 252), _f34_soft_down(sharesbas, 252, 252),
             _f34_soft_up(grossmargin, 252, 252), _f34_soft_up(assetturnover, 252, 252)]
    bse = pd.concat(comps, axis=1).std(axis=1)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_weaklink_252d_slope_v045_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    comps = [_f34_soft_pos(netinc, 252), _f34_soft_pos(ncfo, 252), _f34_soft_up(roa, 252, 252),
             _f34_soft_gt(ncfo, netinc, 252), _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
             _f34_soft_up(currentratio, 252, 252), _f34_soft_up(grossmargin, 252, 252), _f34_soft_up(assetturnover, 252, 252)]
    bse = pd.concat(comps, axis=1).min(axis=1).ewm(span=42, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_strongpillar_252d_slope_v046_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    comps = [_f34_soft_pos(netinc, 252), _f34_soft_pos(ncfo, 252), _f34_soft_up(roa, 252, 252),
             _f34_soft_gt(ncfo, netinc, 252), _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
             _f34_soft_up(currentratio, 252, 252), _f34_soft_up(grossmargin, 252, 252), _f34_soft_up(assetturnover, 252, 252)]
    bse = pd.concat(comps, axis=1).max(axis=1).ewm(span=42, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roalvl_252d_slope_v047_signal(roa):
    sc = roa.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(roa / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfroalvl_252d_slope_v048_signal(ncfo, assets):
    bse = np.tanh(3.0 * _safe_div(ncfo, assets))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrlvl_252d_slope_v049_signal(netinc, ncfo, assets):
    accr = _safe_div(netinc - ncfo, assets)
    bse = -accr.rolling(504, min_periods=126).rank(pct=True) + 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levlvl_252d_slope_v050_signal(debt, assets):
    bse = -np.tanh(_z(_f34_leverage(debt, assets), 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currconvex_63d_slope_v051_signal(currentratio):
    d = _chg(currentratio, 63); accel = d - d.shift(63)
    sc = currentratio.rolling(252, min_periods=126).mean()
    bse = np.tanh(accel / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dilaccel_252d_slope_v052_signal(sharesbas):
    g = _pctchg(sharesbas, 126); accel = g - g.shift(126)
    sc = g.abs().rolling(504, min_periods=126).mean()
    bse = -np.tanh(accel / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmtrend_126d_slope_v053_signal(grossmargin):
    d = _chg(grossmargin, 126); sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(d / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_atoslope_252d_slope_v054_signal(assetturnover):
    sl = _rollslope(assetturnover, 252, 126); sc = assetturnover.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_debtcover_252d_slope_v055_signal(netinc, debt):
    cover = _safe_div(netinc, debt); chg = cover - cover.shift(126)
    sc = cover.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(chg / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrxdroa_126d_slope_v056_signal(ncfo, netinc, roa):
    accr = _f34_soft_gt(ncfo, netinc, 126); droa = _f34_soft_up(roa, 126, 126)
    bse = (accr - droa).abs() * np.sign(accr + droa)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmxato_252d_slope_v057_signal(grossmargin, assetturnover):
    bse = _f34_soft_up(grossmargin, 252, 252) * _f34_soft_up(assetturnover, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currxnodil_252d_slope_v058_signal(currentratio, sharesbas):
    bse = _f34_soft_up(currentratio, 252, 252) * _f34_soft_down(sharesbas, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cashmargin_252d_slope_v059_signal(ncfo, assets, grossmargin):
    bse = np.tanh(_z(_safe_div(ncfo, assets), 252) - _z(grossmargin, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_breadth_252d_slope_v060_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [_f34_soft_pos(netinc, 252), _f34_soft_pos(ncfo, 252), _f34_soft_up(roa, 252, 252),
             _f34_soft_gt(ncfo, netinc, 252), _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
             _f34_soft_up(currentratio, 252, 252), _f34_soft_down(sharesbas, 252, 252),
             _f34_soft_up(grossmargin, 252, 252), _f34_soft_up(assetturnover, 252, 252)]
    pos = sum((c > 0).astype(float) for c in comps); neg = sum((c < 0).astype(float) for c in comps)
    bse = ((pos - neg) / 9.0).rolling(21, min_periods=10).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrrev_252d_slope_v061_signal(netinc, ncfo, assets):
    accr = _safe_div(netinc - ncfo, assets)
    bse = np.tanh(5.0 * (accr.shift(252) - accr))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dupontagree_252d_slope_v062_signal(grossmargin, assetturnover):
    dgm = np.sign(_chg(grossmargin, 252)); dato = np.sign(_chg(assetturnover, 252))
    mag = np.tanh(_z(_chg(grossmargin, 252), 252)).abs()
    bse = ((dgm * dato) * (0.5 + 0.5 * mag)).rolling(21, min_periods=10).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_finqual_252d_slope_v063_signal(debt, assets, sharesbas):
    delev = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    buyback = np.tanh(-8.0 * _pctchg(sharesbas, 252))
    bse = (delev + buyback) / 2.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_profpersist_504d_slope_v064_signal(netinc):
    bse = (_f34_soft_pos(netinc, 126) > 0.5).astype(float).rolling(504, min_periods=252).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrpersist_504d_slope_v065_signal(ncfo, netinc):
    soft = _f34_soft_gt(ncfo, netinc, 126)
    bse = (soft > 0.2).astype(float).rolling(504, min_periods=252).mean() + 0.2 * soft.clip(lower=0).rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsaccel_252d_slope_v066_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    d = fs - fs.shift(126); bse = d - d.shift(126)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levadjroa_252d_slope_v067_signal(netinc, assets, debt):
    roaq = _safe_div(netinc, assets); lev = _f34_leverage(debt, assets)
    bse = np.tanh(2.0 * roaq) * (1.0 - np.tanh(lev))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_qmd_252d_slope_v068_signal(ncfo, netinc, assets, sharesbas):
    cfps = _safe_div(ncfo, sharesbas); g = _pctchg(cfps, 252)
    accr = np.tanh(5.0 * _safe_div(ncfo - netinc, assets))
    bse = np.tanh(2.0 * g) + 0.3 * accr
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsz_504d_slope_v069_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    bse = _z(fs, 504)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_distqual_252d_slope_v070_signal(debt, assets, roa, grossmargin):
    gate = (1.0 + _f34_soft_down(_f34_leverage(debt, assets), 126, 252)) / 2.0
    ops = (_f34_soft_up(roa, 126, 252) + _f34_soft_up(grossmargin, 126, 252)) / 2.0
    bse = ops * gate
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cashgrowth_252d_slope_v071_signal(ncfo, assets, assetturnover):
    cfroa = _safe_div(ncfo, assets)
    turn = _safe_div(assetturnover, assetturnover.rolling(252, min_periods=126).mean())
    bse = np.tanh(2.0 * _z(cfroa, 252)) * turn
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_allfronts_252d_slope_v072_signal(roa, grossmargin, assetturnover, currentratio):
    def above_med(s):
        med = s.rolling(252, min_periods=126).median()
        return (s > med).astype(float)
    diff = above_med(roa) + above_med(grossmargin) + above_med(assetturnover) + above_med(currentratio)
    jitter = (_z(roa, 252) + _z(currentratio, 252)) * 0.01
    bse = (diff + jitter).rolling(21, min_periods=10).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_ecconverge_252d_slope_v073_signal(ncfo, netinc, assets):
    gn = _pctchg(ncfo, 21); ge = _pctchg(netinc, 21)
    bse = gn.rolling(252, min_periods=126).corr(ge)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_logitfs_126d_slope_v074_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    def lg(x):
        return 1.0 / (1.0 + np.exp(-x))
    p1 = lg(2.0 * _safe_div(netinc, assets) / _safe_div(netinc, assets).abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    p2 = lg(3.0 * _safe_div(ncfo, assets)); p3 = lg(40.0 * _chg(roa, 126))
    p4 = lg(5.0 * _safe_div(ncfo - netinc, assets)); p5 = lg(-8.0 * _chg(_f34_leverage(debt, assets), 126))
    p6 = lg(2.0 * _chg(currentratio, 126)); p8 = lg(15.0 * _chg(grossmargin, 126)); p9 = lg(4.0 * _chg(assetturnover, 126))
    bse = (p1 + p2 + p3 + p4 + p5 + p6 + p8 + p9) / 8.0 - 0.5
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fslongtrend_252d_slope_v075_signal(netinc, ncfo, roa, assets, debt, grossmargin):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8) / 6.0
    bse = fs.rolling(252, min_periods=126).mean() - fs.rolling(756, min_periods=378).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_nirank_504d_slope_v076_signal(netinc, assets):
    bse = _safe_div(netinc, assets).rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfrank_504d_slope_v077_signal(ncfo, assets):
    bse = _safe_div(ncfo, assets).rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roacross_126d_slope_v078_signal(roa):
    short = roa.rolling(126, min_periods=63).mean(); long = roa.rolling(504, min_periods=252).mean()
    sc = roa.abs().rolling(504, min_periods=126).mean()
    bse = np.tanh((short - long) / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrz_252d_slope_v079_signal(netinc, ncfo, assets):
    bse = -_z(_safe_div(netinc - ncfo, assets), 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levrank_504d_slope_v080_signal(debt, assets):
    bse = 0.5 - _f34_leverage(debt, assets).rolling(504, min_periods=126).rank(pct=True)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currrank_504d_slope_v081_signal(currentratio):
    bse = currentratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_shareoverhang_504d_slope_v082_signal(sharesbas):
    lo = sharesbas.rolling(504, min_periods=252).min()
    bse = -np.tanh(5.0 * (_safe_div(sharesbas, lo) - 1.0))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmrank_504d_slope_v083_signal(grossmargin):
    bse = grossmargin.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_atorank_504d_slope_v084_signal(assetturnover):
    bse = assetturnover.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roaslope_252d_slope_v085_signal(roa):
    sl = _rollslope(roa, 252, 126); sc = roa.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmslope_126d_slope_v086_signal(grossmargin):
    sl = _rollslope(grossmargin, 126, 63); sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(126.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currslope_252d_slope_v087_signal(currentratio):
    sl = _rollslope(currentratio, 252, 126); sc = currentratio.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levslope_252d_slope_v088_signal(debt, assets):
    lev = _f34_leverage(debt, assets); sl = _rollslope(lev, 252, 126)
    sc = lev.abs().rolling(252, min_periods=126).mean()
    bse = -np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_shareslope_252d_slope_v089_signal(sharesbas):
    sl = _rollslope(sharesbas, 252, 126); sc = sharesbas.abs().rolling(252, min_periods=126).mean()
    bse = -np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfroaslope_252d_slope_v090_signal(ncfo, assets):
    r = _safe_div(ncfo, assets); sl = _rollslope(r, 252, 126)
    sc = r.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roahit_252d_slope_v091_signal(roa):
    bse = (roa > roa.shift(63)).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmhit_252d_slope_v092_signal(grossmargin):
    bse = (grossmargin > grossmargin.shift(63)).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_atohit_252d_slope_v093_signal(assetturnover):
    bse = (assetturnover > assetturnover.shift(63)).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrhit_252d_slope_v094_signal(ncfo, netinc):
    gn = _pctchg(ncfo, 63); ge = _pctchg(netinc, 63)
    hit = (gn > ge).astype(float); depth = np.tanh(2.0 * (gn - ge))
    bse = hit.rolling(252, min_periods=126).mean() - 0.5 + 0.1 * depth.rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levhit_252d_slope_v095_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    bse = (lev < lev.shift(63)).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_nihit_252d_slope_v096_signal(netinc):
    pos = (netinc > 0).astype(float); depth = _f34_soft_pos(netinc, 126).clip(lower=0)
    bse = pos.rolling(252, min_periods=126).mean() - 0.5 + 0.05 * depth.rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roastab_252d_slope_v097_signal(roa):
    sd = roa.rolling(252, min_periods=126).std(); mn = roa.rolling(252, min_periods=126).mean().abs()
    bse = -np.tanh(sd / mn.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmstab_252d_slope_v098_signal(grossmargin):
    sd = grossmargin.rolling(252, min_periods=126).std(); mn = grossmargin.rolling(252, min_periods=126).mean().abs()
    bse = -np.tanh(10.0 * sd / mn.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfsemi_252d_slope_v099_signal(ncfo):
    g = _pctchg(ncfo, 21); downs = g.where(g < 0, 0.0)
    semi = (downs ** 2).rolling(252, min_periods=126).mean() ** 0.5
    bse = -np.tanh(10.0 * semi)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levstab_252d_slope_v100_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    sd = lev.rolling(252, min_periods=126).std(); mn = lev.rolling(252, min_periods=126).mean().abs()
    bse = -np.tanh(5.0 * sd / mn.replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_bstrust_252d_slope_v101_signal(debt, assets, currentratio, sharesbas):
    lev = _f34_leverage(debt, assets)
    c5 = -np.tanh(252.0 * _rollslope(lev, 252, 126) / lev.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c6 = np.tanh(252.0 * _rollslope(currentratio, 252, 126) / currentratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c7 = -np.tanh(252.0 * _rollslope(sharesbas, 252, 126) / sharesbas.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    bse = (c5 + c6 + c7) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_opqual_252d_slope_v102_signal(roa, grossmargin, assetturnover):
    c3 = np.tanh(252.0 * _rollslope(roa, 252, 126) / roa.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c8 = np.tanh(252.0 * _rollslope(grossmargin, 252, 126) / grossmargin.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c9 = np.tanh(252.0 * _rollslope(assetturnover, 252, 126) / assetturnover.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    bse = (c3 + c8 + c9) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cashqual_252d_slope_v103_signal(ncfo, netinc):
    pos = _f34_soft_pos(ncfo, 252); accr = _f34_soft_gt(ncfo, netinc, 252)
    sd = ncfo.rolling(252, min_periods=126).std(); mn = ncfo.rolling(252, min_periods=126).mean().abs()
    stab = -np.tanh(sd / mn.replace(0, np.nan))
    bse = (pos + accr + stab) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_hitcomp_252d_slope_v104_signal(roa, grossmargin, assetturnover, currentratio, ncfo, netinc, debt, assets):
    h3 = (roa > roa.shift(63)).astype(float); h8 = (grossmargin > grossmargin.shift(63)).astype(float)
    h9 = (assetturnover > assetturnover.shift(63)).astype(float); h6 = (currentratio > currentratio.shift(63)).astype(float)
    h4 = (ncfo > netinc).astype(float); lev = _f34_leverage(debt, assets); h5 = (lev < lev.shift(63)).astype(float)
    raw = (h3 + h8 + h9 + h6 + h4 + h5) / 6.0
    bse = raw.rolling(126, min_periods=63).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_minimprove_126d_slope_v105_signal(roa, grossmargin, assetturnover):
    c3 = _f34_soft_up(roa, 126, 126); c8 = _f34_soft_up(grossmargin, 126, 126); c9 = _f34_soft_up(assetturnover, 126, 126)
    stacked = pd.concat([c3, c8, c9], axis=1)
    bse = stacked.median(axis=1) - stacked.min(axis=1)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roaimpxlvl_126d_slope_v106_signal(roa, netinc, assets):
    impr = _f34_soft_up(roa, 63, 126); lvl = np.tanh(2.0 * _safe_div(netinc, assets))
    bse = (impr * np.sign(lvl)).rolling(21, min_periods=10).mean() + 0.2 * lvl
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmxatolvl_252d_slope_v107_signal(grossmargin, assetturnover):
    dgm = _f34_soft_up(grossmargin, 252, 252); atolvl = np.tanh(_z(assetturnover, 252))
    bse = dgm + 0.5 * dgm * atolvl
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_debtburden_252d_slope_v108_signal(debt, assets, netinc):
    burden = _safe_div(debt, netinc)
    bse = -np.tanh(0.5 * _chg(burden, 252) / burden.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrxroalvl_126d_slope_v109_signal(ncfo, netinc, assets):
    accrg = _pctchg(_safe_div(ncfo - netinc, assets).abs() + 1e-9, 126)
    roalvl = np.tanh(3.0 * _safe_div(netinc, assets))
    bse = np.tanh(accrg) * (0.5 + 0.5 * np.sign(roalvl))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_currnetdil_252d_slope_v110_signal(currentratio, sharesbas):
    liqps = _safe_div(currentratio, sharesbas)
    bse = np.tanh(3.0 * _pctchg(liqps, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsmom_63d_slope_v111_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126); c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 63, 126); c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 63, 126); c6 = _f34_soft_up(currentratio, 63, 126)
    c8 = _f34_soft_up(grossmargin, 63, 126); c9 = _f34_soft_up(assetturnover, 63, 126)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    bse = fs - fs.shift(63)
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsvol_252d_slope_v112_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126); c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252); c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 126, 252); c6 = _f34_soft_up(currentratio, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252); c9 = _f34_soft_up(assetturnover, 126, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    bse = fs.rolling(252, min_periods=126).std()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsdisp_252d_slope_v113_signal(netinc, ncfo, roa, assets, debt, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8 + c9) / 7.0
    bse = fs - fs.ewm(span=126, min_periods=63).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsregime_252d_slope_v114_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    comps = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    stacked = pd.concat(comps, axis=1)
    bse = stacked.median(axis=1) - stacked.mean(axis=1)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsdd_252d_slope_v115_signal(netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    bse = fs - fs.rolling(252, min_periods=126).max()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dupontlead_252d_slope_v116_signal(grossmargin, assetturnover):
    bse = _f34_soft_up(grossmargin, 252, 252) - _f34_soft_up(assetturnover, 252, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roaimplied_252d_slope_v117_signal(grossmargin, assetturnover, roa):
    implied = grossmargin * assetturnover
    gap = _safe_div(roa - implied, implied.abs().rolling(252, min_periods=126).mean())
    bse = np.tanh(gap)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dupontgrow_252d_slope_v118_signal(grossmargin, assetturnover):
    prod = grossmargin * assetturnover
    bse = _z(prod, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roa2y_504d_slope_v119_signal(roa):
    bse = _f34_soft_up(roa, 504, 504)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_lev2y_504d_slope_v120_signal(debt, assets):
    bse = _f34_soft_down(_f34_leverage(debt, assets), 504, 504)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gm2y_504d_slope_v121_signal(grossmargin):
    bse = _f34_soft_up(grossmargin, 504, 504)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roaaccel_126d_slope_v122_signal(roa):
    d = _chg(roa, 126); accel = d - d.shift(126); sc = roa.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(accel / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmaccel_126d_slope_v123_signal(grossmargin):
    d = _chg(grossmargin, 126); accel = d - d.shift(126); sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    bse = np.tanh(accel / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levaccel_126d_slope_v124_signal(debt, assets):
    lev = _f34_leverage(debt, assets); d = _chg(lev, 126); accel = d - d.shift(126)
    sc = lev.abs().rolling(252, min_periods=126).mean()
    bse = -np.tanh(accel / sc.replace(0, np.nan))
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cespread_126d_slope_v125_signal(ncfo, netinc, assets):
    spread = _safe_div(ncfo - netinc, assets)
    bse = spread.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_proflevratio_252d_slope_v126_signal(netinc, assets, debt):
    roaq = _safe_div(netinc, assets); lev = _f34_leverage(debt, assets); ratio = _safe_div(roaq, lev)
    bse = np.tanh(ratio / ratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_liqturn_252d_slope_v127_signal(currentratio, assetturnover):
    bse = -np.tanh(2.0 * _pctchg(_safe_div(currentratio, assetturnover), 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_gmatospread_252d_slope_v128_signal(grossmargin, assetturnover):
    bse = np.tanh(_z(grossmargin, 252) - _z(assetturnover, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfdebt_252d_slope_v129_signal(ncfo, debt):
    bse = np.tanh(2.0 * _pctchg(_safe_div(ncfo, debt), 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_proftally_252d_slope_v130_signal(netinc, ncfo, roa, assets):
    s = ((netinc > 0).astype(float) + (ncfo > 0).astype(float) + (_chg(roa, 252) > 0).astype(float) + (ncfo > netinc).astype(float))
    jitter = (_z(_safe_div(netinc, assets), 252)) * 0.02
    bse = (s + jitter).rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_levtally_252d_slope_v131_signal(debt, assets, currentratio, sharesbas):
    lev = _f34_leverage(debt, assets)
    s = ((_chg(lev, 252) < 0).astype(float) + (_chg(currentratio, 252) > 0).astype(float) + (_chg(sharesbas, 252) <= 0).astype(float))
    jitter = (_z(currentratio, 252)) * 0.02
    bse = (s + jitter).rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_efftally_252d_slope_v132_signal(grossmargin, assetturnover):
    s = ((_chg(grossmargin, 252) > 0).astype(float) + (_chg(assetturnover, 252) > 0).astype(float))
    jitter = (_z(grossmargin, 252)) * 0.02
    bse = (s + jitter).rolling(63, min_periods=21).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fulltally_252d_slope_v133_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    lev = _f34_leverage(debt, assets)
    s = ((netinc > 0).astype(float) + (ncfo > 0).astype(float) + (_chg(roa, 252) > 0).astype(float)
         + (ncfo > netinc).astype(float) + (_chg(lev, 252) < 0).astype(float) + (_chg(currentratio, 252) > 0).astype(float)
         + (_chg(sharesbas, 252) <= 0).astype(float) + (_chg(grossmargin, 252) > 0).astype(float) + (_chg(assetturnover, 252) > 0).astype(float))
    jitter = (_z(_safe_div(ncfo, assets), 252)) * 0.03
    bse = (s + jitter).rolling(126, min_periods=63).mean()
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_hqimprover_126d_slope_v134_signal(netinc, ncfo, roa, assets):
    a = _f34_soft_pos(netinc, 126); b2 = _f34_soft_up(roa, 126, 126); c = _f34_soft_gt(ncfo, netinc, 126)
    weak = pd.concat([a, b2, c], axis=1).min(axis=1)
    bse = weak.rolling(63, min_periods=21).mean()
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fragility_126d_slope_v135_signal(debt, assets, grossmargin):
    levrank = _f34_leverage(debt, assets).rolling(252, min_periods=126).rank(pct=True)
    margdet = (_f34_soft_down(grossmargin, 126, 126) + 1) / 2
    bse = -(levrank * margdet).rolling(21, min_periods=10).mean() + 0.25
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_turnaround_252d_slope_v136_signal(roa, grossmargin, netinc, assets):
    weak = (-np.tanh(3.0 * _safe_div(netinc, assets)) + 1) / 2
    impr = (_f34_soft_up(roa, 252, 252) + _f34_soft_up(grossmargin, 252, 252)) / 2.0
    bse = weak * ((impr + 1) / 2) - 0.25
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_selffund_252d_slope_v137_signal(ncfo, assets, sharesbas, debt):
    cf = np.tanh(3.0 * _safe_div(ncfo, assets)); nodil = _f34_soft_down(sharesbas, 252, 252)
    delev = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    bse = (cf + nodil + delev) / 3.0
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_qualitygate_126d_slope_v138_signal(roa, ncfo, netinc):
    droa = _f34_soft_up(roa, 126, 126)
    gate = (_f34_soft_gt(ncfo, netinc, 126) > 0).astype(float)
    bse = (droa * gate).rolling(21, min_periods=10).mean()
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_strengthgate_126d_slope_v139_signal(grossmargin, debt, assets):
    gmrank = grossmargin.rolling(252, min_periods=126).rank(pct=True)
    levrank = _f34_leverage(debt, assets).rolling(252, min_periods=126).rank(pct=True)
    bse = gmrank - levrank
    result = _roc(bse, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsrank756_252d_slope_v140_signal(netinc, ncfo, roa, assets, debt, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252); c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8 + c9) / 7.0
    bse = fs.rolling(756, min_periods=252).rank(pct=True) - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_diffusion_252d_slope_v141_signal(roa, grossmargin, assetturnover, currentratio, ncfo, assets):
    cfroa = _safe_div(ncfo, assets); diff = None
    for s in [roa, grossmargin, assetturnover, currentratio, cfroa]:
        z = (s > s.rolling(252, min_periods=126).mean()).astype(float)
        diff = z if diff is None else diff + z
    jitter = _z(roa, 252) * 0.02
    bse = (diff / 5.0 + jitter).rolling(21, min_periods=10).mean() - 0.5
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_fsyoy_252d_slope_v142_signal(netinc, ncfo, roa, assets, currentratio, grossmargin):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252); c4 = _f34_soft_gt(ncfo, netinc, 252)
    c6 = _f34_soft_up(currentratio, 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c6 + c8) / 6.0
    bse = fs - fs.shift(252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_roaminuscf_252d_slope_v143_signal(netinc, ncfo, assets):
    roaq = _safe_div(netinc, assets); cfroa = _safe_div(ncfo, assets)
    bse = -roaq.rolling(252, min_periods=126).corr(cfroa)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_netsolv_252d_slope_v144_signal(debt, assets, currentratio):
    risk = _safe_div(_f34_leverage(debt, assets), currentratio)
    bse = -np.tanh(_z(risk, 252))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_cfaccrete_252d_slope_v145_signal(ncfo, sharesbas):
    cfps = _safe_div(ncfo, sharesbas)
    bse = _z(cfps, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_conviction_252d_slope_v146_signal(netinc, ncfo, roa, assets, debt, grossmargin):
    l1 = np.tanh(2.0 * _safe_div(netinc, assets)); l2 = np.tanh(2.0 * _safe_div(ncfo, assets))
    l5 = -np.tanh(_z(_f34_leverage(debt, assets), 252)); l8 = np.tanh(_z(grossmargin, 252))
    levels = (l1 + l2 + l5 + l8) / 4.0; disp = pd.concat([l1, l2, l5, l8], axis=1).std(axis=1)
    bse = levels * (1.0 - disp.clip(upper=1.0))
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_dureffic_252d_slope_v147_signal(assetturnover, grossmargin):
    dato = _f34_soft_up(assetturnover, 252, 252)
    sd = grossmargin.rolling(252, min_periods=126).std(); mn = grossmargin.rolling(252, min_periods=126).mean().abs()
    stab = (1.0 - np.tanh(10.0 * sd / mn.replace(0, np.nan)))
    bse = dato * stab
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_accrreliab_252d_slope_v148_signal(roa, ncfo, assets):
    cfroa = _safe_div(ncfo, assets)
    bse = roa.rolling(252, min_periods=126).corr(cfroa)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_imppersist_252d_slope_v149_signal(roa, grossmargin, assetturnover, currentratio):
    c3 = _f34_soft_up(roa, 252, 252); c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252); c6 = _f34_soft_up(currentratio, 252, 252)
    fs = (c3 + c8 + c9 + c6) / 4.0
    pos = (fs > 0).astype(float)
    bse = pos.rolling(252, min_periods=126).mean() - 0.5 + 0.05 * fs
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34pf_f34_piotroski_fscore_healthindex_252d_slope_v150_signal(netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252); c2 = _f34_soft_pos(ncfo, 252)
    c3 = np.tanh(252.0 * _rollslope(roa, 252, 126) / roa.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = -np.tanh(252.0 * _rollslope(_f34_leverage(debt, assets), 252, 126) / _f34_leverage(debt, assets).abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c6 = np.tanh(252.0 * _rollslope(currentratio, 252, 126) / currentratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = np.tanh(252.0 * _rollslope(grossmargin, 252, 126) / grossmargin.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c9 = np.tanh(252.0 * _rollslope(assetturnover, 252, 126) / assetturnover.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    bse = _z(fs, 252)
    result = _roc(bse, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34pf_f34_piotroski_fscore_posni_252d_slope_v001_signal,
    f34pf_f34_piotroski_fscore_posnism_63d_slope_v002_signal,
    f34pf_f34_piotroski_fscore_nivol_252d_slope_v003_signal,
    f34pf_f34_piotroski_fscore_posocf_252d_slope_v004_signal,
    f34pf_f34_piotroski_fscore_posocfa_252d_slope_v005_signal,
    f34pf_f34_piotroski_fscore_posocffrac_252d_slope_v006_signal,
    f34pf_f34_piotroski_fscore_droa_252d_slope_v007_signal,
    f34pf_f34_piotroski_fscore_droah_126d_slope_v008_signal,
    f34pf_f34_piotroski_fscore_droasyn_252d_slope_v009_signal,
    f34pf_f34_piotroski_fscore_accr_252d_slope_v010_signal,
    f34pf_f34_piotroski_fscore_accra_252d_slope_v011_signal,
    f34pf_f34_piotroski_fscore_accrsm_63d_slope_v012_signal,
    f34pf_f34_piotroski_fscore_dlev_252d_slope_v013_signal,
    f34pf_f34_piotroski_fscore_dlevh_126d_slope_v014_signal,
    f34pf_f34_piotroski_fscore_paydownstreak_252d_slope_v015_signal,
    f34pf_f34_piotroski_fscore_dcurr_252d_slope_v016_signal,
    f34pf_f34_piotroski_fscore_dcurrq_63d_slope_v017_signal,
    f34pf_f34_piotroski_fscore_currlvl_252d_slope_v018_signal,
    f34pf_f34_piotroski_fscore_nodil_252d_slope_v019_signal,
    f34pf_f34_piotroski_fscore_nodilh_126d_slope_v020_signal,
    f34pf_f34_piotroski_fscore_buybackcons_252d_slope_v021_signal,
    f34pf_f34_piotroski_fscore_dgm_252d_slope_v022_signal,
    f34pf_f34_piotroski_fscore_dgmq_63d_slope_v023_signal,
    f34pf_f34_piotroski_fscore_gmlvl_252d_slope_v024_signal,
    f34pf_f34_piotroski_fscore_dato_252d_slope_v025_signal,
    f34pf_f34_piotroski_fscore_datoh_126d_slope_v026_signal,
    f34pf_f34_piotroski_fscore_atolvl_252d_slope_v027_signal,
    f34pf_f34_piotroski_fscore_fscore9_252d_slope_v028_signal,
    f34pf_f34_piotroski_fscore_fscorehard_252d_slope_v029_signal,
    f34pf_f34_piotroski_fscore_fscore9h_126d_slope_v030_signal,
    f34pf_f34_piotroski_fscore_profsub_252d_slope_v031_signal,
    f34pf_f34_piotroski_fscore_levsub_252d_slope_v032_signal,
    f34pf_f34_piotroski_fscore_effsub_252d_slope_v033_signal,
    f34pf_f34_piotroski_fscore_qualcore_252d_slope_v034_signal,
    f34pf_f34_piotroski_fscore_imptrio_63d_slope_v035_signal,
    f34pf_f34_piotroski_fscore_wmag_252d_slope_v036_signal,
    f34pf_f34_piotroski_fscore_wprof_252d_slope_v037_signal,
    f34pf_f34_piotroski_fscore_weff_252d_slope_v038_signal,
    f34pf_f34_piotroski_fscore_wrecency_63d_slope_v039_signal,
    f34pf_f34_piotroski_fscore_rollmean_252d_slope_v040_signal,
    f34pf_f34_piotroski_fscore_fschg_252d_slope_v041_signal,
    f34pf_f34_piotroski_fscore_fsrank_504d_slope_v042_signal,
    f34pf_f34_piotroski_fscore_strongcnt_252d_slope_v043_signal,
    f34pf_f34_piotroski_fscore_compdisp_252d_slope_v044_signal,
    f34pf_f34_piotroski_fscore_weaklink_252d_slope_v045_signal,
    f34pf_f34_piotroski_fscore_strongpillar_252d_slope_v046_signal,
    f34pf_f34_piotroski_fscore_roalvl_252d_slope_v047_signal,
    f34pf_f34_piotroski_fscore_cfroalvl_252d_slope_v048_signal,
    f34pf_f34_piotroski_fscore_accrlvl_252d_slope_v049_signal,
    f34pf_f34_piotroski_fscore_levlvl_252d_slope_v050_signal,
    f34pf_f34_piotroski_fscore_currconvex_63d_slope_v051_signal,
    f34pf_f34_piotroski_fscore_dilaccel_252d_slope_v052_signal,
    f34pf_f34_piotroski_fscore_gmtrend_126d_slope_v053_signal,
    f34pf_f34_piotroski_fscore_atoslope_252d_slope_v054_signal,
    f34pf_f34_piotroski_fscore_debtcover_252d_slope_v055_signal,
    f34pf_f34_piotroski_fscore_accrxdroa_126d_slope_v056_signal,
    f34pf_f34_piotroski_fscore_gmxato_252d_slope_v057_signal,
    f34pf_f34_piotroski_fscore_currxnodil_252d_slope_v058_signal,
    f34pf_f34_piotroski_fscore_cashmargin_252d_slope_v059_signal,
    f34pf_f34_piotroski_fscore_breadth_252d_slope_v060_signal,
    f34pf_f34_piotroski_fscore_accrrev_252d_slope_v061_signal,
    f34pf_f34_piotroski_fscore_dupontagree_252d_slope_v062_signal,
    f34pf_f34_piotroski_fscore_finqual_252d_slope_v063_signal,
    f34pf_f34_piotroski_fscore_profpersist_504d_slope_v064_signal,
    f34pf_f34_piotroski_fscore_accrpersist_504d_slope_v065_signal,
    f34pf_f34_piotroski_fscore_fsaccel_252d_slope_v066_signal,
    f34pf_f34_piotroski_fscore_levadjroa_252d_slope_v067_signal,
    f34pf_f34_piotroski_fscore_qmd_252d_slope_v068_signal,
    f34pf_f34_piotroski_fscore_fsz_504d_slope_v069_signal,
    f34pf_f34_piotroski_fscore_distqual_252d_slope_v070_signal,
    f34pf_f34_piotroski_fscore_cashgrowth_252d_slope_v071_signal,
    f34pf_f34_piotroski_fscore_allfronts_252d_slope_v072_signal,
    f34pf_f34_piotroski_fscore_ecconverge_252d_slope_v073_signal,
    f34pf_f34_piotroski_fscore_logitfs_126d_slope_v074_signal,
    f34pf_f34_piotroski_fscore_fslongtrend_252d_slope_v075_signal,
    f34pf_f34_piotroski_fscore_nirank_504d_slope_v076_signal,
    f34pf_f34_piotroski_fscore_cfrank_504d_slope_v077_signal,
    f34pf_f34_piotroski_fscore_roacross_126d_slope_v078_signal,
    f34pf_f34_piotroski_fscore_accrz_252d_slope_v079_signal,
    f34pf_f34_piotroski_fscore_levrank_504d_slope_v080_signal,
    f34pf_f34_piotroski_fscore_currrank_504d_slope_v081_signal,
    f34pf_f34_piotroski_fscore_shareoverhang_504d_slope_v082_signal,
    f34pf_f34_piotroski_fscore_gmrank_504d_slope_v083_signal,
    f34pf_f34_piotroski_fscore_atorank_504d_slope_v084_signal,
    f34pf_f34_piotroski_fscore_roaslope_252d_slope_v085_signal,
    f34pf_f34_piotroski_fscore_gmslope_126d_slope_v086_signal,
    f34pf_f34_piotroski_fscore_currslope_252d_slope_v087_signal,
    f34pf_f34_piotroski_fscore_levslope_252d_slope_v088_signal,
    f34pf_f34_piotroski_fscore_shareslope_252d_slope_v089_signal,
    f34pf_f34_piotroski_fscore_cfroaslope_252d_slope_v090_signal,
    f34pf_f34_piotroski_fscore_roahit_252d_slope_v091_signal,
    f34pf_f34_piotroski_fscore_gmhit_252d_slope_v092_signal,
    f34pf_f34_piotroski_fscore_atohit_252d_slope_v093_signal,
    f34pf_f34_piotroski_fscore_accrhit_252d_slope_v094_signal,
    f34pf_f34_piotroski_fscore_levhit_252d_slope_v095_signal,
    f34pf_f34_piotroski_fscore_nihit_252d_slope_v096_signal,
    f34pf_f34_piotroski_fscore_roastab_252d_slope_v097_signal,
    f34pf_f34_piotroski_fscore_gmstab_252d_slope_v098_signal,
    f34pf_f34_piotroski_fscore_cfsemi_252d_slope_v099_signal,
    f34pf_f34_piotroski_fscore_levstab_252d_slope_v100_signal,
    f34pf_f34_piotroski_fscore_bstrust_252d_slope_v101_signal,
    f34pf_f34_piotroski_fscore_opqual_252d_slope_v102_signal,
    f34pf_f34_piotroski_fscore_cashqual_252d_slope_v103_signal,
    f34pf_f34_piotroski_fscore_hitcomp_252d_slope_v104_signal,
    f34pf_f34_piotroski_fscore_minimprove_126d_slope_v105_signal,
    f34pf_f34_piotroski_fscore_roaimpxlvl_126d_slope_v106_signal,
    f34pf_f34_piotroski_fscore_gmxatolvl_252d_slope_v107_signal,
    f34pf_f34_piotroski_fscore_debtburden_252d_slope_v108_signal,
    f34pf_f34_piotroski_fscore_accrxroalvl_126d_slope_v109_signal,
    f34pf_f34_piotroski_fscore_currnetdil_252d_slope_v110_signal,
    f34pf_f34_piotroski_fscore_fsmom_63d_slope_v111_signal,
    f34pf_f34_piotroski_fscore_fsvol_252d_slope_v112_signal,
    f34pf_f34_piotroski_fscore_fsdisp_252d_slope_v113_signal,
    f34pf_f34_piotroski_fscore_fsregime_252d_slope_v114_signal,
    f34pf_f34_piotroski_fscore_fsdd_252d_slope_v115_signal,
    f34pf_f34_piotroski_fscore_dupontlead_252d_slope_v116_signal,
    f34pf_f34_piotroski_fscore_roaimplied_252d_slope_v117_signal,
    f34pf_f34_piotroski_fscore_dupontgrow_252d_slope_v118_signal,
    f34pf_f34_piotroski_fscore_roa2y_504d_slope_v119_signal,
    f34pf_f34_piotroski_fscore_lev2y_504d_slope_v120_signal,
    f34pf_f34_piotroski_fscore_gm2y_504d_slope_v121_signal,
    f34pf_f34_piotroski_fscore_roaaccel_126d_slope_v122_signal,
    f34pf_f34_piotroski_fscore_gmaccel_126d_slope_v123_signal,
    f34pf_f34_piotroski_fscore_levaccel_126d_slope_v124_signal,
    f34pf_f34_piotroski_fscore_cespread_126d_slope_v125_signal,
    f34pf_f34_piotroski_fscore_proflevratio_252d_slope_v126_signal,
    f34pf_f34_piotroski_fscore_liqturn_252d_slope_v127_signal,
    f34pf_f34_piotroski_fscore_gmatospread_252d_slope_v128_signal,
    f34pf_f34_piotroski_fscore_cfdebt_252d_slope_v129_signal,
    f34pf_f34_piotroski_fscore_proftally_252d_slope_v130_signal,
    f34pf_f34_piotroski_fscore_levtally_252d_slope_v131_signal,
    f34pf_f34_piotroski_fscore_efftally_252d_slope_v132_signal,
    f34pf_f34_piotroski_fscore_fulltally_252d_slope_v133_signal,
    f34pf_f34_piotroski_fscore_hqimprover_126d_slope_v134_signal,
    f34pf_f34_piotroski_fscore_fragility_126d_slope_v135_signal,
    f34pf_f34_piotroski_fscore_turnaround_252d_slope_v136_signal,
    f34pf_f34_piotroski_fscore_selffund_252d_slope_v137_signal,
    f34pf_f34_piotroski_fscore_qualitygate_126d_slope_v138_signal,
    f34pf_f34_piotroski_fscore_strengthgate_126d_slope_v139_signal,
    f34pf_f34_piotroski_fscore_fsrank756_252d_slope_v140_signal,
    f34pf_f34_piotroski_fscore_diffusion_252d_slope_v141_signal,
    f34pf_f34_piotroski_fscore_fsyoy_252d_slope_v142_signal,
    f34pf_f34_piotroski_fscore_roaminuscf_252d_slope_v143_signal,
    f34pf_f34_piotroski_fscore_netsolv_252d_slope_v144_signal,
    f34pf_f34_piotroski_fscore_cfaccrete_252d_slope_v145_signal,
    f34pf_f34_piotroski_fscore_conviction_252d_slope_v146_signal,
    f34pf_f34_piotroski_fscore_dureffic_252d_slope_v147_signal,
    f34pf_f34_piotroski_fscore_accrreliab_252d_slope_v148_signal,
    f34pf_f34_piotroski_fscore_imppersist_252d_slope_v149_signal,
    f34pf_f34_piotroski_fscore_healthindex_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_PIOTROSKI_FSCORE_REGISTRY_001_150 = REGISTRY


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

    netinc = _fund(101, base=5e7, drift=0.03, vol=0.08, allow_neg=True, n=n).rename("netinc")
    ncfo = _fund(102, base=7e7, drift=0.03, vol=0.07, allow_neg=True, n=n).rename("ncfo")
    roa = _fund(103, base=0.08, drift=0.01, vol=0.06, allow_neg=True, n=n).rename("roa")
    assets = _fund(104, base=1e9, drift=0.02, vol=0.03, allow_neg=False, n=n).rename("assets")
    debt = _fund(105, base=4e8, drift=0.015, vol=0.05, allow_neg=False, n=n).rename("debt")
    currentratio = _fund(106, base=1.8, drift=0.005, vol=0.04, allow_neg=False, n=n).rename("currentratio")
    sharesbas = _fund(107, base=1e8, drift=0.005, vol=0.02, allow_neg=False, n=n).rename("sharesbas")
    grossmargin = _fund(108, base=0.42, drift=0.004, vol=0.03, allow_neg=False, n=n).rename("grossmargin")
    assetturnover = _fund(109, base=0.9, drift=0.006, vol=0.04, allow_neg=False, n=n).rename("assetturnover")

    cols = {
        "netinc": netinc, "ncfo": ncfo, "roa": roa, "assets": assets, "debt": debt,
        "currentratio": currentratio, "sharesbas": sharesbas, "grossmargin": grossmargin,
        "assetturnover": assetturnover,
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

    print("OK f34_piotroski_fscore_2nd_derivatives_001_150_claude: %d features pass" % n_features)
