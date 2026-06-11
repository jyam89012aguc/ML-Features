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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _macd(s, a, b):
    # fast-minus-slow EWM band-pass of a series
    return s.ewm(span=a, min_periods=max(2, a // 2)).mean() - s.ewm(span=b, min_periods=max(3, b // 2)).mean()


# ===== folder domain primitives (stock-based-comp dilution overhang) =====
def _f48_dilrate(sbcomp, marketcap):
    # annualized SBC dilution rate = stock comp as a fraction of market cap
    return sbcomp / marketcap.replace(0, np.nan)


def _f48_promote(sbcomp, opex):
    # promote intensity = SBC as a fraction of total operating expense
    return sbcomp / opex.replace(0, np.nan)


def _f48_sgna_load(sbcomp, sgna):
    # SBC as a fraction of SG&A (where stock comp usually books)
    return sbcomp / sgna.replace(0, np.nan)


def _f48_rev_load(sbcomp, revenue):
    # SBC per dollar of revenue (meaningful for producers)
    return sbcomp / revenue.replace(0, np.nan)


def _f48_burn_subsidy(sbcomp, ncfo):
    # non-cash comp subsidy relative to the magnitude of operating cash burn
    return sbcomp / ncfo.abs().replace(0, np.nan)


def _f48_overhang(shareswadil, shareswa):
    # diluted-vs-basic share overhang from options / RSUs / warrants
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f48_papermix(sbcomp, ncfcommon):
    # paper-vs-cash mix: SBC vs net cash raised from common (ncfcommon swings sign)
    return sbcomp / (sbcomp + ncfcommon.abs()).replace(0, np.nan)


def _f48_growth(s, w):
    # log growth of a (possibly negative) fundamental series over w days, on magnitude
    return np.log(s.abs().replace(0, np.nan) / s.shift(w).abs().replace(0, np.nan))


def _f48_truedil(sbcomp, marketcap, shareswa, w):
    # combined true dilution = SBC/mktcap + realized weighted-share growth
    rate = sbcomp / marketcap.replace(0, np.nan)
    grow = shareswa / shareswa.shift(w).replace(0, np.nan) - 1.0
    return rate + grow


# SBC dilution rate (SBC/marketcap) smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_dilrate_126d_base_v076_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate percentile-ranked vs its multi-year (1260d) history
def f48sb_f48_sbc_dilution_overhang_dilrate_1260d_base_v077_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _rank(r, 1260)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate z-scored vs its 504d history (slower de-trend)
def f48sb_f48_sbc_dilution_overhang_dilratezlong_504d_base_v078_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# tanh-squashed SBC dilution-rate deviation from its 252d mean
def f48sb_f48_sbc_dilution_overhang_dilratetanh_252d_base_v079_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    d = r - r.rolling(252, min_periods=84).mean()
    result = np.tanh(50.0 * d)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate now minus its level one year ago (YoY overhang change)
def f48sb_f48_sbc_dilution_overhang_dilrateyoy_252d_base_v080_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r - r.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity (SBC/opex) smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_promote_126d_base_v081_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity percentile-ranked vs its 1260d history
def f48sb_f48_sbc_dilution_overhang_promote_1260d_base_v082_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _rank(p, 1260)
    return result.replace([np.inf, -np.inf], np.nan)

# log promote intensity (tail-compressed SBC/opex)
def f48sb_f48_sbc_dilution_overhang_promotelog_252d_base_v083_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = np.log1p(p.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity now minus one year ago
def f48sb_f48_sbc_dilution_overhang_promoteyoy_252d_base_v084_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p - p.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# coefficient of variation of promote intensity
def f48sb_f48_sbc_dilution_overhang_promotecv_252d_base_v085_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _std(p, 252) / _mean(p, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/SG&A load percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_sgnaload_504d_base_v086_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = _rank(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/SG&A load now minus one year ago
def f48sb_f48_sbc_dilution_overhang_sgnaloadyoy_252d_base_v087_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = g - g.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/SG&A load minus its 126d EMA (displacement)
def f48sb_f48_sbc_dilution_overhang_sgnaloaddev_126d_base_v088_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = g - g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# spread: SG&A load (SBC/sgna) minus promote intensity (SBC/opex), reversed view
def f48sb_f48_sbc_dilution_overhang_sgnavsopex_252d_base_v089_signal(sbcomp, sgna, opex):
    g = _f48_sgna_load(sbcomp, sgna)
    p = _f48_promote(sbcomp, opex)
    result = g - p
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/revenue load smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_revload_126d_base_v090_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = rl.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/revenue load percentile-ranked vs its 1260d history
def f48sb_f48_sbc_dilution_overhang_revload_1260d_base_v091_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = _rank(rl, 1260)
    return result.replace([np.inf, -np.inf], np.nan)

# tanh-squashed SBC/revenue load deviation from its 252d median
def f48sb_f48_sbc_dilution_overhang_revloadtanh_252d_base_v092_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    med = rl.rolling(252, min_periods=84).median()
    result = np.tanh(2.0 * (rl - med))
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/revenue load now minus one year ago
def f48sb_f48_sbc_dilution_overhang_revloadyoy_252d_base_v093_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = rl - rl.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy ratio smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_burnsub_126d_base_v094_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = bs.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# log burn-subsidy ratio (tail-compressed SBC plug of cash burn)
def f48sb_f48_sbc_dilution_overhang_burnsublog_252d_base_v095_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = np.log1p(bs.clip(lower=0, upper=50.0))
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy ratio now minus one year ago
def f48sb_f48_sbc_dilution_overhang_burnsubyoy_252d_base_v096_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = bs - bs.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# coefficient of variation of the burn-subsidy ratio
def f48sb_f48_sbc_dilution_overhang_burnsubcv_252d_base_v097_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = _std(bs, 252) / _mean(bs, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_overhang_126d_base_v098_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang percentile-ranked vs its 1260d history
def f48sb_f48_sbc_dilution_overhang_overhang_1260d_base_v099_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _rank(o, 1260)
    return result.replace([np.inf, -np.inf], np.nan)

# log share overhang (tail-compressed dilutive-securities cushion)
def f48sb_f48_sbc_dilution_overhang_overhanglog_252d_base_v100_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = np.log1p(o.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)

# tanh-squashed share-overhang deviation from its 252d mean
def f48sb_f48_sbc_dilution_overhang_overhangtanh_252d_base_v101_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    d = o - o.rolling(252, min_periods=84).mean()
    result = np.tanh(40.0 * d)
    return result.replace([np.inf, -np.inf], np.nan)

# share-overhang momentum over a half-year (change in dilutive overhang)
def f48sb_f48_sbc_dilution_overhang_overhanghalf_126d_base_v102_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o - o.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash mix smoothed over a half-year
def f48sb_f48_sbc_dilution_overhang_papermix_126d_base_v103_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = m.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash mix now minus one year ago
def f48sb_f48_sbc_dilution_overhang_papermixyoy_252d_base_v104_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = m - m.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion of the paper-vs-cash mix (financing-channel instability)
def f48sb_f48_sbc_dilution_overhang_papermixdisp_126d_base_v105_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC relative to net cash raised: log ratio of SBC to |ncfcommon|
def f48sb_f48_sbc_dilution_overhang_papervscash_252d_base_v106_signal(sbcomp, ncfcommon):
    result = np.log(sbcomp.replace(0, np.nan) / ncfcommon.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution with a half-year share-growth window
def f48sb_f48_sbc_dilution_overhang_truedil_126d_base_v107_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 126)
    result = t.rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution now minus one year ago
def f48sb_f48_sbc_dilution_overhang_truedilyoy_252d_base_v108_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = t - t.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion of combined true dilution
def f48sb_f48_sbc_dilution_overhang_truedildisp_126d_base_v109_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = _std(t, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution percentile-ranked vs its multi-year history
def f48sb_f48_sbc_dilution_overhang_truedildil_1260d_base_v110_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = _rank(t, 1260)
    return result.replace([np.inf, -np.inf], np.nan)

# two-year SBC growth (log), multi-cycle silent-dilution expansion
def f48sb_f48_sbc_dilution_overhang_sbcgrow_504d_base_v111_signal(sbcomp):
    result = _f48_growth(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# half-year SBC growth rate
def f48sb_f48_sbc_dilution_overhang_sbcgrow_126d_base_v112_signal(sbcomp):
    result = sbcomp / sbcomp.shift(126).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# annual SBC growth percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_sbcgrowrank_504d_base_v113_signal(sbcomp):
    g = _f48_growth(sbcomp, 252)
    result = _rank(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# sign x sqrt-magnitude of annual SBC growth (directional, tail-tamed)
def f48sb_f48_sbc_dilution_overhang_sbcgrowsignmag_252d_base_v114_signal(sbcomp):
    g = _f48_growth(sbcomp, 252)
    result = np.sign(g) * g.abs() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# SBC-vs-opex growth balance bounded [-1,1] (comp outgrowing the cost base)
def f48sb_f48_sbc_dilution_overhang_sbcvsopexbal_252d_base_v115_signal(sbcomp, opex):
    gs = _f48_growth(sbcomp, 252)
    go = _f48_growth(opex, 252)
    result = (gs - go) / (gs.abs() + go.abs()).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# realized weighted-share growth as a fraction of SBC growth (cash-issuance share of total comp expansion)
def f48sb_f48_sbc_dilution_overhang_sharegrowvssbc_252d_base_v116_signal(sbcomp, shareswa):
    gs = _f48_growth(sbcomp, 252)
    gh = _f48_growth(shareswa, 252)
    result = gh / gs.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC-vs-SG&A growth balance bounded [-1,1]
def f48sb_f48_sbc_dilution_overhang_sbcvssgnabal_252d_base_v117_signal(sbcomp, sgna):
    gs = _f48_growth(sbcomp, 252)
    gg = _f48_growth(sgna, 252)
    result = (gs - gg) / (gs.abs() + gg.abs()).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: SBC dilution rate times burn-subsidy (overhang on a cash-burning junior)
def f48sb_f48_sbc_dilution_overhang_dilrateXburn_252d_base_v118_signal(sbcomp, marketcap, ncfo):
    r = _f48_dilrate(sbcomp, marketcap)
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=5.0)
    result = (r * bs).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: promote intensity times share overhang
def f48sb_f48_sbc_dilution_overhang_promoteXoverhang_252d_base_v119_signal(sbcomp, opex, shareswadil, shareswa):
    p = _f48_promote(sbcomp, opex)
    o = _f48_overhang(shareswadil, shareswa)
    result = (p * o).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: SBC/SG&A load times SBC dilution rate (concentrated overhang channel)
def f48sb_f48_sbc_dilution_overhang_sgnaloadXdilrate_252d_base_v120_signal(sbcomp, sgna, marketcap):
    g = _f48_sgna_load(sbcomp, sgna)
    r = _f48_dilrate(sbcomp, marketcap)
    result = (g * r).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# fraction of last year SBC dilution rate sits above its 252d 80th-pct band (high-overhang regime time)
def f48sb_f48_sbc_dilution_overhang_dilratehighfrac_252d_base_v121_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    q80 = r.rolling(252, min_periods=84).quantile(0.80)
    result = (r > q80).astype(float).rolling(126, min_periods=42).mean() - 0.25
    return result.replace([np.inf, -np.inf], np.nan)

# high-overhang regime distance: overhang vs its 252d 80th-pct band
def f48sb_f48_sbc_dilution_overhang_overhangrgime_252d_base_v122_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    q80 = o.rolling(252, min_periods=84).quantile(0.80)
    result = o - q80
    return result.replace([np.inf, -np.inf], np.nan)

# fraction of last year burn-subsidy exceeds 1.0 (SBC bigger than cash burn)
def f48sb_f48_sbc_dilution_overhang_burnsubrgime_252d_base_v123_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = (bs > 1.0).astype(float).rolling(252, min_periods=84).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# skew of the SBC dilution rate over a year (grant-spike asymmetry)
def f48sb_f48_sbc_dilution_overhang_dilrateskew_252d_base_v124_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# skew of share overhang over a year
def f48sb_f48_sbc_dilution_overhang_overhangskew_252d_base_v125_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# skew of promote intensity over a year
def f48sb_f48_sbc_dilution_overhang_promoteskew_252d_base_v126_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate relative to its trailing 252d max (drawdown from peak overhang)
def f48sb_f48_sbc_dilution_overhang_dilratedd_252d_base_v127_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    hi = _rmax(r, 252)
    result = r / hi.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang relative to its trailing 252d max
def f48sb_f48_sbc_dilution_overhang_overhangdd_252d_base_v128_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    hi = _rmax(o, 252)
    result = o / hi.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# composite overhang index: avg of standardized dilrate, overhang and burn-subsidy
def f48sb_f48_sbc_dilution_overhang_truedilcompose_252d_base_v129_signal(sbcomp, marketcap, shareswadil, shareswa, ncfo):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    bs = _z(_f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0), 252)
    result = pd.concat([r, o, bs], axis=1).mean(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)

# disagreement across overhang channels: std of standardized dilrate/overhang/promote
def f48sb_f48_sbc_dilution_overhang_overhangindexdisp_252d_base_v130_signal(sbcomp, marketcap, shareswadil, shareswa, opex):
    r = _z(_f48_dilrate(sbcomp, marketcap), 252)
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    p = _z(_f48_promote(sbcomp, opex), 252)
    result = pd.concat([r, o, p], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)

# balance of SBC growth vs revenue growth, bounded [-1,1]
def f48sb_f48_sbc_dilution_overhang_sbcrevbalance_252d_base_v131_signal(sbcomp, revenue):
    gs = _f48_growth(sbcomp, 252)
    gr = _f48_growth(revenue, 252)
    result = (gs - gr) / (gs.abs() + gr.abs()).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# balance of SBC growth vs market-cap growth, bounded [-1,1]
def f48sb_f48_sbc_dilution_overhang_sbcmcapbalance_252d_base_v132_signal(sbcomp, marketcap):
    gs = _f48_growth(sbcomp, 252)
    gm = _f48_growth(marketcap, 252)
    result = (gs - gm) / (gs.abs() + gm.abs()).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# quarterly momentum of the SBC dilution rate
def f48sb_f48_sbc_dilution_overhang_dilratehalfmom_63d_base_v133_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# quarterly momentum of promote intensity
def f48sb_f48_sbc_dilution_overhang_promotehalfmom_63d_base_v134_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p - p.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# quarterly momentum of the burn-subsidy ratio
def f48sb_f48_sbc_dilution_overhang_burnsubhalfmom_63d_base_v135_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = bs - bs.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# EWM share overhang minus its raw level (overhang persistence gap)
def f48sb_f48_sbc_dilution_overhang_overhangewm_126d_base_v136_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o.ewm(span=126, min_periods=42).mean() - o
    return result.replace([np.inf, -np.inf], np.nan)

# ratio of SBC dilution rate to its 252d median (relative overhang elevation)
def f48sb_f48_sbc_dilution_overhang_dilrateminratio_252d_base_v137_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    med = r.rolling(252, min_periods=84).median()
    result = r / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio of promote intensity to its 252d median
def f48sb_f48_sbc_dilution_overhang_promoteminratio_252d_base_v138_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    med = p.rolling(252, min_periods=84).median()
    result = p / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: overhang times annual SBC growth (expanding option overhang)
def f48sb_f48_sbc_dilution_overhang_sbcoverhangXgrow_252d_base_v139_signal(shareswadil, shareswa, sbcomp):
    o = _f48_overhang(shareswadil, shareswa)
    g = _f48_growth(sbcomp, 252)
    result = (o * g).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: SBC/revenue load times revenue contraction flag (overhang as revenue falls)
def f48sb_f48_sbc_dilution_overhang_revloadXgrow_252d_base_v140_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    gr = _f48_growth(revenue, 252)
    contr = (gr < 0).astype(float)
    result = (rl * contr).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution-rate acceleration: 63d change now vs a quarter ago
def f48sb_f48_sbc_dilution_overhang_dilrateaccel_252d_base_v141_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    d = r - r.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy acceleration
def f48sb_f48_sbc_dilution_overhang_burnsubaccel_252d_base_v142_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    d = bs - bs.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash mix acceleration
def f48sb_f48_sbc_dilution_overhang_papermixaccel_252d_base_v143_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    d = m - m.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# share-overhang acceleration (63d change of 63d change)
def f48sb_f48_sbc_dilution_overhang_overhangaccel2_252d_base_v144_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    d = o - o.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# trough promote intensity over the last year (lowest grant period)
def f48sb_f48_sbc_dilution_overhang_promotemin_252d_base_v145_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _rmin(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# trough SBC dilution rate over the last year
def f48sb_f48_sbc_dilution_overhang_dilratemin_252d_base_v146_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _rmin(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# EWM-smoothed annual SBC growth (de-noised silent-dilution trend)
def f48sb_f48_sbc_dilution_overhang_sbcgrowewm_252d_base_v147_signal(sbcomp):
    g = _f48_growth(sbcomp, 252)
    result = g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy relative to its 252d max (paper-plug drawdown)
def f48sb_f48_sbc_dilution_overhang_burnsubdd_252d_base_v148_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    hi = _rmax(bs, 252)
    result = bs / hi.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EWM SBC/revenue load minus its raw level (producer overhang persistence)
def f48sb_f48_sbc_dilution_overhang_revloadewm_126d_base_v149_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = rl.ewm(span=126, min_periods=42).mean() - rl
    return result.replace([np.inf, -np.inf], np.nan)

# fraction of last year SBC dominates total comp+financing (paper-dominant share)
def f48sb_f48_sbc_dilution_overhang_papermixregime_252d_base_v150_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = (m > 0.5).astype(float).rolling(252, min_periods=84).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f48sb_f48_sbc_dilution_overhang_dilrate_126d_base_v076_signal,
    f48sb_f48_sbc_dilution_overhang_dilrate_1260d_base_v077_signal,
    f48sb_f48_sbc_dilution_overhang_dilratezlong_504d_base_v078_signal,
    f48sb_f48_sbc_dilution_overhang_dilratetanh_252d_base_v079_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateyoy_252d_base_v080_signal,
    f48sb_f48_sbc_dilution_overhang_promote_126d_base_v081_signal,
    f48sb_f48_sbc_dilution_overhang_promote_1260d_base_v082_signal,
    f48sb_f48_sbc_dilution_overhang_promotelog_252d_base_v083_signal,
    f48sb_f48_sbc_dilution_overhang_promoteyoy_252d_base_v084_signal,
    f48sb_f48_sbc_dilution_overhang_promotecv_252d_base_v085_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaload_504d_base_v086_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadyoy_252d_base_v087_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloaddev_126d_base_v088_signal,
    f48sb_f48_sbc_dilution_overhang_sgnavsopex_252d_base_v089_signal,
    f48sb_f48_sbc_dilution_overhang_revload_126d_base_v090_signal,
    f48sb_f48_sbc_dilution_overhang_revload_1260d_base_v091_signal,
    f48sb_f48_sbc_dilution_overhang_revloadtanh_252d_base_v092_signal,
    f48sb_f48_sbc_dilution_overhang_revloadyoy_252d_base_v093_signal,
    f48sb_f48_sbc_dilution_overhang_burnsub_126d_base_v094_signal,
    f48sb_f48_sbc_dilution_overhang_burnsublog_252d_base_v095_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubyoy_252d_base_v096_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubcv_252d_base_v097_signal,
    f48sb_f48_sbc_dilution_overhang_overhang_126d_base_v098_signal,
    f48sb_f48_sbc_dilution_overhang_overhang_1260d_base_v099_signal,
    f48sb_f48_sbc_dilution_overhang_overhanglog_252d_base_v100_signal,
    f48sb_f48_sbc_dilution_overhang_overhangtanh_252d_base_v101_signal,
    f48sb_f48_sbc_dilution_overhang_overhanghalf_126d_base_v102_signal,
    f48sb_f48_sbc_dilution_overhang_papermix_126d_base_v103_signal,
    f48sb_f48_sbc_dilution_overhang_papermixyoy_252d_base_v104_signal,
    f48sb_f48_sbc_dilution_overhang_papermixdisp_126d_base_v105_signal,
    f48sb_f48_sbc_dilution_overhang_papervscash_252d_base_v106_signal,
    f48sb_f48_sbc_dilution_overhang_truedil_126d_base_v107_signal,
    f48sb_f48_sbc_dilution_overhang_truedilyoy_252d_base_v108_signal,
    f48sb_f48_sbc_dilution_overhang_truedildisp_126d_base_v109_signal,
    f48sb_f48_sbc_dilution_overhang_truedildil_1260d_base_v110_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrow_504d_base_v111_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrow_126d_base_v112_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowrank_504d_base_v113_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowsignmag_252d_base_v114_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsopexbal_252d_base_v115_signal,
    f48sb_f48_sbc_dilution_overhang_sharegrowvssbc_252d_base_v116_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvssgnabal_252d_base_v117_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateXburn_252d_base_v118_signal,
    f48sb_f48_sbc_dilution_overhang_promoteXoverhang_252d_base_v119_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadXdilrate_252d_base_v120_signal,
    f48sb_f48_sbc_dilution_overhang_dilratehighfrac_252d_base_v121_signal,
    f48sb_f48_sbc_dilution_overhang_overhangrgime_252d_base_v122_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubrgime_252d_base_v123_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateskew_252d_base_v124_signal,
    f48sb_f48_sbc_dilution_overhang_overhangskew_252d_base_v125_signal,
    f48sb_f48_sbc_dilution_overhang_promoteskew_252d_base_v126_signal,
    f48sb_f48_sbc_dilution_overhang_dilratedd_252d_base_v127_signal,
    f48sb_f48_sbc_dilution_overhang_overhangdd_252d_base_v128_signal,
    f48sb_f48_sbc_dilution_overhang_truedilcompose_252d_base_v129_signal,
    f48sb_f48_sbc_dilution_overhang_overhangindexdisp_252d_base_v130_signal,
    f48sb_f48_sbc_dilution_overhang_sbcrevbalance_252d_base_v131_signal,
    f48sb_f48_sbc_dilution_overhang_sbcmcapbalance_252d_base_v132_signal,
    f48sb_f48_sbc_dilution_overhang_dilratehalfmom_63d_base_v133_signal,
    f48sb_f48_sbc_dilution_overhang_promotehalfmom_63d_base_v134_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubhalfmom_63d_base_v135_signal,
    f48sb_f48_sbc_dilution_overhang_overhangewm_126d_base_v136_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateminratio_252d_base_v137_signal,
    f48sb_f48_sbc_dilution_overhang_promoteminratio_252d_base_v138_signal,
    f48sb_f48_sbc_dilution_overhang_sbcoverhangXgrow_252d_base_v139_signal,
    f48sb_f48_sbc_dilution_overhang_revloadXgrow_252d_base_v140_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateaccel_252d_base_v141_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubaccel_252d_base_v142_signal,
    f48sb_f48_sbc_dilution_overhang_papermixaccel_252d_base_v143_signal,
    f48sb_f48_sbc_dilution_overhang_overhangaccel2_252d_base_v144_signal,
    f48sb_f48_sbc_dilution_overhang_promotemin_252d_base_v145_signal,
    f48sb_f48_sbc_dilution_overhang_dilratemin_252d_base_v146_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowewm_252d_base_v147_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubdd_252d_base_v148_signal,
    f48sb_f48_sbc_dilution_overhang_revloadewm_126d_base_v149_signal,
    f48sb_f48_sbc_dilution_overhang_papermixregime_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SBC_DILUTION_OVERHANG_REGISTRY_076_150 = REGISTRY


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

    sbcomp = _fund(201, base=1.2e7, drift=0.03, vol=0.10).rename("sbcomp")
    opex = _fund(202, base=6.0e7, drift=0.02, vol=0.07).rename("opex")
    sgna = _fund(203, base=2.4e7, drift=0.02, vol=0.08).rename("sgna")
    revenue = _fund(204, base=5.0e7, drift=0.025, vol=0.12).rename("revenue")
    marketcap = _fund(205, base=4.0e8, drift=0.01, vol=0.18).rename("marketcap")
    shareswa = _fund(206, base=7.6e7, drift=0.038, vol=0.05).rename("shareswa")
    _gap = _fund(207, base=6.0e6, drift=0.04, vol=0.09).abs()
    shareswadil = (shareswa + _gap).rename("shareswadil")
    _raise = _fund(208, base=2.0e7, drift=0.02, vol=0.5)
    _return = _fund(209, base=1.6e7, drift=0.02, vol=0.45)
    ncfcommon = (_return - _raise).rename("ncfcommon")
    _burn = _fund(210, base=3.0e7, drift=0.015, vol=0.20)
    ncfo = (_burn - 3.0e7 * 0.9).rename("ncfo")

    cols = {"sbcomp": sbcomp, "opex": opex, "sgna": sgna, "revenue": revenue,
            "marketcap": marketcap, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon, "ncfo": ncfo}

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

    print("OK f48_sbc_dilution_overhang_base_076_150_claude: %d features pass" % n_features)
