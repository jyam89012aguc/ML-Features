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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _dlog(s, k):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(k).replace(0, np.nan))


# ===== f22 operating-leverage primitives (revenue-vs-profit GROWTH sensitivity only) =====
# NOTE: on real data opinc == gp - opex exactly, so incremental-margin / contribution
# constructs collapse into one another.  These primitives are deliberately kept few; the
# 150 features diversify by FACET (rank / dispersion / asymmetry / conditional / streak /
# elasticity-of-magnitudes / break-even-distance) rather than by re-windowing the same ratio.
def _f22ol_dol(opinc, revenue, k):
    gr = revenue.pct_change(k)
    go = opinc.pct_change(k)
    return go / gr.replace(0, np.nan)


def _f22ol_dol_ebit(ebit, revenue, k):
    gr = revenue.pct_change(k)
    ge = ebit.pct_change(k)
    return ge / gr.replace(0, np.nan)


def _f22ol_incmargin(opinc, revenue, k):
    do = opinc - opinc.shift(k)
    dr = revenue - revenue.shift(k)
    return do / dr.replace(0, np.nan)


def _f22ol_incgm(gp, revenue, k):
    dg = gp - gp.shift(k)
    dr = revenue - revenue.shift(k)
    return dg / dr.replace(0, np.nan)


def _f22ol_spread_op(opinc, revenue, k):
    return _dlog(opinc, k) - _dlog(revenue, k)


def _f22ol_spread_gp(gp, revenue, k):
    return _dlog(gp, k) - _dlog(revenue, k)


def _f22ol_spread_ebit(ebit, revenue, k):
    return _dlog(ebit, k) - _dlog(revenue, k)


def _f22ol_opexscale(opex, revenue, k):
    r = opex / revenue.replace(0, np.nan)
    return -(r - r.shift(k))


def _f22ol_gpscale(gp, revenue, k):
    r = gp / revenue.replace(0, np.nan)
    return r - r.shift(k)


def _f22ol_fixedabsorb(opinc, opex, k):
    do = opinc - opinc.shift(k)
    dx = opex - opex.shift(k)
    return do / dx.replace(0, np.nan)


def _f22ol_opexelas(opex, revenue, k):
    return _dlog(opex, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpelas(gp, revenue, k):
    return _dlog(gp, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_ebitelas(ebit, revenue, k):
    return _dlog(ebit, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_breakeven_rev(opex, gp, revenue, k):
    # break-even revenue = fixed-ish opex / contribution-margin ratio (gp/revenue);
    # margin-of-safety = (revenue - break-even-revenue) / revenue, a DOL construct
    cm = (gp / revenue.replace(0, np.nan)).rolling(k, min_periods=max(2, k // 2)).mean()
    be = opex / cm.replace(0, np.nan)
    return (revenue - be) / revenue.replace(0, np.nan)


def _f22ol_updown_incm(opinc, revenue, k):
    # conditional incremental margin asymmetry: incremental op margin earned in
    # FAST-growth windows minus that in SLOW-growth windows (lever asymmetry), split
    # at the rolling-median revenue-growth so both buckets are populated each window.
    im = _f22ol_incmargin(opinc, revenue, k)
    g = _dlog(revenue, k)
    med = g.rolling(252, min_periods=63).median()
    fast = im.where(g >= med)
    slow = im.where(g < med)
    return (fast.rolling(252, min_periods=63).mean()
            - slow.rolling(252, min_periods=63).mean())


# ============================================================
# degree of operating leverage opinc/revenue 63d
def f22ol_f22_operating_leverage_dolop_63d_base_v001_signal(opinc, revenue):
    b = _f22ol_dol(opinc, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage opinc/revenue 126d
def f22ol_f22_operating_leverage_dolop_126d_base_v002_signal(opinc, revenue):
    b = _f22ol_dol(opinc, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage opinc/revenue 252d
def f22ol_f22_operating_leverage_dolop_252d_base_v003_signal(opinc, revenue):
    b = _f22ol_dol(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage opinc/revenue 504d
def f22ol_f22_operating_leverage_dolop_504d_base_v004_signal(opinc, revenue):
    b = _f22ol_dol(opinc, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL via ebit minus DOL via opinc (which line amplifies more) 126d
def f22ol_f22_operating_leverage_dolebitgap_126d_base_v005_signal(ebit, opinc, revenue):
    de = _f22ol_dol_ebit(ebit, revenue, 126)
    do = _f22ol_dol(opinc, revenue, 126)
    b = np.tanh(de / 5.0) - np.tanh(do / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL via ebit, bounded 252d (raw amplification of ebit to revenue)
def f22ol_f22_operating_leverage_dolebit_252d_base_v006_signal(ebit, revenue):
    b = np.tanh(_f22ol_dol_ebit(ebit, revenue, 252) / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL via ebit, bounded 504d
def f22ol_f22_operating_leverage_dolebit_504d_base_v007_signal(ebit, revenue):
    b = np.tanh(_f22ol_dol_ebit(ebit, revenue, 504) / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored DOL 126d
def f22ol_f22_operating_leverage_dolopz_126d_base_v008_signal(opinc, revenue):
    b = _z(_f22ol_dol(opinc, revenue, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored DOL 252d
def f22ol_f22_operating_leverage_dolopz_252d_base_v009_signal(opinc, revenue):
    b = _z(_f22ol_dol(opinc, revenue, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of DOL estimate 126d
def f22ol_f22_operating_leverage_dolopvol_126d_base_v010_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 63)
    b = d.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL inter-quartile dispersion over a year (robust lever uncertainty)
def f22ol_f22_operating_leverage_doliqr_252d_base_v011_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 63)
    q3 = d.rolling(252, min_periods=126).quantile(0.75)
    q1 = d.rolling(252, min_periods=126).quantile(0.25)
    b = q3 - q1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DOL 252d
def f22ol_f22_operating_leverage_doloprank_252d_base_v012_signal(opinc, revenue):
    b = _rank(_f22ol_dol(opinc, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of DOL 504d
def f22ol_f22_operating_leverage_doloprank_504d_base_v013_signal(opinc, revenue):
    b = _rank(_f22ol_dol(opinc, revenue, 504), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year with amplifying |DOL|>1 (lever-active regime)
def f22ol_f22_operating_leverage_dolampstreak_252d_base_v014_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 63)
    amp = (d.abs() > 1.0).astype(float)
    b = amp.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL skew: asymmetry of the lever distribution over a year
def f22ol_f22_operating_leverage_dolskew_252d_base_v015_signal(opinc, revenue):
    d = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0)
    b = d.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of ebit-DOL
def f22ol_f22_operating_leverage_dolebitvol_252d_base_v016_signal(ebit, revenue):
    d = np.tanh(_f22ol_dol_ebit(ebit, revenue, 63) / 5.0)
    b = d.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded DOL times revenue growth (lever loaded by the size of the revenue move)
def f22ol_f22_operating_leverage_dolXgrow_252d_base_v017_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 252)
    g = _dlog(revenue, 252)
    b = np.tanh(d / 5.0) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin 63d
def f22ol_f22_operating_leverage_incmop_63d_base_v018_signal(opinc, revenue):
    b = _f22ol_incmargin(opinc, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin 126d
def f22ol_f22_operating_leverage_incmop_126d_base_v019_signal(opinc, revenue):
    b = _f22ol_incmargin(opinc, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin 252d
def f22ol_f22_operating_leverage_incmop_252d_base_v020_signal(opinc, revenue):
    b = _f22ol_incmargin(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin 504d
def f22ol_f22_operating_leverage_incmop_504d_base_v021_signal(opinc, revenue):
    b = _f22ol_incmargin(opinc, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z incremental op margin 252d
def f22ol_f22_operating_leverage_incmopz_252d_base_v022_signal(opinc, revenue):
    b = _z(_f22ol_incmargin(opinc, revenue, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank incremental op margin
def f22ol_f22_operating_leverage_incmoprank_252d_base_v023_signal(opinc, revenue):
    b = _rank(_f22ol_incmargin(opinc, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of incremental op margin
def f22ol_f22_operating_leverage_incmopvol_252d_base_v024_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 63)
    b = im.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conditional incremental op margin: up-window minus down-window lever asymmetry
def f22ol_f22_operating_leverage_incmop_asym_252d_base_v025_signal(opinc, revenue):
    b = _f22ol_updown_incm(opinc, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin 63d
def f22ol_f22_operating_leverage_incmgp_63d_base_v026_signal(gp, revenue):
    b = _f22ol_incgm(gp, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin 126d
def f22ol_f22_operating_leverage_incmgp_126d_base_v027_signal(gp, revenue):
    b = _f22ol_incgm(gp, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin 252d
def f22ol_f22_operating_leverage_incmgp_252d_base_v028_signal(gp, revenue):
    b = _f22ol_incgm(gp, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin 504d
def f22ol_f22_operating_leverage_incmgp_504d_base_v029_signal(gp, revenue):
    b = _f22ol_incgm(gp, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank incremental gross margin
def f22ol_f22_operating_leverage_incmgprank_252d_base_v030_signal(gp, revenue):
    b = _rank(_f22ol_incgm(gp, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of incremental gross margin
def f22ol_f22_operating_leverage_incmgpvol_252d_base_v031_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 63)
    b = im.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex operating leverage: ratio of gp-growth magnitude to opex-growth magnitude 63d
# (how much gross profit the cost base buys -- a contribution-style lever, NOT rev-opex)
def f22ol_f22_operating_leverage_gpopxlev_63d_base_v032_signal(gp, opex):
    dg = _dlog(gp, 63)
    dx = _dlog(opex, 63)
    b = dg / dx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex operating leverage gp-growth / opex-growth 126d
def f22ol_f22_operating_leverage_gpopxlev_126d_base_v033_signal(gp, opex):
    dg = _dlog(gp, 126)
    dx = _dlog(opex, 126)
    b = dg / dx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-opex contribution lever dispersion across 63/126/252 windows
# (multi-horizon disagreement of the cost-base lever; not affine to the level lever)
def f22ol_f22_operating_leverage_gpopxlevdisp_252d_base_v034_signal(gp, opex):
    l1 = np.tanh((_dlog(gp, 63) / _dlog(opex, 63).replace(0, np.nan)) / 3.0)
    l2 = np.tanh((_dlog(gp, 126) / _dlog(opex, 126).replace(0, np.nan)) / 3.0)
    l3 = np.tanh((_dlog(gp, 252) / _dlog(opex, 252).replace(0, np.nan)) / 3.0)
    b = pd.concat([l1, l2, l3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex operating leverage, bounded & z-scored 252d
def f22ol_f22_operating_leverage_gpopxlevz_252d_base_v035_signal(gp, opex):
    dg = _dlog(gp, 252)
    dx = _dlog(opex, 252)
    lev = np.tanh((dg / dx.replace(0, np.nan)) / 3.0)
    b = _z(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin dispersion across 63/126/252 windows
def f22ol_f22_operating_leverage_incmgpdisp_252d_base_v036_signal(gp, revenue):
    m1 = _f22ol_incgm(gp, revenue, 63)
    m2 = _f22ol_incgm(gp, revenue, 126)
    m3 = _f22ol_incgm(gp, revenue, 252)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex elasticity to revenue, ranked 252d (cost-base sensitivity percentile)
def f22ol_f22_operating_leverage_opxelasrank_252d_base_v037_signal(opex, revenue):
    e = np.tanh(_f22ol_opexelas(opex, revenue, 252) / 3.0)
    b = _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-operating incremental flow-through ratio 252d
# (what share of incremental gross profit survives to op income -- opex drag, as RATIO)
def f22ol_f22_operating_leverage_flowthru_252d_base_v038_signal(gp, opinc):
    do = opinc - opinc.shift(252)
    dg = gp - gp.shift(252)
    b = do / dg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-growth minus revenue-growth 63d
def f22ol_f22_operating_leverage_sprop_63d_base_v039_signal(opinc, revenue):
    b = _f22ol_spread_op(opinc, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-growth minus revenue-growth 126d
def f22ol_f22_operating_leverage_sprop_126d_base_v040_signal(opinc, revenue):
    b = _f22ol_spread_op(opinc, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-growth minus revenue-growth 252d
def f22ol_f22_operating_leverage_sprop_252d_base_v041_signal(opinc, revenue):
    b = _f22ol_spread_op(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-growth minus revenue-growth 504d
def f22ol_f22_operating_leverage_sprop_504d_base_v042_signal(opinc, revenue):
    b = _f22ol_spread_op(opinc, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth minus revenue-growth 63d
def f22ol_f22_operating_leverage_sprgp_63d_base_v043_signal(gp, revenue):
    b = _f22ol_spread_gp(gp, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth minus revenue-growth 126d
def f22ol_f22_operating_leverage_sprgp_126d_base_v044_signal(gp, revenue):
    b = _f22ol_spread_gp(gp, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth minus revenue-growth 252d
def f22ol_f22_operating_leverage_sprgp_252d_base_v045_signal(gp, revenue):
    b = _f22ol_spread_gp(gp, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth minus revenue-growth 504d
def f22ol_f22_operating_leverage_sprgp_504d_base_v046_signal(gp, revenue):
    b = _f22ol_spread_gp(gp, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-growth minus revenue-growth 126d
def f22ol_f22_operating_leverage_sprebit_126d_base_v047_signal(ebit, revenue):
    b = _f22ol_spread_ebit(ebit, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-growth minus revenue-growth 252d
def f22ol_f22_operating_leverage_sprebit_252d_base_v048_signal(ebit, revenue):
    b = _f22ol_spread_ebit(ebit, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus opex-growth 126d (cost-scale spread)
def f22ol_f22_operating_leverage_spropx_126d_base_v049_signal(opex, revenue):
    b = _dlog(revenue, 126) - _dlog(opex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus opex-growth 252d
def f22ol_f22_operating_leverage_spropx_252d_base_v050_signal(opex, revenue):
    b = _dlog(revenue, 252) - _dlog(opex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of gp spread
def f22ol_f22_operating_leverage_sprgprank_252d_base_v051_signal(gp, revenue):
    b = _rank(_f22ol_spread_gp(gp, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of ebit spread
def f22ol_f22_operating_leverage_sprebitrank_252d_base_v052_signal(ebit, revenue):
    b = _rank(_f22ol_spread_ebit(ebit, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of op spread
def f22ol_f22_operating_leverage_spropsignmag_252d_base_v053_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 252)
    b = np.sign(s) * (s.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net spread streak: (op-outgrows-rev minus rev-outgrows-op) fraction over a year
def f22ol_f22_operating_leverage_spropposstreak_252d_base_v054_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 63)
    net = np.sign(s)
    b = net.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-spread net-sign streak over a year
def f22ol_f22_operating_leverage_sprgpposstreak_252d_base_v055_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 63)
    net = np.sign(s)
    b = net.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread dispersion across opinc/gp/ebit lines (leverage disagreement)
def f22ol_f22_operating_leverage_sprdisp_lines_252d_base_v056_signal(opinc, gp, ebit, revenue):
    a = _f22ol_spread_op(opinc, revenue, 252)
    c = _f22ol_spread_gp(gp, revenue, 252)
    e = _f22ol_spread_ebit(ebit, revenue, 252)
    b = pd.concat([a, c, e], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# below-the-gross-line drag share: opex growth relative to gp growth (cost-line
# absorption ratio); >1 means opex outpaced gross profit -- leverage eroding
def f22ol_f22_operating_leverage_sprdrag_gpop_252d_base_v057_signal(gp, opex):
    dx = _dlog(opex, 252)
    dg = _dlog(gp, 252)
    ratio = dx / dg.replace(0, np.nan)
    b = np.tanh((ratio - 1.0) / 2.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op spread times revenue growth (lever loaded by revenue move)
def f22ol_f22_operating_leverage_sprXgrow_op_252d_base_v058_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 252)
    g = _dlog(revenue, 252)
    b = s * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of op spread
def f22ol_f22_operating_leverage_spropvol_252d_base_v059_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 63)
    b = s.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of opex absorption (opex/revenue falling = scale absorption)
def f22ol_f22_operating_leverage_opxabsrank_252d_base_v060_signal(opex, revenue):
    b = _rank(_f22ol_opexscale(opex, revenue, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of opex absorption
def f22ol_f22_operating_leverage_opxabsvol_252d_base_v061_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 63)
    b = s.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net opex-absorption streak (sign-balanced) over a year
def f22ol_f22_operating_leverage_opxabsstreak_252d_base_v062_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 63)
    b = np.sign(s).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of gp/revenue scale change
def f22ol_f22_operating_leverage_gpsclvol_252d_base_v063_signal(gp, revenue):
    s = _f22ol_gpscale(gp, revenue, 63)
    b = s.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-of-safety: distance of revenue above contribution break-even revenue 252d
def f22ol_f22_operating_leverage_mos_be_252d_base_v064_signal(opex, gp, revenue):
    b = _f22ol_breakeven_rev(opex, gp, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in margin-of-safety (break-even cushion building/eroding) 252d
def f22ol_f22_operating_leverage_mos_be_chg_252d_base_v065_signal(opex, gp, revenue):
    mos = _f22ol_breakeven_rev(opex, gp, revenue, 252)
    b = mos - mos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-contribution safety buffer change z-scored 252d
def f22ol_f22_operating_leverage_safetygp_z_252d_base_v066_signal(gp, opex):
    buf = (gp - opex) / gp.replace(0, np.nan)
    ch = buf - buf.shift(252)
    b = _z(ch, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# break-even DISTANCE magnitude: |opinc|/revenue scaled by sign-of-leverage (how far from zero) 252d
# (continuous distance to operating break-even, NOT a posfrac count -> distinct from f24)
def f22ol_f22_operating_leverage_bedist_op_252d_base_v067_signal(opinc, revenue):
    d = opinc / revenue.replace(0, np.nan)
    sm = np.sign(d) * (d.abs() ** 0.5)
    b = sm.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# break-even DISTANCE magnitude via ebit, smoothed 252d (continuous, not a count)
def f22ol_f22_operating_leverage_bedist_ebit_252d_base_v068_signal(ebit, revenue):
    d = ebit / revenue.replace(0, np.nan)
    sm = np.sign(d) * (d.abs() ** 0.5)
    b = sm.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost lever d-opinc/d-opex 126d
def f22ol_f22_operating_leverage_fixlev_126d_base_v069_signal(opinc, opex):
    b = _f22ol_fixedabsorb(opinc, opex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost lever d-opinc/d-opex 252d
def f22ol_f22_operating_leverage_fixlev_252d_base_v070_signal(opinc, opex):
    b = _f22ol_fixedabsorb(opinc, opex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z fixed-cost lever
def f22ol_f22_operating_leverage_fixlevz_252d_base_v071_signal(opinc, opex):
    b = _z(_f22ol_fixedabsorb(opinc, opex, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of fixed-cost lever
def f22ol_f22_operating_leverage_fixlevvol_252d_base_v072_signal(opinc, opex):
    s = _f22ol_fixedabsorb(opinc, opex, 63)
    b = s.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit elasticity to revenue, bounded 126d (distinct from raw DOL by bounding+window)
def f22ol_f22_operating_leverage_ebitelas_126d_base_v073_signal(ebit, revenue):
    b = np.tanh(_f22ol_ebitelas(ebit, revenue, 126) / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity spread: ebit-elasticity minus gp-elasticity (below-gross amplification) 252d
def f22ol_f22_operating_leverage_elasspr_ebitgp_252d_base_v074_signal(ebit, gp, revenue):
    e = np.tanh(_f22ol_ebitelas(ebit, revenue, 252) / 3.0)
    c = np.tanh(_f22ol_gpelas(gp, revenue, 252) / 3.0)
    b = e - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity dispersion across opex/gp/ebit lines (multi-line lever disagreement)
def f22ol_f22_operating_leverage_elasdisp_252d_base_v075_signal(opex, gp, ebit, revenue):
    a = np.tanh(_f22ol_opexelas(opex, revenue, 252) / 3.0)
    c = np.tanh(_f22ol_gpelas(gp, revenue, 252) / 3.0)
    e = np.tanh(_f22ol_ebitelas(ebit, revenue, 252) / 3.0)
    b = pd.concat([a, c, e], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ol_f22_operating_leverage_dolop_63d_base_v001_signal,
    f22ol_f22_operating_leverage_dolop_126d_base_v002_signal,
    f22ol_f22_operating_leverage_dolop_252d_base_v003_signal,
    f22ol_f22_operating_leverage_dolop_504d_base_v004_signal,
    f22ol_f22_operating_leverage_dolebitgap_126d_base_v005_signal,
    f22ol_f22_operating_leverage_dolebit_252d_base_v006_signal,
    f22ol_f22_operating_leverage_dolebit_504d_base_v007_signal,
    f22ol_f22_operating_leverage_dolopz_126d_base_v008_signal,
    f22ol_f22_operating_leverage_dolopz_252d_base_v009_signal,
    f22ol_f22_operating_leverage_dolopvol_126d_base_v010_signal,
    f22ol_f22_operating_leverage_doliqr_252d_base_v011_signal,
    f22ol_f22_operating_leverage_doloprank_252d_base_v012_signal,
    f22ol_f22_operating_leverage_doloprank_504d_base_v013_signal,
    f22ol_f22_operating_leverage_dolampstreak_252d_base_v014_signal,
    f22ol_f22_operating_leverage_dolskew_252d_base_v015_signal,
    f22ol_f22_operating_leverage_dolebitvol_252d_base_v016_signal,
    f22ol_f22_operating_leverage_dolXgrow_252d_base_v017_signal,
    f22ol_f22_operating_leverage_incmop_63d_base_v018_signal,
    f22ol_f22_operating_leverage_incmop_126d_base_v019_signal,
    f22ol_f22_operating_leverage_incmop_252d_base_v020_signal,
    f22ol_f22_operating_leverage_incmop_504d_base_v021_signal,
    f22ol_f22_operating_leverage_incmopz_252d_base_v022_signal,
    f22ol_f22_operating_leverage_incmoprank_252d_base_v023_signal,
    f22ol_f22_operating_leverage_incmopvol_252d_base_v024_signal,
    f22ol_f22_operating_leverage_incmop_asym_252d_base_v025_signal,
    f22ol_f22_operating_leverage_incmgp_63d_base_v026_signal,
    f22ol_f22_operating_leverage_incmgp_126d_base_v027_signal,
    f22ol_f22_operating_leverage_incmgp_252d_base_v028_signal,
    f22ol_f22_operating_leverage_incmgp_504d_base_v029_signal,
    f22ol_f22_operating_leverage_incmgprank_252d_base_v030_signal,
    f22ol_f22_operating_leverage_incmgpvol_252d_base_v031_signal,
    f22ol_f22_operating_leverage_gpopxlev_63d_base_v032_signal,
    f22ol_f22_operating_leverage_gpopxlev_126d_base_v033_signal,
    f22ol_f22_operating_leverage_gpopxlevdisp_252d_base_v034_signal,
    f22ol_f22_operating_leverage_gpopxlevz_252d_base_v035_signal,
    f22ol_f22_operating_leverage_incmgpdisp_252d_base_v036_signal,
    f22ol_f22_operating_leverage_opxelasrank_252d_base_v037_signal,
    f22ol_f22_operating_leverage_flowthru_252d_base_v038_signal,
    f22ol_f22_operating_leverage_sprop_63d_base_v039_signal,
    f22ol_f22_operating_leverage_sprop_126d_base_v040_signal,
    f22ol_f22_operating_leverage_sprop_252d_base_v041_signal,
    f22ol_f22_operating_leverage_sprop_504d_base_v042_signal,
    f22ol_f22_operating_leverage_sprgp_63d_base_v043_signal,
    f22ol_f22_operating_leverage_sprgp_126d_base_v044_signal,
    f22ol_f22_operating_leverage_sprgp_252d_base_v045_signal,
    f22ol_f22_operating_leverage_sprgp_504d_base_v046_signal,
    f22ol_f22_operating_leverage_sprebit_126d_base_v047_signal,
    f22ol_f22_operating_leverage_sprebit_252d_base_v048_signal,
    f22ol_f22_operating_leverage_spropx_126d_base_v049_signal,
    f22ol_f22_operating_leverage_spropx_252d_base_v050_signal,
    f22ol_f22_operating_leverage_sprgprank_252d_base_v051_signal,
    f22ol_f22_operating_leverage_sprebitrank_252d_base_v052_signal,
    f22ol_f22_operating_leverage_spropsignmag_252d_base_v053_signal,
    f22ol_f22_operating_leverage_spropposstreak_252d_base_v054_signal,
    f22ol_f22_operating_leverage_sprgpposstreak_252d_base_v055_signal,
    f22ol_f22_operating_leverage_sprdisp_lines_252d_base_v056_signal,
    f22ol_f22_operating_leverage_sprdrag_gpop_252d_base_v057_signal,
    f22ol_f22_operating_leverage_sprXgrow_op_252d_base_v058_signal,
    f22ol_f22_operating_leverage_spropvol_252d_base_v059_signal,
    f22ol_f22_operating_leverage_opxabsrank_252d_base_v060_signal,
    f22ol_f22_operating_leverage_opxabsvol_252d_base_v061_signal,
    f22ol_f22_operating_leverage_opxabsstreak_252d_base_v062_signal,
    f22ol_f22_operating_leverage_gpsclvol_252d_base_v063_signal,
    f22ol_f22_operating_leverage_mos_be_252d_base_v064_signal,
    f22ol_f22_operating_leverage_mos_be_chg_252d_base_v065_signal,
    f22ol_f22_operating_leverage_safetygp_z_252d_base_v066_signal,
    f22ol_f22_operating_leverage_bedist_op_252d_base_v067_signal,
    f22ol_f22_operating_leverage_bedist_ebit_252d_base_v068_signal,
    f22ol_f22_operating_leverage_fixlev_126d_base_v069_signal,
    f22ol_f22_operating_leverage_fixlev_252d_base_v070_signal,
    f22ol_f22_operating_leverage_fixlevz_252d_base_v071_signal,
    f22ol_f22_operating_leverage_fixlevvol_252d_base_v072_signal,
    f22ol_f22_operating_leverage_ebitelas_126d_base_v073_signal,
    f22ol_f22_operating_leverage_elasspr_ebitgp_252d_base_v074_signal,
    f22ol_f22_operating_leverage_elasdisp_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


F22_OPERATING_LEVERAGE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp) * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp) * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _margin(seed, lo, hi, rho=0.995):
        g = np.random.default_rng(seed)
        e = g.normal(0, 0.01, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = rho * ar[t - 1] + e[t]
        m = (ar - ar.min()) / (ar.max() - ar.min() + 1e-9)
        return pd.Series(lo + (hi - lo) * m, name=None)

    revenue = _fund(1, base=1.2e8, drift=0.035, vol=0.06).rename("revenue")
    opex = _fund(2, base=7.0e7, drift=0.030, vol=0.05).rename("opex")
    gp = (revenue * _margin(10, 0.34, 0.62)).rename("gp")
    opinc = (revenue * _margin(11, -0.16, 0.26)).rename("opinc")
    ebit = (revenue * _margin(12, -0.05, 0.27)).rename("ebit")

    cols = {"closeadj": closeadj, "close": close, "open": openp, "high": high,
            "low": low, "volume": volume, "revenue": revenue, "opex": opex,
            "gp": gp, "opinc": opinc, "ebit": ebit}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume", "revenue", "revenueusd",
             "deferredrev", "gp", "grossmargin", "opinc", "opex", "sgna", "cor", "rnd",
             "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc", "netinccmn", "netmargin",
             "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt",
             "ncfbus", "capex", "depamor", "sharesbas", "shareswa", "shareswadil", "assets",
             "assetsc", "tangibles", "intangibles", "ppnenet", "investments", "inventory",
             "receivables", "payables", "equity", "retearn", "workingcapital", "debt", "debtc",
             "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio", "roic", "roe",
             "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps",
             "de", "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis", "marketcap", "ev",
             "evebit", "evebitda", "pe", "pb", "ps", "shrholders", "shrvalue", "shrunits",
             "totalvalue", "percentoftotal", "fndholders", "undholders", "prfholders",
             "dbtholders", "putholders", "putvalue", "cllholders", "cllvalue", "wntholders",
             "wntvalue", "dbtvalue"}
    FUND = {"revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
            "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
            "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
            "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
            "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
            "investments", "inventory", "receivables", "payables", "equity", "retearn",
            "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
            "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
            "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
            "payoutratio", "prefdivis"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        inp = meta["inputs"]
        assert set(inp) <= ALLOW, "%s inputs not in allowlist: %s" % (name, inp)
        assert len(set(inp) & FUND) >= 1, "%s has no fundamental column" % name
        fn = meta["func"]
        args = [cols[c] for c in inp]
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

    print("OK f22_operating_leverage_base_001_075_claude: %d features pass" % n_features)
