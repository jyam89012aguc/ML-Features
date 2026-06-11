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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (hypergrowth signature composites) =====
def _f37_growth(revenue, w):
    return _roc(revenue, w)


def _f37_gp_growth(gp, w):
    return _roc(gp, w)


def _f37_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f37_rnd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f37_rule40(revenue, ncfo, w):
    g = _roc(revenue, w)
    m = ncfo / revenue.replace(0, np.nan)
    return g + m


def _f37_durable(revenue, grossmargin, w):
    return _roc(revenue, w) * grossmargin


# ============================================================
# growth-margin co-movement: rolling correlation of growth & margin change, 252d
def f37hg_f37_hypergrowth_signature_gmcorr_252d_base_v076_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 63)
    dm = grossmargin - grossmargin.shift(63)
    b = g.rolling(252, min_periods=126).corr(dm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 stability ranked: low-volatility durable growth, 252d
def f37hg_f37_hypergrowth_signature_r40stab_252d_base_v077_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    inv_vol = 1.0 / _std(r40, 252).replace(0, np.nan)
    b = _rank(inv_vol, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin expansion streak weighted by revenue growth, 252d
def f37hg_f37_hypergrowth_signature_gmstreak_252d_base_v078_signal(revenue, grossmargin):
    up = (grossmargin > grossmargin.shift(21)).astype(float)
    streak = up.rolling(252, min_periods=63).mean()
    g = _f37_growth(revenue, 252)
    b = streak * np.sign(g) + 0.2 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite curvature: 2nd-difference of g*gm, 252d
def f37hg_f37_hypergrowth_signature_durqcurv_252d_base_v079_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq - 2.0 * dq.shift(63) + dq.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin minus reinvestment-intensity spread (cash vs spend), 252d
def f37hg_f37_hypergrowth_signature_cashspend_252d_base_v080_signal(ncfo, revenue, rnd):
    m = _f37_ocf_margin(ncfo, revenue)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = m - ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit per R&D dollar (research productivity), 252d
def f37hg_f37_hypergrowth_signature_gpperrnd_252d_base_v081_signal(gp, rnd):
    b = gp / rnd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality composite: rank(growth) x rank(gross margin), 252d
def f37hg_f37_hypergrowth_signature_gqrank_252d_base_v082_signal(revenue, grossmargin):
    gr = _rank(_f37_growth(revenue, 252), 504)
    mr = _rank(grossmargin, 504)
    b = gr * mr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion penalty x gross margin (volatile-growth discount), 252d
def f37hg_f37_hypergrowth_signature_growthsmooth_252d_base_v083_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 63)
    gvol = _std(g, 252)
    gmean = _mean(g, 252)
    b = gmean / gvol.replace(0, np.nan) * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 minus its 252d-ago level (year-over-year improvement), 252d
def f37hg_f37_hypergrowth_signature_r40yoy_252d_base_v084_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    b = r40 - r40.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth acceleration weighted by margin, 126d
def f37hg_f37_hypergrowth_signature_gpacc_126d_base_v085_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 126)
    gpacc = gpg - gpg.shift(63)
    b = gpacc * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf-margin level ranked, gated by growth regime, 252d
def f37hg_f37_hypergrowth_signature_ocfrank_252d_base_v086_signal(ncfo, revenue):
    m = _f37_ocf_margin(ncfo, revenue)
    g = _f37_growth(revenue, 126)
    b = _rank(m, 504) * np.tanh(10.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity level percentile gated by gross margin (heavy-but-profitable), 252d
def f37hg_f37_hypergrowth_signature_reinvtrend_252d_base_v087_signal(rnd, revenue, grossmargin):
    ri = _f37_rnd_intensity(rnd, revenue)
    b = _rank(ri, 504) * (grossmargin - 0.4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x gross margin minus its long EMA, normalized (composite z-displacement), 252d
def f37hg_f37_hypergrowth_signature_durqzdisp_252d_base_v088_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = (dq - dq.ewm(span=126, min_periods=42).mean()) / _std(dq, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 contribution split: growth-share of total r40, 252d
def f37hg_f37_hypergrowth_signature_r40split_252d_base_v089_signal(revenue, ncfo):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    tot = g.abs() + m.abs()
    b = (g - m) / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-adjusted billings proxy growth (gp+revenue blend growth), 252d
def f37hg_f37_hypergrowth_signature_blendgrowth_252d_base_v090_signal(gp, revenue, grossmargin):
    blend = 0.5 * _f37_growth(revenue, 252) + 0.5 * _f37_gp_growth(gp, 252)
    b = blend * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable growth signal vs its cross-time median (regime distance), 504d
def f37hg_f37_hypergrowth_signature_durqregime_504d_base_v091_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 504)
    med = dq.rolling(504, min_periods=126).median()
    b = dq - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-funded growth: ncfo growth x revenue growth co-movement, 252d
def f37hg_f37_hypergrowth_signature_cashgrowth_252d_base_v092_signal(ncfo, revenue):
    ng = _roc(ncfo.abs() + 1.0, 252)
    rg = _f37_growth(revenue, 252)
    b = np.sign(rg) * np.sign(ng) * (rg.abs() + ng.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin stability premium: inverse margin-volatility ranked, growth-sign tilt, 252d
def f37hg_f37_hypergrowth_signature_gmstable_252d_base_v093_signal(revenue, grossmargin):
    gmvol = _std(grossmargin, 252)
    g = _f37_growth(revenue, 252)
    b = _rank(-gmvol, 504) + 0.3 * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded gp growth efficiency: gp growth / rnd growth, 252d
def f37hg_f37_hypergrowth_signature_gpvsrnd_252d_base_v094_signal(gp, rnd):
    gpg = _f37_gp_growth(gp, 252)
    rg = _roc(rnd, 252)
    b = gpg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 percentile vs own 2y history, ocf-weighted, 252d
def f37hg_f37_hypergrowth_signature_r40pct_252d_base_v095_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    b = _rank(r40, 504) + 0.3 * np.sign(m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth tail-compressed (signed sqrt) of triple z-blend, 252d
def f37hg_f37_hypergrowth_signature_trisqrt_252d_base_v096_signal(revenue, grossmargin, ncfo):
    g = _z(_f37_growth(revenue, 252), 252)
    gm = _z(grossmargin, 252)
    m = _z(_f37_ocf_margin(ncfo, revenue), 252)
    s = g + gm + m
    b = np.sign(s) * (s.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth with margin-AND-cash both improving (double-confirm), 252d
def f37hg_f37_hypergrowth_signature_doubleconf_252d_base_v097_signal(revenue, grossmargin, ncfo):
    g = _f37_growth(revenue, 252)
    mup = (grossmargin > grossmargin.shift(126)).astype(float)
    m = _f37_ocf_margin(ncfo, revenue)
    cup = (m > m.shift(126)).astype(float)
    b = g * (mup + cup - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit dollar momentum z (scale durability), 252d
def f37hg_f37_hypergrowth_signature_gpmomz_252d_base_v098_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 252)
    b = _z(gpg, 504) * np.sign(grossmargin - 0.4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity vs gross margin spread (spend-vs-profitability), 252d
def f37hg_f37_hypergrowth_signature_spendmargin_252d_base_v099_signal(rnd, revenue, grossmargin):
    ri = _f37_rnd_intensity(rnd, revenue)
    b = grossmargin - ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth EMA crossover (fast minus slow composite), 252d
def f37hg_f37_hypergrowth_signature_durqcross_252d_base_v100_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    fast = dq.ewm(span=42, min_periods=21).mean()
    slow = dq.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with sequential acceleration emphasis, 63d
def f37hg_f37_hypergrowth_signature_r40seqacc_63d_base_v101_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 63)
    b = r40 + 2.0 * (r40 - r40.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth durability via gross-margin-weighted log revenue level slope, 252d
def f37hg_f37_hypergrowth_signature_levslope_252d_base_v102_signal(revenue, grossmargin):
    lr = np.log(revenue.replace(0, np.nan))
    slope = lr - lr.shift(126)
    b = slope * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash margin gap trend (gross margin minus ocf margin), de-meaned, 252d
def f37hg_f37_hypergrowth_signature_margingap_252d_base_v103_signal(grossmargin, ncfo, revenue):
    m = _f37_ocf_margin(ncfo, revenue)
    gap = grossmargin - m
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth durable: (g - rnd growth) x gross margin, 252d
def f37hg_f37_hypergrowth_signature_reinvdur_252d_base_v104_signal(revenue, rnd, grossmargin):
    g = _f37_growth(revenue, 252)
    rg = _roc(rnd, 252)
    b = (g - rg) * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 cash-side strength: ocf-margin trend ranked, 252d
def f37hg_f37_hypergrowth_signature_ocftrend_252d_base_v105_signal(ncfo, revenue):
    m = _f37_ocf_margin(ncfo, revenue)
    mtrend = m - m.shift(126)
    b = _rank(mtrend, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite Sharpe (mean/std of g*gm over a year), 252d
def f37hg_f37_hypergrowth_signature_durqsharpe_252d_base_v106_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = _mean(dq, 252) / _std(dq, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x (gross margin minus its 252d mean) margin-surprise interaction, 252d
def f37hg_f37_hypergrowth_signature_gmsurp_252d_base_v107_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 252)
    gmsurp = grossmargin - _mean(grossmargin, 252)
    b = g * gmsurp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 above-threshold magnitude x gross margin quality, 252d
def f37hg_f37_hypergrowth_signature_r40magq_252d_base_v108_signal(revenue, ncfo, grossmargin):
    r40 = _f37_rule40(revenue, ncfo, 252)
    excess = (r40 - 0.40).clip(lower=0)
    b = excess * _rank(grossmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth, normalized by gross profit scale, 252d
def f37hg_f37_hypergrowth_signature_rndvsgp_252d_base_v109_signal(rnd, gp):
    ratio = rnd / gp.replace(0, np.nan)
    b = ratio - ratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth percentile minus Rule-of-40 percentile (which engine leads), 252d
def f37hg_f37_hypergrowth_signature_enginegap_252d_base_v110_signal(revenue, grossmargin, ncfo):
    dq = _rank(_f37_durable(revenue, grossmargin, 252), 504)
    r40 = _rank(_f37_rule40(revenue, ncfo, 252), 504)
    b = dq - r40
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend x ocf-margin trend (twin-margin expansion), 252d
def f37hg_f37_hypergrowth_signature_twinmargin_252d_base_v111_signal(grossmargin, ncfo, revenue):
    gmt = grossmargin - grossmargin.shift(126)
    m = _f37_ocf_margin(ncfo, revenue)
    mt = m - m.shift(126)
    b = gmt * mt * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-funded-by-cash: revenue growth scaled by ocf-margin percentile, 252d
def f37hg_f37_hypergrowth_signature_growthcashpct_252d_base_v112_signal(revenue, ncfo):
    g = _f37_growth(revenue, 252)
    mpct = _rank(_f37_ocf_margin(ncfo, revenue), 504)
    b = g * (0.5 + mpct)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity acceleration x gross margin (intensifying quality reinvestment), 252d
def f37hg_f37_hypergrowth_signature_riacc_252d_base_v113_signal(rnd, revenue, grossmargin):
    ri = _f37_rnd_intensity(rnd, revenue)
    riacc = ri - 2.0 * ri.shift(126) + ri.shift(252)
    b = riacc * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite long-short window spread (252 vs 63), 252d
def f37hg_f37_hypergrowth_signature_durqspread_252d_base_v114_signal(revenue, grossmargin):
    dq_l = _f37_durable(revenue, grossmargin, 252)
    dq_s = _f37_durable(revenue, grossmargin, 63)
    b = dq_s - dq_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 cash-side vs growth-side balance, short-window emphasis
def f37hg_f37_hypergrowth_signature_r40spread_base_v115_signal(revenue, ncfo):
    g = _f37_growth(revenue, 63)
    m = _f37_ocf_margin(ncfo, revenue)
    b = _rank(m, 504) - _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit cash conversion (ncfo/gp) ranked x growth sign, 252d
def f37hg_f37_hypergrowth_signature_gpconv_252d_base_v116_signal(ncfo, gp, revenue):
    conv = ncfo / gp.replace(0, np.nan)
    g = _f37_growth(revenue, 126)
    b = _rank(conv, 504) * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite half-life smoothing minus raw (lag signal), 252d
def f37hg_f37_hypergrowth_signature_durqlag_252d_base_v117_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq.ewm(span=21, min_periods=10).mean() - dq.ewm(span=84, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality: gp growth minus revenue growth, gated by ocf positivity, 252d
def f37hg_f37_hypergrowth_signature_gpqual_252d_base_v118_signal(gp, revenue, ncfo):
    gpg = _f37_gp_growth(gp, 252)
    rg = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    b = (gpg - rg) * np.sign(m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 z minus reinvestment-intensity z (efficient durable growth), 252d
def f37hg_f37_hypergrowth_signature_r40eff_252d_base_v119_signal(revenue, ncfo, rnd):
    r40z = _z(_f37_rule40(revenue, ncfo, 252), 252)
    riz = _z(_f37_rnd_intensity(rnd, revenue), 252)
    b = r40z - 0.5 * riz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin breadth: fraction of last year margin above its median, growth-tilted, 252d
def f37hg_f37_hypergrowth_signature_gmbreadth_252d_base_v120_signal(grossmargin, revenue):
    med = grossmargin.rolling(252, min_periods=63).median()
    above = (grossmargin > med).astype(float)
    breadth = above.rolling(252, min_periods=63).mean() - 0.5
    g = _f37_growth(revenue, 252)
    b = breadth + 0.5 * np.tanh(5.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite minus reinvestment-funded composite (quality-vs-spend), 252d
def f37hg_f37_hypergrowth_signature_qualspend_252d_base_v121_signal(revenue, grossmargin, rnd):
    dq = _z(_f37_durable(revenue, grossmargin, 252), 252)
    g = _f37_growth(revenue, 252)
    rg = _roc(rnd, 252)
    reinv = _z((g - rg), 252)
    b = dq - reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin acceleration (2nd diff ocf-margin) x growth, 252d
def f37hg_f37_hypergrowth_signature_cashacc_252d_base_v122_signal(ncfo, revenue):
    m = _f37_ocf_margin(ncfo, revenue)
    macc = m - 2.0 * m.shift(126) + m.shift(252)
    g = _f37_growth(revenue, 252)
    b = macc * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-weighted revenue z-level (scaled durable size), 252d
def f37hg_f37_hypergrowth_signature_sizeq_252d_base_v123_signal(revenue, grossmargin):
    rz = _z(np.log(revenue.replace(0, np.nan)), 252)
    b = rz * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 sign-persistence (consistently above 40), 252d
def f37hg_f37_hypergrowth_signature_r40persist_252d_base_v124_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 126)
    above = (r40 > 0.40).astype(float)
    b = above.rolling(252, min_periods=63).mean() * 2.0 - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment quality: gp growth per unit R&D intensity, ranked, 252d
def f37hg_f37_hypergrowth_signature_reinvqual_252d_base_v125_signal(gp, rnd, revenue):
    gpg = _f37_gp_growth(gp, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = _rank(gpg / ri.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth momentum minus mean-reversion blend, 252d
def f37hg_f37_hypergrowth_signature_durqmix_252d_base_v126_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    mom = dq - dq.shift(63)
    rev = _mean(dq, 252) - dq
    b = mom + 0.5 * rev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x gross margin, downside semivariance penalized, 252d
def f37hg_f37_hypergrowth_signature_durqdown_252d_base_v127_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    neg = dq.where(dq < 0, 0.0)
    downside = _std(neg, 252)
    b = _mean(dq, 252) - 0.5 * downside
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf coverage of R&D, trend over a year (improving self-funding of research), 252d
def f37hg_f37_hypergrowth_signature_rndcover_252d_base_v128_signal(ncfo, rnd):
    cover = ncfo / rnd.replace(0, np.nan)
    b = _rank(cover - cover.shift(252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 x gross-margin-expansion confirmation, 252d
def f37hg_f37_hypergrowth_signature_r40confirm_252d_base_v129_signal(revenue, ncfo, grossmargin):
    r40 = _f37_rule40(revenue, ncfo, 252)
    mexp = np.sign(grossmargin - grossmargin.shift(252))
    b = r40 * mexp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite vs gp-growth composite divergence, 252d
def f37hg_f37_hypergrowth_signature_durgpdiv_252d_base_v130_signal(revenue, grossmargin, gp):
    dq = _z(_f37_durable(revenue, grossmargin, 252), 252)
    gpq = _z(_f37_gp_growth(gp, 252) * grossmargin, 252)
    b = dq - gpq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin interaction smoothed and ranked (persistent quality), 252d
def f37hg_f37_hypergrowth_signature_durqsmrank_252d_base_v131_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252).ewm(span=63, min_periods=21).mean()
    b = _rank(dq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment headroom: cash flow net of R&D over revenue, ranked level, 252d
def f37hg_f37_hypergrowth_signature_r40headroom_252d_base_v132_signal(revenue, ncfo, rnd):
    headroom = (ncfo - rnd) / revenue.replace(0, np.nan)
    b = _rank(headroom, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin convexity of growth: g x (gm - gm_min) over a year, 252d
def f37hg_f37_hypergrowth_signature_gmconvex2_252d_base_v133_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 252)
    gmlift = grossmargin - grossmargin.rolling(252, min_periods=63).min()
    b = g * gmlift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth z minus cash-margin z (growth-quality vs cash-quality), 252d
def f37hg_f37_hypergrowth_signature_gqcq_252d_base_v134_signal(revenue, grossmargin, ncfo):
    dq = _z(_f37_durable(revenue, grossmargin, 252), 252)
    cq = _z(_f37_ocf_margin(ncfo, revenue), 252)
    b = 0.6 * dq + 0.4 * cq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth tanh-bounded momentum, 252d
def f37hg_f37_hypergrowth_signature_reinvtanh_252d_base_v135_signal(revenue, rnd):
    g = _f37_growth(revenue, 252)
    rg = _roc(rnd, 252)
    diff = g - rg
    b = np.tanh(4.0 * (diff - diff.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted durable growth: durable composite mean over its rolling volatility, 252d
def f37hg_f37_hypergrowth_signature_durqra_252d_base_v136_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = _rank(_mean(dq, 126) / _std(dq, 252).replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 acceleration ranked (improving durable trajectory), 252d
def f37hg_f37_hypergrowth_signature_r40accrank_252d_base_v137_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    acc = r40 - r40.shift(126)
    b = _rank(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-share level percentile x revenue scale (high-margin scale durability), 252d
def f37hg_f37_hypergrowth_signature_mixshift_252d_base_v138_signal(gp, revenue):
    share = gp / revenue.replace(0, np.nan)
    rz = _z(np.log(revenue.replace(0, np.nan)), 252)
    b = _rank(share, 504) * (1.0 + 0.5 * rz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite minus reinvestment intensity level, ranked, 252d
def f37hg_f37_hypergrowth_signature_durqnet_252d_base_v139_signal(revenue, grossmargin, rnd):
    dq = _z(_f37_durable(revenue, grossmargin, 252), 252)
    riz = _z(_f37_rnd_intensity(rnd, revenue), 252)
    b = _rank(dq - riz, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin level x revenue-scale (absolute cash-generative growth), 252d
def f37hg_f37_hypergrowth_signature_cashscale_252d_base_v140_signal(ncfo, revenue):
    m = _f37_ocf_margin(ncfo, revenue)
    rz = _z(np.log(revenue.replace(0, np.nan)), 252)
    b = m * (1.0 + rz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with both engines positive (clean durable-growth flag), 252d
def f37hg_f37_hypergrowth_signature_r40clean_252d_base_v141_signal(revenue, ncfo, grossmargin):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    clean = ((g > 0) & (m > 0)).astype(float) - 0.5
    b = clean * grossmargin + 0.3 * (g + m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin momentum z scaled by gp growth (margin-led GP expansion), 252d
def f37hg_f37_hypergrowth_signature_gmled_252d_base_v142_signal(grossmargin, gp):
    gmm = _z(grossmargin - grossmargin.shift(126), 252)
    gpg = _f37_gp_growth(gp, 252)
    b = gmm * np.sign(gpg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth funded by cash: (g - rnd_g) confirmed by ocf-margin trend, 252d
def f37hg_f37_hypergrowth_signature_reinvcash_252d_base_v143_signal(revenue, rnd, ncfo):
    g = _f37_growth(revenue, 252)
    rg = _roc(rnd, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    cashtrend = np.sign(m - m.shift(252))
    b = _z(g - rg, 252) * cashtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite year-over-year acceleration (2y diff), 252d
def f37hg_f37_hypergrowth_signature_durqyoyacc_252d_base_v144_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = (dq - dq.shift(252)) - (dq.shift(252) - dq.shift(504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-growth tension: low-cash-margin within high-growth regime (burn-funded growth), 252d
def f37hg_f37_hypergrowth_signature_durqburn_252d_base_v145_signal(revenue, grossmargin, ncfo):
    m = _f37_ocf_margin(ncfo, revenue)
    g = _f37_growth(revenue, 252)
    gpct = _rank(g, 504)
    mpct = _rank(m, 504)
    b = (gpct - mpct) * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 weighted by gross-profit growth momentum sign, 252d
def f37hg_f37_hypergrowth_signature_r40gpmom_252d_base_v146_signal(revenue, ncfo, gp):
    r40 = _f37_rule40(revenue, ncfo, 252)
    gpmom = np.sign(_f37_gp_growth(gp, 126) - _f37_gp_growth(gp, 252))
    b = r40 * gpmom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-scaled growth acceleration (durable inflection), 126d
def f37hg_f37_hypergrowth_signature_durqinflect_126d_base_v147_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 63)
    gacc = g - 2.0 * g.shift(63) + g.shift(126)
    b = gacc * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite hypergrowth score: weighted z(growth, gm, ocf, gp-growth) - z(rnd-intensity), 252d
def f37hg_f37_hypergrowth_signature_megascore_252d_base_v148_signal(revenue, grossmargin, ncfo, gp, rnd):
    g = _z(_f37_growth(revenue, 252), 252)
    gm = _z(grossmargin, 252)
    m = _z(_f37_ocf_margin(ncfo, revenue), 252)
    gpg = _z(_f37_gp_growth(gp, 252), 252)
    riz = _z(_f37_rnd_intensity(rnd, revenue), 252)
    b = 0.3 * g + 0.25 * gm + 0.2 * m + 0.25 * gpg - 0.15 * riz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite percentile vs full multi-year history, 504d
def f37hg_f37_hypergrowth_signature_durqpct_504d_base_v149_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = _rank(dq, 1008)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 cash-tilt durability: ocf-margin dominant blend ranked, 252d
def f37hg_f37_hypergrowth_signature_r40cashtilt_252d_base_v150_signal(revenue, ncfo, grossmargin):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    blend = 0.3 * g + 0.7 * m
    b = _rank(blend, 504) + 0.2 * (grossmargin - 0.4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hg_f37_hypergrowth_signature_gmcorr_252d_base_v076_signal,
    f37hg_f37_hypergrowth_signature_r40stab_252d_base_v077_signal,
    f37hg_f37_hypergrowth_signature_gmstreak_252d_base_v078_signal,
    f37hg_f37_hypergrowth_signature_durqcurv_252d_base_v079_signal,
    f37hg_f37_hypergrowth_signature_cashspend_252d_base_v080_signal,
    f37hg_f37_hypergrowth_signature_gpperrnd_252d_base_v081_signal,
    f37hg_f37_hypergrowth_signature_gqrank_252d_base_v082_signal,
    f37hg_f37_hypergrowth_signature_growthsmooth_252d_base_v083_signal,
    f37hg_f37_hypergrowth_signature_r40yoy_252d_base_v084_signal,
    f37hg_f37_hypergrowth_signature_gpacc_126d_base_v085_signal,
    f37hg_f37_hypergrowth_signature_ocfrank_252d_base_v086_signal,
    f37hg_f37_hypergrowth_signature_reinvtrend_252d_base_v087_signal,
    f37hg_f37_hypergrowth_signature_durqzdisp_252d_base_v088_signal,
    f37hg_f37_hypergrowth_signature_r40split_252d_base_v089_signal,
    f37hg_f37_hypergrowth_signature_blendgrowth_252d_base_v090_signal,
    f37hg_f37_hypergrowth_signature_durqregime_504d_base_v091_signal,
    f37hg_f37_hypergrowth_signature_cashgrowth_252d_base_v092_signal,
    f37hg_f37_hypergrowth_signature_gmstable_252d_base_v093_signal,
    f37hg_f37_hypergrowth_signature_gpvsrnd_252d_base_v094_signal,
    f37hg_f37_hypergrowth_signature_r40pct_252d_base_v095_signal,
    f37hg_f37_hypergrowth_signature_trisqrt_252d_base_v096_signal,
    f37hg_f37_hypergrowth_signature_doubleconf_252d_base_v097_signal,
    f37hg_f37_hypergrowth_signature_gpmomz_252d_base_v098_signal,
    f37hg_f37_hypergrowth_signature_spendmargin_252d_base_v099_signal,
    f37hg_f37_hypergrowth_signature_durqcross_252d_base_v100_signal,
    f37hg_f37_hypergrowth_signature_r40seqacc_63d_base_v101_signal,
    f37hg_f37_hypergrowth_signature_levslope_252d_base_v102_signal,
    f37hg_f37_hypergrowth_signature_margingap_252d_base_v103_signal,
    f37hg_f37_hypergrowth_signature_reinvdur_252d_base_v104_signal,
    f37hg_f37_hypergrowth_signature_ocftrend_252d_base_v105_signal,
    f37hg_f37_hypergrowth_signature_durqsharpe_252d_base_v106_signal,
    f37hg_f37_hypergrowth_signature_gmsurp_252d_base_v107_signal,
    f37hg_f37_hypergrowth_signature_r40magq_252d_base_v108_signal,
    f37hg_f37_hypergrowth_signature_rndvsgp_252d_base_v109_signal,
    f37hg_f37_hypergrowth_signature_enginegap_252d_base_v110_signal,
    f37hg_f37_hypergrowth_signature_twinmargin_252d_base_v111_signal,
    f37hg_f37_hypergrowth_signature_growthcashpct_252d_base_v112_signal,
    f37hg_f37_hypergrowth_signature_riacc_252d_base_v113_signal,
    f37hg_f37_hypergrowth_signature_durqspread_252d_base_v114_signal,
    f37hg_f37_hypergrowth_signature_r40spread_base_v115_signal,
    f37hg_f37_hypergrowth_signature_gpconv_252d_base_v116_signal,
    f37hg_f37_hypergrowth_signature_durqlag_252d_base_v117_signal,
    f37hg_f37_hypergrowth_signature_gpqual_252d_base_v118_signal,
    f37hg_f37_hypergrowth_signature_r40eff_252d_base_v119_signal,
    f37hg_f37_hypergrowth_signature_gmbreadth_252d_base_v120_signal,
    f37hg_f37_hypergrowth_signature_qualspend_252d_base_v121_signal,
    f37hg_f37_hypergrowth_signature_cashacc_252d_base_v122_signal,
    f37hg_f37_hypergrowth_signature_sizeq_252d_base_v123_signal,
    f37hg_f37_hypergrowth_signature_r40persist_252d_base_v124_signal,
    f37hg_f37_hypergrowth_signature_reinvqual_252d_base_v125_signal,
    f37hg_f37_hypergrowth_signature_durqmix_252d_base_v126_signal,
    f37hg_f37_hypergrowth_signature_durqdown_252d_base_v127_signal,
    f37hg_f37_hypergrowth_signature_rndcover_252d_base_v128_signal,
    f37hg_f37_hypergrowth_signature_r40confirm_252d_base_v129_signal,
    f37hg_f37_hypergrowth_signature_durgpdiv_252d_base_v130_signal,
    f37hg_f37_hypergrowth_signature_durqsmrank_252d_base_v131_signal,
    f37hg_f37_hypergrowth_signature_r40headroom_252d_base_v132_signal,
    f37hg_f37_hypergrowth_signature_gmconvex2_252d_base_v133_signal,
    f37hg_f37_hypergrowth_signature_gqcq_252d_base_v134_signal,
    f37hg_f37_hypergrowth_signature_reinvtanh_252d_base_v135_signal,
    f37hg_f37_hypergrowth_signature_durqra_252d_base_v136_signal,
    f37hg_f37_hypergrowth_signature_r40accrank_252d_base_v137_signal,
    f37hg_f37_hypergrowth_signature_mixshift_252d_base_v138_signal,
    f37hg_f37_hypergrowth_signature_durqnet_252d_base_v139_signal,
    f37hg_f37_hypergrowth_signature_cashscale_252d_base_v140_signal,
    f37hg_f37_hypergrowth_signature_r40clean_252d_base_v141_signal,
    f37hg_f37_hypergrowth_signature_gmled_252d_base_v142_signal,
    f37hg_f37_hypergrowth_signature_reinvcash_252d_base_v143_signal,
    f37hg_f37_hypergrowth_signature_durqyoyacc_252d_base_v144_signal,
    f37hg_f37_hypergrowth_signature_durqburn_252d_base_v145_signal,
    f37hg_f37_hypergrowth_signature_r40gpmom_252d_base_v146_signal,
    f37hg_f37_hypergrowth_signature_durqinflect_126d_base_v147_signal,
    f37hg_f37_hypergrowth_signature_megascore_252d_base_v148_signal,
    f37hg_f37_hypergrowth_signature_durqpct_504d_base_v149_signal,
    f37hg_f37_hypergrowth_signature_r40cashtilt_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1.0e8, drift=0.05, vol=0.06).rename("revenue")
    gp = _fund(102, base=0.55e8, drift=0.05, vol=0.09).rename("gp")
    rnd = _fund(103, base=0.18e8, drift=0.04, vol=0.11).rename("rnd")
    grossmargin = (0.42 + 0.12 * _fund(104, base=1.0, drift=0.0, vol=0.18)).rename("grossmargin")
    ncfo = _fund(105, base=0.12e8, drift=0.02, vol=0.16, allow_neg=True).rename("ncfo")

    cols = {"revenue": revenue, "gp": gp, "rnd": rnd,
            "grossmargin": grossmargin, "ncfo": ncfo}

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

    print("OK f37_hypergrowth_signature_base_076_150_claude: %d features pass" % n_features)
