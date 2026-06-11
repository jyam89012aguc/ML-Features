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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # normalized linear-time slope over a window (per-step drift)
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives: SBC dilution / overhang =====
def _sb_dilrate(sbcomp, marketcap):
    return _safe_div(sbcomp, marketcap)


def _sb_promote_opex(sbcomp, opex):
    return _safe_div(sbcomp, opex)


def _sb_promote_rev(sbcomp, revenue):
    return _safe_div(sbcomp, revenue)


def _sb_burn_subsidy(sbcomp, ncfo):
    return _safe_div(sbcomp, ncfo.abs())


def _sb_overhang(shareswadil, shareswa):
    return _safe_div(shareswadil, shareswa) - 1.0


def _sb_paper_vs_cash(sbcomp, ncfcommon):
    return _safe_div(sbcomp, ncfcommon.abs())


# ============================================================
# --- cross-channel SBC composites & interactions, v076-v090 ---

# total paper-comp burden: SBC as a fraction of revenue plus opex (combined cost base)
def f28sb_f28_sbc_dilution_overhang_burden_combined_63d_base_v076_signal(sbcomp, revenue, opex):
    b = _mean(_safe_div(sbcomp, revenue + opex), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate x overhang interaction (paper cost meets latent share creep)
def f28sb_f28_sbc_dilution_overhang_dil_x_overhang_63d_base_v077_signal(sbcomp, marketcap, shareswadil, shareswa):
    d = _sb_dilrate(sbcomp, marketcap)
    o = _sb_overhang(shareswadil, shareswa)
    b = _mean(d * o, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue minus promote-vs-opex (where the comp burden concentrates)
def f28sb_f28_sbc_dilution_overhang_prom_spread_63d_base_v078_signal(sbcomp, revenue, opex):
    pr = _sb_promote_rev(sbcomp, revenue)
    po = _sb_promote_opex(sbcomp, opex)
    b = _mean(pr - po, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC vs combined cash drains: sbcomp / (|ncfo| + |ncfcommon|) (total cash subsidy)
def f28sb_f28_sbc_dilution_overhang_cashsubsidy_63d_base_v079_signal(sbcomp, ncfo, ncfcommon):
    b = _mean(_safe_div(sbcomp, ncfo.abs() + ncfcommon.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy x dilution-rate (paper comp both subsidizing burn and diluting)
def f28sb_f28_sbc_dilution_overhang_burn_x_dil_63d_base_v080_signal(sbcomp, ncfo, marketcap):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    d = _sb_dilrate(sbcomp, marketcap)
    b = _mean(s * d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: SBC growth vs market-cap growth (dilution outrunning value)
def f28sb_f28_sbc_dilution_overhang_sbc_vs_mcap_grow_126d_base_v081_signal(sbcomp, marketcap):
    b = _roc(sbcomp, 126) - _roc(marketcap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang relative to dilution-rate (latent share creep per dollar of paper cost)
def f28sb_f28_sbc_dilution_overhang_overhang_per_dil_63d_base_v082_signal(shareswadil, shareswa, sbcomp, marketcap):
    o = _sb_overhang(shareswadil, shareswa)
    d = _sb_dilrate(sbcomp, marketcap)
    b = _mean(_safe_div(o, d), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dilution pressure: SBC issuance net of common cash flow, scaled by market cap
def f28sb_f28_sbc_dilution_overhang_net_dil_pressure_63d_base_v083_signal(sbcomp, marketcap, ncfcommon):
    # ncfcommon>0 returns cash (offsets dilution); <0 raises cash (adds dilution)
    net_issuance = sbcomp - ncfcommon
    b = _mean(_safe_div(net_issuance, marketcap), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity per unit of operating cash: sbcomp / (|ncfo| + revenue) blended base
def f28sb_f28_sbc_dilution_overhang_sbc_blendbase_63d_base_v084_signal(sbcomp, ncfo, revenue):
    b = _mean(_safe_div(sbcomp, ncfo.abs() + revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-occurrence: fraction of half-year both comp burden and overhang sit above their medians
def f28sb_f28_sbc_dilution_overhang_cochannel_126d_base_v085_signal(sbcomp, revenue, shareswadil, shareswa):
    pr = _sb_promote_rev(sbcomp, revenue)
    ov = _sb_overhang(shareswadil, shareswa)
    pr_hi = (pr >= pr.rolling(252, min_periods=63).median()).astype(float)
    ov_hi = (ov >= ov.rolling(252, min_periods=63).median()).astype(float)
    both = (pr_hi * ov_hi)
    b = both.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounded dilution intensity: product of dilution-rate z and overhang z (both spikes align)
def f28sb_f28_sbc_dilution_overhang_compound_126d_base_v086_signal(sbcomp, marketcap, shareswadil, shareswa):
    zd = _z(_sb_dilrate(sbcomp, marketcap), 126)
    zo = _z(_sb_overhang(shareswadil, shareswa), 126)
    b = zd * zo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: SBC growth vs revenue growth (paper comp outrunning the business)
def f28sb_f28_sbc_dilution_overhang_sbc_vs_rev_grow_126d_base_v087_signal(sbcomp, revenue):
    b = _roc(sbcomp, 126) - _roc(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# which cash drain SBC dominates: z(paper-vs-cash) minus z(burn-subsidy), normalized
def f28sb_f28_sbc_dilution_overhang_papercash_vs_burn_126d_base_v088_signal(sbcomp, ncfcommon, ncfo):
    pc = _z(_sb_paper_vs_cash(sbcomp, ncfcommon), 126)
    bs = _z(_sb_burn_subsidy(sbcomp, ncfo), 126)
    b = pc - bs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang plus dilution-rate composite z (two normalized dilution channels, 126d)
def f28sb_f28_sbc_dilution_overhang_dualz_126d_base_v089_signal(sbcomp, marketcap, shareswadil, shareswa):
    zd = _z(_sb_dilrate(sbcomp, marketcap), 126)
    zo = _z(_sb_overhang(shareswadil, shareswa), 126)
    b = 0.5 * (zd + zo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC fraction of total spend covered by paper: sbcomp / (opex + |ncfcommon|)
def f28sb_f28_sbc_dilution_overhang_sbc_spendcover_63d_base_v090_signal(sbcomp, opex, ncfcommon):
    b = _mean(_safe_div(sbcomp, opex + ncfcommon.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- second-order dynamics (slopes/accels/vol-of) v091-v110 ---

# dilution-rate slope over a half-year (trajectory of paper-cost intensity)
def f28sb_f28_sbc_dilution_overhang_dilrate_slope_126d_base_v091_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    b = _slope(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang slope over a half-year (trajectory of latent dilution)
def f28sb_f28_sbc_dilution_overhang_overhang_slope_126d_base_v092_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 21)
    b = _slope(o, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex volatility-of-level (instability of comp embedment)
def f28sb_f28_sbc_dilution_overhang_promopex_voloflvl_126d_base_v093_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    b = _std(_roc(p, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy volatility-of-change (instability of cash subsidy)
def f28sb_f28_sbc_dilution_overhang_burnsub_volofchg_126d_base_v094_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    b = _std(s - s.shift(21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue acceleration (2nd diff of comp burden, half-year spans)
def f28sb_f28_sbc_dilution_overhang_promrev_accel_126d_base_v095_signal(sbcomp, revenue):
    p = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    b = (p - p.shift(126)) - (p.shift(126) - p.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate jerk-as-level: change in its quarterly acceleration
def f28sb_f28_sbc_dilution_overhang_dilrate_jerklvl_63d_base_v096_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    acc = (d - d.shift(63)) - (d.shift(63) - d.shift(126))
    b = acc - acc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash slope over a quarter (trajectory of paper-vs-cash mix)
def f28sb_f28_sbc_dilution_overhang_papercash_slope_63d_base_v097_signal(sbcomp, ncfcommon):
    p = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 21)
    b = _slope(p, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang volatility (instability of diluted-vs-basic gap)
def f28sb_f28_sbc_dilution_overhang_overhang_vol_126d_base_v098_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = _std(o, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate vol-of-vol (regime instability of paper-cost dispersion)
def f28sb_f28_sbc_dilution_overhang_dilrate_volofvol_126d_base_v099_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    v = _std(d, 63)
    b = _std(v, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex slope minus promote-vs-revenue slope (divergent burden trajectories)
def f28sb_f28_sbc_dilution_overhang_prom_slopespr_126d_base_v100_signal(sbcomp, opex, revenue):
    po = _mean(_sb_promote_opex(sbcomp, opex), 21)
    pr = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    b = _slope(po, 126) - _slope(pr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy slope over a half-year (trajectory of cash subsidy reliance)
def f28sb_f28_sbc_dilution_overhang_burnsub_slope_126d_base_v101_signal(sbcomp, ncfo):
    s = _mean(_sb_burn_subsidy(sbcomp, ncfo), 21)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang acceleration over half-year spans (2nd diff of latent creep)
def f28sb_f28_sbc_dilution_overhang_overhang_accel_126d_base_v102_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 21)
    b = (o - o.shift(126)) - (o.shift(126) - o.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue vol-of-change (instability of comp burden momentum)
def f28sb_f28_sbc_dilution_overhang_promrev_volofchg_126d_base_v103_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = _std(p - p.shift(21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate slope acceleration: short-horizon slope minus long-horizon slope
def f28sb_f28_sbc_dilution_overhang_dilrate_slopeaccel_126d_base_v104_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    b = _slope(d, 63) - _slope(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash acceleration (2nd diff of mix, quarterly spans)
def f28sb_f28_sbc_dilution_overhang_papercash_accel_63d_base_v105_signal(sbcomp, ncfcommon):
    p = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 21)
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy slope acceleration: short-horizon slope minus long-horizon slope
def f28sb_f28_sbc_dilution_overhang_burnsub_slopeaccel_126d_base_v106_signal(sbcomp, ncfo):
    s = _mean(_sb_burn_subsidy(sbcomp, ncfo), 21)
    b = _slope(s, 63) - _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex slope over a quarter (short-horizon burden trajectory)
def f28sb_f28_sbc_dilution_overhang_promopex_slope_63d_base_v107_signal(sbcomp, opex):
    p = _mean(_sb_promote_opex(sbcomp, opex), 21)
    b = _slope(p, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang slope acceleration: short-horizon slope minus long-horizon slope
def f28sb_f28_sbc_dilution_overhang_overhang_slopeaccel_126d_base_v108_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 21)
    b = _slope(o, 63) - _slope(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue slope over a quarter
def f28sb_f28_sbc_dilution_overhang_promrev_slope_63d_base_v109_signal(sbcomp, revenue):
    p = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    b = _slope(p, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate slope over a quarter (short-horizon paper-cost trajectory)
def f28sb_f28_sbc_dilution_overhang_dilrate_slope_63d_base_v110_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    b = _slope(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regime / streak / distance facets v111-v130 ---

# longest above-median run for SBC dilution rate over the year (persistence of heavy dilution)
def f28sb_f28_sbc_dilution_overhang_dilrate_abovemed_run_252d_base_v111_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    above = (d >= d.rolling(252, min_periods=63).median()).astype(float)
    b = above.rolling(126, min_periods=42).sum() / 126.0 - above.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of dilution rate from its 252d max (headroom below peak dilution)
def f28sb_f28_sbc_dilution_overhang_dilrate_distmax_252d_base_v112_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    mx = d.rolling(252, min_periods=63).max()
    b = _safe_div(d - mx, mx.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency of peak overhang: fraction of the year since the 252d-max overhang occurred
def f28sb_f28_sbc_dilution_overhang_overhang_dsincemax_252d_base_v113_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = o.rolling(252, min_periods=63).apply(_dsh, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue regime: current level vs its 504d max (at-peak-burden distance)
def f28sb_f28_sbc_dilution_overhang_promrev_peakdist_504d_base_v114_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    mx = p.rolling(504, min_periods=126).max()
    b = _safe_div(p, mx)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# heavy-subsidy episode intensity: crossing count plus mean depth above prior-year median
def f28sb_f28_sbc_dilution_overhang_burnsub_episodes_252d_base_v115_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    med = s.rolling(504, min_periods=126).median()
    cross = ((s >= med) & (s.shift(1) < med)).astype(float)
    depth = (s - med).clip(lower=0)
    b = cross.rolling(252, min_periods=63).sum() + 5.0 * depth.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash position within its own 252d range (mix-position in range)
def f28sb_f28_sbc_dilution_overhang_papercash_rngpos_252d_base_v116_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    mn = p.rolling(252, min_periods=63).min()
    mx = p.rolling(252, min_periods=63).max()
    b = _safe_div(p - mn, mx - mn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate position within its own 252d range
def f28sb_f28_sbc_dilution_overhang_dilrate_rngpos_252d_base_v117_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    mn = d.rolling(252, min_periods=63).min()
    mx = d.rolling(252, min_periods=63).max()
    b = _safe_div(d - mn, mx - mn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang position within its own 504d range (long-horizon creep position)
def f28sb_f28_sbc_dilution_overhang_overhang_rngpos_504d_base_v118_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    mn = o.rolling(504, min_periods=126).min()
    mx = o.rolling(504, min_periods=126).max()
    b = _safe_div(o - mn, mx - mn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year promote-vs-opex rose quarter-on-quarter (rising-burden frequency)
def f28sb_f28_sbc_dilution_overhang_promopex_risefreq_252d_base_v119_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    rising = (p > p.shift(63)).astype(float)
    b = rising.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year overhang rose quarter-on-quarter (rising-creep frequency)
def f28sb_f28_sbc_dilution_overhang_overhang_risefreq_252d_base_v120_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    rising = (o > o.shift(63)).astype(float)
    b = rising.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy regime: fraction of year SBC subsidy exceeded half the cash burn
def f28sb_f28_sbc_dilution_overhang_burnsub_halfcover_252d_base_v121_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    thr = s.rolling(504, min_periods=126).quantile(0.4)
    b = (s >= thr).astype(float).rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate gap to its own 63d mean vs 252d mean (short-vs-long regime distance)
def f28sb_f28_sbc_dilution_overhang_dilrate_regimedist_63d_base_v122_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = _safe_div(_mean(d, 63) - _mean(d, 252), _std(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue regime distance (short vs long mean in dispersion units)
def f28sb_f28_sbc_dilution_overhang_promrev_regimedist_63d_base_v123_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = _safe_div(_mean(p, 63) - _mean(p, 252), _std(p, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang regime distance (short vs long mean in dispersion units)
def f28sb_f28_sbc_dilution_overhang_overhang_regimedist_63d_base_v124_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = _safe_div(_mean(o, 63) - _mean(o, 252), _std(o, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of quarters dilution rate set a new 252d high (escalating dilution episodes)
def f28sb_f28_sbc_dilution_overhang_dilrate_newhigh_252d_base_v125_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    is_high = (d >= d.rolling(252, min_periods=63).max() * 0.999).astype(float)
    b = is_high.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy distance from its 504d max (headroom below peak subsidy reliance)
def f28sb_f28_sbc_dilution_overhang_burnsub_peakdist_504d_base_v126_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    mx = s.rolling(504, min_periods=126).max()
    b = _safe_div(s, mx)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-dominant streak: persistence of net (sbcomp - |ncfcommon|) above its own 252d median
def f28sb_f28_sbc_dilution_overhang_papercash_netstreak_126d_base_v127_signal(sbcomp, ncfcommon):
    net = sbcomp - ncfcommon.abs()
    med = net.rolling(252, min_periods=63).median()
    sign = np.sign(net - med)
    b = sign.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang momentum normalized by typical change magnitude (standardized creep impulse)
def f28sb_f28_sbc_dilution_overhang_overhang_momz_126d_base_v128_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    chg = o - o.shift(63)
    typ = chg.abs().rolling(252, min_periods=63).mean()
    b = _safe_div(chg, typ)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex above-median signed depth in dispersion units
def f28sb_f28_sbc_dilution_overhang_promopex_meddepth_252d_base_v129_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    med = p.rolling(504, min_periods=126).median()
    b = _safe_div(p - med, p.rolling(252, min_periods=63).std())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate distributional skew over the year (asymmetry of paper-cost spikes)
def f28sb_f28_sbc_dilution_overhang_dilrate_skew_252d_base_v130_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = d.rolling(252, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- longer-horizon levels, yoy, and blended ratios v131-v150 ---

# SBC dilution rate smoothed over a half-year (persistent paper-cost level)
def f28sb_f28_sbc_dilution_overhang_dilrate_lvl_126d_base_v131_signal(sbcomp, marketcap):
    b = _mean(_sb_dilrate(sbcomp, marketcap), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue smoothed over a half-year
def f28sb_f28_sbc_dilution_overhang_promrev_lvl_126d_base_v132_signal(sbcomp, revenue):
    b = _mean(_sb_promote_rev(sbcomp, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy smoothed over a half-year (persistent cash-subsidy reliance)
def f28sb_f28_sbc_dilution_overhang_burnsub_lvl_126d_base_v133_signal(sbcomp, ncfo):
    b = _mean(_sb_burn_subsidy(sbcomp, ncfo), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang smoothed over a half-year (persistent latent-dilution level)
def f28sb_f28_sbc_dilution_overhang_overhang_lvl_126d_base_v134_signal(shareswadil, shareswa):
    b = _mean(_sb_overhang(shareswadil, shareswa), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex smoothed over a half-year
def f28sb_f28_sbc_dilution_overhang_promopex_lvl_126d_base_v135_signal(sbcomp, opex):
    b = _mean(_sb_promote_opex(sbcomp, opex), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution rate year-over-year ratio (multiplicative dilution growth)
def f28sb_f28_sbc_dilution_overhang_dilrate_yoyratio_252d_base_v136_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    b = _safe_div(d, d.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue year-over-year ratio
def f28sb_f28_sbc_dilution_overhang_promrev_yoyratio_252d_base_v137_signal(sbcomp, revenue):
    p = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    b = _safe_div(p, p.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang year-over-year ratio (multiplicative creep growth)
def f28sb_f28_sbc_dilution_overhang_overhang_yoyratio_252d_base_v138_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 21)
    b = _safe_div(o, o.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the revenue-vs-opex burden spread (where comp burden migrated)
def f28sb_f28_sbc_dilution_overhang_burdenspread_yoy_252d_base_v139_signal(sbcomp, revenue, opex):
    spread = _sb_promote_rev(sbcomp, revenue) - _sb_promote_opex(sbcomp, opex)
    b = spread - spread.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended dilution index: mean of dilution rate, promote-rev, and overhang (composite level)
def f28sb_f28_sbc_dilution_overhang_blended_index_63d_base_v140_signal(sbcomp, marketcap, revenue, shareswadil, shareswa):
    d = _sb_dilrate(sbcomp, marketcap)
    pr = _sb_promote_rev(sbcomp, revenue)
    o = _sb_overhang(shareswadil, shareswa)
    b = _mean((d + pr + o) / 3.0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy year-over-year change
def f28sb_f28_sbc_dilution_overhang_burnsub_yoy_252d_base_v141_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution-rate dispersion over a half-year (paper-cost instability)
def f28sb_f28_sbc_dilution_overhang_dilrate_dispersion_126d_base_v142_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = _std(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang coefficient of variation over a half-year (scale-free creep instability)
def f28sb_f28_sbc_dilution_overhang_overhang_cv_126d_base_v143_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = _std(o, 126) / _mean(o, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate vs overhang ratio level (paper cost per unit of latent dilution)
def f28sb_f28_sbc_dilution_overhang_dil_over_ratio_126d_base_v144_signal(sbcomp, marketcap, shareswadil, shareswa):
    d = _sb_dilrate(sbcomp, marketcap)
    o = _sb_overhang(shareswadil, shareswa)
    b = _mean(_safe_div(d, o), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex year-over-year change
def f28sb_f28_sbc_dilution_overhang_promopex_yoy_252d_base_v145_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    b = p - p.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash level smoothed over a half-year (persistent mix level)
def f28sb_f28_sbc_dilution_overhang_papercash_lvl_126d_base_v146_signal(sbcomp, ncfcommon):
    b = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC burden on revenue, two-year change (long-horizon paper-comp trend)
def f28sb_f28_sbc_dilution_overhang_promrev_2yrchg_504d_base_v147_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = p - p.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang two-year change (long-horizon latent-dilution build)
def f28sb_f28_sbc_dilution_overhang_overhang_2yrchg_504d_base_v148_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = o - o.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended dilution index year-over-year change (composite trend)
def f28sb_f28_sbc_dilution_overhang_blended_yoy_252d_base_v149_signal(sbcomp, marketcap, revenue, shareswadil, shareswa):
    d = _sb_dilrate(sbcomp, marketcap)
    pr = _sb_promote_rev(sbcomp, revenue)
    o = _sb_overhang(shareswadil, shareswa)
    idx = (d + pr + o) / 3.0
    b = idx - idx.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate as a fraction of total cash flows to capital providers
# sbcomp / (|ncfcommon| + |ncfo|) smoothed over a half-year (structural paper reliance)
def f28sb_f28_sbc_dilution_overhang_paper_reliance_126d_base_v150_signal(sbcomp, ncfcommon, ncfo):
    b = _mean(_safe_div(sbcomp, ncfcommon.abs() + ncfo.abs()), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sb_f28_sbc_dilution_overhang_burden_combined_63d_base_v076_signal,
    f28sb_f28_sbc_dilution_overhang_dil_x_overhang_63d_base_v077_signal,
    f28sb_f28_sbc_dilution_overhang_prom_spread_63d_base_v078_signal,
    f28sb_f28_sbc_dilution_overhang_cashsubsidy_63d_base_v079_signal,
    f28sb_f28_sbc_dilution_overhang_burn_x_dil_63d_base_v080_signal,
    f28sb_f28_sbc_dilution_overhang_sbc_vs_mcap_grow_126d_base_v081_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_per_dil_63d_base_v082_signal,
    f28sb_f28_sbc_dilution_overhang_net_dil_pressure_63d_base_v083_signal,
    f28sb_f28_sbc_dilution_overhang_sbc_blendbase_63d_base_v084_signal,
    f28sb_f28_sbc_dilution_overhang_cochannel_126d_base_v085_signal,
    f28sb_f28_sbc_dilution_overhang_compound_126d_base_v086_signal,
    f28sb_f28_sbc_dilution_overhang_sbc_vs_rev_grow_126d_base_v087_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_vs_burn_126d_base_v088_signal,
    f28sb_f28_sbc_dilution_overhang_dualz_126d_base_v089_signal,
    f28sb_f28_sbc_dilution_overhang_sbc_spendcover_63d_base_v090_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_slope_126d_base_v091_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_slope_126d_base_v092_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_voloflvl_126d_base_v093_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_volofchg_126d_base_v094_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_accel_126d_base_v095_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_jerklvl_63d_base_v096_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_slope_63d_base_v097_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_vol_126d_base_v098_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_volofvol_126d_base_v099_signal,
    f28sb_f28_sbc_dilution_overhang_prom_slopespr_126d_base_v100_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_slope_126d_base_v101_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_accel_126d_base_v102_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_volofchg_126d_base_v103_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_slopeaccel_126d_base_v104_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_accel_63d_base_v105_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_slopeaccel_126d_base_v106_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_slope_63d_base_v107_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_slopeaccel_126d_base_v108_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_slope_63d_base_v109_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_slope_63d_base_v110_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_abovemed_run_252d_base_v111_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_distmax_252d_base_v112_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_dsincemax_252d_base_v113_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_peakdist_504d_base_v114_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_episodes_252d_base_v115_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_rngpos_252d_base_v116_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_rngpos_252d_base_v117_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_rngpos_504d_base_v118_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_risefreq_252d_base_v119_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_risefreq_252d_base_v120_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_halfcover_252d_base_v121_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_regimedist_63d_base_v122_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_regimedist_63d_base_v123_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_regimedist_63d_base_v124_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_newhigh_252d_base_v125_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_peakdist_504d_base_v126_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_netstreak_126d_base_v127_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_momz_126d_base_v128_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_meddepth_252d_base_v129_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_skew_252d_base_v130_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_lvl_126d_base_v131_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_lvl_126d_base_v132_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_lvl_126d_base_v133_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_lvl_126d_base_v134_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_lvl_126d_base_v135_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_yoyratio_252d_base_v136_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_yoyratio_252d_base_v137_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_yoyratio_252d_base_v138_signal,
    f28sb_f28_sbc_dilution_overhang_burdenspread_yoy_252d_base_v139_signal,
    f28sb_f28_sbc_dilution_overhang_blended_index_63d_base_v140_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_yoy_252d_base_v141_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_dispersion_126d_base_v142_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_cv_126d_base_v143_signal,
    f28sb_f28_sbc_dilution_overhang_dil_over_ratio_126d_base_v144_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_yoy_252d_base_v145_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_lvl_126d_base_v146_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_2yrchg_504d_base_v147_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_2yrchg_504d_base_v148_signal,
    f28sb_f28_sbc_dilution_overhang_blended_yoy_252d_base_v149_signal,
    f28sb_f28_sbc_dilution_overhang_paper_reliance_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SBC_DILUTION_OVERHANG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    sbcomp = _fund(101, base=4e7, drift=0.03, vol=0.08).rename("sbcomp")
    opex = _fund(102, base=3e8, drift=0.025, vol=0.05).rename("opex")
    revenue = _fund(103, base=5e8, drift=0.03, vol=0.05).rename("revenue")
    marketcap = _fund(104, base=2e9, drift=0.02, vol=0.09).rename("marketcap")
    ncfcommon = _fund(105, base=3e7, drift=0.0, vol=0.10, allow_neg=True).rename("ncfcommon")
    shareswa = _fund(106, base=2e8, drift=0.01, vol=0.02).rename("shareswa")
    _dilfac = pd.Series(np.abs(np.random.default_rng(107).normal(0.05, 0.03, n)), name=None)
    shareswadil = (shareswa * (1.0 + _dilfac)).rename("shareswadil")
    ncfo = _fund(108, base=6e7, drift=0.02, vol=0.10, allow_neg=True).rename("ncfo")

    cols = {
        "sbcomp": sbcomp, "opex": opex, "revenue": revenue, "marketcap": marketcap,
        "ncfcommon": ncfcommon, "shareswa": shareswa, "shareswadil": shareswadil,
        "ncfo": ncfo, "closeadj": closeadj,
    }

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

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset of allowlist" % (name, meta["inputs"])
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

    print("OK f28_sbc_dilution_overhang_base_076_150_claude: %d features pass" % n_features)
