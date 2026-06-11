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
    # smoothed yoy-style revenue growth
    return _roc(revenue, w)


def _f37_gm_level(grossmargin):
    # gross-margin level (fraction)
    return grossmargin


def _f37_gp_growth(gp, w):
    return _roc(gp, w)


def _f37_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f37_rnd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f37_rule40(revenue, ncfo, w):
    # growth + ocf-margin (Rule-of-40, fractional)
    g = _roc(revenue, w)
    m = ncfo / revenue.replace(0, np.nan)
    return g + m


def _f37_durable(revenue, grossmargin, w):
    # growth scaled by gross-margin level (durable, high-quality growth)
    return _roc(revenue, w) * grossmargin


# ============================================================
# revenue-growth x gross-margin-level (durable quality growth), 252d
def f37hg_f37_hypergrowth_signature_durq_252d_base_v001_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 252)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x gross-margin-level, 126d
def f37hg_f37_hypergrowth_signature_durq_126d_base_v002_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 126)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x gross-margin-level, 63d
def f37hg_f37_hypergrowth_signature_durq_63d_base_v003_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 63)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-with-expanding-margin: revenue growth x change in gross margin, 252d
def f37hg_f37_hypergrowth_signature_gxmexp_252d_base_v004_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 252)
    dm = grossmargin - grossmargin.shift(252)
    b = g * np.sign(dm) * (dm.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-with-expanding-margin, 126d
def f37hg_f37_hypergrowth_signature_gxmexp_126d_base_v005_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 126)
    dm = grossmargin - grossmargin.shift(126)
    b = g + 3.0 * dm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40: revenue growth + ocf margin, 252d
def f37hg_f37_hypergrowth_signature_r40_252d_base_v006_signal(revenue, ncfo):
    b = _f37_rule40(revenue, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40, 126d
def f37hg_f37_hypergrowth_signature_r40_126d_base_v007_signal(revenue, ncfo):
    b = _f37_rule40(revenue, ncfo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40, 63d
def f37hg_f37_hypergrowth_signature_r40_63d_base_v008_signal(revenue, ncfo):
    b = _f37_rule40(revenue, ncfo, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth: revenue growth minus R&D growth (growth outrunning spend), 252d
def f37hg_f37_hypergrowth_signature_reinvg_252d_base_v009_signal(revenue, rnd):
    g = _f37_growth(revenue, 252)
    rg = _roc(rnd, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = (g - rg) * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth (126d): revenue growth minus R&D growth differential
def f37hg_f37_hypergrowth_signature_reinvg_126d_base_v010_signal(revenue, rnd):
    g = _f37_growth(revenue, 126)
    rg = _roc(rnd, 126)
    b = g - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite: z(growth)+z(gm)+z(ocf), equal-weight standardized blend, 252d
def f37hg_f37_hypergrowth_signature_durcomp_252d_base_v011_signal(revenue, grossmargin, ncfo):
    g = _z(_f37_growth(revenue, 252), 504)
    gm = _z(grossmargin, 504)
    m = _z(_f37_ocf_margin(ncfo, revenue), 504)
    b = (g + gm + m) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite (126d): rank(growth)+rank(gm)+rank(ocf) breadth score
def f37hg_f37_hypergrowth_signature_durcomp_126d_base_v012_signal(revenue, grossmargin, ncfo):
    g = _rank(_f37_growth(revenue, 126), 252)
    gm = _rank(grossmargin, 252)
    m = _rank(_f37_ocf_margin(ncfo, revenue), 252)
    b = g + gm + m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth x gross-margin level (margin-weighted GP growth), 252d
def f37hg_f37_hypergrowth_signature_gpgm_252d_base_v013_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 252)
    b = gpg * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth x gross-margin level, 126d
def f37hg_f37_hypergrowth_signature_gpgm_126d_base_v014_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 126)
    b = gpg * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus revenue growth (margin tailwind in growth), 252d
def f37hg_f37_hypergrowth_signature_gpminusrev_252d_base_v015_signal(gp, revenue):
    gpg = _f37_gp_growth(gp, 252)
    rg = _f37_growth(revenue, 252)
    b = gpg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus revenue growth, 126d
def f37hg_f37_hypergrowth_signature_gpminusrev_126d_base_v016_signal(gp, revenue):
    gpg = _f37_gp_growth(gp, 126)
    rg = _f37_growth(revenue, 126)
    b = gpg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 gross-margin interaction: r40 gated by gross-margin percentile rank, 252d
def f37hg_f37_hypergrowth_signature_r40gm_252d_base_v017_signal(revenue, ncfo, grossmargin):
    r40 = _f37_rule40(revenue, ncfo, 252)
    gmr = _rank(grossmargin, 504)
    b = r40 * gmr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 (126d) plus gross-margin momentum tilt (improving-margin durable)
def f37hg_f37_hypergrowth_signature_r40gm_126d_base_v018_signal(revenue, ncfo, grossmargin):
    r40 = _f37_rule40(revenue, ncfo, 126)
    mm = grossmargin - grossmargin.shift(126)
    b = _z(r40, 252) + 1.5 * _z(mm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency of growth: revenue growth divided by R&D intensity (growth per reinvest), 252d
def f37hg_f37_hypergrowth_signature_effgrowth_252d_base_v019_signal(revenue, grossmargin, rnd):
    g = _f37_growth(revenue, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    gmgate = (grossmargin > grossmargin.rolling(252, min_periods=63).median()).astype(float)
    b = g / ri.replace(0, np.nan) * (0.5 + gmgate)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-efficiency of growth: gross-profit growth per unit R&D intensity, 252d
def f37hg_f37_hypergrowth_signature_gpperrnd_252d_base_v020_signal(gp, rnd, revenue):
    gpg = _f37_gp_growth(gp, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = gpg / ri.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded growth: ocf-margin level gated by positive growth (cash-generative growth), 252d
def f37hg_f37_hypergrowth_signature_selffund_252d_base_v021_signal(revenue, ncfo):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    b = m * (g > 0).astype(float) - m * (g <= 0).astype(float) * 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded growth, 126d
def f37hg_f37_hypergrowth_signature_selffund_126d_base_v022_signal(revenue, ncfo):
    g = _f37_growth(revenue, 126)
    m = _f37_ocf_margin(ncfo, revenue)
    b = g * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-adjusted growth z-score (durable growth, de-trended), 252d
def f37hg_f37_hypergrowth_signature_durqz_252d_base_v023_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = _z(dq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 z-score vs own history, 252d
def f37hg_f37_hypergrowth_signature_r40z_252d_base_v024_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    b = _z(r40, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite percentile rank vs own history, 252d
def f37hg_f37_hypergrowth_signature_durqrank_252d_base_v025_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = _rank(dq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined growth+margin+reinvest score (sum of normalized drivers), 252d
def f37hg_f37_hypergrowth_signature_triscore_252d_base_v026_signal(revenue, grossmargin, rnd):
    g = _z(_f37_growth(revenue, 252), 252)
    m = _z(grossmargin, 252)
    ri = _z(_f37_rnd_intensity(rnd, revenue), 252)
    b = g + m + ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined growth+margin+ocf score (Rule-of-40 style triple), 252d
def f37hg_f37_hypergrowth_signature_quadscore_252d_base_v027_signal(revenue, grossmargin, ncfo):
    g = _z(_f37_growth(revenue, 252), 252)
    m = _z(grossmargin, 252)
    ocf = _z(_f37_ocf_margin(ncfo, revenue), 252)
    b = g + m + ocf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration x gross margin (accelerating durable growth), 252d
def f37hg_f37_hypergrowth_signature_accgm_252d_base_v028_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 126)
    gacc = g - g.shift(126)
    b = gacc * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 acceleration (change in r40 over a quarter), 126d window
def f37hg_f37_hypergrowth_signature_r40acc_126d_base_v029_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 126)
    b = r40 - r40.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth acceleration, 252d
def f37hg_f37_hypergrowth_signature_reinvgacc_252d_base_v030_signal(revenue, rnd):
    g = _f37_growth(revenue, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    comp = g * ri
    b = comp - comp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin x gross-profit growth, ranked (quality GP momentum), 252d
def f37hg_f37_hypergrowth_signature_gpgmrank_252d_base_v031_signal(gp, grossmargin):
    comp = _f37_gp_growth(gp, 252) * grossmargin
    b = _rank(comp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite smoothed (EMA) for persistence, 252d
def f37hg_f37_hypergrowth_signature_durqema_252d_base_v032_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-vs-reinvest balance: revenue growth minus R&D-intensity momentum, gm-tilted, 252d
def f37hg_f37_hypergrowth_signature_gmbal_252d_base_v033_signal(revenue, rnd, grossmargin):
    g = _z(_f37_growth(revenue, 252), 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    rimom = _z(ri - ri.shift(126), 252)
    gmz = _z(grossmargin, 252)
    b = g - rimom + gmz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 threshold-crossing persistence: fraction of last year r40 above 0.40
def f37hg_f37_hypergrowth_signature_r40surplus_252d_base_v034_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    above = (r40 > 0.40).astype(float)
    b = above.rolling(252, min_periods=63).mean() + 0.25 * (r40 - r40.rolling(252, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion gp growth: gp growth x change in gross margin, 252d
def f37hg_f37_hypergrowth_signature_gpmexp_252d_base_v035_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 252)
    dm = grossmargin - grossmargin.shift(252)
    b = gpg + 4.0 * dm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality ratio: ocf-margin per unit revenue growth, 252d
def f37hg_f37_hypergrowth_signature_ocfpergrowth_252d_base_v036_signal(ncfo, revenue):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    b = m / g.abs().replace(0, np.nan) * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite minus its long average (mean-reversion), 252d
def f37hg_f37_hypergrowth_signature_durqdisp_252d_base_v037_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq - _mean(dq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity weighted by gross margin (quality of reinvestment), 252d
def f37hg_f37_hypergrowth_signature_qualreinv_252d_base_v038_signal(rnd, revenue, grossmargin):
    ri = _f37_rnd_intensity(rnd, revenue)
    b = ri * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended quality: gross margin plus ocf-margin level, growth-gated regime, 252d
def f37hg_f37_hypergrowth_signature_blendq_252d_base_v039_signal(revenue, grossmargin, ncfo):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    gate = np.tanh(8.0 * g)
    b = (grossmargin + m) * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended quality (126d): z(gm)+z(ocf) minus z(rnd-intensity), profitability-net-of-burn
def f37hg_f37_hypergrowth_signature_blendq_126d_base_v040_signal(revenue, grossmargin, ncfo):
    gm = _z(grossmargin, 252)
    m = _z(_f37_ocf_margin(ncfo, revenue), 252)
    g = _z(_f37_growth(revenue, 126), 252)
    b = gm + m + 0.5 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential growth surprise vs gross-margin trend (short composite), 63d
def f37hg_f37_hypergrowth_signature_seqdurq_63d_base_v041_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 63)
    gsurp = g - g.shift(63)
    mm = grossmargin - grossmargin.shift(63)
    b = gsurp + 6.0 * mm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus ocf-margin slope (paper-vs-cash GP divergence), 252d
def f37hg_f37_hypergrowth_signature_gpocf_252d_base_v042_signal(gp, ncfo, revenue):
    gpg = _f37_gp_growth(gp, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    mslope = m - m.shift(252)
    b = _z(gpg, 252) - _z(mslope, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 consistency: r40 mean / r40 std over a year, 126d
def f37hg_f37_hypergrowth_signature_r40consist_126d_base_v043_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 126)
    b = _mean(r40, 252) / _std(r40, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth signal-magnitude (sign x sqrt) for tail compression, 252d
def f37hg_f37_hypergrowth_signature_durqsm_252d_base_v044_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = np.sign(dq) * (dq.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth z-score, 252d
def f37hg_f37_hypergrowth_signature_reinvgz_252d_base_v045_signal(revenue, rnd):
    g = _f37_growth(revenue, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = _z(g * ri, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth+gm tanh-bounded composite momentum, 252d
def f37hg_f37_hypergrowth_signature_durqtanh_252d_base_v046_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    chg = dq - dq.shift(63)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth gated by margin-expansion regime (durable only when margins rising), 252d
def f37hg_f37_hypergrowth_signature_loggm_252d_base_v047_signal(revenue, grossmargin):
    lg = _logroc(revenue, 252)
    expanding = (grossmargin > grossmargin.shift(126)).astype(float) - 0.5
    b = lg * expanding
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 net of reinvestment momentum (deteriorating-burn penalty), 252d
def f37hg_f37_hypergrowth_signature_r40net_252d_base_v048_signal(revenue, ncfo, rnd):
    r40 = _f37_rule40(revenue, ncfo, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    rimom = ri - ri.shift(252)
    b = _z(r40, 252) - _z(rimom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-drag regime: rising R&D intensity while margins compress (anti-durable), 252d
def f37hg_f37_hypergrowth_signature_durqdrag_252d_base_v049_signal(revenue, grossmargin, rnd):
    ri = _f37_rnd_intensity(rnd, revenue)
    rimom = ri - ri.shift(252)
    mm = grossmargin - grossmargin.shift(252)
    b = -(rimom) + mm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-quality GP growth (126d): gp growth gated by positive-and-rising ocf margin
def f37hg_f37_hypergrowth_signature_gpocf_126d_base_v050_signal(gp, ncfo, revenue):
    gpg = _f37_gp_growth(gp, 126)
    m = _f37_ocf_margin(ncfo, revenue)
    quality = ((m > 0) & (m > m.shift(63))).astype(float) - 0.5
    b = gpg * quality
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon durable-growth stack (avg of 63/126/252 durable growth)
def f37hg_f37_hypergrowth_signature_durqstack_base_v051_signal(revenue, grossmargin):
    d1 = _f37_growth(revenue, 63) * grossmargin
    d2 = _f37_growth(revenue, 126) * grossmargin
    d3 = _f37_growth(revenue, 252) * grossmargin
    b = (d1 + d2 + d3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 multi-horizon stack (avg of 63/126/252)
def f37hg_f37_hypergrowth_signature_r40stack_base_v052_signal(revenue, ncfo):
    r1 = _f37_rule40(revenue, ncfo, 63)
    r2 = _f37_rule40(revenue, ncfo, 126)
    r3 = _f37_rule40(revenue, ncfo, 252)
    b = (r1 + r2 + r3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-with-expanding-margin using gp-share trend, 252d
def f37hg_f37_hypergrowth_signature_gpshare_252d_base_v053_signal(gp, revenue):
    share = gp / revenue.replace(0, np.nan)
    g = _f37_growth(revenue, 252)
    b = g * (share - share.shift(252) + share)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded reinvestment: ocf coverage of R&D spend (ncfo/rnd), trend, 252d
def f37hg_f37_hypergrowth_signature_selfreinv_252d_base_v054_signal(ncfo, revenue, rnd):
    cover = ncfo / rnd.replace(0, np.nan)
    b = cover - cover.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth slope-of-margin interaction (g x margin momentum), 126d
def f37hg_f37_hypergrowth_signature_gmmom_126d_base_v055_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 126)
    mm = grossmargin - grossmargin.shift(63)
    b = g * mm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 rank vs own 2y history, 252d
def f37hg_f37_hypergrowth_signature_r40rank_252d_base_v056_signal(revenue, ncfo):
    r40 = _f37_rule40(revenue, ncfo, 252)
    b = _rank(r40, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth z-score weighted by margin, 252d
def f37hg_f37_hypergrowth_signature_gpgz_252d_base_v057_signal(gp, grossmargin):
    gpg = _f37_gp_growth(gp, 252)
    b = _z(gpg, 252) * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x margin minus its own EMA (durable-growth surprise), 252d
def f37hg_f37_hypergrowth_signature_durqsurp_252d_base_v058_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq - dq.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-funded R&D runway: operating cash flow as multiple of R&D spend, growth-scaled, 252d
def f37hg_f37_hypergrowth_signature_cashrunwg_252d_base_v059_signal(ncfo, revenue, rnd):
    cover = ncfo / rnd.replace(0, np.nan)
    g = _f37_growth(revenue, 252)
    b = _rank(cover, 504) * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite vol-adjusted (composite / its own std), 252d
def f37hg_f37_hypergrowth_signature_durqvol_252d_base_v060_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq / _std(dq, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-adjusted growth-quality rank: growth-per-rnd ranked, ocf-tilt, 252d
def f37hg_f37_hypergrowth_signature_r40netrank_252d_base_v061_signal(revenue, ncfo, rnd):
    g = _f37_growth(revenue, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    eff = g / ri.replace(0, np.nan)
    m = _f37_ocf_margin(ncfo, revenue)
    b = _rank(eff, 504) + _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expanding-margin AND improving-cash co-movement (both-rising regime), 252d
def f37hg_f37_hypergrowth_signature_gxmocf_252d_base_v062_signal(revenue, grossmargin, ncfo):
    dm = grossmargin - grossmargin.shift(252)
    m = _f37_ocf_margin(ncfo, revenue)
    dmcf = m - m.shift(252)
    both = (np.sign(dm) + np.sign(dmcf))
    b = both * (dm.abs() + dmcf.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded gp growth: gp growth x rnd-intensity, 252d
def f37hg_f37_hypergrowth_signature_gpreinv_252d_base_v063_signal(gp, rnd, revenue):
    gpg = _f37_gp_growth(gp, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = gpg * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite long-horizon (504d growth x gm)
def f37hg_f37_hypergrowth_signature_durq_504d_base_v064_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 504)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon Rule-of-40 quality: 504d r40 z-scored, ocf-margin emphasis
def f37hg_f37_hypergrowth_signature_r40_504d_base_v065_signal(revenue, ncfo):
    g = _f37_growth(revenue, 504)
    m = _f37_ocf_margin(ncfo, revenue)
    b = _z(g, 504) + 2.0 * _z(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin dispersion in growth regime: gross-margin volatility scaled by growth sign, 252d
def f37hg_f37_hypergrowth_signature_gmconvex_252d_base_v066_signal(revenue, grossmargin):
    g = _f37_growth(revenue, 126)
    gmvol = _std(grossmargin, 252)
    b = np.sign(g) * gmvol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion of gross profit, gm-tilted level (ncfo/gp), 252d
def f37hg_f37_hypergrowth_signature_durqconv_252d_base_v067_signal(revenue, grossmargin, ncfo, gp):
    conv = ncfo / gp.replace(0, np.nan)
    b = _z(conv, 252) + (grossmargin - grossmargin.rolling(252, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-margin durable regime distance: gross-margin excess x Rule-of-40 sign, 252d
def f37hg_f37_hypergrowth_signature_r40gmfloor_252d_base_v068_signal(revenue, ncfo, grossmargin):
    r40 = _f37_rule40(revenue, ncfo, 252)
    gmexcess = grossmargin - grossmargin.rolling(504, min_periods=126).mean()
    b = gmexcess * np.sign(r40 - 0.40) + 0.05 * np.tanh(r40)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth surplus vs own median (regime distance), 252d
def f37hg_f37_hypergrowth_signature_reinvgdist_252d_base_v069_signal(revenue, rnd):
    g = _f37_growth(revenue, 252)
    ri = _f37_rnd_intensity(rnd, revenue)
    comp = g * ri
    med = comp.rolling(504, min_periods=126).median()
    b = comp - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite year-over-year change, 252d
def f37hg_f37_hypergrowth_signature_durqyoy_252d_base_v070_signal(revenue, grossmargin):
    dq = _f37_durable(revenue, grossmargin, 252)
    b = dq - dq.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x ocf-margin minus growth x rnd-intensity (cash vs reinvest tilt), 252d
def f37hg_f37_hypergrowth_signature_cashvsreinv_252d_base_v071_signal(revenue, ncfo, rnd):
    g = _f37_growth(revenue, 252)
    m = _f37_ocf_margin(ncfo, revenue)
    ri = _f37_rnd_intensity(rnd, revenue)
    b = g * (m - ri)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin trajectory x growth (path-to-scale-margin growth), 126d
def f37hg_f37_hypergrowth_signature_gptraj_126d_base_v072_signal(gp, revenue, grossmargin):
    gpg = _f37_gp_growth(gp, 126)
    mm = grossmargin - grossmargin.shift(126)
    b = gpg + 5.0 * mm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite durable-growth health: weighted sum (g, gm, ocf, -rnd drag), 252d
def f37hg_f37_hypergrowth_signature_health_252d_base_v073_signal(revenue, grossmargin, ncfo, rnd):
    g = _z(_f37_growth(revenue, 252), 252)
    m = _z(grossmargin, 252)
    ocf = _z(_f37_ocf_margin(ncfo, revenue), 252)
    ri = _z(_f37_rnd_intensity(rnd, revenue), 252)
    b = 0.4 * g + 0.3 * m + 0.3 * ocf - 0.2 * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 ocf-margin slope interaction (improving cash + growth), 126d
def f37hg_f37_hypergrowth_signature_r40ocfslope_126d_base_v074_signal(revenue, ncfo):
    g = _f37_growth(revenue, 126)
    m = _f37_ocf_margin(ncfo, revenue)
    mslope = m - m.shift(63)
    b = g + m + 2.0 * mslope
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-share momentum gated by growth direction (mix-shift to high-margin growth), 252d
def f37hg_f37_hypergrowth_signature_durqshare_252d_base_v075_signal(revenue, grossmargin, gp):
    share = gp / revenue.replace(0, np.nan)
    smom = share - share.shift(126)
    g = _f37_growth(revenue, 126)
    b = smom * np.sign(g) + 0.1 * (grossmargin - grossmargin.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hg_f37_hypergrowth_signature_durq_252d_base_v001_signal,
    f37hg_f37_hypergrowth_signature_durq_126d_base_v002_signal,
    f37hg_f37_hypergrowth_signature_durq_63d_base_v003_signal,
    f37hg_f37_hypergrowth_signature_gxmexp_252d_base_v004_signal,
    f37hg_f37_hypergrowth_signature_gxmexp_126d_base_v005_signal,
    f37hg_f37_hypergrowth_signature_r40_252d_base_v006_signal,
    f37hg_f37_hypergrowth_signature_r40_126d_base_v007_signal,
    f37hg_f37_hypergrowth_signature_r40_63d_base_v008_signal,
    f37hg_f37_hypergrowth_signature_reinvg_252d_base_v009_signal,
    f37hg_f37_hypergrowth_signature_reinvg_126d_base_v010_signal,
    f37hg_f37_hypergrowth_signature_durcomp_252d_base_v011_signal,
    f37hg_f37_hypergrowth_signature_durcomp_126d_base_v012_signal,
    f37hg_f37_hypergrowth_signature_gpgm_252d_base_v013_signal,
    f37hg_f37_hypergrowth_signature_gpgm_126d_base_v014_signal,
    f37hg_f37_hypergrowth_signature_gpminusrev_252d_base_v015_signal,
    f37hg_f37_hypergrowth_signature_gpminusrev_126d_base_v016_signal,
    f37hg_f37_hypergrowth_signature_r40gm_252d_base_v017_signal,
    f37hg_f37_hypergrowth_signature_r40gm_126d_base_v018_signal,
    f37hg_f37_hypergrowth_signature_effgrowth_252d_base_v019_signal,
    f37hg_f37_hypergrowth_signature_gpperrnd_252d_base_v020_signal,
    f37hg_f37_hypergrowth_signature_selffund_252d_base_v021_signal,
    f37hg_f37_hypergrowth_signature_selffund_126d_base_v022_signal,
    f37hg_f37_hypergrowth_signature_durqz_252d_base_v023_signal,
    f37hg_f37_hypergrowth_signature_r40z_252d_base_v024_signal,
    f37hg_f37_hypergrowth_signature_durqrank_252d_base_v025_signal,
    f37hg_f37_hypergrowth_signature_triscore_252d_base_v026_signal,
    f37hg_f37_hypergrowth_signature_quadscore_252d_base_v027_signal,
    f37hg_f37_hypergrowth_signature_accgm_252d_base_v028_signal,
    f37hg_f37_hypergrowth_signature_r40acc_126d_base_v029_signal,
    f37hg_f37_hypergrowth_signature_reinvgacc_252d_base_v030_signal,
    f37hg_f37_hypergrowth_signature_gpgmrank_252d_base_v031_signal,
    f37hg_f37_hypergrowth_signature_durqema_252d_base_v032_signal,
    f37hg_f37_hypergrowth_signature_gmbal_252d_base_v033_signal,
    f37hg_f37_hypergrowth_signature_r40surplus_252d_base_v034_signal,
    f37hg_f37_hypergrowth_signature_gpmexp_252d_base_v035_signal,
    f37hg_f37_hypergrowth_signature_ocfpergrowth_252d_base_v036_signal,
    f37hg_f37_hypergrowth_signature_durqdisp_252d_base_v037_signal,
    f37hg_f37_hypergrowth_signature_qualreinv_252d_base_v038_signal,
    f37hg_f37_hypergrowth_signature_blendq_252d_base_v039_signal,
    f37hg_f37_hypergrowth_signature_blendq_126d_base_v040_signal,
    f37hg_f37_hypergrowth_signature_seqdurq_63d_base_v041_signal,
    f37hg_f37_hypergrowth_signature_gpocf_252d_base_v042_signal,
    f37hg_f37_hypergrowth_signature_r40consist_126d_base_v043_signal,
    f37hg_f37_hypergrowth_signature_durqsm_252d_base_v044_signal,
    f37hg_f37_hypergrowth_signature_reinvgz_252d_base_v045_signal,
    f37hg_f37_hypergrowth_signature_durqtanh_252d_base_v046_signal,
    f37hg_f37_hypergrowth_signature_loggm_252d_base_v047_signal,
    f37hg_f37_hypergrowth_signature_r40net_252d_base_v048_signal,
    f37hg_f37_hypergrowth_signature_durqdrag_252d_base_v049_signal,
    f37hg_f37_hypergrowth_signature_gpocf_126d_base_v050_signal,
    f37hg_f37_hypergrowth_signature_durqstack_base_v051_signal,
    f37hg_f37_hypergrowth_signature_r40stack_base_v052_signal,
    f37hg_f37_hypergrowth_signature_gpshare_252d_base_v053_signal,
    f37hg_f37_hypergrowth_signature_selfreinv_252d_base_v054_signal,
    f37hg_f37_hypergrowth_signature_gmmom_126d_base_v055_signal,
    f37hg_f37_hypergrowth_signature_r40rank_252d_base_v056_signal,
    f37hg_f37_hypergrowth_signature_gpgz_252d_base_v057_signal,
    f37hg_f37_hypergrowth_signature_durqsurp_252d_base_v058_signal,
    f37hg_f37_hypergrowth_signature_cashrunwg_252d_base_v059_signal,
    f37hg_f37_hypergrowth_signature_durqvol_252d_base_v060_signal,
    f37hg_f37_hypergrowth_signature_r40netrank_252d_base_v061_signal,
    f37hg_f37_hypergrowth_signature_gxmocf_252d_base_v062_signal,
    f37hg_f37_hypergrowth_signature_gpreinv_252d_base_v063_signal,
    f37hg_f37_hypergrowth_signature_durq_504d_base_v064_signal,
    f37hg_f37_hypergrowth_signature_r40_504d_base_v065_signal,
    f37hg_f37_hypergrowth_signature_gmconvex_252d_base_v066_signal,
    f37hg_f37_hypergrowth_signature_durqconv_252d_base_v067_signal,
    f37hg_f37_hypergrowth_signature_r40gmfloor_252d_base_v068_signal,
    f37hg_f37_hypergrowth_signature_reinvgdist_252d_base_v069_signal,
    f37hg_f37_hypergrowth_signature_durqyoy_252d_base_v070_signal,
    f37hg_f37_hypergrowth_signature_cashvsreinv_252d_base_v071_signal,
    f37hg_f37_hypergrowth_signature_gptraj_126d_base_v072_signal,
    f37hg_f37_hypergrowth_signature_health_252d_base_v073_signal,
    f37hg_f37_hypergrowth_signature_r40ocfslope_126d_base_v074_signal,
    f37hg_f37_hypergrowth_signature_durqshare_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f37_hypergrowth_signature_base_001_075_claude: %d features pass" % n_features)
