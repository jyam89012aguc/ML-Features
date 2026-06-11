import inspect
import numpy as np
import pandas as pd

"""2nd math derivatives (jerk): change-of-change of an f24 base."""


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def f24pi_f24_profitability_inflection_netinc_profitshare126_63d_jerk_v001_signal(netinc):
    pos = netinc.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = netinc.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_profitshare126_63d_jerk_v002_signal(ebit):
    pos = ebit.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = ebit.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_profitshare126_63d_jerk_v003_signal(opinc):
    pos = opinc.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = opinc.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_profitshare126_63d_jerk_v004_signal(ncfo):
    pos = ncfo.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = ncfo.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_profitshare126_63d_jerk_v005_signal(eps):
    pos = eps.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = eps.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_profitshare126_63d_jerk_v006_signal(retearn):
    pos = retearn.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = retearn.abs().rolling(126, min_periods=63).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_profitshare252_63d_jerk_v007_signal(netinc):
    pos = netinc.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = netinc.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_profitshare252_63d_jerk_v008_signal(ebit):
    pos = ebit.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = ebit.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_profitshare252_63d_jerk_v009_signal(opinc):
    pos = opinc.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = opinc.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_profitshare252_63d_jerk_v010_signal(ncfo):
    pos = ncfo.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = ncfo.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_profitshare252_63d_jerk_v011_signal(eps):
    pos = eps.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = eps.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_profitshare252_63d_jerk_v012_signal(retearn):
    pos = retearn.clip(lower=0).rolling(252, min_periods=126).sum()
    gross = retearn.abs().rolling(252, min_periods=126).sum()
    base = pos / gross.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_posfrac252_63d_jerk_v013_signal(opinc):
    base = (opinc > 0).astype(float).rolling(252, min_periods=126).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_posfrac252_63d_jerk_v014_signal(ncfo):
    base = (ncfo > 0).astype(float).rolling(252, min_periods=126).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_posfrac252_63d_jerk_v015_signal(eps):
    base = (eps > 0).astype(float).rolling(252, min_periods=126).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_posfrac252_63d_jerk_v016_signal(retearn):
    base = (retearn > 0).astype(float).rolling(252, min_periods=126).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_recency63_63d_jerk_v017_signal(netinc):
    base = (netinc > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_recency63_63d_jerk_v018_signal(ebit):
    base = (ebit > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_recency63_63d_jerk_v019_signal(opinc):
    base = (opinc > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_recency63_63d_jerk_v020_signal(ncfo):
    base = (ncfo > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_recency63_63d_jerk_v021_signal(eps):
    base = (eps > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_recency63_63d_jerk_v022_signal(retearn):
    base = (retearn > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_recency126_63d_jerk_v023_signal(ebit):
    base = (ebit > 0).astype(float).ewm(span=126, min_periods=42).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_recency126_63d_jerk_v024_signal(opinc):
    base = (opinc > 0).astype(float).ewm(span=126, min_periods=42).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_recency126_63d_jerk_v025_signal(eps):
    base = (eps > 0).astype(float).ewm(span=126, min_periods=42).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_recency126_63d_jerk_v026_signal(retearn):
    base = (retearn > 0).astype(float).ewm(span=126, min_periods=42).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_signmagz252_63d_jerk_v027_signal(netinc):
    sm = np.sign(netinc) * np.sqrt(np.abs(netinc))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_signmagz252_63d_jerk_v028_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(np.abs(ebit))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_signmagz252_63d_jerk_v029_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_signmagz252_63d_jerk_v030_signal(ncfo):
    sm = np.sign(ncfo) * np.sqrt(np.abs(ncfo))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_signmagz252_63d_jerk_v031_signal(eps):
    sm = np.sign(eps) * np.sqrt(np.abs(eps))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_signmagz252_63d_jerk_v032_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    mn = sm.rolling(252, min_periods=126).mean()
    sd = sm.rolling(252, min_periods=126).std()
    base = (sm - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_slopescaled126_63d_jerk_v033_signal(opinc):
    sl = _slope(opinc, 126)
    scale = opinc.abs().rolling(252, min_periods=126).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_slopescaled126_63d_jerk_v034_signal(ncfo):
    sl = _slope(ncfo, 126)
    scale = ncfo.abs().rolling(252, min_periods=126).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_slopescaled126_63d_jerk_v035_signal(retearn):
    sl = _slope(retearn, 126)
    scale = retearn.abs().rolling(252, min_periods=126).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_slopescaled63_63d_jerk_v036_signal(netinc):
    sl = _slope(netinc, 63)
    scale = netinc.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_slopescaled63_63d_jerk_v037_signal(ebit):
    sl = _slope(ebit, 63)
    scale = ebit.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_slopescaled63_63d_jerk_v038_signal(opinc):
    sl = _slope(opinc, 63)
    scale = opinc.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_slopescaled63_63d_jerk_v039_signal(ncfo):
    sl = _slope(ncfo, 63)
    scale = ncfo.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_slopescaled63_63d_jerk_v040_signal(eps):
    sl = _slope(eps, 63)
    scale = eps.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_slopescaled63_63d_jerk_v041_signal(retearn):
    sl = _slope(retearn, 63)
    scale = retearn.abs().rolling(126, min_periods=63).mean()
    base = sl / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_logclose63_63d_jerk_v042_signal(netinc):
    deficit = (-netinc).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_logclose63_63d_jerk_v043_signal(ebit):
    deficit = (-ebit).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_logclose63_63d_jerk_v044_signal(opinc):
    deficit = (-opinc).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_logclose63_63d_jerk_v045_signal(ncfo):
    deficit = (-ncfo).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_logclose63_63d_jerk_v046_signal(eps):
    deficit = (-eps).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_logclose63_63d_jerk_v047_signal(retearn):
    deficit = (-retearn).clip(lower=0)
    base = np.log((deficit.shift(63) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_logclose126_63d_jerk_v048_signal(netinc):
    deficit = (-netinc).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_logclose126_63d_jerk_v049_signal(ebit):
    deficit = (-ebit).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_logclose126_63d_jerk_v050_signal(opinc):
    deficit = (-opinc).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_logclose126_63d_jerk_v051_signal(ncfo):
    deficit = (-ncfo).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_logclose126_63d_jerk_v052_signal(eps):
    deficit = (-eps).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_logclose126_63d_jerk_v053_signal(retearn):
    deficit = (-retearn).clip(lower=0)
    base = np.log((deficit.shift(126) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_worstlossrelief_63d_jerk_v054_signal(netinc):
    depth = (-netinc).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    base = 1.0 - cur / worst.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_worstlossrelief_63d_jerk_v055_signal(ebit):
    depth = (-ebit).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    base = 1.0 - cur / worst.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_worstlossrelief_63d_jerk_v056_signal(ncfo):
    depth = (-ncfo).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    base = 1.0 - cur / worst.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_worstlossrelief_63d_jerk_v057_signal(eps):
    depth = (-eps).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    base = 1.0 - cur / worst.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_worstlossrelief_63d_jerk_v058_signal(retearn):
    depth = (-retearn).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    base = 1.0 - cur / worst.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_disp252_63d_jerk_v059_signal(netinc):
    sm = np.sign(netinc) * np.sqrt(np.abs(netinc))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_disp252_63d_jerk_v060_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(np.abs(ebit))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_disp252_63d_jerk_v061_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_disp252_63d_jerk_v062_signal(ncfo):
    sm = np.sign(ncfo) * np.sqrt(np.abs(ncfo))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_disp252_63d_jerk_v063_signal(eps):
    sm = np.sign(eps) * np.sqrt(np.abs(eps))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_disp252_63d_jerk_v064_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    sd = sm.rolling(252, min_periods=126).std()
    scale = sm.abs().rolling(252, min_periods=126).mean()
    base = sd / scale.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_crossupdepth252_63d_jerk_v065_signal(netinc):
    ev = ((netinc > 0) & (netinc.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = netinc.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_crossupdepth252_63d_jerk_v066_signal(ebit):
    ev = ((ebit > 0) & (ebit.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = ebit.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_crossupdepth252_63d_jerk_v067_signal(opinc):
    ev = ((opinc > 0) & (opinc.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = opinc.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_crossupdepth252_63d_jerk_v068_signal(ncfo):
    ev = ((ncfo > 0) & (ncfo.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = ncfo.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_crossupdepth252_63d_jerk_v069_signal(eps):
    ev = ((eps > 0) & (eps.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = eps.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_crossupdepth252_63d_jerk_v070_signal(retearn):
    ev = ((retearn > 0) & (retearn.shift(1) <= 0)).astype(float)
    cnt = ev.rolling(252, min_periods=126).sum()
    depth = retearn.clip(lower=0)
    relief = depth / depth.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = cnt + 0.3 * relief.rolling(21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_breakeven252_63d_jerk_v071_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).mean()
    base = -(netinc.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_breakeven252_63d_jerk_v072_signal(ebit):
    scale = ebit.abs().rolling(252, min_periods=126).mean()
    base = -(ebit.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_breakeven252_63d_jerk_v073_signal(opinc):
    scale = opinc.abs().rolling(252, min_periods=126).mean()
    base = -(opinc.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_breakeven252_63d_jerk_v074_signal(ncfo):
    scale = ncfo.abs().rolling(252, min_periods=126).mean()
    base = -(ncfo.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_breakeven252_63d_jerk_v075_signal(eps):
    scale = eps.abs().rolling(252, min_periods=126).mean()
    base = -(eps.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_breakeven252_63d_jerk_v076_signal(retearn):
    scale = retearn.abs().rolling(252, min_periods=126).mean()
    base = -(retearn.abs() / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_signmag_yoy_63d_jerk_v077_signal(netinc):
    sm = np.sign(netinc) * np.sqrt(np.abs(netinc))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_signmag_yoy_63d_jerk_v078_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(np.abs(ebit))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_signmag_yoy_63d_jerk_v079_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_signmag_yoy_63d_jerk_v080_signal(ncfo):
    sm = np.sign(ncfo) * np.sqrt(np.abs(ncfo))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_signmag_yoy_63d_jerk_v081_signal(eps):
    sm = np.sign(eps) * np.sqrt(np.abs(eps))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_signmag_yoy_63d_jerk_v082_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    base = sm - sm.shift(252)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_sharetrend126_63d_jerk_v083_signal(netinc):
    pos = netinc.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = netinc.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_sharetrend126_63d_jerk_v084_signal(ebit):
    pos = ebit.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = ebit.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_sharetrend126_63d_jerk_v085_signal(opinc):
    pos = opinc.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = opinc.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_sharetrend126_63d_jerk_v086_signal(ncfo):
    pos = ncfo.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = ncfo.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_sharetrend126_63d_jerk_v087_signal(eps):
    pos = eps.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = eps.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_sharetrend126_63d_jerk_v088_signal(retearn):
    pos = retearn.clip(lower=0).rolling(126, min_periods=63).sum()
    gross = retearn.abs().rolling(126, min_periods=63).sum()
    sh = pos / gross.replace(0, np.nan)
    base = sh - sh.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_recencyspread_63d_jerk_v089_signal(netinc):
    fast = (netinc > 0).astype(float).ewm(span=42, min_periods=14).mean()
    slow = (netinc > 0).astype(float).ewm(span=168, min_periods=56).mean()
    base = fast - slow
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_recencyspread_63d_jerk_v090_signal(opinc):
    fast = (opinc > 0).astype(float).ewm(span=42, min_periods=14).mean()
    slow = (opinc > 0).astype(float).ewm(span=168, min_periods=56).mean()
    base = fast - slow
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_recencyspread_63d_jerk_v091_signal(eps):
    fast = (eps > 0).astype(float).ewm(span=42, min_periods=14).mean()
    slow = (eps > 0).astype(float).ewm(span=168, min_periods=56).mean()
    base = fast - slow
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_recencyspread_63d_jerk_v092_signal(retearn):
    fast = (retearn > 0).astype(float).ewm(span=42, min_periods=14).mean()
    slow = (retearn > 0).astype(float).ewm(span=168, min_periods=56).mean()
    base = fast - slow
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_breakprox_med504_63d_jerk_v093_signal(retearn):
    scale = retearn.abs().rolling(504, min_periods=252).median()
    base = np.tanh(retearn / scale.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_profitdepthgrow_63d_jerk_v094_signal(opinc):
    depth = opinc.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    base = avg - avg.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_profitdepthgrow_63d_jerk_v095_signal(ncfo):
    depth = ncfo.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    base = avg - avg.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_profitdepthgrow_63d_jerk_v096_signal(eps):
    depth = eps.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    base = avg - avg.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_profitdepthgrow_63d_jerk_v097_signal(retearn):
    depth = retearn.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    base = avg - avg.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_inflect63_63d_jerk_v098_signal(netinc):
    sm = np.sign(netinc) * np.sqrt(np.abs(netinc))
    dd = sm.diff(63)
    base = dd - dd.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_inflect63_63d_jerk_v099_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(np.abs(ebit))
    dd = sm.diff(63)
    base = dd - dd.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_inflect63_63d_jerk_v100_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    dd = sm.diff(63)
    base = dd - dd.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_inflect63_63d_jerk_v101_signal(eps):
    sm = np.sign(eps) * np.sqrt(np.abs(eps))
    dd = sm.diff(63)
    base = dd - dd.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_inflect63_63d_jerk_v102_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    dd = sm.diff(63)
    base = dd - dd.shift(63)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_zscore126_63d_jerk_v103_signal(opinc):
    mn = opinc.rolling(126, min_periods=63).mean()
    sd = opinc.rolling(126, min_periods=63).std()
    base = (opinc - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_zscore126_63d_jerk_v104_signal(retearn):
    mn = retearn.rolling(126, min_periods=63).mean()
    sd = retearn.rolling(126, min_periods=63).std()
    base = (retearn - mn) / sd.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_posfrac126_63d_jerk_v105_signal(opinc):
    base = (opinc > 0).astype(float).rolling(126, min_periods=63).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_posfrac126_63d_jerk_v106_signal(ncfo):
    base = (ncfo > 0).astype(float).rolling(126, min_periods=63).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_posfrac126_63d_jerk_v107_signal(eps):
    base = (eps > 0).astype(float).rolling(126, min_periods=63).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_posfrac126_63d_jerk_v108_signal(retearn):
    base = (retearn > 0).astype(float).rolling(126, min_periods=63).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_slopevol126_63d_jerk_v109_signal(eps):
    sl = _slope(eps, 126)
    vol = eps.rolling(252, min_periods=126).std()
    base = sl / vol.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_signmag_q_63d_jerk_v110_signal(ebit):
    sm = np.sign(ebit) * np.sqrt(np.abs(ebit))
    base = sm - sm.shift(126)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_signmag_q_63d_jerk_v111_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    base = sm - sm.shift(126)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_signmag_q_63d_jerk_v112_signal(ncfo):
    sm = np.sign(ncfo) * np.sqrt(np.abs(ncfo))
    base = sm - sm.shift(126)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_signmag_q_63d_jerk_v113_signal(eps):
    sm = np.sign(eps) * np.sqrt(np.abs(eps))
    base = sm - sm.shift(126)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_signmag_q_63d_jerk_v114_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    base = sm - sm.shift(126)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_logclose252_63d_jerk_v115_signal(opinc):
    deficit = (-opinc).clip(lower=0)
    base = np.log((deficit.shift(252) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_logclose252_63d_jerk_v116_signal(ncfo):
    deficit = (-ncfo).clip(lower=0)
    base = np.log((deficit.shift(252) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_logclose252_63d_jerk_v117_signal(eps):
    deficit = (-eps).clip(lower=0)
    base = np.log((deficit.shift(252) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_logclose252_63d_jerk_v118_signal(retearn):
    deficit = (-retearn).clip(lower=0)
    base = np.log((deficit.shift(252) + 1.0) / (deficit + 1.0))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_ranklvl252_63d_jerk_v119_signal(opinc):
    sm = np.sign(opinc) * np.sqrt(np.abs(opinc))
    base = sm.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_ranklvl252_63d_jerk_v120_signal(retearn):
    sm = np.sign(retearn) * np.sqrt(np.abs(retearn))
    base = sm.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_bestprofitprog_63d_jerk_v121_signal(netinc):
    prof = netinc.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_bestprofitprog_63d_jerk_v122_signal(ebit):
    prof = ebit.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_bestprofitprog_63d_jerk_v123_signal(opinc):
    prof = opinc.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_bestprofitprog_63d_jerk_v124_signal(ncfo):
    prof = ncfo.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_bestprofitprog_63d_jerk_v125_signal(eps):
    prof = eps.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_bestprofitprog_63d_jerk_v126_signal(retearn):
    prof = retearn.clip(lower=0)
    best = prof.rolling(252, min_periods=126).max()
    cur = prof.rolling(21, min_periods=10).mean()
    base = cur / best.replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_zsmooth252_63d_jerk_v127_signal(retearn):
    mn = retearn.rolling(252, min_periods=126).mean()
    sd = retearn.rolling(252, min_periods=126).std()
    z = (retearn - mn) / sd.replace(0, np.nan)
    base = z.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_absnarrow126_63d_jerk_v128_signal(netinc):
    a = netinc.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_absnarrow126_63d_jerk_v129_signal(ebit):
    a = ebit.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_absnarrow126_63d_jerk_v130_signal(opinc):
    a = opinc.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_absnarrow126_63d_jerk_v131_signal(ncfo):
    a = ncfo.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_absnarrow126_63d_jerk_v132_signal(eps):
    a = eps.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_retearn_absnarrow126_63d_jerk_v133_signal(retearn):
    a = retearn.abs()
    avg = a.rolling(126, min_periods=63).mean()
    base = -(avg - avg.shift(63)) / avg.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_netinc_shareSpr126_63d_jerk_v134_signal(ebit, netinc):
    pa = ebit.clip(lower=0).rolling(126, min_periods=63).sum() / ebit.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    pb = netinc.clip(lower=0).rolling(126, min_periods=63).sum() / netinc.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    base = pa - pb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_ebit_shareSpr126_63d_jerk_v135_signal(ebit, opinc):
    pa = opinc.clip(lower=0).rolling(126, min_periods=63).sum() / opinc.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    pb = ebit.clip(lower=0).rolling(126, min_periods=63).sum() / ebit.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    base = pa - pb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_netinc_shareSpr126_63d_jerk_v136_signal(eps, netinc):
    pa = eps.clip(lower=0).rolling(126, min_periods=63).sum() / eps.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    pb = netinc.clip(lower=0).rolling(126, min_periods=63).sum() / netinc.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    base = pa - pb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_retearn_shareSpr126_63d_jerk_v137_signal(netinc, retearn):
    pa = netinc.clip(lower=0).rolling(126, min_periods=63).sum() / netinc.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    pb = retearn.clip(lower=0).rolling(126, min_periods=63).sum() / retearn.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    base = pa - pb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_ncfo_proxSpr252_63d_jerk_v138_signal(ncfo, netinc):
    sa = netinc.abs().rolling(252, min_periods=126).median()
    sb = ncfo.abs().rolling(252, min_periods=126).median()
    base = np.tanh(netinc / sa.replace(0, np.nan)) - np.tanh(ncfo / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_netinc_proxSpr252_63d_jerk_v139_signal(ebit, netinc):
    sa = ebit.abs().rolling(252, min_periods=126).median()
    sb = netinc.abs().rolling(252, min_periods=126).median()
    base = np.tanh(ebit / sa.replace(0, np.nan)) - np.tanh(netinc / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_ebit_proxSpr252_63d_jerk_v140_signal(ebit, opinc):
    sa = opinc.abs().rolling(252, min_periods=126).median()
    sb = ebit.abs().rolling(252, min_periods=126).median()
    base = np.tanh(opinc / sa.replace(0, np.nan)) - np.tanh(ebit / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_opinc_proxSpr252_63d_jerk_v141_signal(ncfo, opinc):
    sa = ncfo.abs().rolling(252, min_periods=126).median()
    sb = opinc.abs().rolling(252, min_periods=126).median()
    base = np.tanh(ncfo / sa.replace(0, np.nan)) - np.tanh(opinc / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_netinc_proxSpr252_63d_jerk_v142_signal(eps, netinc):
    sa = eps.abs().rolling(252, min_periods=126).median()
    sb = netinc.abs().rolling(252, min_periods=126).median()
    base = np.tanh(eps / sa.replace(0, np.nan)) - np.tanh(netinc / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_retearn_proxSpr252_63d_jerk_v143_signal(netinc, retearn):
    sa = netinc.abs().rolling(252, min_periods=126).median()
    sb = retearn.abs().rolling(252, min_periods=126).median()
    base = np.tanh(netinc / sa.replace(0, np.nan)) - np.tanh(retearn / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_retearn_proxSpr252_63d_jerk_v144_signal(ncfo, retearn):
    sa = ncfo.abs().rolling(252, min_periods=126).median()
    sb = retearn.abs().rolling(252, min_periods=126).median()
    base = np.tanh(ncfo / sa.replace(0, np.nan)) - np.tanh(retearn / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_ncfo_proxSpr252_63d_jerk_v145_signal(eps, ncfo):
    sa = eps.abs().rolling(252, min_periods=126).median()
    sb = ncfo.abs().rolling(252, min_periods=126).median()
    base = np.tanh(eps / sa.replace(0, np.nan)) - np.tanh(ncfo / sb.replace(0, np.nan))
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_netinc_ncfo_climbSpr126_63d_jerk_v146_signal(ncfo, netinc):
    sa = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sb = _slope(ncfo, 126) / ncfo.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = sa - sb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ebit_netinc_climbSpr126_63d_jerk_v147_signal(ebit, netinc):
    sa = _slope(ebit, 126) / ebit.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sb = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = sa - sb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_opinc_ebit_climbSpr126_63d_jerk_v148_signal(ebit, opinc):
    sa = _slope(opinc, 126) / opinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sb = _slope(ebit, 126) / ebit.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = sa - sb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_ncfo_opinc_climbSpr126_63d_jerk_v149_signal(ncfo, opinc):
    sa = _slope(ncfo, 126) / ncfo.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sb = _slope(opinc, 126) / opinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = sa - sb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24pi_f24_profitability_inflection_eps_netinc_climbSpr126_63d_jerk_v150_signal(eps, netinc):
    sa = _slope(eps, 126) / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sb = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = sa - sb
    d = base - base.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24pi_f24_profitability_inflection_netinc_profitshare126_63d_jerk_v001_signal,
    f24pi_f24_profitability_inflection_ebit_profitshare126_63d_jerk_v002_signal,
    f24pi_f24_profitability_inflection_opinc_profitshare126_63d_jerk_v003_signal,
    f24pi_f24_profitability_inflection_ncfo_profitshare126_63d_jerk_v004_signal,
    f24pi_f24_profitability_inflection_eps_profitshare126_63d_jerk_v005_signal,
    f24pi_f24_profitability_inflection_retearn_profitshare126_63d_jerk_v006_signal,
    f24pi_f24_profitability_inflection_netinc_profitshare252_63d_jerk_v007_signal,
    f24pi_f24_profitability_inflection_ebit_profitshare252_63d_jerk_v008_signal,
    f24pi_f24_profitability_inflection_opinc_profitshare252_63d_jerk_v009_signal,
    f24pi_f24_profitability_inflection_ncfo_profitshare252_63d_jerk_v010_signal,
    f24pi_f24_profitability_inflection_eps_profitshare252_63d_jerk_v011_signal,
    f24pi_f24_profitability_inflection_retearn_profitshare252_63d_jerk_v012_signal,
    f24pi_f24_profitability_inflection_opinc_posfrac252_63d_jerk_v013_signal,
    f24pi_f24_profitability_inflection_ncfo_posfrac252_63d_jerk_v014_signal,
    f24pi_f24_profitability_inflection_eps_posfrac252_63d_jerk_v015_signal,
    f24pi_f24_profitability_inflection_retearn_posfrac252_63d_jerk_v016_signal,
    f24pi_f24_profitability_inflection_netinc_recency63_63d_jerk_v017_signal,
    f24pi_f24_profitability_inflection_ebit_recency63_63d_jerk_v018_signal,
    f24pi_f24_profitability_inflection_opinc_recency63_63d_jerk_v019_signal,
    f24pi_f24_profitability_inflection_ncfo_recency63_63d_jerk_v020_signal,
    f24pi_f24_profitability_inflection_eps_recency63_63d_jerk_v021_signal,
    f24pi_f24_profitability_inflection_retearn_recency63_63d_jerk_v022_signal,
    f24pi_f24_profitability_inflection_ebit_recency126_63d_jerk_v023_signal,
    f24pi_f24_profitability_inflection_opinc_recency126_63d_jerk_v024_signal,
    f24pi_f24_profitability_inflection_eps_recency126_63d_jerk_v025_signal,
    f24pi_f24_profitability_inflection_retearn_recency126_63d_jerk_v026_signal,
    f24pi_f24_profitability_inflection_netinc_signmagz252_63d_jerk_v027_signal,
    f24pi_f24_profitability_inflection_ebit_signmagz252_63d_jerk_v028_signal,
    f24pi_f24_profitability_inflection_opinc_signmagz252_63d_jerk_v029_signal,
    f24pi_f24_profitability_inflection_ncfo_signmagz252_63d_jerk_v030_signal,
    f24pi_f24_profitability_inflection_eps_signmagz252_63d_jerk_v031_signal,
    f24pi_f24_profitability_inflection_retearn_signmagz252_63d_jerk_v032_signal,
    f24pi_f24_profitability_inflection_opinc_slopescaled126_63d_jerk_v033_signal,
    f24pi_f24_profitability_inflection_ncfo_slopescaled126_63d_jerk_v034_signal,
    f24pi_f24_profitability_inflection_retearn_slopescaled126_63d_jerk_v035_signal,
    f24pi_f24_profitability_inflection_netinc_slopescaled63_63d_jerk_v036_signal,
    f24pi_f24_profitability_inflection_ebit_slopescaled63_63d_jerk_v037_signal,
    f24pi_f24_profitability_inflection_opinc_slopescaled63_63d_jerk_v038_signal,
    f24pi_f24_profitability_inflection_ncfo_slopescaled63_63d_jerk_v039_signal,
    f24pi_f24_profitability_inflection_eps_slopescaled63_63d_jerk_v040_signal,
    f24pi_f24_profitability_inflection_retearn_slopescaled63_63d_jerk_v041_signal,
    f24pi_f24_profitability_inflection_netinc_logclose63_63d_jerk_v042_signal,
    f24pi_f24_profitability_inflection_ebit_logclose63_63d_jerk_v043_signal,
    f24pi_f24_profitability_inflection_opinc_logclose63_63d_jerk_v044_signal,
    f24pi_f24_profitability_inflection_ncfo_logclose63_63d_jerk_v045_signal,
    f24pi_f24_profitability_inflection_eps_logclose63_63d_jerk_v046_signal,
    f24pi_f24_profitability_inflection_retearn_logclose63_63d_jerk_v047_signal,
    f24pi_f24_profitability_inflection_netinc_logclose126_63d_jerk_v048_signal,
    f24pi_f24_profitability_inflection_ebit_logclose126_63d_jerk_v049_signal,
    f24pi_f24_profitability_inflection_opinc_logclose126_63d_jerk_v050_signal,
    f24pi_f24_profitability_inflection_ncfo_logclose126_63d_jerk_v051_signal,
    f24pi_f24_profitability_inflection_eps_logclose126_63d_jerk_v052_signal,
    f24pi_f24_profitability_inflection_retearn_logclose126_63d_jerk_v053_signal,
    f24pi_f24_profitability_inflection_netinc_worstlossrelief_63d_jerk_v054_signal,
    f24pi_f24_profitability_inflection_ebit_worstlossrelief_63d_jerk_v055_signal,
    f24pi_f24_profitability_inflection_ncfo_worstlossrelief_63d_jerk_v056_signal,
    f24pi_f24_profitability_inflection_eps_worstlossrelief_63d_jerk_v057_signal,
    f24pi_f24_profitability_inflection_retearn_worstlossrelief_63d_jerk_v058_signal,
    f24pi_f24_profitability_inflection_netinc_disp252_63d_jerk_v059_signal,
    f24pi_f24_profitability_inflection_ebit_disp252_63d_jerk_v060_signal,
    f24pi_f24_profitability_inflection_opinc_disp252_63d_jerk_v061_signal,
    f24pi_f24_profitability_inflection_ncfo_disp252_63d_jerk_v062_signal,
    f24pi_f24_profitability_inflection_eps_disp252_63d_jerk_v063_signal,
    f24pi_f24_profitability_inflection_retearn_disp252_63d_jerk_v064_signal,
    f24pi_f24_profitability_inflection_netinc_crossupdepth252_63d_jerk_v065_signal,
    f24pi_f24_profitability_inflection_ebit_crossupdepth252_63d_jerk_v066_signal,
    f24pi_f24_profitability_inflection_opinc_crossupdepth252_63d_jerk_v067_signal,
    f24pi_f24_profitability_inflection_ncfo_crossupdepth252_63d_jerk_v068_signal,
    f24pi_f24_profitability_inflection_eps_crossupdepth252_63d_jerk_v069_signal,
    f24pi_f24_profitability_inflection_retearn_crossupdepth252_63d_jerk_v070_signal,
    f24pi_f24_profitability_inflection_netinc_breakeven252_63d_jerk_v071_signal,
    f24pi_f24_profitability_inflection_ebit_breakeven252_63d_jerk_v072_signal,
    f24pi_f24_profitability_inflection_opinc_breakeven252_63d_jerk_v073_signal,
    f24pi_f24_profitability_inflection_ncfo_breakeven252_63d_jerk_v074_signal,
    f24pi_f24_profitability_inflection_eps_breakeven252_63d_jerk_v075_signal,
    f24pi_f24_profitability_inflection_retearn_breakeven252_63d_jerk_v076_signal,
    f24pi_f24_profitability_inflection_netinc_signmag_yoy_63d_jerk_v077_signal,
    f24pi_f24_profitability_inflection_ebit_signmag_yoy_63d_jerk_v078_signal,
    f24pi_f24_profitability_inflection_opinc_signmag_yoy_63d_jerk_v079_signal,
    f24pi_f24_profitability_inflection_ncfo_signmag_yoy_63d_jerk_v080_signal,
    f24pi_f24_profitability_inflection_eps_signmag_yoy_63d_jerk_v081_signal,
    f24pi_f24_profitability_inflection_retearn_signmag_yoy_63d_jerk_v082_signal,
    f24pi_f24_profitability_inflection_netinc_sharetrend126_63d_jerk_v083_signal,
    f24pi_f24_profitability_inflection_ebit_sharetrend126_63d_jerk_v084_signal,
    f24pi_f24_profitability_inflection_opinc_sharetrend126_63d_jerk_v085_signal,
    f24pi_f24_profitability_inflection_ncfo_sharetrend126_63d_jerk_v086_signal,
    f24pi_f24_profitability_inflection_eps_sharetrend126_63d_jerk_v087_signal,
    f24pi_f24_profitability_inflection_retearn_sharetrend126_63d_jerk_v088_signal,
    f24pi_f24_profitability_inflection_netinc_recencyspread_63d_jerk_v089_signal,
    f24pi_f24_profitability_inflection_opinc_recencyspread_63d_jerk_v090_signal,
    f24pi_f24_profitability_inflection_eps_recencyspread_63d_jerk_v091_signal,
    f24pi_f24_profitability_inflection_retearn_recencyspread_63d_jerk_v092_signal,
    f24pi_f24_profitability_inflection_retearn_breakprox_med504_63d_jerk_v093_signal,
    f24pi_f24_profitability_inflection_opinc_profitdepthgrow_63d_jerk_v094_signal,
    f24pi_f24_profitability_inflection_ncfo_profitdepthgrow_63d_jerk_v095_signal,
    f24pi_f24_profitability_inflection_eps_profitdepthgrow_63d_jerk_v096_signal,
    f24pi_f24_profitability_inflection_retearn_profitdepthgrow_63d_jerk_v097_signal,
    f24pi_f24_profitability_inflection_netinc_inflect63_63d_jerk_v098_signal,
    f24pi_f24_profitability_inflection_ebit_inflect63_63d_jerk_v099_signal,
    f24pi_f24_profitability_inflection_opinc_inflect63_63d_jerk_v100_signal,
    f24pi_f24_profitability_inflection_eps_inflect63_63d_jerk_v101_signal,
    f24pi_f24_profitability_inflection_retearn_inflect63_63d_jerk_v102_signal,
    f24pi_f24_profitability_inflection_opinc_zscore126_63d_jerk_v103_signal,
    f24pi_f24_profitability_inflection_retearn_zscore126_63d_jerk_v104_signal,
    f24pi_f24_profitability_inflection_opinc_posfrac126_63d_jerk_v105_signal,
    f24pi_f24_profitability_inflection_ncfo_posfrac126_63d_jerk_v106_signal,
    f24pi_f24_profitability_inflection_eps_posfrac126_63d_jerk_v107_signal,
    f24pi_f24_profitability_inflection_retearn_posfrac126_63d_jerk_v108_signal,
    f24pi_f24_profitability_inflection_eps_slopevol126_63d_jerk_v109_signal,
    f24pi_f24_profitability_inflection_ebit_signmag_q_63d_jerk_v110_signal,
    f24pi_f24_profitability_inflection_opinc_signmag_q_63d_jerk_v111_signal,
    f24pi_f24_profitability_inflection_ncfo_signmag_q_63d_jerk_v112_signal,
    f24pi_f24_profitability_inflection_eps_signmag_q_63d_jerk_v113_signal,
    f24pi_f24_profitability_inflection_retearn_signmag_q_63d_jerk_v114_signal,
    f24pi_f24_profitability_inflection_opinc_logclose252_63d_jerk_v115_signal,
    f24pi_f24_profitability_inflection_ncfo_logclose252_63d_jerk_v116_signal,
    f24pi_f24_profitability_inflection_eps_logclose252_63d_jerk_v117_signal,
    f24pi_f24_profitability_inflection_retearn_logclose252_63d_jerk_v118_signal,
    f24pi_f24_profitability_inflection_opinc_ranklvl252_63d_jerk_v119_signal,
    f24pi_f24_profitability_inflection_retearn_ranklvl252_63d_jerk_v120_signal,
    f24pi_f24_profitability_inflection_netinc_bestprofitprog_63d_jerk_v121_signal,
    f24pi_f24_profitability_inflection_ebit_bestprofitprog_63d_jerk_v122_signal,
    f24pi_f24_profitability_inflection_opinc_bestprofitprog_63d_jerk_v123_signal,
    f24pi_f24_profitability_inflection_ncfo_bestprofitprog_63d_jerk_v124_signal,
    f24pi_f24_profitability_inflection_eps_bestprofitprog_63d_jerk_v125_signal,
    f24pi_f24_profitability_inflection_retearn_bestprofitprog_63d_jerk_v126_signal,
    f24pi_f24_profitability_inflection_retearn_zsmooth252_63d_jerk_v127_signal,
    f24pi_f24_profitability_inflection_netinc_absnarrow126_63d_jerk_v128_signal,
    f24pi_f24_profitability_inflection_ebit_absnarrow126_63d_jerk_v129_signal,
    f24pi_f24_profitability_inflection_opinc_absnarrow126_63d_jerk_v130_signal,
    f24pi_f24_profitability_inflection_ncfo_absnarrow126_63d_jerk_v131_signal,
    f24pi_f24_profitability_inflection_eps_absnarrow126_63d_jerk_v132_signal,
    f24pi_f24_profitability_inflection_retearn_absnarrow126_63d_jerk_v133_signal,
    f24pi_f24_profitability_inflection_ebit_netinc_shareSpr126_63d_jerk_v134_signal,
    f24pi_f24_profitability_inflection_opinc_ebit_shareSpr126_63d_jerk_v135_signal,
    f24pi_f24_profitability_inflection_eps_netinc_shareSpr126_63d_jerk_v136_signal,
    f24pi_f24_profitability_inflection_netinc_retearn_shareSpr126_63d_jerk_v137_signal,
    f24pi_f24_profitability_inflection_netinc_ncfo_proxSpr252_63d_jerk_v138_signal,
    f24pi_f24_profitability_inflection_ebit_netinc_proxSpr252_63d_jerk_v139_signal,
    f24pi_f24_profitability_inflection_opinc_ebit_proxSpr252_63d_jerk_v140_signal,
    f24pi_f24_profitability_inflection_ncfo_opinc_proxSpr252_63d_jerk_v141_signal,
    f24pi_f24_profitability_inflection_eps_netinc_proxSpr252_63d_jerk_v142_signal,
    f24pi_f24_profitability_inflection_netinc_retearn_proxSpr252_63d_jerk_v143_signal,
    f24pi_f24_profitability_inflection_ncfo_retearn_proxSpr252_63d_jerk_v144_signal,
    f24pi_f24_profitability_inflection_eps_ncfo_proxSpr252_63d_jerk_v145_signal,
    f24pi_f24_profitability_inflection_netinc_ncfo_climbSpr126_63d_jerk_v146_signal,
    f24pi_f24_profitability_inflection_ebit_netinc_climbSpr126_63d_jerk_v147_signal,
    f24pi_f24_profitability_inflection_opinc_ebit_climbSpr126_63d_jerk_v148_signal,
    f24pi_f24_profitability_inflection_ncfo_opinc_climbSpr126_63d_jerk_v149_signal,
    f24pi_f24_profitability_inflection_eps_netinc_climbSpr126_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_PROFITABILITY_INFLECTION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume", "revenue", "revenueusd",
        "deferredrev", "gp", "grossmargin", "opinc", "opex", "sgna", "cor", "rnd",
        "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc", "netinccmn", "netmargin", "eps",
        "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt",
        "ncfbus", "capex", "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq",
        "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp",
        "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb",
        "ps", "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders", "undholders",
        "prfholders", "dbtholders", "putholders", "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
        "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _swing(seed, base, amp, per, allow_neg=True):
        core = _fund(seed, base=base, drift=0.0, vol=0.10, allow_neg=allow_neg)
        g = np.random.default_rng(seed + 7000)
        t = np.arange(n, dtype=float)
        osc = np.sin(2.0 * np.pi * t / per + g.uniform(0, 6.28))
        noise = g.normal(0.0, 0.35, n)
        return pd.Series(core.values - base * 0.6 + amp * base * (osc + noise))

    netinc = _swing(101, 8e7, 0.9, 180).rename("netinc")
    ebit = _swing(102, 9e7, 0.85, 150).rename("ebit")
    opinc = _swing(103, 9e7, 0.8, 210).rename("opinc")
    ncfo = _swing(104, 7e7, 1.0, 130).rename("ncfo")
    eps = _swing(105, 1.5, 0.95, 160).rename("eps")
    retearn = _swing(106, 2e8, 0.7, 320).rename("retearn")

    cols = {"netinc": netinc, "ebit": ebit, "opinc": opinc, "ncfo": ncfo,
            "eps": eps, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f24_profitability_inflection_3rd_derivatives_001_150_claude: %d features pass" % n_features)
