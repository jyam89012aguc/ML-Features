import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (earnings / news gap dynamics) =====
# Per-day gap uses UNADJUSTED open/high/low/close (<=1d event); longer rolling
# stats operate on the per-day gap SERIES.
def _f12gd_gap(open, close):
    return open / close.shift(1).replace(0, np.nan) - 1.0


def _f12gd_loggap(open, close):
    return np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


def _f12gd_intraday(open, close):
    return close / open.replace(0, np.nan) - 1.0


def _f12gd_truerange(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def f12gd_f12_earnings_gap_dynamics_gapmean_3d_jerk_v001_signal(open, close):  # j3
    g = _f12gd_gap(open, close)
    b = g.rolling(5, min_periods=3).mean()
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmean_8d_jerk_v002_signal(open, close):  # j8
    g = _f12gd_gap(open, close)
    b = g.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmean_10d_jerk_v003_signal(open, close):  # j10
    graw = _f12gd_gap(open, close)
    lo = graw.rolling(63, min_periods=21).quantile(0.10)
    hi = graw.rolling(63, min_periods=21).quantile(0.90)
    g = graw.where((graw >= lo) & (graw <= hi))
    b = g.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_loggapema_8d_jerk_v004_signal(open, close):  # j8
    g = _f12gd_loggap(open, close)
    b = g.ewm(span=21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgap_5d_jerk_v005_signal(open, close):  # j5
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgap_15d_jerk_v006_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapsurprise_5d_jerk_v007_signal(open, close):  # j5
    g = _f12gd_gap(open, close)
    var = (g ** 2).rolling(63, min_periods=21).mean()
    b = np.sign(g) * (g ** 2) / var.replace(0, np.nan)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapz_15d_jerk_v008_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    m = g.rolling(63, min_periods=21).mean()
    sd = g.rolling(63, min_periods=21).std()
    b = (g - m) / sd.replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvov_21d_jerk_v009_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    s21 = g.rolling(21, min_periods=10).std()
    s126 = g.rolling(126, min_periods=63).std()
    b = s21 / s126.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgapz_15d_jerk_v010_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    b = (g - g.rolling(63, min_periods=21).mean()) / g.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_maxgapz_5d_jerk_v011_signal(open, close):  # j5
    g = _f12gd_gap(open, close)
    z = (g - g.rolling(126, min_periods=63).mean()) / g.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = z.abs().rolling(21, min_periods=10).max()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaprank_63d_jerk_v012_signal(open, close):  # j63
    g = _f12gd_gap(open, close)
    sm = g.rolling(21, min_periods=10).mean()
    b = sm.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapfreq_10d_jerk_v013_signal(open, close):  # j10
    g = (_f12gd_gap(open, close)).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 1.5 * sd).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapfreq_30d_jerk_v014_signal(open, close):  # j30
    g = (_f12gd_gap(open, close)).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 2.0 * sd).clip(lower=0)
    b = exc.rolling(126, min_periods=63).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdirbias_10d_jerk_v015_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    s = np.sign(g)
    chg = (s != s.shift(1)).cumsum()
    rl = (s.groupby(chg).cumcount() + 1) * s
    b = rl.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_upgapcnt_8d_jerk_v016_signal(open, close):  # j8
    g = _f12gd_gap(open, close)
    w = g.clip(lower=0)
    b = w.rolling(21, min_periods=10).sum()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_dngapcnt_5d_jerk_v017_signal(open, close):  # j5
    g = _f12gd_gap(open, close)
    w = (-g).clip(lower=0)
    b = w.rolling(21, min_periods=10).sum()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_dayssincegap_15d_jerk_v018_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    sd = g.rolling(126, min_periods=42).std()
    big = (g > 2.5 * sd).astype(float)
    grp = big.cumsum()
    dsl = big.groupby(grp).cumcount().astype(float).where(grp > 0)
    b = dsl * g.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapfill_5d_jerk_v019_signal(open, low, high, close):  # j5
    pc = close.shift(1)
    g = open - pc
    up = (open - low) / g.replace(0, np.nan)
    dn = (high - open) / (-g).replace(0, np.nan)
    f = up.where(g > 0, dn).clip(-2, 2)
    b = f.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fullfill_15d_jerk_v020_signal(open, low, high, close):  # j15
    pc = close.shift(1)
    g = open - pc
    filled = ((g > 0) & (low <= pc)) | ((g < 0) & (high >= pc))
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01)
    num = (filled & ev).astype(float)
    den = ev.astype(float)
    b = num.rolling(63, min_periods=21).sum() / den.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaphold_5d_jerk_v021_signal(open, close):  # j5
    g = _f12gd_gap(open, close)
    cg = close / close.shift(1).replace(0, np.nan) - 1.0
    hold = cg / g.replace(0, np.nan)
    b = hold.clip(-3, 3).rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillasym_30d_jerk_v022_signal(open, low, high, close):  # j30
    pc = close.shift(1)
    g = open - pc
    upf = ((open - low) / g.replace(0, np.nan)).where(g > 0)
    dnf = ((high - open) / (-g).replace(0, np.nan)).where(g < 0)
    b = upf.rolling(126, min_periods=42).mean() - dnf.rolling(126, min_periods=42).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnret_5d_jerk_v023_signal(open, close):  # j5
    ov = _f12gd_gap(open, close)
    b = ov.rolling(5, min_periods=3).mean() - ov.ewm(span=21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_intraret_8d_jerk_v024_signal(open, close):  # j8
    intr = _f12gd_intraday(open, close)
    b = intr.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnminusintra_10d_jerk_v025_signal(open, close):  # j10
    ov = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    b = (ov - intr).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnshare_15d_jerk_v026_signal(open, close):  # j15
    ov = (_f12gd_gap(open, close))
    intr = (_f12gd_intraday(open, close))
    num = ov.abs().rolling(63, min_periods=21).sum()
    den = (ov.abs() + intr.abs()).rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan) - 0.5
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovncorr_10d_jerk_v027_signal(open, close):  # j10
    ov = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    b = ov.rolling(63, min_periods=21).corr(intr)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnvol_15d_jerk_v028_signal(open, close):  # j15
    ov = _f12gd_gap(open, close)
    b = ov.rolling(63, min_periods=21).std()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvol_5d_jerk_v029_signal(open, close, volume):  # j5
    g = _f12gd_gap(open, close)
    vs = volume / volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
    b = (g * vs).rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgapvol_15d_jerk_v030_signal(open, close, volume):  # j15
    g = (_f12gd_gap(open, close)).abs()
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (g * vs).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolfreq_10d_jerk_v031_signal(open, close, volume):  # j10
    g = (_f12gd_gap(open, close)).abs()
    sd = g.rolling(126, min_periods=42).std()
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    exc = (g - 1.5 * sd).clip(lower=0) * (vs - 1.0).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_volwgap_15d_jerk_v032_signal(open, close, volume):  # j15
    g = _f12gd_gap(open, close)
    num = (g * volume).rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaptr_5d_jerk_v033_signal(open, high, low, close):  # j5
    pc = close.shift(1)
    tr = _f12gd_truerange(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    gr = (open - pc) / atr.replace(0, np.nan)
    b = gr.rolling(21, min_periods=10).std()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgaptr_15d_jerk_v034_signal(open, high, low, close):  # j15
    pc = close.shift(1)
    tr = _f12gd_truerange(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open - pc).abs()
    b = (g / atr.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapstdvol_10d_jerk_v035_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    vol = g.rolling(63, min_periods=21).std()
    sg = (g / vol.replace(0, np.nan)).abs()
    b = sg.rolling(63, min_periods=21).quantile(0.90)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdisp_8d_jerk_v036_signal(open, close):  # j8
    g = _f12gd_gap(open, close)
    b = g.rolling(21, min_periods=10).std()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdisp_21d_jerk_v037_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    b = g.rolling(126, min_periods=63).std()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapfattail_15d_jerk_v038_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(63, min_periods=21).max() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapac_10d_jerk_v039_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    b = g.rolling(63, min_periods=21).corr(g.shift(1))
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapcluster_30d_jerk_v040_signal(open, close):  # j30
    g = (_f12gd_gap(open, close)).abs()
    s = g.rolling(21, min_periods=10).std()
    b = s / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapskew_21d_jerk_v041_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    b = g.rolling(126, min_periods=63).skew()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmagasym_15d_jerk_v042_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    upsd = g.where(g > 0).rolling(63, min_periods=21).std()
    dnsd = (-g).where(g < 0).rolling(63, min_periods=21).std()
    b = upsd - dnsd
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_tailasym_21d_jerk_v043_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    b = g.rolling(126, min_periods=63).max() + g.rolling(126, min_periods=63).min()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_postgapcont_15d_jerk_v044_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    fwd = close.shift(-1) / close.replace(0, np.nan) - 1.0
    cont = (np.sign(g) * fwd)
    b = cont.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapclosestr_5d_jerk_v045_signal(open, high, low, close):  # j5
    pos = (close - low) / (high - low).replace(0, np.nan)
    g = (_f12gd_gap(open, close)).abs()
    w = (g > 0.02).astype(float)
    b = (pos * w).rolling(21, min_periods=10).sum() / w.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapandgo_15d_jerk_v046_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    same = (np.sign(g) == np.sign(intr)).astype(float)
    ev = (g.abs() > 0.015).astype(float)
    b = (same * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_cumovn_10d_jerk_v047_signal(open, close):  # j10
    ov = _f12gd_loggap(open, close)
    b = ov.rolling(63, min_periods=21).sum()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_cumintra_15d_jerk_v048_signal(open, close):  # j15
    intr = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = intr.rolling(63, min_periods=21).sum()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_driftspread_21d_jerk_v049_signal(open, close):  # j21
    ov = _f12gd_loggap(open, close)
    intr = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = ov.rolling(126, min_periods=63).sum() - intr.rolling(126, min_periods=63).sum()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaprelhist_63d_jerk_v050_signal(open, close):  # j63
    g = (_f12gd_gap(open, close)).abs()
    q95 = g.rolling(252, min_periods=63).quantile(0.95)
    med = g.rolling(252, min_periods=63).median()
    b = q95 / med.replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmom_10d_jerk_v051_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    b = g.rolling(5, min_periods=3).mean() - g.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillfail_15d_jerk_v052_signal(open, low, high, close):  # j15
    pc = close.shift(1)
    g = open - pc
    stuck = (((g > 0) & (low > pc)) | ((g < 0) & (high < pc))).astype(float)
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01).astype(float)
    b = stuck.rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnsharpe_10d_jerk_v053_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    upsd = g.clip(lower=0).rolling(63, min_periods=21).std()
    dnsd = g.clip(upper=0).rolling(63, min_periods=21).std()
    b = upsd / dnsd.replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_intrasharpe_15d_jerk_v054_signal(open, close):  # j15
    intr = _f12gd_intraday(open, close)
    dn = intr.clip(upper=0).rolling(63, min_periods=21).std()
    tot = intr.rolling(63, min_periods=21).std()
    b = dn / tot.replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaprangeexp_5d_jerk_v055_signal(open, high, low, close):  # j5
    pc = close.shift(1)
    tr = _f12gd_truerange(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    exp = (tr / atr.replace(0, np.nan)) * (g > 0.02).astype(float)
    b = exp.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaptrend_8d_jerk_v056_signal(open, close):  # j8
    g = _f12gd_gap(open, close)
    b = g.ewm(span=10, min_periods=5).mean() - g.ewm(span=42, min_periods=21).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_upgapprop_21d_jerk_v057_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    ev = (g.abs() > 0.02)
    up = (g > 0.02).astype(float)
    b = up.rolling(126, min_periods=42).sum() / ev.astype(float).rolling(126, min_periods=42).sum().replace(0, np.nan) - 0.5
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapentropy_15d_jerk_v058_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    b = 1.0 - g.rolling(63, min_periods=21).mean().abs() / g.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_maxupgap_10d_jerk_v059_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    b = g.rolling(63, min_periods=21).max()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_maxdngap_15d_jerk_v060_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    b = g.rolling(63, min_periods=21).min()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapspan_10d_jerk_v061_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    b = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapfade_30d_jerk_v062_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    b = -g.rolling(126, min_periods=63).corr(intr)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovncontribz_42d_jerk_v063_signal(open, close):  # j42
    ov = _f12gd_gap(open, close)
    c = ov.rolling(21, min_periods=10).sum()
    b = (c - c.rolling(252, min_periods=63).mean()) / c.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolshare_15d_jerk_v064_signal(open, close, volume):  # j15
    g = (_f12gd_gap(open, close)).abs()
    ev = (g > 0.02).astype(float)
    evol = (ev * volume).rolling(63, min_periods=21).sum()
    b = evol / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillspeed_5d_jerk_v065_signal(open, high, low, close):  # j5
    pc = close.shift(1)
    g = open - pc
    retr_up = (open - low) / (high - low).replace(0, np.nan)
    retr_dn = (high - open) / (high - low).replace(0, np.nan)
    r = retr_up.where(g > 0, retr_dn)
    b = r.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgapaccel_15d_jerk_v066_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(21, min_periods=10).mean() - g.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapstreak_5d_jerk_v067_signal(open, close):  # j5
    g = _f12gd_gap(open, close)
    s = np.sign(g)
    chg = (s != s.shift(1)).cumsum()
    rl = s.groupby(chg).cumcount() + 1
    b = (rl * s).astype(float)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnsemidev_15d_jerk_v068_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    neg = g.clip(upper=0)
    b = neg.rolling(63, min_periods=21).std()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnsemidevup_10d_jerk_v069_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    pos = g.clip(lower=0)
    b = pos.rolling(63, min_periods=21).std()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdecay_8d_jerk_v070_signal(open, close):  # j8
    g = (_f12gd_gap(open, close)).abs()
    sm = g.rolling(5, min_periods=3).mean()
    b = sm - sm.shift(10)
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnvolshare_10d_jerk_v071_signal(open, close):  # j10
    ov = _f12gd_gap(open, close)
    tot = close / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(63, min_periods=21).std() / tot.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapevententry_30d_jerk_v072_signal(open, close):  # j30
    g = (_f12gd_gap(open, close)).abs()
    sd = g.rolling(126, min_periods=42).std()
    ev = (g > 1.8 * sd).astype(float)
    entry = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    b = entry.rolling(126, min_periods=42).sum() + 20.0 * g.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmedian_21d_jerk_v073_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    b = g.rolling(126, min_periods=63).median()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapiqr_30d_jerk_v074_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    b = g.rolling(126, min_periods=63).quantile(0.75) - g.rolling(126, min_periods=63).quantile(0.25)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolbeta_21d_jerk_v075_signal(open, close, volume):  # j21
    g = _f12gd_gap(open, close)
    vs = volume / volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
    cov = g.rolling(126, min_periods=63).cov(vs)
    var = vs.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_breakawayup_15d_jerk_v076_signal(open, high, close):  # j15
    ph = high.shift(1)
    bo = (open - ph).clip(lower=0) / close.shift(1).replace(0, np.nan)
    b = bo.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_breakawaydn_10d_jerk_v077_signal(open, low, close):  # j10
    pl = low.shift(1)
    bo = (pl - open).clip(lower=0) / close.shift(1).replace(0, np.nan)
    b = bo.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_clearairgap_8d_jerk_v078_signal(open, high, low, close):  # j8
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    g = (up + dn) / close.shift(1).replace(0, np.nan)
    b = g.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_breakawaybias_21d_jerk_v079_signal(open, high, low, close):  # j21
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    b = ((up - dn) / close.shift(1).replace(0, np.nan)).rolling(126, min_periods=42).mean()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvsrange_8d_jerk_v080_signal(open, high, low, close):  # j8
    pr = (high.shift(1) - low.shift(1))
    g = (open - close.shift(1)).abs()
    b = (g / pr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_openinrange_5d_jerk_v081_signal(open, high, low):  # j5
    ph = high.shift(1)
    pl = low.shift(1)
    pos = (open - pl) / (ph - pl).replace(0, np.nan)
    b = pos.rolling(21, min_periods=10).mean() - 0.5
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_openrangedisp_15d_jerk_v082_signal(open, high, low):  # j15
    ph = high.shift(1)
    pl = low.shift(1)
    pos = (open - pl) / (ph - pl).replace(0, np.nan)
    b = pos.rolling(63, min_periods=21).std()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdayexp_10d_jerk_v083_signal(open, high, low, close):  # j10
    pc = close.shift(1)
    tr = _f12gd_truerange(high, low, close)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    ratio = tr / tr.shift(1).replace(0, np.nan)
    ev = (g > 0.02).astype(float)
    b = (ratio * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnintravolratio_15d_jerk_v084_signal(open, close):  # j15
    ov = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    b = ov.rolling(63, min_periods=21).std() / intr.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgapewm_10d_jerk_v085_signal(open, close):  # j10
    g = (_f12gd_gap(open, close)).abs()
    b = g.ewm(span=42, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnewm_8d_jerk_v086_signal(open, close):  # j8
    ov = _f12gd_gap(open, close)
    b = (ov ** 2).ewm(span=21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_intraewm_5d_jerk_v087_signal(open, close):  # j5
    intr = _f12gd_intraday(open, close)
    b = intr.ewm(span=21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_volgapsent_15d_jerk_v088_signal(open, close, volume):  # j15
    g = _f12gd_gap(open, close)
    vw = volume * np.sign(g)
    b = vw.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapperdvol_10d_jerk_v089_signal(open, close, volume):  # j10
    g = (_f12gd_gap(open, close)).abs()
    dv = volume / volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    b = (g / dv.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolcorr_30d_jerk_v090_signal(open, close, volume):  # j30
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(126, min_periods=63).corr(volume)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_volgapupdn_21d_jerk_v091_signal(open, close, volume):  # j21
    g = _f12gd_gap(open, close)
    upv = (volume * (g > 0.02).astype(float)).rolling(126, min_periods=42).sum()
    dnv = (volume * (g < -0.02).astype(float)).rolling(126, min_periods=42).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapreverse_30d_jerk_v092_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    fwd = close.shift(-1) / open.shift(-1).replace(0, np.nan) - 1.0
    b = (-np.sign(g) * fwd).rolling(126, min_periods=63).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapintramom_10d_jerk_v093_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    ev = (g.abs() > 0.02).astype(float)
    b = (intr * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapecho_15d_jerk_v094_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    prod = (g * g.shift(1)).rolling(63, min_periods=21).mean()
    var = (g ** 2).rolling(63, min_periods=21).mean()
    b = prod / var.replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapp90_21d_jerk_v095_signal(open, close):  # j21
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(126, min_periods=63).quantile(0.90)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapexceed_30d_jerk_v096_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    sd = g.rolling(126, min_periods=63).std()
    ex = (g.abs() - 2.0 * sd).clip(lower=0)
    b = ex.rolling(126, min_periods=63).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaptailmean_42d_jerk_v097_signal(open, close):  # j42
    g = (_f12gd_gap(open, close)).abs()
    thr = g.rolling(252, min_periods=63).quantile(0.90)
    exc = (g - thr).clip(lower=0)
    b = exc.rolling(252, min_periods=63).mean()
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_c2o_8d_jerk_v098_signal(open, close):  # j8
    c2o = _f12gd_loggap(open, close)
    tot = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    cov = c2o.rolling(21, min_periods=10).sum()
    ctot = tot.rolling(21, min_periods=10).sum()
    b = cov / ctot.where(ctot.abs() > 1e-9)
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_o2c_5d_jerk_v099_signal(open, close):  # j5
    o2c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = o2c.rolling(21, min_periods=10).sum()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnintraretratio_30d_jerk_v100_signal(open, close):  # j30
    ov = _f12gd_loggap(open, close).rolling(126, min_periods=63).sum()
    ic = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)).rolling(126, min_periods=63).sum()
    b = ov / (ov.abs() + ic.abs()).replace(0, np.nan)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapretdepth_5d_jerk_v101_signal(open, low, high, close):  # j5
    pc = close.shift(1)
    g = open - pc
    depth_up = (open - low) / g.replace(0, np.nan)
    depth_dn = (high - open) / (-g).replace(0, np.nan)
    d = depth_up.where(g > 0, depth_dn).clip(-1, 3)
    b = d.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_partialfill_15d_jerk_v102_signal(open, low, high, close):  # j15
    pc = close.shift(1)
    g = open - pc
    frac_up = ((open - low) / g.replace(0, np.nan)).where(g > 0)
    frac_dn = ((high - open) / (-g).replace(0, np.nan)).where(g < 0)
    f = pd.concat([frac_up, frac_dn], axis=1).sum(axis=1, min_count=1).clip(0, 1)
    b = f.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillvshold_21d_jerk_v103_signal(open, low, high, close):  # j21
    pc = close.shift(1)
    g = open - pc
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01)
    filled = (((g > 0) & (low <= pc)) | ((g < 0) & (high >= pc))) & ev
    held = (((g > 0) & (low > pc)) | ((g < 0) & (high < pc))) & ev
    b = (filled.astype(float) - held.astype(float)).rolling(126, min_periods=42).mean()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_sqrtsigngap_8d_jerk_v104_signal(open, close):  # j8
    g = _f12gd_gap(open, close)
    t = np.sign(g) * np.sqrt(g.abs())
    b = t.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_wingapmean_10d_jerk_v105_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    lo = g.rolling(126, min_periods=42).quantile(0.05)
    hi = g.rolling(126, min_periods=42).quantile(0.95)
    gw = g.clip(lower=lo, upper=hi)
    b = g.rolling(63, min_periods=21).mean() - gw.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_logabsgap_15d_jerk_v106_signal(open, close):  # j15
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(63, min_periods=21).std() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gappinessdist_42d_jerk_v107_signal(open, close):  # j42
    g = (_f12gd_gap(open, close)).abs()
    cur = g.rolling(21, min_periods=10).mean()
    nrm = g.rolling(252, min_periods=63).mean()
    b = cur / nrm.replace(0, np.nan) - 1.0
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapregimez_63d_jerk_v108_signal(open, close):  # j63
    g = _f12gd_gap(open, close)
    sv = g.rolling(21, min_periods=10).std()
    b = (sv - sv.rolling(252, min_periods=63).mean()) / sv.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_elevgapfrac_21d_jerk_v109_signal(open, close):  # j21
    g = (_f12gd_gap(open, close)).abs()
    sv = g.rolling(21, min_periods=10).mean()
    med = sv.rolling(126, min_periods=63).median()
    hot = (sv > med).astype(float)
    b = hot.rolling(126, min_periods=63).mean() - 0.5
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvsdayrange_8d_jerk_v110_signal(open, high, low, close):  # j8
    g = (open - close.shift(1)).abs()
    dr = (high - low)
    b = (g / dr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(8) + b.shift(16)) / float(64)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapabsorbed_10d_jerk_v111_signal(open, high, low, close):  # j10
    g = (open - close.shift(1)).abs()
    dr = (high - low)
    ratio = (g / dr.replace(0, np.nan))
    ev = (g / close.shift(1).replace(0, np.nan) > 0.02).astype(float)
    absorbed = (1.0 - ratio).clip(-1, 1)
    b = (absorbed * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnmom_15d_jerk_v112_signal(open, close):  # j15
    ov = _f12gd_gap(open, close)
    b = ov.rolling(5, min_periods=3).sum() - ov.rolling(63, min_periods=21).mean() * 5.0
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_intramom_10d_jerk_v113_signal(open, close):  # j10
    intr = _f12gd_intraday(open, close)
    b = intr.rolling(5, min_periods=3).sum() - intr.rolling(63, min_periods=21).mean() * 5.0
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_upgapcontinue_15d_jerk_v114_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    w = g.clip(lower=0)
    b = (w * intr).rolling(63, min_periods=21).sum() / w.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_dngapcontinue_10d_jerk_v115_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    w = (-g).clip(lower=0)
    b = (w * intr).rolling(63, min_periods=21).sum() / w.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgaprank_30d_jerk_v116_signal(open, close):  # j30
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnrank_42d_jerk_v117_signal(open, close):  # j42
    ov = _f12gd_gap(open, close)
    b = ov.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolrank_63d_jerk_v118_signal(open, close):  # j63
    g = _f12gd_gap(open, close)
    sv = g.rolling(21, min_periods=10).std()
    b = sv.rolling(252, min_periods=63).corr(sv.shift(21))
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapherd_10d_jerk_v119_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    trail = np.sign(g.rolling(5, min_periods=3).mean())
    b = (g * trail).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovncubeskew_30d_jerk_v120_signal(open, close):  # j30
    ov = _f12gd_gap(open, close)
    num = (ov ** 3).rolling(126, min_periods=63).mean()
    den = (ov.rolling(126, min_periods=63).std()) ** 3
    b = num / den.replace(0, np.nan)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdaybull_21d_jerk_v121_signal(open, close):  # j21
    g = (_f12gd_gap(open, close)).abs()
    bull = ((close > open).astype(float) - 0.5) * 2.0
    b = (bull * g).rolling(126, min_periods=42).mean()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapatrratio_15d_jerk_v122_signal(open, high, low, close):  # j15
    pc = close.shift(1)
    tr = _f12gd_truerange(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open - pc).abs()
    b = (g / atr.replace(0, np.nan)).rolling(63, min_periods=21).quantile(0.75)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillhalflife_42d_jerk_v123_signal(open, low, high, close):  # j42
    pc = close.shift(1)
    g = open - pc
    ev = (g.abs() / pc.replace(0, np.nan) > 0.02)
    touched = (((g > 0) & (low <= open - 0.5 * g)) | ((g < 0) & (high >= open - 0.5 * g))) & ev
    b = touched.astype(float).rolling(252, min_periods=63).sum() / ev.astype(float).rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapenergy_15d_jerk_v124_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    e = (g ** 2)
    b = e.rolling(5, min_periods=3).sum() / e.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnqvshare_10d_jerk_v125_signal(open, close):  # j10
    ov = _f12gd_gap(open, close)
    qov = (ov ** 2).rolling(63, min_periods=21).sum()
    b = qov.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapconc_30d_jerk_v126_signal(open, close):  # j30
    g = (_f12gd_gap(open, close)).abs()
    top = g.rolling(126, min_periods=63).apply(lambda a: np.sort(a)[-5:].sum() if len(a) >= 5 else np.nan, raw=True)
    tot = g.rolling(126, min_periods=63).sum()
    b = top / tot.replace(0, np.nan)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnreversal_21d_jerk_v127_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    nextov = open.shift(-1) / close.replace(0, np.nan) - 1.0
    b = (-np.sign(g) * nextov).rolling(126, min_periods=63).mean()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapsignconsist_15d_jerk_v128_signal(open, close):  # j15
    g = _f12gd_gap(open, close)
    m = g.rolling(63, min_periods=21).mean()
    agree = np.sign(g) * np.sign(m) * g.abs()
    b = agree.rolling(63, min_periods=21).sum() / g.abs().rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_intrarecovers_10d_jerk_v129_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    rec = ((g > 0.02) & (close < close.shift(1))) | ((g < -0.02) & (close > close.shift(1)))
    ev = (g.abs() > 0.02)
    b = rec.astype(float).rolling(63, min_periods=21).sum() / ev.astype(float).rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolz_15d_jerk_v130_signal(open, close, volume):  # j15
    g = _f12gd_gap(open, close)
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    x = g * vs
    b = (x - x.rolling(63, min_periods=21).mean()) / x.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolslope_10d_jerk_v131_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    sv = g.rolling(21, min_periods=10).std()
    b = sv - sv.shift(21)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_alphaspreadrank_30d_jerk_v132_signal(open, close):  # j30
    ov = (_f12gd_gap(open, close)).rolling(63, min_periods=21).mean()
    ic = (_f12gd_intraday(open, close)).rolling(63, min_periods=21).mean()
    sp = ov - ic
    b = sp.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapmomalign_10d_jerk_v133_signal(open, close):  # j10
    g = _f12gd_gap(open, close)
    prevmove = close.shift(1) / close.shift(2).replace(0, np.nan) - 1.0
    align = (np.sign(g) == np.sign(prevmove)).astype(float)
    b = align.rolling(63, min_periods=21).mean() - 0.5
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapvolelast_30d_jerk_v134_signal(open, close, volume):  # j30
    g = (_f12gd_gap(open, close)).abs()
    lv = np.log(volume.replace(0, np.nan))
    cov = g.rolling(126, min_periods=63).cov(lv)
    var = lv.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovndownfreq_10d_jerk_v135_signal(open, close):  # j10
    ov = _f12gd_gap(open, close)
    b = (-ov).clip(lower=0).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnupfreq_15d_jerk_v136_signal(open, close):  # j15
    ov = _f12gd_gap(open, close)
    b = ov.clip(lower=0).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gaprevtime_42d_jerk_v137_signal(open, close):  # j42
    pc = close.shift(1)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 2.0 * sd).clip(lower=0)
    b = exc.rolling(252, min_periods=63).sum()
    result = (b - 2.0 * b.shift(42) + b.shift(84)) / float(1764)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_netclearair_30d_jerk_v138_signal(open, high, low, close):  # j30
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    mag = (up + dn) / close.shift(1).replace(0, np.nan)
    b = mag.rolling(126, min_periods=42).std()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdayvolz_10d_jerk_v139_signal(open, close, volume):  # j10
    g = (_f12gd_gap(open, close)).abs()
    vz = (volume - volume.rolling(63, min_periods=21).mean()) / volume.rolling(63, min_periods=21).std().replace(0, np.nan)
    b = (vz * g).rolling(63, min_periods=21).sum() / g.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapenergyratio_63d_jerk_v140_signal(open, close):  # j63
    g = _f12gd_gap(open, close)
    e = (g ** 2)
    b = e.rolling(21, min_periods=10).sum() / e.rolling(252, min_periods=63).sum().replace(0, np.nan) * 12.0
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovntstat_21d_jerk_v141_signal(open, close):  # j21
    ov = _f12gd_gap(open, close)
    m = ov.rolling(126, min_periods=63).mean()
    s = ov.rolling(126, min_periods=63).std()
    b = m / (s / np.sqrt(126)).replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_fillbalance_30d_jerk_v142_signal(open, low, high, close):  # j30
    pc = close.shift(1)
    g = open - pc
    ufill = (((g > 0) & (low <= pc))).astype(float)
    dfill = (((g < 0) & (high >= pc))).astype(float)
    b = (ufill - dfill).rolling(126, min_periods=42).mean()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_absgapac_21d_jerk_v143_signal(open, close):  # j21
    g = (_f12gd_gap(open, close)).abs()
    b = g.rolling(126, min_periods=63).corr(g.shift(1))
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gappassthrough_30d_jerk_v144_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    cm = close / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).corr(cm)
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapsurpriseidx_21d_jerk_v145_signal(open, close):  # j21
    g = (_f12gd_gap(open, close)).abs()
    e = g.ewm(span=10, min_periods=5).mean()
    b = (e - e.rolling(126, min_periods=63).mean()) / e.rolling(126, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_ovnmedian_30d_jerk_v146_signal(open, close):  # j30
    ov = _f12gd_gap(open, close)
    b = ov.rolling(126, min_periods=63).median()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapdominance_10d_jerk_v147_signal(open, close):  # j10
    g = (_f12gd_gap(open, close)).abs()
    intr = (_f12gd_intraday(open, close)).abs()
    b = (g / (g + intr).replace(0, np.nan)).rolling(63, min_periods=21).mean() - 0.5
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapgoupct_30d_jerk_v148_signal(open, close):  # j30
    g = _f12gd_gap(open, close)
    intr = _f12gd_intraday(open, close)
    ev = g.clip(lower=0) * intr.clip(lower=0)
    b = ev.rolling(126, min_periods=42).sum()
    result = (b - 2.0 * b.shift(30) + b.shift(60)) / float(900)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapenergytanh_21d_jerk_v149_signal(open, close):  # j21
    g = _f12gd_gap(open, close)
    e = (g ** 2)
    r = e.rolling(21, min_periods=10).sum() / e.rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = np.tanh(r / 21.0 - 1.0)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gd_f12_earnings_gap_dynamics_gapwick_15d_jerk_v150_signal(open, high, low, close):  # j15
    pc = close.shift(1)
    wick = (high - pd.concat([open, close], axis=1).max(axis=1)) / (high - low).replace(0, np.nan)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    ev = (g > 0.02).astype(float)
    b = (wick * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (b - 2.0 * b.shift(15) + b.shift(30)) / float(225)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f12gd_f12_earnings_gap_dynamics_gapmean_3d_jerk_v001_signal,
    f12gd_f12_earnings_gap_dynamics_gapmean_8d_jerk_v002_signal,
    f12gd_f12_earnings_gap_dynamics_gapmean_10d_jerk_v003_signal,
    f12gd_f12_earnings_gap_dynamics_loggapema_8d_jerk_v004_signal,
    f12gd_f12_earnings_gap_dynamics_absgap_5d_jerk_v005_signal,
    f12gd_f12_earnings_gap_dynamics_absgap_15d_jerk_v006_signal,
    f12gd_f12_earnings_gap_dynamics_gapsurprise_5d_jerk_v007_signal,
    f12gd_f12_earnings_gap_dynamics_gapz_15d_jerk_v008_signal,
    f12gd_f12_earnings_gap_dynamics_gapvov_21d_jerk_v009_signal,
    f12gd_f12_earnings_gap_dynamics_absgapz_15d_jerk_v010_signal,
    f12gd_f12_earnings_gap_dynamics_maxgapz_5d_jerk_v011_signal,
    f12gd_f12_earnings_gap_dynamics_gaprank_63d_jerk_v012_signal,
    f12gd_f12_earnings_gap_dynamics_gapfreq_10d_jerk_v013_signal,
    f12gd_f12_earnings_gap_dynamics_gapfreq_30d_jerk_v014_signal,
    f12gd_f12_earnings_gap_dynamics_gapdirbias_10d_jerk_v015_signal,
    f12gd_f12_earnings_gap_dynamics_upgapcnt_8d_jerk_v016_signal,
    f12gd_f12_earnings_gap_dynamics_dngapcnt_5d_jerk_v017_signal,
    f12gd_f12_earnings_gap_dynamics_dayssincegap_15d_jerk_v018_signal,
    f12gd_f12_earnings_gap_dynamics_gapfill_5d_jerk_v019_signal,
    f12gd_f12_earnings_gap_dynamics_fullfill_15d_jerk_v020_signal,
    f12gd_f12_earnings_gap_dynamics_gaphold_5d_jerk_v021_signal,
    f12gd_f12_earnings_gap_dynamics_fillasym_30d_jerk_v022_signal,
    f12gd_f12_earnings_gap_dynamics_ovnret_5d_jerk_v023_signal,
    f12gd_f12_earnings_gap_dynamics_intraret_8d_jerk_v024_signal,
    f12gd_f12_earnings_gap_dynamics_ovnminusintra_10d_jerk_v025_signal,
    f12gd_f12_earnings_gap_dynamics_ovnshare_15d_jerk_v026_signal,
    f12gd_f12_earnings_gap_dynamics_ovncorr_10d_jerk_v027_signal,
    f12gd_f12_earnings_gap_dynamics_ovnvol_15d_jerk_v028_signal,
    f12gd_f12_earnings_gap_dynamics_gapvol_5d_jerk_v029_signal,
    f12gd_f12_earnings_gap_dynamics_absgapvol_15d_jerk_v030_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolfreq_10d_jerk_v031_signal,
    f12gd_f12_earnings_gap_dynamics_volwgap_15d_jerk_v032_signal,
    f12gd_f12_earnings_gap_dynamics_gaptr_5d_jerk_v033_signal,
    f12gd_f12_earnings_gap_dynamics_absgaptr_15d_jerk_v034_signal,
    f12gd_f12_earnings_gap_dynamics_gapstdvol_10d_jerk_v035_signal,
    f12gd_f12_earnings_gap_dynamics_gapdisp_8d_jerk_v036_signal,
    f12gd_f12_earnings_gap_dynamics_gapdisp_21d_jerk_v037_signal,
    f12gd_f12_earnings_gap_dynamics_gapfattail_15d_jerk_v038_signal,
    f12gd_f12_earnings_gap_dynamics_gapac_10d_jerk_v039_signal,
    f12gd_f12_earnings_gap_dynamics_gapcluster_30d_jerk_v040_signal,
    f12gd_f12_earnings_gap_dynamics_gapskew_21d_jerk_v041_signal,
    f12gd_f12_earnings_gap_dynamics_gapmagasym_15d_jerk_v042_signal,
    f12gd_f12_earnings_gap_dynamics_tailasym_21d_jerk_v043_signal,
    f12gd_f12_earnings_gap_dynamics_postgapcont_15d_jerk_v044_signal,
    f12gd_f12_earnings_gap_dynamics_gapclosestr_5d_jerk_v045_signal,
    f12gd_f12_earnings_gap_dynamics_gapandgo_15d_jerk_v046_signal,
    f12gd_f12_earnings_gap_dynamics_cumovn_10d_jerk_v047_signal,
    f12gd_f12_earnings_gap_dynamics_cumintra_15d_jerk_v048_signal,
    f12gd_f12_earnings_gap_dynamics_driftspread_21d_jerk_v049_signal,
    f12gd_f12_earnings_gap_dynamics_gaprelhist_63d_jerk_v050_signal,
    f12gd_f12_earnings_gap_dynamics_gapmom_10d_jerk_v051_signal,
    f12gd_f12_earnings_gap_dynamics_fillfail_15d_jerk_v052_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsharpe_10d_jerk_v053_signal,
    f12gd_f12_earnings_gap_dynamics_intrasharpe_15d_jerk_v054_signal,
    f12gd_f12_earnings_gap_dynamics_gaprangeexp_5d_jerk_v055_signal,
    f12gd_f12_earnings_gap_dynamics_gaptrend_8d_jerk_v056_signal,
    f12gd_f12_earnings_gap_dynamics_upgapprop_21d_jerk_v057_signal,
    f12gd_f12_earnings_gap_dynamics_gapentropy_15d_jerk_v058_signal,
    f12gd_f12_earnings_gap_dynamics_maxupgap_10d_jerk_v059_signal,
    f12gd_f12_earnings_gap_dynamics_maxdngap_15d_jerk_v060_signal,
    f12gd_f12_earnings_gap_dynamics_gapspan_10d_jerk_v061_signal,
    f12gd_f12_earnings_gap_dynamics_gapfade_30d_jerk_v062_signal,
    f12gd_f12_earnings_gap_dynamics_ovncontribz_42d_jerk_v063_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolshare_15d_jerk_v064_signal,
    f12gd_f12_earnings_gap_dynamics_fillspeed_5d_jerk_v065_signal,
    f12gd_f12_earnings_gap_dynamics_absgapaccel_15d_jerk_v066_signal,
    f12gd_f12_earnings_gap_dynamics_gapstreak_5d_jerk_v067_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsemidev_15d_jerk_v068_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsemidevup_10d_jerk_v069_signal,
    f12gd_f12_earnings_gap_dynamics_gapdecay_8d_jerk_v070_signal,
    f12gd_f12_earnings_gap_dynamics_ovnvolshare_10d_jerk_v071_signal,
    f12gd_f12_earnings_gap_dynamics_gapevententry_30d_jerk_v072_signal,
    f12gd_f12_earnings_gap_dynamics_gapmedian_21d_jerk_v073_signal,
    f12gd_f12_earnings_gap_dynamics_gapiqr_30d_jerk_v074_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolbeta_21d_jerk_v075_signal,
    f12gd_f12_earnings_gap_dynamics_breakawayup_15d_jerk_v076_signal,
    f12gd_f12_earnings_gap_dynamics_breakawaydn_10d_jerk_v077_signal,
    f12gd_f12_earnings_gap_dynamics_clearairgap_8d_jerk_v078_signal,
    f12gd_f12_earnings_gap_dynamics_breakawaybias_21d_jerk_v079_signal,
    f12gd_f12_earnings_gap_dynamics_gapvsrange_8d_jerk_v080_signal,
    f12gd_f12_earnings_gap_dynamics_openinrange_5d_jerk_v081_signal,
    f12gd_f12_earnings_gap_dynamics_openrangedisp_15d_jerk_v082_signal,
    f12gd_f12_earnings_gap_dynamics_gapdayexp_10d_jerk_v083_signal,
    f12gd_f12_earnings_gap_dynamics_ovnintravolratio_15d_jerk_v084_signal,
    f12gd_f12_earnings_gap_dynamics_absgapewm_10d_jerk_v085_signal,
    f12gd_f12_earnings_gap_dynamics_ovnewm_8d_jerk_v086_signal,
    f12gd_f12_earnings_gap_dynamics_intraewm_5d_jerk_v087_signal,
    f12gd_f12_earnings_gap_dynamics_volgapsent_15d_jerk_v088_signal,
    f12gd_f12_earnings_gap_dynamics_gapperdvol_10d_jerk_v089_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolcorr_30d_jerk_v090_signal,
    f12gd_f12_earnings_gap_dynamics_volgapupdn_21d_jerk_v091_signal,
    f12gd_f12_earnings_gap_dynamics_gapreverse_30d_jerk_v092_signal,
    f12gd_f12_earnings_gap_dynamics_gapintramom_10d_jerk_v093_signal,
    f12gd_f12_earnings_gap_dynamics_gapecho_15d_jerk_v094_signal,
    f12gd_f12_earnings_gap_dynamics_gapp90_21d_jerk_v095_signal,
    f12gd_f12_earnings_gap_dynamics_gapexceed_30d_jerk_v096_signal,
    f12gd_f12_earnings_gap_dynamics_gaptailmean_42d_jerk_v097_signal,
    f12gd_f12_earnings_gap_dynamics_c2o_8d_jerk_v098_signal,
    f12gd_f12_earnings_gap_dynamics_o2c_5d_jerk_v099_signal,
    f12gd_f12_earnings_gap_dynamics_ovnintraretratio_30d_jerk_v100_signal,
    f12gd_f12_earnings_gap_dynamics_gapretdepth_5d_jerk_v101_signal,
    f12gd_f12_earnings_gap_dynamics_partialfill_15d_jerk_v102_signal,
    f12gd_f12_earnings_gap_dynamics_fillvshold_21d_jerk_v103_signal,
    f12gd_f12_earnings_gap_dynamics_sqrtsigngap_8d_jerk_v104_signal,
    f12gd_f12_earnings_gap_dynamics_wingapmean_10d_jerk_v105_signal,
    f12gd_f12_earnings_gap_dynamics_logabsgap_15d_jerk_v106_signal,
    f12gd_f12_earnings_gap_dynamics_gappinessdist_42d_jerk_v107_signal,
    f12gd_f12_earnings_gap_dynamics_gapregimez_63d_jerk_v108_signal,
    f12gd_f12_earnings_gap_dynamics_elevgapfrac_21d_jerk_v109_signal,
    f12gd_f12_earnings_gap_dynamics_gapvsdayrange_8d_jerk_v110_signal,
    f12gd_f12_earnings_gap_dynamics_gapabsorbed_10d_jerk_v111_signal,
    f12gd_f12_earnings_gap_dynamics_ovnmom_15d_jerk_v112_signal,
    f12gd_f12_earnings_gap_dynamics_intramom_10d_jerk_v113_signal,
    f12gd_f12_earnings_gap_dynamics_upgapcontinue_15d_jerk_v114_signal,
    f12gd_f12_earnings_gap_dynamics_dngapcontinue_10d_jerk_v115_signal,
    f12gd_f12_earnings_gap_dynamics_absgaprank_30d_jerk_v116_signal,
    f12gd_f12_earnings_gap_dynamics_ovnrank_42d_jerk_v117_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolrank_63d_jerk_v118_signal,
    f12gd_f12_earnings_gap_dynamics_gapherd_10d_jerk_v119_signal,
    f12gd_f12_earnings_gap_dynamics_ovncubeskew_30d_jerk_v120_signal,
    f12gd_f12_earnings_gap_dynamics_gapdaybull_21d_jerk_v121_signal,
    f12gd_f12_earnings_gap_dynamics_gapatrratio_15d_jerk_v122_signal,
    f12gd_f12_earnings_gap_dynamics_fillhalflife_42d_jerk_v123_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergy_15d_jerk_v124_signal,
    f12gd_f12_earnings_gap_dynamics_ovnqvshare_10d_jerk_v125_signal,
    f12gd_f12_earnings_gap_dynamics_gapconc_30d_jerk_v126_signal,
    f12gd_f12_earnings_gap_dynamics_ovnreversal_21d_jerk_v127_signal,
    f12gd_f12_earnings_gap_dynamics_gapsignconsist_15d_jerk_v128_signal,
    f12gd_f12_earnings_gap_dynamics_intrarecovers_10d_jerk_v129_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolz_15d_jerk_v130_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolslope_10d_jerk_v131_signal,
    f12gd_f12_earnings_gap_dynamics_alphaspreadrank_30d_jerk_v132_signal,
    f12gd_f12_earnings_gap_dynamics_gapmomalign_10d_jerk_v133_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolelast_30d_jerk_v134_signal,
    f12gd_f12_earnings_gap_dynamics_ovndownfreq_10d_jerk_v135_signal,
    f12gd_f12_earnings_gap_dynamics_ovnupfreq_15d_jerk_v136_signal,
    f12gd_f12_earnings_gap_dynamics_gaprevtime_42d_jerk_v137_signal,
    f12gd_f12_earnings_gap_dynamics_netclearair_30d_jerk_v138_signal,
    f12gd_f12_earnings_gap_dynamics_gapdayvolz_10d_jerk_v139_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergyratio_63d_jerk_v140_signal,
    f12gd_f12_earnings_gap_dynamics_ovntstat_21d_jerk_v141_signal,
    f12gd_f12_earnings_gap_dynamics_fillbalance_30d_jerk_v142_signal,
    f12gd_f12_earnings_gap_dynamics_absgapac_21d_jerk_v143_signal,
    f12gd_f12_earnings_gap_dynamics_gappassthrough_30d_jerk_v144_signal,
    f12gd_f12_earnings_gap_dynamics_gapsurpriseidx_21d_jerk_v145_signal,
    f12gd_f12_earnings_gap_dynamics_ovnmedian_30d_jerk_v146_signal,
    f12gd_f12_earnings_gap_dynamics_gapdominance_10d_jerk_v147_signal,
    f12gd_f12_earnings_gap_dynamics_gapgoupct_30d_jerk_v148_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergytanh_21d_jerk_v149_signal,
    f12gd_f12_earnings_gap_dynamics_gapwick_15d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_EARNINGS_GAP_DYNAMICS_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f12_earnings_gap_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
