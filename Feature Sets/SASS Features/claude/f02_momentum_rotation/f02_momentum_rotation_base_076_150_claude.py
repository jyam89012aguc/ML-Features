import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (momentum rotation) =====
def _f02_roc(close, w):
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _f02_logmom(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_vol(close, w):
    return close.pct_change().rolling(w, min_periods=max(1, w // 2)).std()


def _f02_ewmamom(close, span):
    return close.pct_change().ewm(span=span, min_periods=max(2, span // 2)).mean()


def _f02_annmom(close, w):
    # annualized log momentum over window w
    return _f02_logmom(close, w) * (252.0 / w)


# ============================================================
# --- EWMA crossover momentum: fast EWMA price vs slow EWMA price (MACD-style, on closeadj) ---
def f02mr_f02_momentum_rotation_emacross_21_63_base_v076_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=10).mean()
    slow = closeadj.ewm(span=63, min_periods=21).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emacross_63_126_base_v077_signal(closeadj):
    fast = closeadj.ewm(span=63, min_periods=21).mean()
    slow = closeadj.ewm(span=126, min_periods=63).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emacross_50_200_base_v078_signal(closeadj):
    # 50/200 EMA cross minus its own signal line (golden/death-cross momentum, de-trended)
    fast = closeadj.ewm(span=50, min_periods=25).mean()
    slow = closeadj.ewm(span=200, min_periods=100).mean()
    cross = fast / slow.replace(0, np.nan) - 1.0
    b = cross - cross.ewm(span=50, min_periods=25).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MACD signal-line histogram (momentum of the EMA-cross itself) ---
def f02mr_f02_momentum_rotation_macdhist_base_v079_signal(closeadj):
    macd = closeadj.ewm(span=26, min_periods=13).mean() - closeadj.ewm(span=12, min_periods=6).mean()
    sig = macd.ewm(span=9, min_periods=5).mean()
    b = (macd - sig) / closeadj.replace(0, np.nan)
    result = -b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum-of-momentum: ROC of the 63d ROC series (second-order trend) ---
def f02mr_f02_momentum_rotation_momofmom_63d_base_v080_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-of-momentum over a longer base (126d ROC change over a quarter)
def f02mr_f02_momentum_rotation_momofmom_126d_base_v081_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-window momentum ratio (short / long annualized momentum), tanh-bounded ---
def f02mr_f02_momentum_rotation_momratio_21v63_base_v082_signal(closeadj):
    short = _f02_annmom(closeadj, 21)
    long = _f02_annmom(closeadj, 63)
    b = np.tanh(short - long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momratio_63v126_base_v083_signal(closeadj):
    short = _f02_annmom(closeadj, 63)
    long = _f02_annmom(closeadj, 126)
    b = np.tanh(short - long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momratio_126v252_base_v084_signal(closeadj):
    short = _f02_annmom(closeadj, 126)
    long = _f02_annmom(closeadj, 252)
    b = np.tanh(short - long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- percentile term-structure: rank(63d mom over 126) minus rank(126d mom over 252) ---
def f02mr_f02_momentum_rotation_rankts_63v126_base_v085_signal(closeadj):
    r63 = _rank(_f02_roc(closeadj, 63), 126)
    r126 = _rank(_f02_roc(closeadj, 126), 252)
    b = r63 - r126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume-weighted momentum: dollar-volume weighted average daily return over 63d ---
def f02mr_f02_momentum_rotation_dvwmom_63d_base_v086_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    num = (r * dv).rolling(63, min_periods=21).sum()
    den = dv.rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted momentum minus equal-weighted momentum (smart-money tilt)
def f02mr_f02_momentum_rotation_dvwtilt_63d_base_v087_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    vw = (r * dv).rolling(63, min_periods=21).sum() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    ew = r.rolling(63, min_periods=21).mean()
    b = (vw - ew) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative-volume-confirmed momentum: 63d ROC times z-scored relative volume ---
def f02mr_f02_momentum_rotation_relvolmom_63d_base_v088_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 63)
    relvol = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = np.sign(roc) * np.tanh(_z(relvol, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Aroon-style momentum oscillator: (days since N-high - days since N-low)/N ---
def f02mr_f02_momentum_rotation_aroon_63d_base_v089_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    up = 1.0 - closeadj.rolling(63, min_periods=21).apply(_dsh, raw=True)
    dn = 1.0 - closeadj.rolling(63, min_periods=21).apply(_dsl, raw=True)
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_aroon_126d_base_v090_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    up = 1.0 - closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    dn = 1.0 - closeadj.rolling(126, min_periods=63).apply(_dsl, raw=True)
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RSI-style momentum: normalized average gain vs average loss over 21d ---
def f02mr_f02_momentum_rotation_rsi_21d_base_v091_signal(closeadj):
    d = closeadj.diff()
    gain = d.where(d > 0, 0.0).rolling(21, min_periods=10).mean()
    loss = (-d.where(d < 0, 0.0)).rolling(21, min_periods=10).mean()
    rs = gain / loss.replace(0, np.nan)
    b = (1.0 - 1.0 / (1.0 + rs)) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsi_63d_base_v092_signal(closeadj):
    d = closeadj.diff()
    gain = d.where(d > 0, 0.0).rolling(63, min_periods=21).mean()
    loss = (-d.where(d < 0, 0.0)).rolling(63, min_periods=21).mean()
    rs = gain / loss.replace(0, np.nan)
    b = (1.0 - 1.0 / (1.0 + rs)) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RSI divergence vs price: 21d RSI change minus 21d price-momentum change (oscillator divergence)
def f02mr_f02_momentum_rotation_rsidiverge_base_v093_signal(closeadj):
    d = closeadj.diff()
    g = d.where(d > 0, 0.0).rolling(21, min_periods=10).mean()
    l = (-d.where(d < 0, 0.0)).rolling(21, min_periods=10).mean()
    rsi = 1.0 - 1.0 / (1.0 + g / l.replace(0, np.nan))
    rsi_chg = rsi - rsi.shift(21)
    px_chg = _f02_roc(closeadj, 21) - _f02_roc(closeadj, 21).shift(21)
    b = np.tanh(10.0 * rsi_chg) - np.tanh(20.0 * px_chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TSI (true strength index): double-smoothed momentum ---
def f02mr_f02_momentum_rotation_tsi_base_v094_signal(closeadj):
    d = closeadj.diff()
    pc1 = d.ewm(span=25, min_periods=13).mean().ewm(span=13, min_periods=7).mean()
    apc1 = d.abs().ewm(span=25, min_periods=13).mean().ewm(span=13, min_periods=7).mean()
    b = pc1 / apc1.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Coppock-style long-horizon momentum (weighted sum of two ROCs, smoothed) ---
def f02mr_f02_momentum_rotation_coppock_base_v095_signal(closeadj):
    roc1 = _f02_roc(closeadj, 294)
    roc2 = _f02_roc(closeadj, 231)
    b = (roc1 + roc2).rolling(210, min_periods=63).apply(
        lambda a: float(np.average(a, weights=np.arange(1, len(a) + 1))), raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- KST-style: sum of four smoothed ROCs of increasing horizon (know-sure-thing) ---
def f02mr_f02_momentum_rotation_kst_base_v096_signal(closeadj):
    r1 = _f02_roc(closeadj, 21).rolling(21, min_periods=10).mean()
    r2 = _f02_roc(closeadj, 42).rolling(21, min_periods=10).mean()
    r3 = _f02_roc(closeadj, 63).rolling(21, min_periods=10).mean()
    r4 = _f02_roc(closeadj, 126).rolling(31, min_periods=15).mean()
    b = 1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum vol-of-vol: dispersion of 21d momentum readings over a year (rotation instability) ---
def f02mr_f02_momentum_rotation_momvov_base_v097_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- skip-month reversal: most recent 21d return sign vs prior 11-month return (rotation tilt) ---
def f02mr_f02_momentum_rotation_skiprev_base_v098_signal(closeadj):
    recent = _f02_roc(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(252).replace(0, np.nan) - 1.0
    b = np.sign(prior) * (-recent)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum breadth across overlapping horizons weighted by recency ---
def f02mr_f02_momentum_rotation_recencybreadth_base_v099_signal(closeadj):
    ws = [5, 10, 21, 42, 63, 126, 252]
    wts = [7, 6, 5, 4, 3, 2, 1]
    num = sum(wt * np.tanh(8.0 * _f02_roc(closeadj, w)) for w, wt in zip(ws, wts))
    b = num / float(sum(wts))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- annualized momentum dispersion across 21/63/126/252 (term-structure width) ranked ---
def f02mr_f02_momentum_rotation_anndispr_base_v100_signal(closeadj):
    a = _f02_annmom(closeadj, 21)
    b1 = _f02_annmom(closeadj, 63)
    c = _f02_annmom(closeadj, 126)
    d = _f02_annmom(closeadj, 252)
    disp = pd.concat([a, b1, c, d], axis=1).std(axis=1)
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum z-spread: z(21d mom) minus z(252d mom) over their own histories ---
def f02mr_f02_momentum_rotation_zspread_21v252_base_v101_signal(closeadj):
    z21 = _z(_f02_roc(closeadj, 21), 126)
    z252 = _z(_f02_roc(closeadj, 252), 504)
    b = z21 - z252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- positive-month count: fraction of last 12 21d-blocks that were up (consistency) ---
def f02mr_f02_momentum_rotation_posmonths_base_v102_signal(closeadj):
    mom21 = _f02_roc(closeadj, 21)
    blocks = [mom21.shift(21 * k) for k in range(12)]
    pos = sum((b > 0).astype(float) for b in blocks) / 12.0
    mag = mom21.rolling(252, min_periods=126).mean()
    b = (pos - 0.5) + 5.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum half-life via decay of autocorrelated drift (ewm spread of returns) ---
def f02mr_f02_momentum_rotation_decayspread_base_v103_signal(closeadj):
    r = closeadj.pct_change()
    fast = r.ewm(span=10, min_periods=5).mean()
    mid = r.ewm(span=42, min_periods=21).mean()
    slow = r.ewm(span=126, min_periods=63).mean()
    b = (fast - 2.0 * mid + slow) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- risk-adjusted momentum dispersion: spread of Sharpe across windows ---
def f02mr_f02_momentum_rotation_sharpedispr_base_v104_signal(closeadj):
    r = closeadj.pct_change()
    sh21 = _mean(r, 21) / _std(r, 21).replace(0, np.nan)
    sh63 = _mean(r, 63) / _std(r, 63).replace(0, np.nan)
    sh126 = _mean(r, 126) / _std(r, 126).replace(0, np.nan)
    b = pd.concat([sh21, sh63, sh126], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum acceleration agreement across windows (tanh-weighted, continuous) ---
def f02mr_f02_momentum_rotation_accelagree_base_v105_signal(closeadj):
    a21 = _f02_roc(closeadj, 21) - _f02_roc(closeadj, 21).shift(21)
    a63 = _f02_roc(closeadj, 63) - _f02_roc(closeadj, 63).shift(63)
    a126 = _f02_roc(closeadj, 126) - _f02_roc(closeadj, 126).shift(126)
    b = (np.tanh(8.0 * a21) + np.tanh(5.0 * a63) + np.tanh(4.0 * a126)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- trend-quality: 63d log-slope divided by residual std around the trend (R-like) ---
def f02mr_f02_momentum_rotation_trendqual_63d_base_v106_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _tq(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd ** 2).sum()
        if denom == 0:
            return np.nan
        slope = np.dot(xd, a - a.mean()) / denom
        resid = a - (a.mean() + slope * xd)
        rs = resid.std()
        if rs == 0:
            return np.nan
        return float(slope / rs)
    b = lp.rolling(63, min_periods=31).apply(_tq, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_trendqual_126d_base_v107_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _tq(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd ** 2).sum()
        if denom == 0:
            return np.nan
        slope = np.dot(xd, a - a.mean()) / denom
        resid = a - (a.mean() + slope * xd)
        rs = resid.std()
        if rs == 0:
            return np.nan
        return float(slope / rs)
    b = lp.rolling(126, min_periods=63).apply(_tq, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum percentile vs cross-time, smoothed and signed by long trend ---
def f02mr_f02_momentum_rotation_rankgate_base_v108_signal(closeadj):
    rk = _rank(_f02_roc(closeadj, 63), 252)
    longsig = np.sign(_f02_logmom(closeadj, 252))
    b = rk * longsig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exponential-window weighted momentum (linearly-weighted ROC over 63d) ---
def f02mr_f02_momentum_rotation_wgtmom_63d_base_v109_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(63, min_periods=21).apply(
        lambda a: float(np.average(a, weights=np.arange(1, len(a) + 1))), raw=True) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- front-weighted minus back-weighted momentum (where in the window the move happened) ---
def f02mr_f02_momentum_rotation_wgtskew_63d_base_v110_signal(closeadj):
    r = closeadj.pct_change()
    fwd = r.rolling(63, min_periods=21).apply(
        lambda a: float(np.average(a, weights=np.arange(1, len(a) + 1))), raw=True)
    bwd = r.rolling(63, min_periods=21).apply(
        lambda a: float(np.average(a, weights=np.arange(len(a), 0, -1))), raw=True)
    b = (fwd - bwd) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-regime momentum gate: 63d momentum only counted when vol is below its median ---
def f02mr_f02_momentum_rotation_lowvolmom_63d_base_v111_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    vol = _f02_vol(closeadj, 63)
    volrank = _rank(vol, 252) + 0.5
    b = roc * (1.0 - volrank)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum entropy: how evenly distributed daily returns are (Shannon-like on |r| shares) ---
def f02mr_f02_momentum_rotation_retentropy_63d_base_v112_signal(closeadj):
    ar = closeadj.pct_change().abs()

    def _ent(a):
        s = a.sum()
        if s <= 0:
            return np.nan
        p = a / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(a)))
    b = ar.rolling(63, min_periods=31).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cumulative momentum drift via net up-days blended with net dollar drift (continuous) ---
def f02mr_f02_momentum_rotation_netupdays_126d_base_v113_signal(closeadj):
    sgn = np.sign(closeadj.pct_change())
    net = sgn.rolling(126, min_periods=63).sum() / 126.0
    drift = _f02_roc(closeadj, 126)
    b = net + 3.0 * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 21d momentum rank gated by whether 63d momentum confirms direction ---
def f02mr_f02_momentum_rotation_confirmrank_base_v114_signal(closeadj):
    rk21 = _rank(_f02_roc(closeadj, 21), 126)
    confirm = (np.sign(_f02_roc(closeadj, 21)) == np.sign(_f02_roc(closeadj, 63))).astype(float)
    b = rk21 * (0.5 + confirm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum curvature via three-point second difference of log price, ranked vs history ---
def f02mr_f02_momentum_rotation_logcurv_126d_base_v115_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    curv = lp - 2.0 * lp.shift(63) + lp.shift(126)
    b = _rank(curv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- excess momentum vs its own 504d mean (de-trended long momentum) ranked ---
def f02mr_f02_momentum_rotation_excessrank_252d_base_v116_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    ex = roc - roc.rolling(504, min_periods=252).mean()
    b = _rank(ex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- short-vs-long up-day-rate spread (consistency rotation) ---
def f02mr_f02_momentum_rotation_hitratespr_base_v117_signal(closeadj):
    up = (closeadj.pct_change() > 0).astype(float)
    hr21 = up.rolling(21, min_periods=10).mean()
    hr126 = up.rolling(126, min_periods=63).mean()
    b = hr21 - hr126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum quality: 126d return divided by 126d ulcer index (downside-path-aware) ---
def f02mr_f02_momentum_rotation_ulcermom_126d_base_v118_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    peak = closeadj.rolling(126, min_periods=63).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0)
    ulcer = np.sqrt((dd ** 2).rolling(126, min_periods=63).mean())
    b = roc / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regression-residual momentum: latest log-price minus its 63d trend extrapolation ---
def f02mr_f02_momentum_rotation_trendresid_63d_base_v119_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _resid(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd ** 2).sum()
        if denom == 0:
            return np.nan
        slope = np.dot(xd, a - a.mean()) / denom
        fit_last = a.mean() + slope * xd[-1]
        return float(a[-1] - fit_last)
    b = lp.rolling(63, min_periods=31).apply(_resid, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum diffusion change: how the multi-horizon positivity shifted over a month ---
def f02mr_f02_momentum_rotation_diffusechg_base_v120_signal(closeadj):
    ws = [5, 21, 63, 126]
    soft = sum(np.tanh(5.0 * _f02_annmom(closeadj, w)) for w in ws) / float(len(ws))
    b = soft - soft.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum vs benchmark drift: 63d ROC minus its own 252d EWMA (regime excess) ---
def f02mr_f02_momentum_rotation_regimeexcess_63d_base_v121_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.ewm(span=252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- turnover-scaled momentum efficiency, ranked vs its own 252d history ---
def f02mr_f02_momentum_rotation_turnmom_63d_base_v122_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    turn = closeadj.pct_change().abs().rolling(63, min_periods=21).sum()
    eff = roc / turn.replace(0, np.nan)
    b = _rank(eff, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum sign persistence weighted by daily return size (trend-aligned participation) ---
def f02mr_f02_momentum_rotation_signpersist_63d_base_v123_signal(closeadj):
    r = closeadj.pct_change()
    trend = np.sign(_f02_roc(closeadj, 63))
    aligned = (r * trend)
    b = aligned.rolling(63, min_periods=21).mean() / r.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- annualized momentum convexity across the term structure (short+long-2mid) ranked ---
def f02mr_f02_momentum_rotation_anncurv_base_v124_signal(closeadj):
    short = _f02_annmom(closeadj, 21)
    mid = _f02_annmom(closeadj, 63)
    long = _f02_annmom(closeadj, 252)
    curv = short + long - 2.0 * mid
    b = _rank(curv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-normalized cumulative return path (z of price vs its own 63d band) ---
def f02mr_f02_momentum_rotation_pricez_63d_base_v125_signal(closeadj):
    b = _z(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- price z-score spread: short band vs long band (momentum stretch rotation) ---
def f02mr_f02_momentum_rotation_pricezspr_base_v126_signal(closeadj):
    z63 = _z(closeadj, 63)
    z252 = _z(closeadj, 252)
    b = z63 - z252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum reversal pressure: distance of 5d return from its 63d mean in std units ---
def f02mr_f02_momentum_rotation_shockz_5d_base_v127_signal(closeadj):
    r5 = _f02_roc(closeadj, 5)
    b = _z(r5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum stability ratio: |252d mom| divided by sum of |quarterly moms| (smoothness) ---
def f02mr_f02_momentum_rotation_stabratio_base_v128_signal(closeadj):
    net = _f02_logmom(closeadj, 252).abs()
    q1 = _f02_logmom(closeadj, 63).abs()
    q2 = np.log(closeadj.shift(63).replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan)).abs()
    q3 = np.log(closeadj.shift(126).replace(0, np.nan) / closeadj.shift(189).replace(0, np.nan)).abs()
    q4 = np.log(closeadj.shift(189).replace(0, np.nan) / closeadj.shift(252).replace(0, np.nan)).abs()
    gross = q1 + q2 + q3 + q4
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- recency-weighted relative strength: EWMA(span21) drift minus EWMA(span252) drift ---
def f02mr_f02_momentum_rotation_rsdrift_base_v129_signal(closeadj):
    r = closeadj.pct_change()
    b = (r.ewm(span=21, min_periods=10).mean() - r.ewm(span=252, min_periods=126).mean()) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum impulse: net magnitude of >1.5-sigma up vs down days over 63d (continuous) ---
def f02mr_f02_momentum_rotation_impulse_63d_base_v130_signal(closeadj):
    r = closeadj.pct_change()
    sd = r.rolling(63, min_periods=21).std()
    big_up = r.where(r > 1.5 * sd, 0.0)
    big_dn = (-r).where(r < -1.5 * sd, 0.0)
    b = (big_up - big_dn).rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum quality index: hit-rate times path-efficiency (consistent AND smooth) ---
def f02mr_f02_momentum_rotation_qualindex_63d_base_v131_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    net = (closeadj - closeadj.shift(63))
    gross = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = net / gross.replace(0, np.nan)
    b = hr * eff * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-horizon momentum rank average (composite rotation rank) ---
def f02mr_f02_momentum_rotation_rankcomposite_base_v132_signal(closeadj):
    r21 = _rank(_f02_roc(closeadj, 21), 126)
    r63 = _rank(_f02_roc(closeadj, 63), 252)
    r252 = _rank(_f02_roc(closeadj, 252), 504)
    b = (r21 + r63 + r252) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum dispersion-adjusted strength: 63d mom divided by cross-horizon dispersion ---
def f02mr_f02_momentum_rotation_dispadjmom_base_v133_signal(closeadj):
    a = _f02_annmom(closeadj, 21)
    b1 = _f02_annmom(closeadj, 63)
    c = _f02_annmom(closeadj, 126)
    d = _f02_annmom(closeadj, 252)
    disp = pd.concat([a, b1, c, d], axis=1).std(axis=1)
    b = b1 / (disp + disp.rolling(252, min_periods=63).mean()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 5d-vs-21d EWMA price oscillator (fast micro-momentum) ---
def f02mr_f02_momentum_rotation_microosc_base_v134_signal(closeadj):
    fast = closeadj.ewm(span=5, min_periods=3).mean()
    slow = closeadj.ewm(span=21, min_periods=10).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum z of EWMA-crossover (de-trended MACD-style) ---
def f02mr_f02_momentum_rotation_crossz_base_v135_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=10).mean()
    slow = closeadj.ewm(span=126, min_periods=63).mean()
    cross = fast / slow.replace(0, np.nan) - 1.0
    b = _z(cross, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volatility asymmetry (126d): upside vol share vs downside vol share, z-scored (regime, sign-free) ---
def f02mr_f02_momentum_rotation_asymmom_126d_base_v136_signal(closeadj):
    r = closeadj.pct_change()
    upvol = r.where(r > 0, 0.0).rolling(126, min_periods=63).std()
    dnvol = (-r.where(r < 0, 0.0)).rolling(126, min_periods=63).std()
    asym = (upvol - dnvol) / (upvol + dnvol).replace(0, np.nan)
    b = _z(asym, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum across calendar gaps: 252d return vs same window one year prior (persistence) ---
def f02mr_f02_momentum_rotation_yoypersist_base_v137_signal(closeadj):
    roc_now = _f02_roc(closeadj, 252)
    roc_prior = roc_now.shift(252)
    b = np.sign(roc_now) * np.sign(roc_prior) * (roc_now.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- directional-strength term-structure: 21d directional index minus 126d directional index ---
def f02mr_f02_momentum_rotation_dirstrength_63d_base_v138_signal(closeadj):
    upmove = closeadj.diff().clip(lower=0)
    dnmove = (-closeadj.diff()).clip(lower=0)

    def _di(w):
        u = upmove.rolling(w, min_periods=max(5, w // 2)).sum()
        d = dnmove.rolling(w, min_periods=max(5, w // 2)).sum()
        return (u - d) / (u + d).replace(0, np.nan)
    b = _di(21) - _di(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum thrust: fraction of 21d sub-windows in last year with positive return, signed ---
def f02mr_f02_momentum_rotation_thrust_base_v139_signal(closeadj):
    mom21 = _f02_roc(closeadj, 21)
    pos = (mom21 > 0).astype(float).rolling(252, min_periods=126).mean()
    b = (pos - 0.5) * np.sign(_f02_logmom(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum reversion gap: short z stretch opposing long trend (mean-reversion within trend) ---
def f02mr_f02_momentum_rotation_revgap_base_v140_signal(closeadj):
    stretch = _z(closeadj, 21)
    trend = np.sign(_f02_logmom(closeadj, 252))
    b = -stretch * trend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- compound risk-adjusted rotation: tanh(63d Sharpe-mom) times momentum diffusion ---
def f02mr_f02_momentum_rotation_compradj_base_v141_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    radj = np.tanh(roc / (_f02_vol(closeadj, 63) * np.sqrt(63)).replace(0, np.nan))
    diff = sum((_f02_roc(closeadj, w) > 0).astype(float) for w in [21, 63, 126]) / 3.0 - 0.5
    b = radj * (1.0 + diff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- velocity of relative strength rank (how fast the momentum percentile is changing) ---
def f02mr_f02_momentum_rotation_rankvel_base_v142_signal(closeadj):
    rk = _rank(_f02_roc(closeadj, 63), 252)
    b = rk - rk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum drawdown-of-momentum: how far below its 252d peak the 21d mom sits ---
def f02mr_f02_momentum_rotation_momdd_base_v143_signal(closeadj):
    mom = _f02_roc(closeadj, 21)
    peak = mom.rolling(252, min_periods=126).max()
    b = mom - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- accel-confirmed momentum: 63d momentum times sign of its own acceleration ---
def f02mr_f02_momentum_rotation_accelconfirm_base_v144_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    accel = roc - roc.shift(21)
    b = roc * np.sign(accel) * np.tanh(accel.abs() * 10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-scale momentum coherence: correlation of price with a linear ramp over 126d ---
def f02mr_f02_momentum_rotation_coherence_126d_base_v145_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _coh(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        if a.std() == 0:
            return np.nan
        return float(np.corrcoef(x, a)[0, 1])
    b = lp.rolling(126, min_periods=63).apply(_coh, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 2-week relative strength: 10d return rank vs its 126d distribution (smoothed micro-RS) ---
def f02mr_f02_momentum_rotation_wkrsrank_base_v146_signal(closeadj):
    mom = _f02_roc(closeadj, 10).ewm(span=5, min_periods=3).mean()
    b = _rank(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum vol-adjusted spread between 21d and 126d (term structure in risk units) ---
def f02mr_f02_momentum_rotation_radjspread_base_v147_signal(closeadj):
    radj21 = _f02_roc(closeadj, 21) / (_f02_vol(closeadj, 21) * np.sqrt(21)).replace(0, np.nan)
    radj126 = _f02_roc(closeadj, 126) / (_f02_vol(closeadj, 126) * np.sqrt(126)).replace(0, np.nan)
    b = radj21 - radj126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum gated by trend coherence: 252d mom only when path is coherent (high R) ---
def f02mr_f02_momentum_rotation_cohgatemom_base_v148_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _coh(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        if a.std() == 0:
            return np.nan
        return float(np.corrcoef(x, a)[0, 1])
    coh = lp.rolling(126, min_periods=63).apply(_coh, raw=True)
    roc = _f02_roc(closeadj, 252)
    b = roc * coh.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum surprise: 21d return minus EWMA-forecast of 21d returns (innovation) ---
def f02mr_f02_momentum_rotation_surprise_21d_base_v149_signal(closeadj):
    mom = _f02_roc(closeadj, 21)
    forecast = mom.ewm(span=63, min_periods=21).mean()
    sd = mom.rolling(126, min_periods=63).std()
    b = (mom - forecast) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- grand rotation composite: blended z of risk-adj mom, diffusion, and term-structure tilt ---
def f02mr_f02_momentum_rotation_grandcomposite_base_v150_signal(closeadj):
    radj = np.tanh(_f02_roc(closeadj, 63) / (_f02_vol(closeadj, 63) * np.sqrt(63)).replace(0, np.nan))
    tilt = np.tanh(_f02_annmom(closeadj, 21) - _f02_annmom(closeadj, 252))
    diff = sum((_f02_roc(closeadj, w) > 0).astype(float) for w in [21, 63, 126, 252]) / 4.0 - 0.5
    b = (radj + tilt + 2.0 * diff) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02mr_f02_momentum_rotation_emacross_21_63_base_v076_signal,
    f02mr_f02_momentum_rotation_emacross_63_126_base_v077_signal,
    f02mr_f02_momentum_rotation_emacross_50_200_base_v078_signal,
    f02mr_f02_momentum_rotation_macdhist_base_v079_signal,
    f02mr_f02_momentum_rotation_momofmom_63d_base_v080_signal,
    f02mr_f02_momentum_rotation_momofmom_126d_base_v081_signal,
    f02mr_f02_momentum_rotation_momratio_21v63_base_v082_signal,
    f02mr_f02_momentum_rotation_momratio_63v126_base_v083_signal,
    f02mr_f02_momentum_rotation_momratio_126v252_base_v084_signal,
    f02mr_f02_momentum_rotation_rankts_63v126_base_v085_signal,
    f02mr_f02_momentum_rotation_dvwmom_63d_base_v086_signal,
    f02mr_f02_momentum_rotation_dvwtilt_63d_base_v087_signal,
    f02mr_f02_momentum_rotation_relvolmom_63d_base_v088_signal,
    f02mr_f02_momentum_rotation_aroon_63d_base_v089_signal,
    f02mr_f02_momentum_rotation_aroon_126d_base_v090_signal,
    f02mr_f02_momentum_rotation_rsi_21d_base_v091_signal,
    f02mr_f02_momentum_rotation_rsi_63d_base_v092_signal,
    f02mr_f02_momentum_rotation_rsidiverge_base_v093_signal,
    f02mr_f02_momentum_rotation_tsi_base_v094_signal,
    f02mr_f02_momentum_rotation_coppock_base_v095_signal,
    f02mr_f02_momentum_rotation_kst_base_v096_signal,
    f02mr_f02_momentum_rotation_momvov_base_v097_signal,
    f02mr_f02_momentum_rotation_skiprev_base_v098_signal,
    f02mr_f02_momentum_rotation_recencybreadth_base_v099_signal,
    f02mr_f02_momentum_rotation_anndispr_base_v100_signal,
    f02mr_f02_momentum_rotation_zspread_21v252_base_v101_signal,
    f02mr_f02_momentum_rotation_posmonths_base_v102_signal,
    f02mr_f02_momentum_rotation_decayspread_base_v103_signal,
    f02mr_f02_momentum_rotation_sharpedispr_base_v104_signal,
    f02mr_f02_momentum_rotation_accelagree_base_v105_signal,
    f02mr_f02_momentum_rotation_trendqual_63d_base_v106_signal,
    f02mr_f02_momentum_rotation_trendqual_126d_base_v107_signal,
    f02mr_f02_momentum_rotation_rankgate_base_v108_signal,
    f02mr_f02_momentum_rotation_wgtmom_63d_base_v109_signal,
    f02mr_f02_momentum_rotation_wgtskew_63d_base_v110_signal,
    f02mr_f02_momentum_rotation_lowvolmom_63d_base_v111_signal,
    f02mr_f02_momentum_rotation_retentropy_63d_base_v112_signal,
    f02mr_f02_momentum_rotation_netupdays_126d_base_v113_signal,
    f02mr_f02_momentum_rotation_confirmrank_base_v114_signal,
    f02mr_f02_momentum_rotation_logcurv_126d_base_v115_signal,
    f02mr_f02_momentum_rotation_excessrank_252d_base_v116_signal,
    f02mr_f02_momentum_rotation_hitratespr_base_v117_signal,
    f02mr_f02_momentum_rotation_ulcermom_126d_base_v118_signal,
    f02mr_f02_momentum_rotation_trendresid_63d_base_v119_signal,
    f02mr_f02_momentum_rotation_diffusechg_base_v120_signal,
    f02mr_f02_momentum_rotation_regimeexcess_63d_base_v121_signal,
    f02mr_f02_momentum_rotation_turnmom_63d_base_v122_signal,
    f02mr_f02_momentum_rotation_signpersist_63d_base_v123_signal,
    f02mr_f02_momentum_rotation_anncurv_base_v124_signal,
    f02mr_f02_momentum_rotation_pricez_63d_base_v125_signal,
    f02mr_f02_momentum_rotation_pricezspr_base_v126_signal,
    f02mr_f02_momentum_rotation_shockz_5d_base_v127_signal,
    f02mr_f02_momentum_rotation_stabratio_base_v128_signal,
    f02mr_f02_momentum_rotation_rsdrift_base_v129_signal,
    f02mr_f02_momentum_rotation_impulse_63d_base_v130_signal,
    f02mr_f02_momentum_rotation_qualindex_63d_base_v131_signal,
    f02mr_f02_momentum_rotation_rankcomposite_base_v132_signal,
    f02mr_f02_momentum_rotation_dispadjmom_base_v133_signal,
    f02mr_f02_momentum_rotation_microosc_base_v134_signal,
    f02mr_f02_momentum_rotation_crossz_base_v135_signal,
    f02mr_f02_momentum_rotation_asymmom_126d_base_v136_signal,
    f02mr_f02_momentum_rotation_yoypersist_base_v137_signal,
    f02mr_f02_momentum_rotation_dirstrength_63d_base_v138_signal,
    f02mr_f02_momentum_rotation_thrust_base_v139_signal,
    f02mr_f02_momentum_rotation_revgap_base_v140_signal,
    f02mr_f02_momentum_rotation_compradj_base_v141_signal,
    f02mr_f02_momentum_rotation_rankvel_base_v142_signal,
    f02mr_f02_momentum_rotation_momdd_base_v143_signal,
    f02mr_f02_momentum_rotation_accelconfirm_base_v144_signal,
    f02mr_f02_momentum_rotation_coherence_126d_base_v145_signal,
    f02mr_f02_momentum_rotation_wkrsrank_base_v146_signal,
    f02mr_f02_momentum_rotation_radjspread_base_v147_signal,
    f02mr_f02_momentum_rotation_cohgatemom_base_v148_signal,
    f02mr_f02_momentum_rotation_surprise_21d_base_v149_signal,
    f02mr_f02_momentum_rotation_grandcomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_076_150 = REGISTRY


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

    print("OK f02_momentum_rotation_base_076_150_claude: %d features pass" % n_features)
