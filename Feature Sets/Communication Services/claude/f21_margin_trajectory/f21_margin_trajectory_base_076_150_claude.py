import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

ALLOWLIST = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
    "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
    "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
    "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
    "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
    "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
    "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
    "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
    "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
    "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}


# ===== generic helpers =====
def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx * idx).sum())

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum()) / denom
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (margin level & trajectory) =====
def _f21_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f21_gp_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f21_trend(s, w):
    return s - s.shift(w)


def _f21_swing(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _f21_spread(a, b):
    return a - b


def _f21_expansion(s, w_short, w_long):
    return _mean(s, w_short) - _mean(s, w_long)


# ============================================================
# gross margin level, month-smoothed (fast level)
def f21mt_f21_margin_trajectory_gmlvl_021d_base_v076_signal(grossmargin):
    b = _mean(grossmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level, month-smoothed
def f21mt_f21_margin_trajectory_nmlvl_021d_base_v077_signal(netmargin):
    b = _mean(netmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level, two-year smoothed (durable scale margin)
def f21mt_f21_margin_trajectory_emlvl_504d_base_v078_signal(ebitdamargin):
    b = _mean(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level, two-year smoothed
def f21mt_f21_margin_trajectory_nmlvl_504d_base_v079_signal(netmargin):
    b = _mean(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin level, two-year smoothed
def f21mt_f21_margin_trajectory_omlvl_504d_base_v080_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _mean(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend over a month (fast trajectory)
def f21mt_f21_margin_trajectory_gmtrend_021d_base_v081_signal(grossmargin):
    b = _f21_trend(grossmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin trend over a month
def f21mt_f21_margin_trajectory_nmtrend_021d_base_v082_signal(netmargin):
    b = _f21_trend(netmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin trend over a month
def f21mt_f21_margin_trajectory_emtrend_021d_base_v083_signal(ebitdamargin):
    b = _f21_trend(ebitdamargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin trend over a year (long trajectory)
def f21mt_f21_margin_trajectory_omtrend_252d_base_v084_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _f21_trend(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin OLS slope over a year (long smooth trajectory)
def f21mt_f21_margin_trajectory_gmslope_252d_base_v085_signal(grossmargin):
    b = _slope(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin OLS slope over a year
def f21mt_f21_margin_trajectory_nmslope_252d_base_v086_signal(netmargin):
    b = _slope(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin OLS slope over a quarter (fast slope)
def f21mt_f21_margin_trajectory_emslope_063d_base_v087_signal(ebitdamargin):
    b = _slope(ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin OLS slope over a quarter
def f21mt_f21_margin_trajectory_nmslope_063d_base_v088_signal(netmargin):
    b = _slope(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread momentum: fast wedge change over a month (leakage-wedge velocity)
def f21mt_f21_margin_trajectory_gnspread_021d_base_v089_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    sm = _mean(spr, 21)
    b = sm - sm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-net spread as a share of ebitda margin (relative below-ebitda wedge)
def f21mt_f21_margin_trajectory_enspreadrel_063d_base_v090_signal(ebitdamargin, netmargin):
    spr = _f21_spread(ebitdamargin, netmargin)
    rel = spr / ebitdamargin.replace(0, np.nan)
    b = _mean(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread as a share of gross margin (relative leakage)
def f21mt_f21_margin_trajectory_gnspreadrel_063d_base_v091_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    rel = spr / grossmargin.replace(0, np.nan)
    b = _mean(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-net spread (below-operating wedge level)
def f21mt_f21_margin_trajectory_onspread_063d_base_v092_signal(opinc, revenue, netmargin):
    om = _f21_op_margin(opinc, revenue)
    b = _mean(_f21_spread(om, netmargin), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin expansion: half-year recent vs two-year baseline (durable expansion)
def f21mt_f21_margin_trajectory_gmexp_126v504_base_v093_signal(grossmargin):
    b = _f21_expansion(grossmargin, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin expansion: half-year recent vs two-year baseline
def f21mt_f21_margin_trajectory_nmexp_126v504_base_v094_signal(netmargin):
    b = _f21_expansion(netmargin, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin expansion acceleration: how the quarter-vs-half-year emergence is changing
def f21mt_f21_margin_trajectory_emexp_021v126_base_v095_signal(ebitdamargin):
    exp = _f21_expansion(ebitdamargin, 21, 126)
    b = exp - exp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level z-scored vs its own half-year (short de-trended extremity)
def f21mt_f21_margin_trajectory_gmz_126d_base_v096_signal(grossmargin):
    b = _z(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level z-scored vs its own two-year (long de-trended extremity)
def f21mt_f21_margin_trajectory_nmz_504d_base_v097_signal(netmargin):
    b = _z(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level z-scored vs its own half-year
def f21mt_f21_margin_trajectory_emz_126d_base_v098_signal(ebitdamargin):
    b = _z(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin swing over a quarter (fast level dispersion)
def f21mt_f21_margin_trajectory_gmswing_063d_base_v099_signal(grossmargin):
    b = _f21_swing(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin swing over a year (long level dispersion)
def f21mt_f21_margin_trajectory_nmswing_252d_base_v100_signal(netmargin):
    b = _f21_swing(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin swing over a year
def f21mt_f21_margin_trajectory_emswing_252d_base_v101_signal(ebitdamargin):
    b = _f21_swing(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin distance below its 252d best (room to recover bottom-line margin)
def f21mt_f21_margin_trajectory_nmfrombest_252d_base_v102_signal(netmargin):
    hi = _rmax(netmargin, 252)
    b = netmargin - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin distance above its 252d worst (recovery off trough margin)
def f21mt_f21_margin_trajectory_emfromworst_252d_base_v103_signal(ebitdamargin):
    lo = _rmin(ebitdamargin, 252)
    b = ebitdamargin - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin position within its 252d range (path-to-scale position)
def f21mt_f21_margin_trajectory_omrngpos_252d_base_v104_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    hi = _rmax(om, 252)
    lo = _rmin(om, 252)
    b = (om - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin position within its 504d range (long path-to-scale position)
def f21mt_f21_margin_trajectory_gmrngpos_504d_base_v105_signal(grossmargin):
    hi = _rmax(grossmargin, 504)
    lo = _rmin(grossmargin, 504)
    b = (grossmargin - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend normalized by its own swing over a quarter (short risk-adjusted trajectory)
def f21mt_f21_margin_trajectory_gmtrendadj_063d_base_v106_signal(grossmargin):
    tr = _f21_trend(grossmargin, 63)
    sw = _f21_swing(grossmargin, 63).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin trend normalized by its own swing over a year (long risk-adjusted trajectory)
def f21mt_f21_margin_trajectory_nmtrendadj_252d_base_v107_signal(netmargin):
    tr = _f21_trend(netmargin, 252)
    sw = _f21_swing(netmargin, 252).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin trend normalized by its own swing over a quarter
def f21mt_f21_margin_trajectory_emtrendadj_063d_base_v108_signal(ebitdamargin):
    tr = _f21_trend(ebitdamargin, 63)
    sw = _f21_swing(ebitdamargin, 63).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-net conversion ratio over a half-year (durable survival to bottom line)
def f21mt_f21_margin_trajectory_gnconv_126d_base_v109_signal(grossmargin, netmargin):
    r = netmargin / grossmargin.replace(0, np.nan)
    b = _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-to-net conversion ratio (below-operating survival)
def f21mt_f21_margin_trajectory_onconv_063d_base_v110_signal(opinc, revenue, netmargin):
    om = _f21_op_margin(opinc, revenue)
    r = netmargin / om.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-operating conversion ratio (opex efficiency: how much gross survives opex)
def f21mt_f21_margin_trajectory_goconv_063d_base_v111_signal(grossmargin, opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    r = om / grossmargin.replace(0, np.nan)
    b = _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread swing (how volatile the leakage wedge is)
def f21mt_f21_margin_trajectory_gnsprswing_126d_base_v112_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    b = _f21_swing(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-net spread swing
def f21mt_f21_margin_trajectory_ensprswing_126d_base_v113_signal(ebitdamargin, netmargin):
    spr = _f21_spread(ebitdamargin, netmargin)
    b = _f21_swing(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-ebitda spread swing
def f21mt_f21_margin_trajectory_gesprswing_126d_base_v114_signal(grossmargin, ebitdamargin):
    spr = _f21_spread(grossmargin, ebitdamargin)
    b = _f21_swing(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin inflection over short vs long windows (fast minus slow trajectory)
def f21mt_f21_margin_trajectory_nminfl_021v126_base_v115_signal(netmargin):
    short = _f21_trend(netmargin, 21)
    long = _f21_trend(netmargin, 126) / 6.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin inflection over short vs long windows
def f21mt_f21_margin_trajectory_gminfl_021v126_base_v116_signal(grossmargin):
    short = _f21_trend(grossmargin, 21)
    long = _f21_trend(grossmargin, 126) / 6.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin inflection over short vs long windows
def f21mt_f21_margin_trajectory_eminfl_021v126_base_v117_signal(ebitdamargin):
    short = _f21_trend(ebitdamargin, 21)
    long = _f21_trend(ebitdamargin, 126) / 6.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin demeaned vs its own half-year mean (short centered level)
def f21mt_f21_margin_trajectory_gmdemean_126d_base_v118_signal(grossmargin):
    b = grossmargin - _mean(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin demeaned vs its own half-year mean
def f21mt_f21_margin_trajectory_nmdemean_126d_base_v119_signal(netmargin):
    b = netmargin - _mean(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin demeaned vs its own two-year mean (long centered level)
def f21mt_f21_margin_trajectory_emdemean_504d_base_v120_signal(ebitdamargin):
    b = ebitdamargin - _mean(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin demeaned vs its own year mean
def f21mt_f21_margin_trajectory_omdemean_252d_base_v121_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = om - _mean(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level percentile-ranked vs its own year history
def f21mt_f21_margin_trajectory_gmrank_252d_base_v122_signal(grossmargin):
    b = grossmargin.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level percentile-ranked vs its own year history
def f21mt_f21_margin_trajectory_nmrank_252d_base_v123_signal(netmargin):
    b = netmargin.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin level percentile-ranked vs its own 504d history
def f21mt_f21_margin_trajectory_omrank_504d_base_v124_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = om.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-profile minimum margin (worst of the three margins — bottleneck level)
def f21mt_f21_margin_trajectory_profmin_063d_base_v125_signal(grossmargin, netmargin, ebitdamargin):
    stk = pd.concat([_mean(grossmargin, 63), _mean(netmargin, 63), _mean(ebitdamargin, 63)], axis=1)
    b = stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-profile range (best minus worst margin — profile spread level)
def f21mt_f21_margin_trajectory_profrange_063d_base_v126_signal(grossmargin, netmargin, ebitdamargin):
    stk = pd.concat([_mean(grossmargin, 63), _mean(netmargin, 63), _mean(ebitdamargin, 63)], axis=1)
    b = stk.max(axis=1) - stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin year-over-year change over a month-smoothed level (annual step, fast smooth)
def f21mt_f21_margin_trajectory_gmyoy_021d_base_v127_signal(grossmargin):
    sm = _mean(grossmargin, 21)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin two-year change (multi-year trajectory step)
def f21mt_f21_margin_trajectory_nm2yr_504d_base_v128_signal(netmargin):
    sm = _mean(netmargin, 63)
    b = sm - sm.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin two-year change
def f21mt_f21_margin_trajectory_em2yr_504d_base_v129_signal(ebitdamargin):
    sm = _mean(ebitdamargin, 63)
    b = sm - sm.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin sign-magnitude trend over a half-year (bounded directional trajectory)
def f21mt_f21_margin_trajectory_nmsignmag_126d_base_v130_signal(netmargin):
    tr = _f21_trend(netmargin, 126)
    b = np.sign(tr) * np.sqrt(tr.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin sign-magnitude trend over a quarter
def f21mt_f21_margin_trajectory_emsignmag_063d_base_v131_signal(ebitdamargin):
    tr = _f21_trend(ebitdamargin, 63)
    b = np.sign(tr) * np.sqrt(tr.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin expansion streak: fraction of last half-year level rose above its 21d-ago value
def f21mt_f21_margin_trajectory_nmupstreak_126d_base_v132_signal(netmargin):
    up = (netmargin > netmargin.shift(21)).astype(float)
    b = up.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin compression streak: fraction of last quarter below its 63d-ago value
def f21mt_f21_margin_trajectory_emdownstreak_063d_base_v133_signal(ebitdamargin):
    down = (ebitdamargin < ebitdamargin.shift(63)).astype(float)
    b = down.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin stability over a year (inverse coefficient of variation, durable margin)
def f21mt_f21_margin_trajectory_gmstab_252d_base_v134_signal(grossmargin):
    m = _mean(grossmargin, 252)
    sd = _std(grossmargin, 252).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin stability over a half-year
def f21mt_f21_margin_trajectory_nmstab_126d_base_v135_signal(netmargin):
    m = _mean(netmargin, 126)
    sd = _std(netmargin, 126).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin stability over a year
def f21mt_f21_margin_trajectory_emstab_252d_base_v136_signal(ebitdamargin):
    m = _mean(ebitdamargin, 252)
    sd = _std(ebitdamargin, 252).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net conversion stability (consistency of the survival ratio)
def f21mt_f21_margin_trajectory_gnconvstab_252d_base_v137_signal(grossmargin, netmargin):
    r = netmargin / grossmargin.replace(0, np.nan)
    m = _mean(r, 252)
    sd = _std(r, 252).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin smoothed by EMA (persistent operating-margin level)
def f21mt_f21_margin_trajectory_omema_063d_base_v138_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = om.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin displacement normalized by its dispersion (standardized EMA displacement)
def f21mt_f21_margin_trajectory_gmdisp_063d_base_v139_signal(grossmargin):
    disp = grossmargin - grossmargin.ewm(span=126, min_periods=42).mean()
    sd = _std(grossmargin, 126).replace(0, np.nan)
    b = disp / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin displacement normalized by its dispersion (standardized EMA displacement)
def f21mt_f21_margin_trajectory_nmdisp_063d_base_v140_signal(netmargin):
    disp = netmargin - netmargin.ewm(span=126, min_periods=42).mean()
    sd = _std(netmargin, 126).replace(0, np.nan)
    b = disp / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin EMA-crossover normalized by level (relative trajectory regime)
def f21mt_f21_margin_trajectory_emcross_base_v141_signal(ebitdamargin):
    fast = ebitdamargin.ewm(span=21, min_periods=10).mean()
    slow = ebitdamargin.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EMA-crossover momentum: change in the fast-slow EMA gap over a quarter
def f21mt_f21_margin_trajectory_gmcross_base_v142_signal(grossmargin):
    fast = grossmargin.ewm(span=21, min_periods=10).mean()
    slow = grossmargin.ewm(span=126, min_periods=42).mean()
    gap = fast - slow
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin vs ebitda margin spread (D&A wedge level, op-vs-ebitda)
def f21mt_f21_margin_trajectory_oespread_063d_base_v143_signal(opinc, revenue, ebitdamargin):
    om = _f21_op_margin(opinc, revenue)
    b = _mean(_f21_spread(ebitdamargin, om), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin acceleration-of-expansion: expansion now vs expansion a half-year ago
def f21mt_f21_margin_trajectory_gmexpacc_base_v144_signal(grossmargin):
    exp = _f21_expansion(grossmargin, 63, 252)
    b = exp - exp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin acceleration-of-expansion
def f21mt_f21_margin_trajectory_nmexpacc_base_v145_signal(netmargin):
    exp = _f21_expansion(netmargin, 63, 252)
    b = exp - exp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-floor proximity: ebitda margin distance to its trailing-year worst, scaled (downside cushion)
def f21mt_f21_margin_trajectory_emfloor_252d_base_v146_signal(ebitdamargin):
    lo = _rmin(ebitdamargin, 252)
    rng = (_rmax(ebitdamargin, 252) - lo).replace(0, np.nan)
    b = (ebitdamargin - lo) / rng - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin tanh-bounded demeaned level (squashed extremity)
def f21mt_f21_margin_trajectory_gmtanhlvl_252d_base_v147_signal(grossmargin):
    dm = grossmargin - _mean(grossmargin, 252)
    b = np.tanh(8.0 * dm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin breadth vs ebitda margin: fraction of last year net leads ebitda direction
def f21mt_f21_margin_trajectory_lead_252d_base_v148_signal(netmargin, ebitdamargin):
    nm_up = (netmargin > netmargin.shift(21)).astype(float)
    em_up = (ebitdamargin > ebitdamargin.shift(21)).astype(float)
    agree = (nm_up == em_up).astype(float)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin slope-of-slope: curvature of operating margin over a half-year
def f21mt_f21_margin_trajectory_omcurv_126d_base_v149_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    sl = _slope(om, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite margin-quality: ebitda margin level x its stability (durable scale margin)
def f21mt_f21_margin_trajectory_emquality_252d_base_v150_signal(ebitdamargin):
    m = _mean(ebitdamargin, 252)
    sd = _std(ebitdamargin, 252).replace(0, np.nan)
    b = m * np.tanh(m / sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21mt_f21_margin_trajectory_gmlvl_021d_base_v076_signal,
    f21mt_f21_margin_trajectory_nmlvl_021d_base_v077_signal,
    f21mt_f21_margin_trajectory_emlvl_504d_base_v078_signal,
    f21mt_f21_margin_trajectory_nmlvl_504d_base_v079_signal,
    f21mt_f21_margin_trajectory_omlvl_504d_base_v080_signal,
    f21mt_f21_margin_trajectory_gmtrend_021d_base_v081_signal,
    f21mt_f21_margin_trajectory_nmtrend_021d_base_v082_signal,
    f21mt_f21_margin_trajectory_emtrend_021d_base_v083_signal,
    f21mt_f21_margin_trajectory_omtrend_252d_base_v084_signal,
    f21mt_f21_margin_trajectory_gmslope_252d_base_v085_signal,
    f21mt_f21_margin_trajectory_nmslope_252d_base_v086_signal,
    f21mt_f21_margin_trajectory_emslope_063d_base_v087_signal,
    f21mt_f21_margin_trajectory_nmslope_063d_base_v088_signal,
    f21mt_f21_margin_trajectory_gnspread_021d_base_v089_signal,
    f21mt_f21_margin_trajectory_enspreadrel_063d_base_v090_signal,
    f21mt_f21_margin_trajectory_gnspreadrel_063d_base_v091_signal,
    f21mt_f21_margin_trajectory_onspread_063d_base_v092_signal,
    f21mt_f21_margin_trajectory_gmexp_126v504_base_v093_signal,
    f21mt_f21_margin_trajectory_nmexp_126v504_base_v094_signal,
    f21mt_f21_margin_trajectory_emexp_021v126_base_v095_signal,
    f21mt_f21_margin_trajectory_gmz_126d_base_v096_signal,
    f21mt_f21_margin_trajectory_nmz_504d_base_v097_signal,
    f21mt_f21_margin_trajectory_emz_126d_base_v098_signal,
    f21mt_f21_margin_trajectory_gmswing_063d_base_v099_signal,
    f21mt_f21_margin_trajectory_nmswing_252d_base_v100_signal,
    f21mt_f21_margin_trajectory_emswing_252d_base_v101_signal,
    f21mt_f21_margin_trajectory_nmfrombest_252d_base_v102_signal,
    f21mt_f21_margin_trajectory_emfromworst_252d_base_v103_signal,
    f21mt_f21_margin_trajectory_omrngpos_252d_base_v104_signal,
    f21mt_f21_margin_trajectory_gmrngpos_504d_base_v105_signal,
    f21mt_f21_margin_trajectory_gmtrendadj_063d_base_v106_signal,
    f21mt_f21_margin_trajectory_nmtrendadj_252d_base_v107_signal,
    f21mt_f21_margin_trajectory_emtrendadj_063d_base_v108_signal,
    f21mt_f21_margin_trajectory_gnconv_126d_base_v109_signal,
    f21mt_f21_margin_trajectory_onconv_063d_base_v110_signal,
    f21mt_f21_margin_trajectory_goconv_063d_base_v111_signal,
    f21mt_f21_margin_trajectory_gnsprswing_126d_base_v112_signal,
    f21mt_f21_margin_trajectory_ensprswing_126d_base_v113_signal,
    f21mt_f21_margin_trajectory_gesprswing_126d_base_v114_signal,
    f21mt_f21_margin_trajectory_nminfl_021v126_base_v115_signal,
    f21mt_f21_margin_trajectory_gminfl_021v126_base_v116_signal,
    f21mt_f21_margin_trajectory_eminfl_021v126_base_v117_signal,
    f21mt_f21_margin_trajectory_gmdemean_126d_base_v118_signal,
    f21mt_f21_margin_trajectory_nmdemean_126d_base_v119_signal,
    f21mt_f21_margin_trajectory_emdemean_504d_base_v120_signal,
    f21mt_f21_margin_trajectory_omdemean_252d_base_v121_signal,
    f21mt_f21_margin_trajectory_gmrank_252d_base_v122_signal,
    f21mt_f21_margin_trajectory_nmrank_252d_base_v123_signal,
    f21mt_f21_margin_trajectory_omrank_504d_base_v124_signal,
    f21mt_f21_margin_trajectory_profmin_063d_base_v125_signal,
    f21mt_f21_margin_trajectory_profrange_063d_base_v126_signal,
    f21mt_f21_margin_trajectory_gmyoy_021d_base_v127_signal,
    f21mt_f21_margin_trajectory_nm2yr_504d_base_v128_signal,
    f21mt_f21_margin_trajectory_em2yr_504d_base_v129_signal,
    f21mt_f21_margin_trajectory_nmsignmag_126d_base_v130_signal,
    f21mt_f21_margin_trajectory_emsignmag_063d_base_v131_signal,
    f21mt_f21_margin_trajectory_nmupstreak_126d_base_v132_signal,
    f21mt_f21_margin_trajectory_emdownstreak_063d_base_v133_signal,
    f21mt_f21_margin_trajectory_gmstab_252d_base_v134_signal,
    f21mt_f21_margin_trajectory_nmstab_126d_base_v135_signal,
    f21mt_f21_margin_trajectory_emstab_252d_base_v136_signal,
    f21mt_f21_margin_trajectory_gnconvstab_252d_base_v137_signal,
    f21mt_f21_margin_trajectory_omema_063d_base_v138_signal,
    f21mt_f21_margin_trajectory_gmdisp_063d_base_v139_signal,
    f21mt_f21_margin_trajectory_nmdisp_063d_base_v140_signal,
    f21mt_f21_margin_trajectory_emcross_base_v141_signal,
    f21mt_f21_margin_trajectory_gmcross_base_v142_signal,
    f21mt_f21_margin_trajectory_oespread_063d_base_v143_signal,
    f21mt_f21_margin_trajectory_gmexpacc_base_v144_signal,
    f21mt_f21_margin_trajectory_nmexpacc_base_v145_signal,
    f21mt_f21_margin_trajectory_emfloor_252d_base_v146_signal,
    f21mt_f21_margin_trajectory_gmtanhlvl_252d_base_v147_signal,
    f21mt_f21_margin_trajectory_lead_252d_base_v148_signal,
    f21mt_f21_margin_trajectory_omcurv_126d_base_v149_signal,
    f21mt_f21_margin_trajectory_emquality_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_MARGIN_TRAJECTORY_REGISTRY_076_150 = REGISTRY


def _build_inputs(n=1500):
    np.random.seed(42)
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

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    grossmargin = _fund(101, base=0.45, drift=0.0, vol=0.05).clip(0.05, 0.85).rename("grossmargin")
    netmargin = _fund(102, base=0.12, drift=0.0, vol=0.06).clip(-0.2, 0.5).rename("netmargin")
    ebitdamargin = _fund(103, base=0.22, drift=0.0, vol=0.05).clip(-0.1, 0.6).rename("ebitdamargin")
    revenue = _fund(104, base=1.5e8, drift=0.03, vol=0.06).rename("revenue")
    gp = (revenue * grossmargin).rename("gp")
    opinc = _fund(106, base=2.0e7, drift=0.02, vol=0.09, allow_neg=True).rename("opinc")

    return {
        "closeadj": closeadj, "close": close, "open": openp, "high": high,
        "low": low, "volume": volume, "grossmargin": grossmargin,
        "netmargin": netmargin, "ebitdamargin": ebitdamargin,
        "revenue": revenue, "gp": gp, "opinc": opinc,
    }


if __name__ == "__main__":
    cols = _build_inputs(1500)

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOWLIST, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOWLIST)
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

    print("OK f21_margin_trajectory_base_076_150_claude: %d features pass" % n_features)
