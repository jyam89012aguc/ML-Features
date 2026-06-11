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
    # trailing growth rate of revenue over window w
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


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
# --- Classic Rule-of-40 (growth + fcf-margin) level at one horizon ---

# Rule-of-40 (annual growth + fcf-margin) raw level
def f23r40_f23_rule_of_40_r40fcf_252d_base_v001_signal(revenue, fcf):
    b = _r40_score_fcf(revenue, fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 fcf score, z-scored vs its own 504d history (de-trended quality)
def f23r40_f23_rule_of_40_r40fcfz_126d_base_v002_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 126)
    b = _z(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 fcf score (quarterly growth), change over a month (composite velocity)
def f23r40_f23_rule_of_40_r40fcfvel_63d_base_v003_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 63)
    b = score - score.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 fcf score (two-year growth), percentile rank vs 504d history
def f23r40_f23_rule_of_40_r40fcfrank_504d_base_v004_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 504)
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with OCF margin (ocf variant), decorrelated facets ---

# Rule-of-40 ocf score (annual growth) minus its slow trend (displacement)
def f23r40_f23_rule_of_40_r40ocfdisp_252d_base_v005_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = score - score.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 ocf score (semiannual growth), z-scored vs 252d history
def f23r40_f23_rule_of_40_r40ocfz_126d_base_v006_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 126)
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 ocf score (quarterly growth), change over a quarter (momentum)
def f23r40_f23_rule_of_40_r40ocfmom_63d_base_v007_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 63)
    b = score - score.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with EBITDA margin (ebitda variant) ---

# Rule-of-40 ebitda score, percentile rank vs 252d history (cross-time quality)
def f23r40_f23_rule_of_40_r40ebdrank_252d_base_v008_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = _rank(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 ebitda score (semiannual growth), z-scored
def f23r40_f23_rule_of_40_r40ebdz_126d_base_v009_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 126)
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 ebitda score (quarterly growth), change over a month
def f23r40_f23_rule_of_40_r40ebdvel_63d_base_v010_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 63)
    b = score - score.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 with gross margin as the quality term ---

# Rule-of-40 gross score, z-scored vs 252d history (de-trended)
def f23r40_f23_rule_of_40_r40grsz_252d_base_v011_signal(revenue, grossmargin):
    score = _r40_score_gross(revenue, grossmargin, 252)
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 gross score (semiannual growth), change over a quarter
def f23r40_f23_rule_of_40_r40grsmom_126d_base_v012_signal(revenue, grossmargin):
    score = _r40_score_gross(revenue, grossmargin, 126)
    b = score - score.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 "passes 40" regime flags (bounded, regime) ---

# fraction of last year the fcf Rule-of-40 score clears the 0.40 bar
def f23r40_f23_rule_of_40_passfcf_252d_base_v013_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    passes = (score >= 0.40).astype(float)
    b = passes.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the ocf Rule-of-40 score clears the 0.40 bar
def f23r40_f23_rule_of_40_passocf_252d_base_v014_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    passes = (score >= 0.40).astype(float)
    b = passes.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded distance of ebitda Rule-of-40 above/below the 0.40 hurdle
def f23r40_f23_rule_of_40_hurdle_ebd_252d_base_v015_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = np.tanh(2.5 * (score - 0.40))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Growth-vs-profitability tradeoff (which side carries the score) ---

# growth-minus-fcf-margin tradeoff, normalized (growth-led vs margin-led)
def f23r40_f23_rule_of_40_balfcf_252d_base_v016_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    b = (g - m) / (g.abs() + m.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-minus-ocf-margin tradeoff, normalized
def f23r40_f23_rule_of_40_balocf_252d_base_v017_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    b = (g - m) / (g.abs() + m.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-minus-ebitda-margin tradeoff (quarterly growth leg), normalized
def f23r40_f23_rule_of_40_balebd_252d_base_v018_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 63)
    b = (g - ebitdamargin) / (g.abs() + ebitdamargin.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-minus-gross-margin tradeoff, normalized
def f23r40_f23_rule_of_40_balgrs_252d_base_v019_signal(revenue, grossmargin):
    g = _r40_growth(revenue, 252)
    b = (g - grossmargin) / (g.abs() + grossmargin.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Efficiency score: growth per unit of cash burn ---

# growth as a fraction of growth-plus-burn (bounded burn-efficiency of growth)
def f23r40_f23_rule_of_40_effburn_252d_base_v020_signal(revenue, fcf):
    g = _r40_growth(revenue, 252).clip(lower=0)
    burn = (-_r40_fcf_margin(fcf, revenue)).clip(lower=0)
    b = (g - burn) / (g + burn + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth per unit of ocf burn, z-scored vs own history (de-trended efficiency)
def f23r40_f23_rule_of_40_effocfburn_252d_base_v021_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    burn = (-_r40_ocf_margin(ncfo, revenue)).clip(lower=0)
    eff = g / (burn + 0.05)
    b = _z(eff, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Growth-with-margin quality: product interaction ---

# growth x fcf-margin interaction (durable growth quality), z-scored vs own history
def f23r40_f23_rule_of_40_qfcf_252d_base_v022_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    b = _z(g * m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x ocf-margin interaction, change over a quarter (quality momentum)
def f23r40_f23_rule_of_40_qocfmom_252d_base_v023_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    q = g * m
    b = q - q.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x ebitda-margin interaction, change over a half-year (quality momentum)
def f23r40_f23_rule_of_40_qebdmom_252d_base_v024_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    q = g * ebitdamargin
    b = q - q.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x gross-margin interaction, change over a quarter (gross-funded growth momentum)
def f23r40_f23_rule_of_40_qgrsmom_252d_base_v025_signal(revenue, grossmargin):
    g = _r40_growth(revenue, 252)
    q = g * grossmargin
    b = q - q.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 momentum at different score builds ---

# year-over-year change in fcf Rule-of-40 score (durable improvement)
def f23r40_f23_rule_of_40_r40fcfyoy_252d_base_v026_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = score - score.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf Rule-of-40 score, ratio of recent mean to year-ago mean (relative improvement)
def f23r40_f23_rule_of_40_r40ocfimprov_252d_base_v027_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    recent = _mean(score, 63)
    prior = _mean(score, 63).shift(189)
    b = recent - prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda Rule-of-40 score acceleration (second difference, jerk-of-quality)
def f23r40_f23_rule_of_40_r40ebdaccel_252d_base_v028_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    d = score - score.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross Rule-of-40 score, percentile rank vs 504d history
def f23r40_f23_rule_of_40_r40grsrank_504d_base_v029_signal(revenue, grossmargin):
    score = _r40_score_gross(revenue, grossmargin, 252)
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf Rule-of-40 score, change over a quarter (composite momentum)
def f23r40_f23_rule_of_40_r40fcfmom_252d_base_v030_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = score - score.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended multi-margin Rule-of-40 composites (distinct combos) ---

# blended cash Rule-of-40 (growth + mean cash-margin), change over a half-year
def f23r40_f23_rule_of_40_blendcashmom_252d_base_v031_signal(revenue, fcf, ncfo):
    g = _r40_growth(revenue, 252)
    m = 0.5 * (_r40_fcf_margin(fcf, revenue) + _r40_ocf_margin(ncfo, revenue))
    score = g + m
    b = score - score.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-leg share of the blended margin Rule-of-40 (how margin-led the composite is)
def f23r40_f23_rule_of_40_blendmgnshare_252d_base_v032_signal(revenue, ebitdamargin, grossmargin):
    g = _r40_growth(revenue, 252)
    m = 0.5 * (ebitdamargin + grossmargin)
    b = m / (g.abs() + m.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# four-way blended Rule-of-40 momentum: change in the all-leg composite
def f23r40_f23_rule_of_40_blendallmom_252d_base_v033_signal(revenue, fcf, ncfo, ebitdamargin):
    g = _r40_growth(revenue, 252)
    m = (_r40_fcf_margin(fcf, revenue) + _r40_ocf_margin(ncfo, revenue) + ebitdamargin) / 3.0
    score = g + m
    b = score - score.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between fcf-blend and gross-blend Rule-of-40 (cash vs accrual blend)
def f23r40_f23_rule_of_40_blendspr_252d_base_v034_signal(revenue, fcf, grossmargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    sg = _r40_score_gross(revenue, grossmargin, 252)
    b = sf - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- consistency / durability of the Rule-of-40 over time ---

# durability: mean fcf Rule-of-40 score minus its volatility (consistent quality)
def f23r40_f23_rule_of_40_durfcf_252d_base_v035_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = _mean(score, 252) - _std(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durability spread: durability of ocf score minus durability of fcf score
def f23r40_f23_rule_of_40_durspr_252d_base_v036_signal(revenue, ncfo, fcf):
    so = _r40_score_ocf(revenue, ncfo, 252)
    sf = _r40_score_fcf(revenue, fcf, 252)
    do = _mean(so, 252) - _std(so, 252)
    df = _mean(sf, 252) - _std(sf, 252)
    b = do - df
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 stability: inverse coefficient of variation of the ebitda score
def f23r40_f23_rule_of_40_stabebd_126d_base_v037_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 126)
    b = _mean(score, 126) / _std(score, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 fcf score volatility (instability of the growth-quality composite)
def f23r40_f23_rule_of_40_volfcf_252d_base_v038_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    b = _std(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durability: mean ocf Rule-of-40 score minus its volatility
def f23r40_f23_rule_of_40_durocf_252d_base_v039_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    b = _mean(score, 252) - _std(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- spreads between cash-based and accrual-margin R40 versions ---

# spread: fcf Rule-of-40 minus ebitda Rule-of-40 (cash vs accrual quality)
def f23r40_f23_rule_of_40_spr_fcfebd_252d_base_v040_signal(revenue, fcf, ebitdamargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    se = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = sf - se
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of ocf Rule-of-40 score to fcf Rule-of-40 score (capex drag inside composite)
def f23r40_f23_rule_of_40_spr_ocffcf_252d_base_v041_signal(revenue, ncfo, fcf):
    so = _r40_score_ocf(revenue, ncfo, 252)
    sf = _r40_score_fcf(revenue, fcf, 252)
    b = _z(so / sf.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-absorption ratio (ebitda-margin retained out of gross-margin), z-scored
def f23r40_f23_rule_of_40_spr_grsebd_252d_base_v042_signal(grossmargin, ebitdamargin):
    retain = ebitdamargin / grossmargin.replace(0, np.nan)
    b = _z(retain, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- short-vs-long horizon Rule-of-40 (accelerating quality) ---

# fcf Rule-of-40: quarterly-growth score minus annual-growth score
def f23r40_f23_rule_of_40_accfcf_63v252_base_v043_signal(revenue, fcf):
    ss = _r40_score_fcf(revenue, fcf, 63)
    sl = _r40_score_fcf(revenue, fcf, 252)
    b = ss - sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf Rule-of-40: semiannual-growth score minus two-year-growth score
def f23r40_f23_rule_of_40_accocf_126v504_base_v044_signal(revenue, ncfo):
    ss = _r40_score_ocf(revenue, ncfo, 126)
    sl = _r40_score_ocf(revenue, ncfo, 504)
    b = ss - sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda Rule-of-40: quarterly-growth score minus semiannual-growth score
def f23r40_f23_rule_of_40_accebd_63v126_base_v045_signal(revenue, ebitdamargin):
    ss = _r40_score_ebitda(revenue, ebitdamargin, 63)
    sl = _r40_score_ebitda(revenue, ebitdamargin, 126)
    b = ss - sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- sign x magnitude of the growth/margin tradeoff ---

# signed-root of the growth-minus-fcf-margin gap (compress tails, keep direction)
def f23r40_f23_rule_of_40_signgapfcf_252d_base_v046_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    gap = g - m
    b = np.sign(gap) * (gap.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of the growth-minus-ebitda-margin gap
def f23r40_f23_rule_of_40_signgapebd_252d_base_v047_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    gap = g - ebitdamargin
    b = np.sign(gap) * (gap.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of the growth-minus-ocf-margin gap
def f23r40_f23_rule_of_40_signgapocf_252d_base_v048_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    gap = g - m
    b = np.sign(gap) * (gap.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin-leg facets (profitability side of R40) ---

# fcf-margin level minus its slow trend (cash-profitability displacement)
def f23r40_f23_rule_of_40_fcfmgn_disp_base_v049_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    b = m - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-margin level, z-scored vs own history
def f23r40_f23_rule_of_40_fcfmgn_z_base_v050_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf-margin level minus fcf-margin level (capex intensity of the cash leg)
def f23r40_f23_rule_of_40_capexgap_base_v051_signal(revenue, fcf, ncfo):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    b = om - fm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-margin trend (improving cash profitability leg over a half-year)
def f23r40_f23_rule_of_40_fcfmgn_trend_base_v052_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend, z-scored
def f23r40_f23_rule_of_40_ebdmgn_trendz_base_v053_signal(revenue, ebitdamargin):
    t = ebitdamargin - ebitdamargin.shift(126)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- quality-gated growth (domain-coupled growth) ---

# revenue growth gated by improving fcf-margin (efficient growth)
def f23r40_f23_rule_of_40_gategrowfcf_252d_base_v054_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    gate = (m - m.shift(63) > 0).astype(float)
    b = g * (0.25 + 0.75 * gate)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semiannual revenue growth gated by ebitda-margin, minus margin drag (net quality growth)
def f23r40_f23_rule_of_40_gategrowebd_252d_base_v055_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 126)
    gate = (ebitdamargin > 0).astype(float)
    b = g * (0.25 + 0.75 * gate) - (ebitdamargin < 0).astype(float) * ebitdamargin.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 surplus / deficit area over the bar ---

# interquartile dispersion of the fcf Rule-of-40 score over the last year (quality range)
def f23r40_f23_rule_of_40_surplusfcf_252d_base_v056_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    q75 = score.rolling(252, min_periods=126).quantile(0.75)
    q25 = score.rolling(252, min_periods=126).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-day streak the ocf Rule-of-40 score sits below the 0.40 bar (deficiency run)
def f23r40_f23_rule_of_40_deficitocf_252d_base_v057_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    below = (score < 0.40)
    grp = (~below).cumsum()
    b = below.groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-margin co-movement / decoupling ---

# rolling correlation of revenue-growth with fcf-margin (do they move together)
def f23r40_f23_rule_of_40_comovefcf_252d_base_v058_signal(revenue, fcf):
    g = _r40_growth(revenue, 63)
    m = _r40_fcf_margin(fcf, revenue)
    b = g.rolling(252, min_periods=126).corr(m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of revenue-growth with ebitda-margin
def f23r40_f23_rule_of_40_comoveebd_252d_base_v059_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 63)
    b = g.rolling(252, min_periods=126).corr(ebitdamargin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- weighted Rule-of-40 (growth-tilted vs margin-tilted) ---

# growth-tilted Rule-of-40: 1.5x growth + 0.5x fcf-margin, z-scored
def f23r40_f23_rule_of_40_grtiltfcf_252d_base_v060_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    m = _r40_fcf_margin(fcf, revenue)
    score = 1.5 * g + 0.5 * m
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-tilted Rule-of-40 (0.5x growth + 1.5x ocf-margin), z-scored vs own history
def f23r40_f23_rule_of_40_mgtiltocf_252d_base_v061_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252)
    m = _r40_ocf_margin(ncfo, revenue)
    b = _z(0.5 * g + 1.5 * m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- geometric / harmonic quality blends ---

# geometric-mean quality of shifted growth and shifted fcf-margin
def f23r40_f23_rule_of_40_geomfcf_252d_base_v062_signal(revenue, fcf):
    g = _r40_growth(revenue, 252) + 0.5
    m = _r40_fcf_margin(fcf, revenue) + 0.5
    raw = np.sign(g * m) * (g.abs() * m.abs()) ** 0.5 - 0.5
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 streak regime ---

# streak length: consecutive periods the fcf Rule-of-40 score stays above 0.40
def f23r40_f23_rule_of_40_streakfcf_252d_base_v063_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    passes = (score >= 0.40)
    grp = (~passes).cumsum()
    b = passes.groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak length: consecutive periods the ebitda Rule-of-40 score stays above 0.40
def f23r40_f23_rule_of_40_streakebd_252d_base_v064_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    passes = (score >= 0.40)
    grp = (~passes).cumsum()
    b = passes.groupby(grp).cumsum().astype(float) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dispersion / spread of margin legs ---

# spread between gross-margin and ebitda-margin (operating-cost absorption)
def f23r40_f23_rule_of_40_opexgap_base_v065_signal(grossmargin, ebitdamargin):
    b = grossmargin - ebitdamargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the three margin legs (which cash metric anchors quality)
def f23r40_f23_rule_of_40_mgndisp_base_v066_signal(revenue, fcf, ncfo, ebitdamargin):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    b = pd.concat([fm, om, ebitdamargin], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- risk-adjusted growth (growth scaled by margin volatility) ---

# revenue growth divided by margin volatility (stable-margin growth), ranked
def f23r40_f23_rule_of_40_growpermgnvol_252d_base_v067_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    mvol = _std(ebitdamargin, 126)
    b = _rank(g / (mvol + 0.02), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mixed-leg Rule-of-40 (fast growth + slow margin) ---

# fast revenue growth + slow average fcf-margin, z-scored (forward-looking R40)
def f23r40_f23_rule_of_40_mixfcf_base_v068_signal(revenue, fcf):
    g = _r40_growth(revenue, 63)
    m = _mean(_r40_fcf_margin(fcf, revenue), 252)
    score = g + m
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast revenue growth + slow average ebitda-margin, z-scored vs own history
def f23r40_f23_rule_of_40_mixebdz_base_v069_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 63)
    m = _mean(ebitdamargin, 252)
    score = g + m
    b = _z(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- normalized Rule-of-40 (score over its own typical magnitude) ---

# fcf Rule-of-40 score normalized by trailing absolute revenue-growth scale
def f23r40_f23_rule_of_40_normfcf_252d_base_v070_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    scale = _mean(_r40_growth(revenue, 252).abs(), 252) + 0.05
    b = score / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 leg breadth (regime, count-friendly) ---

# count of positive legs among growth, fcf-margin, ocf-margin, ebitda-margin
def f23r40_f23_rule_of_40_breadth_base_v071_signal(revenue, fcf, ncfo, ebitdamargin):
    g = _r40_growth(revenue, 252)
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    cnt = (g > 0).astype(float) + (fm > 0).astype(float) + (om > 0).astype(float) + (ebitdamargin > 0).astype(float)
    b = cnt.rolling(63, min_periods=21).mean() + 0.5 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-margin as efficiency multiplier on the cash R40 ---

# Rule-of-40 (growth + ocf-margin) scaled by gross-margin quality, percentile-ranked
def f23r40_f23_rule_of_40_grsmult_252d_base_v072_signal(revenue, ncfo, grossmargin):
    score = _r40_score_ocf(revenue, ncfo, 252)
    raw = score * (0.5 + grossmargin)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log-growth Rule-of-40 momentum (compounding form) ---

# log-revenue-growth + fcf-margin, acceleration (second difference of the log-R40)
def f23r40_f23_rule_of_40_logfcfaccel_252d_base_v073_signal(revenue, fcf):
    lg = np.log(revenue.replace(0, np.nan) / revenue.shift(252).replace(0, np.nan))
    m = _r40_fcf_margin(fcf, revenue)
    score = lg + m
    d = score - score.shift(42)
    b = d - d.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rule-of-40 displacement vs slow EMA ---

# ebitda Rule-of-40 score minus its slow EMA (quality displacement)
def f23r40_f23_rule_of_40_dispebd_252d_base_v074_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = score - score.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- combined growth-quality composite ---

# margin-quality agreement: mean of three margin legs net of their dispersion (cohesion)
def f23r40_f23_rule_of_40_mgncohesion_252d_base_v075_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    cohesion = legs.mean(axis=1) - (legs.max(axis=1) - legs.min(axis=1))
    g = _r40_growth(revenue, 252)
    b = cohesion * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23r40_f23_rule_of_40_r40fcf_252d_base_v001_signal,
    f23r40_f23_rule_of_40_r40fcfz_126d_base_v002_signal,
    f23r40_f23_rule_of_40_r40fcfvel_63d_base_v003_signal,
    f23r40_f23_rule_of_40_r40fcfrank_504d_base_v004_signal,
    f23r40_f23_rule_of_40_r40ocfdisp_252d_base_v005_signal,
    f23r40_f23_rule_of_40_r40ocfz_126d_base_v006_signal,
    f23r40_f23_rule_of_40_r40ocfmom_63d_base_v007_signal,
    f23r40_f23_rule_of_40_r40ebdrank_252d_base_v008_signal,
    f23r40_f23_rule_of_40_r40ebdz_126d_base_v009_signal,
    f23r40_f23_rule_of_40_r40ebdvel_63d_base_v010_signal,
    f23r40_f23_rule_of_40_r40grsz_252d_base_v011_signal,
    f23r40_f23_rule_of_40_r40grsmom_126d_base_v012_signal,
    f23r40_f23_rule_of_40_passfcf_252d_base_v013_signal,
    f23r40_f23_rule_of_40_passocf_252d_base_v014_signal,
    f23r40_f23_rule_of_40_hurdle_ebd_252d_base_v015_signal,
    f23r40_f23_rule_of_40_balfcf_252d_base_v016_signal,
    f23r40_f23_rule_of_40_balocf_252d_base_v017_signal,
    f23r40_f23_rule_of_40_balebd_252d_base_v018_signal,
    f23r40_f23_rule_of_40_balgrs_252d_base_v019_signal,
    f23r40_f23_rule_of_40_effburn_252d_base_v020_signal,
    f23r40_f23_rule_of_40_effocfburn_252d_base_v021_signal,
    f23r40_f23_rule_of_40_qfcf_252d_base_v022_signal,
    f23r40_f23_rule_of_40_qocfmom_252d_base_v023_signal,
    f23r40_f23_rule_of_40_qebdmom_252d_base_v024_signal,
    f23r40_f23_rule_of_40_qgrsmom_252d_base_v025_signal,
    f23r40_f23_rule_of_40_r40fcfyoy_252d_base_v026_signal,
    f23r40_f23_rule_of_40_r40ocfimprov_252d_base_v027_signal,
    f23r40_f23_rule_of_40_r40ebdaccel_252d_base_v028_signal,
    f23r40_f23_rule_of_40_r40grsrank_504d_base_v029_signal,
    f23r40_f23_rule_of_40_r40fcfmom_252d_base_v030_signal,
    f23r40_f23_rule_of_40_blendcashmom_252d_base_v031_signal,
    f23r40_f23_rule_of_40_blendmgnshare_252d_base_v032_signal,
    f23r40_f23_rule_of_40_blendallmom_252d_base_v033_signal,
    f23r40_f23_rule_of_40_blendspr_252d_base_v034_signal,
    f23r40_f23_rule_of_40_durfcf_252d_base_v035_signal,
    f23r40_f23_rule_of_40_durspr_252d_base_v036_signal,
    f23r40_f23_rule_of_40_stabebd_126d_base_v037_signal,
    f23r40_f23_rule_of_40_volfcf_252d_base_v038_signal,
    f23r40_f23_rule_of_40_durocf_252d_base_v039_signal,
    f23r40_f23_rule_of_40_spr_fcfebd_252d_base_v040_signal,
    f23r40_f23_rule_of_40_spr_ocffcf_252d_base_v041_signal,
    f23r40_f23_rule_of_40_spr_grsebd_252d_base_v042_signal,
    f23r40_f23_rule_of_40_accfcf_63v252_base_v043_signal,
    f23r40_f23_rule_of_40_accocf_126v504_base_v044_signal,
    f23r40_f23_rule_of_40_accebd_63v126_base_v045_signal,
    f23r40_f23_rule_of_40_signgapfcf_252d_base_v046_signal,
    f23r40_f23_rule_of_40_signgapebd_252d_base_v047_signal,
    f23r40_f23_rule_of_40_signgapocf_252d_base_v048_signal,
    f23r40_f23_rule_of_40_fcfmgn_disp_base_v049_signal,
    f23r40_f23_rule_of_40_fcfmgn_z_base_v050_signal,
    f23r40_f23_rule_of_40_capexgap_base_v051_signal,
    f23r40_f23_rule_of_40_fcfmgn_trend_base_v052_signal,
    f23r40_f23_rule_of_40_ebdmgn_trendz_base_v053_signal,
    f23r40_f23_rule_of_40_gategrowfcf_252d_base_v054_signal,
    f23r40_f23_rule_of_40_gategrowebd_252d_base_v055_signal,
    f23r40_f23_rule_of_40_surplusfcf_252d_base_v056_signal,
    f23r40_f23_rule_of_40_deficitocf_252d_base_v057_signal,
    f23r40_f23_rule_of_40_comovefcf_252d_base_v058_signal,
    f23r40_f23_rule_of_40_comoveebd_252d_base_v059_signal,
    f23r40_f23_rule_of_40_grtiltfcf_252d_base_v060_signal,
    f23r40_f23_rule_of_40_mgtiltocf_252d_base_v061_signal,
    f23r40_f23_rule_of_40_geomfcf_252d_base_v062_signal,
    f23r40_f23_rule_of_40_streakfcf_252d_base_v063_signal,
    f23r40_f23_rule_of_40_streakebd_252d_base_v064_signal,
    f23r40_f23_rule_of_40_opexgap_base_v065_signal,
    f23r40_f23_rule_of_40_mgndisp_base_v066_signal,
    f23r40_f23_rule_of_40_growpermgnvol_252d_base_v067_signal,
    f23r40_f23_rule_of_40_mixfcf_base_v068_signal,
    f23r40_f23_rule_of_40_mixebdz_base_v069_signal,
    f23r40_f23_rule_of_40_normfcf_252d_base_v070_signal,
    f23r40_f23_rule_of_40_breadth_base_v071_signal,
    f23r40_f23_rule_of_40_grsmult_252d_base_v072_signal,
    f23r40_f23_rule_of_40_logfcfaccel_252d_base_v073_signal,
    f23r40_f23_rule_of_40_dispebd_252d_base_v074_signal,
    f23r40_f23_rule_of_40_mgncohesion_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_RULE_OF_40_REGISTRY_001_075 = REGISTRY


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

    print("OK f23_rule_of_40_base_001_075_claude: %d features pass" % n_features)
