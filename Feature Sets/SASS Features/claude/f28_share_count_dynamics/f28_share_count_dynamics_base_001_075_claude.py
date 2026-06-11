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


def _logchg(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s over a trailing window, per-step
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (share-count dynamics) =====
def _f28_dilution(shares, w):
    # net share-count growth over window: >0 dilution, <0 buyback
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f28_creep(shareswadil, shareswa):
    # diluted-share creep: how much dilution lurks beyond basic count
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f28_buyback_intensity(ncfcommon, shares, px=1.0):
    # -ncfcommon is cash returned to holders (buyback); normalize by share base
    return (-ncfcommon) / shares.replace(0, np.nan)


def _f28_net_issuance(ncfcommon, w):
    # cumulative net common cash flow trend (issuance>0, buyback<0)
    return ncfcommon.rolling(w, min_periods=max(1, w // 2)).sum()


def _f28_dilution_streak(shares, w):
    # fraction of last w periods with rising share count (dilution persistence)
    up = (shares.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean()


def _f28_buyback_streak(shares, w):
    down = (shares.diff() < 0).astype(float)
    return down.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- share-count change (dilution / buyback) on sharesbas ---
def f28sc_f28_share_count_dynamics_dilbas_63d_base_v001_signal(sharesbas):
    b = _f28_dilution(sharesbas, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas_252d_base_v002_signal(sharesbas):
    b = _f28_dilution(sharesbas, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilbas_504d_base_v003_signal(sharesbas):
    b = _f28_dilution(sharesbas, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log share-count change z-scored vs own history (de-trended dilution intensity)
def f28sc_f28_share_count_dynamics_dilbasz_252d_base_v004_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution rank vs own 504d history (percentile of issuance pace)
def f28sc_f28_share_count_dynamics_dilbasrank_252d_base_v005_signal(sharesbas):
    g = _f28_dilution(sharesbas, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- weighted-average shares dilution ---
def f28sc_f28_share_count_dynamics_dilwa_63d_base_v006_signal(shareswa):
    b = _f28_dilution(shareswa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_dilwa_252d_base_v007_signal(shareswa):
    b = _f28_dilution(shareswa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average share growth acceleration-as-level (annual vs prior annual)
def f28sc_f28_share_count_dynamics_dilwaaccel_252d_base_v008_signal(shareswa):
    g = _f28_dilution(shareswa, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution smoothed (persistent issuance regime)
def f28sc_f28_share_count_dynamics_dilwaema_252d_base_v009_signal(shareswa):
    g = _logchg(shareswa, 252)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- diluted-share creep (shareswadil vs shareswa) ---
def f28sc_f28_share_count_dynamics_creep_0d_base_v010_signal(shareswadil, shareswa):
    b = _f28_creep(shareswadil, shareswa)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep change over a year (is the dilution overhang widening?)
def f28sc_f28_share_count_dynamics_creepchg_252d_base_v011_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep z-scored vs own 252d history
def f28sc_f28_share_count_dynamics_creepz_252d_base_v012_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep percentile-ranked vs own 504d history
def f28sc_f28_share_count_dynamics_creeprank_504d_base_v013_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share own growth, ranked vs its own two-year history (overhang growth percentile)
def f28sc_f28_share_count_dynamics_dildil_252d_base_v014_signal(shareswadil):
    g = _f28_dilution(shareswadil, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic growth ratio (how many times faster the overhang is expanding)
def f28sc_f28_share_count_dynamics_dilspread_252d_base_v015_signal(shareswadil, shareswa):
    gd = _logchg(shareswadil, 252)
    gb = _logchg(shareswa, 252)
    b = np.tanh(gd / gb.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- buyback intensity (-ncfcommon) ---
def f28sc_f28_share_count_dynamics_bbintens_0d_base_v016_signal(ncfcommon, sharesbas):
    b = _f28_buyback_intensity(ncfcommon, sharesbas)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity smoothed over a quarter
def f28sc_f28_share_count_dynamics_bbintens_63d_base_v017_signal(ncfcommon, sharesbas):
    raw = _f28_buyback_intensity(ncfcommon, sharesbas)
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity z-scored vs own history
def f28sc_f28_share_count_dynamics_bbintensz_252d_base_v018_signal(ncfcommon, shareswa):
    raw = _f28_buyback_intensity(ncfcommon, shareswa)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign of net common cash flow x magnitude (issuance vs buyback regime)
def f28sc_f28_share_count_dynamics_ncfsignmag_252d_base_v019_signal(ncfcommon):
    s = _f28_net_issuance(ncfcommon, 252)
    b = np.sign(s) * np.log1p(s.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common cash flow normalized by trailing absolute flow (directional purity)
def f28sc_f28_share_count_dynamics_ncfpurity_252d_base_v020_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- share-count trend (slope) ---
def f28sc_f28_share_count_dynamics_trendbas_252d_base_v021_signal(sharesbas):
    lg = np.log(sharesbas.replace(0, np.nan))
    b = _slope(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f28sc_f28_share_count_dynamics_trendwa_126d_base_v022_signal(shareswa):
    lg = np.log(shareswa.replace(0, np.nan))
    b = _slope(lg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend curvature: short trend minus long trend (acceleration of dilution)
def f28sc_f28_share_count_dynamics_trendcurv_base_v023_signal(sharesbas):
    lg = np.log(sharesbas.replace(0, np.nan))
    short = _slope(lg, 63)
    long = _slope(lg, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net issuance: annual net common flow z-scored vs its own multi-year history ---
def f28sc_f28_share_count_dynamics_netiss_252d_base_v024_signal(ncfcommon):
    net = _f28_net_issuance(ncfcommon, 252)
    sm = np.sign(net) * np.log1p(net.abs())
    b = _z(sm, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# net issuance trend (slope of cumulative common flow)
def f28sc_f28_share_count_dynamics_netisstrend_252d_base_v025_signal(ncfcommon):
    cum = ncfcommon.cumsum()
    b = _slope(cum, 252)
    result = np.sign(b) * np.log1p(b.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# --- dilution streak ---
def f28sc_f28_share_count_dynamics_dilstreak_252d_base_v026_signal(sharesbas):
    b = _f28_dilution_streak(sharesbas, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback lumpiness: peak monthly cash returned vs its yearly average (concentration)
def f28sc_f28_share_count_dynamics_bbstreak_252d_base_v027_signal(ncfcommon):
    m = (-ncfcommon).rolling(21, min_periods=10).sum().clip(lower=0)
    peak = m.rolling(252, min_periods=126).max()
    avg = m.rolling(252, min_periods=126).mean()
    b = peak / avg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-minus-buyback streak balance (net persistence of issuance)
def f28sc_f28_share_count_dynamics_streakbal_252d_base_v028_signal(shareswa):
    up = _f28_dilution_streak(shareswa, 252)
    dn = _f28_buyback_streak(shareswa, 252)
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interactions & spreads (diversifiers) ---
# dilution dispersion: std of quarterly share-growth over two years (erratic issuance)
def f28sc_f28_share_count_dynamics_dildisp_504d_base_v029_signal(sharesbas):
    g = _logchg(sharesbas, 63)
    b = _std(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution intensity x creep (issuing AND option overhang growing = double dilution)
def f28sc_f28_share_count_dynamics_dilxcreep_252d_base_v030_signal(sharesbas, shareswadil, shareswa):
    dil = _z(_f28_dilution(sharesbas, 252), 252)
    creep = _z(_f28_creep(shareswadil, shareswa), 252)
    b = dil * creep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash returned per unit of share-count reduced (buyback price-efficiency proxy)
def f28sc_f28_share_count_dynamics_netyield_252d_base_v031_signal(ncfcommon, sharesbas):
    bb = (-ncfcommon).rolling(252, min_periods=126).sum()
    cnt_chg = (sharesbas.shift(252) - sharesbas)  # >0 when count fell
    b = np.tanh(bb / (cnt_chg.abs() + 1.0) / 1e3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long dilution spread on weighted-average shares (issuance regime change)
def f28sc_f28_share_count_dynamics_dilwaspr_63v252_base_v032_signal(shareswa):
    short = _f28_dilution(shareswa, 63)
    long = _f28_dilution(shareswa, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-weighted-average count divergence (timing of issuance within year)
def f28sc_f28_share_count_dynamics_baswadiv_0d_base_v033_signal(sharesbas, shareswa):
    b = sharesbas / shareswa.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence change: is end-of-period count running ahead of the average?
def f28sc_f28_share_count_dynamics_baswadivchg_252d_base_v034_signal(sharesbas, shareswa):
    d = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed dilution momentum (bounded change in annual dilution)
def f28sc_f28_share_count_dynamics_diltanh_252d_base_v035_signal(sharesbas):
    g = _f28_dilution(sharesbas, 252)
    chg = g - g.shift(63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution per unit of issuance-volatility (risk-adjusted dilution)
def f28sc_f28_share_count_dynamics_dilvol_252d_base_v036_signal(sharesbas):
    g = _f28_dilution(sharesbas, 252)
    vol = _std(_logchg(sharesbas, 21), 252)
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback consistency: fraction of quarters with net cash returned over two years
def f28sc_f28_share_count_dynamics_bbconsist_504d_base_v037_signal(ncfcommon):
    qsum = ncfcommon.rolling(63, min_periods=21).sum()
    ret = (qsum < 0).astype(float)
    b = ret.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance magnitude: average size of capital-raising quarters over two years
def f28sc_f28_share_count_dynamics_issconsist_504d_base_v038_signal(ncfcommon):
    qsum = ncfcommon.rolling(63, min_periods=21).sum()
    raise_amt = qsum.clip(lower=0)
    b = np.log1p(raise_amt.rolling(504, min_periods=252).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep level x diluted-share growth (option-driven dilution pressure)
def f28sc_f28_share_count_dynamics_creepxdil_252d_base_v039_signal(shareswadil, shareswa):
    creep = _f28_creep(shareswadil, shareswa)
    gd = _f28_dilution(shareswadil, 252)
    b = creep * np.sign(gd) * (gd.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon dilution disagreement (63/252/504 share-growth dispersion)
def f28sc_f28_share_count_dynamics_dilmultidisp_base_v040_signal(sharesbas):
    g1 = _f28_dilution(sharesbas, 63)
    g2 = _f28_dilution(sharesbas, 252)
    g3 = _f28_dilution(sharesbas, 504)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-rate acceleration: change in per-share net common flow vs a quarter ago
def f28sc_f28_share_count_dynamics_issrate_252d_base_v041_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    rate = net / sharesbas.replace(0, np.nan)
    sm = np.sign(rate) * np.log1p(rate.abs())
    b = sm - sm.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


# dilution streak depth: streak fraction weighted by average dilution size
def f28sc_f28_share_count_dynamics_dilstreakdepth_252d_base_v042_signal(sharesbas):
    streak = _f28_dilution_streak(sharesbas, 252)
    b = _z(streak, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution pace vs its own medium-term baseline (deviation from 504d typical pace)
def f28sc_f28_share_count_dynamics_dilyoy_252d_base_v043_signal(shareswa):
    g = _logchg(shareswa, 252)
    base = g.rolling(504, min_periods=252).median()
    b = g - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep trend slope over a year (overhang trajectory)
def f28sc_f28_share_count_dynamics_creeptrend_252d_base_v044_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _slope(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base half-life: how long since last buyback (count below recent max)
def f28sc_f28_share_count_dynamics_belowmax_504d_base_v045_signal(sharesbas):
    rmax = _rmax(sharesbas, 504)
    b = sharesbas / rmax.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base above recent min (how much has it grown off its trough)
def f28sc_f28_share_count_dynamics_abovemin_504d_base_v046_signal(sharesbas):
    rmin = _rmin(sharesbas, 504)
    b = sharesbas / rmin.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position of current count within its 504d range (issuance cycle phase)
def f28sc_f28_share_count_dynamics_countrngpos_504d_base_v047_signal(sharesbas):
    hi = _rmax(sharesbas, 504)
    lo = _rmin(sharesbas, 504)
    b = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity rank vs own history (relative aggressiveness)
def f28sc_f28_share_count_dynamics_bbrank_504d_base_v048_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share creep dispersion (volatility of overhang)
def f28sc_f28_share_count_dynamics_creepdisp_252d_base_v049_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _std(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year where diluted count rose faster than basic (overhang-driven days)
def f28sc_f28_share_count_dynamics_dilminusdil_252d_base_v050_signal(shareswa, shareswadil):
    overhang_lead = (shareswadil.pct_change() > shareswa.pct_change()).astype(float)
    b = overhang_lead.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count momentum: 126d growth minus 126d-lagged 126d growth
def f28sc_f28_share_count_dynamics_dilmom_126d_base_v051_signal(sharesbas):
    g = _f28_dilution(sharesbas, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow EMA (smoothed issuance/buyback bias)
def f28sc_f28_share_count_dynamics_ncfema_base_v052_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    s = q.ewm(span=126, min_periods=42).mean()
    b = np.sign(s) * np.log1p(s.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution hit-rate asymmetry: up-quarters minus down-quarters share-count moves
def f28sc_f28_share_count_dynamics_dilasym_252d_base_v053_signal(shareswa):
    chg = _logchg(shareswa, 21)
    up = (chg > 0).astype(float).rolling(252, min_periods=126).mean()
    dn = (chg < 0).astype(float).rolling(252, min_periods=126).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback funded yield: cash returned per share relative to count growth (efficiency)
def f28sc_f28_share_count_dynamics_bbeff_252d_base_v054_signal(ncfcommon, sharesbas):
    cash = (-ncfcommon).rolling(252, min_periods=126).sum()
    growth = _f28_dilution(sharesbas, 252)
    b = np.sign(cash) * np.log1p(cash.abs()) * np.sign(-growth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share trend slope (overhang-inclusive count trajectory)
def f28sc_f28_share_count_dynamics_trenddil_252d_base_v055_signal(shareswadil):
    lg = np.log(shareswadil.replace(0, np.nan))
    b = _slope(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep convexity: squared signed deviation of creep from its own mean
def f28sc_f28_share_count_dynamics_creepconv_252d_base_v056_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    dev = c - c.rolling(252, min_periods=126).mean()
    b = np.sign(dev) * (dev ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance directional momentum: change in net-flow purity over a year
def f28sc_f28_share_count_dynamics_puritymom_252d_base_v057_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    b = pur - pur.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count level relative to its 252d mean (deviation from issuance trend)
def f28sc_f28_share_count_dynamics_countdev_252d_base_v058_signal(sharesbas):
    m = _mean(sharesbas, 252)
    b = sharesbas / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution percentile vs own 252d history
def f28sc_f28_share_count_dynamics_dilwarank_252d_base_v059_signal(shareswa):
    g = _f28_dilution(shareswa, 252)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-to-creep offset: z-scored buyback intensity minus z-scored option creep
def f28sc_f28_share_count_dynamics_bbvscreep_252d_base_v060_signal(ncfcommon, shareswadil, shareswa):
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / shareswa.replace(0, np.nan)
    creep = _f28_creep(shareswadil, shareswa)
    b = _z(bb, 252) - _z(creep, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration as level: 63d growth minus prior 63d growth
def f28sc_f28_share_count_dynamics_dilaccel_63d_base_v061_signal(sharesbas):
    g = _f28_dilution(sharesbas, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year dilution z vs two-year history
def f28sc_f28_share_count_dynamics_dilz_126d_base_v062_signal(sharesbas):
    g = _logchg(sharesbas, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep relative to its 504d max (overhang vs worst dilution overhang)
def f28sc_f28_share_count_dynamics_creepvsmax_504d_base_v063_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    cmax = _rmax(c, 504)
    b = c - cmax
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow stance turnover blended with average stance (issuance regime texture)
def f28sc_f28_share_count_dynamics_ncfsignpersist_252d_base_v064_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    sgn = np.sign(q)
    flips = (sgn != sgn.shift(5)).astype(float).rolling(252, min_periods=126).mean()
    tilt = q.rolling(252, min_periods=126).mean()
    b = flips + np.tanh(tilt / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count growth smoothness: |trend| over total path traveled (efficiency ratio)
def f28sc_f28_share_count_dynamics_diler_252d_base_v065_signal(sharesbas):
    lg = np.log(sharesbas.replace(0, np.nan))
    net = (lg - lg.shift(252)).abs()
    path = lg.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average count vs basic count gap, smoothed (issuance-timing bias)
def f28sc_f28_share_count_dynamics_watobasema_base_v066_signal(shareswa, sharesbas):
    d = shareswa / sharesbas.replace(0, np.nan) - 1.0
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution trend sign x creep level (issuing-while-overhang-high flag)
def f28sc_f28_share_count_dynamics_dilsignxcreep_base_v067_signal(shareswa, shareswadil):
    lg = np.log(shareswa.replace(0, np.nan))
    sl = _slope(lg, 252)
    creep = _f28_creep(shareswadil, shareswa)
    b = np.sign(sl) * creep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution drag over two years, ranked vs its own five-year history
def f28sc_f28_share_count_dynamics_cumdrag_504d_base_v068_signal(sharesbas):
    g = _logchg(sharesbas, 504)
    b = _rank(g, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity dispersion (lumpy vs steady repurchases)
def f28sc_f28_share_count_dynamics_bbdisp_504d_base_v069_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = _std(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average share quarterly-growth impulse, percentile-ranked vs own history
def f28sc_f28_share_count_dynamics_dilimpulse_63d_base_v070_signal(shareswa):
    g = _logchg(shareswa, 63)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share growth z vs own history (overhang growth extremity)
def f28sc_f28_share_count_dynamics_dildilz_252d_base_v071_signal(shareswadil):
    g = _logchg(shareswadil, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance vs creep spread: rank of cash-issuance pace minus rank of option creep
def f28sc_f28_share_count_dynamics_issvscreep_252d_base_v072_signal(ncfcommon, sharesbas, shareswadil, shareswa):
    iss = ncfcommon.rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    creep = _f28_creep(shareswadil, shareswa)
    b = _rank(iss, 504) - _rank(creep, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count drawup: distance below the cleanest (min) count over five years
def f28sc_f28_share_count_dynamics_leangap_1260d_base_v073_signal(sharesbas):
    lo = _rmin(sharesbas, 1260)
    b = np.log(sharesbas.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution streak balance over five years (long-run issuance bias)
def f28sc_f28_share_count_dynamics_streakbal_1260d_base_v074_signal(shareswa):
    up = _f28_dilution_streak(shareswa, 1260)
    dn = _f28_buyback_streak(shareswa, 1260)
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined count-reduction quality: buyback purity x magnitude of count decline
def f28sc_f28_share_count_dynamics_reductqual_252d_base_v075_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = -net / gross.replace(0, np.nan)
    decline = (-_f28_dilution(sharesbas, 252)).clip(lower=0)
    b = pur * np.log1p(decline)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sc_f28_share_count_dynamics_dilbas_63d_base_v001_signal,
    f28sc_f28_share_count_dynamics_dilbas_252d_base_v002_signal,
    f28sc_f28_share_count_dynamics_dilbas_504d_base_v003_signal,
    f28sc_f28_share_count_dynamics_dilbasz_252d_base_v004_signal,
    f28sc_f28_share_count_dynamics_dilbasrank_252d_base_v005_signal,
    f28sc_f28_share_count_dynamics_dilwa_63d_base_v006_signal,
    f28sc_f28_share_count_dynamics_dilwa_252d_base_v007_signal,
    f28sc_f28_share_count_dynamics_dilwaaccel_252d_base_v008_signal,
    f28sc_f28_share_count_dynamics_dilwaema_252d_base_v009_signal,
    f28sc_f28_share_count_dynamics_creep_0d_base_v010_signal,
    f28sc_f28_share_count_dynamics_creepchg_252d_base_v011_signal,
    f28sc_f28_share_count_dynamics_creepz_252d_base_v012_signal,
    f28sc_f28_share_count_dynamics_creeprank_504d_base_v013_signal,
    f28sc_f28_share_count_dynamics_dildil_252d_base_v014_signal,
    f28sc_f28_share_count_dynamics_dilspread_252d_base_v015_signal,
    f28sc_f28_share_count_dynamics_bbintens_0d_base_v016_signal,
    f28sc_f28_share_count_dynamics_bbintens_63d_base_v017_signal,
    f28sc_f28_share_count_dynamics_bbintensz_252d_base_v018_signal,
    f28sc_f28_share_count_dynamics_ncfsignmag_252d_base_v019_signal,
    f28sc_f28_share_count_dynamics_ncfpurity_252d_base_v020_signal,
    f28sc_f28_share_count_dynamics_trendbas_252d_base_v021_signal,
    f28sc_f28_share_count_dynamics_trendwa_126d_base_v022_signal,
    f28sc_f28_share_count_dynamics_trendcurv_base_v023_signal,
    f28sc_f28_share_count_dynamics_netiss_252d_base_v024_signal,
    f28sc_f28_share_count_dynamics_netisstrend_252d_base_v025_signal,
    f28sc_f28_share_count_dynamics_dilstreak_252d_base_v026_signal,
    f28sc_f28_share_count_dynamics_bbstreak_252d_base_v027_signal,
    f28sc_f28_share_count_dynamics_streakbal_252d_base_v028_signal,
    f28sc_f28_share_count_dynamics_dildisp_504d_base_v029_signal,
    f28sc_f28_share_count_dynamics_dilxcreep_252d_base_v030_signal,
    f28sc_f28_share_count_dynamics_netyield_252d_base_v031_signal,
    f28sc_f28_share_count_dynamics_dilwaspr_63v252_base_v032_signal,
    f28sc_f28_share_count_dynamics_baswadiv_0d_base_v033_signal,
    f28sc_f28_share_count_dynamics_baswadivchg_252d_base_v034_signal,
    f28sc_f28_share_count_dynamics_diltanh_252d_base_v035_signal,
    f28sc_f28_share_count_dynamics_dilvol_252d_base_v036_signal,
    f28sc_f28_share_count_dynamics_bbconsist_504d_base_v037_signal,
    f28sc_f28_share_count_dynamics_issconsist_504d_base_v038_signal,
    f28sc_f28_share_count_dynamics_creepxdil_252d_base_v039_signal,
    f28sc_f28_share_count_dynamics_dilmultidisp_base_v040_signal,
    f28sc_f28_share_count_dynamics_issrate_252d_base_v041_signal,
    f28sc_f28_share_count_dynamics_dilstreakdepth_252d_base_v042_signal,
    f28sc_f28_share_count_dynamics_dilyoy_252d_base_v043_signal,
    f28sc_f28_share_count_dynamics_creeptrend_252d_base_v044_signal,
    f28sc_f28_share_count_dynamics_belowmax_504d_base_v045_signal,
    f28sc_f28_share_count_dynamics_abovemin_504d_base_v046_signal,
    f28sc_f28_share_count_dynamics_countrngpos_504d_base_v047_signal,
    f28sc_f28_share_count_dynamics_bbrank_504d_base_v048_signal,
    f28sc_f28_share_count_dynamics_creepdisp_252d_base_v049_signal,
    f28sc_f28_share_count_dynamics_dilminusdil_252d_base_v050_signal,
    f28sc_f28_share_count_dynamics_dilmom_126d_base_v051_signal,
    f28sc_f28_share_count_dynamics_ncfema_base_v052_signal,
    f28sc_f28_share_count_dynamics_dilasym_252d_base_v053_signal,
    f28sc_f28_share_count_dynamics_bbeff_252d_base_v054_signal,
    f28sc_f28_share_count_dynamics_trenddil_252d_base_v055_signal,
    f28sc_f28_share_count_dynamics_creepconv_252d_base_v056_signal,
    f28sc_f28_share_count_dynamics_puritymom_252d_base_v057_signal,
    f28sc_f28_share_count_dynamics_countdev_252d_base_v058_signal,
    f28sc_f28_share_count_dynamics_dilwarank_252d_base_v059_signal,
    f28sc_f28_share_count_dynamics_bbvscreep_252d_base_v060_signal,
    f28sc_f28_share_count_dynamics_dilaccel_63d_base_v061_signal,
    f28sc_f28_share_count_dynamics_dilz_126d_base_v062_signal,
    f28sc_f28_share_count_dynamics_creepvsmax_504d_base_v063_signal,
    f28sc_f28_share_count_dynamics_ncfsignpersist_252d_base_v064_signal,
    f28sc_f28_share_count_dynamics_diler_252d_base_v065_signal,
    f28sc_f28_share_count_dynamics_watobasema_base_v066_signal,
    f28sc_f28_share_count_dynamics_dilsignxcreep_base_v067_signal,
    f28sc_f28_share_count_dynamics_cumdrag_504d_base_v068_signal,
    f28sc_f28_share_count_dynamics_bbdisp_504d_base_v069_signal,
    f28sc_f28_share_count_dynamics_dilimpulse_63d_base_v070_signal,
    f28sc_f28_share_count_dynamics_dildilz_252d_base_v071_signal,
    f28sc_f28_share_count_dynamics_issvscreep_252d_base_v072_signal,
    f28sc_f28_share_count_dynamics_leangap_1260d_base_v073_signal,
    f28sc_f28_share_count_dynamics_streakbal_1260d_base_v074_signal,
    f28sc_f28_share_count_dynamics_reductqual_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SHARE_COUNT_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    sharesbas = _fund(101, base=5e8, drift=0.015, vol=0.04).rename("sharesbas")
    shareswa = _fund(102, base=4.9e8, drift=0.015, vol=0.04).rename("shareswa")
    # diluted shares: basic plus an option-overhang factor that has its own drift/path
    _overhang = _fund(103, base=1.0, drift=0.01, vol=0.06).values  # independent overhang multiplier path
    shareswadil = (shareswa * (1.0 + 0.02 + 0.06 * np.clip(_overhang / _overhang[0] - 1.0, -0.5, None))).rename("shareswadil")
    # ncfcommon oscillates between issuance (>0) and buyback (<0) quarter to quarter
    _ncf_rng = np.random.default_rng(104)
    _ncf_steps = np.repeat(_ncf_rng.normal(0.0, 1.0, n // 63 + 1), 63)[:n]
    ncfcommon = pd.Series(_ncf_steps * 5e6 + _fund(105, base=1e6, drift=0.0, vol=0.4, allow_neg=True).values,
                          name="ncfcommon")

    cols = {"sharesbas": sharesbas, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon}

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

    print("OK f28_share_count_dynamics_base_001_075_claude: %d features pass" % n_features)
