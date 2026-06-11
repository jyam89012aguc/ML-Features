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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx * idx).sum())

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (FCF trajectory) =====
def _f25_growth(s, w):
    base = s.shift(w)
    return np.sign(base) * (s - base) / base.abs().replace(0, np.nan)


def _f25_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f25_margin_trend(fcf, revenue, w):
    return _slope(_f25_fcf_margin(fcf, revenue), w)


def _f25_pos_streak(s):
    pos = (s > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()


def _f25_consistency(s, w):
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _f25_ema_growth(s, w, span):
    return _f25_growth(s, w).ewm(span=span, min_periods=max(5, span // 2)).mean()


# ============================================================
# FCF revenue-scaled growth: dollar change in FCF over a year per revenue dollar
def f25ft_f25_fcf_trajectory_fcfdeltarev_252d_base_v076_signal(fcf, revenue):
    b = (fcf - fcf.shift(252)) / _mean(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo revenue-scaled change over a half year
def f25ft_f25_fcf_trajectory_ncfodeltarev_126d_base_v077_signal(ncfo, revenue):
    b = (ncfo - ncfo.shift(126)) / _mean(revenue, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin EMA crossover: fast EMA minus slow EMA of fcf/revenue
def f25ft_f25_fcf_trajectory_fcfmargemacross_base_v078_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo EMA crossover (fast minus slow level, normalized by slow)
def f25ft_f25_fcf_trajectory_ncfoemacross_base_v079_signal(ncfo):
    fast = ncfo.ewm(span=42, min_periods=21).mean()
    slow = ncfo.ewm(span=189, min_periods=90).mean()
    b = (fast - slow) / slow.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth z-score interacted with positivity consistency
def f25ft_f25_fcf_trajectory_fcfgrzcons_252d_base_v080_signal(fcf):
    g = _z(_f25_growth(fcf, 126), 252)
    cons = _f25_consistency(fcf, 252)
    b = g * cons
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF acceleration of margin: third-window curvature of fcf/revenue
def f25ft_f25_fcf_trajectory_fcfmargjolt_base_v081_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    d1 = m - m.shift(63)
    d2 = d1 - d1.shift(63)
    b = d2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF per-share momentum minus FCF momentum (per-share dilution-adjusted trajectory)
def f25ft_f25_fcf_trajectory_fcfpsvsfcf_252d_base_v082_signal(fcfps, fcf):
    gp = _f25_growth(fcfps, 252)
    gf = _f25_growth(fcf, 252)
    b = gp - gf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trend cleanliness: slope divided by max-drawdown of FCF over the window
def f25ft_f25_fcf_trajectory_fcftrendclean_252d_base_v083_signal(fcf):
    sl = _slope(fcf, 252)
    hi = fcf.rolling(252, min_periods=126).max()
    dd = (hi - fcf.rolling(252, min_periods=126).min()).abs()
    b = sl / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin Sharpe-like: mean margin over its own dispersion
def f25ft_f25_fcf_trajectory_fcfmargsharpe_252d_base_v084_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo Sharpe-like trajectory: mean ncfo growth over growth dispersion
def f25ft_f25_fcf_trajectory_ncfogrsharpe_252d_base_v085_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positivity streak length minus ncfo positivity streak length (quality gap)
def f25ft_f25_fcf_trajectory_streakgap_base_v086_signal(fcf, ncfo):
    b = (_f25_pos_streak(fcf) - _f25_pos_streak(ncfo)) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin half-vs-full year average spread (recent vs baseline margin)
def f25ft_f25_fcf_trajectory_fcfmargrecbase_base_v087_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = _mean(m, 126) - _mean(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo recent-vs-baseline level spread, scale-free
def f25ft_f25_fcf_trajectory_ncforecbase_base_v088_signal(ncfo):
    b = (_mean(ncfo, 63) - _mean(ncfo, 504)) / _mean(ncfo, 504).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trajectory curvature: second difference of FCF level scaled by mean
def f25ft_f25_fcf_trajectory_fcfcurv_252d_base_v089_signal(fcf):
    d1 = fcf - fcf.shift(126)
    d2 = d1 - d1.shift(126)
    b = d2 / _mean(fcf, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo trajectory curvature, scale-free
def f25ft_f25_fcf_trajectory_ncfocurv_252d_base_v090_signal(ncfo):
    d1 = ncfo - ncfo.shift(126)
    d2 = d1 - d1.shift(126)
    b = d2 / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin expansion hit-rate: fraction of last year margin rose vs a quarter prior
def f25ft_f25_fcf_trajectory_fcfmarghit_252d_base_v091_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    up = (m > m.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF expansion hit-rate weighted by average growth magnitude
def f25ft_f25_fcf_trajectory_fcfhitmag_252d_base_v092_signal(fcf):
    up = (fcf > fcf.shift(63)).astype(float)
    rate = up.rolling(252, min_periods=126).mean()
    mag = _f25_growth(fcf, 63).abs().rolling(252, min_periods=126).mean()
    b = rate * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin slope minus ncfo-margin slope (capex-trajectory divergence)
def f25ft_f25_fcf_trajectory_margslopediv_252d_base_v093_signal(fcf, ncfo, revenue):
    fm = _slope(fcf / revenue.replace(0, np.nan), 252)
    nm = _slope(ncfo / revenue.replace(0, np.nan), 252)
    b = fm - nm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth EMA (smoothed half-year growth)
def f25ft_f25_fcf_trajectory_fcfgrema_126d_base_v094_signal(fcf):
    b = _f25_ema_growth(fcf, 126, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth EMA (smoothed year growth)
def f25ft_f25_fcf_trajectory_ncfogrema_252d_base_v095_signal(ncfo):
    b = _f25_ema_growth(ncfo, 252, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF level vs its 252d EMA (cash trajectory displacement, scale-free)
def f25ft_f25_fcf_trajectory_fcflvldisp_252d_base_v096_signal(fcf):
    ema = fcf.ewm(span=252, min_periods=126).mean()
    b = (fcf - ema) / ema.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share level vs its 126d EMA, scale-free
def f25ft_f25_fcf_trajectory_fcfpsdisp_126d_base_v097_signal(fcfps):
    ema = fcfps.ewm(span=126, min_periods=63).mean()
    b = (fcfps - ema) / ema.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend rank interacted with sign of level (improving-and-positive)
def f25ft_f25_fcf_trajectory_fcfmargtrsign_base_v098_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    tr = _slope(m, 252)
    b = _rank(tr, 252) * np.sign(_mean(m, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF stability score: 1 minus normalized growth dispersion over two years
def f25ft_f25_fcf_trajectory_fcfstabscore_504d_base_v099_signal(fcf):
    g = _f25_growth(fcf, 63)
    disp = _std(g, 504)
    b = 1.0 / (1.0 + disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo stability score over a year
def f25ft_f25_fcf_trajectory_ncfostabscore_252d_base_v100_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    disp = _std(g, 252)
    b = 1.0 / (1.0 + disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin acceleration ranked vs history (relative margin inflection)
def f25ft_f25_fcf_trajectory_fcfmargaccrank_base_v101_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    acc = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    b = _rank(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion (fcf/ncfo) trend interacted with its level
def f25ft_f25_fcf_trajectory_convtrendlvl_252d_base_v102_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = _slope(conv, 252) * np.sign(_mean(conv, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth asymmetry: upside growth magnitude minus downside magnitude
def f25ft_f25_fcf_trajectory_fcfgrasym_252d_base_v103_signal(fcf):
    g = _f25_growth(fcf, 63)
    up = g.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-g.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth asymmetry
def f25ft_f25_fcf_trajectory_ncfograsym_252d_base_v104_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    up = g.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-g.clip(upper=0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin level percentile rank vs its own two-year window
def f25ft_f25_fcf_trajectory_fcfmargrank_504d_base_v105_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin acceleration sign-times-strength (signed inflection conviction)
def f25ft_f25_fcf_trajectory_fcfmargaccconv_base_v106_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    acc = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    b = np.sign(acc) * (acc.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF directional run quality: net up-minus-down day fraction over a half year
def f25ft_f25_fcf_trajectory_fcfnetdir_126d_base_v107_signal(fcf):
    d = fcf.diff()
    net = (np.sign(d)).rolling(126, min_periods=63).mean()
    b = net
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo level z-score minus FCF level z-score (cash-source divergence)
def f25ft_f25_fcf_trajectory_ncfofcfzdiv_504d_base_v108_signal(ncfo, fcf):
    b = _z(ncfo, 504) - _z(fcf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend times revenue-growth (growth-funded margin expansion)
def f25ft_f25_fcf_trajectory_marggrowthx_252d_base_v109_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 252)
    gr = _f25_growth(revenue, 252)
    b = np.tanh(200.0 * tr) * np.tanh(3.0 * gr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth over revenue-growth ratio (cash leverage to top-line)
def f25ft_f25_fcf_trajectory_fcfrevgrratio_252d_base_v110_signal(fcf, revenue):
    gf = _f25_growth(fcf, 252)
    gr = _f25_growth(revenue, 252)
    b = np.tanh(gf / gr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin compression flag depth: how far below own median over a half year
def f25ft_f25_fcf_trajectory_fcfmargcompress_base_v111_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    below = (med - m).clip(lower=0)
    b = below.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin expansion persistence: longest recent stretch above its median
def f25ft_f25_fcf_trajectory_fcfmargabovestrk_base_v112_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    above = (m > med).astype(float)
    grp = (above == 0).cumsum()
    b = above.groupby(grp).cumsum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF YoY growth de-meaned by its own 2y average (growth surprise)
def f25ft_f25_fcf_trajectory_fcfgrsurprise_base_v113_signal(fcf):
    g = _f25_growth(fcf, 252)
    b = g - _mean(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo YoY growth de-meaned by its own 2y average
def f25ft_f25_fcf_trajectory_ncfogrsurprise_base_v114_signal(ncfo):
    g = _f25_growth(ncfo, 252)
    b = g - _mean(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF half-year slope per unit of FCF dispersion (clean short trajectory)
def f25ft_f25_fcf_trajectory_fcfslopecln_126d_base_v115_signal(fcf):
    sl = _slope(fcf, 126)
    b = sl / _std(fcf, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo half-year slope per unit of dispersion
def f25ft_f25_fcf_trajectory_ncfoslopecln_126d_base_v116_signal(ncfo):
    sl = _slope(ncfo, 126)
    b = sl / _std(ncfo, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/revenue change interacted with revenue scale rank (big-business margin shift)
def f25ft_f25_fcf_trajectory_fcfmargchgscale_base_v117_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    chg = m - m.shift(252)
    b = chg * (_rank(revenue, 504) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positive-quarters count over two years (consistency as a count)
def f25ft_f25_fcf_trajectory_fcfposqtrs_504d_base_v118_signal(fcf):
    qpos = (fcf.rolling(63, min_periods=42).mean() > 0).astype(float)
    b = qpos.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo positive-quarters fraction interacted with growth sign
def f25ft_f25_fcf_trajectory_ncfoposqtrs_504d_base_v119_signal(ncfo):
    qpos = (ncfo.rolling(63, min_periods=42).mean() > 0).astype(float)
    frac = qpos.rolling(504, min_periods=252).mean()
    b = frac * np.sign(_f25_growth(ncfo, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin range width (max-min of fcf/revenue) — trajectory dispersion
def f25ft_f25_fcf_trajectory_fcfmargwidth_504d_base_v120_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = m.rolling(504, min_periods=252).max() - m.rolling(504, min_periods=252).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth tilt: weighted recent-minus-old growth using EMAs of different spans
def f25ft_f25_fcf_trajectory_fcfgrtilt_base_v121_signal(fcf):
    g = _f25_growth(fcf, 63)
    b = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth tilt
def f25ft_f25_fcf_trajectory_ncfogrtilt_base_v122_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    b = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Capex-efficiency drift: year-over-year change in the (fcf-ncfo)/revenue spread, ranked
def f25ft_f25_fcf_trajectory_capexefftrend_base_v123_signal(fcf, ncfo, revenue):
    spread = fcf / revenue.replace(0, np.nan) - ncfo / revenue.replace(0, np.nan)
    chg = spread - spread.shift(252)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin volatility level (instability of cash margin over a year)
def f25ft_f25_fcf_trajectory_fcfmargvol_252d_base_v124_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = _std(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth momentum minus ncfo growth momentum (which cash line accelerates)
def f25ft_f25_fcf_trajectory_fcfncfomom_base_v125_signal(fcf, ncfo):
    gf = _f25_growth(fcf, 126) - _f25_growth(fcf, 126).shift(126)
    gn = _f25_growth(ncfo, 126) - _f25_growth(ncfo, 126).shift(126)
    b = gf - gn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share growth stability (negative dispersion of per-share growth)
def f25ft_f25_fcf_trajectory_fcfpsgrstab_252d_base_v126_signal(fcfps):
    g = _f25_growth(fcfps, 63)
    b = -_std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend EMA (persistent margin-direction signal)
def f25ft_f25_fcf_trajectory_fcfmargtrendema_base_v127_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 126)
    b = tr.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF level normalized change vs revenue level normalized change (relative trajectory)
def f25ft_f25_fcf_trajectory_fcfrevnormchg_base_v128_signal(fcf, revenue):
    cf = (fcf - _mean(fcf, 252)) / _std(fcf, 252).replace(0, np.nan)
    cr = (revenue - _mean(revenue, 252)) / _std(revenue, 252).replace(0, np.nan)
    b = cf - cr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection sign-confirmed by ncfo inflection (joint direction change)
def f25ft_f25_fcf_trajectory_jointinflect_base_v129_signal(fcf, ncfo):
    fi = _slope(fcf, 63) - _slope(fcf, 252)
    ni = _slope(ncfo, 63) - _slope(ncfo, 252)
    b = np.tanh(fi / _mean(fcf, 252).abs().replace(0, np.nan)) \
        + np.tanh(ni / _mean(ncfo, 252).abs().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin quarter-over-quarter sequential change EMA (recent margin drift)
def f25ft_f25_fcf_trajectory_fcfmargseq_base_v130_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    seq = m - m.shift(63)
    b = seq.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trough-to-current span relative to peak-to-trough range (recovery position)
def f25ft_f25_fcf_trajectory_fcfrecovpos_504d_base_v131_signal(fcf):
    hi = fcf.rolling(504, min_periods=252).max()
    lo = fcf.rolling(504, min_periods=252).min()
    b = (fcf - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo recovery position within its own two-year band
def f25ft_f25_fcf_trajectory_ncforecovpos_504d_base_v132_signal(ncfo):
    hi = ncfo.rolling(504, min_periods=252).max()
    lo = ncfo.rolling(504, min_periods=252).min()
    b = (ncfo - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth crossing zero rate (how often FCF growth flips sign — instability)
def f25ft_f25_fcf_trajectory_fcfgrflip_252d_base_v133_signal(fcf):
    g = _f25_growth(fcf, 63)
    flip = (np.sign(g) != np.sign(g.shift(21))).astype(float)
    b = flip.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin improvement vs revenue-decline (efficiency in a shrinking top line)
def f25ft_f25_fcf_trajectory_fcfefficiency_base_v134_signal(fcf, revenue):
    mtr = _f25_margin_trend(fcf, revenue, 252)
    rgr = _f25_growth(revenue, 252)
    b = np.tanh(200.0 * mtr) * np.sign(-rgr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF level rank minus its own one-year-ago rank (trajectory rank momentum)
def f25ft_f25_fcf_trajectory_fcfrankmom_504d_base_v135_signal(fcf):
    r = _rank(fcf, 504)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo level rank momentum
def f25ft_f25_fcf_trajectory_ncforankmom_504d_base_v136_signal(ncfo):
    r = _rank(ncfo, 504)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/revenue acceleration EMA (smoothed margin second-derivative as a level)
def f25ft_f25_fcf_trajectory_fcfmargaccema_base_v137_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    acc = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    b = acc.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth dispersion ratio: short-window vs long-window growth volatility
def f25ft_f25_fcf_trajectory_fcfgrdispratio_base_v138_signal(fcf):
    g = _f25_growth(fcf, 21)
    short = _std(g, 63)
    long = _std(g, 252)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo trend confirmed by FCF trend: product of normalized slopes (co-movement)
def f25ft_f25_fcf_trajectory_trendcomove_252d_base_v139_signal(ncfo, fcf):
    sn = np.tanh(_slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan))
    sf = np.tanh(_slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan))
    b = sn * sf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend over a quarter (short cash-margin direction)
def f25ft_f25_fcf_trajectory_fcfmargtrend_63d_base_v140_signal(fcf, revenue):
    b = _f25_margin_trend(fcf, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth over a month relative to revenue growth over a month (fast leverage)
def f25ft_f25_fcf_trajectory_fcfrevgr_21d_base_v141_signal(fcf, revenue):
    gf = _f25_growth(fcf, 21)
    gr = _f25_growth(revenue, 21)
    b = np.tanh(2.0 * (gf - gr))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positivity recency weighting: EMA of the positivity indicator
def f25ft_f25_fcf_trajectory_fcfposema_base_v142_signal(fcf):
    pos = (fcf > 0).astype(float)
    b = pos.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin de-trended residual (margin minus its own OLS-fit level)
def f25ft_f25_fcf_trajectory_fcfmargresid_252d_base_v143_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    sl = _slope(m, 252)
    fitted = _mean(m, 252) + sl * (252.0 / 2.0)
    b = m - fitted
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trajectory consistency: correlation-like sign-agreement of level vs time
def f25ft_f25_fcf_trajectory_fcftrendconsist_base_v144_signal(fcf):
    d = np.sign(fcf.diff())
    b = d.rolling(252, min_periods=126).mean() * _std(fcf.diff(), 252).rank(pct=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo margin trend (ncfo/revenue slope) — operating cash margin trajectory
def f25ft_f25_fcf_trajectory_ncfomargtrend_252d_base_v145_signal(ncfo, revenue):
    nm = ncfo / revenue.replace(0, np.nan)
    b = _slope(nm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo margin change vs a year ago
def f25ft_f25_fcf_trajectory_ncfomargchg_252d_base_v146_signal(ncfo, revenue):
    nm = ncfo / revenue.replace(0, np.nan)
    b = nm - nm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend ranked and signed by recent FCF growth (quality-weighted)
def f25ft_f25_fcf_trajectory_fcfmargtrwt_base_v147_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 252)
    b = _rank(tr, 504) * np.tanh(_f25_growth(fcf, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF level acceleration: difference of two consecutive half-year slopes
def f25ft_f25_fcf_trajectory_fcfslopeacc_base_v148_signal(fcf):
    sl = _slope(fcf, 126) / _mean(fcf, 126).abs().replace(0, np.nan)
    b = sl - sl.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share trajectory: per-share margin proxy trend (fcfps vs revenue scale)
def f25ft_f25_fcf_trajectory_fcfpstrendrev_base_v149_signal(fcfps, revenue):
    ratio = fcfps / (revenue / 1e8).replace(0, np.nan)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Combined trajectory quality: growth EMA x consistency x margin-trend sign
def f25ft_f25_fcf_trajectory_trajqualcomp_base_v150_signal(fcf, revenue):
    g = _f25_ema_growth(fcf, 126, 63)
    cons = _f25_consistency(fcf, 252)
    mtr = np.tanh(200.0 * _f25_margin_trend(fcf, revenue, 252))
    b = np.tanh(g) * cons + 0.5 * mtr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25ft_f25_fcf_trajectory_fcfdeltarev_252d_base_v076_signal,
    f25ft_f25_fcf_trajectory_ncfodeltarev_126d_base_v077_signal,
    f25ft_f25_fcf_trajectory_fcfmargemacross_base_v078_signal,
    f25ft_f25_fcf_trajectory_ncfoemacross_base_v079_signal,
    f25ft_f25_fcf_trajectory_fcfgrzcons_252d_base_v080_signal,
    f25ft_f25_fcf_trajectory_fcfmargjolt_base_v081_signal,
    f25ft_f25_fcf_trajectory_fcfpsvsfcf_252d_base_v082_signal,
    f25ft_f25_fcf_trajectory_fcftrendclean_252d_base_v083_signal,
    f25ft_f25_fcf_trajectory_fcfmargsharpe_252d_base_v084_signal,
    f25ft_f25_fcf_trajectory_ncfogrsharpe_252d_base_v085_signal,
    f25ft_f25_fcf_trajectory_streakgap_base_v086_signal,
    f25ft_f25_fcf_trajectory_fcfmargrecbase_base_v087_signal,
    f25ft_f25_fcf_trajectory_ncforecbase_base_v088_signal,
    f25ft_f25_fcf_trajectory_fcfcurv_252d_base_v089_signal,
    f25ft_f25_fcf_trajectory_ncfocurv_252d_base_v090_signal,
    f25ft_f25_fcf_trajectory_fcfmarghit_252d_base_v091_signal,
    f25ft_f25_fcf_trajectory_fcfhitmag_252d_base_v092_signal,
    f25ft_f25_fcf_trajectory_margslopediv_252d_base_v093_signal,
    f25ft_f25_fcf_trajectory_fcfgrema_126d_base_v094_signal,
    f25ft_f25_fcf_trajectory_ncfogrema_252d_base_v095_signal,
    f25ft_f25_fcf_trajectory_fcflvldisp_252d_base_v096_signal,
    f25ft_f25_fcf_trajectory_fcfpsdisp_126d_base_v097_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrsign_base_v098_signal,
    f25ft_f25_fcf_trajectory_fcfstabscore_504d_base_v099_signal,
    f25ft_f25_fcf_trajectory_ncfostabscore_252d_base_v100_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccrank_base_v101_signal,
    f25ft_f25_fcf_trajectory_convtrendlvl_252d_base_v102_signal,
    f25ft_f25_fcf_trajectory_fcfgrasym_252d_base_v103_signal,
    f25ft_f25_fcf_trajectory_ncfograsym_252d_base_v104_signal,
    f25ft_f25_fcf_trajectory_fcfmargrank_504d_base_v105_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccconv_base_v106_signal,
    f25ft_f25_fcf_trajectory_fcfnetdir_126d_base_v107_signal,
    f25ft_f25_fcf_trajectory_ncfofcfzdiv_504d_base_v108_signal,
    f25ft_f25_fcf_trajectory_marggrowthx_252d_base_v109_signal,
    f25ft_f25_fcf_trajectory_fcfrevgrratio_252d_base_v110_signal,
    f25ft_f25_fcf_trajectory_fcfmargcompress_base_v111_signal,
    f25ft_f25_fcf_trajectory_fcfmargabovestrk_base_v112_signal,
    f25ft_f25_fcf_trajectory_fcfgrsurprise_base_v113_signal,
    f25ft_f25_fcf_trajectory_ncfogrsurprise_base_v114_signal,
    f25ft_f25_fcf_trajectory_fcfslopecln_126d_base_v115_signal,
    f25ft_f25_fcf_trajectory_ncfoslopecln_126d_base_v116_signal,
    f25ft_f25_fcf_trajectory_fcfmargchgscale_base_v117_signal,
    f25ft_f25_fcf_trajectory_fcfposqtrs_504d_base_v118_signal,
    f25ft_f25_fcf_trajectory_ncfoposqtrs_504d_base_v119_signal,
    f25ft_f25_fcf_trajectory_fcfmargwidth_504d_base_v120_signal,
    f25ft_f25_fcf_trajectory_fcfgrtilt_base_v121_signal,
    f25ft_f25_fcf_trajectory_ncfogrtilt_base_v122_signal,
    f25ft_f25_fcf_trajectory_capexefftrend_base_v123_signal,
    f25ft_f25_fcf_trajectory_fcfmargvol_252d_base_v124_signal,
    f25ft_f25_fcf_trajectory_fcfncfomom_base_v125_signal,
    f25ft_f25_fcf_trajectory_fcfpsgrstab_252d_base_v126_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendema_base_v127_signal,
    f25ft_f25_fcf_trajectory_fcfrevnormchg_base_v128_signal,
    f25ft_f25_fcf_trajectory_jointinflect_base_v129_signal,
    f25ft_f25_fcf_trajectory_fcfmargseq_base_v130_signal,
    f25ft_f25_fcf_trajectory_fcfrecovpos_504d_base_v131_signal,
    f25ft_f25_fcf_trajectory_ncforecovpos_504d_base_v132_signal,
    f25ft_f25_fcf_trajectory_fcfgrflip_252d_base_v133_signal,
    f25ft_f25_fcf_trajectory_fcfefficiency_base_v134_signal,
    f25ft_f25_fcf_trajectory_fcfrankmom_504d_base_v135_signal,
    f25ft_f25_fcf_trajectory_ncforankmom_504d_base_v136_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccema_base_v137_signal,
    f25ft_f25_fcf_trajectory_fcfgrdispratio_base_v138_signal,
    f25ft_f25_fcf_trajectory_trendcomove_252d_base_v139_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_63d_base_v140_signal,
    f25ft_f25_fcf_trajectory_fcfrevgr_21d_base_v141_signal,
    f25ft_f25_fcf_trajectory_fcfposema_base_v142_signal,
    f25ft_f25_fcf_trajectory_fcfmargresid_252d_base_v143_signal,
    f25ft_f25_fcf_trajectory_fcftrendconsist_base_v144_signal,
    f25ft_f25_fcf_trajectory_ncfomargtrend_252d_base_v145_signal,
    f25ft_f25_fcf_trajectory_ncfomargchg_252d_base_v146_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrwt_base_v147_signal,
    f25ft_f25_fcf_trajectory_fcfslopeacc_base_v148_signal,
    f25ft_f25_fcf_trajectory_fcfpstrendrev_base_v149_signal,
    f25ft_f25_fcf_trajectory_trajqualcomp_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_FCF_TRAJECTORY_REGISTRY_076_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    fcf = _fund(3, n, base=8e7, drift=0.0, vol=0.55, allow_neg=True).rename("fcf")
    fcfps = _fund(5, n, base=3.0, drift=0.0, vol=0.55, allow_neg=True).rename("fcfps")
    ncfo = _fund(7, n, base=1.2e8, drift=0.0, vol=0.55, allow_neg=True).rename("ncfo")
    revenue = _fund(4, n, base=5e8, drift=0.01, vol=0.30).rename("revenue")

    cols = {"fcf": fcf, "fcfps": fcfps, "ncfo": ncfo, "revenue": revenue}

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

    print("OK f25_fcf_trajectory_base_076_150_claude: %d features pass" % n_features)
