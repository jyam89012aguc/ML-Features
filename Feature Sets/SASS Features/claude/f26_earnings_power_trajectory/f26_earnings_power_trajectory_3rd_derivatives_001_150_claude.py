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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _slope(s, w):
    x = np.arange(w, dtype=float)
    xm = x.mean()
    xd = x - xm
    denom = (xd ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((xd * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _f26_growth(s, w):
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


def _f26_stability(s, w):
    chg = s - s.shift(21)
    m = chg.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = chg.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f26_posstreak(s, w):
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_accel_level(s, w):
    g_now = _f26_growth(s, w)
    g_prev = _f26_growth(s.shift(w), w)
    return g_now - g_prev


def _f26_eps_spread(eps, epsdil):
    return (eps - epsdil) / eps.abs().replace(0, np.nan)


def _f26_eps_recon(netinc, shareswa):
    return netinc / shareswa.replace(0, np.nan)


def f26ep_f26_earnings_power_trajectory_epsgraw_252d_jerk_v001_signal(eps):
    base = _f26_growth(eps, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgz_252d_jerk_v002_signal(eps):
    base = _f26_growth(eps, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgrank_252d_jerk_v003_signal(eps):
    base = _f26_growth(eps, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgewm_252d_jerk_v004_signal(eps):
    base = _f26_growth(eps, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtanh_252d_jerk_v005_signal(eps):
    base = _f26_growth(eps, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgqraw_63d_jerk_v006_signal(eps):
    base = _f26_growth(eps, 63)
    feat = base
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgqz_63d_jerk_v007_signal(eps):
    base = _f26_growth(eps, 63)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgqrank_63d_jerk_v008_signal(eps):
    base = _f26_growth(eps, 63)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgqewm_63d_jerk_v009_signal(eps):
    base = _f26_growth(eps, 63)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgqtanh_63d_jerk_v010_signal(eps):
    base = _f26_growth(eps, 63)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsghraw_126d_jerk_v011_signal(eps):
    base = _f26_growth(eps, 126)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsghz_126d_jerk_v012_signal(eps):
    base = _f26_growth(eps, 126)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsghrank_126d_jerk_v013_signal(eps):
    base = _f26_growth(eps, 126)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsghewm_126d_jerk_v014_signal(eps):
    base = _f26_growth(eps, 126)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsghtanh_126d_jerk_v015_signal(eps):
    base = _f26_growth(eps, 126)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigraw_252d_jerk_v016_signal(netinc):
    base = _f26_growth(netinc, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigz_252d_jerk_v017_signal(netinc):
    base = _f26_growth(netinc, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigrank_252d_jerk_v018_signal(netinc):
    base = _f26_growth(netinc, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigewm_252d_jerk_v019_signal(netinc):
    base = _f26_growth(netinc, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigtanh_252d_jerk_v020_signal(netinc):
    base = _f26_growth(netinc, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigqraw_63d_jerk_v021_signal(netinc):
    base = _f26_growth(netinc, 63)
    feat = base
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigqz_63d_jerk_v022_signal(netinc):
    base = _f26_growth(netinc, 63)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigqrank_63d_jerk_v023_signal(netinc):
    base = _f26_growth(netinc, 63)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigqewm_63d_jerk_v024_signal(netinc):
    base = _f26_growth(netinc, 63)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nigqtanh_63d_jerk_v025_signal(netinc):
    base = _f26_growth(netinc, 63)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_ncmngraw_252d_jerk_v026_signal(netinccmn):
    base = _f26_growth(netinccmn, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_ncmngz_252d_jerk_v027_signal(netinccmn):
    base = _f26_growth(netinccmn, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_ncmngrank_252d_jerk_v028_signal(netinccmn):
    base = _f26_growth(netinccmn, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_ncmngewm_252d_jerk_v029_signal(netinccmn):
    base = _f26_growth(netinccmn, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_ncmngtanh_252d_jerk_v030_signal(netinccmn):
    base = _f26_growth(netinccmn, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgraw_252d_jerk_v031_signal(epsdil):
    base = _f26_growth(epsdil, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgz_252d_jerk_v032_signal(epsdil):
    base = _f26_growth(epsdil, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgrank_252d_jerk_v033_signal(epsdil):
    base = _f26_growth(epsdil, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgewm_252d_jerk_v034_signal(epsdil):
    base = _f26_growth(epsdil, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgtanh_252d_jerk_v035_signal(epsdil):
    base = _f26_growth(epsdil, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilghraw_126d_jerk_v036_signal(epsdil):
    base = _f26_growth(epsdil, 126)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilghz_126d_jerk_v037_signal(epsdil):
    base = _f26_growth(epsdil, 126)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilghrank_126d_jerk_v038_signal(epsdil):
    base = _f26_growth(epsdil, 126)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilghewm_126d_jerk_v039_signal(epsdil):
    base = _f26_growth(epsdil, 126)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilghtanh_126d_jerk_v040_signal(epsdil):
    base = _f26_growth(epsdil, 126)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtermraw_252d_jerk_v041_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    base = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtermz_252d_jerk_v042_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    base = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtermrank_252d_jerk_v043_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    base = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtermewm_252d_jerk_v044_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    base = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsgtermtanh_252d_jerk_v045_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    base = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nihitraw_252d_jerk_v046_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nihitz_252d_jerk_v047_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nihitrank_252d_jerk_v048_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nihitewm_252d_jerk_v049_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nihittanh_252d_jerk_v050_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistabraw_252d_jerk_v051_signal(netinc):
    base = _f26_stability(netinc, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistabz_252d_jerk_v052_signal(netinc):
    base = _f26_stability(netinc, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistabrank_252d_jerk_v053_signal(netinc):
    base = _f26_stability(netinc, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistabewm_252d_jerk_v054_signal(netinc):
    base = _f26_stability(netinc, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistabtanh_252d_jerk_v055_signal(netinc):
    base = _f26_stability(netinc, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstabraw_504d_jerk_v056_signal(eps):
    base = _f26_stability(eps, 504)
    feat = base
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstabz_504d_jerk_v057_signal(eps):
    base = _f26_stability(eps, 504)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstabrank_504d_jerk_v058_signal(eps):
    base = _f26_stability(eps, 504)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstabewm_504d_jerk_v059_signal(eps):
    base = _f26_stability(eps, 504)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstabtanh_504d_jerk_v060_signal(eps):
    base = _f26_stability(eps, 504)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilstabraw_252d_jerk_v061_signal(epsdil):
    base = _f26_stability(epsdil, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilstabz_252d_jerk_v062_signal(epsdil):
    base = _f26_stability(epsdil, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilstabrank_252d_jerk_v063_signal(epsdil):
    base = _f26_stability(epsdil, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilstabewm_252d_jerk_v064_signal(epsdil):
    base = _f26_stability(epsdil, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilstabtanh_252d_jerk_v065_signal(epsdil):
    base = _f26_stability(epsdil, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsaccraw_252d_jerk_v066_signal(eps):
    base = _f26_accel_level(eps, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsaccz_252d_jerk_v067_signal(eps):
    base = _f26_accel_level(eps, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsaccrank_252d_jerk_v068_signal(eps):
    base = _f26_accel_level(eps, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsaccewm_252d_jerk_v069_signal(eps):
    base = _f26_accel_level(eps, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsacctanh_252d_jerk_v070_signal(eps):
    base = _f26_accel_level(eps, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niaccraw_252d_jerk_v071_signal(netinc):
    base = _f26_accel_level(netinc, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niaccz_252d_jerk_v072_signal(netinc):
    base = _f26_accel_level(netinc, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niaccrank_252d_jerk_v073_signal(netinc):
    base = _f26_accel_level(netinc, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niaccewm_252d_jerk_v074_signal(netinc):
    base = _f26_accel_level(netinc, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niacctanh_252d_jerk_v075_signal(netinc):
    base = _f26_accel_level(netinc, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilaccraw_252d_jerk_v076_signal(epsdil):
    base = _f26_accel_level(epsdil, 252)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilaccz_252d_jerk_v077_signal(epsdil):
    base = _f26_accel_level(epsdil, 252)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilaccrank_252d_jerk_v078_signal(epsdil):
    base = _f26_accel_level(epsdil, 252)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilaccewm_252d_jerk_v079_signal(epsdil):
    base = _f26_accel_level(epsdil, 252)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilacctanh_252d_jerk_v080_signal(epsdil):
    base = _f26_accel_level(epsdil, 252)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssprraw_63d_jerk_v081_signal(eps, epsdil):
    base = _f26_eps_spread(eps, epsdil)
    feat = base
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssprz_63d_jerk_v082_signal(eps, epsdil):
    base = _f26_eps_spread(eps, epsdil)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssprrank_63d_jerk_v083_signal(eps, epsdil):
    base = _f26_eps_spread(eps, epsdil)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssprewm_63d_jerk_v084_signal(eps, epsdil):
    base = _f26_eps_spread(eps, epsdil)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssprtanh_63d_jerk_v085_signal(eps, epsdil):
    base = _f26_eps_spread(eps, epsdil)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(5)) / 5.0
    d2 = (d1 - d1.shift(5)) / 5.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilratioraw_252d_jerk_v086_signal(eps, epsdil):
    base = epsdil / eps.replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilratioz_252d_jerk_v087_signal(eps, epsdil):
    base = epsdil / eps.replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilratiorank_252d_jerk_v088_signal(eps, epsdil):
    base = epsdil / eps.replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilratioewm_252d_jerk_v089_signal(eps, epsdil):
    base = epsdil / eps.replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilratiotanh_252d_jerk_v090_signal(eps, epsdil):
    base = epsdil / eps.replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgapraw_252d_jerk_v091_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    base = gd - gb
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgapz_252d_jerk_v092_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    base = gd - gb
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgaprank_252d_jerk_v093_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    base = gd - gb
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgapewm_252d_jerk_v094_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    base = gd - gb
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_dilgaptanh_252d_jerk_v095_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    base = gd - gb
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistreakraw_252d_jerk_v096_signal(netinc):
    scl = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = (netinc / scl).clip(lower=0).rolling(252, min_periods=126).mean()
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistreakz_252d_jerk_v097_signal(netinc):
    scl = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = (netinc / scl).clip(lower=0).rolling(252, min_periods=126).mean()
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistreakrank_252d_jerk_v098_signal(netinc):
    scl = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = (netinc / scl).clip(lower=0).rolling(252, min_periods=126).mean()
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistreakewm_252d_jerk_v099_signal(netinc):
    scl = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = (netinc / scl).clip(lower=0).rolling(252, min_periods=126).mean()
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nistreaktanh_252d_jerk_v100_signal(netinc):
    scl = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = (netinc / scl).clip(lower=0).rolling(252, min_periods=126).mean()
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstreakraw_504d_jerk_v101_signal(eps):
    scl = eps.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    base = (eps / scl).clip(lower=0).rolling(504, min_periods=252).mean()
    feat = base
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstreakz_504d_jerk_v102_signal(eps):
    scl = eps.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    base = (eps / scl).clip(lower=0).rolling(504, min_periods=252).mean()
    feat = _z(base, 126)
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstreakrank_504d_jerk_v103_signal(eps):
    scl = eps.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    base = (eps / scl).clip(lower=0).rolling(504, min_periods=252).mean()
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstreakewm_504d_jerk_v104_signal(eps):
    scl = eps.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    base = (eps / scl).clip(lower=0).rolling(504, min_periods=252).mean()
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsstreaktanh_504d_jerk_v105_signal(eps):
    scl = eps.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    base = (eps / scl).clip(lower=0).rolling(504, min_periods=252).mean()
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niinflectraw_252d_jerk_v106_signal(netinc):
    m = _mean(netinc, 252)
    base = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niinflectz_252d_jerk_v107_signal(netinc):
    m = _mean(netinc, 252)
    base = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niinflectrank_252d_jerk_v108_signal(netinc):
    m = _mean(netinc, 252)
    base = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niinflectewm_252d_jerk_v109_signal(netinc):
    m = _mean(netinc, 252)
    base = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_niinflecttanh_252d_jerk_v110_signal(netinc):
    m = _mean(netinc, 252)
    base = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsinflectraw_126d_jerk_v111_signal(eps):
    m = _mean(eps, 126)
    base = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsinflectz_126d_jerk_v112_signal(eps):
    m = _mean(eps, 126)
    base = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsinflectrank_126d_jerk_v113_signal(eps):
    m = _mean(eps, 126)
    base = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsinflectewm_126d_jerk_v114_signal(eps):
    m = _mean(eps, 126)
    base = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsinflecttanh_126d_jerk_v115_signal(eps):
    m = _mean(eps, 126)
    base = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssloperaw_252d_jerk_v116_signal(eps):
    sl = _slope(eps, 252)
    base = sl / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsslopez_252d_jerk_v117_signal(eps):
    sl = _slope(eps, 252)
    base = sl / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epssloperank_252d_jerk_v118_signal(eps):
    sl = _slope(eps, 252)
    base = sl / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsslopeewm_252d_jerk_v119_signal(eps):
    sl = _slope(eps, 252)
    base = sl / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsslopetanh_252d_jerk_v120_signal(eps):
    sl = _slope(eps, 252)
    base = sl / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nisloperaw_504d_jerk_v121_signal(netinc):
    sl = _slope(netinc, 504)
    base = sl / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nislopez_504d_jerk_v122_signal(netinc):
    sl = _slope(netinc, 504)
    base = sl / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nisloperank_504d_jerk_v123_signal(netinc):
    sl = _slope(netinc, 504)
    base = sl / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nislopeewm_504d_jerk_v124_signal(netinc):
    sl = _slope(netinc, 504)
    base = sl / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nislopetanh_504d_jerk_v125_signal(netinc):
    sl = _slope(netinc, 504)
    base = sl / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsddraw_252d_jerk_v126_signal(eps):
    pk = _rmax(eps, 252)
    base = eps / pk.replace(0, np.nan) - 1.0
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsddz_252d_jerk_v127_signal(eps):
    pk = _rmax(eps, 252)
    base = eps / pk.replace(0, np.nan) - 1.0
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsddrank_252d_jerk_v128_signal(eps):
    pk = _rmax(eps, 252)
    base = eps / pk.replace(0, np.nan) - 1.0
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsddewm_252d_jerk_v129_signal(eps):
    pk = _rmax(eps, 252)
    base = eps / pk.replace(0, np.nan) - 1.0
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsddtanh_252d_jerk_v130_signal(eps):
    pk = _rmax(eps, 252)
    base = eps / pk.replace(0, np.nan) - 1.0
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nirecovraw_252d_jerk_v131_signal(netinc):
    tr = _rmin(netinc, 252)
    base = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nirecovz_252d_jerk_v132_signal(netinc):
    tr = _rmin(netinc, 252)
    base = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nirecovrank_252d_jerk_v133_signal(netinc):
    tr = _rmin(netinc, 252)
    base = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nirecovewm_252d_jerk_v134_signal(netinc):
    tr = _rmin(netinc, 252)
    base = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_nirecovtanh_252d_jerk_v135_signal(netinc):
    tr = _rmin(netinc, 252)
    base = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsrngposraw_252d_jerk_v136_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    base = (eps - lo) / (hi - lo).replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsrngposz_252d_jerk_v137_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    base = (eps - lo) / (hi - lo).replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsrngposrank_252d_jerk_v138_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    base = (eps - lo) / (hi - lo).replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsrngposewm_252d_jerk_v139_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    base = (eps - lo) / (hi - lo).replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_epsrngpostanh_252d_jerk_v140_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    base = (eps - lo) / (hi - lo).replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconraw_252d_jerk_v141_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gr = _f26_growth(_f26_eps_recon(netinc, shareswa), 252)
    base = gn - gr
    feat = base
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconz_252d_jerk_v142_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gr = _f26_growth(_f26_eps_recon(netinc, shareswa), 252)
    base = gn - gr
    feat = _z(base, 126)
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconrank_252d_jerk_v143_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gr = _f26_growth(_f26_eps_recon(netinc, shareswa), 252)
    base = gn - gr
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconewm_252d_jerk_v144_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gr = _f26_growth(_f26_eps_recon(netinc, shareswa), 252)
    base = gn - gr
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_recontanh_252d_jerk_v145_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gr = _f26_growth(_f26_eps_recon(netinc, shareswa), 252)
    base = gn - gr
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(21)) / 21.0
    d2 = (d1 - d1.shift(21)) / 21.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconampraw_504d_jerk_v146_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    hi = _rmax(re, 504)
    lo = _rmin(re, 504)
    base = (hi - lo) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconampz_504d_jerk_v147_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    hi = _rmax(re, 504)
    lo = _rmin(re, 504)
    base = (hi - lo) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = _z(base, 126)
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconamprank_504d_jerk_v148_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    hi = _rmax(re, 504)
    lo = _rmin(re, 504)
    base = (hi - lo) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconampewm_504d_jerk_v149_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    hi = _rmax(re, 504)
    lo = _rmin(re, 504)
    base = (hi - lo) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=21).mean() - base.ewm(span=21, min_periods=10).mean()
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f26ep_f26_earnings_power_trajectory_reconamptanh_504d_jerk_v150_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    hi = _rmax(re, 504)
    lo = _rmin(re, 504)
    base = (hi - lo) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    feat = np.tanh(2.0 * base / (base.abs().rolling(189, min_periods=63).mean().replace(0, np.nan)))
    d1 = (feat - feat.shift(63)) / 63.0
    d2 = (d1 - d1.shift(63)) / 63.0
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f26ep_f26_earnings_power_trajectory_epsgraw_252d_jerk_v001_signal,
    f26ep_f26_earnings_power_trajectory_epsgz_252d_jerk_v002_signal,
    f26ep_f26_earnings_power_trajectory_epsgrank_252d_jerk_v003_signal,
    f26ep_f26_earnings_power_trajectory_epsgewm_252d_jerk_v004_signal,
    f26ep_f26_earnings_power_trajectory_epsgtanh_252d_jerk_v005_signal,
    f26ep_f26_earnings_power_trajectory_epsgqraw_63d_jerk_v006_signal,
    f26ep_f26_earnings_power_trajectory_epsgqz_63d_jerk_v007_signal,
    f26ep_f26_earnings_power_trajectory_epsgqrank_63d_jerk_v008_signal,
    f26ep_f26_earnings_power_trajectory_epsgqewm_63d_jerk_v009_signal,
    f26ep_f26_earnings_power_trajectory_epsgqtanh_63d_jerk_v010_signal,
    f26ep_f26_earnings_power_trajectory_epsghraw_126d_jerk_v011_signal,
    f26ep_f26_earnings_power_trajectory_epsghz_126d_jerk_v012_signal,
    f26ep_f26_earnings_power_trajectory_epsghrank_126d_jerk_v013_signal,
    f26ep_f26_earnings_power_trajectory_epsghewm_126d_jerk_v014_signal,
    f26ep_f26_earnings_power_trajectory_epsghtanh_126d_jerk_v015_signal,
    f26ep_f26_earnings_power_trajectory_nigraw_252d_jerk_v016_signal,
    f26ep_f26_earnings_power_trajectory_nigz_252d_jerk_v017_signal,
    f26ep_f26_earnings_power_trajectory_nigrank_252d_jerk_v018_signal,
    f26ep_f26_earnings_power_trajectory_nigewm_252d_jerk_v019_signal,
    f26ep_f26_earnings_power_trajectory_nigtanh_252d_jerk_v020_signal,
    f26ep_f26_earnings_power_trajectory_nigqraw_63d_jerk_v021_signal,
    f26ep_f26_earnings_power_trajectory_nigqz_63d_jerk_v022_signal,
    f26ep_f26_earnings_power_trajectory_nigqrank_63d_jerk_v023_signal,
    f26ep_f26_earnings_power_trajectory_nigqewm_63d_jerk_v024_signal,
    f26ep_f26_earnings_power_trajectory_nigqtanh_63d_jerk_v025_signal,
    f26ep_f26_earnings_power_trajectory_ncmngraw_252d_jerk_v026_signal,
    f26ep_f26_earnings_power_trajectory_ncmngz_252d_jerk_v027_signal,
    f26ep_f26_earnings_power_trajectory_ncmngrank_252d_jerk_v028_signal,
    f26ep_f26_earnings_power_trajectory_ncmngewm_252d_jerk_v029_signal,
    f26ep_f26_earnings_power_trajectory_ncmngtanh_252d_jerk_v030_signal,
    f26ep_f26_earnings_power_trajectory_dilgraw_252d_jerk_v031_signal,
    f26ep_f26_earnings_power_trajectory_dilgz_252d_jerk_v032_signal,
    f26ep_f26_earnings_power_trajectory_dilgrank_252d_jerk_v033_signal,
    f26ep_f26_earnings_power_trajectory_dilgewm_252d_jerk_v034_signal,
    f26ep_f26_earnings_power_trajectory_dilgtanh_252d_jerk_v035_signal,
    f26ep_f26_earnings_power_trajectory_dilghraw_126d_jerk_v036_signal,
    f26ep_f26_earnings_power_trajectory_dilghz_126d_jerk_v037_signal,
    f26ep_f26_earnings_power_trajectory_dilghrank_126d_jerk_v038_signal,
    f26ep_f26_earnings_power_trajectory_dilghewm_126d_jerk_v039_signal,
    f26ep_f26_earnings_power_trajectory_dilghtanh_126d_jerk_v040_signal,
    f26ep_f26_earnings_power_trajectory_epsgtermraw_252d_jerk_v041_signal,
    f26ep_f26_earnings_power_trajectory_epsgtermz_252d_jerk_v042_signal,
    f26ep_f26_earnings_power_trajectory_epsgtermrank_252d_jerk_v043_signal,
    f26ep_f26_earnings_power_trajectory_epsgtermewm_252d_jerk_v044_signal,
    f26ep_f26_earnings_power_trajectory_epsgtermtanh_252d_jerk_v045_signal,
    f26ep_f26_earnings_power_trajectory_nihitraw_252d_jerk_v046_signal,
    f26ep_f26_earnings_power_trajectory_nihitz_252d_jerk_v047_signal,
    f26ep_f26_earnings_power_trajectory_nihitrank_252d_jerk_v048_signal,
    f26ep_f26_earnings_power_trajectory_nihitewm_252d_jerk_v049_signal,
    f26ep_f26_earnings_power_trajectory_nihittanh_252d_jerk_v050_signal,
    f26ep_f26_earnings_power_trajectory_nistabraw_252d_jerk_v051_signal,
    f26ep_f26_earnings_power_trajectory_nistabz_252d_jerk_v052_signal,
    f26ep_f26_earnings_power_trajectory_nistabrank_252d_jerk_v053_signal,
    f26ep_f26_earnings_power_trajectory_nistabewm_252d_jerk_v054_signal,
    f26ep_f26_earnings_power_trajectory_nistabtanh_252d_jerk_v055_signal,
    f26ep_f26_earnings_power_trajectory_epsstabraw_504d_jerk_v056_signal,
    f26ep_f26_earnings_power_trajectory_epsstabz_504d_jerk_v057_signal,
    f26ep_f26_earnings_power_trajectory_epsstabrank_504d_jerk_v058_signal,
    f26ep_f26_earnings_power_trajectory_epsstabewm_504d_jerk_v059_signal,
    f26ep_f26_earnings_power_trajectory_epsstabtanh_504d_jerk_v060_signal,
    f26ep_f26_earnings_power_trajectory_dilstabraw_252d_jerk_v061_signal,
    f26ep_f26_earnings_power_trajectory_dilstabz_252d_jerk_v062_signal,
    f26ep_f26_earnings_power_trajectory_dilstabrank_252d_jerk_v063_signal,
    f26ep_f26_earnings_power_trajectory_dilstabewm_252d_jerk_v064_signal,
    f26ep_f26_earnings_power_trajectory_dilstabtanh_252d_jerk_v065_signal,
    f26ep_f26_earnings_power_trajectory_epsaccraw_252d_jerk_v066_signal,
    f26ep_f26_earnings_power_trajectory_epsaccz_252d_jerk_v067_signal,
    f26ep_f26_earnings_power_trajectory_epsaccrank_252d_jerk_v068_signal,
    f26ep_f26_earnings_power_trajectory_epsaccewm_252d_jerk_v069_signal,
    f26ep_f26_earnings_power_trajectory_epsacctanh_252d_jerk_v070_signal,
    f26ep_f26_earnings_power_trajectory_niaccraw_252d_jerk_v071_signal,
    f26ep_f26_earnings_power_trajectory_niaccz_252d_jerk_v072_signal,
    f26ep_f26_earnings_power_trajectory_niaccrank_252d_jerk_v073_signal,
    f26ep_f26_earnings_power_trajectory_niaccewm_252d_jerk_v074_signal,
    f26ep_f26_earnings_power_trajectory_niacctanh_252d_jerk_v075_signal,
    f26ep_f26_earnings_power_trajectory_dilaccraw_252d_jerk_v076_signal,
    f26ep_f26_earnings_power_trajectory_dilaccz_252d_jerk_v077_signal,
    f26ep_f26_earnings_power_trajectory_dilaccrank_252d_jerk_v078_signal,
    f26ep_f26_earnings_power_trajectory_dilaccewm_252d_jerk_v079_signal,
    f26ep_f26_earnings_power_trajectory_dilacctanh_252d_jerk_v080_signal,
    f26ep_f26_earnings_power_trajectory_epssprraw_63d_jerk_v081_signal,
    f26ep_f26_earnings_power_trajectory_epssprz_63d_jerk_v082_signal,
    f26ep_f26_earnings_power_trajectory_epssprrank_63d_jerk_v083_signal,
    f26ep_f26_earnings_power_trajectory_epssprewm_63d_jerk_v084_signal,
    f26ep_f26_earnings_power_trajectory_epssprtanh_63d_jerk_v085_signal,
    f26ep_f26_earnings_power_trajectory_dilratioraw_252d_jerk_v086_signal,
    f26ep_f26_earnings_power_trajectory_dilratioz_252d_jerk_v087_signal,
    f26ep_f26_earnings_power_trajectory_dilratiorank_252d_jerk_v088_signal,
    f26ep_f26_earnings_power_trajectory_dilratioewm_252d_jerk_v089_signal,
    f26ep_f26_earnings_power_trajectory_dilratiotanh_252d_jerk_v090_signal,
    f26ep_f26_earnings_power_trajectory_dilgapraw_252d_jerk_v091_signal,
    f26ep_f26_earnings_power_trajectory_dilgapz_252d_jerk_v092_signal,
    f26ep_f26_earnings_power_trajectory_dilgaprank_252d_jerk_v093_signal,
    f26ep_f26_earnings_power_trajectory_dilgapewm_252d_jerk_v094_signal,
    f26ep_f26_earnings_power_trajectory_dilgaptanh_252d_jerk_v095_signal,
    f26ep_f26_earnings_power_trajectory_nistreakraw_252d_jerk_v096_signal,
    f26ep_f26_earnings_power_trajectory_nistreakz_252d_jerk_v097_signal,
    f26ep_f26_earnings_power_trajectory_nistreakrank_252d_jerk_v098_signal,
    f26ep_f26_earnings_power_trajectory_nistreakewm_252d_jerk_v099_signal,
    f26ep_f26_earnings_power_trajectory_nistreaktanh_252d_jerk_v100_signal,
    f26ep_f26_earnings_power_trajectory_epsstreakraw_504d_jerk_v101_signal,
    f26ep_f26_earnings_power_trajectory_epsstreakz_504d_jerk_v102_signal,
    f26ep_f26_earnings_power_trajectory_epsstreakrank_504d_jerk_v103_signal,
    f26ep_f26_earnings_power_trajectory_epsstreakewm_504d_jerk_v104_signal,
    f26ep_f26_earnings_power_trajectory_epsstreaktanh_504d_jerk_v105_signal,
    f26ep_f26_earnings_power_trajectory_niinflectraw_252d_jerk_v106_signal,
    f26ep_f26_earnings_power_trajectory_niinflectz_252d_jerk_v107_signal,
    f26ep_f26_earnings_power_trajectory_niinflectrank_252d_jerk_v108_signal,
    f26ep_f26_earnings_power_trajectory_niinflectewm_252d_jerk_v109_signal,
    f26ep_f26_earnings_power_trajectory_niinflecttanh_252d_jerk_v110_signal,
    f26ep_f26_earnings_power_trajectory_epsinflectraw_126d_jerk_v111_signal,
    f26ep_f26_earnings_power_trajectory_epsinflectz_126d_jerk_v112_signal,
    f26ep_f26_earnings_power_trajectory_epsinflectrank_126d_jerk_v113_signal,
    f26ep_f26_earnings_power_trajectory_epsinflectewm_126d_jerk_v114_signal,
    f26ep_f26_earnings_power_trajectory_epsinflecttanh_126d_jerk_v115_signal,
    f26ep_f26_earnings_power_trajectory_epssloperaw_252d_jerk_v116_signal,
    f26ep_f26_earnings_power_trajectory_epsslopez_252d_jerk_v117_signal,
    f26ep_f26_earnings_power_trajectory_epssloperank_252d_jerk_v118_signal,
    f26ep_f26_earnings_power_trajectory_epsslopeewm_252d_jerk_v119_signal,
    f26ep_f26_earnings_power_trajectory_epsslopetanh_252d_jerk_v120_signal,
    f26ep_f26_earnings_power_trajectory_nisloperaw_504d_jerk_v121_signal,
    f26ep_f26_earnings_power_trajectory_nislopez_504d_jerk_v122_signal,
    f26ep_f26_earnings_power_trajectory_nisloperank_504d_jerk_v123_signal,
    f26ep_f26_earnings_power_trajectory_nislopeewm_504d_jerk_v124_signal,
    f26ep_f26_earnings_power_trajectory_nislopetanh_504d_jerk_v125_signal,
    f26ep_f26_earnings_power_trajectory_epsddraw_252d_jerk_v126_signal,
    f26ep_f26_earnings_power_trajectory_epsddz_252d_jerk_v127_signal,
    f26ep_f26_earnings_power_trajectory_epsddrank_252d_jerk_v128_signal,
    f26ep_f26_earnings_power_trajectory_epsddewm_252d_jerk_v129_signal,
    f26ep_f26_earnings_power_trajectory_epsddtanh_252d_jerk_v130_signal,
    f26ep_f26_earnings_power_trajectory_nirecovraw_252d_jerk_v131_signal,
    f26ep_f26_earnings_power_trajectory_nirecovz_252d_jerk_v132_signal,
    f26ep_f26_earnings_power_trajectory_nirecovrank_252d_jerk_v133_signal,
    f26ep_f26_earnings_power_trajectory_nirecovewm_252d_jerk_v134_signal,
    f26ep_f26_earnings_power_trajectory_nirecovtanh_252d_jerk_v135_signal,
    f26ep_f26_earnings_power_trajectory_epsrngposraw_252d_jerk_v136_signal,
    f26ep_f26_earnings_power_trajectory_epsrngposz_252d_jerk_v137_signal,
    f26ep_f26_earnings_power_trajectory_epsrngposrank_252d_jerk_v138_signal,
    f26ep_f26_earnings_power_trajectory_epsrngposewm_252d_jerk_v139_signal,
    f26ep_f26_earnings_power_trajectory_epsrngpostanh_252d_jerk_v140_signal,
    f26ep_f26_earnings_power_trajectory_reconraw_252d_jerk_v141_signal,
    f26ep_f26_earnings_power_trajectory_reconz_252d_jerk_v142_signal,
    f26ep_f26_earnings_power_trajectory_reconrank_252d_jerk_v143_signal,
    f26ep_f26_earnings_power_trajectory_reconewm_252d_jerk_v144_signal,
    f26ep_f26_earnings_power_trajectory_recontanh_252d_jerk_v145_signal,
    f26ep_f26_earnings_power_trajectory_reconampraw_504d_jerk_v146_signal,
    f26ep_f26_earnings_power_trajectory_reconampz_504d_jerk_v147_signal,
    f26ep_f26_earnings_power_trajectory_reconamprank_504d_jerk_v148_signal,
    f26ep_f26_earnings_power_trajectory_reconampewm_504d_jerk_v149_signal,
    f26ep_f26_earnings_power_trajectory_reconamptanh_504d_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EARNINGS_POWER_TRAJECTORY_REGISTRY_001_150 = REGISTRY


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
    netinc = _fund(7, base=5e8, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("netinc")
    netinccmn = _fund(8, base=4.6e8, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("netinccmn")
    eps = _fund(3, base=3.0, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("eps")
    epsdil = _fund(5, base=2.85, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("epsdil")
    shareswa = _fund(11, base=2.0e8, drift=0.01, vol=0.08, allow_neg=False, n=n).rename("shareswa")

    cols = {"netinc": netinc, "netinccmn": netinccmn, "eps": eps,
            "epsdil": epsdil, "shareswa": shareswa}

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

    print("OK f26_earnings_power_trajectory_jerk_001_150_claude: %d features pass" % n_features)
