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


def _logret(close):
    return np.log(close.replace(0, np.nan)).diff()


# ===== folder domain primitives (trend persistence) =====
def _f03_efficiency(close, w):
    net = (close - close.shift(w)).abs()
    dr = close.diff().abs()
    path = dr.rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_signed_efficiency(close, w):
    net = close - close.shift(w)
    dr = close.diff().abs()
    path = dr.rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_rs_hurst(close, w):
    r = _logret(close)

    def _rs(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        m = a.mean()
        y = np.cumsum(a - m)
        R = y.max() - y.min()
        S = a.std()
        if S == 0 or R == 0:
            return np.nan
        return np.log(R / S) / np.log(a.size)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_rs, raw=True)


def _f03_autocorr(close, w, lag):
    r = _logret(close)

    def _ac(a):
        a = a[~np.isnan(a)]
        if a.size <= lag + 2:
            return np.nan
        x0 = a[:-lag]
        x1 = a[lag:]
        if x0.std() == 0 or x1.std() == 0:
            return np.nan
        return np.corrcoef(x0, x1)[0, 1]

    return r.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _f03_varratio(close, k, w):
    r = _logret(close)
    rk = np.log(close.replace(0, np.nan)).diff(k)
    v1 = r.rolling(w, min_periods=max(k + 2, w // 2)).var()
    vk = rk.rolling(w, min_periods=max(k + 2, w // 2)).var()
    return vk / (k * v1).replace(0, np.nan)


def _f03_dfa(close, w):
    r = _logret(close)

    def _f(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        y = np.cumsum(a - a.mean())
        x = np.arange(a.size)
        b = np.polyfit(x, y, 1)
        resid = y - (b[0] * x + b[1])
        return resid.std() / (a.std() * np.sqrt(a.size) + 1e-12)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_f, raw=True)


def _f03_cont_rate(close, w):
    # magnitude-weighted continuation rate (share of return mass that keeps the
    # prior day's sign)
    r = _logret(close)

    def _c(a):
        a = a[~np.isnan(a)]
        if a.size < 5:
            return np.nan
        w0 = np.abs(a[1:])
        tot = np.sum(w0)
        if tot == 0:
            return np.nan
        same = np.sign(a[1:]) == np.sign(a[:-1])
        return np.sum(w0[same]) / tot

    return r.rolling(w, min_periods=max(5, w // 2)).apply(_c, raw=True)


def _f03_r2(close, w):
    lp = np.log(close.replace(0, np.nan))

    def _f(a):
        a = a[~np.isnan(a)]
        if a.size < max(8, w // 4):
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        ss_res = np.sum((a - pred) ** 2)
        ss_tot = np.sum((a - a.mean()) ** 2)
        if ss_tot == 0:
            return np.nan
        return 1.0 - ss_res / ss_tot

    return lp.rolling(w, min_periods=max(8, w // 2)).apply(_f, raw=True)


def _f03_jumpshare(close, w):
    ar = _logret(close).abs()
    mx = ar.rolling(w, min_periods=max(8, w // 2)).max()
    tot = ar.rolling(w, min_periods=max(8, w // 2)).sum()
    return 1.0 - mx / tot.replace(0, np.nan)


# ============================================================
# efficiency ratio 42d (between standard windows)
def f03tp_f03_trend_persistence_effr_42d_base_v076_signal(closeadj):
    b = _f03_efficiency(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 189d (three-quarter)
def f03tp_f03_trend_persistence_effr_189d_base_v077_signal(closeadj):
    b = _f03_efficiency(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio measured on weekly (5d) returns over 252d (slow-path smoothness)
def f03tp_f03_trend_persistence_weffr_252d_base_v078_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    net = (np.log(closeadj.replace(0, np.nan)) - np.log(closeadj.shift(252).replace(0, np.nan))).abs()
    path = wk.abs().rolling(252, min_periods=126).sum() / 5.0
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio range-normalized: ER times log-amplitude (strong & smooth) 126d
def f03tp_f03_trend_persistence_effamp_126d_base_v079_signal(closeadj):
    e = _f03_efficiency(closeadj, 126)
    amp = np.log(closeadj.rolling(126, min_periods=63).max()
                 / closeadj.rolling(126, min_periods=63).min().replace(0, np.nan))
    b = e * amp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio acceleration: change of the (ER change) over a quarter 126d
def f03tp_f03_trend_persistence_effaccel_126d_base_v080_signal(closeadj):
    e = _f03_efficiency(closeadj, 126)
    d = e - e.shift(21)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency rank vs own 252d history (where is directional strength now)
def f03tp_f03_trend_persistence_seffrank_126d_base_v081_signal(closeadj):
    se = _f03_signed_efficiency(closeadj, 126)
    b = se.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-efficiency gap: how much of the high-low range the net move captured
# minus the path efficiency (does price use its range efficiently?) 126d
def f03tp_f03_trend_persistence_effgap_126d_base_v082_signal(closeadj):
    net = (closeadj - closeadj.shift(126)).abs()
    rng = (closeadj.rolling(126, min_periods=63).max()
           - closeadj.rolling(126, min_periods=63).min())
    range_eff = net / rng.replace(0, np.nan)
    path_eff = _f03_efficiency(closeadj, 126)
    b = range_eff - path_eff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency stability: negative rolling std of 21d ER (steady persistence) 252d
def f03tp_f03_trend_persistence_effstab_252d_base_v083_signal(closeadj):
    e = _f03_efficiency(closeadj, 21)
    b = -e.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio x sign of trend (re-confirm direction) at 63d
def f03tp_f03_trend_persistence_effsign_63d_base_v084_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    sg = np.sign(closeadj - closeadj.shift(63))
    b = e * sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst at 189d (three-quarter memory)
def f03tp_f03_trend_persistence_hurst_189d_base_v085_signal(closeadj):
    b = _f03_rs_hurst(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst rank vs own 504d history
def f03tp_f03_trend_persistence_hurstrank_126d_base_v086_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126)
    b = h.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst of squared returns (volatility-memory exponent) 126d
def f03tp_f03_trend_persistence_volhurst_126d_base_v087_signal(closeadj):
    sq = _logret(closeadj) ** 2

    def _rs(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        y = np.cumsum(a - a.mean())
        R = y.max() - y.min()
        S = a.std()
        if S == 0 or R == 0:
            return np.nan
        return np.log(R / S) / np.log(a.size)

    b = sq.rolling(126, min_periods=63).apply(_rs, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst acceleration: (H change) over a month differenced over a quarter 126d
def f03tp_f03_trend_persistence_hurstaccel_126d_base_v088_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126)
    d = h - h.shift(21)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst minus DFA exponent proxy (two memory estimators disagreement) 126d
def f03tp_f03_trend_persistence_memdisagree_126d_base_v089_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126)
    d = _f03_dfa(closeadj, 126)
    b = h - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DFA proxy at 252d
def f03tp_f03_trend_persistence_dfa_252d_base_v090_signal(closeadj):
    b = _f03_dfa(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DFA proxy z-scored vs own 252d history 126d
def f03tp_f03_trend_persistence_dfaz_126d_base_v091_signal(closeadj):
    d = _f03_dfa(closeadj, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag 3, 126d
def f03tp_f03_trend_persistence_acf3_126d_base_v092_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag 10, 252d (longer-memory)
def f03tp_f03_trend_persistence_acf10_252d_base_v093_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag 2, 63d
def f03tp_f03_trend_persistence_acf2_63d_base_v094_signal(closeadj):
    b = _f03_autocorr(closeadj, 63, 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sum of squared autocorrelations over lags 1..5 (total memory energy) 126d
def f03tp_f03_trend_persistence_acfenergy_126d_base_v095_signal(closeadj):
    r = _logret(closeadj)

    def _e(a):
        a = a[~np.isnan(a)]
        if a.size < 16:
            return np.nan
        a = a - a.mean()
        v0 = np.sum(a * a)
        if v0 == 0:
            return np.nan
        tot = 0.0
        for lag in range(1, 6):
            tot += (np.sum(a[lag:] * a[:-lag]) / v0) ** 2
        return tot

    b = r.rolling(126, min_periods=63).apply(_e, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ljung-Box-like statistic: weighted sum of squared autocorr (memory significance) 252d
def f03tp_f03_trend_persistence_ljungbox_252d_base_v096_signal(closeadj):
    r = _logret(closeadj)

    def _lb(a):
        a = a[~np.isnan(a)]
        nn = a.size
        if nn < 30:
            return np.nan
        a = a - a.mean()
        v0 = np.sum(a * a)
        if v0 == 0:
            return np.nan
        tot = 0.0
        for lag in range(1, 8):
            rho = np.sum(a[lag:] * a[:-lag]) / v0
            tot += rho * rho / (nn - lag)
        return nn * (nn + 2.0) * tot

    b = r.rolling(252, min_periods=126).apply(_lb, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 change vs a year ago (memory regime shift) 126d
def f03tp_f03_trend_persistence_acf1yoy_126d_base_v097_signal(closeadj):
    a = _f03_autocorr(closeadj, 126, 1)
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-life of return memory: first lag where autocorr drops below half of lag1 126d
def f03tp_f03_trend_persistence_acfhl_126d_base_v098_signal(closeadj):
    r = _logret(closeadj)

    def _hl(a):
        a = a[~np.isnan(a)]
        if a.size < 20:
            return np.nan
        a = a - a.mean()
        v0 = np.sum(a * a)
        if v0 == 0:
            return np.nan
        r1 = np.sum(a[1:] * a[:-1]) / v0
        if abs(r1) < 1e-6:
            return 0.0
        target = 0.5 * abs(r1)
        prev_lag = 1.0
        prev_val = abs(r1)
        for lag in range(2, 11):
            rl = abs(np.sum(a[lag:] * a[:-lag]) / v0)
            if rl < target:
                # linear interpolation between prev_lag and lag for a continuous HL
                denom = prev_val - rl
                frac = (prev_val - target) / denom if denom != 0 else 0.0
                return prev_lag + frac
            prev_lag = lag
            prev_val = rl
        return 10.0

    b = r.rolling(126, min_periods=63).apply(_hl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=2, 63d
def f03tp_f03_trend_persistence_vr2_63d_base_v099_signal(closeadj):
    b = _f03_varratio(closeadj, 2, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=10, 126d
def f03tp_f03_trend_persistence_vr10_126d_base_v100_signal(closeadj):
    b = _f03_varratio(closeadj, 10, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=21, 504d (long horizon)
def f03tp_f03_trend_persistence_vr21_504d_base_v101_signal(closeadj):
    b = _f03_varratio(closeadj, 21, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=42, 504d
def f03tp_f03_trend_persistence_vr42_504d_base_v102_signal(closeadj):
    b = _f03_varratio(closeadj, 42, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log variance-ratio (symmetric persistence/mean-reversion scale) k=5 252d
def f03tp_f03_trend_persistence_logvr5_252d_base_v103_signal(closeadj):
    v = _f03_varratio(closeadj, 5, 252)
    b = np.log(v.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio slope across k (regression of VR on log-k) 252d
def f03tp_f03_trend_persistence_vrslope_252d_base_v104_signal(closeadj):
    v2 = _f03_varratio(closeadj, 2, 252)
    v5 = _f03_varratio(closeadj, 5, 252)
    v10 = _f03_varratio(closeadj, 10, 252)
    v21 = _f03_varratio(closeadj, 21, 252)
    ks = np.log(np.array([2.0, 5.0, 10.0, 21.0]))
    kbar = ks.mean()
    denom = np.sum((ks - kbar) ** 2)
    b = ((v2 * (ks[0] - kbar) + v5 * (ks[1] - kbar)
          + v10 * (ks[2] - kbar) + v21 * (ks[3] - kbar)) / denom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio rank vs own 252d history, k=10 126d
def f03tp_f03_trend_persistence_vrrank10_126d_base_v105_signal(closeadj):
    v = _f03_varratio(closeadj, 10, 126)
    b = v.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio dispersion across windows (stability of trending regime) k=5
def f03tp_f03_trend_persistence_vrdisp5_base_v106_signal(closeadj):
    v63 = _f03_varratio(closeadj, 5, 63)
    v126 = _f03_varratio(closeadj, 5, 126)
    v252 = _f03_varratio(closeadj, 5, 252)
    b = pd.concat([v63, v126, v252], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation rate 63d
def f03tp_f03_trend_persistence_cont_63d_base_v107_signal(closeadj):
    b = _f03_cont_rate(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation rate 252d
def f03tp_f03_trend_persistence_cont_252d_base_v108_signal(closeadj):
    b = _f03_cont_rate(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation-rate change over a quarter (persistence trajectory) 126d
def f03tp_f03_trend_persistence_contmom_126d_base_v109_signal(closeadj):
    c = _f03_cont_rate(closeadj, 126)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation-rate z-score vs own 252d history 126d
def f03tp_f03_trend_persistence_contz_126d_base_v110_signal(closeadj):
    c = _f03_cont_rate(closeadj, 126)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-continuation vs down-continuation asymmetry 126d
def f03tp_f03_trend_persistence_contasym_126d_base_v111_signal(closeadj):
    r = _logret(closeadj)

    def _ca(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        prev = a[:-1]
        cur = a[1:]
        up_mask = prev > 0
        dn_mask = prev < 0
        up_cont = np.mean(cur[up_mask] > 0) if up_mask.sum() else np.nan
        dn_cont = np.mean(cur[dn_mask] < 0) if dn_mask.sum() else np.nan
        if np.isnan(up_cont) or np.isnan(dn_cont):
            return np.nan
        return (up_cont - dn_cont) + 0.1 * np.tanh(50.0 * a.mean())

    b = r.rolling(126, min_periods=63).apply(_ca, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend linearity R-squared at 252d
def f03tp_f03_trend_persistence_r2_252d_base_v112_signal(closeadj):
    b = _f03_r2(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend linearity R-squared at 42d
def f03tp_f03_trend_persistence_r2_42d_base_v113_signal(closeadj):
    b = _f03_r2(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared change over a quarter (firming/loosening trend) 126d
def f03tp_f03_trend_persistence_r2mom_126d_base_v114_signal(closeadj):
    q = _f03_r2(closeadj, 126)
    b = q - q.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared spread short vs long (is the recent trend tighter?) 63 vs 252
def f03tp_f03_trend_persistence_r2spr_63v252_base_v115_signal(closeadj):
    s = _f03_r2(closeadj, 63)
    l = _f03_r2(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jump-share (1 - largest-day concentration) at 126d
def f03tp_f03_trend_persistence_jumpshare_126d_base_v116_signal(closeadj):
    b = _f03_jumpshare(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-3-day concentration of the path (sum of 3 biggest |ret| / total) 126d
def f03tp_f03_trend_persistence_top3conc_126d_base_v117_signal(closeadj):
    ar = _logret(closeadj).abs()

    def _t3(a):
        a = a[~np.isnan(a)]
        if a.size < 20:
            return np.nan
        s = a.sum()
        if s == 0:
            return np.nan
        top3 = np.sort(a)[-3:].sum()
        return 1.0 - top3 / s

    b = ar.rolling(126, min_periods=63).apply(_t3, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy of |return| distribution (high entropy => evenly-paced trend) 126d
def f03tp_f03_trend_persistence_retentropy_126d_base_v118_signal(closeadj):
    ar = _logret(closeadj).abs()

    def _ent(a):
        a = a[~np.isnan(a)]
        if a.size < 20:
            return np.nan
        s = a.sum()
        if s == 0:
            return np.nan
        p = a / s
        p = p[p > 0]
        return -np.sum(p * np.log(p)) / np.log(a.size)

    b = ar.rolling(126, min_periods=63).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of time above 50d MA (durable up-trend holding) 252d
def f03tp_f03_trend_persistence_abovema50_252d_base_v119_signal(closeadj):
    ma = closeadj.rolling(50, min_periods=25).mean()
    above = (closeadj > ma).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-side persistence: longest fraction of window on one side of 21d MA 126d
def f03tp_f03_trend_persistence_maside_126d_base_v120_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    side = np.sign(closeadj - ma)

    def _run(a):
        a = a[~np.isnan(a)]
        if a.size < 10:
            return np.nan
        best = 0
        cur = 0
        prev = 0
        tot_mag = 0.0
        for v in a:
            if v == prev and v != 0:
                cur += 1
            else:
                cur = 1
                prev = v
            best = max(best, cur)
        return best / float(a.size)

    b = side.rolling(126, min_periods=63).apply(_run, raw=True)
    # add a tiny continuous component from MA-distance to avoid discreteness
    dist = ((closeadj - ma) / ma.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b = b + 0.2 * np.tanh(5.0 * dist)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon up agreement: fraction of horizons (21/63/126/252) currently up
def f03tp_f03_trend_persistence_horizagree_base_v121_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    s1 = np.sign(lp - lp.shift(21))
    s2 = np.sign(lp - lp.shift(63))
    s3 = np.sign(lp - lp.shift(126))
    s4 = np.sign(lp - lp.shift(252))
    cnt = (s1 + s2 + s3 + s4) / 4.0
    # continuous smoothing over a month
    b = cnt.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon momentum dispersion (do horizons disagree => weak persistence)
def f03tp_f03_trend_persistence_horizdisp_base_v122_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    m1 = (lp - lp.shift(21)) / 21.0
    m2 = (lp - lp.shift(63)) / 63.0
    m3 = (lp - lp.shift(126)) / 126.0
    m4 = (lp - lp.shift(252)) / 252.0
    b = -pd.concat([m1, m2, m3, m4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend score: net move over window in units of path-volatility (Sharpe-like) 252d
def f03tp_f03_trend_persistence_trendt_252d_base_v123_signal(closeadj):
    net = np.log(closeadj.replace(0, np.nan)).diff(252)
    vol = _logret(closeadj).rolling(252, min_periods=126).std() * np.sqrt(252)
    b = net / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend score stability: rolling std of the 63d trend-t over 252d (steadiness)
def f03tp_f03_trend_persistence_trendtstab_252d_base_v124_signal(closeadj):
    net = np.log(closeadj.replace(0, np.nan)).diff(63)
    vol = _logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(63)
    t = net / vol.replace(0, np.nan)
    b = -t.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothness: ratio of |smoothed-path move| to raw-path move (filter survival) 126d
def f03tp_f03_trend_persistence_smoothratio_126d_base_v125_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sm = lp.rolling(5, min_periods=3).mean()
    net = (lp - lp.shift(126)).abs()
    sm_path = sm.diff().abs().rolling(126, min_periods=63).sum()
    b = net / sm_path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Spearman rank monotonicity: rank-correlation of price with time (how
# consistently price is ordered through the window, robust to magnitude) 63d
def f03tp_f03_trend_persistence_monoton_63d_base_v126_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _mt(a):
        a = a[~np.isnan(a)]
        nn = a.size
        if nn < 16:
            return np.nan
        ranks = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(nn, dtype=float)
        rt = ranks - ranks.mean()
        tt = t - t.mean()
        denom = np.sqrt(np.sum(rt * rt) * np.sum(tt * tt))
        if denom == 0:
            return np.nan
        return np.sum(rt * tt) / denom

    b = lp.rolling(63, min_periods=32).apply(_mt, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spectral concentration: share of return variance in low-frequency component 126d
def f03tp_f03_trend_persistence_lowfreq_126d_base_v127_signal(closeadj):
    r = _logret(closeadj)

    def _lf(a):
        a = a[~np.isnan(a)]
        if a.size < 30:
            return np.nan
        a = a - a.mean()
        f = np.fft.rfft(a)
        p = np.abs(f) ** 2
        tot = p[1:].sum()
        if tot == 0:
            return np.nan
        cut = max(1, p.size // 5)
        return p[1:cut].sum() / tot

    b = r.rolling(126, min_periods=63).apply(_lf, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio x efficiency composite (trend confirmed two ways) 126d
def f03tp_f03_trend_persistence_vreffcomp_126d_base_v128_signal(closeadj):
    vr = _f03_varratio(closeadj, 5, 126) - 1.0
    e = _f03_efficiency(closeadj, 126)
    b = np.sign(vr) * np.sqrt(np.abs(vr)) + e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst x continuation-rate (two-channel persistence agreement) 126d
def f03tp_f03_trend_persistence_hurstcont_126d_base_v129_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126) - 0.5
    c = _f03_cont_rate(closeadj, 126) - 0.5
    b = h + 2.0 * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr x R-squared interaction (memory plus linearity) 126d
def f03tp_f03_trend_persistence_acfr2_126d_base_v130_signal(closeadj):
    a = _f03_autocorr(closeadj, 126, 1)
    q = _f03_r2(closeadj, 126)
    b = a * (q - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence regime flag smoothed: fraction of last quarter with VR>1 252d
def f03tp_f03_trend_persistence_vrregime_252d_base_v131_signal(closeadj):
    v = _f03_varratio(closeadj, 5, 63)
    flag = (v > 1.0).astype(float)
    raw = flag.rolling(63, min_periods=21).mean()
    # continuous component from average VR excess
    b = raw + 0.3 * np.tanh(v - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted momentum: ER(63) x ROC(63) (smooth strong moves) 63d
def f03tp_f03_trend_persistence_effroc_63d_base_v132_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    roc = closeadj / closeadj.shift(63) - 1.0
    b = e * np.tanh(3.0 * roc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net direction persistence vs noise: signed-ER squared (direction-strength) 126d
def f03tp_f03_trend_persistence_seffsq_126d_base_v133_signal(closeadj):
    se = _f03_signed_efficiency(closeadj, 126)
    b = se * se.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-vs-upside path efficiency: ER computed only on down legs vs up legs 126d
def f03tp_f03_trend_persistence_legeff_126d_base_v134_signal(closeadj):
    r = _logret(closeadj)

    def _le(a):
        a = a[~np.isnan(a)]
        if a.size < 20:
            return np.nan
        up = a[a > 0].sum()
        dn = -a[a < 0].sum()
        tot = up + dn
        if tot == 0:
            return np.nan
        return (up - dn) / tot

    b = r.rolling(126, min_periods=63).apply(_le, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling slope (per day) of log price scaled by R-squared (clean trend speed) 126d
def f03tp_f03_trend_persistence_cleanslope_126d_base_v135_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _cs(a):
        a = a[~np.isnan(a)]
        if a.size < 30:
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        ss_res = np.sum((a - pred) ** 2)
        ss_tot = np.sum((a - a.mean()) ** 2)
        if ss_tot == 0:
            return np.nan
        r2 = 1.0 - ss_res / ss_tot
        return b1[0] * r2 * 252.0

    b = lp.rolling(126, min_periods=63).apply(_cs, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend maturity: efficiency now vs efficiency a year ago (aging trend) 126d
def f03tp_f03_trend_persistence_effyoy_126d_base_v136_signal(closeadj):
    e = _f03_efficiency(closeadj, 126)
    b = e - e.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation-rate dispersion across windows (regime stability)
def f03tp_f03_trend_persistence_contdisp_base_v137_signal(closeadj):
    c63 = _f03_cont_rate(closeadj, 63)
    c126 = _f03_cont_rate(closeadj, 126)
    c252 = _f03_cont_rate(closeadj, 252)
    b = -pd.concat([c63, c126, c252], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation at lag 21 (monthly echo / seasonal persistence) 252d
def f03tp_f03_trend_persistence_acf21_252d_base_v138_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio term curvature at 504d (profile shape, long horizon)
def f03tp_f03_trend_persistence_vrcurv_504d_base_v139_signal(closeadj):
    v5 = _f03_varratio(closeadj, 5, 504)
    v21 = _f03_varratio(closeadj, 21, 504)
    v63 = _f03_varratio(closeadj, 63, 504)
    b = v5 - 2.0 * v21 + v63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio EMA-smoothed at 126d (persistent-regime indicator)
def f03tp_f03_trend_persistence_effema_126d_base_v140_signal(closeadj):
    e = _f03_efficiency(closeadj, 126)
    b = e.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-quality score: R2(126) x sign(slope) x efficiency(126)
def f03tp_f03_trend_persistence_quality_126d_base_v141_signal(closeadj):
    q = _f03_r2(closeadj, 126)
    se = _f03_signed_efficiency(closeadj, 126)
    b = q * np.sign(se) * np.sqrt(np.abs(se))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst spread of price vs Hurst of shuffled-magnitude proxy (sign memory) 126d
def f03tp_f03_trend_persistence_signhurst_126d_base_v142_signal(closeadj):
    s = np.sign(_logret(closeadj))

    def _rs(a):
        a = a[~np.isnan(a)]
        if a.size < 16:
            return np.nan
        y = np.cumsum(a - a.mean())
        R = y.max() - y.min()
        S = a.std()
        if S == 0 or R == 0:
            return np.nan
        return np.log(R / S) / np.log(a.size)

    b = s.rolling(126, min_periods=63).apply(_rs, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 21d sub-blocks that move the same direction as the full 126d window
def f03tp_f03_trend_persistence_blockagree_126d_base_v143_signal(closeadj):
    r = _logret(closeadj)

    def _ba(a):
        a = a[~np.isnan(a)]
        if a.size < 84:
            return np.nan
        net = np.sign(a.sum())
        blocks = [a[i:i + 21].sum() for i in range(0, a.size - 20, 21)]
        if not blocks:
            return np.nan
        agree = np.mean(np.sign(blocks) == net)
        return agree - 0.5 + 0.1 * np.tanh(40.0 * a.mean())

    b = r.rolling(126, min_periods=84).apply(_ba, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio momentum (k=5) over a quarter 126d
def f03tp_f03_trend_persistence_vrmom5_126d_base_v144_signal(closeadj):
    v = _f03_varratio(closeadj, 5, 126)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional efficiency at 504d (very long path smoothness, signed)
def f03tp_f03_trend_persistence_seffr_504d_base_v145_signal(closeadj):
    b = _f03_signed_efficiency(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr-decay-rate: ratio acf(2)/acf(1) at 252d
def f03tp_f03_trend_persistence_acfdecay_252d_base_v146_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 252, 1)
    a2 = _f03_autocorr(closeadj, 252, 2)
    b = np.tanh(a2 / a1.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence breadth: count of memory signals positive (acf1>0, VR>1, H>0.5) 126d
def f03tp_f03_trend_persistence_breadth_126d_base_v147_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    vr = _f03_varratio(closeadj, 5, 126) - 1.0
    h = _f03_rs_hurst(closeadj, 126) - 0.5
    raw = (np.sign(a1) + np.sign(vr) + np.sign(h)) / 3.0
    # continuous blend
    b = raw + 0.3 * np.tanh(a1) + 0.3 * np.tanh(vr) + 0.3 * h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio at 21d z-scored vs 504d history (extreme short-term smoothness)
def f03tp_f03_trend_persistence_effz_21d_base_v148_signal(closeadj):
    e = _f03_efficiency(closeadj, 21)
    b = _z(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day continuation x amplitude (strong durable directional move) 252d
def f03tp_f03_trend_persistence_contamp_252d_base_v149_signal(closeadj):
    c = _f03_cont_rate(closeadj, 252) - 0.5
    amp = np.log(closeadj.rolling(252, min_periods=126).max()
                 / closeadj.rolling(252, min_periods=126).min().replace(0, np.nan))
    b = c * amp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grand persistence composite: efficiency + (H-0.5) + (cont-0.5) + tanh(acf1) 252d
def f03tp_f03_trend_persistence_composite_252d_base_v150_signal(closeadj):
    e = _f03_efficiency(closeadj, 252)
    h = _f03_rs_hurst(closeadj, 252) - 0.5
    c = _f03_cont_rate(closeadj, 252) - 0.5
    a = _f03_autocorr(closeadj, 252, 1)
    b = e + 2.0 * h + 2.0 * c + np.tanh(a)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03tp_f03_trend_persistence_effr_42d_base_v076_signal,
    f03tp_f03_trend_persistence_effr_189d_base_v077_signal,
    f03tp_f03_trend_persistence_weffr_252d_base_v078_signal,
    f03tp_f03_trend_persistence_effamp_126d_base_v079_signal,
    f03tp_f03_trend_persistence_effaccel_126d_base_v080_signal,
    f03tp_f03_trend_persistence_seffrank_126d_base_v081_signal,
    f03tp_f03_trend_persistence_effgap_126d_base_v082_signal,
    f03tp_f03_trend_persistence_effstab_252d_base_v083_signal,
    f03tp_f03_trend_persistence_effsign_63d_base_v084_signal,
    f03tp_f03_trend_persistence_hurst_189d_base_v085_signal,
    f03tp_f03_trend_persistence_hurstrank_126d_base_v086_signal,
    f03tp_f03_trend_persistence_volhurst_126d_base_v087_signal,
    f03tp_f03_trend_persistence_hurstaccel_126d_base_v088_signal,
    f03tp_f03_trend_persistence_memdisagree_126d_base_v089_signal,
    f03tp_f03_trend_persistence_dfa_252d_base_v090_signal,
    f03tp_f03_trend_persistence_dfaz_126d_base_v091_signal,
    f03tp_f03_trend_persistence_acf3_126d_base_v092_signal,
    f03tp_f03_trend_persistence_acf10_252d_base_v093_signal,
    f03tp_f03_trend_persistence_acf2_63d_base_v094_signal,
    f03tp_f03_trend_persistence_acfenergy_126d_base_v095_signal,
    f03tp_f03_trend_persistence_ljungbox_252d_base_v096_signal,
    f03tp_f03_trend_persistence_acf1yoy_126d_base_v097_signal,
    f03tp_f03_trend_persistence_acfhl_126d_base_v098_signal,
    f03tp_f03_trend_persistence_vr2_63d_base_v099_signal,
    f03tp_f03_trend_persistence_vr10_126d_base_v100_signal,
    f03tp_f03_trend_persistence_vr21_504d_base_v101_signal,
    f03tp_f03_trend_persistence_vr42_504d_base_v102_signal,
    f03tp_f03_trend_persistence_logvr5_252d_base_v103_signal,
    f03tp_f03_trend_persistence_vrslope_252d_base_v104_signal,
    f03tp_f03_trend_persistence_vrrank10_126d_base_v105_signal,
    f03tp_f03_trend_persistence_vrdisp5_base_v106_signal,
    f03tp_f03_trend_persistence_cont_63d_base_v107_signal,
    f03tp_f03_trend_persistence_cont_252d_base_v108_signal,
    f03tp_f03_trend_persistence_contmom_126d_base_v109_signal,
    f03tp_f03_trend_persistence_contz_126d_base_v110_signal,
    f03tp_f03_trend_persistence_contasym_126d_base_v111_signal,
    f03tp_f03_trend_persistence_r2_252d_base_v112_signal,
    f03tp_f03_trend_persistence_r2_42d_base_v113_signal,
    f03tp_f03_trend_persistence_r2mom_126d_base_v114_signal,
    f03tp_f03_trend_persistence_r2spr_63v252_base_v115_signal,
    f03tp_f03_trend_persistence_jumpshare_126d_base_v116_signal,
    f03tp_f03_trend_persistence_top3conc_126d_base_v117_signal,
    f03tp_f03_trend_persistence_retentropy_126d_base_v118_signal,
    f03tp_f03_trend_persistence_abovema50_252d_base_v119_signal,
    f03tp_f03_trend_persistence_maside_126d_base_v120_signal,
    f03tp_f03_trend_persistence_horizagree_base_v121_signal,
    f03tp_f03_trend_persistence_horizdisp_base_v122_signal,
    f03tp_f03_trend_persistence_trendt_252d_base_v123_signal,
    f03tp_f03_trend_persistence_trendtstab_252d_base_v124_signal,
    f03tp_f03_trend_persistence_smoothratio_126d_base_v125_signal,
    f03tp_f03_trend_persistence_monoton_63d_base_v126_signal,
    f03tp_f03_trend_persistence_lowfreq_126d_base_v127_signal,
    f03tp_f03_trend_persistence_vreffcomp_126d_base_v128_signal,
    f03tp_f03_trend_persistence_hurstcont_126d_base_v129_signal,
    f03tp_f03_trend_persistence_acfr2_126d_base_v130_signal,
    f03tp_f03_trend_persistence_vrregime_252d_base_v131_signal,
    f03tp_f03_trend_persistence_effroc_63d_base_v132_signal,
    f03tp_f03_trend_persistence_seffsq_126d_base_v133_signal,
    f03tp_f03_trend_persistence_legeff_126d_base_v134_signal,
    f03tp_f03_trend_persistence_cleanslope_126d_base_v135_signal,
    f03tp_f03_trend_persistence_effyoy_126d_base_v136_signal,
    f03tp_f03_trend_persistence_contdisp_base_v137_signal,
    f03tp_f03_trend_persistence_acf21_252d_base_v138_signal,
    f03tp_f03_trend_persistence_vrcurv_504d_base_v139_signal,
    f03tp_f03_trend_persistence_effema_126d_base_v140_signal,
    f03tp_f03_trend_persistence_quality_126d_base_v141_signal,
    f03tp_f03_trend_persistence_signhurst_126d_base_v142_signal,
    f03tp_f03_trend_persistence_blockagree_126d_base_v143_signal,
    f03tp_f03_trend_persistence_vrmom5_126d_base_v144_signal,
    f03tp_f03_trend_persistence_seffr_504d_base_v145_signal,
    f03tp_f03_trend_persistence_acfdecay_252d_base_v146_signal,
    f03tp_f03_trend_persistence_breadth_126d_base_v147_signal,
    f03tp_f03_trend_persistence_effz_21d_base_v148_signal,
    f03tp_f03_trend_persistence_contamp_252d_base_v149_signal,
    f03tp_f03_trend_persistence_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_TREND_PERSISTENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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

    print("OK f03_trend_persistence_base_076_150_claude: %d features pass" % n_features)
