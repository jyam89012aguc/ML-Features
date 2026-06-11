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


# mean overnight gap over 5d

def f12gd_f12_earnings_gap_dynamics_gapmean_5d_base_v001_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean overnight gap over 21d

def f12gd_f12_earnings_gap_dynamics_gapmean_21d_base_v002_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trimmed-mean overnight gap over 63d (robust central drift)

def f12gd_f12_earnings_gap_dynamics_gapmean_63d_base_v003_signal(open, close):
    graw = open / close.shift(1).replace(0, np.nan) - 1.0
    lo = graw.rolling(63, min_periods=21).quantile(0.10)
    hi = graw.rolling(63, min_periods=21).quantile(0.90)
    g = graw.where((graw >= lo) & (graw <= hi))
    b = g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-gap EMA span 21 (smoothed news-gap drift)

def f12gd_f12_earnings_gap_dynamics_loggapema_21d_base_v004_signal(open, close):
    g = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b = g.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap magnitude mean 21d (gappiness level)

def f12gd_f12_earnings_gap_dynamics_absgap_21d_base_v005_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap magnitude mean 63d

def f12gd_f12_earnings_gap_dynamics_absgap_63d_base_v006_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap impulse asymmetry: today's gap squared signed vs typical-variance 21d

def f12gd_f12_earnings_gap_dynamics_gapsurprise_21d_base_v007_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    var = (g ** 2).rolling(63, min_periods=21).mean()
    b = np.sign(g) * (g ** 2) / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# today's gap z-scored vs 63d gap history

def f12gd_f12_earnings_gap_dynamics_gapz_63d_base_v008_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    m = g.rolling(63, min_periods=21).mean()
    sd = g.rolling(63, min_periods=21).std()
    b = (g - m) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap vol-of-vol: 21d gap-std over 126d gap-std (dispersion regime)

def f12gd_f12_earnings_gap_dynamics_gapvov_126d_base_v009_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    s21 = g.rolling(21, min_periods=10).std()
    s126 = g.rolling(126, min_periods=63).std()
    b = s21 / s126.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap z (magnitude extremity) vs 63d

def f12gd_f12_earnings_gap_dynamics_absgapz_63d_base_v010_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = (g - g.rolling(63, min_periods=21).mean()) / g.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max abs gap z over last 21d (recent shock peak)

def f12gd_f12_earnings_gap_dynamics_maxgapz_21d_base_v011_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    z = (g - g.rolling(126, min_periods=63).mean()) / g.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = z.abs().rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed-gap rank: 21d-mean-gap percentile vs 252d history

def f12gd_f12_earnings_gap_dynamics_gaprank_252d_base_v012_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    sm = g.rolling(21, min_periods=10).mean()
    b = sm.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted gap-event frequency vs own scale 63d

def f12gd_f12_earnings_gap_dynamics_gapfreq_63d_base_v013_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 1.5 * sd).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted large-surprise frequency vs own scale 126d

def f12gd_f12_earnings_gap_dynamics_gapfreq_126d_base_v014_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 2.0 * sd).clip(lower=0)
    b = exc.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap direction persistence: mean run-signed-length of gap streaks 63d

def f12gd_f12_earnings_gap_dynamics_gapdirbias_63d_base_v015_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    s = np.sign(g)
    chg = (s != s.shift(1)).cumsum()
    rl = (s.groupby(chg).cumcount() + 1) * s
    b = rl.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of up-gaps over 21d weighted by magnitude

def f12gd_f12_earnings_gap_dynamics_upgapcnt_21d_base_v016_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    w = g.clip(lower=0)
    b = w.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of down-gaps over 21d weighted by magnitude

def f12gd_f12_earnings_gap_dynamics_dngapcnt_21d_base_v017_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    w = (-g).clip(lower=0)
    b = w.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since last big (>2.5sigma) gap event, scaled by recent gappiness

def f12gd_f12_earnings_gap_dynamics_dayssincegap_63d_base_v018_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    big = (g > 2.5 * sd).astype(float)
    grp = big.cumsum()
    dsl = big.groupby(grp).cumcount().astype(float).where(grp > 0)
    b = dsl * g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill fraction smoothed 21d (digestion of news gaps)

def f12gd_f12_earnings_gap_dynamics_gapfill_21d_base_v019_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    up = (open - low) / g.replace(0, np.nan)
    dn = (high - open) / (-g).replace(0, np.nan)
    f = up.where(g > 0, dn).clip(-2, 2)
    b = f.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of gaps fully filled same day over 63d

def f12gd_f12_earnings_gap_dynamics_fullfill_63d_base_v020_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    filled = ((g > 0) & (low <= pc)) | ((g < 0) & (high >= pc))
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01)
    num = (filled & ev).astype(float)
    den = ev.astype(float)
    b = num.rolling(63, min_periods=21).sum() / den.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# residual unfilled gap at close vs open gap (gap that held)

def f12gd_f12_earnings_gap_dynamics_gaphold_21d_base_v021_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    cg = close / close.shift(1).replace(0, np.nan) - 1.0
    hold = cg / g.replace(0, np.nan)
    b = hold.clip(-3, 3).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill asymmetry: up-gap fill minus down-gap fill 126d

def f12gd_f12_earnings_gap_dynamics_fillasym_126d_base_v022_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    upf = ((open - low) / g.replace(0, np.nan)).where(g > 0)
    dnf = ((high - open) / (-g).replace(0, np.nan)).where(g < 0)
    b = upf.rolling(126, min_periods=42).mean() - dnf.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return displacement: 5d mean minus 21d EMA (gap impulse)

def f12gd_f12_earnings_gap_dynamics_ovnret_21d_base_v023_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(5, min_periods=3).mean() - ov.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return mean 21d (digestion component)

def f12gd_f12_earnings_gap_dynamics_intraret_21d_base_v024_signal(open, close):
    intr = close / open.replace(0, np.nan) - 1.0
    b = intr.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight minus intraday mean 63d (where the return is made)

def f12gd_f12_earnings_gap_dynamics_ovnminusintra_63d_base_v025_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    b = (ov - intr).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of total return from overnight gaps 63d

def f12gd_f12_earnings_gap_dynamics_ovnshare_63d_base_v026_signal(open, close):
    ov = (open / close.shift(1).replace(0, np.nan) - 1.0)
    intr = (close / open.replace(0, np.nan) - 1.0)
    num = ov.abs().rolling(63, min_periods=21).sum()
    den = (ov.abs() + intr.abs()).rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-intraday return correlation 63d (reversal vs continuation)

def f12gd_f12_earnings_gap_dynamics_ovncorr_63d_base_v027_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    b = ov.rolling(63, min_periods=21).corr(intr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return volatility 63d (gap-driven risk)

def f12gd_f12_earnings_gap_dynamics_ovnvol_63d_base_v028_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap times volume-spike 21d (volume-confirmed gap intensity)

def f12gd_f12_earnings_gap_dynamics_gapvol_21d_base_v029_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    vs = volume / volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
    b = (g * vs).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap times volume-spike (confirmed event magnitude) 63d

def f12gd_f12_earnings_gap_dynamics_absgapvol_63d_base_v030_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (g * vs).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed gap intensity vs own scale 63d

def f12gd_f12_earnings_gap_dynamics_gapvolfreq_63d_base_v031_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    exc = (g - 1.5 * sd).clip(lower=0) * (vs - 1.0).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted average gap 63d

def f12gd_f12_earnings_gap_dynamics_volwgap_63d_base_v032_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    num = (g * volume).rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-in-TR-units dispersion 21d (range-relative gap variability)

def f12gd_f12_earnings_gap_dynamics_gaptr_21d_base_v033_signal(open, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=10).mean()
    gr = (open - pc) / atr.replace(0, np.nan)
    b = gr.rolling(21, min_periods=10).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap in ATR units mean 63d (range-relative gappiness)

def f12gd_f12_earnings_gap_dynamics_absgaptr_63d_base_v034_signal(open, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open - pc).abs()
    b = (g / atr.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# standardized-gap tail load: 90th pct of |gap|/gap-vol 63d

def f12gd_f12_earnings_gap_dynamics_gapstdvol_63d_base_v035_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    vol = g.rolling(63, min_periods=21).std()
    sg = (g / vol.replace(0, np.nan)).abs()
    b = sg.rolling(63, min_periods=21).quantile(0.90)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion (std of gaps) 21d

def f12gd_f12_earnings_gap_dynamics_gapdisp_21d_base_v036_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(21, min_periods=10).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion 126d

def f12gd_f12_earnings_gap_dynamics_gapdisp_126d_base_v037_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap kurtosis-like: max|gap| over mean|gap| 63d (fat-tail gaps)

def f12gd_f12_earnings_gap_dynamics_gapfattail_63d_base_v038_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(63, min_periods=21).max() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap autocorrelation lag-1 over 63d (gap momentum)

def f12gd_f12_earnings_gap_dynamics_gapac_63d_base_v039_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(63, min_periods=21).corr(g.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap clustering: rolling std-of-absgap over 21d vs 126d

def f12gd_f12_earnings_gap_dynamics_gapcluster_126d_base_v040_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    s = g.rolling(21, min_periods=10).std()
    b = s / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap skewness 126d (asymmetry of surprises)

def f12gd_f12_earnings_gap_dynamics_gapskew_126d_base_v041_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap up/down dispersion balance: upside gap std minus downside gap std 63d

def f12gd_f12_earnings_gap_dynamics_gapmagasym_63d_base_v042_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    upsd = g.where(g > 0).rolling(63, min_periods=21).std()
    dnsd = (-g).where(g < 0).rolling(63, min_periods=21).std()
    b = upsd - dnsd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest up-gap minus largest down-gap 126d (tail asymmetry)

def f12gd_f12_earnings_gap_dynamics_tailasym_126d_base_v043_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).max() + g.rolling(126, min_periods=63).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-gap continuation: next-day return after up-gaps 63d

def f12gd_f12_earnings_gap_dynamics_postgapcont_63d_base_v044_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    fwd = close.shift(-1) / close.replace(0, np.nan) - 1.0
    cont = (np.sign(g) * fwd)
    b = cont.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day close strength: close-in-gap-day-range 21d

def f12gd_f12_earnings_gap_dynamics_gapclosestr_21d_base_v045_signal(open, high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    w = (g > 0.02).astype(float)
    b = (pos * w).rolling(21, min_periods=10).sum() / w.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-and-go: gap same-sign as intraday over 63d

def f12gd_f12_earnings_gap_dynamics_gapandgo_63d_base_v046_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    same = (np.sign(g) == np.sign(intr)).astype(float)
    ev = (g.abs() > 0.015).astype(float)
    b = (same * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight gap return 63d (gap alpha drift)

def f12gd_f12_earnings_gap_dynamics_cumovn_63d_base_v047_signal(open, close):
    ov = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b = ov.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative intraday return 63d

def f12gd_f12_earnings_gap_dynamics_cumintra_63d_base_v048_signal(open, close):
    intr = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = intr.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift minus intraday drift 126d

def f12gd_f12_earnings_gap_dynamics_driftspread_126d_base_v049_signal(open, close):
    ov = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    intr = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = ov.rolling(126, min_periods=63).sum() - intr.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap tail concentration: 95th-pct |gap| over median |gap| 252d

def f12gd_f12_earnings_gap_dynamics_gaprelhist_252d_base_v050_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    q95 = g.rolling(252, min_periods=63).quantile(0.95)
    med = g.rolling(252, min_periods=63).median()
    b = q95 / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap momentum: 5d mean gap minus 63d mean gap

def f12gd_f12_earnings_gap_dynamics_gapmom_63d_base_v051_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(5, min_periods=3).mean() - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cumulative gap-fill failure 63d (gaps that stuck)

def f12gd_f12_earnings_gap_dynamics_fillfail_63d_base_v052_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    stuck = (((g > 0) & (low > pc)) | ((g < 0) & (high < pc))).astype(float)
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01).astype(float)
    b = stuck.rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight upside/downside dispersion ratio 63d (gap risk asymmetry)

def f12gd_f12_earnings_gap_dynamics_ovnsharpe_63d_base_v053_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    upsd = g.clip(lower=0).rolling(63, min_periods=21).std()
    dnsd = g.clip(upper=0).rolling(63, min_periods=21).std()
    b = upsd / dnsd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday downside-deviation share: neg-intraday std over total 63d

def f12gd_f12_earnings_gap_dynamics_intrasharpe_63d_base_v054_signal(open, close):
    intr = close / open.replace(0, np.nan) - 1.0
    dn = intr.clip(upper=0).rolling(63, min_periods=21).std()
    tot = intr.rolling(63, min_periods=21).std()
    b = dn / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap range expansion: gap-day TR vs 21d ATR 21d

def f12gd_f12_earnings_gap_dynamics_gaprangeexp_21d_base_v055_signal(open, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    exp = (tr / atr.replace(0, np.nan)) * (g > 0.02).astype(float)
    b = exp.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed gap EMA fast minus slow (gap trend) 

def f12gd_f12_earnings_gap_dynamics_gaptrend_21d_base_v056_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.ewm(span=10, min_periods=5).mean() - g.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of upside gaps among events 126d (sentiment tilt)

def f12gd_f12_earnings_gap_dynamics_upgapprop_126d_base_v057_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    ev = (g.abs() > 0.02)
    up = (g > 0.02).astype(float)
    b = up.rolling(126, min_periods=42).sum() / ev.astype(float).rolling(126, min_periods=42).sum().replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap entropy proxy: 1 minus |mean gap|/mean|gap| 63d

def f12gd_f12_earnings_gap_dynamics_gapentropy_63d_base_v058_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = 1.0 - g.rolling(63, min_periods=21).mean().abs() / g.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single up-gap over 63d

def f12gd_f12_earnings_gap_dynamics_maxupgap_63d_base_v059_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single down-gap (most negative) over 63d

def f12gd_f12_earnings_gap_dynamics_maxdngap_63d_base_v060_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap range: max minus min gap 63d (gap span)

def f12gd_f12_earnings_gap_dynamics_gapspan_63d_base_v061_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday reversal of gap: -corr(gap, intraday) 126d (fade strength)

def f12gd_f12_earnings_gap_dynamics_gapfade_126d_base_v062_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    b = -g.rolling(126, min_periods=63).corr(intr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight contribution z vs 252d

def f12gd_f12_earnings_gap_dynamics_ovncontribz_252d_base_v063_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    c = ov.rolling(21, min_periods=10).sum()
    b = (c - c.rolling(252, min_periods=63).mean()) / c.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day volume share of 21d volume (event volume concentration)

def f12gd_f12_earnings_gap_dynamics_gapvolshare_63d_base_v064_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    ev = (g > 0.02).astype(float)
    evol = (ev * volume).rolling(63, min_periods=21).sum()
    b = evol / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday gap-retrace extent vs day range 21d

def f12gd_f12_earnings_gap_dynamics_fillspeed_21d_base_v065_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    retr_up = (open - low) / (high - low).replace(0, np.nan)
    retr_dn = (high - open) / (high - low).replace(0, np.nan)
    r = retr_up.where(g > 0, retr_dn)
    b = r.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap acceleration as level: 21d absgap minus 63d absgap

def f12gd_f12_earnings_gap_dynamics_absgapaccel_63d_base_v066_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(21, min_periods=10).mean() - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak of consecutive same-direction gaps (gap run length)

def f12gd_f12_earnings_gap_dynamics_gapstreak_21d_base_v067_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    s = np.sign(g)
    chg = (s != s.shift(1)).cumsum()
    rl = s.groupby(chg).cumcount() + 1
    b = (rl * s).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside overnight semi-deviation 63d (gap-down risk)

def f12gd_f12_earnings_gap_dynamics_ovnsemidev_63d_base_v068_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    neg = g.clip(upper=0)
    b = neg.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside overnight semi-deviation 63d (gap-up potential)

def f12gd_f12_earnings_gap_dynamics_ovnsemidevup_63d_base_v069_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    pos = g.clip(lower=0)
    b = pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap shock decay: |gap| now vs its 10d-ago value

def f12gd_f12_earnings_gap_dynamics_gapdecay_21d_base_v070_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sm = g.rolling(5, min_periods=3).mean()
    b = sm - sm.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of overnight vol to total daily vol 63d

def f12gd_f12_earnings_gap_dynamics_ovnvolshare_63d_base_v071_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    tot = close / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(63, min_periods=21).std() / tot.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of distinct gap events (entries) plus magnitude tilt 126d

def f12gd_f12_earnings_gap_dynamics_gapevententry_126d_base_v072_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    ev = (g > 1.8 * sd).astype(float)
    entry = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    b = entry.rolling(126, min_periods=42).sum() + 20.0 * g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# median gap level 126d (typical surprise)

def f12gd_f12_earnings_gap_dynamics_gapmedian_126d_base_v073_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interquartile gap range 126d (robust dispersion)

def f12gd_f12_earnings_gap_dynamics_gapiqr_126d_base_v074_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).quantile(0.75) - g.rolling(126, min_periods=63).quantile(0.25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vol beta: regression slope gap on volume-spike 126d

def f12gd_f12_earnings_gap_dynamics_gapvolbeta_126d_base_v075_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    vs = volume / volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
    cov = g.rolling(126, min_periods=63).cov(vs)
    var = vs.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f12gd_f12_earnings_gap_dynamics_gapmean_5d_base_v001_signal,
    f12gd_f12_earnings_gap_dynamics_gapmean_21d_base_v002_signal,
    f12gd_f12_earnings_gap_dynamics_gapmean_63d_base_v003_signal,
    f12gd_f12_earnings_gap_dynamics_loggapema_21d_base_v004_signal,
    f12gd_f12_earnings_gap_dynamics_absgap_21d_base_v005_signal,
    f12gd_f12_earnings_gap_dynamics_absgap_63d_base_v006_signal,
    f12gd_f12_earnings_gap_dynamics_gapsurprise_21d_base_v007_signal,
    f12gd_f12_earnings_gap_dynamics_gapz_63d_base_v008_signal,
    f12gd_f12_earnings_gap_dynamics_gapvov_126d_base_v009_signal,
    f12gd_f12_earnings_gap_dynamics_absgapz_63d_base_v010_signal,
    f12gd_f12_earnings_gap_dynamics_maxgapz_21d_base_v011_signal,
    f12gd_f12_earnings_gap_dynamics_gaprank_252d_base_v012_signal,
    f12gd_f12_earnings_gap_dynamics_gapfreq_63d_base_v013_signal,
    f12gd_f12_earnings_gap_dynamics_gapfreq_126d_base_v014_signal,
    f12gd_f12_earnings_gap_dynamics_gapdirbias_63d_base_v015_signal,
    f12gd_f12_earnings_gap_dynamics_upgapcnt_21d_base_v016_signal,
    f12gd_f12_earnings_gap_dynamics_dngapcnt_21d_base_v017_signal,
    f12gd_f12_earnings_gap_dynamics_dayssincegap_63d_base_v018_signal,
    f12gd_f12_earnings_gap_dynamics_gapfill_21d_base_v019_signal,
    f12gd_f12_earnings_gap_dynamics_fullfill_63d_base_v020_signal,
    f12gd_f12_earnings_gap_dynamics_gaphold_21d_base_v021_signal,
    f12gd_f12_earnings_gap_dynamics_fillasym_126d_base_v022_signal,
    f12gd_f12_earnings_gap_dynamics_ovnret_21d_base_v023_signal,
    f12gd_f12_earnings_gap_dynamics_intraret_21d_base_v024_signal,
    f12gd_f12_earnings_gap_dynamics_ovnminusintra_63d_base_v025_signal,
    f12gd_f12_earnings_gap_dynamics_ovnshare_63d_base_v026_signal,
    f12gd_f12_earnings_gap_dynamics_ovncorr_63d_base_v027_signal,
    f12gd_f12_earnings_gap_dynamics_ovnvol_63d_base_v028_signal,
    f12gd_f12_earnings_gap_dynamics_gapvol_21d_base_v029_signal,
    f12gd_f12_earnings_gap_dynamics_absgapvol_63d_base_v030_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolfreq_63d_base_v031_signal,
    f12gd_f12_earnings_gap_dynamics_volwgap_63d_base_v032_signal,
    f12gd_f12_earnings_gap_dynamics_gaptr_21d_base_v033_signal,
    f12gd_f12_earnings_gap_dynamics_absgaptr_63d_base_v034_signal,
    f12gd_f12_earnings_gap_dynamics_gapstdvol_63d_base_v035_signal,
    f12gd_f12_earnings_gap_dynamics_gapdisp_21d_base_v036_signal,
    f12gd_f12_earnings_gap_dynamics_gapdisp_126d_base_v037_signal,
    f12gd_f12_earnings_gap_dynamics_gapfattail_63d_base_v038_signal,
    f12gd_f12_earnings_gap_dynamics_gapac_63d_base_v039_signal,
    f12gd_f12_earnings_gap_dynamics_gapcluster_126d_base_v040_signal,
    f12gd_f12_earnings_gap_dynamics_gapskew_126d_base_v041_signal,
    f12gd_f12_earnings_gap_dynamics_gapmagasym_63d_base_v042_signal,
    f12gd_f12_earnings_gap_dynamics_tailasym_126d_base_v043_signal,
    f12gd_f12_earnings_gap_dynamics_postgapcont_63d_base_v044_signal,
    f12gd_f12_earnings_gap_dynamics_gapclosestr_21d_base_v045_signal,
    f12gd_f12_earnings_gap_dynamics_gapandgo_63d_base_v046_signal,
    f12gd_f12_earnings_gap_dynamics_cumovn_63d_base_v047_signal,
    f12gd_f12_earnings_gap_dynamics_cumintra_63d_base_v048_signal,
    f12gd_f12_earnings_gap_dynamics_driftspread_126d_base_v049_signal,
    f12gd_f12_earnings_gap_dynamics_gaprelhist_252d_base_v050_signal,
    f12gd_f12_earnings_gap_dynamics_gapmom_63d_base_v051_signal,
    f12gd_f12_earnings_gap_dynamics_fillfail_63d_base_v052_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsharpe_63d_base_v053_signal,
    f12gd_f12_earnings_gap_dynamics_intrasharpe_63d_base_v054_signal,
    f12gd_f12_earnings_gap_dynamics_gaprangeexp_21d_base_v055_signal,
    f12gd_f12_earnings_gap_dynamics_gaptrend_21d_base_v056_signal,
    f12gd_f12_earnings_gap_dynamics_upgapprop_126d_base_v057_signal,
    f12gd_f12_earnings_gap_dynamics_gapentropy_63d_base_v058_signal,
    f12gd_f12_earnings_gap_dynamics_maxupgap_63d_base_v059_signal,
    f12gd_f12_earnings_gap_dynamics_maxdngap_63d_base_v060_signal,
    f12gd_f12_earnings_gap_dynamics_gapspan_63d_base_v061_signal,
    f12gd_f12_earnings_gap_dynamics_gapfade_126d_base_v062_signal,
    f12gd_f12_earnings_gap_dynamics_ovncontribz_252d_base_v063_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolshare_63d_base_v064_signal,
    f12gd_f12_earnings_gap_dynamics_fillspeed_21d_base_v065_signal,
    f12gd_f12_earnings_gap_dynamics_absgapaccel_63d_base_v066_signal,
    f12gd_f12_earnings_gap_dynamics_gapstreak_21d_base_v067_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsemidev_63d_base_v068_signal,
    f12gd_f12_earnings_gap_dynamics_ovnsemidevup_63d_base_v069_signal,
    f12gd_f12_earnings_gap_dynamics_gapdecay_21d_base_v070_signal,
    f12gd_f12_earnings_gap_dynamics_ovnvolshare_63d_base_v071_signal,
    f12gd_f12_earnings_gap_dynamics_gapevententry_126d_base_v072_signal,
    f12gd_f12_earnings_gap_dynamics_gapmedian_126d_base_v073_signal,
    f12gd_f12_earnings_gap_dynamics_gapiqr_126d_base_v074_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolbeta_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_EARNINGS_GAP_DYNAMICS_REGISTRY_001_075 = REGISTRY


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

    print("OK f12_earnings_gap_dynamics_base_001_075_claude: %d features pass" % n_features)
