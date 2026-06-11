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
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (reinvestment dynamics) =====
def _f27_capex_rev(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f27_rnd_rev(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f27_sbc_rev(sbcomp, revenue):
    return sbcomp / revenue.replace(0, np.nan)


def _f27_reinv_rate(capex, rnd, revenue):
    return (capex + rnd) / revenue.replace(0, np.nan)


def _f27_growth_capex(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f27_rnd_assets(rnd, assets):
    return rnd / assets.replace(0, np.nan)


def _f27_capex_assets(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f27_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ============================================================
# capex/revenue smoothed over a half-year (faster intensity read)
def f27ri_f27_reinvestment_dynamics_capexrev_126d_base_v076_signal(capex, revenue):
    b = _mean(_f27_capex_rev(capex, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity smoothed over a half-year
def f27ri_f27_reinvestment_dynamics_rndrev_126d_base_v077_signal(rnd, revenue):
    b = _mean(_f27_rnd_rev(rnd, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate half-year minus full-year level (short vs long intensity gap)
def f27ri_f27_reinvestment_dynamics_reinvgap_126v252_base_v078_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    b = _mean(rr, 126) - _mean(rr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue half-year minus full-year (capex intensity acceleration vs base)
def f27ri_f27_reinvestment_dynamics_capexgap_126v252_base_v079_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    b = _mean(ci, 126) - _mean(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity half-year minus full-year
def f27ri_f27_reinvestment_dynamics_rndgap_126v252_base_v080_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    b = _mean(ri, 126) - _mean(ri, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex 63d log growth (short-horizon spend ramp)
def f27ri_f27_reinvestment_dynamics_capexgrow_63d_base_v081_signal(capex):
    b = _f27_growth(capex, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D 63d log growth
def f27ri_f27_reinvestment_dynamics_rndgrow_63d_base_v082_signal(rnd):
    b = _f27_growth(rnd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC 126d log growth (comp ramp)
def f27ri_f27_reinvestment_dynamics_sbcgrow_126d_base_v083_signal(sbcomp):
    b = _f27_growth(sbcomp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet 504d log growth (long capital-base build)
def f27ri_f27_reinvestment_dynamics_ppnegrow_504d_base_v084_signal(ppnenet):
    b = _f27_growth(ppnenet, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth minus ppnenet growth (capex outpacing the installed base)
def f27ri_f27_reinvestment_dynamics_capexvsppne_252d_base_v085_signal(capex, ppnenet):
    b = _f27_growth(capex, 252) - _f27_growth(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth minus capex growth (research outpacing physical investment)
def f27ri_f27_reinvestment_dynamics_rndvscapexgrow_252d_base_v086_signal(rnd, capex):
    b = _f27_growth(rnd, 252) - _f27_growth(capex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth minus R&D growth (comp inflation vs research)
def f27ri_f27_reinvestment_dynamics_sbcvsrndgrow_252d_base_v087_signal(sbcomp, rnd):
    b = _f27_growth(sbcomp, 252) - _f27_growth(rnd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue dispersion over 126d (short-horizon investment stability)
def f27ri_f27_reinvestment_dynamics_capexrevdisp_126d_base_v088_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    b = _std(ci, 126) / _mean(ci, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth dispersion (volatility of R&D growth path over 252d)
def f27ri_f27_reinvestment_dynamics_rndgrowdisp_252d_base_v089_signal(rnd):
    g = rnd.pct_change(21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth dispersion
def f27ri_f27_reinvestment_dynamics_capexgrowdisp_252d_base_v090_signal(capex):
    g = capex.pct_change(21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate EMA displacement (rate vs its slow EMA)
def f27ri_f27_reinvestment_dynamics_reinvratedisp_ema_base_v091_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    b = rr - rr.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex EMA displacement
def f27ri_f27_reinvestment_dynamics_growthcapexdisp_ema_base_v092_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    b = gc - gc.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity EMA displacement
def f27ri_f27_reinvestment_dynamics_sbcrevdisp_ema_base_v093_signal(sbcomp, revenue):
    si = _f27_sbc_rev(sbcomp, revenue)
    b = si - si.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue 126d slope scaled by level (short reinvestment trend)
def f27ri_f27_reinvestment_dynamics_capexrevslope_126d_base_v094_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    sl = _slope(ci, 126)
    b = sl / _mean(ci, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/assets 126d slope scaled by level
def f27ri_f27_reinvestment_dynamics_rndassetsslope_126d_base_v095_signal(rnd, assets):
    ra = _f27_rnd_assets(rnd, assets)
    sl = _slope(ra, 126)
    b = sl / _mean(ra, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets 252d slope scaled by level (long capital-intensity trend)
def f27ri_f27_reinvestment_dynamics_capexassetsslope_252d_base_v096_signal(capex, assets):
    ca = _f27_capex_assets(capex, assets)
    sl = _slope(ca, 252)
    b = sl / _mean(ca, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/revenue 252d slope scaled by level (comp-intensity trend)
def f27ri_f27_reinvestment_dynamics_sbcrevslope_252d_base_v097_signal(sbcomp, revenue):
    si = _f27_sbc_rev(sbcomp, revenue)
    sl = _slope(si, 252)
    b = sl / _mean(si, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate convexity: distance from its 252d range midpoint
def f27ri_f27_reinvestment_dynamics_reinvratemid_252d_base_v098_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    hi = rr.rolling(252, min_periods=126).max()
    lo = rr.rolling(252, min_periods=126).min()
    mid = (hi + lo) / 2.0
    b = (rr - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity range position (where R&D/rev sits in its 252d range)
def f27ri_f27_reinvestment_dynamics_rndrevrng_252d_base_v099_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    hi = ri.rolling(252, min_periods=126).max()
    lo = ri.rolling(252, min_periods=126).min()
    b = (ri - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex range position
def f27ri_f27_reinvestment_dynamics_growthcapexrng_252d_base_v100_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    hi = gc.rolling(252, min_periods=126).max()
    lo = gc.rolling(252, min_periods=126).min()
    b = (gc - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate signed-sqrt momentum over a half-year
def f27ri_f27_reinvestment_dynamics_reinvsqrtmom_126d_base_v101_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    chg = rr - rr.shift(126)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity tanh-squashed quarterly change (bounded ramp signal)
def f27ri_f27_reinvestment_dynamics_capextanh_63d_base_v102_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    chg = ci - ci.shift(63)
    b = np.tanh(chg / _std(ci, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity tanh-squashed quarterly change
def f27ri_f27_reinvestment_dynamics_rndtanh_63d_base_v103_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    chg = ri - ri.shift(63)
    b = np.tanh(chg / _std(ri, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity vs ppnenet: (capex+rnd)/ppnenet level (build vs installed base)
def f27ri_f27_reinvestment_dynamics_reinvppne_252d_base_v104_signal(capex, rnd, ppnenet):
    rp = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = _mean(rp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (capex+rnd)/ppnenet z-scored vs own history
def f27ri_f27_reinvestment_dynamics_reinvppnez_504d_base_v105_signal(capex, rnd, ppnenet):
    rp = (capex + rnd) / ppnenet.replace(0, np.nan)
    b = _z(rp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/ppnenet level (intangible-build vs physical base)
def f27ri_f27_reinvestment_dynamics_rndppne_252d_base_v106_signal(rnd, ppnenet):
    b = _mean(rnd / ppnenet.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/ppnenet year-over-year change (comp scaling vs physical base drift)
def f27ri_f27_reinvestment_dynamics_sbcppne_252d_base_v107_signal(sbcomp, ppnenet):
    sp = sbcomp / ppnenet.replace(0, np.nan)
    b = sp - sp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/ppnenet (fixed-asset turnover) interacted with capex intensity (efficient builder)
def f27ri_f27_reinvestment_dynamics_buildeff_252d_base_v108_signal(revenue, ppnenet, capex):
    fat = _mean(revenue / ppnenet.replace(0, np.nan), 252)
    ci = _mean(_f27_capex_rev(capex, revenue), 252)
    b = fat * ci
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue minus SBC/revenue (cash-capex vs equity-comp tilt)
def f27ri_f27_reinvestment_dynamics_capexsbctilt_252d_base_v109_signal(capex, sbcomp, revenue):
    tilt = _f27_capex_rev(capex, revenue) - _f27_sbc_rev(sbcomp, revenue)
    b = _mean(tilt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/revenue minus SBC/revenue (research vs comp tilt)
def f27ri_f27_reinvestment_dynamics_rndsbctilt_252d_base_v110_signal(rnd, sbcomp, revenue):
    tilt = _f27_rnd_rev(rnd, revenue) - _f27_sbc_rev(sbcomp, revenue)
    b = _mean(tilt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate year-over-year second difference (changing direction)
def f27ri_f27_reinvestment_dynamics_reinvyoy2_252d_base_v111_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    d1 = rr - rr.shift(252)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity year-over-year second difference
def f27ri_f27_reinvestment_dynamics_rndyoy2_252d_base_v112_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    d1 = ri - ri.shift(252)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex year-over-year second difference
def f27ri_f27_reinvestment_dynamics_growthcapexyoy2_252d_base_v113_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    d1 = gc - gc.shift(252)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-mix (rnd share) range position
def f27ri_f27_reinvestment_dynamics_rndmixrng_252d_base_v114_signal(capex, rnd):
    mix = rnd / (capex + rnd).replace(0, np.nan)
    hi = mix.rolling(252, min_periods=126).max()
    lo = mix.rolling(252, min_periods=126).min()
    b = (mix - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage dispersion: volatility of revenue/capex over 252d (build-funding stability)
def f27ri_f27_reinvestment_dynamics_capexcovertrend_126d_base_v115_signal(revenue, capex):
    cover = revenue / capex.replace(0, np.nan)
    b = _std(cover, 252) / _mean(cover, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D coverage: revenue/rnd z-scored (research leverage on sales)
def f27ri_f27_reinvestment_dynamics_rndcoverz_252d_base_v116_signal(revenue, rnd):
    cover = revenue / rnd.replace(0, np.nan)
    b = _z(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC coverage: revenue/sbcomp ranked (comp leverage percentile)
def f27ri_f27_reinvestment_dynamics_sbccoverrank_252d_base_v117_signal(revenue, sbcomp):
    cover = revenue / sbcomp.replace(0, np.nan)
    b = _rank(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment per asset interacted with revenue growth (productive reinvestment)
def f27ri_f27_reinvestment_dynamics_prodreinv_252d_base_v118_signal(capex, rnd, assets, revenue):
    ra = _mean((capex + rnd) / assets.replace(0, np.nan), 252)
    g = _f27_growth(revenue, 252)
    b = ra * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity asymmetry: upside dispersion vs downside dispersion of capex/rev
def f27ri_f27_reinvestment_dynamics_capexasym_252d_base_v119_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    chg = ci.diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity asymmetry
def f27ri_f27_reinvestment_dynamics_rndasym_252d_base_v120_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    chg = ri.diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reinvestment intensity 126d slope scaled by level
def f27ri_f27_reinvestment_dynamics_totinvslope_126d_base_v121_signal(capex, rnd, sbcomp, revenue):
    tot = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    sl = _slope(tot, 126)
    b = sl / _mean(tot, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets z-scored vs own history
def f27ri_f27_reinvestment_dynamics_capexassetsz_504d_base_v122_signal(capex, assets):
    b = _z(_f27_capex_assets(capex, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/assets percentile-ranked vs own 252d history
def f27ri_f27_reinvestment_dynamics_rndassetsrank_252d_base_v123_signal(rnd, assets):
    b = _rank(_f27_rnd_assets(rnd, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex per unit of revenue growth (capex needed per point of growth)
def f27ri_f27_reinvestment_dynamics_capexpergrowth_252d_base_v124_signal(capex, ppnenet, revenue):
    gc = _mean(_f27_growth_capex(capex, ppnenet), 252)
    g = _f27_growth(revenue, 252)
    b = gc / g.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate stability over a half-year (level / dispersion)
def f27ri_f27_reinvestment_dynamics_reinvstab_126d_base_v125_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    b = _mean(rr, 126) / _std(rr, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity quarterly hit-rate vs prior week (high-freq ramp persistence)
def f27ri_f27_reinvestment_dynamics_capexhit_63d_base_v126_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    up = (ci > ci.shift(5)).astype(float)
    b = up.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth EMA (persistent research-spend momentum)
def f27ri_f27_reinvestment_dynamics_rndgrowema_252d_base_v127_signal(rnd):
    g = _f27_growth(rnd, 126)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth EMA
def f27ri_f27_reinvestment_dynamics_capexgrowema_252d_base_v128_signal(capex):
    g = _f27_growth(capex, 126)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment composition entropy proxy: dispersion of the three intensity shares
def f27ri_f27_reinvestment_dynamics_mixdisp_252d_base_v129_signal(capex, rnd, sbcomp):
    tot = (capex + rnd + sbcomp).replace(0, np.nan)
    s1 = capex / tot
    s2 = rnd / tot
    s3 = sbcomp / tot
    shares = pd.concat([s1, s2, s3], axis=1)
    b = _mean(shares.std(axis=1), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex share of total reinvestment, year-over-year change
def f27ri_f27_reinvestment_dynamics_capexshare_252d_base_v130_signal(capex, rnd, sbcomp):
    sh = capex / (capex + rnd + sbcomp).replace(0, np.nan)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC share of total reinvestment, z-scored
def f27ri_f27_reinvestment_dynamics_sbcsharez_504d_base_v131_signal(capex, rnd, sbcomp):
    sh = sbcomp / (capex + rnd + sbcomp).replace(0, np.nan)
    b = _z(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate quarterly slope minus annual slope (trend curvature)
def f27ri_f27_reinvestment_dynamics_reinvcurv_base_v132_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    short = _slope(rr, 63) / _mean(rr, 63).abs().replace(0, np.nan)
    long = _slope(rr, 252) / _mean(rr, 252).abs().replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity quarterly slope minus annual slope (research-budget curvature)
def f27ri_f27_reinvestment_dynamics_capexcurv_base_v133_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    short = _slope(ri, 63) / _mean(ri, 63).abs().replace(0, np.nan)
    long = _slope(ri, 252) / _mean(ri, 252).abs().replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per unit of installed-base growth, scaled by capex intensity (build productivity)
def f27ri_f27_reinvestment_dynamics_buildprod_252d_base_v134_signal(revenue, ppnenet, capex):
    rev_g = _f27_growth(revenue, 252)
    ppne_g = _f27_growth(ppnenet, 252)
    ci = _mean(_f27_capex_rev(capex, revenue), 252)
    b = (rev_g - ppne_g) * ci
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity smoothed minus its 252d-lagged self (slow regime change)
def f27ri_f27_reinvestment_dynamics_rndregime_252d_base_v135_signal(rnd, revenue):
    ri = _mean(_f27_rnd_rev(rnd, revenue), 63)
    b = ri - ri.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet rank vs own 504d history
def f27ri_f27_reinvestment_dynamics_growthcapexrank_504d_base_v136_signal(capex, ppnenet):
    b = _rank(_f27_growth_capex(capex, ppnenet), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate vs assets composite: reinvest rate times (1 - capex/assets) (sales-light build)
def f27ri_f27_reinvestment_dynamics_reinvlight_252d_base_v137_signal(capex, rnd, revenue, assets):
    rr = _mean(_f27_reinv_rate(capex, rnd, revenue), 252)
    ca = _mean(_f27_capex_assets(capex, assets), 252)
    b = rr * (1.0 - ca)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity drawdown from its 252d peak (research-budget pullback depth)
def f27ri_f27_reinvestment_dynamics_rndconvex_252d_base_v138_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    peak = ri.rolling(252, min_periods=126).max()
    b = ri / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth minus revenue growth, smoothed (persistent dilution-vs-sales)
def f27ri_f27_reinvestment_dynamics_sbcdilutetrend_252d_base_v139_signal(sbcomp, revenue):
    spread = _f27_growth(sbcomp, 126) - _f27_growth(revenue, 126)
    b = spread.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration relative to its own dispersion (standardized capex jolt)
def f27ri_f27_reinvestment_dynamics_capexjolt_252d_base_v140_signal(capex):
    g = capex.pct_change(63)
    b = (g - _mean(g, 252)) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D acceleration relative to its own dispersion (standardized R&D jolt)
def f27ri_f27_reinvestment_dynamics_rndjolt_252d_base_v141_signal(rnd):
    g = rnd.pct_change(63)
    b = (g - _mean(g, 252)) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity vs assets, half-year slope scaled by level
def f27ri_f27_reinvestment_dynamics_reinvassetsslope_126d_base_v142_signal(capex, rnd, assets):
    ra = (capex + rnd) / assets.replace(0, np.nan)
    sl = _slope(ra, 126)
    b = sl / _mean(ra, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vs R&D intensity correlation-of-direction (co-movement of the two budgets)
def f27ri_f27_reinvestment_dynamics_budgetcomove_252d_base_v143_signal(capex, rnd, revenue):
    ci = _f27_capex_rev(capex, revenue).diff()
    ri = _f27_rnd_rev(rnd, revenue).diff()
    same = np.sign(ci) * np.sign(ri)
    b = same.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reinvestment / ppnenet z-scored vs own 504d history (full build vs installed base)
def f27ri_f27_reinvestment_dynamics_totinvppne_252d_base_v144_signal(capex, rnd, sbcomp, ppnenet):
    tot = (capex + rnd + sbcomp) / ppnenet.replace(0, np.nan)
    b = _z(tot, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate momentum minus revenue-growth momentum (intensity vs growth divergence)
def f27ri_f27_reinvestment_dynamics_reinvvsgrowmom_252d_base_v145_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    rr_mom = rr - rr.shift(126)
    g = _f27_growth(revenue, 126)
    g_mom = g - g.shift(126)
    b = rr_mom - g_mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity log-level (compresses scale, level read of physical reinvestment)
def f27ri_f27_reinvestment_dynamics_capexlog_252d_base_v146_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    b = np.log(_mean(ci, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-to-capex ratio z-scored (research-vs-physical posture, standardized)
def f27ri_f27_reinvestment_dynamics_rndcapexz_504d_base_v147_signal(rnd, capex):
    ratio = rnd / capex.replace(0, np.nan)
    b = _z(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity quarterly change relative to dispersion (standardized comp jolt)
def f27ri_f27_reinvestment_dynamics_sbcjolt_252d_base_v148_signal(sbcomp, revenue):
    si = _f27_sbc_rev(sbcomp, revenue)
    chg = si - si.shift(63)
    b = chg / _std(si, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate breadth: fraction of last year above its 252d median
def f27ri_f27_reinvestment_dynamics_reinvbreadth_252d_base_v149_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    med = rr.rolling(252, min_periods=126).median()
    above = (rr > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# research-overlaid build momentum: change in growth-capex weighted by R&D intensity
def f27ri_f27_reinvestment_dynamics_buildoverlay_252d_base_v150_signal(capex, ppnenet, rnd, revenue):
    gc = _f27_growth_capex(capex, ppnenet)
    gc_mom = gc - gc.shift(126)
    ri = _mean(_f27_rnd_rev(rnd, revenue), 252)
    b = gc_mom * (1.0 + ri)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ri_f27_reinvestment_dynamics_capexrev_126d_base_v076_signal,
    f27ri_f27_reinvestment_dynamics_rndrev_126d_base_v077_signal,
    f27ri_f27_reinvestment_dynamics_reinvgap_126v252_base_v078_signal,
    f27ri_f27_reinvestment_dynamics_capexgap_126v252_base_v079_signal,
    f27ri_f27_reinvestment_dynamics_rndgap_126v252_base_v080_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow_63d_base_v081_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow_63d_base_v082_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow_126d_base_v083_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrow_504d_base_v084_signal,
    f27ri_f27_reinvestment_dynamics_capexvsppne_252d_base_v085_signal,
    f27ri_f27_reinvestment_dynamics_rndvscapexgrow_252d_base_v086_signal,
    f27ri_f27_reinvestment_dynamics_sbcvsrndgrow_252d_base_v087_signal,
    f27ri_f27_reinvestment_dynamics_capexrevdisp_126d_base_v088_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowdisp_252d_base_v089_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowdisp_252d_base_v090_signal,
    f27ri_f27_reinvestment_dynamics_reinvratedisp_ema_base_v091_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexdisp_ema_base_v092_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevdisp_ema_base_v093_signal,
    f27ri_f27_reinvestment_dynamics_capexrevslope_126d_base_v094_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsslope_126d_base_v095_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsslope_252d_base_v096_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevslope_252d_base_v097_signal,
    f27ri_f27_reinvestment_dynamics_reinvratemid_252d_base_v098_signal,
    f27ri_f27_reinvestment_dynamics_rndrevrng_252d_base_v099_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexrng_252d_base_v100_signal,
    f27ri_f27_reinvestment_dynamics_reinvsqrtmom_126d_base_v101_signal,
    f27ri_f27_reinvestment_dynamics_capextanh_63d_base_v102_signal,
    f27ri_f27_reinvestment_dynamics_rndtanh_63d_base_v103_signal,
    f27ri_f27_reinvestment_dynamics_reinvppne_252d_base_v104_signal,
    f27ri_f27_reinvestment_dynamics_reinvppnez_504d_base_v105_signal,
    f27ri_f27_reinvestment_dynamics_rndppne_252d_base_v106_signal,
    f27ri_f27_reinvestment_dynamics_sbcppne_252d_base_v107_signal,
    f27ri_f27_reinvestment_dynamics_buildeff_252d_base_v108_signal,
    f27ri_f27_reinvestment_dynamics_capexsbctilt_252d_base_v109_signal,
    f27ri_f27_reinvestment_dynamics_rndsbctilt_252d_base_v110_signal,
    f27ri_f27_reinvestment_dynamics_reinvyoy2_252d_base_v111_signal,
    f27ri_f27_reinvestment_dynamics_rndyoy2_252d_base_v112_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexyoy2_252d_base_v113_signal,
    f27ri_f27_reinvestment_dynamics_rndmixrng_252d_base_v114_signal,
    f27ri_f27_reinvestment_dynamics_capexcovertrend_126d_base_v115_signal,
    f27ri_f27_reinvestment_dynamics_rndcoverz_252d_base_v116_signal,
    f27ri_f27_reinvestment_dynamics_sbccoverrank_252d_base_v117_signal,
    f27ri_f27_reinvestment_dynamics_prodreinv_252d_base_v118_signal,
    f27ri_f27_reinvestment_dynamics_capexasym_252d_base_v119_signal,
    f27ri_f27_reinvestment_dynamics_rndasym_252d_base_v120_signal,
    f27ri_f27_reinvestment_dynamics_totinvslope_126d_base_v121_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsz_504d_base_v122_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsrank_252d_base_v123_signal,
    f27ri_f27_reinvestment_dynamics_capexpergrowth_252d_base_v124_signal,
    f27ri_f27_reinvestment_dynamics_reinvstab_126d_base_v125_signal,
    f27ri_f27_reinvestment_dynamics_capexhit_63d_base_v126_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowema_252d_base_v127_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowema_252d_base_v128_signal,
    f27ri_f27_reinvestment_dynamics_mixdisp_252d_base_v129_signal,
    f27ri_f27_reinvestment_dynamics_capexshare_252d_base_v130_signal,
    f27ri_f27_reinvestment_dynamics_sbcsharez_504d_base_v131_signal,
    f27ri_f27_reinvestment_dynamics_reinvcurv_base_v132_signal,
    f27ri_f27_reinvestment_dynamics_capexcurv_base_v133_signal,
    f27ri_f27_reinvestment_dynamics_buildprod_252d_base_v134_signal,
    f27ri_f27_reinvestment_dynamics_rndregime_252d_base_v135_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexrank_504d_base_v136_signal,
    f27ri_f27_reinvestment_dynamics_reinvlight_252d_base_v137_signal,
    f27ri_f27_reinvestment_dynamics_rndconvex_252d_base_v138_signal,
    f27ri_f27_reinvestment_dynamics_sbcdilutetrend_252d_base_v139_signal,
    f27ri_f27_reinvestment_dynamics_capexjolt_252d_base_v140_signal,
    f27ri_f27_reinvestment_dynamics_rndjolt_252d_base_v141_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsslope_126d_base_v142_signal,
    f27ri_f27_reinvestment_dynamics_budgetcomove_252d_base_v143_signal,
    f27ri_f27_reinvestment_dynamics_totinvppne_252d_base_v144_signal,
    f27ri_f27_reinvestment_dynamics_reinvvsgrowmom_252d_base_v145_signal,
    f27ri_f27_reinvestment_dynamics_capexlog_252d_base_v146_signal,
    f27ri_f27_reinvestment_dynamics_rndcapexz_504d_base_v147_signal,
    f27ri_f27_reinvestment_dynamics_sbcjolt_252d_base_v148_signal,
    f27ri_f27_reinvestment_dynamics_reinvbreadth_252d_base_v149_signal,
    f27ri_f27_reinvestment_dynamics_buildoverlay_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REINVESTMENT_DYNAMICS_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    capex = _fund(102, base=8e7, drift=0.025, vol=0.06).rename("capex")
    rnd = _fund(103, base=6e7, drift=0.035, vol=0.07).rename("rnd")
    sbcomp = _fund(104, base=3e7, drift=0.04, vol=0.08).rename("sbcomp")
    assets = _fund(105, base=2e9, drift=0.02, vol=0.03).rename("assets")
    ppnenet = _fund(106, base=5e8, drift=0.02, vol=0.05).rename("ppnenet")

    cols = {"revenue": revenue, "capex": capex, "rnd": rnd,
            "sbcomp": sbcomp, "assets": assets, "ppnenet": ppnenet}

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

    print("OK f27_reinvestment_dynamics_base_076_150_claude: %d features pass" % n_features)
