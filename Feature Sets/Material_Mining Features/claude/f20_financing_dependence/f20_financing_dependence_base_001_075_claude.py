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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (financing dependence) =====
# All inputs are SIGNED cash flows (allow_neg). We measure how much a miner
# leans on external financing (ncff) to cover an operating cash gap (ncfo<0),
# the equity-vs-debt mix of that financing (ncfcommon vs ncfdebt), and the
# self-funding gap (operating+investing vs financing).
def _f20_burn(ncfo):
    # operating cash burn magnitude (only when operating CF is negative)
    return (-ncfo).clip(lower=0)


def _f20_raise(ncff):
    # external capital raised (only when financing CF is positive)
    return ncff.clip(lower=0)


def _f20_fin_cover(ncff, ncfo, w):
    # how much of the rolling operating burn is covered by financing inflows
    burn = _rsum(_f20_burn(ncfo), w)
    fin = _rsum(_f20_raise(ncff), w)
    return fin / burn.replace(0, np.nan)


def _f20_dependence(ncff, ncfo, w):
    # external-financing reliance: |ncff| relative to |ncfo|
    a = _rsum(ncff.abs(), w)
    b = _rsum(ncfo.abs(), w)
    return a / b.replace(0, np.nan)


def _f20_eqdebt_mix(ncfcommon, ncfdebt, w):
    # equity-vs-debt financing tilt in [-1,1]: +1 all equity, -1 all debt
    eq = _rsum(ncfcommon.clip(lower=0), w)
    dt = _rsum(ncfdebt.clip(lower=0), w)
    return (eq - dt) / (eq + dt).replace(0, np.nan)


def _f20_selffund_gap(ncfo, ncfi, ncff, w):
    # self-funding gap: internal cash (op+inv) vs externally financed amount
    internal = _rsum(ncfo + ncfi, w)
    external = _rsum(ncff, w)
    return external / (internal.abs() + external.abs()).replace(0, np.nan)


# ============================================================
# external-financing reliance |ncff| vs |ncfo| over a year
def f20fd_f20_financing_dependence_relreli_252d_base_v001_signal(ncff, ncfo):
    b = _f20_dependence(ncff, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-financing reliance over half-year, z-scored vs own 252d history
def f20fd_f20_financing_dependence_relreli_126d_base_v002_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-financing reliance over 504d, percentile-ranked vs own history
def f20fd_f20_financing_dependence_relreli_504d_base_v003_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 504)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage: financing inflows / operating burn (252d)
def f20fd_f20_financing_dependence_fincover_252d_base_v004_signal(ncff, ncfo):
    b = _f20_fin_cover(ncff, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage over 126d, log-compressed
def f20fd_f20_financing_dependence_fincover_126d_base_v005_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 126)
    b = np.log1p(c.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing covers burn flag intensity: share of quarters with full coverage (504d)
def f20fd_f20_financing_dependence_covshare_504d_base_v006_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 63)
    burn = _rsum(_f20_burn(ncfo), 63)
    covered = (fin >= burn).astype(float)
    b = covered.rolling(504, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt financing mix tilt over a year
def f20fd_f20_financing_dependence_eqdebt_252d_base_v007_signal(ncfcommon, ncfdebt):
    b = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix over 126d, change vs a quarter ago (mix rotation)
def f20fd_f20_financing_dependence_eqdebtmom_126d_base_v008_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 126)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix over 504d, z-scored vs own 252d history
def f20fd_f20_financing_dependence_eqdebtz_504d_base_v009_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 504)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap: external financing vs internal cash generation (252d)
def f20fd_f20_financing_dependence_selfgap_252d_base_v010_signal(ncfo, ncfi, ncff):
    b = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap over 126d, smoothed with an EMA (persistent dependence)
def f20fd_f20_financing_dependence_selfgap_126d_base_v011_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 126)
    b = g.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap over 504d, percentile-ranked vs own history
def f20fd_f20_financing_dependence_selfgap_504d_base_v012_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 504)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence: financing inflows as share of total inflows (252d)
def f20fd_f20_financing_dependence_raiseshare_252d_base_v013_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 252)
    op_in = _rsum(ncfo.clip(lower=0), 252)
    inv_in = _rsum(ncfi.clip(lower=0), 252)
    tot = raise_ + op_in + inv_in
    b = raise_ / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence over 126d, change vs a quarter ago
def f20fd_f20_financing_dependence_raisesharemom_126d_base_v014_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 126)
    op_in = _rsum(ncfo.clip(lower=0), 126)
    inv_in = _rsum(ncfi.clip(lower=0), 126)
    share = raise_ / (raise_ + op_in + inv_in).replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net external financing flow normalized by gross cash turnover (252d)
def f20fd_f20_financing_dependence_netfinturn_252d_base_v015_signal(ncff, ncfo, ncfi):
    net_fin = _rsum(ncff, 252)
    turnover = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    b = net_fin / turnover.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity issuance intensity vs burn, de-trended as a z-score (issuance pressure)
def f20fd_f20_financing_dependence_eqburn_252d_base_v016_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    r = eq / burn.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-issuance share of total raises during burn periods only (burn-time leverage)
def f20fd_f20_financing_dependence_dtburn_252d_base_v017_signal(ncfdebt, ncfcommon, ncfo):
    burning = (ncfo < 0).astype(float)
    dt_b = _rsum(ncfdebt.clip(lower=0) * burning, 252)
    eq_b = _rsum(ncfcommon.clip(lower=0) * burning, 252)
    b = dt_b / (dt_b + eq_b).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence spread: short (126d) reliance minus long (504d) reliance
def f20fd_f20_financing_dependence_relelispr_base_v018_signal(ncff, ncfo):
    s = _f20_dependence(ncff, ncfo, 126)
    l = _f20_dependence(ncff, ncfo, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing covers burn momentum: coverage now vs a quarter ago (252d)
def f20fd_f20_financing_dependence_covmom_252d_base_v019_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 252)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence per unit of cash-flow volatility (risk-adjusted reliance)
def f20fd_f20_financing_dependence_relelivol_252d_base_v020_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    vol = _std(ncfo, 252)
    b = d / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt-financing flow normalized by total financing turnover (252d)
def f20fd_f20_financing_dependence_netdebtflow_252d_base_v021_signal(ncfdebt, ncff):
    nd = _rsum(ncfdebt, 252)
    turn = _rsum(ncff.abs(), 252)
    b = nd / turn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net equity-financing flow normalized by total financing turnover (252d)
def f20fd_f20_financing_dependence_neteqflow_252d_base_v022_signal(ncfcommon, ncff):
    ne = _rsum(ncfcommon, 252)
    turn = _rsum(ncff.abs(), 252)
    b = ne / turn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-to-investing ratio: are raises funding capex/investing? (252d)
def f20fd_f20_financing_dependence_finvsinv_252d_base_v023_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 252)
    inv_out = _rsum((-ncfi).clip(lower=0), 252)
    b = fin / inv_out.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence z-score on the raw net financing flow (252d)
def f20fd_f20_financing_dependence_netfinz_252d_base_v024_signal(ncff):
    f = _rsum(ncff, 63)
    b = _z(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap dispersion across 126/252/504 windows (term disagreement)
def f20fd_f20_financing_dependence_selfgapdisp_base_v025_signal(ncfo, ncfi, ncff):
    g1 = _f20_selffund_gap(ncfo, ncfi, ncff, 126)
    g2 = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    g3 = _f20_selffund_gap(ncfo, ncfi, ncff, 504)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance regime: fraction of last year fully dependent (raise > burn)
def f20fd_f20_financing_dependence_reliregime_252d_base_v026_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 63)
    burn = _rsum(_f20_burn(ncfo), 63)
    dep = (fin > burn).astype(float)
    b = dep.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix percentile rank vs own 504d history
def f20fd_f20_financing_dependence_eqdebtrank_252d_base_v027_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-dependence tanh-squashed change over a quarter (bounded mix shift)
def f20fd_f20_financing_dependence_raisetanh_252d_base_v028_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 252)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 252)
    share = raise_ / (raise_ + inflow).replace(0, np.nan)
    b = np.tanh(3.0 * (share - share.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing as a fraction of operating burn (financing-funded-burn, signed) 252d
def f20fd_f20_financing_dependence_netfinburn_252d_base_v029_signal(ncff, ncfo):
    nf = _rsum(ncff, 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    b = nf / (burn.abs() + nf.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance acceleration imbalance: 126d vs 252d coverage gap, ranked
def f20fd_f20_financing_dependence_covgaprank_base_v030_signal(ncff, ncfo):
    c1 = _f20_fin_cover(ncff, ncfo, 126)
    c2 = _f20_fin_cover(ncff, ncfo, 252)
    gap = c1 - c2
    b = _rank(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-financing reliance: |ncfdebt| relative to |ncfo| (252d)
def f20fd_f20_financing_dependence_debtreli_252d_base_v031_signal(ncfdebt, ncfo):
    a = _rsum(ncfdebt.abs(), 252)
    b_ = _rsum(ncfo.abs(), 252)
    b = a / b_.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-financing reliance: |ncfcommon| relative to |ncfo| (252d)
def f20fd_f20_financing_dependence_eqreli_252d_base_v032_signal(ncfcommon, ncfo):
    a = _rsum(ncfcommon.abs(), 252)
    b_ = _rsum(ncfo.abs(), 252)
    b = a / b_.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow sign streak: consecutive quarters of net positive financing (252d)
def f20fd_f20_financing_dependence_finstreak_252d_base_v033_signal(ncff):
    q = _rsum(ncff, 63)
    pos = (q > 0).astype(float)
    streak = pos.groupby((pos != pos.shift()).cumsum()).cumsum() * pos
    b = streak.rolling(252, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-funded-by-financing share: -ncfi covered by raises (252d)
def f20fd_f20_financing_dependence_invfunded_252d_base_v034_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    b = fin / (fin + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap year-over-year change (structural dependence shift)
def f20fd_f20_financing_dependence_selfgapyoy_252d_base_v035_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence interaction with burn magnitude (deep & dependent)
def f20fd_f20_financing_dependence_relixburn_252d_base_v036_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    burn_n = _z(burn, 252)
    b = d * burn_n
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix smoothed long-run bias (504d EMA)
def f20fd_f20_financing_dependence_eqdebtema_504d_base_v037_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 504)
    b = m.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-share displacement from its own slow EMA (dependence surprise)
def f20fd_f20_financing_dependence_raisedisp_252d_base_v038_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 252)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 252)
    share = raise_ / (raise_ + inflow).replace(0, np.nan)
    b = share - share.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow per unit of investing outflow (growth-funding leverage) 252d
def f20fd_f20_financing_dependence_finlevinv_252d_base_v039_signal(ncff, ncfi):
    nf = _rsum(ncff, 252)
    inv = _rsum(ncfi.abs(), 252)
    b = nf / inv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding sufficiency: does ncfo alone cover ncfi outflow? (252d)
def f20fd_f20_financing_dependence_opcoversinv_252d_base_v040_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    b = op / (op + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance entries: dependence-onset count blended with burn-cover depth
def f20fd_f20_financing_dependence_relientry_252d_base_v041_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 63)
    burn = _rsum(_f20_burn(ncfo), 63)
    dep = (fin > burn).astype(float)
    entries = ((dep == 1) & (dep.shift(1) == 0)).astype(float)
    count = entries.rolling(252, min_periods=126).sum()
    depth = (fin - burn) / (fin + burn).replace(0, np.nan)
    b = count + depth.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing mix entropy-ish balance: how evenly split equity/debt raises are (252d)
def f20fd_f20_financing_dependence_mixbalance_252d_base_v042_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    p = eq / (eq + dt).replace(0, np.nan)
    b = 1.0 - (2.0 * p - 1.0).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing volatility: dispersion of quarterly financing flows (252d)
def f20fd_f20_financing_dependence_finvol_252d_base_v043_signal(ncff):
    q = ncff.rolling(63, min_periods=21).sum()
    b = _std(q, 252) / (_mean(q.abs(), 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence ratio between debt-reliance and equity-reliance (financing tilt) 252d
def f20fd_f20_financing_dependence_dtoeqreli_252d_base_v044_signal(ncfdebt, ncfcommon):
    dt = _rsum(ncfdebt.abs(), 252)
    eq = _rsum(ncfcommon.abs(), 252)
    b = (dt - eq) / (dt + eq).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage z-scored vs own 252d history (504d)
def f20fd_f20_financing_dependence_covz_504d_base_v045_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 504)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance vs investing intensity interaction (raise-to-grow) 252d
def f20fd_f20_financing_dependence_raisetogrow_252d_base_v046_signal(ncff, ncfi, ncfo):
    raise_ = _rsum(_f20_raise(ncff), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    b = (raise_ - inv) / (burn + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow change of pace over a quarter (financing acceleration proxy)
def f20fd_f20_financing_dependence_finpace_252d_base_v047_signal(ncff):
    f = _rsum(ncff, 126)
    scale = _rsum(ncff.abs(), 252).replace(0, np.nan)
    b = (f - f.shift(63)) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap regime: fraction of year reliant on external financing (252d)
def f20fd_f20_financing_dependence_extregime_252d_base_v048_signal(ncfo, ncfi, ncff):
    internal = ncfo.rolling(63, min_periods=21).sum() + ncfi.rolling(63, min_periods=21).sum()
    ext = ncff.rolling(63, min_periods=21).sum()
    reliant = ((internal < 0) & (ext > 0)).astype(float)
    b = reliant.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-reliance z-scored vs own history (leverage-dependence extremity) 252d
def f20fd_f20_financing_dependence_debtreliz_252d_base_v049_signal(ncfdebt, ncfo):
    a = _rsum(ncfdebt.abs(), 126)
    b_ = _rsum(ncfo.abs(), 126)
    r = a / b_.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-reliance momentum over a quarter (rising equity dependence)
def f20fd_f20_financing_dependence_eqrelimom_252d_base_v050_signal(ncfcommon, ncfo):
    a = _rsum(ncfcommon.abs(), 252)
    b_ = _rsum(ncfo.abs(), 252)
    r = a / b_.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow sign-magnitude (signed sqrt of net annual financing) scaled
def f20fd_f20_financing_dependence_finsignmag_252d_base_v051_signal(ncff, ncfo):
    nf = _rsum(ncff, 252)
    scale = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    r = nf / scale
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative external dependence over the full cycle (mean of dependence) 504d
def f20fd_f20_financing_dependence_cumdep_504d_base_v052_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 126)
    b = d.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of financing that is net debt issuance vs net equity (signed) 252d
def f20fd_f20_financing_dependence_netmixtilt_252d_base_v053_signal(ncfdebt, ncfcommon, ncff):
    nd = _rsum(ncfdebt, 252)
    ne = _rsum(ncfcommon, 252)
    b = (nd - ne) / _rsum(ncff.abs(), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-cover crossing momentum: surplus delta over a quarter (252d)
def f20fd_f20_financing_dependence_covburnmom_252d_base_v054_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    surplus = (fin - burn) / (fin + burn).replace(0, np.nan)
    b = surplus - surplus.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance percentile vs its own deep 1260d history (cycle-relative)
def f20fd_f20_financing_dependence_relicyc_252d_base_v055_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    b = d.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing per gross financing (financing efficiency / direction) 504d
def f20fd_f20_financing_dependence_findir_504d_base_v056_signal(ncff):
    nf = _rsum(ncff, 504)
    gf = _rsum(ncff.abs(), 504)
    b = nf / gf.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity issuance vs investing outflow (equity funding capex) 252d
def f20fd_f20_financing_dependence_eqfundsinv_252d_base_v057_signal(ncfcommon, ncfi):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    b = eq / (eq + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt issuance vs investing outflow (debt funding capex) 252d
def f20fd_f20_financing_dependence_dtfundsinv_252d_base_v058_signal(ncfdebt, ncfi):
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    b = dt / (dt + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total external funding (equity+debt raises) vs total cash needs (burn+capex) 252d
def f20fd_f20_financing_dependence_extvsneed_252d_base_v059_signal(ncfcommon, ncfdebt, ncfo, ncfi):
    raises = _rsum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    needs = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 252)
    b = raises / needs.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence dispersion across equity/debt reliance (252d)
def f20fd_f20_financing_dependence_relidisp_252d_base_v060_signal(ncfcommon, ncfdebt, ncfo):
    base = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    eq = _rsum(ncfcommon.abs(), 252) / base
    dt = _rsum(ncfdebt.abs(), 252) / base
    b = pd.concat([eq, dt], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage minus 1, tanh-bounded (surplus/deficit) 126d
def f20fd_f20_financing_dependence_covexcess_126d_base_v061_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 126)
    b = np.tanh(c - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap interaction with mix-shift momentum (dependent AND rotating mix)
def f20fd_f20_financing_dependence_gapxmix_252d_base_v062_signal(ncfo, ncfi, ncff, ncfcommon, ncfdebt):
    gap = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    mix = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    mix_mom = mix - mix.shift(63)
    b = gap * mix_mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow vs prior-year financing (financing persistence) 252d
def f20fd_f20_financing_dependence_finpersist_252d_base_v063_signal(ncff):
    cur = _rsum(ncff, 252)
    prior = _rsum(ncff, 252).shift(252)
    b = (cur - prior) / (cur.abs() + prior.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash self-sufficiency vs external pull (signed gap, 504d)
def f20fd_f20_financing_dependence_opvsext_504d_base_v064_signal(ncfo, ncff):
    op = _rsum(ncfo, 504)
    ext = _rsum(_f20_raise(ncff), 504)
    b = op / (op.abs() + ext).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-equity reliance momentum: mix tilt change over half-year (126d)
def f20fd_f20_financing_dependence_tiltmom_126d_base_v065_signal(ncfdebt, ncfcommon):
    dt = _rsum(ncfdebt.abs(), 126)
    eq = _rsum(ncfcommon.abs(), 126)
    tilt = (dt - eq) / (dt + eq).replace(0, np.nan)
    b = tilt - tilt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise frequency: count of net-raising quarters over a year (252d)
def f20fd_f20_financing_dependence_raisefreq_252d_base_v066_signal(ncff):
    q = _rsum(ncff, 63)
    raising = (q > 0).astype(float)
    b = raising.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance smoothed level (persistent dependence, EMA on dependence)
def f20fd_f20_financing_dependence_reliema_252d_base_v067_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 126)
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing direction vs operating direction agreement (both-negative stress)
def f20fd_f20_financing_dependence_dirgree_252d_base_v068_signal(ncff, ncfo):
    f = _rsum(ncff, 252)
    o = _rsum(ncfo, 252)
    b = np.sign(f) * np.sign(o) * (f.abs() / (f.abs() + o.abs()).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt raise ratio log scaled (issuance preference) 252d
def f20fd_f20_financing_dependence_eqdtlog_252d_base_v069_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    b = np.log((eq + 1.0) / (dt + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total cash-flow turnover share that is financing (financing footprint) 252d
def f20fd_f20_financing_dependence_finfootprint_252d_base_v070_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 252)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    b = fin / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap rank vs cycle history, sign-flipped (dependence severity) 252d
def f20fd_f20_financing_dependence_gapsev_252d_base_v071_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    b = -(g.rolling(1260, min_periods=252).rank(pct=True) - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-cover surplus interaction with mix balance (cushion x diversity)
def f20fd_f20_financing_dependence_coverdiv_252d_base_v072_signal(ncff, ncfo, ncfcommon, ncfdebt):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    surplus = (fin - burn) / (fin + burn).replace(0, np.nan)
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    p = eq / (eq + dt).replace(0, np.nan)
    div = 1.0 - (2.0 * p - 1.0).abs()
    b = surplus * div
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net external financing scaled by investing intensity, z-scored (growth-fund z)
def f20fd_f20_financing_dependence_growfundz_252d_base_v073_signal(ncff, ncfi):
    nf = _rsum(ncff, 126)
    inv = _rsum(ncfi.abs(), 126)
    r = nf / inv.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance breadth: how many of equity/debt/total reliance exceed median
def f20fd_f20_financing_dependence_relibreadth_252d_base_v074_signal(ncfcommon, ncfdebt, ncff, ncfo):
    base = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    eq = _rsum(ncfcommon.abs(), 252) / base
    dt = _rsum(ncfdebt.abs(), 252) / base
    tot = _rsum(ncff.abs(), 252) / base
    eq_hi = (eq > eq.rolling(504, min_periods=126).median()).astype(float)
    dt_hi = (dt > dt.rolling(504, min_periods=126).median()).astype(float)
    tot_hi = (tot > tot.rolling(504, min_periods=126).median()).astype(float)
    breadth = (eq_hi + dt_hi + tot_hi) / 3.0
    b = breadth + 0.2 * _z(tot, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite self-funding-gap momentum balance (improving vs worsening) 504d
def f20fd_f20_financing_dependence_gapbalance_504d_base_v075_signal(ncfo, ncfi, ncff):
    internal = _rsum(ncfo + ncfi, 504)
    external = _rsum(_f20_raise(ncff), 504)
    bal = (internal - external) / (internal.abs() + external).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20fd_f20_financing_dependence_relreli_252d_base_v001_signal,
    f20fd_f20_financing_dependence_relreli_126d_base_v002_signal,
    f20fd_f20_financing_dependence_relreli_504d_base_v003_signal,
    f20fd_f20_financing_dependence_fincover_252d_base_v004_signal,
    f20fd_f20_financing_dependence_fincover_126d_base_v005_signal,
    f20fd_f20_financing_dependence_covshare_504d_base_v006_signal,
    f20fd_f20_financing_dependence_eqdebt_252d_base_v007_signal,
    f20fd_f20_financing_dependence_eqdebtmom_126d_base_v008_signal,
    f20fd_f20_financing_dependence_eqdebtz_504d_base_v009_signal,
    f20fd_f20_financing_dependence_selfgap_252d_base_v010_signal,
    f20fd_f20_financing_dependence_selfgap_126d_base_v011_signal,
    f20fd_f20_financing_dependence_selfgap_504d_base_v012_signal,
    f20fd_f20_financing_dependence_raiseshare_252d_base_v013_signal,
    f20fd_f20_financing_dependence_raisesharemom_126d_base_v014_signal,
    f20fd_f20_financing_dependence_netfinturn_252d_base_v015_signal,
    f20fd_f20_financing_dependence_eqburn_252d_base_v016_signal,
    f20fd_f20_financing_dependence_dtburn_252d_base_v017_signal,
    f20fd_f20_financing_dependence_relelispr_base_v018_signal,
    f20fd_f20_financing_dependence_covmom_252d_base_v019_signal,
    f20fd_f20_financing_dependence_relelivol_252d_base_v020_signal,
    f20fd_f20_financing_dependence_netdebtflow_252d_base_v021_signal,
    f20fd_f20_financing_dependence_neteqflow_252d_base_v022_signal,
    f20fd_f20_financing_dependence_finvsinv_252d_base_v023_signal,
    f20fd_f20_financing_dependence_netfinz_252d_base_v024_signal,
    f20fd_f20_financing_dependence_selfgapdisp_base_v025_signal,
    f20fd_f20_financing_dependence_reliregime_252d_base_v026_signal,
    f20fd_f20_financing_dependence_eqdebtrank_252d_base_v027_signal,
    f20fd_f20_financing_dependence_raisetanh_252d_base_v028_signal,
    f20fd_f20_financing_dependence_netfinburn_252d_base_v029_signal,
    f20fd_f20_financing_dependence_covgaprank_base_v030_signal,
    f20fd_f20_financing_dependence_debtreli_252d_base_v031_signal,
    f20fd_f20_financing_dependence_eqreli_252d_base_v032_signal,
    f20fd_f20_financing_dependence_finstreak_252d_base_v033_signal,
    f20fd_f20_financing_dependence_invfunded_252d_base_v034_signal,
    f20fd_f20_financing_dependence_selfgapyoy_252d_base_v035_signal,
    f20fd_f20_financing_dependence_relixburn_252d_base_v036_signal,
    f20fd_f20_financing_dependence_eqdebtema_504d_base_v037_signal,
    f20fd_f20_financing_dependence_raisedisp_252d_base_v038_signal,
    f20fd_f20_financing_dependence_finlevinv_252d_base_v039_signal,
    f20fd_f20_financing_dependence_opcoversinv_252d_base_v040_signal,
    f20fd_f20_financing_dependence_relientry_252d_base_v041_signal,
    f20fd_f20_financing_dependence_mixbalance_252d_base_v042_signal,
    f20fd_f20_financing_dependence_finvol_252d_base_v043_signal,
    f20fd_f20_financing_dependence_dtoeqreli_252d_base_v044_signal,
    f20fd_f20_financing_dependence_covz_504d_base_v045_signal,
    f20fd_f20_financing_dependence_raisetogrow_252d_base_v046_signal,
    f20fd_f20_financing_dependence_finpace_252d_base_v047_signal,
    f20fd_f20_financing_dependence_extregime_252d_base_v048_signal,
    f20fd_f20_financing_dependence_debtreliz_252d_base_v049_signal,
    f20fd_f20_financing_dependence_eqrelimom_252d_base_v050_signal,
    f20fd_f20_financing_dependence_finsignmag_252d_base_v051_signal,
    f20fd_f20_financing_dependence_cumdep_504d_base_v052_signal,
    f20fd_f20_financing_dependence_netmixtilt_252d_base_v053_signal,
    f20fd_f20_financing_dependence_covburnmom_252d_base_v054_signal,
    f20fd_f20_financing_dependence_relicyc_252d_base_v055_signal,
    f20fd_f20_financing_dependence_findir_504d_base_v056_signal,
    f20fd_f20_financing_dependence_eqfundsinv_252d_base_v057_signal,
    f20fd_f20_financing_dependence_dtfundsinv_252d_base_v058_signal,
    f20fd_f20_financing_dependence_extvsneed_252d_base_v059_signal,
    f20fd_f20_financing_dependence_relidisp_252d_base_v060_signal,
    f20fd_f20_financing_dependence_covexcess_126d_base_v061_signal,
    f20fd_f20_financing_dependence_gapxmix_252d_base_v062_signal,
    f20fd_f20_financing_dependence_finpersist_252d_base_v063_signal,
    f20fd_f20_financing_dependence_opvsext_504d_base_v064_signal,
    f20fd_f20_financing_dependence_tiltmom_126d_base_v065_signal,
    f20fd_f20_financing_dependence_raisefreq_252d_base_v066_signal,
    f20fd_f20_financing_dependence_reliema_252d_base_v067_signal,
    f20fd_f20_financing_dependence_dirgree_252d_base_v068_signal,
    f20fd_f20_financing_dependence_eqdtlog_252d_base_v069_signal,
    f20fd_f20_financing_dependence_finfootprint_252d_base_v070_signal,
    f20fd_f20_financing_dependence_gapsev_252d_base_v071_signal,
    f20fd_f20_financing_dependence_coverdiv_252d_base_v072_signal,
    f20fd_f20_financing_dependence_growfundz_252d_base_v073_signal,
    f20fd_f20_financing_dependence_relibreadth_252d_base_v074_signal,
    f20fd_f20_financing_dependence_gapbalance_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_FINANCING_DEPENDENCE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    # Signed cyclical cash flows (allow_neg semantics): detrend a _fund cyclical
    # walk into a zero-centered oscillation, then shift by an economic center so
    # each flow genuinely spans positive (raises / operating surplus) and negative
    # (repayment / operating burn) regimes across the cycle.
    def _flow(seed, center, amp=1.0, vol=0.09):
        f = _fund(seed, base=1e8, drift=0.0, vol=vol, allow_neg=False)
        osc = f - f.rolling(189, min_periods=20).mean()
        osc = osc.bfill()
        return center + amp * osc

    ncff = _flow(201, 8e6, 1.0).rename("ncff")
    ncfcommon = _flow(202, 0.0, 1.1).rename("ncfcommon")
    ncfdebt = _flow(203, 4e6, 0.9).rename("ncfdebt")
    ncfo = _flow(204, -6e6, 1.2).rename("ncfo")
    ncfi = _flow(205, -10e6, 1.3).rename("ncfi")

    cols = {"ncff": ncff, "ncfcommon": ncfcommon, "ncfdebt": ncfdebt,
            "ncfo": ncfo, "ncfi": ncfi}

    fundamental_cols = set(cols.keys())
    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        ins = meta["inputs"]
        assert any(c in fundamental_cols for c in ins), "no fundamental input: %s" % name
        fn = meta["func"]
        args = [cols[c] for c in ins]
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

    print("OK f20_financing_dependence_base_001_075_claude: %d features pass" % n_features)
