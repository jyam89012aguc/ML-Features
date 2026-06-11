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


def _chg(s, w):
    return s - s.shift(w)


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s on time index over window w
    idx = np.arange(w)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        ym = a.mean()
        return ((idx - xm) * (a - ym)).sum() / xden

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (quality-compounder economics) =====
def _f33_roic_level(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f33_fcf_roic(fcf, equity, w):
    r = fcf / equity.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_reinvest_rate(fcf, netinc, w):
    payout = fcf / netinc.replace(0, np.nan)
    reinv = 1.0 - payout
    return reinv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_dilution(sharesbas, w):
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f33_revgrowth(revenue, w):
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


def _f33_fcf_margin(fcf, revenue, w):
    r = fcf / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_capital_turnover(revenue, equity, w):
    t = revenue / equity.replace(0, np.nan)
    return t.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- 126d-horizon high-stable-ROIC x dilution composites ---

# 126d ROIC level minus 126d dilution, ranked (faster quality-minus-dilution)
def f33qc_f33_quality_compounder_qmd126_126d_base_v076_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 126)
    b = _rank(r - d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC slope (improving returns) x anti-dilution (improving + clean cap structure)
def f33qc_f33_quality_compounder_roicslopebb_252d_base_v077_signal(roic, sharesbas):
    sl = _slope(_f33_roic_level(roic, 63), 252)
    bb = -_f33_dilution(sharesbas, 252)
    b = sl * (1.0 + bb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC dispersion (instability) penalized by dilution (low-quality compounder, signed neg)
def f33qc_f33_quality_compounder_instabdil_252d_base_v078_signal(roic, sharesbas):
    disp = _std(roic, 252)
    d = _f33_dilution(sharesbas, 252)
    b = -(disp * (1.0 + d.clip(-0.5, 1.0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z-score interacted with dilution z-score (cross-economics interaction)
def f33qc_f33_quality_compounder_roicdilx_252d_base_v079_signal(roic, sharesbas):
    rz = _z(_f33_roic_level(roic, 126), 504)
    dz = _z(_f33_dilution(sharesbas, 126), 504)
    b = rz * dz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count efficiency: ROIC level per unit of share-count growth (de-trended)
def f33qc_f33_quality_compounder_roicpersg_504d_base_v080_signal(roic, sharesbas):
    sg = sharesbas / sharesbas.shift(504).replace(0, np.nan)
    eff = _f33_roic_level(roic, 252) / sg.replace(0, np.nan)
    b = _z(eff, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-return (FCF-ROIC) variants ---

# 126d FCF-ROIC slope x reinvestment (accelerating cash returns reinvested)
def f33qc_f33_quality_compounder_cashslopereinv_252d_base_v081_signal(fcf, equity, netinc):
    sl = _slope(_f33_fcf_roic(fcf, equity, 63), 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = sl * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-on-revenue x FCF-on-equity geometric blend (two cash-return views)
def f33qc_f33_quality_compounder_cashblend_252d_base_v082_signal(fcf, revenue, equity):
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    b = (fm + cash) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-return acceleration gated by buyback (improving cash returns + shrinking base)
def f33qc_f33_quality_compounder_cashaccelbb_504d_base_v083_signal(fcf, equity, sharesbas):
    cash = _f33_fcf_roic(fcf, equity, 126)
    accel = (cash - cash.shift(126)) - (cash.shift(126) - cash.shift(252))
    bb = -_f33_dilution(sharesbas, 252)
    b = accel * (1.0 + bb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC stability x reinvestment (steady cash returns reinvested)
def f33qc_f33_quality_compounder_cashstabreinv_252d_base_v084_signal(fcf, equity, netinc):
    cash = fcf / equity.replace(0, np.nan)
    stab = cash.rolling(252, min_periods=126).mean() / cash.rolling(252, min_periods=126).std().replace(0, np.nan)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = np.tanh(stab / 5.0) * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash return minus accounting return, momentum (improving earnings quality of returns)
def f33qc_f33_quality_compounder_cashconvmom_504d_base_v085_signal(roic, fcf, equity):
    cash = _f33_fcf_roic(fcf, equity, 252)
    acct = _f33_roic_level(roic, 252)
    spread = cash - acct
    b = spread - spread.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- reinvestment-at-high-returns variants ---

# reinvestment rate x ROIC slope (reinvesting INTO improving returns)
def f33qc_f33_quality_compounder_reinvslope_252d_base_v086_signal(roic, fcf, netinc):
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    sl = _slope(_f33_roic_level(roic, 63), 252)
    b = reinv * np.tanh(20.0 * sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounding velocity: change in (ROIC x reinvest) over a half-year
def f33qc_f33_quality_compounder_compvel_252d_base_v087_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    reinv = _f33_reinvest_rate(fcf, netinc, 126)
    comp = r * reinv
    b = comp - comp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment x revenue-growth interaction de-trended (reinvestment turning into sales)
def f33qc_f33_quality_compounder_reinvrevx_504d_base_v088_signal(fcf, netinc, revenue):
    reinv = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    g = _z(_f33_revgrowth(revenue, 504), 504)
    b = reinv * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x equity-growth (capital base compounding at high returns), rank-space interaction
def f33qc_f33_quality_compounder_roiceqgrow_504d_base_v089_signal(roic, equity):
    rr = _rank(_f33_roic_level(roic, 252), 504)
    er = _rank(_f33_revgrowth(equity, 252), 504)
    b = (rr + 0.5) * (er + 0.5) - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-return reinvestment above hurdle, ranked (value-creating reinvestment percentile)
def f33qc_f33_quality_compounder_hurdlerank_252d_base_v090_signal(roic, fcf, netinc):
    excess = (_f33_roic_level(roic, 252) - 0.08)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = _rank(excess * reinv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF-margin / profitability x return ---

# FCF margin slope x ROIC level (improving cash conversion at high returns)
def f33qc_f33_quality_compounder_fmslroic_252d_base_v091_signal(fcf, revenue, roic):
    sl = _slope(_f33_fcf_margin(fcf, revenue, 63), 252)
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = sl * np.sqrt(r.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin x ROIC rank-space interaction (profitability quality percentile)
def f33qc_f33_quality_compounder_nmroicrank_252d_base_v092_signal(netinc, revenue, roic):
    nm = _rank((netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean(), 504)
    rr = _rank(_f33_roic_level(roic, 252), 504)
    b = (nm + 0.5) * (rr + 0.5) - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin minus net margin (cash quality) interacted with anti-dilution, de-trended
def f33qc_f33_quality_compounder_cashqualdil_252d_base_v093_signal(fcf, netinc, revenue, sharesbas):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    cq = _z(fm - nm, 504)
    bb = _z(-_f33_dilution(sharesbas, 252), 504)
    b = cq * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin x return composite ranked vs both (blended profitability-quality percentile)
def f33qc_f33_quality_compounder_marginretrank_504d_base_v094_signal(fcf, revenue, roic):
    fm = _rank(_f33_fcf_margin(fcf, revenue, 252), 504)
    rr = _rank(_f33_roic_level(roic, 252), 504)
    b = fm + rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- capital efficiency x return / per-share compounding ---

# capital turnover slope x ROIC (improving efficiency at high returns)
def f33qc_f33_quality_compounder_turnsloperoic_252d_base_v095_signal(revenue, equity, roic):
    sl = _slope(_f33_capital_turnover(revenue, equity, 63), 252)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = sl * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share level growth x FCF-ROIC (per-share top-line + cash returns)
def f33qc_f33_quality_compounder_revpscash_504d_base_v096_signal(revenue, sharesbas, fcf, equity):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 252)
    b = g * cash
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share growth x ROIC stability (durable per-share cash compounding)
def f33qc_f33_quality_compounder_fcfpsdurable_504d_base_v097_signal(fcf, sharesbas, roic):
    fps = fcf / sharesbas.replace(0, np.nan)
    g = _z(fps / fps.shift(504).replace(0, np.nan) - 1.0, 252)
    stab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    b = g * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-per-share growth ranked minus dilution rank (per-share earnings vs issuance)
def f33qc_f33_quality_compounder_epspsbb_252d_base_v098_signal(netinc, sharesbas):
    eps = netinc / sharesbas.replace(0, np.nan)
    g = _rank(eps / eps.shift(252).replace(0, np.nan) - 1.0, 504)
    dr = _rank(_f33_dilution(sharesbas, 252), 504)
    b = g - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- durable / multi-horizon composites ---

# 5-year durable compounder: ROIC stability x revenue CAGR x anti-dilution
def f33qc_f33_quality_compounder_dur5y_1260d_base_v099_signal(roic, revenue, sharesbas):
    stab = np.tanh(_f33_roic_stability(roic, 504) / 5.0)
    cagr = (revenue / revenue.shift(1260).replace(0, np.nan)) ** (1.0 / 5.0) - 1.0
    bb = (1.0 - _f33_dilution(sharesbas, 1260).clip(-0.5, 1.5))
    b = stab * cagr.clip(-0.5, 1.0) * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC premium vs long baseline x reinvestment (improving compounder)
def f33qc_f33_quality_compounder_roicpremreinv_756d_base_v100_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    base = _f33_roic_level(roic, 756)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = (r - base) * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF-ROIC x revenue growth interaction de-trended (durable cash growth)
def f33qc_f33_quality_compounder_durcashgrow_504d_base_v101_signal(fcf, equity, revenue):
    cash = _z(_f33_fcf_roic(fcf, equity, 504), 252)
    g = _z(_f33_revgrowth(revenue, 504), 252)
    b = cash * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon dilution consistency x ROIC level (consistent buyback at high returns)
def f33qc_f33_quality_compounder_dilconsistroic_504d_base_v102_signal(sharesbas, roic):
    d252 = _f33_dilution(sharesbas, 252)
    d504 = _f33_dilution(sharesbas, 504)
    bothbb = ((d252 < 0) & (d504 < 0)).astype(float)
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = bothbb * np.sqrt(r.abs() + 0.01) - 0.5 * (d252 + d504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 3-year per-share equity compounding minus dilution, ROIC-stability weighted (durable BVPS)
def f33qc_f33_quality_compounder_bvps5y_1260d_base_v103_signal(equity, sharesbas, roic):
    bvps = equity / sharesbas.replace(0, np.nan)
    g = _rank(bvps / bvps.shift(756).replace(0, np.nan) - 1.0, 252)
    stab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    d = _rank(_f33_dilution(sharesbas, 504), 252)
    b = g * (0.5 + stab) - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional cross-economics interactions ---

# economic-spread (ROIC - hurdle) x reinvestment x anti-dilution (full value-creation)
def f33qc_f33_quality_compounder_valuecreate_252d_base_v104_signal(roic, fcf, netinc, sharesbas):
    spread = (_f33_roic_level(roic, 252) - 0.08)
    reinv = _f33_reinvest_rate(fcf, netinc, 252).clip(-1.0, 2.0)
    bb = (1.0 - _f33_dilution(sharesbas, 252).clip(-0.5, 1.0))
    b = spread * reinv * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth funded by FCF (reinvestment) x ROIC, rank-space
def f33qc_f33_quality_compounder_fcffundgrow_504d_base_v105_signal(fcf, revenue, roic):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    g = _f33_revgrowth(revenue, 504)
    r = _f33_roic_level(roic, 252)
    b = _rank(fm, 504) + _rank(g, 504) + _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE (netinc/equity) x retention (sustainable book growth), de-trended interaction
def f33qc_f33_quality_compounder_roeretain_252d_base_v106_signal(netinc, equity, fcf):
    roe = _z((netinc / equity.replace(0, np.nan)).rolling(252, min_periods=126).mean(), 504)
    reinv = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    b = roe * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital trend gated by dilution regime (improving returns, clean structure)
def f33qc_f33_quality_compounder_roictrendgate_504d_base_v107_signal(roic, sharesbas):
    sl = _slope(_f33_roic_level(roic, 126), 504)
    d = _f33_dilution(sharesbas, 252)
    b = sl * np.where(d <= 0, 1.0, -0.5)
    result = pd.Series(b, index=sl.index)
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounder index: mean of standardized FCF-margin, FCF-ROIC, reinvest, anti-dilution
def f33qc_f33_quality_compounder_cashindex_252d_base_v108_signal(fcf, revenue, equity, netinc, sharesbas):
    a = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    c = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    e = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    f = _z(-_f33_dilution(sharesbas, 252), 504)
    b = (a + c + e + f) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC dispersion ratio short/long x anti-dilution (stabilizing returns + buybacks)
def f33qc_f33_quality_compounder_dispratiobb_252d_base_v109_signal(roic, sharesbas):
    short = _std(roic, 126)
    long = _std(roic, 504)
    ratio = short / long.replace(0, np.nan)
    bb = -_f33_dilution(sharesbas, 252)
    b = (1.0 - ratio.clip(0, 3)) * (1.0 + bb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC percentile minus dilution percentile (cash quality-minus-dilution rank)
def f33qc_f33_quality_compounder_cashqmdrank_504d_base_v110_signal(fcf, equity, sharesbas):
    cr = _rank(_f33_fcf_roic(fcf, equity, 252), 504)
    dr = _rank(_f33_dilution(sharesbas, 252), 504)
    b = cr - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate dispersion (stable reinvestor) x ROIC (steady high-return reinvestor)
def f33qc_f33_quality_compounder_reinvdisproic_252d_base_v111_signal(fcf, netinc, roic):
    reinv = 1.0 - (fcf / netinc.replace(0, np.nan)).clip(-3, 3)
    stab = reinv.rolling(252, min_periods=126).mean() / reinv.rolling(252, min_periods=126).std().replace(0, np.nan)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = np.tanh(stab / 3.0) * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth x ROIC level minus dilution, standardized (growth-quality net of issuance)
def f33qc_f33_quality_compounder_grqnet_504d_base_v112_signal(revenue, roic, sharesbas):
    g = _z(_f33_revgrowth(revenue, 504), 252)
    r = _z(_f33_roic_level(roic, 252), 252)
    d = _z(_f33_dilution(sharesbas, 504), 252)
    b = 0.5 * (g + r) - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding ratio: FCF vs reinvestment need, x ROIC (internally-funded compounder)
def f33qc_f33_quality_compounder_selffundroic_504d_base_v113_signal(fcf, revenue, equity, roic):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    g = _f33_revgrowth(revenue, 504)
    capneed = g / _f33_capital_turnover(revenue, equity, 252).replace(0, np.nan)
    cover = fm - capneed.clip(-1, 1)
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = _z(cover, 504) * np.sqrt(r.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x FCF-conversion (cash backing of returns) acceleration, rank-space
def f33qc_f33_quality_compounder_roicconvmom_504d_base_v114_signal(roic, fcf, netinc):
    conv = (fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(126, min_periods=63).mean()
    r = _f33_roic_level(roic, 126)
    comp = conv * r
    mom = comp - comp.shift(126)
    b = _rank(mom - mom.shift(126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-compounder breadth: count of (ROIC>0, FCF-ROIC>0, reinvest>0, buyback) conditions
def f33qc_f33_quality_compounder_breadth_252d_base_v115_signal(roic, fcf, equity, netinc, sharesbas):
    c1 = (_f33_roic_level(roic, 252) > 0.08).astype(float)
    c2 = (_f33_fcf_roic(fcf, equity, 252) > 0).astype(float)
    c3 = (_f33_reinvest_rate(fcf, netinc, 252) > 0).astype(float)
    c4 = (_f33_dilution(sharesbas, 252) < 0).astype(float)
    qmd = _f33_roic_level(roic, 252) - _f33_dilution(sharesbas, 252)
    b = (c1 + c2 + c3 + c4) + 0.5 * np.tanh(qmd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level x reinvestment, EMA-smoothed displacement (compounder regime shift)
def f33qc_f33_quality_compounder_compdisp_252d_base_v116_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    reinv = _f33_reinvest_rate(fcf, netinc, 126)
    comp = r * reinv
    b = comp - comp.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash returns x capital turnover momentum (cash-return DuPont velocity)
def f33qc_f33_quality_compounder_cashdupontvel_504d_base_v117_signal(fcf, equity, revenue):
    cash = _f33_fcf_roic(fcf, equity, 126)
    t = _f33_capital_turnover(revenue, equity, 126)
    comp = cash * t
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net buyback yield x revenue per share growth (shrinking base + per-share top-line)
def f33qc_f33_quality_compounder_bbrevps_504d_base_v118_signal(sharesbas, revenue):
    bb = _z(-_f33_dilution(sharesbas, 252), 252)
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    b = bb * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-return composite: harmonic blend of ROIC level and FCF-ROIC minus dilution
def f33qc_f33_quality_compounder_harmret_252d_base_v119_signal(roic, fcf, equity, sharesbas):
    r = _f33_roic_level(roic, 252).clip(lower=0.001)
    cash = _f33_fcf_roic(fcf, equity, 252).clip(lower=0.001)
    harm = 2.0 / (1.0 / r + 1.0 / cash)
    d = _f33_dilution(sharesbas, 252)
    b = harm - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC above its own 2y median (regime) x reinvestment (high-regime reinvestor)
def f33qc_f33_quality_compounder_regimereinv_252d_base_v120_signal(roic, fcf, netinc):
    med = _f33_roic_level(roic, 126).rolling(504, min_periods=126).median()
    above = (_f33_roic_level(roic, 126) - med)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = above * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin x equity-turnover (cash generation per capital deployed)
def f33qc_f33_quality_compounder_fcfeqturn_252d_base_v121_signal(fcf, revenue, equity):
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b = (fm + t) / 2.0 + fm * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability minus dilution-volatility (steady returns + steady share count)
def f33qc_f33_quality_compounder_steadyboth_252d_base_v122_signal(roic, sharesbas):
    rstab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    dvol = _std(_f33_dilution(sharesbas, 63), 252)
    b = rstab - _z(dvol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic profit margin: (ROIC - hurdle) x revenue intensity (value per sales)
def f33qc_f33_quality_compounder_epmargin_252d_base_v123_signal(roic, revenue, equity):
    spread = _f33_roic_level(roic, 252) - 0.08
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b = spread * (1.0 + np.tanh(t))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded FCF growth x ROIC (cash compounding engine), momentum
def f33qc_f33_quality_compounder_fcfgrowroicmom_504d_base_v124_signal(fcf, roic):
    fg = _roc(fcf.rolling(63, min_periods=21).mean(), 252)
    r = _f33_roic_level(roic, 126)
    comp = fg.clip(-3, 3) * r
    b = comp - comp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution dispersion (regime stability of the compounder score)
def f33qc_f33_quality_compounder_qmddisp_504d_base_v125_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 126)
    qmd = r - d
    m = qmd.rolling(504, min_periods=252).mean()
    sd = qmd.rolling(504, min_periods=252).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow yield on equity x retention rank (cash-funded reinvestment percentile)
def f33qc_f33_quality_compounder_cashreinvrank_252d_base_v126_signal(fcf, equity, netinc):
    cr = _rank(_f33_fcf_roic(fcf, equity, 252), 504)
    reinvr = _rank(_f33_reinvest_rate(fcf, netinc, 252), 504)
    b = (cr + 0.5) * (reinvr + 0.5) - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x revenue-growth z minus dilution z (compounding triple in standardized space)
def f33qc_f33_quality_compounder_tripz_504d_base_v127_signal(roic, revenue, sharesbas):
    r = _z(_f33_roic_level(roic, 252), 504)
    g = _z(_f33_revgrowth(revenue, 504), 504)
    d = _z(_f33_dilution(sharesbas, 504), 504)
    b = r * g - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth x FCF conversion (quality-of-earnings growth)
def f33qc_f33_quality_compounder_nigrowconv_504d_base_v128_signal(netinc, fcf):
    nig = _z(_roc(netinc.rolling(63, min_periods=21).mean(), 504).clip(-3, 3), 252)
    conv = _z((fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(252, min_periods=126).mean(), 252)
    b = nig * conv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x FCF-margin interaction minus dilution (cash-rich high-return net of issuance)
def f33qc_f33_quality_compounder_richnet_252d_base_v129_signal(roic, fcf, revenue, sharesbas):
    r = _z(_f33_roic_level(roic, 252), 504)
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    d = _z(_f33_dilution(sharesbas, 252), 504)
    b = r * fm - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-at-high-returns above hurdle, smoothed (persistent value reinvestment)
def f33qc_f33_quality_compounder_valreinvema_252d_base_v130_signal(roic, fcf, netinc):
    excess = (_f33_roic_level(roic, 126) - 0.08).clip(lower=0)
    reinv = _f33_reinvest_rate(fcf, netinc, 126).clip(lower=0)
    b = (excess * reinv).ewm(span=84, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light high-return compounder: turnover x ROIC x anti-dilution (de-trended)
def f33qc_f33_quality_compounder_capliteret_252d_base_v131_signal(revenue, equity, roic, sharesbas):
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    r = _z(_f33_roic_level(roic, 252), 504)
    bb = _z(-_f33_dilution(sharesbas, 252), 504)
    b = (t + r + bb) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC slope minus dilution slope (improving cash returns + improving cap structure)
def f33qc_f33_quality_compounder_cashdilslope_504d_base_v132_signal(fcf, equity, sharesbas):
    cashsl = _slope(_f33_fcf_roic(fcf, equity, 63), 252)
    dsl = _slope(_f33_dilution(sharesbas, 63), 252)
    b = cashsl - dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-return percentile composite: rank of ROIC stability minus rank of dilution
def f33qc_f33_quality_compounder_durrank_504d_base_v133_signal(roic, sharesbas):
    sr = _rank(_f33_roic_stability(roic, 252), 504)
    dr = _rank(_f33_dilution(sharesbas, 252), 504)
    b = sr - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-acceleration penalized net-margin compounder (share-issuance-driven quality)
def f33qc_f33_quality_compounder_cagrnmnet_1260d_base_v134_signal(revenue, netinc, sharesbas):
    d126 = _f33_dilution(sharesbas, 126)
    dilaccel = d126 - d126.shift(126)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    b = np.tanh(8.0 * dilaccel) * (-1.0) * np.sign(nm) * (0.5 + _rank(nm, 504) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x reinvestment, dispersion-penalized (consistent compounder), rank
def f33qc_f33_quality_compounder_consistcomprank_504d_base_v135_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    reinv = _f33_reinvest_rate(fcf, netinc, 126)
    comp = r * reinv
    sd = comp.rolling(252, min_periods=126).std()
    score = comp / (1.0 + sd.abs())
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounder momentum: FCF-ROIC x reinvest, half-year change, ranked
def f33qc_f33_quality_compounder_cashmomrank_504d_base_v136_signal(fcf, equity, netinc):
    cash = _f33_fcf_roic(fcf, equity, 126)
    reinv = _f33_reinvest_rate(fcf, netinc, 126)
    comp = cash * reinv
    mom = comp - comp.shift(126)
    b = _rank(mom, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE minus dilution net of cost (return to existing owners above hurdle)
def f33qc_f33_quality_compounder_ownerexcess_252d_base_v137_signal(netinc, equity, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    excess = roe - 0.10
    d = _f33_dilution(sharesbas, 252)
    b = _z(excess, 504) - _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth stability x ROIC level x anti-dilution (steady-growth compounder)
def f33qc_f33_quality_compounder_steadygrowcomp_504d_base_v138_signal(revenue, roic, sharesbas):
    g = _f33_revgrowth(revenue, 126)
    gstab = g.rolling(504, min_periods=252).mean() / g.rolling(504, min_periods=252).std().replace(0, np.nan)
    r = _z(_f33_roic_level(roic, 252), 504)
    bb = _z(-_f33_dilution(sharesbas, 252), 504)
    b = np.tanh(gstab) * r + 0.5 * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin x ROIC interaction momentum (improving cash-rich returns)
def f33qc_f33_quality_compounder_fcfroicintmom_504d_base_v139_signal(fcf, revenue, roic):
    fm = _f33_fcf_margin(fcf, revenue, 126)
    r = _f33_roic_level(roic, 126)
    comp = fm * r
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted earnings yield on equity (ROE deflated by share growth)
def f33qc_f33_quality_compounder_roepershare_504d_base_v140_signal(netinc, equity, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    sg = sharesbas / sharesbas.shift(504).replace(0, np.nan)
    b = _z(roe / sg.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder acceleration: second difference of full compounder index
def f33qc_f33_quality_compounder_indexaccel_252d_base_v141_signal(roic, fcf, equity, netinc, sharesbas):
    a = _z(_f33_roic_level(roic, 126), 252)
    c = _z(_f33_fcf_roic(fcf, equity, 126), 252)
    e = _z(_f33_reinvest_rate(fcf, netinc, 126), 252)
    f = _z(-_f33_dilution(sharesbas, 126), 252)
    idx = (a + c + e + f) / 4.0
    chg = idx - idx.shift(126)
    b = chg - chg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-return reinvestment vs payout tilt (reinvestor vs distributor at high ROIC)
def f33qc_f33_quality_compounder_reinvtilt_252d_base_v142_signal(roic, fcf, netinc):
    payout = (fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(252, min_periods=126).mean()
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = -np.tanh(payout) * np.sqrt(r.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x FCF-margin minus dilution, ranked composite (cash-rich quality net of issuance)
def f33qc_f33_quality_compounder_richqmdrank_504d_base_v143_signal(roic, fcf, revenue, sharesbas):
    rr = _rank(_f33_roic_level(roic, 252), 504)
    fr = _rank(_f33_fcf_margin(fcf, revenue, 252), 504)
    dr = _rank(_f33_dilution(sharesbas, 252), 504)
    b = (rr + fr) / 2.0 - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit growth: spread x equity-growth momentum (compounding value created)
def f33qc_f33_quality_compounder_epgrowth_504d_base_v144_signal(roic, equity):
    spread = _f33_roic_level(roic, 126) - 0.08
    eqg = _f33_revgrowth(equity, 126)
    comp = spread * eqg
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-return-on-equity x retention minus dilution (internally-funded cash compounder)
def f33qc_f33_quality_compounder_intfundnet_252d_base_v145_signal(fcf, equity, netinc, sharesbas):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    reinv = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    d = _z(_f33_dilution(sharesbas, 252), 504)
    b = cash * reinv - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable compounder: ROIC stability x FCF-margin x anti-dilution (triple quality rank)
def f33qc_f33_quality_compounder_durtripleB_252d_base_v146_signal(roic, fcf, revenue, sharesbas):
    sr = _rank(_f33_roic_stability(roic, 252), 504)
    fr = _rank(_f33_fcf_margin(fcf, revenue, 252), 504)
    br = _rank(-_f33_dilution(sharesbas, 252), 504)
    b = sr + fr + br
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x FCF per share co-compounding minus dilution
def f33qc_f33_quality_compounder_persharecocomp_504d_base_v147_signal(revenue, fcf, sharesbas):
    rps = revenue / sharesbas.replace(0, np.nan)
    fps = fcf / sharesbas.replace(0, np.nan)
    rg = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    fg = _z(fps / fps.shift(504).replace(0, np.nan) - 1.0, 252)
    d = _z(_f33_dilution(sharesbas, 504), 252)
    b = rg * fg - 0.3 * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-quality convexity: sign(ROIC-hurdle) x squared reinvestment (convex compounding)
def f33qc_f33_quality_compounder_convexcomp_252d_base_v148_signal(roic, fcf, netinc):
    spread = _f33_roic_level(roic, 252) - 0.08
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = np.sign(spread) * (reinv ** 2) * np.tanh(5.0 * spread.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-economics agreement: do ROIC, FCF-ROIC, reinvest, anti-dilution all point up?
def f33qc_f33_quality_compounder_agreement_252d_base_v149_signal(roic, fcf, equity, netinc, sharesbas):
    s1 = np.sign(_z(_f33_roic_level(roic, 252), 504))
    s2 = np.sign(_z(_f33_fcf_roic(fcf, equity, 252), 504))
    s3 = np.sign(_z(_f33_reinvest_rate(fcf, netinc, 252), 504))
    s4 = np.sign(_z(-_f33_dilution(sharesbas, 252), 504))
    mag = _z(_f33_roic_level(roic, 252) - _f33_dilution(sharesbas, 252), 504)
    b = (s1 + s2 + s3 + s4) * np.tanh(mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grand compounder score: weighted blend of returns, reinvestment, cash, anti-dilution
def f33qc_f33_quality_compounder_grandscore_504d_base_v150_signal(roic, fcf, equity, netinc, revenue, sharesbas):
    r = _z(_f33_roic_level(roic, 252), 504)
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    reinv = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    g = _z(_f33_revgrowth(revenue, 504), 504)
    bb = _z(-_f33_dilution(sharesbas, 504), 504)
    b = 0.3 * r + 0.25 * cash + 0.2 * reinv + 0.15 * g + 0.1 * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33qc_f33_quality_compounder_qmd126_126d_base_v076_signal,
    f33qc_f33_quality_compounder_roicslopebb_252d_base_v077_signal,
    f33qc_f33_quality_compounder_instabdil_252d_base_v078_signal,
    f33qc_f33_quality_compounder_roicdilx_252d_base_v079_signal,
    f33qc_f33_quality_compounder_roicpersg_504d_base_v080_signal,
    f33qc_f33_quality_compounder_cashslopereinv_252d_base_v081_signal,
    f33qc_f33_quality_compounder_cashblend_252d_base_v082_signal,
    f33qc_f33_quality_compounder_cashaccelbb_504d_base_v083_signal,
    f33qc_f33_quality_compounder_cashstabreinv_252d_base_v084_signal,
    f33qc_f33_quality_compounder_cashconvmom_504d_base_v085_signal,
    f33qc_f33_quality_compounder_reinvslope_252d_base_v086_signal,
    f33qc_f33_quality_compounder_compvel_252d_base_v087_signal,
    f33qc_f33_quality_compounder_reinvrevx_504d_base_v088_signal,
    f33qc_f33_quality_compounder_roiceqgrow_504d_base_v089_signal,
    f33qc_f33_quality_compounder_hurdlerank_252d_base_v090_signal,
    f33qc_f33_quality_compounder_fmslroic_252d_base_v091_signal,
    f33qc_f33_quality_compounder_nmroicrank_252d_base_v092_signal,
    f33qc_f33_quality_compounder_cashqualdil_252d_base_v093_signal,
    f33qc_f33_quality_compounder_marginretrank_504d_base_v094_signal,
    f33qc_f33_quality_compounder_turnsloperoic_252d_base_v095_signal,
    f33qc_f33_quality_compounder_revpscash_504d_base_v096_signal,
    f33qc_f33_quality_compounder_fcfpsdurable_504d_base_v097_signal,
    f33qc_f33_quality_compounder_epspsbb_252d_base_v098_signal,
    f33qc_f33_quality_compounder_dur5y_1260d_base_v099_signal,
    f33qc_f33_quality_compounder_roicpremreinv_756d_base_v100_signal,
    f33qc_f33_quality_compounder_durcashgrow_504d_base_v101_signal,
    f33qc_f33_quality_compounder_dilconsistroic_504d_base_v102_signal,
    f33qc_f33_quality_compounder_bvps5y_1260d_base_v103_signal,
    f33qc_f33_quality_compounder_valuecreate_252d_base_v104_signal,
    f33qc_f33_quality_compounder_fcffundgrow_504d_base_v105_signal,
    f33qc_f33_quality_compounder_roeretain_252d_base_v106_signal,
    f33qc_f33_quality_compounder_roictrendgate_504d_base_v107_signal,
    f33qc_f33_quality_compounder_cashindex_252d_base_v108_signal,
    f33qc_f33_quality_compounder_dispratiobb_252d_base_v109_signal,
    f33qc_f33_quality_compounder_cashqmdrank_504d_base_v110_signal,
    f33qc_f33_quality_compounder_reinvdisproic_252d_base_v111_signal,
    f33qc_f33_quality_compounder_grqnet_504d_base_v112_signal,
    f33qc_f33_quality_compounder_selffundroic_504d_base_v113_signal,
    f33qc_f33_quality_compounder_roicconvmom_504d_base_v114_signal,
    f33qc_f33_quality_compounder_breadth_252d_base_v115_signal,
    f33qc_f33_quality_compounder_compdisp_252d_base_v116_signal,
    f33qc_f33_quality_compounder_cashdupontvel_504d_base_v117_signal,
    f33qc_f33_quality_compounder_bbrevps_504d_base_v118_signal,
    f33qc_f33_quality_compounder_harmret_252d_base_v119_signal,
    f33qc_f33_quality_compounder_regimereinv_252d_base_v120_signal,
    f33qc_f33_quality_compounder_fcfeqturn_252d_base_v121_signal,
    f33qc_f33_quality_compounder_steadyboth_252d_base_v122_signal,
    f33qc_f33_quality_compounder_epmargin_252d_base_v123_signal,
    f33qc_f33_quality_compounder_fcfgrowroicmom_504d_base_v124_signal,
    f33qc_f33_quality_compounder_qmddisp_504d_base_v125_signal,
    f33qc_f33_quality_compounder_cashreinvrank_252d_base_v126_signal,
    f33qc_f33_quality_compounder_tripz_504d_base_v127_signal,
    f33qc_f33_quality_compounder_nigrowconv_504d_base_v128_signal,
    f33qc_f33_quality_compounder_richnet_252d_base_v129_signal,
    f33qc_f33_quality_compounder_valreinvema_252d_base_v130_signal,
    f33qc_f33_quality_compounder_capliteret_252d_base_v131_signal,
    f33qc_f33_quality_compounder_cashdilslope_504d_base_v132_signal,
    f33qc_f33_quality_compounder_durrank_504d_base_v133_signal,
    f33qc_f33_quality_compounder_cagrnmnet_1260d_base_v134_signal,
    f33qc_f33_quality_compounder_consistcomprank_504d_base_v135_signal,
    f33qc_f33_quality_compounder_cashmomrank_504d_base_v136_signal,
    f33qc_f33_quality_compounder_ownerexcess_252d_base_v137_signal,
    f33qc_f33_quality_compounder_steadygrowcomp_504d_base_v138_signal,
    f33qc_f33_quality_compounder_fcfroicintmom_504d_base_v139_signal,
    f33qc_f33_quality_compounder_roepershare_504d_base_v140_signal,
    f33qc_f33_quality_compounder_indexaccel_252d_base_v141_signal,
    f33qc_f33_quality_compounder_reinvtilt_252d_base_v142_signal,
    f33qc_f33_quality_compounder_richqmdrank_504d_base_v143_signal,
    f33qc_f33_quality_compounder_epgrowth_504d_base_v144_signal,
    f33qc_f33_quality_compounder_intfundnet_252d_base_v145_signal,
    f33qc_f33_quality_compounder_durtripleB_252d_base_v146_signal,
    f33qc_f33_quality_compounder_persharecocomp_504d_base_v147_signal,
    f33qc_f33_quality_compounder_convexcomp_252d_base_v148_signal,
    f33qc_f33_quality_compounder_agreement_252d_base_v149_signal,
    f33qc_f33_quality_compounder_grandscore_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_QUALITY_COMPOUNDER_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    n = 1500
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    roic = _fund(101, base=0.15, drift=0.01, vol=0.20, allow_neg=True).rename("roic")
    fcf = _fund(102, base=5e7, drift=0.02, vol=0.06, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=1e8, drift=0.005, vol=0.02).rename("sharesbas")
    revenue = _fund(104, base=5e8, drift=0.02, vol=0.04).rename("revenue")
    equity = _fund(105, base=4e8, drift=0.015, vol=0.04).rename("equity")
    netinc = _fund(106, base=6e7, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "revenue": revenue, "equity": equity, "netinc": netinc}

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

    print("OK f33_quality_compounder_base_076_150_claude: %d features pass" % n_features)
