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


def _slp(b, w):
    # 1st math derivative (slope) via w-day finite difference
    return (b - b.shift(w)) / float(w)


def _jrk(b, w):
    # 2nd math derivative (jerk) via w-day finite second difference
    return (b - 2.0 * b.shift(w) + b.shift(2 * w)) / float(w * w)


# ===== folder domain primitives (ownership concentration & breadth) =====
def _f43_total_holders(fndholders, undholders, prfholders, dbtholders):
    return fndholders + undholders + prfholders + dbtholders


def _f43_share(part, fndholders, undholders, prfholders, dbtholders):
    tot = fndholders + undholders + prfholders + dbtholders
    return part / tot.replace(0, np.nan)


def _f43_hhi(fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    return (fndholders / tot) ** 2 + (undholders / tot) ** 2 + (prfholders / tot) ** 2 + (dbtholders / tot) ** 2


def _f43_entropy(fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = (part / tot).clip(lower=1e-12)
        term = -s * np.log(s)
        out = term if out is None else out + term
    return out


def _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders):
    dumb = (undholders + prfholders + dbtholders).replace(0, np.nan)
    return fndholders / dumb


def _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    return totalvalue / tot


def f43oc_f43_ownership_concentration_breadth_breadthraw_21d_jerk_v001_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC breadth/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_breadthema_42d_jerk_v002_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC breadth/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_breadthzsc_63d_jerk_v003_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC breadth/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_breadthdisp_126d_jerk_v004_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC breadth/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_breadthavg_189d_jerk_v005_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC breadth/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_breadthrnk_252d_jerk_v006_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC breadth/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndshareraw_21d_jerk_v007_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC fndshare/raw
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndshareema_42d_jerk_v008_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fndshare/ema
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndsharezsc_63d_jerk_v009_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fndshare/zsc
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndsharedisp_126d_jerk_v010_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC fndshare/disp
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndshareavg_189d_jerk_v011_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC fndshare/avg
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndsharernk_252d_jerk_v012_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fndshare/rnk
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undshareraw_21d_jerk_v013_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC undshare/raw
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undshareema_42d_jerk_v014_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC undshare/ema
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undsharezsc_63d_jerk_v015_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC undshare/zsc
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undsharedisp_126d_jerk_v016_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC undshare/disp
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undshareavg_189d_jerk_v017_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC undshare/avg
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undsharernk_252d_jerk_v018_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC undshare/rnk
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfshareraw_21d_jerk_v019_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC prfshare/raw
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfshareema_42d_jerk_v020_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC prfshare/ema
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfsharezsc_63d_jerk_v021_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC prfshare/zsc
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfsharedisp_126d_jerk_v022_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC prfshare/disp
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfshareavg_189d_jerk_v023_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC prfshare/avg
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfsharernk_252d_jerk_v024_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC prfshare/rnk
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtshareraw_21d_jerk_v025_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC dbtshare/raw
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtshareema_42d_jerk_v026_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC dbtshare/ema
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtsharezsc_63d_jerk_v027_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC dbtshare/zsc
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtsharedisp_126d_jerk_v028_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC dbtshare/disp
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtshareavg_189d_jerk_v029_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC dbtshare/avg
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtsharernk_252d_jerk_v030_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC dbtshare/rnk
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2shareraw_21d_jerk_v031_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC top2share/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2shareema_42d_jerk_v032_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC top2share/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2sharezsc_63d_jerk_v033_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC top2share/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2sharedisp_126d_jerk_v034_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC top2share/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2shareavg_189d_jerk_v035_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC top2share/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_top2sharernk_252d_jerk_v036_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC top2share/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rk = sh.rank(axis=1, ascending=False)
    b = sh.where(rk <= 2).sum(axis=1)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropyraw_21d_jerk_v037_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC entropy/raw
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropyema_42d_jerk_v038_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC entropy/ema
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropyzsc_63d_jerk_v039_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC entropy/zsc
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropydisp_126d_jerk_v040_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC entropy/disp
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropyavg_189d_jerk_v041_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC entropy/avg
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_entropyrnk_252d_jerk_v042_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC entropy/rnk
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconcraw_21d_jerk_v043_signal(percentoftotal):  # jerk 5d-ROC topconc/raw
    b = percentoftotal
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconcema_42d_jerk_v044_signal(percentoftotal):  # jerk 21d-ROC topconc/ema
    b = percentoftotal
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconczsc_63d_jerk_v045_signal(percentoftotal):  # jerk 21d-ROC topconc/zsc
    b = percentoftotal
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconcdisp_126d_jerk_v046_signal(percentoftotal):  # jerk 63d-ROC topconc/disp
    b = percentoftotal
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconcavg_189d_jerk_v047_signal(percentoftotal):  # jerk 63d-ROC topconc/avg
    b = percentoftotal
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_topconcrnk_252d_jerk_v048_signal(percentoftotal):  # jerk 21d-ROC topconc/rnk
    b = percentoftotal
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginiraw_21d_jerk_v049_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC mixgini/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginiema_42d_jerk_v050_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC mixgini/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginizsc_63d_jerk_v051_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC mixgini/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginidisp_126d_jerk_v052_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC mixgini/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginiavg_189d_jerk_v053_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC mixgini/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_mixginirnk_252d_jerk_v054_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC mixgini/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sl = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = sum((sl[a] - sl[c]).abs() for a in range(4) for c in range(a + 1, 4))
    b = mad / 6.0
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvalraw_21d_jerk_v055_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC avgval/raw
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvalema_42d_jerk_v056_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC avgval/ema
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvalzsc_63d_jerk_v057_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC avgval/zsc
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvaldisp_126d_jerk_v058_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC avgval/disp
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvalavg_189d_jerk_v059_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC avgval/avg
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_avgvalrnk_252d_jerk_v060_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC avgval/rnk
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconcraw_21d_jerk_v061_signal(totalvalue, percentoftotal):  # jerk 5d-ROC valconc/raw
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconcema_42d_jerk_v062_signal(totalvalue, percentoftotal):  # jerk 21d-ROC valconc/ema
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconczsc_63d_jerk_v063_signal(totalvalue, percentoftotal):  # jerk 21d-ROC valconc/zsc
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconcdisp_126d_jerk_v064_signal(totalvalue, percentoftotal):  # jerk 63d-ROC valconc/disp
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconcavg_189d_jerk_v065_signal(totalvalue, percentoftotal):  # jerk 63d-ROC valconc/avg
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valconcrnk_252d_jerk_v066_signal(totalvalue, percentoftotal):  # jerk 21d-ROC valconc/rnk
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountraw_21d_jerk_v067_signal(fndholders):  # jerk 5d-ROC fndcount/raw
    b = np.log(fndholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountema_42d_jerk_v068_signal(fndholders):  # jerk 21d-ROC fndcount/ema
    b = np.log(fndholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountzsc_63d_jerk_v069_signal(fndholders):  # jerk 21d-ROC fndcount/zsc
    b = np.log(fndholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountdisp_126d_jerk_v070_signal(fndholders):  # jerk 63d-ROC fndcount/disp
    b = np.log(fndholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountavg_189d_jerk_v071_signal(fndholders):  # jerk 63d-ROC fndcount/avg
    b = np.log(fndholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndcountrnk_252d_jerk_v072_signal(fndholders):  # jerk 21d-ROC fndcount/rnk
    b = np.log(fndholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountraw_21d_jerk_v073_signal(dbtholders):  # jerk 5d-ROC dbtcount/raw
    b = np.log(dbtholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountema_42d_jerk_v074_signal(dbtholders):  # jerk 21d-ROC dbtcount/ema
    b = np.log(dbtholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountzsc_63d_jerk_v075_signal(dbtholders):  # jerk 21d-ROC dbtcount/zsc
    b = np.log(dbtholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountdisp_126d_jerk_v076_signal(dbtholders):  # jerk 63d-ROC dbtcount/disp
    b = np.log(dbtholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountavg_189d_jerk_v077_signal(dbtholders):  # jerk 63d-ROC dbtcount/avg
    b = np.log(dbtholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtcountrnk_252d_jerk_v078_signal(dbtholders):  # jerk 21d-ROC dbtcount/rnk
    b = np.log(dbtholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountraw_21d_jerk_v079_signal(prfholders):  # jerk 5d-ROC prfcount/raw
    b = np.log(prfholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountema_42d_jerk_v080_signal(prfholders):  # jerk 21d-ROC prfcount/ema
    b = np.log(prfholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountzsc_63d_jerk_v081_signal(prfholders):  # jerk 21d-ROC prfcount/zsc
    b = np.log(prfholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountdisp_126d_jerk_v082_signal(prfholders):  # jerk 63d-ROC prfcount/disp
    b = np.log(prfholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountavg_189d_jerk_v083_signal(prfholders):  # jerk 63d-ROC prfcount/avg
    b = np.log(prfholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_prfcountrnk_252d_jerk_v084_signal(prfholders):  # jerk 21d-ROC prfcount/rnk
    b = np.log(prfholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountraw_21d_jerk_v085_signal(undholders):  # jerk 5d-ROC undcount/raw
    b = np.log(undholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountema_42d_jerk_v086_signal(undholders):  # jerk 21d-ROC undcount/ema
    b = np.log(undholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountzsc_63d_jerk_v087_signal(undholders):  # jerk 21d-ROC undcount/zsc
    b = np.log(undholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountdisp_126d_jerk_v088_signal(undholders):  # jerk 63d-ROC undcount/disp
    b = np.log(undholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountavg_189d_jerk_v089_signal(undholders):  # jerk 63d-ROC undcount/avg
    b = np.log(undholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_undcountrnk_252d_jerk_v090_signal(undholders):  # jerk 21d-ROC undcount/rnk
    b = np.log(undholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtraw_21d_jerk_v091_signal(fndholders, dbtholders):  # jerk 5d-ROC fnddbt/raw
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtema_42d_jerk_v092_signal(fndholders, dbtholders):  # jerk 21d-ROC fnddbt/ema
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtzsc_63d_jerk_v093_signal(fndholders, dbtholders):  # jerk 21d-ROC fnddbt/zsc
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtdisp_126d_jerk_v094_signal(fndholders, dbtholders):  # jerk 63d-ROC fnddbt/disp
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtavg_189d_jerk_v095_signal(fndholders, dbtholders):  # jerk 63d-ROC fnddbt/avg
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddbtrnk_252d_jerk_v096_signal(fndholders, dbtholders):  # jerk 21d-ROC fnddbt/rnk
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthraw_21d_jerk_v097_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC valbreadth/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthema_42d_jerk_v098_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC valbreadth/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthzsc_63d_jerk_v099_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC valbreadth/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthdisp_126d_jerk_v100_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC valbreadth/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthavg_189d_jerk_v101_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC valbreadth/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valbreadthrnk_252d_jerk_v102_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC valbreadth/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfraw_21d_jerk_v103_signal(dbtholders, prfholders):  # jerk 5d-ROC dbtprf/raw
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfema_42d_jerk_v104_signal(dbtholders, prfholders):  # jerk 21d-ROC dbtprf/ema
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfzsc_63d_jerk_v105_signal(dbtholders, prfholders):  # jerk 21d-ROC dbtprf/zsc
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfdisp_126d_jerk_v106_signal(dbtholders, prfholders):  # jerk 63d-ROC dbtprf/disp
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfavg_189d_jerk_v107_signal(dbtholders, prfholders):  # jerk 63d-ROC dbtprf/avg
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_dbtprfrnk_252d_jerk_v108_signal(dbtholders, prfholders):  # jerk 21d-ROC dbtprf/rnk
    b = np.log(dbtholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomeshareraw_21d_jerk_v109_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC incomeshare/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomeshareema_42d_jerk_v110_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC incomeshare/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomesharezsc_63d_jerk_v111_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC incomeshare/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomesharedisp_126d_jerk_v112_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC incomeshare/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomeshareavg_189d_jerk_v113_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC incomeshare/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomesharernk_252d_jerk_v114_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC incomeshare/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders + dbtholders) / tot
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndundraw_21d_jerk_v115_signal(fndholders, undholders):  # jerk 5d-ROC fndund/raw
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndundema_42d_jerk_v116_signal(fndholders, undholders):  # jerk 21d-ROC fndund/ema
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndundzsc_63d_jerk_v117_signal(fndholders, undholders):  # jerk 21d-ROC fndund/zsc
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndunddisp_126d_jerk_v118_signal(fndholders, undholders):  # jerk 63d-ROC fndund/disp
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndundavg_189d_jerk_v119_signal(fndholders, undholders):  # jerk 63d-ROC fndund/avg
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fndundrnk_252d_jerk_v120_signal(fndholders, undholders):  # jerk 21d-ROC fndund/rnk
    b = np.log(fndholders.replace(0, np.nan) / undholders.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfndraw_21d_jerk_v121_signal(totalvalue, fndholders):  # jerk 5d-ROC valperfnd/raw
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfndema_42d_jerk_v122_signal(totalvalue, fndholders):  # jerk 21d-ROC valperfnd/ema
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfndzsc_63d_jerk_v123_signal(totalvalue, fndholders):  # jerk 21d-ROC valperfnd/zsc
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfnddisp_126d_jerk_v124_signal(totalvalue, fndholders):  # jerk 63d-ROC valperfnd/disp
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfndavg_189d_jerk_v125_signal(totalvalue, fndholders):  # jerk 63d-ROC valperfnd/avg
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_valperfndrnk_252d_jerk_v126_signal(totalvalue, fndholders):  # jerk 21d-ROC valperfnd/rnk
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvalueraw_21d_jerk_v127_signal(totalvalue):  # jerk 5d-ROC totalvalue/raw
    b = np.log(totalvalue.replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvalueema_42d_jerk_v128_signal(totalvalue):  # jerk 21d-ROC totalvalue/ema
    b = np.log(totalvalue.replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvaluezsc_63d_jerk_v129_signal(totalvalue):  # jerk 21d-ROC totalvalue/zsc
    b = np.log(totalvalue.replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvaluedisp_126d_jerk_v130_signal(totalvalue):  # jerk 63d-ROC totalvalue/disp
    b = np.log(totalvalue.replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvalueavg_189d_jerk_v131_signal(totalvalue):  # jerk 63d-ROC totalvalue/avg
    b = np.log(totalvalue.replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_totalvaluernk_252d_jerk_v132_signal(totalvalue):  # jerk 21d-ROC totalvalue/rnk
    b = np.log(totalvalue.replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgapraw_21d_jerk_v133_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC fnddomgap/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgapema_42d_jerk_v134_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fnddomgap/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgapzsc_63d_jerk_v135_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fnddomgap/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgapdisp_126d_jerk_v136_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC fnddomgap/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgapavg_189d_jerk_v137_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC fnddomgap/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_fnddomgaprnk_252d_jerk_v138_signal(fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC fnddomgap/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomraw_21d_jerk_v139_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 5d-ROC concdom/raw
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomema_42d_jerk_v140_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC concdom/ema
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomzsc_63d_jerk_v141_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC concdom/zsc
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomdisp_126d_jerk_v142_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC concdom/disp
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomavg_189d_jerk_v143_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 63d-ROC concdom/avg
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_concdomrnk_252d_jerk_v144_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):  # jerk 21d-ROC concdom/rnk
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log((percentoftotal * tot).replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountraw_21d_jerk_v145_signal(prfholders, dbtholders):  # jerk 5d-ROC incomecount/raw
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    result = _jrk(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountema_42d_jerk_v146_signal(prfholders, dbtholders):  # jerk 21d-ROC incomecount/ema
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    b = b.ewm(span=42, min_periods=max(2, 42 // 2)).mean()
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountzsc_63d_jerk_v147_signal(prfholders, dbtholders):  # jerk 21d-ROC incomecount/zsc
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    b = _z(b, 63)
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountdisp_126d_jerk_v148_signal(prfholders, dbtholders):  # jerk 63d-ROC incomecount/disp
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    b = b - b.ewm(span=126, min_periods=max(2, 126 // 2)).mean()
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountavg_189d_jerk_v149_signal(prfholders, dbtholders):  # jerk 63d-ROC incomecount/avg
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    b = _mean(b, 189)
    result = _jrk(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43oc_f43_ownership_concentration_breadth_incomecountrnk_252d_jerk_v150_signal(prfholders, dbtholders):  # jerk 21d-ROC incomecount/rnk
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    b = b.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = _jrk(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43oc_f43_ownership_concentration_breadth_breadthraw_21d_jerk_v001_signal,
    f43oc_f43_ownership_concentration_breadth_breadthema_42d_jerk_v002_signal,
    f43oc_f43_ownership_concentration_breadth_breadthzsc_63d_jerk_v003_signal,
    f43oc_f43_ownership_concentration_breadth_breadthdisp_126d_jerk_v004_signal,
    f43oc_f43_ownership_concentration_breadth_breadthavg_189d_jerk_v005_signal,
    f43oc_f43_ownership_concentration_breadth_breadthrnk_252d_jerk_v006_signal,
    f43oc_f43_ownership_concentration_breadth_fndshareraw_21d_jerk_v007_signal,
    f43oc_f43_ownership_concentration_breadth_fndshareema_42d_jerk_v008_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharezsc_63d_jerk_v009_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharedisp_126d_jerk_v010_signal,
    f43oc_f43_ownership_concentration_breadth_fndshareavg_189d_jerk_v011_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharernk_252d_jerk_v012_signal,
    f43oc_f43_ownership_concentration_breadth_undshareraw_21d_jerk_v013_signal,
    f43oc_f43_ownership_concentration_breadth_undshareema_42d_jerk_v014_signal,
    f43oc_f43_ownership_concentration_breadth_undsharezsc_63d_jerk_v015_signal,
    f43oc_f43_ownership_concentration_breadth_undsharedisp_126d_jerk_v016_signal,
    f43oc_f43_ownership_concentration_breadth_undshareavg_189d_jerk_v017_signal,
    f43oc_f43_ownership_concentration_breadth_undsharernk_252d_jerk_v018_signal,
    f43oc_f43_ownership_concentration_breadth_prfshareraw_21d_jerk_v019_signal,
    f43oc_f43_ownership_concentration_breadth_prfshareema_42d_jerk_v020_signal,
    f43oc_f43_ownership_concentration_breadth_prfsharezsc_63d_jerk_v021_signal,
    f43oc_f43_ownership_concentration_breadth_prfsharedisp_126d_jerk_v022_signal,
    f43oc_f43_ownership_concentration_breadth_prfshareavg_189d_jerk_v023_signal,
    f43oc_f43_ownership_concentration_breadth_prfsharernk_252d_jerk_v024_signal,
    f43oc_f43_ownership_concentration_breadth_dbtshareraw_21d_jerk_v025_signal,
    f43oc_f43_ownership_concentration_breadth_dbtshareema_42d_jerk_v026_signal,
    f43oc_f43_ownership_concentration_breadth_dbtsharezsc_63d_jerk_v027_signal,
    f43oc_f43_ownership_concentration_breadth_dbtsharedisp_126d_jerk_v028_signal,
    f43oc_f43_ownership_concentration_breadth_dbtshareavg_189d_jerk_v029_signal,
    f43oc_f43_ownership_concentration_breadth_dbtsharernk_252d_jerk_v030_signal,
    f43oc_f43_ownership_concentration_breadth_top2shareraw_21d_jerk_v031_signal,
    f43oc_f43_ownership_concentration_breadth_top2shareema_42d_jerk_v032_signal,
    f43oc_f43_ownership_concentration_breadth_top2sharezsc_63d_jerk_v033_signal,
    f43oc_f43_ownership_concentration_breadth_top2sharedisp_126d_jerk_v034_signal,
    f43oc_f43_ownership_concentration_breadth_top2shareavg_189d_jerk_v035_signal,
    f43oc_f43_ownership_concentration_breadth_top2sharernk_252d_jerk_v036_signal,
    f43oc_f43_ownership_concentration_breadth_entropyraw_21d_jerk_v037_signal,
    f43oc_f43_ownership_concentration_breadth_entropyema_42d_jerk_v038_signal,
    f43oc_f43_ownership_concentration_breadth_entropyzsc_63d_jerk_v039_signal,
    f43oc_f43_ownership_concentration_breadth_entropydisp_126d_jerk_v040_signal,
    f43oc_f43_ownership_concentration_breadth_entropyavg_189d_jerk_v041_signal,
    f43oc_f43_ownership_concentration_breadth_entropyrnk_252d_jerk_v042_signal,
    f43oc_f43_ownership_concentration_breadth_topconcraw_21d_jerk_v043_signal,
    f43oc_f43_ownership_concentration_breadth_topconcema_42d_jerk_v044_signal,
    f43oc_f43_ownership_concentration_breadth_topconczsc_63d_jerk_v045_signal,
    f43oc_f43_ownership_concentration_breadth_topconcdisp_126d_jerk_v046_signal,
    f43oc_f43_ownership_concentration_breadth_topconcavg_189d_jerk_v047_signal,
    f43oc_f43_ownership_concentration_breadth_topconcrnk_252d_jerk_v048_signal,
    f43oc_f43_ownership_concentration_breadth_mixginiraw_21d_jerk_v049_signal,
    f43oc_f43_ownership_concentration_breadth_mixginiema_42d_jerk_v050_signal,
    f43oc_f43_ownership_concentration_breadth_mixginizsc_63d_jerk_v051_signal,
    f43oc_f43_ownership_concentration_breadth_mixginidisp_126d_jerk_v052_signal,
    f43oc_f43_ownership_concentration_breadth_mixginiavg_189d_jerk_v053_signal,
    f43oc_f43_ownership_concentration_breadth_mixginirnk_252d_jerk_v054_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalraw_21d_jerk_v055_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalema_42d_jerk_v056_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalzsc_63d_jerk_v057_signal,
    f43oc_f43_ownership_concentration_breadth_avgvaldisp_126d_jerk_v058_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalavg_189d_jerk_v059_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalrnk_252d_jerk_v060_signal,
    f43oc_f43_ownership_concentration_breadth_valconcraw_21d_jerk_v061_signal,
    f43oc_f43_ownership_concentration_breadth_valconcema_42d_jerk_v062_signal,
    f43oc_f43_ownership_concentration_breadth_valconczsc_63d_jerk_v063_signal,
    f43oc_f43_ownership_concentration_breadth_valconcdisp_126d_jerk_v064_signal,
    f43oc_f43_ownership_concentration_breadth_valconcavg_189d_jerk_v065_signal,
    f43oc_f43_ownership_concentration_breadth_valconcrnk_252d_jerk_v066_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountraw_21d_jerk_v067_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountema_42d_jerk_v068_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountzsc_63d_jerk_v069_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountdisp_126d_jerk_v070_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountavg_189d_jerk_v071_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountrnk_252d_jerk_v072_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountraw_21d_jerk_v073_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountema_42d_jerk_v074_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountzsc_63d_jerk_v075_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountdisp_126d_jerk_v076_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountavg_189d_jerk_v077_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountrnk_252d_jerk_v078_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountraw_21d_jerk_v079_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountema_42d_jerk_v080_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountzsc_63d_jerk_v081_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountdisp_126d_jerk_v082_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountavg_189d_jerk_v083_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountrnk_252d_jerk_v084_signal,
    f43oc_f43_ownership_concentration_breadth_undcountraw_21d_jerk_v085_signal,
    f43oc_f43_ownership_concentration_breadth_undcountema_42d_jerk_v086_signal,
    f43oc_f43_ownership_concentration_breadth_undcountzsc_63d_jerk_v087_signal,
    f43oc_f43_ownership_concentration_breadth_undcountdisp_126d_jerk_v088_signal,
    f43oc_f43_ownership_concentration_breadth_undcountavg_189d_jerk_v089_signal,
    f43oc_f43_ownership_concentration_breadth_undcountrnk_252d_jerk_v090_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtraw_21d_jerk_v091_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtema_42d_jerk_v092_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtzsc_63d_jerk_v093_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtdisp_126d_jerk_v094_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtavg_189d_jerk_v095_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtrnk_252d_jerk_v096_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthraw_21d_jerk_v097_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthema_42d_jerk_v098_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthzsc_63d_jerk_v099_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthdisp_126d_jerk_v100_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthavg_189d_jerk_v101_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthrnk_252d_jerk_v102_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfraw_21d_jerk_v103_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfema_42d_jerk_v104_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfzsc_63d_jerk_v105_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfdisp_126d_jerk_v106_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfavg_189d_jerk_v107_signal,
    f43oc_f43_ownership_concentration_breadth_dbtprfrnk_252d_jerk_v108_signal,
    f43oc_f43_ownership_concentration_breadth_incomeshareraw_21d_jerk_v109_signal,
    f43oc_f43_ownership_concentration_breadth_incomeshareema_42d_jerk_v110_signal,
    f43oc_f43_ownership_concentration_breadth_incomesharezsc_63d_jerk_v111_signal,
    f43oc_f43_ownership_concentration_breadth_incomesharedisp_126d_jerk_v112_signal,
    f43oc_f43_ownership_concentration_breadth_incomeshareavg_189d_jerk_v113_signal,
    f43oc_f43_ownership_concentration_breadth_incomesharernk_252d_jerk_v114_signal,
    f43oc_f43_ownership_concentration_breadth_fndundraw_21d_jerk_v115_signal,
    f43oc_f43_ownership_concentration_breadth_fndundema_42d_jerk_v116_signal,
    f43oc_f43_ownership_concentration_breadth_fndundzsc_63d_jerk_v117_signal,
    f43oc_f43_ownership_concentration_breadth_fndunddisp_126d_jerk_v118_signal,
    f43oc_f43_ownership_concentration_breadth_fndundavg_189d_jerk_v119_signal,
    f43oc_f43_ownership_concentration_breadth_fndundrnk_252d_jerk_v120_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndraw_21d_jerk_v121_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndema_42d_jerk_v122_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndzsc_63d_jerk_v123_signal,
    f43oc_f43_ownership_concentration_breadth_valperfnddisp_126d_jerk_v124_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndavg_189d_jerk_v125_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndrnk_252d_jerk_v126_signal,
    f43oc_f43_ownership_concentration_breadth_totalvalueraw_21d_jerk_v127_signal,
    f43oc_f43_ownership_concentration_breadth_totalvalueema_42d_jerk_v128_signal,
    f43oc_f43_ownership_concentration_breadth_totalvaluezsc_63d_jerk_v129_signal,
    f43oc_f43_ownership_concentration_breadth_totalvaluedisp_126d_jerk_v130_signal,
    f43oc_f43_ownership_concentration_breadth_totalvalueavg_189d_jerk_v131_signal,
    f43oc_f43_ownership_concentration_breadth_totalvaluernk_252d_jerk_v132_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapraw_21d_jerk_v133_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapema_42d_jerk_v134_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapzsc_63d_jerk_v135_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapdisp_126d_jerk_v136_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapavg_189d_jerk_v137_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgaprnk_252d_jerk_v138_signal,
    f43oc_f43_ownership_concentration_breadth_concdomraw_21d_jerk_v139_signal,
    f43oc_f43_ownership_concentration_breadth_concdomema_42d_jerk_v140_signal,
    f43oc_f43_ownership_concentration_breadth_concdomzsc_63d_jerk_v141_signal,
    f43oc_f43_ownership_concentration_breadth_concdomdisp_126d_jerk_v142_signal,
    f43oc_f43_ownership_concentration_breadth_concdomavg_189d_jerk_v143_signal,
    f43oc_f43_ownership_concentration_breadth_concdomrnk_252d_jerk_v144_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountraw_21d_jerk_v145_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountema_42d_jerk_v146_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountzsc_63d_jerk_v147_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountdisp_126d_jerk_v148_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountavg_189d_jerk_v149_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountrnk_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_OWNERSHIP_CONCENTRATION_BREADTH_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    def _jit(seed, sd):
        g = np.random.default_rng(seed)
        e = g.normal(0.0, sd, n)
        out = np.empty(n)
        acc = 0.0
        for k in range(n):
            acc = 0.85 * acc + e[k]
            out[k] = acc
        return np.exp(out)

    fndholders = pd.Series(np.maximum(_fund(101, 120.0, 0.018, 0.07).values * _jit(201, 0.045), 1.0), name="fndholders")
    undholders = pd.Series(np.maximum(_fund(102, 85.0, -0.004, 0.08).values * _jit(202, 0.060), 1.0), name="undholders")
    prfholders = pd.Series(np.maximum(_fund(103, 70.0, 0.002, 0.09).values * _jit(203, 0.070), 1.0), name="prfholders")
    dbtholders = pd.Series(np.maximum(_fund(104, 95.0, -0.001, 0.075).values * _jit(204, 0.055), 1.0), name="dbtholders")
    shrholders = pd.Series(np.maximum(_fund(105, 300.0, 0.012, 0.06).values * _jit(205, 0.030), 1.0), name="shrholders")
    percentoftotal = pd.Series(np.clip(_fund(106, 0.18, 0.003, 0.05).values * _jit(206, 0.040), 0.001, 0.95), name="percentoftotal")
    totalvalue = pd.Series(np.maximum(_fund(107, 5e8, 0.018, 0.05).values * _jit(207, 0.035), 1.0), name="totalvalue")

    cols = {
        "fndholders": fndholders, "undholders": undholders, "prfholders": prfholders,
        "dbtholders": dbtholders, "shrholders": shrholders,
        "percentoftotal": percentoftotal, "totalvalue": totalvalue,
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

    print("OK f43_ownership_concentration_breadth_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
