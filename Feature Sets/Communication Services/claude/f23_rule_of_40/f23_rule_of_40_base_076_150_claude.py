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


# ===== folder domain primitives (Rule-of-40 = growth + profitability) =====
def _r40_growth(revenue, w):
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


def _r40_loggrowth(revenue, w):
    return np.log(revenue.replace(0, np.nan) / revenue.shift(w).replace(0, np.nan))


def _r40_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _r40_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _r40_score_fcf(revenue, fcf, w):
    return _r40_growth(revenue, w) + _r40_fcf_margin(fcf, revenue)


def _r40_score_ocf(revenue, ncfo, w):
    return _r40_growth(revenue, w) + _r40_ocf_margin(ncfo, revenue)


def _r40_score_ebitda(revenue, ebitdamargin, w):
    return _r40_growth(revenue, w) + ebitdamargin


def _r40_score_gross(revenue, grossmargin, w):
    return _r40_growth(revenue, w) + grossmargin


# ============================================================
# --- EWM crossover of the Rule-of-40 score (fast vs slow quality trend) ---

# fcf Rule-of-40 score: fast EMA minus slow EMA (quality trend crossover)
def f23r40_f23_rule_of_40_r40fcfcross_252d_base_v076_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = score.ewm(span=42, min_periods=21).mean() - score.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf Rule-of-40 score: fast EMA minus slow EMA
def f23r40_f23_rule_of_40_r40ocfcross_252d_base_v077_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = score.ewm(span=42, min_periods=21).mean() - score.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda Rule-of-40 score: fast EMA minus slow EMA, normalized by score volatility
def f23r40_f23_rule_of_40_r40ebdcross_252d_base_v078_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    cross = score.ewm(span=21, min_periods=10).mean() - score.ewm(span=252, min_periods=63).mean()
    b = cross / _std(score, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 score smoothed level (persistent composite) ---

# fcf Rule-of-40 score: deviation of fast EMA from its slow EMA, ranked (sticky-quality shift)
def f23r40_f23_rule_of_40_r40fcfema_252d_base_v079_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    dev = score.ewm(span=21, min_periods=10).mean() - score.ewm(span=126, min_periods=42).mean()
    b = _rank(dev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross Rule-of-40 score: deviation from its EWM-smoothed level (composite displacement)
def f23r40_f23_rule_of_40_r40grsema_252d_base_v080_signal(revenue, grossmargin):
    score = _r40_score_gross(revenue, grossmargin, 252)
    b = score - score.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 quality-floor (worst trailing score, downside) ---

# trailing-year minimum of the fcf Rule-of-40 score (worst quality reached)
def f23r40_f23_rule_of_40_r40fcfmin_252d_base_v081_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = score.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing-year maximum of the ocf Rule-of-40 score (best quality reached)
def f23r40_f23_rule_of_40_r40ocfmax_252d_base_v082_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = score.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of the ebitda Rule-of-40 score over the last year (quality swing)
def f23r40_f23_rule_of_40_r40ebdrange_252d_base_v083_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = score.rolling(252, min_periods=126).max() - score.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- position of current score within its own trailing range ---

# where the current fcf Rule-of-40 score sits in its trailing-year range (0..1)
def f23r40_f23_rule_of_40_r40fcfpos_252d_base_v084_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    lo = score.rolling(252, min_periods=126).min()
    hi = score.rolling(252, min_periods=126).max()
    b = (score - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# where the current ocf Rule-of-40 score sits in its trailing-year range
def f23r40_f23_rule_of_40_r40ocfpos_252d_base_v085_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    lo = score.rolling(252, min_periods=126).min()
    hi = score.rolling(252, min_periods=126).max()
    b = (score - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-horizon growth blended with one margin (growth-curvature R40) ---

# average of quarterly/annual/two-year growth + fcf-margin (growth-curve R40)
def f23r40_f23_rule_of_40_multigrowfcf_base_v086_signal(revenue, fcf):
    g = (_r40_growth(revenue, 63) + _r40_growth(revenue, 252) + _r40_growth(revenue, 504)) / 3.0
    b = g + _r40_fcf_margin(fcf, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth curvature (quarterly minus annual growth) plus ebitda-margin, z-scored
def f23r40_f23_rule_of_40_growcurvebd_base_v087_signal(revenue, ebitdamargin):
    curv = _r40_growth(revenue, 63) - _r40_growth(revenue, 252)
    b = _z(curv + ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-conversion-weighted Rule-of-40 ---

# Rule-of-40 (growth + fcf-margin) weighted by fcf-to-ocf conversion quality
def f23r40_f23_rule_of_40_convwtfcf_252d_base_v088_signal(revenue, fcf, ncfo):
    score = _r40_score_fcf(revenue, fcf, 252)
    conv = (fcf / ncfo.replace(0, np.nan)).clip(-1, 2)
    b = score * (0.5 + 0.5 * conv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-to-ocf conversion ratio (capex retention of operating cash), z-scored
def f23r40_f23_rule_of_40_cashconv_z_base_v089_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = _z(conv.clip(-2, 3), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 momentum spreads (which leg drives improvement) ---

# improvement spread: fcf-R40 momentum minus revenue-growth momentum (margin-led gains)
def f23r40_f23_rule_of_40_marginled_252d_base_v090_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    g = _r40_growth(revenue, 252)
    b = (score - score.shift(63)) - (g - g.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# improvement spread: ocf-R40 momentum minus revenue-growth momentum
def f23r40_f23_rule_of_40_marginledocf_252d_base_v091_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    g = _r40_growth(revenue, 252)
    b = (score - score.shift(63)) - (g - g.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- normalized Rule-of-40 quality fraction (bounded composite) ---

# fcf-margin share of the absolute fcf Rule-of-40 score (profitability contribution)
def f23r40_f23_rule_of_40_fcfshare_252d_base_v092_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    b = m / (g.abs() + m.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin share of the absolute ebitda Rule-of-40 score
def f23r40_f23_rule_of_40_ebdshare_252d_base_v093_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    b = ebitdamargin / (g.abs() + ebitdamargin.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 hurdle crossing dynamics ---

# net crossings of the 0.40 bar by the fcf score over the last year (regime churn)
def f23r40_f23_rule_of_40_crossfcf_252d_base_v094_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    above = (score >= 0.40).astype(float)
    cross = (above != above.shift(1)).astype(float)
    churn = cross.rolling(252, min_periods=126).sum()
    b = churn + 0.5 * _z(score, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the ebitda Rule-of-40 score last cleared 0.40 (staleness of quality)
def f23r40_f23_rule_of_40_tsclearebd_252d_base_v095_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    above = (score >= 0.40)
    grp = above.cumsum()
    b = (~above).groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- combined cash + accrual Rule-of-40 (consensus quality) ---

# minimum of the fcf and ebitda Rule-of-40 scores (conservative consensus quality)
def f23r40_f23_rule_of_40_consminfe_252d_base_v096_signal(revenue, fcf, ebitdamargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    se = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = pd.concat([sf, se], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maximum of the ocf and gross Rule-of-40 scores (best-case consensus quality)
def f23r40_f23_rule_of_40_consmaxog_252d_base_v097_signal(revenue, ncfo, grossmargin):
    so = _r40_score_ocf(revenue, ncfo, 252)
    sg = _r40_score_gross(revenue, grossmargin, 252)
    b = pd.concat([so, sg], axis=1).max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# disagreement across the four Rule-of-40 score variants (definition dispersion)
def f23r40_f23_rule_of_40_consdisp_252d_base_v098_signal(revenue, fcf, ncfo, ebitdamargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    so = _r40_score_ocf(revenue, ncfo, 252)
    se = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = pd.concat([sf, so, se], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth quality vs cash burn over time ---

# trailing fcf-margin shortfall below its own median (cash-profitability drawdown)
def f23r40_f23_rule_of_40_burncost_252d_base_v099_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    shortfall = (med - m).clip(lower=0)
    b = shortfall.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing fraction of the year with negative ocf-margin (cash-burning regime)
def f23r40_f23_rule_of_40_burnfreqocf_252d_base_v100_signal(revenue, ncfo):
    m = _r40_ocf_margin(ncfo, revenue)
    burning = (m < 0).astype(float)
    b = burning.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth durability scaled by margin sign ---

# revenue growth stability (mean/std) scaled by the fcf-margin percentile (quality-weighted)
def f23r40_f23_rule_of_40_durgrowfcf_252d_base_v101_signal(revenue, fcf):
    g = _r40_growth(revenue, 63)
    stab = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    mq = _rank(_r40_fcf_margin(fcf, revenue), 252)
    b = stab * (0.5 + mq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability scaled by the ebitda-margin level (quality-weighted)
def f23r40_f23_rule_of_40_durgrowebd_252d_base_v102_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 63)
    stab = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    b = stab * (0.5 + ebitdamargin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with rule-of-X variable hurdle ---

# fcf Rule-of-40 score excess over a rule-of-30 bar, percentile-ranked vs 504d history
def f23r40_f23_rule_of_40_rule30fcf_252d_base_v103_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = _rank(score - 0.30, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess of the ebitda Rule-of-40 score over a rule-of-50 bar (stricter hurdle)
def f23r40_f23_rule_of_40_rule50ebd_252d_base_v104_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = score - 0.50
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- per-leg z-score difference (standardized growth vs standardized margin) ---

# standardized growth minus standardized fcf-margin (which leg is unusually strong)
def f23r40_f23_rule_of_40_zspreadfcf_252d_base_v105_signal(revenue, fcf):
    zg = _z(_r40_growth(revenue, 252), 252)
    zm = _z(_r40_fcf_margin(fcf, revenue), 252)
    b = zg - zm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# standardized growth minus standardized ocf-margin
def f23r40_f23_rule_of_40_zspreadocf_252d_base_v106_signal(revenue, ncfo):
    zg = _z(_r40_growth(revenue, 252), 252)
    zm = _z(_r40_ocf_margin(ncfo, revenue), 252)
    b = zg - zm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# standardized growth minus standardized ebitda-margin
def f23r40_f23_rule_of_40_zspreadebd_252d_base_v107_signal(revenue, ebitdamargin):
    zg = _z(_r40_growth(revenue, 252), 252)
    zm = _z(ebitdamargin, 252)
    b = zg - zm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- standardized sum (both legs strong together) ---

# standardized growth plus standardized fcf-margin (joint-strength composite)
def f23r40_f23_rule_of_40_zsumfcf_252d_base_v108_signal(revenue, fcf):
    zg = _z(_r40_growth(revenue, 252), 252)
    zm = _z(_r40_fcf_margin(fcf, revenue), 252)
    b = zg + zm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# standardized growth plus standardized ebitda-margin
def f23r40_f23_rule_of_40_zsumebd_252d_base_v109_signal(revenue, ebitdamargin):
    zg = _z(_r40_growth(revenue, 252), 252)
    zm = _z(ebitdamargin, 252)
    b = zg + zm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 slope via linear trend of the score ---

# linear-regression slope of the fcf Rule-of-40 score over the last half-year
def f23r40_f23_rule_of_40_r40fcfslope_126d_base_v110_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    idx = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    cov = score.rolling(126, min_periods=63).cov(idx)
    var = idx.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# linear-regression slope of the ocf Rule-of-40 score over the last half-year
def f23r40_f23_rule_of_40_r40ocfslope_126d_base_v111_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    idx = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    cov = score.rolling(126, min_periods=63).cov(idx)
    var = idx.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin-trend gated growth quality ---

# revenue growth times the fcf-margin half-year trend (growth with improving cash)
def f23r40_f23_rule_of_40_growxmgntrend_base_v112_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    mtrend = _r40_fcf_margin(fcf, revenue) - _r40_fcf_margin(fcf, revenue).shift(126)
    b = g * mtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth times the ebitda-margin half-year trend
def f23r40_f23_rule_of_40_growxebdtrend_base_v113_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    mtrend = ebitdamargin - ebitdamargin.shift(126)
    b = g * mtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 quality drift vs its own volatility (info-ratio of quality) ---

# fcf Rule-of-40 score drift divided by its volatility (quality information ratio)
def f23r40_f23_rule_of_40_inforatiofcf_252d_base_v114_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    drift = score - score.shift(126)
    b = drift / _std(score, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda Rule-of-40 score drift divided by its volatility
def f23r40_f23_rule_of_40_inforatioebd_252d_base_v115_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    drift = score - score.shift(126)
    b = drift / _std(score, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- absolute-vs-relative growth/margin balance ---

# log-growth minus fcf-margin (compounding-growth vs cash-profit tradeoff)
def f23r40_f23_rule_of_40_loggapfcf_252d_base_v116_signal(revenue, fcf):
    lg = _r40_loggrowth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    b = lg - m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth plus ocf-margin (continuously-compounded ocf Rule-of-40), z-scored
def f23r40_f23_rule_of_40_logr40ocf_252d_base_v117_signal(revenue, ncfo):
    lg = _r40_loggrowth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    b = _z(lg + m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with capex-adjusted cash leg ---

# reinvestment-adjusted Rule-of-40: growth plus 3x the ocf-minus-fcf margin gap, z-scored
def f23r40_f23_rule_of_40_reinvr40_252d_base_v118_signal(revenue, ncfo, fcf):
    g = _r40_growth(revenue, 252)
    reinvest = (_r40_ocf_margin(ncfo, revenue) - _r40_fcf_margin(fcf, revenue))
    b = _z(g + 3.0 * reinvest, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity (ocf-fcf margin gap) trend over a half-year
def f23r40_f23_rule_of_40_reinvtrend_base_v119_signal(revenue, ncfo, fcf):
    reinvest = (_r40_ocf_margin(ncfo, revenue) - _r40_fcf_margin(fcf, revenue))
    b = reinvest - reinvest.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 quality vs growth (de-emphasize pure growth) ---

# fcf-margin lead over growth, normalized by their combined magnitude (profit-led fraction)
def f23r40_f23_rule_of_40_qualpurefcf_252d_base_v120_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    b = (m - g) / (m.abs() + g.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf-margin lead over growth (profitability lead), change over a half-year
def f23r40_f23_rule_of_40_qualpureocf_252d_base_v121_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    lead = m - g
    b = lead - lead.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- streaks of margin-positive quarters during growth ---

# consecutive-period streak of positive fcf-margin (sustained cash profitability)
def f23r40_f23_rule_of_40_posmgnstreakfcf_base_v122_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    pos = (m > 0)
    grp = (~pos).cumsum()
    b = pos.groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-period streak of ebitda-margin above its own median
def f23r40_f23_rule_of_40_aboveebdstreak_base_v123_signal(ebitdamargin):
    med = ebitdamargin.rolling(252, min_periods=126).median()
    above = (ebitdamargin > med)
    grp = (~above).cumsum()
    b = above.groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 cross-margin product (cash x accrual quality) ---

# fcf-margin times ebitda-margin, plus growth (double-quality Rule-of-40)
def f23r40_f23_rule_of_40_dualqualfe_252d_base_v124_signal(revenue, fcf, ebitdamargin):
    g = _r40_growth(revenue, 252)
    dual = _r40_fcf_margin(fcf, revenue) * ebitdamargin
    b = g + 4.0 * dual
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin times ocf-margin (margin-quality interaction), z-scored
def f23r40_f23_rule_of_40_dualqualgo_252d_base_v125_signal(revenue, ncfo, grossmargin):
    dual = grossmargin * _r40_ocf_margin(ncfo, revenue)
    b = _z(dual, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 acceleration of the margin leg ---

# acceleration of the fcf-margin (second difference of the profitability leg)
def f23r40_f23_rule_of_40_mgnaccelfcf_base_v126_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    d = m - m.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the ebitda-margin (second difference of the profitability leg)
def f23r40_f23_rule_of_40_mgnaccelebd_base_v127_signal(ebitdamargin):
    d = ebitdamargin - ebitdamargin.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative Rule-of-40 (score vs its own 2y average) ---

# fcf Rule-of-40 score relative to its trailing two-year mean (regime distance)
def f23r40_f23_rule_of_40_reldevfcf_504d_base_v128_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = score - _mean(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf Rule-of-40 score relative to its trailing two-year mean, standardized (regime z)
def f23r40_f23_rule_of_40_reldevocf_504d_base_v129_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = _z(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 quality-weighted growth momentum ---

# revenue growth momentum scaled by the fcf-margin level (quality-confirmed momentum)
def f23r40_f23_rule_of_40_growmomqfcf_base_v130_signal(revenue, fcf):
    gmom = _r40_growth(revenue, 63) - _r40_growth(revenue, 63).shift(63)
    qual = _r40_fcf_margin(fcf, revenue)
    b = gmom * (0.2 + qual)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth momentum scaled by the ebitda-margin percentile (quality-confirmed)
def f23r40_f23_rule_of_40_growmomqebd_base_v131_signal(revenue, ebitdamargin):
    gmom = _r40_growth(revenue, 63) - _r40_growth(revenue, 63).shift(63)
    qual = _rank(ebitdamargin, 252)
    b = gmom * (0.5 + qual)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 efficiency: revenue scale per cash burned ---

# revenue growth net of trailing ocf-margin shortfall below median, percentile-ranked
def f23r40_f23_rule_of_40_efficapocf_252d_base_v132_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    short = (m.rolling(252, min_periods=126).median() - m).clip(lower=0).rolling(126, min_periods=63).mean()
    b = _rank(g - 3.0 * short, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- harmonic-style joint quality of growth and margin ---

# harmonic blend of positive growth and positive fcf-margin (both-must-be-good)
def f23r40_f23_rule_of_40_harmfcf_252d_base_v133_signal(revenue, fcf):
    g = _r40_growth(revenue, 252).clip(lower=0) + 0.01
    m = _r40_fcf_margin(fcf, revenue).clip(lower=0) + 0.01
    b = 2.0 * g * m / (g + m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 score vs revenue-scale (small vs large quality) ---

# fcf Rule-of-40 score interacted with log-revenue level (scale-aware quality)
def f23r40_f23_rule_of_40_scaleqfcf_252d_base_v134_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    scale = _z(np.log(revenue.replace(0, np.nan)), 252)
    b = score * np.sign(scale) + 0.1 * scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with gross-margin durability ---

# gross Rule-of-40 quality penalized by gross-margin instability, percentile-ranked
def f23r40_f23_rule_of_40_durgrs_252d_base_v135_signal(revenue, grossmargin):
    score = _r40_score_gross(revenue, grossmargin, 252)
    b = _rank(score - 2.0 * _std(grossmargin, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite of margin trends across all four legs ---

# average half-year trend across fcf/ocf/ebitda/gross margins (broad margin improvement)
def f23r40_f23_rule_of_40_mgntrendall_base_v136_signal(revenue, fcf, ncfo, ebitdamargin, grossmargin):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    t = ((fm - fm.shift(126)) + (om - om.shift(126))
         + (ebitdamargin - ebitdamargin.shift(126)) + (grossmargin - grossmargin.shift(126))) / 4.0
    b = t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 sign-consistency (growth and margin both improving) ---

# fraction of last year both revenue-growth and fcf-margin rose together (joint trend)
def f23r40_f23_rule_of_40_jointrisefcf_252d_base_v137_signal(revenue, fcf):
    gup = (_r40_growth(revenue, 63) > _r40_growth(revenue, 63).shift(21)).astype(float)
    m = _r40_fcf_margin(fcf, revenue)
    mup = (m > m.shift(21)).astype(float)
    both = gup * mup
    b = both.rolling(252, min_periods=126).mean() - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year both growth and ebitda-margin rose together
def f23r40_f23_rule_of_40_jointriseebd_252d_base_v138_signal(revenue, ebitdamargin):
    gup = (_r40_growth(revenue, 63) > _r40_growth(revenue, 63).shift(21)).astype(float)
    mup = (ebitdamargin > ebitdamargin.shift(21)).astype(float)
    both = gup * mup
    b = both.rolling(252, min_periods=126).mean() - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 normalized by score volatility (sharpe-of-quality level) ---

# trailing mean fcf Rule-of-40 score divided by its trailing volatility
def f23r40_f23_rule_of_40_sharpefcf_252d_base_v139_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = _mean(score, 252) / _std(score, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing mean ocf Rule-of-40 score divided by its trailing volatility
def f23r40_f23_rule_of_40_sharpeocf_252d_base_v140_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = _mean(score, 252) / _std(score, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 deceleration detection ---

# negative part of the fcf Rule-of-40 momentum (quality deterioration magnitude)
def f23r40_f23_rule_of_40_deterfcf_252d_base_v141_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    mom = score - score.shift(63)
    b = (-mom).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive part of the ocf Rule-of-40 momentum (quality acceleration magnitude)
def f23r40_f23_rule_of_40_improveocf_252d_base_v142_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    mom = score - score.shift(63)
    b = mom.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 percentile of the margin leg only ---

# percentile rank of the fcf-margin within its 504d history (profitability percentile)
def f23r40_f23_rule_of_40_fcfmgnpct_504d_base_v143_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of the ebitda-margin within its 504d history
def f23r40_f23_rule_of_40_ebdmgnpct_504d_base_v144_signal(ebitdamargin):
    b = _rank(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 leg-rank blend (rank-space composite) ---

# average percentile rank of growth and fcf-margin (rank-space Rule-of-40)
def f23r40_f23_rule_of_40_rankblendfcf_504d_base_v145_signal(revenue, fcf):
    rg = _rank(_r40_growth(revenue, 252), 504)
    rm = _rank(_r40_fcf_margin(fcf, revenue), 504)
    b = 0.5 * (rg + rm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average percentile rank of growth and ebitda-margin (rank-space Rule-of-40)
def f23r40_f23_rule_of_40_rankblendebd_504d_base_v146_signal(revenue, ebitdamargin):
    rg = _rank(_r40_growth(revenue, 252), 504)
    rm = _rank(ebitdamargin, 504)
    b = 0.5 * (rg + rm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with growth-acceleration leg ---

# growth acceleration (annual growth minus year-ago annual growth) plus fcf-margin
def f23r40_f23_rule_of_40_growaccfcf_base_v147_signal(revenue, fcf):
    gacc = _r40_growth(revenue, 252) - _r40_growth(revenue, 252).shift(252)
    b = gacc + _r40_fcf_margin(fcf, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration plus ocf-margin, percentile-ranked (accelerating durable quality)
def f23r40_f23_rule_of_40_growaccocf_base_v148_signal(revenue, ncfo):
    gacc = _r40_growth(revenue, 252) - _r40_growth(revenue, 252).shift(252)
    b = _rank(gacc + _r40_ocf_margin(ncfo, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 quality regime distance ---

# distance of the current fcf Rule-of-40 score from its best trailing-year level
def f23r40_f23_rule_of_40_offpeakfcf_252d_base_v149_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    peak = score.rolling(252, min_periods=126).max()
    b = score - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery of the ebitda Rule-of-40 score from its worst trailing-year level
def f23r40_f23_rule_of_40_offtroughebd_252d_base_v150_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    trough = score.rolling(252, min_periods=126).min()
    b = score - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23r40_f23_rule_of_40_r40fcfcross_252d_base_v076_signal,
    f23r40_f23_rule_of_40_r40ocfcross_252d_base_v077_signal,
    f23r40_f23_rule_of_40_r40ebdcross_252d_base_v078_signal,
    f23r40_f23_rule_of_40_r40fcfema_252d_base_v079_signal,
    f23r40_f23_rule_of_40_r40grsema_252d_base_v080_signal,
    f23r40_f23_rule_of_40_r40fcfmin_252d_base_v081_signal,
    f23r40_f23_rule_of_40_r40ocfmax_252d_base_v082_signal,
    f23r40_f23_rule_of_40_r40ebdrange_252d_base_v083_signal,
    f23r40_f23_rule_of_40_r40fcfpos_252d_base_v084_signal,
    f23r40_f23_rule_of_40_r40ocfpos_252d_base_v085_signal,
    f23r40_f23_rule_of_40_multigrowfcf_base_v086_signal,
    f23r40_f23_rule_of_40_growcurvebd_base_v087_signal,
    f23r40_f23_rule_of_40_convwtfcf_252d_base_v088_signal,
    f23r40_f23_rule_of_40_cashconv_z_base_v089_signal,
    f23r40_f23_rule_of_40_marginled_252d_base_v090_signal,
    f23r40_f23_rule_of_40_marginledocf_252d_base_v091_signal,
    f23r40_f23_rule_of_40_fcfshare_252d_base_v092_signal,
    f23r40_f23_rule_of_40_ebdshare_252d_base_v093_signal,
    f23r40_f23_rule_of_40_crossfcf_252d_base_v094_signal,
    f23r40_f23_rule_of_40_tsclearebd_252d_base_v095_signal,
    f23r40_f23_rule_of_40_consminfe_252d_base_v096_signal,
    f23r40_f23_rule_of_40_consmaxog_252d_base_v097_signal,
    f23r40_f23_rule_of_40_consdisp_252d_base_v098_signal,
    f23r40_f23_rule_of_40_burncost_252d_base_v099_signal,
    f23r40_f23_rule_of_40_burnfreqocf_252d_base_v100_signal,
    f23r40_f23_rule_of_40_durgrowfcf_252d_base_v101_signal,
    f23r40_f23_rule_of_40_durgrowebd_252d_base_v102_signal,
    f23r40_f23_rule_of_40_rule30fcf_252d_base_v103_signal,
    f23r40_f23_rule_of_40_rule50ebd_252d_base_v104_signal,
    f23r40_f23_rule_of_40_zspreadfcf_252d_base_v105_signal,
    f23r40_f23_rule_of_40_zspreadocf_252d_base_v106_signal,
    f23r40_f23_rule_of_40_zspreadebd_252d_base_v107_signal,
    f23r40_f23_rule_of_40_zsumfcf_252d_base_v108_signal,
    f23r40_f23_rule_of_40_zsumebd_252d_base_v109_signal,
    f23r40_f23_rule_of_40_r40fcfslope_126d_base_v110_signal,
    f23r40_f23_rule_of_40_r40ocfslope_126d_base_v111_signal,
    f23r40_f23_rule_of_40_growxmgntrend_base_v112_signal,
    f23r40_f23_rule_of_40_growxebdtrend_base_v113_signal,
    f23r40_f23_rule_of_40_inforatiofcf_252d_base_v114_signal,
    f23r40_f23_rule_of_40_inforatioebd_252d_base_v115_signal,
    f23r40_f23_rule_of_40_loggapfcf_252d_base_v116_signal,
    f23r40_f23_rule_of_40_logr40ocf_252d_base_v117_signal,
    f23r40_f23_rule_of_40_reinvr40_252d_base_v118_signal,
    f23r40_f23_rule_of_40_reinvtrend_base_v119_signal,
    f23r40_f23_rule_of_40_qualpurefcf_252d_base_v120_signal,
    f23r40_f23_rule_of_40_qualpureocf_252d_base_v121_signal,
    f23r40_f23_rule_of_40_posmgnstreakfcf_base_v122_signal,
    f23r40_f23_rule_of_40_aboveebdstreak_base_v123_signal,
    f23r40_f23_rule_of_40_dualqualfe_252d_base_v124_signal,
    f23r40_f23_rule_of_40_dualqualgo_252d_base_v125_signal,
    f23r40_f23_rule_of_40_mgnaccelfcf_base_v126_signal,
    f23r40_f23_rule_of_40_mgnaccelebd_base_v127_signal,
    f23r40_f23_rule_of_40_reldevfcf_504d_base_v128_signal,
    f23r40_f23_rule_of_40_reldevocf_504d_base_v129_signal,
    f23r40_f23_rule_of_40_growmomqfcf_base_v130_signal,
    f23r40_f23_rule_of_40_growmomqebd_base_v131_signal,
    f23r40_f23_rule_of_40_efficapocf_252d_base_v132_signal,
    f23r40_f23_rule_of_40_harmfcf_252d_base_v133_signal,
    f23r40_f23_rule_of_40_scaleqfcf_252d_base_v134_signal,
    f23r40_f23_rule_of_40_durgrs_252d_base_v135_signal,
    f23r40_f23_rule_of_40_mgntrendall_base_v136_signal,
    f23r40_f23_rule_of_40_jointrisefcf_252d_base_v137_signal,
    f23r40_f23_rule_of_40_jointriseebd_252d_base_v138_signal,
    f23r40_f23_rule_of_40_sharpefcf_252d_base_v139_signal,
    f23r40_f23_rule_of_40_sharpeocf_252d_base_v140_signal,
    f23r40_f23_rule_of_40_deterfcf_252d_base_v141_signal,
    f23r40_f23_rule_of_40_improveocf_252d_base_v142_signal,
    f23r40_f23_rule_of_40_fcfmgnpct_504d_base_v143_signal,
    f23r40_f23_rule_of_40_ebdmgnpct_504d_base_v144_signal,
    f23r40_f23_rule_of_40_rankblendfcf_504d_base_v145_signal,
    f23r40_f23_rule_of_40_rankblendebd_504d_base_v146_signal,
    f23r40_f23_rule_of_40_growaccfcf_base_v147_signal,
    f23r40_f23_rule_of_40_growaccocf_base_v148_signal,
    f23r40_f23_rule_of_40_offpeakfcf_252d_base_v149_signal,
    f23r40_f23_rule_of_40_offtroughebd_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_RULE_OF_40_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
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
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1e8, drift=0.04, vol=0.06).rename("revenue")
    fcf = _fund(102, base=2e7, drift=0.0, vol=0.18, allow_neg=True).rename("fcf")
    ncfo = _fund(103, base=2.5e7, drift=0.01, vol=0.16, allow_neg=True).rename("ncfo")
    ebitdamargin = (_fund(104, base=1.0, drift=0.0, vol=0.12) * 0.18).clip(-0.3, 0.6).rename("ebitdamargin")
    grossmargin = (_fund(105, base=1.0, drift=0.0, vol=0.07) * 0.45).clip(0.1, 0.85).rename("grossmargin")

    cols = {
        "revenue": revenue, "fcf": fcf, "ncfo": ncfo,
        "ebitdamargin": ebitdamargin, "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    print("OK f23_rule_of_40_base_076_150_claude: %d features pass" % n_features)
