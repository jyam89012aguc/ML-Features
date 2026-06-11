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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _logmom(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _roc(close, w):
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _tstat(close, w):
    r = close.pct_change()
    m = r.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(2, w // 2)).std()
    return (m / sd.replace(0, np.nan)) * np.sqrt(float(w))


def _efficiency(close, w):
    net = (close - close.shift(w))
    gross = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / gross.replace(0, np.nan)


def _ols1(a):
    m = len(a)
    xc = np.arange(m, dtype=float) - (m - 1) / 2.0
    den = (xc ** 2).sum()
    if den == 0.0:
        return np.nan
    return float(np.dot(xc, a - a.mean()) / den)


def _olsslope(s, win):
    # least-squares slope of s over a trailing window of length `win`
    return s.rolling(win, min_periods=max(3, win // 2)).apply(_ols1, raw=True)


def _robustz(s, w):
    # median/IQR-standardized value over window w
    mp = max(1, w // 2)
    med = s.rolling(w, min_periods=mp).median()
    iqr = (s.rolling(w, min_periods=mp).quantile(0.75)
           - s.rolling(w, min_periods=mp).quantile(0.25))
    return (s - med) / iqr.replace(0, np.nan)


def _emadisp(close, w):
    # price-vs-EMA displacement minus its own slower EMA (band-pass oscillator)
    lp = np.log(close.replace(0, np.nan))
    disp = lp - lp.ewm(span=w, min_periods=max(1, w // 3)).mean()
    return disp - disp.ewm(span=2 * w, min_periods=max(1, w // 2)).mean()


# ---- derivative operators (math 1st/2nd discrete derivatives + decorrelating post-op) ----
def _slope_rank(base, k):
    sl = (base - base.shift(k)) / float(k)
    return sl.rolling(252, min_periods=126).rank(pct=True) - 0.5


def _slope_signrank(base, k):
    sl = (base - base.shift(k)) / float(k)
    return np.sign(sl) * sl.abs().rolling(252, min_periods=126).rank(pct=True)


def _slope_olsz(base, k):
    return _z(_olsslope(base, 2 * k), 252)


def _slope_bandpass(base, k):
    sl = (base - base.shift(k)) / float(k)
    return (sl.ewm(span=max(6, k), min_periods=max(3, k // 2)).mean()
            - sl.ewm(span=max(12, 3 * k), min_periods=max(6, k)).mean())


def _slope_volrank(base, close, k):
    vol = close.pct_change().rolling(max(21, k), min_periods=max(10, k // 2)).std()
    sl = (((base - base.shift(k)) / float(k)) / vol.replace(0, np.nan)).clip(-50, 50)
    return sl.rolling(252, min_periods=126).rank(pct=True) - 0.5


def _jerk_rank(base, k):
    jk = (base - 2.0 * base.shift(k) + base.shift(2 * k)) / float(k * k)
    return jk.rolling(252, min_periods=126).rank(pct=True) - 0.5


def _jerk_signrank(base, k):
    jk = (base - 2.0 * base.shift(k) + base.shift(2 * k)) / float(k * k)
    return np.sign(jk) * jk.abs().rolling(252, min_periods=126).rank(pct=True)


def _jerk_olsz(base, k):
    sl = _olsslope(base, 2 * k)
    return _z((sl - sl.shift(k)) / float(k), 252)


def _jerk_bandpass(base, k):
    jk = (base - 2.0 * base.shift(k) + base.shift(2 * k)) / float(k * k)
    return (jk.ewm(span=max(6, k), min_periods=max(3, k // 2)).mean()
            - jk.ewm(span=max(12, 3 * k), min_periods=max(6, k)).mean())


def _jerk_volrank(base, close, k):
    vol = close.pct_change().rolling(max(21, k), min_periods=max(10, k // 2)).std()
    jk = (((base - 2.0 * base.shift(k) + base.shift(2 * k)) / float(k * k)) / vol.replace(0, np.nan)).clip(-50, 50)
    return jk.rolling(252, min_periods=126).rank(pct=True) - 0.5


# jerk of roc21(21d) k=5 v1
def f02cm_f02_commodity_momentum_rotation_roc21_21d_jerk_v001_signal(closeadj):
    base = _logmom(closeadj, 21)
    result = _jerk_signrank(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc42(42d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_roc42_42d_jerk_v002_signal(closeadj):
    base = _logmom(closeadj, 42)
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc63(63d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_roc63_63d_jerk_v003_signal(closeadj):
    base = _logmom(closeadj, 63)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc126(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_roc126_126d_jerk_v004_signal(closeadj):
    base = _logmom(closeadj, 126)
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc189(189d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_roc189_189d_jerk_v005_signal(closeadj):
    base = _logmom(closeadj, 189)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc252(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_roc252_252d_jerk_v006_signal(closeadj):
    base = _logmom(closeadj, 252)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc378(378d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_roc378_378d_jerk_v007_signal(closeadj):
    base = _logmom(closeadj, 378)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of roc504(504d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_roc504_504d_jerk_v008_signal(closeadj):
    base = _logmom(closeadj, 504)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sroc63(63d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_sroc63_63d_jerk_v009_signal(closeadj):
    base = _roc(closeadj, 63)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sroc126(126d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_sroc126_126d_jerk_v010_signal(closeadj):
    base = _roc(closeadj, 126)
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sroc252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_sroc252_252d_jerk_v011_signal(closeadj):
    base = _roc(closeadj, 252)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex126_21(126d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_momex126_21_126d_jerk_v012_signal(closeadj):
    base = _z((closeadj.shift(21)/closeadj.shift(126).replace(0,np.nan)-1.0), 504)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex189_21(189d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_momex189_21_189d_jerk_v013_signal(closeadj):
    base = _z((closeadj.shift(21)/closeadj.shift(189).replace(0,np.nan)-1.0), 504)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex252_21(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_momex252_21_252d_jerk_v014_signal(closeadj):
    base = _z((closeadj.shift(21)/closeadj.shift(252).replace(0,np.nan)-1.0), 504)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex378_21(378d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_momex378_21_378d_jerk_v015_signal(closeadj):
    base = _z((closeadj.shift(21)/closeadj.shift(378).replace(0,np.nan)-1.0), 504)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex504_21(504d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_momex504_21_504d_jerk_v016_signal(closeadj):
    base = _z((closeadj.shift(21)/closeadj.shift(504).replace(0,np.nan)-1.0), 504)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momex252_63(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_momex252_63_252d_jerk_v017_signal(closeadj):
    base = _z((closeadj.shift(63)/closeadj.shift(252).replace(0,np.nan)-1.0), 504)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tstat42(42d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_tstat42_42d_jerk_v018_signal(closeadj):
    base = _z(_tstat(closeadj, 42), 252)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tstat63(63d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_tstat63_63d_jerk_v019_signal(closeadj):
    base = _z(_tstat(closeadj, 63), 252)
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tstat126(126d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_tstat126_126d_jerk_v020_signal(closeadj):
    base = _z(_tstat(closeadj, 126), 252)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tstat189(189d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_tstat189_189d_jerk_v021_signal(closeadj):
    base = _z(_tstat(closeadj, 189), 504)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tstat252(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_tstat252_252d_jerk_v022_signal(closeadj):
    base = _z(_tstat(closeadj, 252), 504)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of eff42(42d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_eff42_42d_jerk_v023_signal(closeadj):
    base = _efficiency(closeadj, 42).abs()
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of eff63(63d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_eff63_63d_jerk_v024_signal(closeadj):
    base = _efficiency(closeadj, 63).abs()
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of eff126(126d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_eff126_126d_jerk_v025_signal(closeadj):
    base = _efficiency(closeadj, 126).abs()
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of eff189(189d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_eff189_189d_jerk_v026_signal(closeadj):
    base = _efficiency(closeadj, 189).abs()
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of eff252(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_eff252_252d_jerk_v027_signal(closeadj):
    base = _efficiency(closeadj, 252).abs()
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr21v63(63d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_spr21v63_63d_jerk_v028_signal(closeadj):
    base = (_logmom(closeadj, 21) - _logmom(closeadj, 63))
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr21v252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_spr21v252_252d_jerk_v029_signal(closeadj):
    base = (_logmom(closeadj, 21) - _logmom(closeadj, 252))
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr42v126(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_spr42v126_126d_jerk_v030_signal(closeadj):
    base = (_logmom(closeadj, 42) - _logmom(closeadj, 126))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr63v126(126d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_spr63v126_126d_jerk_v031_signal(closeadj):
    base = (_logmom(closeadj, 63) - _logmom(closeadj, 126))
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr63v252(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_spr63v252_252d_jerk_v032_signal(closeadj):
    base = (_logmom(closeadj, 63) - _logmom(closeadj, 252))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr126v252(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_spr126v252_252d_jerk_v033_signal(closeadj):
    base = (_logmom(closeadj, 126) - _logmom(closeadj, 252))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr126v504(504d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_spr126v504_504d_jerk_v034_signal(closeadj):
    base = (_logmom(closeadj, 126) - _logmom(closeadj, 504))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of spr252v504(504d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_spr252v504_504d_jerk_v035_signal(closeadj):
    base = (_logmom(closeadj, 252) - _logmom(closeadj, 504))
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momz63(63d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_momz63_63d_jerk_v036_signal(closeadj):
    base = _robustz(_logmom(closeadj, 63), 252)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momz126(126d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_momz126_126d_jerk_v037_signal(closeadj):
    base = _robustz(_logmom(closeadj, 126), 252)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momz252(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_momz252_252d_jerk_v038_signal(closeadj):
    base = _robustz(_logmom(closeadj, 252), 504)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momz504(504d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_momz504_504d_jerk_v039_signal(closeadj):
    base = _robustz(_logmom(closeadj, 504), 1260)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momrank126(126d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_momrank126_126d_jerk_v040_signal(closeadj):
    base = (_logmom(closeadj, 126).rolling(252, min_periods=126).rank(pct=True)-0.5)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momrank252(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_momrank252_252d_jerk_v041_signal(closeadj):
    base = (_logmom(closeadj, 252).rolling(756, min_periods=378).rank(pct=True)-0.5)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momrank441(441d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_momrank441_441d_jerk_v042_signal(closeadj):
    base = (_logmom(closeadj, 441).rolling(1260, min_periods=630).rank(pct=True)-0.5)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of strength63(63d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_strength63_63d_jerk_v043_signal(closeadj):
    base = _z(_logmom(closeadj, 63).abs(), 504)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of strength126(126d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_strength126_126d_jerk_v044_signal(closeadj):
    base = _z(_logmom(closeadj, 126).abs(), 504)
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of strength252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_strength252_252d_jerk_v045_signal(closeadj):
    base = _z(_logmom(closeadj, 252).abs(), 504)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of consist63(63d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_consist63_63d_jerk_v046_signal(closeadj):
    base = ((closeadj.pct_change()*closeadj.pct_change().shift(1)).rolling(63,min_periods=31).mean()/(closeadj.pct_change()*closeadj.pct_change()).rolling(63,min_periods=31).mean().replace(0,np.nan))
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of consist126(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_consist126_126d_jerk_v047_signal(closeadj):
    base = ((closeadj.pct_change()*closeadj.pct_change().shift(1)).rolling(126,min_periods=63).mean()/(closeadj.pct_change()*closeadj.pct_change()).rolling(126,min_periods=63).mean().replace(0,np.nan))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of consist252(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_consist252_252d_jerk_v048_signal(closeadj):
    base = ((closeadj.pct_change()*closeadj.pct_change().shift(1)).rolling(252,min_periods=126).mean()/(closeadj.pct_change()*closeadj.pct_change()).rolling(252,min_periods=126).mean().replace(0,np.nan))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of madist63(63d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_madist63_63d_jerk_v049_signal(closeadj):
    base = np.log(closeadj.replace(0,np.nan)/closeadj.rolling(63,min_periods=31).mean().replace(0,np.nan))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of madist126(126d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_madist126_126d_jerk_v050_signal(closeadj):
    base = np.log(closeadj.replace(0,np.nan)/closeadj.rolling(126,min_periods=63).mean().replace(0,np.nan))
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of madist252(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_madist252_252d_jerk_v051_signal(closeadj):
    base = np.log(closeadj.replace(0,np.nan)/closeadj.rolling(252,min_periods=126).mean().replace(0,np.nan))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of emadist42(42d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_emadist42_42d_jerk_v052_signal(closeadj):
    base = _emadisp(closeadj, 42)
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of emadist126(126d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_emadist126_126d_jerk_v053_signal(closeadj):
    base = _emadisp(closeadj, 126)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of emadist252(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_emadist252_252d_jerk_v054_signal(closeadj):
    base = _emadisp(closeadj, 252)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momrng126(126d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_momrng126_126d_jerk_v055_signal(closeadj):
    base = ((_logmom(closeadj, 126) - _logmom(closeadj, 126).rolling(504,min_periods=252).min())/(_logmom(closeadj, 126).rolling(504,min_periods=252).max()-_logmom(closeadj, 126).rolling(504,min_periods=252).min()).replace(0,np.nan)-0.5)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of momrng252(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_momrng252_252d_jerk_v056_signal(closeadj):
    base = ((_logmom(closeadj, 252) - _logmom(closeadj, 252).rolling(504,min_periods=252).min())/(_logmom(closeadj, 252).rolling(504,min_periods=252).max()-_logmom(closeadj, 252).rolling(504,min_periods=252).min()).replace(0,np.nan)-0.5)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of downadj126(126d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_downadj126_126d_jerk_v057_signal(closeadj):
    base = (_logmom(closeadj, 126)/((closeadj.pct_change().where(closeadj.pct_change()<0,0.0)).rolling(126,min_periods=63).std()*np.sqrt(126.0)).replace(0,np.nan)).rolling(504,min_periods=252).rank(pct=True)-0.5
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of downadj252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_downadj252_252d_jerk_v058_signal(closeadj):
    base = (_logmom(closeadj, 252)/((closeadj.pct_change().where(closeadj.pct_change()<0,0.0)).rolling(252,min_periods=126).std()*np.sqrt(252.0)).replace(0,np.nan)).rolling(504,min_periods=252).rank(pct=True)-0.5
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tanh126(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_tanh126_126d_jerk_v059_signal(closeadj):
    base = np.tanh(2.0*_logmom(closeadj, 126))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tanh252(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_tanh252_252d_jerk_v060_signal(closeadj):
    base = np.tanh(2.0*_logmom(closeadj, 252))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tanh504(504d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_tanh504_504d_jerk_v061_signal(closeadj):
    base = np.tanh(2.0*_logmom(closeadj, 504))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of signmag126(126d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_signmag126_126d_jerk_v062_signal(closeadj):
    base = (np.sign(_logmom(closeadj, 126))*(_logmom(closeadj, 126).abs()**0.5))
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of signmag252(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_signmag252_252d_jerk_v063_signal(closeadj):
    base = (np.sign(_logmom(closeadj, 252))*(_logmom(closeadj, 252).abs()**0.5))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of smooth63(63d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_smooth63_63d_jerk_v064_signal(closeadj):
    base = _logmom(closeadj, 63).ewm(span=31, min_periods=15).mean()
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of smooth126(126d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_smooth126_126d_jerk_v065_signal(closeadj):
    base = _logmom(closeadj, 126).ewm(span=63, min_periods=31).mean()
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of smooth252(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_smooth252_252d_jerk_v066_signal(closeadj):
    base = _logmom(closeadj, 252).ewm(span=126, min_periods=63).mean()
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of blend(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_blend_252d_jerk_v067_signal(closeadj):
    base = ((_z(_logmom(closeadj,21),252)+_z(_logmom(closeadj,63),252)+_z(_logmom(closeadj,126),252)+_z(_logmom(closeadj,252),504))/4.0)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of dvmom63(63d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_dvmom63_63d_jerk_v068_signal(closeadj, volume):
    base = (np.sign(_logmom(closeadj, 63)) * (((closeadj*volume) - (closeadj*volume).rolling(126,min_periods=63).mean())/(closeadj*volume).rolling(126,min_periods=63).std().replace(0,np.nan)).clip(-5,5))
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of dvmom126(126d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_dvmom126_126d_jerk_v069_signal(closeadj, volume):
    base = (np.sign(_logmom(closeadj, 126)) * (((closeadj*volume) - (closeadj*volume).rolling(252,min_periods=126).mean())/(closeadj*volume).rolling(252,min_periods=126).std().replace(0,np.nan)).clip(-5,5))
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of emagap63v252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_emagap63v252_252d_jerk_v070_signal(closeadj):
    base = (np.log(closeadj.replace(0,np.nan)).ewm(span=63,min_periods=21).mean() - np.log(closeadj.replace(0,np.nan)).ewm(span=252,min_periods=63).mean())
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of emagap21v63(63d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_emagap21v63_63d_jerk_v071_signal(closeadj):
    base = (np.log(closeadj.replace(0,np.nan)).ewm(span=21,min_periods=10).mean() - np.log(closeadj.replace(0,np.nan)).ewm(span=63,min_periods=21).mean())
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of selfrel126(126d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_selfrel126_126d_jerk_v072_signal(closeadj):
    base = (_logmom(closeadj, 126)/_logmom(closeadj, 126).rolling(504,min_periods=252).mean().abs().replace(0,np.nan))
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of selfrel252(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_selfrel252_252d_jerk_v073_signal(closeadj):
    base = (_logmom(closeadj, 252)/_logmom(closeadj, 252).rolling(504,min_periods=252).mean().abs().replace(0,np.nan))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of conv63(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_conv63_126d_jerk_v074_signal(closeadj):
    base = (_logmom(closeadj,63)-0.5*(_logmom(closeadj,21)+_logmom(closeadj,126)))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of conv252(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_conv252_252d_jerk_v075_signal(closeadj):
    base = (_logmom(closeadj,252)-0.5*(_logmom(closeadj,126)+_logmom(closeadj,504)))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of volofmom(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_volofmom_252d_jerk_v076_signal(closeadj):
    base = (_logmom(closeadj,63).rolling(63,min_periods=21).std()/_logmom(closeadj,63).rolling(252,min_periods=126).std().replace(0,np.nan)-1.0)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of stab252(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_stab252_252d_jerk_v077_signal(closeadj):
    base = _logmom(closeadj,21).rolling(252,min_periods=126).std()
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of stab504(504d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_stab504_504d_jerk_v078_signal(closeadj):
    base = _logmom(closeadj,21).rolling(504,min_periods=252).std()
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of cycdev252(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_cycdev252_252d_jerk_v079_signal(closeadj):
    base = (_logmom(closeadj,252)-_logmom(closeadj,252).rolling(504,min_periods=252).mean())
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of exhaust21(21d) k=5 v2
def f02cm_f02_commodity_momentum_rotation_exhaust21_21d_jerk_v080_signal(closeadj):
    base = (_logmom(closeadj, 21).abs() / _logmom(closeadj, 21).abs().rolling(252,min_periods=126).max().replace(0,np.nan))
    result = _jerk_olsz(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of exhaust63(63d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_exhaust63_63d_jerk_v081_signal(closeadj):
    base = (_logmom(closeadj, 63).abs() / _logmom(closeadj, 63).abs().rolling(252,min_periods=126).max().replace(0,np.nan))
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of glasym63(63d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_glasym63_63d_jerk_v082_signal(closeadj):
    base = ((closeadj.pct_change().where(closeadj.pct_change()>0,np.nan)).rolling(63,min_periods=15).mean() - (-closeadj.pct_change().where(closeadj.pct_change()<0,np.nan)).rolling(63,min_periods=15).mean())/((closeadj.pct_change().where(closeadj.pct_change()>0,np.nan)).rolling(63,min_periods=15).mean()+(-closeadj.pct_change().where(closeadj.pct_change()<0,np.nan)).rolling(63,min_periods=15).mean()).replace(0,np.nan)
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of skew126(126d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_skew126_126d_jerk_v083_signal(closeadj):
    base = closeadj.pct_change().rolling(126,min_periods=63).skew()
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of kurt126(126d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_kurt126_126d_jerk_v084_signal(closeadj):
    base = closeadj.pct_change().rolling(126,min_periods=63).kurt()
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of quality252(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_quality252_252d_jerk_v085_signal(closeadj):
    base = (np.sign(_logmom(closeadj,252))*_efficiency(closeadj,252).abs()*_logmom(closeadj,252).abs().rolling(504,min_periods=252).rank(pct=True))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of quality126(126d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_quality126_126d_jerk_v086_signal(closeadj):
    base = (np.sign(_logmom(closeadj,126))*_efficiency(closeadj,126).abs()*_logmom(closeadj,126).abs().rolling(252,min_periods=126).rank(pct=True))
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of xmean(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_xmean_252d_jerk_v087_signal(closeadj):
    base = (pd.concat([_logmom(closeadj,21),_logmom(closeadj,63),_logmom(closeadj,126),_logmom(closeadj,252)],axis=1).mean(axis=1))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of xdisp(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_xdisp_252d_jerk_v088_signal(closeadj):
    base = (pd.concat([_logmom(closeadj,21),_logmom(closeadj,63),_logmom(closeadj,126),_logmom(closeadj,252)],axis=1).std(axis=1))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tilt2412(504d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_tilt2412_504d_jerk_v089_signal(closeadj):
    base = ((closeadj.shift(21)/closeadj.shift(504).replace(0,np.nan)-1.0)-(closeadj.shift(21)/closeadj.shift(252).replace(0,np.nan)-1.0))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of tilt129(252d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_tilt129_252d_jerk_v090_signal(closeadj):
    base = ((closeadj.shift(21)/closeadj.shift(252).replace(0,np.nan)-1.0)-(closeadj.shift(21)/closeadj.shift(189).replace(0,np.nan)-1.0))
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of regimescaled(252d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_regimescaled_252d_jerk_v091_signal(closeadj):
    base = (_z(_logmom(closeadj,252),504)-_z(closeadj.pct_change().rolling(63,min_periods=21).std(),504))
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mom441z(441d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_mom441z_441d_jerk_v092_signal(closeadj):
    base = _z(np.log(closeadj.replace(0,np.nan)/closeadj.shift(441).replace(0,np.nan)),756)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of persist21(252d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_persist21_252d_jerk_v093_signal(closeadj):
    base = ((_logmom(closeadj,21)*_logmom(closeadj,21).shift(21)).rolling(252,min_periods=126).mean()/(_logmom(closeadj,21)*_logmom(closeadj,21)).rolling(252,min_periods=126).mean().replace(0,np.nan))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of vmdiv63(126d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_vmdiv63_126d_jerk_v094_signal(closeadj, volume):
    base = (_logmom(closeadj,63).rolling(252,min_periods=126).rank(pct=True) - np.log((closeadj*volume).rolling(21,min_periods=10).mean().replace(0,np.nan)/(closeadj*volume).rolling(63,min_periods=21).mean().replace(0,np.nan)).rolling(252,min_periods=126).rank(pct=True))
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom84(84d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_logmom84_84d_jerk_v095_signal(closeadj):
    base = _logmom(closeadj, 84)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom105(105d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_logmom105_105d_jerk_v096_signal(closeadj):
    base = _logmom(closeadj, 105)
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom147(147d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_logmom147_147d_jerk_v097_signal(closeadj):
    base = _logmom(closeadj, 147)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom168(168d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_logmom168_168d_jerk_v098_signal(closeadj):
    base = _logmom(closeadj, 168)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom210(210d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_logmom210_210d_jerk_v099_signal(closeadj):
    base = _logmom(closeadj, 210)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom231(231d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_logmom231_231d_jerk_v100_signal(closeadj):
    base = _logmom(closeadj, 231)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom294(294d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_logmom294_294d_jerk_v101_signal(closeadj):
    base = _logmom(closeadj, 294)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom315(315d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_logmom315_315d_jerk_v102_signal(closeadj):
    base = _logmom(closeadj, 315)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom441(441d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_logmom441_441d_jerk_v103_signal(closeadj):
    base = _logmom(closeadj, 441)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of logmom567(567d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_logmom567_567d_jerk_v104_signal(closeadj):
    base = _logmom(closeadj, 567)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of zmom42(42d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_zmom42_42d_jerk_v105_signal(closeadj):
    base = _z(_logmom(closeadj, 42) - _logmom(closeadj, 42).ewm(span=84, min_periods=42).mean(), 252)
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of zmom84(84d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_zmom84_84d_jerk_v106_signal(closeadj):
    base = _z(_logmom(closeadj, 84) - _logmom(closeadj, 84).ewm(span=168, min_periods=84).mean(), 252)
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of zmom189(189d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_zmom189_189d_jerk_v107_signal(closeadj):
    base = _z(_logmom(closeadj, 189) - _logmom(closeadj, 189).ewm(span=378, min_periods=189).mean(), 504)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of zmom378(378d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_zmom378_378d_jerk_v108_signal(closeadj):
    base = _z(_logmom(closeadj, 378) - _logmom(closeadj, 378).ewm(span=756, min_periods=378).mean(), 504)
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rkmom42(42d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_rkmom42_42d_jerk_v109_signal(closeadj):
    base = (_logmom(closeadj, 42).rolling(252,min_periods=126).rank(pct=True)-0.5)
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rkmom63(63d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_rkmom63_63d_jerk_v110_signal(closeadj):
    base = (_logmom(closeadj, 63).rolling(252,min_periods=126).rank(pct=True)-0.5)
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rkmom189(189d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_rkmom189_189d_jerk_v111_signal(closeadj):
    base = (_logmom(closeadj, 189).rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of rkmom378(378d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_rkmom378_378d_jerk_v112_signal(closeadj):
    base = (_logmom(closeadj, 378).rolling(756,min_periods=378).rank(pct=True)-0.5)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm21v126(126d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_trm21v126_126d_jerk_v113_signal(closeadj):
    base = (_logmom(closeadj, 21) - _logmom(closeadj, 126))
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm42v252(252d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_trm42v252_252d_jerk_v114_signal(closeadj):
    base = (_logmom(closeadj, 42) - _logmom(closeadj, 252))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm63v189(189d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_trm63v189_189d_jerk_v115_signal(closeadj):
    base = (_logmom(closeadj, 63) - _logmom(closeadj, 189))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm84v252(252d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_trm84v252_252d_jerk_v116_signal(closeadj):
    base = (_logmom(closeadj, 84) - _logmom(closeadj, 252))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm126v378(378d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_trm126v378_378d_jerk_v117_signal(closeadj):
    base = (_logmom(closeadj, 126) - _logmom(closeadj, 378))
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm189v504(504d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_trm189v504_504d_jerk_v118_signal(closeadj):
    base = (_logmom(closeadj, 189) - _logmom(closeadj, 504))
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm21v504(504d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_trm21v504_504d_jerk_v119_signal(closeadj):
    base = (_logmom(closeadj, 21) - _logmom(closeadj, 504))
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of trm42v504(504d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_trm42v504_504d_jerk_v120_signal(closeadj):
    base = (_logmom(closeadj, 42) - _logmom(closeadj, 504))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ts84(84d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_ts84_84d_jerk_v121_signal(closeadj):
    base = _z(_tstat(closeadj, 84), 252)
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ts105(105d) k=21 v1
def f02cm_f02_commodity_momentum_rotation_ts105_105d_jerk_v122_signal(closeadj):
    base = _z(_tstat(closeadj, 105), 252)
    result = _jerk_signrank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ts168(168d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_ts168_168d_jerk_v123_signal(closeadj):
    base = _z(_tstat(closeadj, 168), 252)
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ts210(210d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_ts210_210d_jerk_v124_signal(closeadj):
    base = _z(_tstat(closeadj, 210), 504)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ts315(315d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_ts315_315d_jerk_v125_signal(closeadj):
    base = _z(_tstat(closeadj, 315), 504)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ef84(84d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_ef84_84d_jerk_v126_signal(closeadj):
    base = _efficiency(closeadj, 84).abs()
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ef105(105d) k=21 v2
def f02cm_f02_commodity_momentum_rotation_ef105_105d_jerk_v127_signal(closeadj):
    base = _efficiency(closeadj, 105).abs()
    result = _jerk_olsz(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ef168(168d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_ef168_168d_jerk_v128_signal(closeadj):
    base = _efficiency(closeadj, 168).abs()
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ef315(315d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_ef315_315d_jerk_v129_signal(closeadj):
    base = _efficiency(closeadj, 315).abs()
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of ef378(378d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_ef378_378d_jerk_v130_signal(closeadj):
    base = _efficiency(closeadj, 378).abs()
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mad42(42d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_mad42_42d_jerk_v131_signal(closeadj):
    base = np.log(closeadj.rolling(10,min_periods=5).mean().replace(0,np.nan)/closeadj.rolling(42,min_periods=21).mean().replace(0,np.nan))
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mad84(84d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_mad84_84d_jerk_v132_signal(closeadj):
    base = np.log(closeadj.rolling(21,min_periods=10).mean().replace(0,np.nan)/closeadj.rolling(84,min_periods=42).mean().replace(0,np.nan))
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mad168(168d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_mad168_168d_jerk_v133_signal(closeadj):
    base = np.log(closeadj.rolling(42,min_periods=21).mean().replace(0,np.nan)/closeadj.rolling(168,min_periods=84).mean().replace(0,np.nan))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mad378(378d) k=63 v4
def f02cm_f02_commodity_momentum_rotation_mad378_378d_jerk_v134_signal(closeadj):
    base = np.log(closeadj.rolling(94,min_periods=47).mean().replace(0,np.nan)/closeadj.rolling(378,min_periods=189).mean().replace(0,np.nan))
    result = _jerk_volrank(base, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of mad504(504d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_mad504_504d_jerk_v135_signal(closeadj):
    base = np.log(closeadj.rolling(126,min_periods=63).mean().replace(0,np.nan)/closeadj.rolling(504,min_periods=252).mean().replace(0,np.nan))
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of str42(42d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_str42_42d_jerk_v136_signal(closeadj):
    base = (_logmom(closeadj, 42).abs().rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of str84(84d) k=21 v4
def f02cm_f02_commodity_momentum_rotation_str84_84d_jerk_v137_signal(closeadj):
    base = (_logmom(closeadj, 84).abs().rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_volrank(base, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of str189(189d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_str189_189d_jerk_v138_signal(closeadj):
    base = (_logmom(closeadj, 189).abs().rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of str315(315d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_str315_315d_jerk_v139_signal(closeadj):
    base = (_logmom(closeadj, 315).abs().rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of str567(567d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_str567_567d_jerk_v140_signal(closeadj):
    base = (_logmom(closeadj, 567).abs().rolling(504,min_periods=252).rank(pct=True)-0.5)
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sm42(42d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_sm42_42d_jerk_v141_signal(closeadj):
    base = _logmom(closeadj, 42).ewm(span=21, min_periods=10).mean()
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sm84(84d) k=21 v0
def f02cm_f02_commodity_momentum_rotation_sm84_84d_jerk_v142_signal(closeadj):
    base = _logmom(closeadj, 84).ewm(span=42, min_periods=21).mean()
    result = _jerk_rank(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sm189(189d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_sm189_189d_jerk_v143_signal(closeadj):
    base = _logmom(closeadj, 189).ewm(span=94, min_periods=47).mean()
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of sm378(378d) k=63 v0
def f02cm_f02_commodity_momentum_rotation_sm378_378d_jerk_v144_signal(closeadj):
    base = _logmom(closeadj, 378).ewm(span=189, min_periods=94).mean()
    result = _jerk_rank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of srel63(63d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_srel63_63d_jerk_v145_signal(closeadj):
    base = (_logmom(closeadj, 63)/_logmom(closeadj, 63).rolling(504,min_periods=252).mean().abs().replace(0,np.nan))
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of srel189(189d) k=63 v3
def f02cm_f02_commodity_momentum_rotation_srel189_189d_jerk_v146_signal(closeadj):
    base = (_logmom(closeadj, 189)/_logmom(closeadj, 189).rolling(504,min_periods=252).mean().abs().replace(0,np.nan))
    result = _jerk_bandpass(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of srel378(378d) k=63 v1
def f02cm_f02_commodity_momentum_rotation_srel378_378d_jerk_v147_signal(closeadj):
    base = (_logmom(closeadj, 378)/_logmom(closeadj, 378).rolling(504,min_periods=252).mean().abs().replace(0,np.nan))
    result = _jerk_signrank(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of dadj105(105d) k=21 v3
def f02cm_f02_commodity_momentum_rotation_dadj105_105d_jerk_v148_signal(closeadj):
    base = _z((_logmom(closeadj, 105)/((closeadj.pct_change().where(closeadj.pct_change()<0,0.0)).rolling(105,min_periods=52).std()*np.sqrt(105.0)).replace(0,np.nan)), 504)
    result = _jerk_bandpass(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of dadj168(168d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_dadj168_168d_jerk_v149_signal(closeadj):
    base = _z((_logmom(closeadj, 168)/((closeadj.pct_change().where(closeadj.pct_change()<0,0.0)).rolling(168,min_periods=84).std()*np.sqrt(168.0)).replace(0,np.nan)), 504)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of dadj378(378d) k=63 v2
def f02cm_f02_commodity_momentum_rotation_dadj378_378d_jerk_v150_signal(closeadj):
    base = _z((_logmom(closeadj, 378)/((closeadj.pct_change().where(closeadj.pct_change()<0,0.0)).rolling(378,min_periods=189).std()*np.sqrt(378.0)).replace(0,np.nan)), 504)
    result = _jerk_olsz(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f02cm_f02_commodity_momentum_rotation_roc21_21d_jerk_v001_signal,
    f02cm_f02_commodity_momentum_rotation_roc42_42d_jerk_v002_signal,
    f02cm_f02_commodity_momentum_rotation_roc63_63d_jerk_v003_signal,
    f02cm_f02_commodity_momentum_rotation_roc126_126d_jerk_v004_signal,
    f02cm_f02_commodity_momentum_rotation_roc189_189d_jerk_v005_signal,
    f02cm_f02_commodity_momentum_rotation_roc252_252d_jerk_v006_signal,
    f02cm_f02_commodity_momentum_rotation_roc378_378d_jerk_v007_signal,
    f02cm_f02_commodity_momentum_rotation_roc504_504d_jerk_v008_signal,
    f02cm_f02_commodity_momentum_rotation_sroc63_63d_jerk_v009_signal,
    f02cm_f02_commodity_momentum_rotation_sroc126_126d_jerk_v010_signal,
    f02cm_f02_commodity_momentum_rotation_sroc252_252d_jerk_v011_signal,
    f02cm_f02_commodity_momentum_rotation_momex126_21_126d_jerk_v012_signal,
    f02cm_f02_commodity_momentum_rotation_momex189_21_189d_jerk_v013_signal,
    f02cm_f02_commodity_momentum_rotation_momex252_21_252d_jerk_v014_signal,
    f02cm_f02_commodity_momentum_rotation_momex378_21_378d_jerk_v015_signal,
    f02cm_f02_commodity_momentum_rotation_momex504_21_504d_jerk_v016_signal,
    f02cm_f02_commodity_momentum_rotation_momex252_63_252d_jerk_v017_signal,
    f02cm_f02_commodity_momentum_rotation_tstat42_42d_jerk_v018_signal,
    f02cm_f02_commodity_momentum_rotation_tstat63_63d_jerk_v019_signal,
    f02cm_f02_commodity_momentum_rotation_tstat126_126d_jerk_v020_signal,
    f02cm_f02_commodity_momentum_rotation_tstat189_189d_jerk_v021_signal,
    f02cm_f02_commodity_momentum_rotation_tstat252_252d_jerk_v022_signal,
    f02cm_f02_commodity_momentum_rotation_eff42_42d_jerk_v023_signal,
    f02cm_f02_commodity_momentum_rotation_eff63_63d_jerk_v024_signal,
    f02cm_f02_commodity_momentum_rotation_eff126_126d_jerk_v025_signal,
    f02cm_f02_commodity_momentum_rotation_eff189_189d_jerk_v026_signal,
    f02cm_f02_commodity_momentum_rotation_eff252_252d_jerk_v027_signal,
    f02cm_f02_commodity_momentum_rotation_spr21v63_63d_jerk_v028_signal,
    f02cm_f02_commodity_momentum_rotation_spr21v252_252d_jerk_v029_signal,
    f02cm_f02_commodity_momentum_rotation_spr42v126_126d_jerk_v030_signal,
    f02cm_f02_commodity_momentum_rotation_spr63v126_126d_jerk_v031_signal,
    f02cm_f02_commodity_momentum_rotation_spr63v252_252d_jerk_v032_signal,
    f02cm_f02_commodity_momentum_rotation_spr126v252_252d_jerk_v033_signal,
    f02cm_f02_commodity_momentum_rotation_spr126v504_504d_jerk_v034_signal,
    f02cm_f02_commodity_momentum_rotation_spr252v504_504d_jerk_v035_signal,
    f02cm_f02_commodity_momentum_rotation_momz63_63d_jerk_v036_signal,
    f02cm_f02_commodity_momentum_rotation_momz126_126d_jerk_v037_signal,
    f02cm_f02_commodity_momentum_rotation_momz252_252d_jerk_v038_signal,
    f02cm_f02_commodity_momentum_rotation_momz504_504d_jerk_v039_signal,
    f02cm_f02_commodity_momentum_rotation_momrank126_126d_jerk_v040_signal,
    f02cm_f02_commodity_momentum_rotation_momrank252_252d_jerk_v041_signal,
    f02cm_f02_commodity_momentum_rotation_momrank441_441d_jerk_v042_signal,
    f02cm_f02_commodity_momentum_rotation_strength63_63d_jerk_v043_signal,
    f02cm_f02_commodity_momentum_rotation_strength126_126d_jerk_v044_signal,
    f02cm_f02_commodity_momentum_rotation_strength252_252d_jerk_v045_signal,
    f02cm_f02_commodity_momentum_rotation_consist63_63d_jerk_v046_signal,
    f02cm_f02_commodity_momentum_rotation_consist126_126d_jerk_v047_signal,
    f02cm_f02_commodity_momentum_rotation_consist252_252d_jerk_v048_signal,
    f02cm_f02_commodity_momentum_rotation_madist63_63d_jerk_v049_signal,
    f02cm_f02_commodity_momentum_rotation_madist126_126d_jerk_v050_signal,
    f02cm_f02_commodity_momentum_rotation_madist252_252d_jerk_v051_signal,
    f02cm_f02_commodity_momentum_rotation_emadist42_42d_jerk_v052_signal,
    f02cm_f02_commodity_momentum_rotation_emadist126_126d_jerk_v053_signal,
    f02cm_f02_commodity_momentum_rotation_emadist252_252d_jerk_v054_signal,
    f02cm_f02_commodity_momentum_rotation_momrng126_126d_jerk_v055_signal,
    f02cm_f02_commodity_momentum_rotation_momrng252_252d_jerk_v056_signal,
    f02cm_f02_commodity_momentum_rotation_downadj126_126d_jerk_v057_signal,
    f02cm_f02_commodity_momentum_rotation_downadj252_252d_jerk_v058_signal,
    f02cm_f02_commodity_momentum_rotation_tanh126_126d_jerk_v059_signal,
    f02cm_f02_commodity_momentum_rotation_tanh252_252d_jerk_v060_signal,
    f02cm_f02_commodity_momentum_rotation_tanh504_504d_jerk_v061_signal,
    f02cm_f02_commodity_momentum_rotation_signmag126_126d_jerk_v062_signal,
    f02cm_f02_commodity_momentum_rotation_signmag252_252d_jerk_v063_signal,
    f02cm_f02_commodity_momentum_rotation_smooth63_63d_jerk_v064_signal,
    f02cm_f02_commodity_momentum_rotation_smooth126_126d_jerk_v065_signal,
    f02cm_f02_commodity_momentum_rotation_smooth252_252d_jerk_v066_signal,
    f02cm_f02_commodity_momentum_rotation_blend_252d_jerk_v067_signal,
    f02cm_f02_commodity_momentum_rotation_dvmom63_63d_jerk_v068_signal,
    f02cm_f02_commodity_momentum_rotation_dvmom126_126d_jerk_v069_signal,
    f02cm_f02_commodity_momentum_rotation_emagap63v252_252d_jerk_v070_signal,
    f02cm_f02_commodity_momentum_rotation_emagap21v63_63d_jerk_v071_signal,
    f02cm_f02_commodity_momentum_rotation_selfrel126_126d_jerk_v072_signal,
    f02cm_f02_commodity_momentum_rotation_selfrel252_252d_jerk_v073_signal,
    f02cm_f02_commodity_momentum_rotation_conv63_126d_jerk_v074_signal,
    f02cm_f02_commodity_momentum_rotation_conv252_252d_jerk_v075_signal,
    f02cm_f02_commodity_momentum_rotation_volofmom_252d_jerk_v076_signal,
    f02cm_f02_commodity_momentum_rotation_stab252_252d_jerk_v077_signal,
    f02cm_f02_commodity_momentum_rotation_stab504_504d_jerk_v078_signal,
    f02cm_f02_commodity_momentum_rotation_cycdev252_252d_jerk_v079_signal,
    f02cm_f02_commodity_momentum_rotation_exhaust21_21d_jerk_v080_signal,
    f02cm_f02_commodity_momentum_rotation_exhaust63_63d_jerk_v081_signal,
    f02cm_f02_commodity_momentum_rotation_glasym63_63d_jerk_v082_signal,
    f02cm_f02_commodity_momentum_rotation_skew126_126d_jerk_v083_signal,
    f02cm_f02_commodity_momentum_rotation_kurt126_126d_jerk_v084_signal,
    f02cm_f02_commodity_momentum_rotation_quality252_252d_jerk_v085_signal,
    f02cm_f02_commodity_momentum_rotation_quality126_126d_jerk_v086_signal,
    f02cm_f02_commodity_momentum_rotation_xmean_252d_jerk_v087_signal,
    f02cm_f02_commodity_momentum_rotation_xdisp_252d_jerk_v088_signal,
    f02cm_f02_commodity_momentum_rotation_tilt2412_504d_jerk_v089_signal,
    f02cm_f02_commodity_momentum_rotation_tilt129_252d_jerk_v090_signal,
    f02cm_f02_commodity_momentum_rotation_regimescaled_252d_jerk_v091_signal,
    f02cm_f02_commodity_momentum_rotation_mom441z_441d_jerk_v092_signal,
    f02cm_f02_commodity_momentum_rotation_persist21_252d_jerk_v093_signal,
    f02cm_f02_commodity_momentum_rotation_vmdiv63_126d_jerk_v094_signal,
    f02cm_f02_commodity_momentum_rotation_logmom84_84d_jerk_v095_signal,
    f02cm_f02_commodity_momentum_rotation_logmom105_105d_jerk_v096_signal,
    f02cm_f02_commodity_momentum_rotation_logmom147_147d_jerk_v097_signal,
    f02cm_f02_commodity_momentum_rotation_logmom168_168d_jerk_v098_signal,
    f02cm_f02_commodity_momentum_rotation_logmom210_210d_jerk_v099_signal,
    f02cm_f02_commodity_momentum_rotation_logmom231_231d_jerk_v100_signal,
    f02cm_f02_commodity_momentum_rotation_logmom294_294d_jerk_v101_signal,
    f02cm_f02_commodity_momentum_rotation_logmom315_315d_jerk_v102_signal,
    f02cm_f02_commodity_momentum_rotation_logmom441_441d_jerk_v103_signal,
    f02cm_f02_commodity_momentum_rotation_logmom567_567d_jerk_v104_signal,
    f02cm_f02_commodity_momentum_rotation_zmom42_42d_jerk_v105_signal,
    f02cm_f02_commodity_momentum_rotation_zmom84_84d_jerk_v106_signal,
    f02cm_f02_commodity_momentum_rotation_zmom189_189d_jerk_v107_signal,
    f02cm_f02_commodity_momentum_rotation_zmom378_378d_jerk_v108_signal,
    f02cm_f02_commodity_momentum_rotation_rkmom42_42d_jerk_v109_signal,
    f02cm_f02_commodity_momentum_rotation_rkmom63_63d_jerk_v110_signal,
    f02cm_f02_commodity_momentum_rotation_rkmom189_189d_jerk_v111_signal,
    f02cm_f02_commodity_momentum_rotation_rkmom378_378d_jerk_v112_signal,
    f02cm_f02_commodity_momentum_rotation_trm21v126_126d_jerk_v113_signal,
    f02cm_f02_commodity_momentum_rotation_trm42v252_252d_jerk_v114_signal,
    f02cm_f02_commodity_momentum_rotation_trm63v189_189d_jerk_v115_signal,
    f02cm_f02_commodity_momentum_rotation_trm84v252_252d_jerk_v116_signal,
    f02cm_f02_commodity_momentum_rotation_trm126v378_378d_jerk_v117_signal,
    f02cm_f02_commodity_momentum_rotation_trm189v504_504d_jerk_v118_signal,
    f02cm_f02_commodity_momentum_rotation_trm21v504_504d_jerk_v119_signal,
    f02cm_f02_commodity_momentum_rotation_trm42v504_504d_jerk_v120_signal,
    f02cm_f02_commodity_momentum_rotation_ts84_84d_jerk_v121_signal,
    f02cm_f02_commodity_momentum_rotation_ts105_105d_jerk_v122_signal,
    f02cm_f02_commodity_momentum_rotation_ts168_168d_jerk_v123_signal,
    f02cm_f02_commodity_momentum_rotation_ts210_210d_jerk_v124_signal,
    f02cm_f02_commodity_momentum_rotation_ts315_315d_jerk_v125_signal,
    f02cm_f02_commodity_momentum_rotation_ef84_84d_jerk_v126_signal,
    f02cm_f02_commodity_momentum_rotation_ef105_105d_jerk_v127_signal,
    f02cm_f02_commodity_momentum_rotation_ef168_168d_jerk_v128_signal,
    f02cm_f02_commodity_momentum_rotation_ef315_315d_jerk_v129_signal,
    f02cm_f02_commodity_momentum_rotation_ef378_378d_jerk_v130_signal,
    f02cm_f02_commodity_momentum_rotation_mad42_42d_jerk_v131_signal,
    f02cm_f02_commodity_momentum_rotation_mad84_84d_jerk_v132_signal,
    f02cm_f02_commodity_momentum_rotation_mad168_168d_jerk_v133_signal,
    f02cm_f02_commodity_momentum_rotation_mad378_378d_jerk_v134_signal,
    f02cm_f02_commodity_momentum_rotation_mad504_504d_jerk_v135_signal,
    f02cm_f02_commodity_momentum_rotation_str42_42d_jerk_v136_signal,
    f02cm_f02_commodity_momentum_rotation_str84_84d_jerk_v137_signal,
    f02cm_f02_commodity_momentum_rotation_str189_189d_jerk_v138_signal,
    f02cm_f02_commodity_momentum_rotation_str315_315d_jerk_v139_signal,
    f02cm_f02_commodity_momentum_rotation_str567_567d_jerk_v140_signal,
    f02cm_f02_commodity_momentum_rotation_sm42_42d_jerk_v141_signal,
    f02cm_f02_commodity_momentum_rotation_sm84_84d_jerk_v142_signal,
    f02cm_f02_commodity_momentum_rotation_sm189_189d_jerk_v143_signal,
    f02cm_f02_commodity_momentum_rotation_sm378_378d_jerk_v144_signal,
    f02cm_f02_commodity_momentum_rotation_srel63_63d_jerk_v145_signal,
    f02cm_f02_commodity_momentum_rotation_srel189_189d_jerk_v146_signal,
    f02cm_f02_commodity_momentum_rotation_srel378_378d_jerk_v147_signal,
    f02cm_f02_commodity_momentum_rotation_dadj105_105d_jerk_v148_signal,
    f02cm_f02_commodity_momentum_rotation_dadj168_168d_jerk_v149_signal,
    f02cm_f02_commodity_momentum_rotation_dadj378_378d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_COMMODITY_MOMENTUM_ROTATION_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f02_commodity_momentum_rotation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
