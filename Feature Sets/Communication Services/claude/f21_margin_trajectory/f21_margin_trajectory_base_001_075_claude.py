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
    # ordinary least-squares slope over a rolling window (per-day)
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
    # operating margin synthesized from opinc / revenue (level)
    return opinc / revenue.replace(0, np.nan)


def _f21_gp_margin(gp, revenue):
    # gross-profit margin reconstructed from gp / revenue (cross-check level)
    return gp / revenue.replace(0, np.nan)


def _f21_trend(s, w):
    # trajectory = level now minus level w days ago
    return s - s.shift(w)


def _f21_swing(s, w):
    # margin swing = rolling dispersion of the margin level
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _f21_spread(a, b):
    # gross-vs-net style spread between two margin levels
    return a - b


def _f21_expansion(s, w_short, w_long):
    # expansion toward scale = recent avg level minus longer avg level
    return _mean(s, w_short) - _mean(s, w_long)


# ============================================================
# gross margin level, smoothed quarter (path-to-scale level)
def f21mt_f21_margin_trajectory_gmlvl_063d_base_v001_signal(grossmargin):
    b = _mean(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level, smoothed quarter
def f21mt_f21_margin_trajectory_nmlvl_063d_base_v002_signal(netmargin):
    b = _mean(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level, smoothed quarter
def f21mt_f21_margin_trajectory_emlvl_063d_base_v003_signal(ebitdamargin):
    b = _mean(ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin level (opinc/revenue), smoothed quarter
def f21mt_f21_margin_trajectory_omlvl_063d_base_v004_signal(opinc, revenue):
    b = _mean(_f21_op_margin(opinc, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-dollar acceleration: gp log-growth now vs a year ago (margin-scale inflection)
def f21mt_f21_margin_trajectory_gpmlvl_063d_base_v005_signal(gp):
    gp_g = np.log(gp.replace(0, np.nan)) - np.log(gp.shift(63).replace(0, np.nan))
    b = gp_g - gp_g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level, half-year smoothed
def f21mt_f21_margin_trajectory_gmlvl_126d_base_v006_signal(grossmargin):
    b = _mean(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level, half-year smoothed
def f21mt_f21_margin_trajectory_nmlvl_126d_base_v007_signal(netmargin):
    b = _mean(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level, half-year smoothed
def f21mt_f21_margin_trajectory_emlvl_126d_base_v008_signal(ebitdamargin):
    b = _mean(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend over a quarter (margin trajectory)
def f21mt_f21_margin_trajectory_gmtrend_063d_base_v009_signal(grossmargin):
    b = _f21_trend(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin trend over a quarter
def f21mt_f21_margin_trajectory_nmtrend_063d_base_v010_signal(netmargin):
    b = _f21_trend(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin trend over a quarter
def f21mt_f21_margin_trajectory_emtrend_063d_base_v011_signal(ebitdamargin):
    b = _f21_trend(ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin trend over a quarter
def f21mt_f21_margin_trajectory_omtrend_063d_base_v012_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _f21_trend(om, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend over a year (long trajectory)
def f21mt_f21_margin_trajectory_gmtrend_252d_base_v013_signal(grossmargin):
    b = _f21_trend(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin trend over a year
def f21mt_f21_margin_trajectory_nmtrend_252d_base_v014_signal(netmargin):
    b = _f21_trend(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin trend over a year
def f21mt_f21_margin_trajectory_emtrend_252d_base_v015_signal(ebitdamargin):
    b = _f21_trend(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin curvature: slope now minus slope a quarter ago (trajectory bend)
def f21mt_f21_margin_trajectory_gmslope_063d_base_v016_signal(grossmargin):
    sl = _slope(grossmargin, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin OLS slope over a half-year
def f21mt_f21_margin_trajectory_nmslope_126d_base_v017_signal(netmargin):
    b = _slope(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin OLS slope over a half-year
def f21mt_f21_margin_trajectory_emslope_126d_base_v018_signal(ebitdamargin):
    b = _slope(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin slope relative to its own dispersion (trajectory signal-to-noise)
def f21mt_f21_margin_trajectory_omslope_063d_base_v019_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    sl = _slope(om, 126)
    sw = _f21_swing(om, 126).replace(0, np.nan)
    b = sl / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net margin spread, de-trended vs its own year (wedge extremity, not level)
def f21mt_f21_margin_trajectory_gnspread_063d_base_v020_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-ebitda margin spread as a share of gross margin (relative D&A+opex wedge)
def f21mt_f21_margin_trajectory_gespread_063d_base_v021_signal(grossmargin, ebitdamargin):
    spr = _f21_spread(grossmargin, ebitdamargin)
    rel = spr / grossmargin.replace(0, np.nan)
    b = _mean(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-net margin spread (below-ebitda wedge level)
def f21mt_f21_margin_trajectory_enspread_063d_base_v022_signal(ebitdamargin, netmargin):
    b = _mean(_f21_spread(ebitdamargin, netmargin), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-operating margin spread (opex wedge level)
def f21mt_f21_margin_trajectory_gospread_063d_base_v023_signal(grossmargin, opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _mean(_f21_spread(grossmargin, om), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin expansion toward scale (recent vs long average)
def f21mt_f21_margin_trajectory_gmexp_063v252_base_v024_signal(grossmargin):
    b = _f21_expansion(grossmargin, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin expansion toward scale
def f21mt_f21_margin_trajectory_nmexp_063v252_base_v025_signal(netmargin):
    b = _f21_expansion(netmargin, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin expansion toward scale
def f21mt_f21_margin_trajectory_emexp_063v252_base_v026_signal(ebitdamargin):
    b = _f21_expansion(ebitdamargin, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin expansion toward scale
def f21mt_f21_margin_trajectory_omexp_063v252_base_v027_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _f21_expansion(om, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level z-scored vs its own year (de-trended margin extremity)
def f21mt_f21_margin_trajectory_gmz_252d_base_v028_signal(grossmargin):
    b = _z(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level z-scored vs its own year
def f21mt_f21_margin_trajectory_nmz_252d_base_v029_signal(netmargin):
    b = _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level z-scored vs its own year
def f21mt_f21_margin_trajectory_emz_252d_base_v030_signal(ebitdamargin):
    b = _z(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin level z-scored vs its own year
def f21mt_f21_margin_trajectory_omz_252d_base_v031_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _z(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin swing (level dispersion) over a half-year
def f21mt_f21_margin_trajectory_gmswing_126d_base_v032_signal(grossmargin):
    b = _f21_swing(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin swing over a half-year
def f21mt_f21_margin_trajectory_nmswing_126d_base_v033_signal(netmargin):
    b = _f21_swing(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin swing over a half-year
def f21mt_f21_margin_trajectory_emswing_126d_base_v034_signal(ebitdamargin):
    b = _f21_swing(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin swing over a half-year
def f21mt_f21_margin_trajectory_omswing_126d_base_v035_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _f21_swing(om, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level relative to its 252d max (distance below best margin)
def f21mt_f21_margin_trajectory_gmfrombest_252d_base_v036_signal(grossmargin):
    hi = _rmax(grossmargin, 252)
    b = grossmargin - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level relative to its 252d min (recovery off worst margin)
def f21mt_f21_margin_trajectory_nmfromworst_252d_base_v037_signal(netmargin):
    lo = _rmin(netmargin, 252)
    b = netmargin - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin position within its 252d range (path-to-scale position)
def f21mt_f21_margin_trajectory_emrngpos_252d_base_v038_signal(ebitdamargin):
    hi = _rmax(ebitdamargin, 252)
    lo = _rmin(ebitdamargin, 252)
    b = (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin position within its 252d range (path-to-scale position, bottom line)
def f21mt_f21_margin_trajectory_gmrngpos_252d_base_v039_signal(netmargin):
    hi = _rmax(netmargin, 252)
    lo = _rmin(netmargin, 252)
    b = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin trend normalized by its own swing (risk-adjusted trajectory)
def f21mt_f21_margin_trajectory_nmtrendadj_126d_base_v040_signal(netmargin):
    tr = _f21_trend(netmargin, 126)
    sw = _f21_swing(netmargin, 126).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend normalized by its own swing
def f21mt_f21_margin_trajectory_gmtrendadj_126d_base_v041_signal(grossmargin):
    tr = _f21_trend(grossmargin, 126)
    sw = _f21_swing(grossmargin, 126).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin trend normalized by its own swing
def f21mt_f21_margin_trajectory_emtrendadj_126d_base_v042_signal(ebitdamargin):
    tr = _f21_trend(ebitdamargin, 126)
    sw = _f21_swing(ebitdamargin, 126).replace(0, np.nan)
    b = tr / sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-net conversion ratio (how much gross margin survives to the bottom line)
def f21mt_f21_margin_trajectory_gnconv_063d_base_v043_signal(grossmargin, netmargin):
    r = netmargin / grossmargin.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-ebitda conversion trend: change in the ebitda/gross ratio over a half-year
def f21mt_f21_margin_trajectory_geconv_063d_base_v044_signal(grossmargin, ebitdamargin):
    r = ebitdamargin / grossmargin.replace(0, np.nan)
    sm = _mean(r, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# below-ebitda survival trend: change in the net/ebitda conversion ratio over a half-year
def f21mt_f21_margin_trajectory_enconv_063d_base_v045_signal(ebitdamargin, netmargin):
    r = netmargin / ebitdamargin.replace(0, np.nan)
    sm = _mean(r, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread trend (is the leakage wedge widening or closing)
def f21mt_f21_margin_trajectory_gnsprtrend_063d_base_v046_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    b = _f21_trend(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-ebitda spread trend
def f21mt_f21_margin_trajectory_gesprtrend_063d_base_v047_signal(grossmargin, ebitdamargin):
    spr = _f21_spread(grossmargin, ebitdamargin)
    b = _f21_trend(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-net spread trend
def f21mt_f21_margin_trajectory_ensprtrend_063d_base_v048_signal(ebitdamargin, netmargin):
    spr = _f21_spread(ebitdamargin, netmargin)
    b = _f21_trend(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-absorption: operating income as a share of gross profit (how much gp converts to opinc)
def f21mt_f21_margin_trajectory_opgpwedge_063d_base_v049_signal(opinc, gp):
    conv = opinc / gp.replace(0, np.nan)
    b = _mean(conv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin acceleration-as-level: short trend minus long trend (margin inflection level)
def f21mt_f21_margin_trajectory_gminfl_base_v050_signal(grossmargin):
    short = _f21_trend(grossmargin, 63)
    long = _f21_trend(grossmargin, 252) / 4.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin inflection level (short minus scaled long trend)
def f21mt_f21_margin_trajectory_nminfl_base_v051_signal(netmargin):
    short = _f21_trend(netmargin, 63)
    long = _f21_trend(netmargin, 252) / 4.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin inflection level
def f21mt_f21_margin_trajectory_eminfl_base_v052_signal(ebitdamargin):
    short = _f21_trend(ebitdamargin, 63)
    long = _f21_trend(ebitdamargin, 252) / 4.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level relative to its 252d mean (centered level)
def f21mt_f21_margin_trajectory_gmdemean_252d_base_v053_signal(grossmargin):
    b = grossmargin - _mean(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level relative to its 252d mean
def f21mt_f21_margin_trajectory_nmdemean_252d_base_v054_signal(netmargin):
    b = netmargin - _mean(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level relative to its 252d mean
def f21mt_f21_margin_trajectory_emdemean_252d_base_v055_signal(ebitdamargin):
    b = ebitdamargin - _mean(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-vs-scale divergence: gross margin trend minus revenue growth (margin path vs scale path)
def f21mt_f21_margin_trajectory_gmdollar_063d_base_v056_signal(grossmargin, revenue):
    gm_tr = _f21_trend(grossmargin, 126)
    rev_g = np.log(revenue.replace(0, np.nan)) - np.log(revenue.shift(126).replace(0, np.nan))
    b = gm_tr - 0.1 * rev_g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin contribution at scale: ebitda margin level times revenue growth (margin x scale)
def f21mt_f21_margin_trajectory_emdollar_063d_base_v057_signal(ebitdamargin, revenue):
    rev_g = np.log(revenue.replace(0, np.nan)) - np.log(revenue.shift(252).replace(0, np.nan))
    md = _mean(ebitdamargin, 63) * rev_g
    b = md
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread acceleration: spread trend now vs a half-year ago (wedge inflection)
def f21mt_f21_margin_trajectory_gmgap_063d_base_v058_signal(grossmargin, netmargin):
    spr = _f21_spread(grossmargin, netmargin)
    tr = _f21_trend(spr, 63)
    b = tr - tr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin breadth: smoothed fraction of the three margins above their own 252d median (regime)
def f21mt_f21_margin_trajectory_breadth_252d_base_v059_signal(grossmargin, netmargin, ebitdamargin):
    g = (grossmargin > grossmargin.rolling(252, min_periods=126).median()).astype(float)
    nn = (netmargin > netmargin.rolling(252, min_periods=126).median()).astype(float)
    e = (ebitdamargin > ebitdamargin.rolling(252, min_periods=126).median()).astype(float)
    b = ((g + nn + e) / 3.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year net margin held above its own trailing-year mean (durability regime)
def f21mt_f21_margin_trajectory_nmposfrac_252d_base_v060_signal(netmargin):
    above = (netmargin > _mean(netmargin, 252)).astype(float)
    b = above.rolling(252, min_periods=126).mean() + 0.05 * _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year ebitda margin held above its own trailing-year median (regime persistence)
def f21mt_f21_margin_trajectory_emposfrac_252d_base_v061_signal(ebitdamargin):
    thr = ebitdamargin.rolling(252, min_periods=126).median()
    above = (ebitdamargin > thr).astype(float)
    b = above.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year operating margin held above its own trailing-year median (regime persistence)
def f21mt_f21_margin_trajectory_omposfrac_252d_base_v062_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    thr = om.rolling(252, min_periods=126).median()
    above = (om > thr).astype(float)
    b = above.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level percentile-ranked vs its own 504d history
def f21mt_f21_margin_trajectory_gmrank_504d_base_v063_signal(grossmargin):
    b = grossmargin.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin level percentile-ranked vs its own 504d history
def f21mt_f21_margin_trajectory_nmrank_504d_base_v064_signal(netmargin):
    b = netmargin.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level percentile-ranked vs its own 504d history
def f21mt_f21_margin_trajectory_emrank_504d_base_v065_signal(ebitdamargin):
    b = ebitdamargin.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-profile dispersion trend: is the gross/ebitda/net profile widening or compressing
def f21mt_f21_margin_trajectory_profdisp_063d_base_v066_signal(grossmargin, netmargin, ebitdamargin):
    stk = pd.concat([_mean(grossmargin, 63), _mean(netmargin, 63), _mean(ebitdamargin, 63)], axis=1)
    disp = stk.std(axis=1)
    b = disp - disp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin year-over-year level change (annual trajectory step)
def f21mt_f21_margin_trajectory_gmyoy_252d_base_v067_signal(grossmargin):
    sm = _mean(grossmargin, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin year-over-year level change
def f21mt_f21_margin_trajectory_nmyoy_252d_base_v068_signal(netmargin):
    sm = _mean(netmargin, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin year-over-year level change
def f21mt_f21_margin_trajectory_emyoy_252d_base_v069_signal(ebitdamargin):
    sm = _mean(ebitdamargin, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-to-gross efficiency trend: change in the om/gross ratio over a half-year
def f21mt_f21_margin_trajectory_omtogm_063d_base_v070_signal(opinc, revenue, grossmargin):
    om = _f21_op_margin(opinc, revenue)
    r = om / grossmargin.replace(0, np.nan)
    sm = _mean(r, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of net margin trend (direction x sqrt magnitude, bounded trajectory)
def f21mt_f21_margin_trajectory_nmsignmag_063d_base_v071_signal(netmargin):
    tr = _f21_trend(netmargin, 63)
    b = np.sign(tr) * np.sqrt(tr.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin expansion streak: fraction of last quarter the level rose above its 21d-ago value
def f21mt_f21_margin_trajectory_gmtanh_063d_base_v072_signal(grossmargin):
    up = (grossmargin > grossmargin.shift(21)).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin compression streak: fraction of last quarter ebitda margin below its 126d mean
def f21mt_f21_margin_trajectory_emcompress_063d_base_v073_signal(ebitdamargin):
    below = (ebitdamargin < _mean(ebitdamargin, 126)).astype(float)
    b = below.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin stability: inverse coefficient of variation of the level (durable margin)
def f21mt_f21_margin_trajectory_gmstab_126d_base_v074_signal(grossmargin):
    m = _mean(grossmargin, 126)
    sd = _std(grossmargin, 126).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin expansion over a half-year vs two-year baseline (scale-margin emergence)
def f21mt_f21_margin_trajectory_omexp_126v504_base_v075_signal(opinc, revenue):
    om = _f21_op_margin(opinc, revenue)
    b = _mean(om, 126) - _mean(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21mt_f21_margin_trajectory_gmlvl_063d_base_v001_signal,
    f21mt_f21_margin_trajectory_nmlvl_063d_base_v002_signal,
    f21mt_f21_margin_trajectory_emlvl_063d_base_v003_signal,
    f21mt_f21_margin_trajectory_omlvl_063d_base_v004_signal,
    f21mt_f21_margin_trajectory_gpmlvl_063d_base_v005_signal,
    f21mt_f21_margin_trajectory_gmlvl_126d_base_v006_signal,
    f21mt_f21_margin_trajectory_nmlvl_126d_base_v007_signal,
    f21mt_f21_margin_trajectory_emlvl_126d_base_v008_signal,
    f21mt_f21_margin_trajectory_gmtrend_063d_base_v009_signal,
    f21mt_f21_margin_trajectory_nmtrend_063d_base_v010_signal,
    f21mt_f21_margin_trajectory_emtrend_063d_base_v011_signal,
    f21mt_f21_margin_trajectory_omtrend_063d_base_v012_signal,
    f21mt_f21_margin_trajectory_gmtrend_252d_base_v013_signal,
    f21mt_f21_margin_trajectory_nmtrend_252d_base_v014_signal,
    f21mt_f21_margin_trajectory_emtrend_252d_base_v015_signal,
    f21mt_f21_margin_trajectory_gmslope_063d_base_v016_signal,
    f21mt_f21_margin_trajectory_nmslope_126d_base_v017_signal,
    f21mt_f21_margin_trajectory_emslope_126d_base_v018_signal,
    f21mt_f21_margin_trajectory_omslope_063d_base_v019_signal,
    f21mt_f21_margin_trajectory_gnspread_063d_base_v020_signal,
    f21mt_f21_margin_trajectory_gespread_063d_base_v021_signal,
    f21mt_f21_margin_trajectory_enspread_063d_base_v022_signal,
    f21mt_f21_margin_trajectory_gospread_063d_base_v023_signal,
    f21mt_f21_margin_trajectory_gmexp_063v252_base_v024_signal,
    f21mt_f21_margin_trajectory_nmexp_063v252_base_v025_signal,
    f21mt_f21_margin_trajectory_emexp_063v252_base_v026_signal,
    f21mt_f21_margin_trajectory_omexp_063v252_base_v027_signal,
    f21mt_f21_margin_trajectory_gmz_252d_base_v028_signal,
    f21mt_f21_margin_trajectory_nmz_252d_base_v029_signal,
    f21mt_f21_margin_trajectory_emz_252d_base_v030_signal,
    f21mt_f21_margin_trajectory_omz_252d_base_v031_signal,
    f21mt_f21_margin_trajectory_gmswing_126d_base_v032_signal,
    f21mt_f21_margin_trajectory_nmswing_126d_base_v033_signal,
    f21mt_f21_margin_trajectory_emswing_126d_base_v034_signal,
    f21mt_f21_margin_trajectory_omswing_126d_base_v035_signal,
    f21mt_f21_margin_trajectory_gmfrombest_252d_base_v036_signal,
    f21mt_f21_margin_trajectory_nmfromworst_252d_base_v037_signal,
    f21mt_f21_margin_trajectory_emrngpos_252d_base_v038_signal,
    f21mt_f21_margin_trajectory_gmrngpos_252d_base_v039_signal,
    f21mt_f21_margin_trajectory_nmtrendadj_126d_base_v040_signal,
    f21mt_f21_margin_trajectory_gmtrendadj_126d_base_v041_signal,
    f21mt_f21_margin_trajectory_emtrendadj_126d_base_v042_signal,
    f21mt_f21_margin_trajectory_gnconv_063d_base_v043_signal,
    f21mt_f21_margin_trajectory_geconv_063d_base_v044_signal,
    f21mt_f21_margin_trajectory_enconv_063d_base_v045_signal,
    f21mt_f21_margin_trajectory_gnsprtrend_063d_base_v046_signal,
    f21mt_f21_margin_trajectory_gesprtrend_063d_base_v047_signal,
    f21mt_f21_margin_trajectory_ensprtrend_063d_base_v048_signal,
    f21mt_f21_margin_trajectory_opgpwedge_063d_base_v049_signal,
    f21mt_f21_margin_trajectory_gminfl_base_v050_signal,
    f21mt_f21_margin_trajectory_nminfl_base_v051_signal,
    f21mt_f21_margin_trajectory_eminfl_base_v052_signal,
    f21mt_f21_margin_trajectory_gmdemean_252d_base_v053_signal,
    f21mt_f21_margin_trajectory_nmdemean_252d_base_v054_signal,
    f21mt_f21_margin_trajectory_emdemean_252d_base_v055_signal,
    f21mt_f21_margin_trajectory_gmdollar_063d_base_v056_signal,
    f21mt_f21_margin_trajectory_emdollar_063d_base_v057_signal,
    f21mt_f21_margin_trajectory_gmgap_063d_base_v058_signal,
    f21mt_f21_margin_trajectory_breadth_252d_base_v059_signal,
    f21mt_f21_margin_trajectory_nmposfrac_252d_base_v060_signal,
    f21mt_f21_margin_trajectory_emposfrac_252d_base_v061_signal,
    f21mt_f21_margin_trajectory_omposfrac_252d_base_v062_signal,
    f21mt_f21_margin_trajectory_gmrank_504d_base_v063_signal,
    f21mt_f21_margin_trajectory_nmrank_504d_base_v064_signal,
    f21mt_f21_margin_trajectory_emrank_504d_base_v065_signal,
    f21mt_f21_margin_trajectory_profdisp_063d_base_v066_signal,
    f21mt_f21_margin_trajectory_gmyoy_252d_base_v067_signal,
    f21mt_f21_margin_trajectory_nmyoy_252d_base_v068_signal,
    f21mt_f21_margin_trajectory_emyoy_252d_base_v069_signal,
    f21mt_f21_margin_trajectory_omtogm_063d_base_v070_signal,
    f21mt_f21_margin_trajectory_nmsignmag_063d_base_v071_signal,
    f21mt_f21_margin_trajectory_gmtanh_063d_base_v072_signal,
    f21mt_f21_margin_trajectory_emcompress_063d_base_v073_signal,
    f21mt_f21_margin_trajectory_gmstab_126d_base_v074_signal,
    f21mt_f21_margin_trajectory_omexp_126v504_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_MARGIN_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    # margins small positive ~0.1-0.6
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

    print("OK f21_margin_trajectory_base_001_075_claude: %d features pass" % n_features)
