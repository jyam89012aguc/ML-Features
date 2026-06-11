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
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (Altman-Z / distress / runway) =====
def _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    a = assets.replace(0, np.nan)
    x1 = workingcapital / a
    x2 = retearn / a
    x3 = ebit / a
    x4 = equity / liabilities.replace(0, np.nan)
    x5 = revenue / a
    return 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5


def _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets):
    a = assets.replace(0, np.nan)
    x1 = workingcapital / a
    x2 = retearn / a
    x3 = ebit / a
    x4 = equity / liabilities.replace(0, np.nan)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _f37_wc_assets(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f37_re_assets(retearn, assets):
    return retearn / assets.replace(0, np.nan)


def _f37_ebit_assets(ebit, assets):
    return ebit / assets.replace(0, np.nan)


def _f37_eq_liab(equity, liabilities):
    return equity / liabilities.replace(0, np.nan)


def _f37_rev_assets(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f37_runway(cashneq, opex):
    return cashneq / opex.replace(0, np.nan)


# ============================================================
# --- longer-window component levels (structural distress) ---

# X1 working-capital/assets, half-year smoothed (structural liquidity)
def f37da_f37_distress_risk_altman_wcassets_lvl_126d_base_v076_signal(workingcapital, assets):
    b = _mean(_f37_wc_assets(workingcapital, assets), 126)
    return b.replace([np.inf, -np.inf], np.nan)


# X3 EBIT/assets, year smoothed (structural operating return)
def f37da_f37_distress_risk_altman_ebitassets_lvl_252d_base_v077_signal(ebit, assets):
    b = _mean(_f37_ebit_assets(ebit, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# X4 equity/liabilities, year smoothed (structural solvency)
def f37da_f37_distress_risk_altman_eqliab_lvl_252d_base_v078_signal(equity, liabilities):
    b = _mean(_f37_eq_liab(equity, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# composite Z, year smoothed (structural distress level)
def f37da_f37_distress_risk_altman_zscore_lvl_252d_base_v079_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _mean(z, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- gray-zone occupancy & probabilistic distress ---

# gray-zone proximity: distance of Z to the nearest distress boundary (1.81 / 2.99), smoothed
def f37da_f37_distress_risk_altman_grayzone_252d_base_v080_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    d_low = (z - 1.81).abs()
    d_high = (z - 2.99).abs()
    nearest = pd.concat([d_low, d_high], axis=1).min(axis=1)
    signed = nearest * np.where(z < 2.40, -1.0, 1.0)
    b = _mean(signed, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# logistic distress probability from Z (bounded default-likelihood proxy)
def f37da_f37_distress_risk_altman_pdistress_63d_base_v081_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    b = _mean(p, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- cross-component spreads (which lever is weak) ---

# liquidity-vs-profitability tilt: ratio of X1 to X3, tanh-squashed (which pillar carries the firm)
def f37da_f37_distress_risk_altman_x1x3spread_63d_base_v082_signal(workingcapital, ebit, assets):
    x1 = _f37_wc_assets(workingcapital, assets)
    x3 = _f37_ebit_assets(ebit, assets)
    b = _mean(np.tanh(x1 / x3.replace(0, np.nan)), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# cushion-vs-turnover spread: X2 minus X5 (retained earnings vs asset turnover)
def f37da_f37_distress_risk_altman_x2x5spread_63d_base_v083_signal(retearn, revenue, assets):
    b = _mean(_f37_re_assets(retearn, assets) - _f37_rev_assets(revenue, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# solvency-vs-liquidity spread: X4 minus X1 (long-term solvency vs short-term liquidity)
def f37da_f37_distress_risk_altman_x4x1spread_63d_base_v084_signal(equity, liabilities, workingcapital, assets):
    b = _mean(_f37_eq_liab(equity, liabilities) - _f37_wc_assets(workingcapital, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- dispersion of Z components (lopsided distress) ---

# component-dispersion trajectory: slope of cross-pillar std (is distress becoming lopsided?)
def f37da_f37_distress_risk_altman_compdisp_63d_base_v085_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x1 = _f37_wc_assets(workingcapital, assets)
    x2 = _f37_re_assets(retearn, assets)
    x3 = _f37_ebit_assets(ebit, assets)
    x4 = _f37_eq_liab(equity, liabilities)
    x5 = _f37_rev_assets(revenue, assets)
    disp = pd.concat([x1, x2, x3, x4, x5], axis=1).std(axis=1)
    b = _slope(disp, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# weakest-link: minimum of the standardized Z components (the worst pillar)
def f37da_f37_distress_risk_altman_weaklink_126d_base_v086_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    x1 = _z(_f37_wc_assets(workingcapital, assets), 252)
    x2 = _z(_f37_re_assets(retearn, assets), 252)
    x3 = _z(_f37_ebit_assets(ebit, assets), 252)
    x4 = _z(_f37_eq_liab(equity, liabilities), 252)
    b = pd.concat([x1, x2, x3, x4], axis=1).min(axis=1)
    return b.replace([np.inf, -np.inf], np.nan)


# --- runway variants ---

# runway floored by retained-earnings drag: cash + ebit cushion over opex (operating runway)
def f37da_f37_distress_risk_altman_oprunway_63d_base_v087_signal(cashneq, ebit, opex):
    b = _mean(_safe_div(cashneq + ebit, opex), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# net-burn months: cash buffer relative to monthly net operating outflow (opex over revenue), z-scored
def f37da_f37_distress_risk_altman_netburn_63d_base_v088_signal(cashneq, opex, revenue):
    burnratio = _safe_div(opex, revenue)
    months = _safe_div(cashneq, opex) * burnratio
    b = _z(months, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# runway-to-liabilities: how runway compares to the debt load it must service
def f37da_f37_distress_risk_altman_runwayliab_63d_base_v089_signal(cashneq, opex, liabilities, assets):
    r = _f37_runway(cashneq, opex)
    lev = _safe_div(liabilities, assets)
    b = _mean(r * (1.0 - lev), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# runway acceleration: second difference of runway (burn speeding up)
def f37da_f37_distress_risk_altman_runwayaccel_126d_base_v090_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    d = r - r.shift(63)
    b = d - d.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- leverage & solvency trajectory ---

# net-liability change: (liabilities - cash) trajectory relative to assets
def f37da_f37_distress_risk_altman_netliabslope_252d_base_v091_signal(liabilities, cashneq, assets):
    nl = _safe_div(liabilities - cashneq, assets)
    b = _slope(nl, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# net debt / assets level (leverage net of cash buffer)
def f37da_f37_distress_risk_altman_netdebt_63d_base_v092_signal(liabilities, cashneq, assets):
    b = _mean(_safe_div(liabilities - cashneq, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# equity/assets level (capitalization ratio)
def f37da_f37_distress_risk_altman_eqassets_63d_base_v093_signal(equity, assets):
    b = _mean(_safe_div(equity, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities/equity (debt-to-equity), sign-magnitude stabilized
def f37da_f37_distress_risk_altman_debttoeq_63d_base_v094_signal(liabilities, equity):
    r = _safe_div(liabilities, equity)
    b = _mean(np.sign(r) * np.log1p(r.abs()), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- year-over-year structural change ---

# equity/liabilities change year-over-year (solvency improvement/erosion)
def f37da_f37_distress_risk_altman_eqliabyoy_252d_base_v095_signal(equity, liabilities):
    x = _f37_eq_liab(equity, liabilities)
    xs = _mean(x, 21)
    b = xs - xs.shift(252)
    return b.replace([np.inf, -np.inf], np.nan)


# retained-earnings/assets change year-over-year (cushion build)
def f37da_f37_distress_risk_altman_reyoy_252d_base_v096_signal(retearn, assets):
    x = _f37_re_assets(retearn, assets)
    xs = _mean(x, 21)
    b = xs - xs.shift(252)
    return b.replace([np.inf, -np.inf], np.nan)


# revenue/assets change year-over-year (turnover trend)
def f37da_f37_distress_risk_altman_revassetsyoy_252d_base_v097_signal(revenue, assets):
    x = _f37_rev_assets(revenue, assets)
    xs = _mean(x, 21)
    b = xs - xs.shift(252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- growth rates of distress inputs ---

# assets growth rate (balance-sheet expansion/contraction)
def f37da_f37_distress_risk_altman_assetsgrow_252d_base_v098_signal(assets):
    b = np.log(assets.replace(0, np.nan) / assets.shift(252).replace(0, np.nan))
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities growth rate (debt accumulation)
def f37da_f37_distress_risk_altman_liabgrow_252d_base_v099_signal(liabilities):
    b = np.log(liabilities.replace(0, np.nan) / liabilities.shift(252).replace(0, np.nan))
    return b.replace([np.inf, -np.inf], np.nan)


# cash growth minus opex growth (is cash keeping up with the burn)
def f37da_f37_distress_risk_altman_cashvsopex_126d_base_v100_signal(cashneq, opex):
    gc = np.log(cashneq.replace(0, np.nan) / cashneq.shift(126).replace(0, np.nan))
    go = np.log(opex.replace(0, np.nan) / opex.shift(126).replace(0, np.nan))
    b = gc - go
    return b.replace([np.inf, -np.inf], np.nan)


# --- z-scored ratios at alternate windows ---

# cash/assets z-scored vs half-year history (liquidity-density shift)
def f37da_f37_distress_risk_altman_cashassetsz_126d_base_v101_signal(cashneq, assets):
    b = _z(_safe_div(cashneq, assets), 126)
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities/ebit z-scored (debt-burden regime, half-year)
def f37da_f37_distress_risk_altman_liabebitz_126d_base_v102_signal(liabilities, ebit):
    b = _z(_safe_div(liabilities, ebit), 126)
    return b.replace([np.inf, -np.inf], np.nan)


# working-capital/liabilities z-scored (short-term solvency regime)
def f37da_f37_distress_risk_altman_wcliabz_252d_base_v103_signal(workingcapital, liabilities):
    b = _z(_safe_div(workingcapital, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# opex/revenue z-scored (cost-burden regime)
def f37da_f37_distress_risk_altman_opexrevz_252d_base_v104_signal(opex, revenue):
    b = _z(_safe_div(opex, revenue), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- ranks at alternate windows ---

# working-capital/assets rank vs 2yr history
def f37da_f37_distress_risk_altman_wcrank_504d_base_v105_signal(workingcapital, assets):
    b = _rank(_f37_wc_assets(workingcapital, assets), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# net-debt/assets rank vs 2yr history
def f37da_f37_distress_risk_altman_netdebtrank_504d_base_v106_signal(liabilities, cashneq, assets):
    b = _rank(_safe_div(liabilities - cashneq, assets), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# cash-coverage rank: cash/liabilities percentile vs 2yr
def f37da_f37_distress_risk_altman_cashcovrank_504d_base_v107_signal(cashneq, liabilities):
    b = _rank(_safe_div(cashneq, liabilities), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# --- interaction composites ---

# distress severity: probability-of-distress times leverage (loss-given-default proxy)
def f37da_f37_distress_risk_altman_severity_63d_base_v108_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    lev = _safe_div(liabilities, assets)
    b = _mean(p * lev, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# runway-weighted profitability gap: short runway penalizes weak EBIT/assets
def f37da_f37_distress_risk_altman_runwayprofgap_63d_base_v109_signal(cashneq, opex, ebit, assets):
    r = _f37_runway(cashneq, opex)
    roa = _f37_ebit_assets(ebit, assets)
    b = _mean(np.tanh(r - 1.0) * roa, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# solvency-times-turnover: equity/liab interacted with revenue/assets (durable franchise)
def f37da_f37_distress_risk_altman_solvturn_63d_base_v110_signal(equity, liabilities, revenue, assets):
    solv = _f37_eq_liab(equity, liabilities)
    turn = _f37_rev_assets(revenue, assets)
    b = _mean(np.tanh(solv) * turn, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- volatility / instability at alternate windows ---

# EBIT/assets instability over a year (earnings fragility)
def f37da_f37_distress_risk_altman_ebitvol_252d_base_v111_signal(ebit, assets):
    b = _std(_f37_ebit_assets(ebit, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# equity/liab instability over a year (solvency fragility)
def f37da_f37_distress_risk_altman_solvvol_252d_base_v112_signal(equity, liabilities):
    b = _std(_f37_eq_liab(equity, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of cash (cash-flow lumpiness)
def f37da_f37_distress_risk_altman_cashcv_126d_base_v113_signal(cashneq):
    b = _std(cashneq, 126) / _mean(cashneq, 126).replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# --- worst-case / drawdown of distress metrics ---

# Z drawdown: current Z relative to its trailing 504d peak (solvency drawdown)
def f37da_f37_distress_risk_altman_zdrawdown_504d_base_v114_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    peak = z.rolling(504, min_periods=126).max()
    b = z - peak
    return b.replace([np.inf, -np.inf], np.nan)


# runway drawdown: current runway vs trailing 504d peak (cash drawdown)
def f37da_f37_distress_risk_altman_runwaydraw_504d_base_v115_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    peak = r.rolling(504, min_periods=126).max()
    b = r / peak.replace(0, np.nan) - 1.0
    return b.replace([np.inf, -np.inf], np.nan)


# equity drawdown from 504d peak (book-value erosion depth)
def f37da_f37_distress_risk_altman_eqdraw_504d_base_v116_signal(equity, assets):
    e = _safe_div(equity, assets)
    peak = e.rolling(504, min_periods=126).max()
    b = e - peak
    return b.replace([np.inf, -np.inf], np.nan)


# --- persistence / streaks ---

# Z-below-median streak: consecutive periods Z under its 252d median, smoothed
def f37da_f37_distress_risk_altman_zweakstreak_252d_base_v117_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    ref = z.rolling(252, min_periods=63).median()
    weak = (z < ref).astype(float)
    b = weak.rolling(63, min_periods=21).sum() - 31.5
    return b.replace([np.inf, -np.inf], np.nan)


# negative-EBIT persistence over half-year, blended with depth of loss
def f37da_f37_distress_risk_altman_lossdepth_126d_base_v118_signal(ebit, assets):
    roa = _f37_ebit_assets(ebit, assets)
    flag = (roa < 0).astype(float)
    occ = flag.rolling(126, min_periods=42).mean()
    depth = (-roa).clip(lower=0).rolling(63, min_periods=21).mean()
    b = occ + 5.0 * depth
    return b.replace([np.inf, -np.inf], np.nan)


# --- tanh-bounded shocks at alternate metrics ---

# bounded solvency shock: jump in equity/liabilities over a quarter, squashed
def f37da_f37_distress_risk_altman_solvshock_63d_base_v119_signal(equity, liabilities):
    x = _f37_eq_liab(equity, liabilities)
    chg = x - x.shift(63)
    b = np.tanh(2.0 * chg)
    return b.replace([np.inf, -np.inf], np.nan)


# bounded runway shock: relative change in runway over a quarter, squashed
def f37da_f37_distress_risk_altman_runwayshock_63d_base_v120_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    rel = r / r.shift(63).replace(0, np.nan) - 1.0
    b = np.tanh(3.0 * rel)
    return b.replace([np.inf, -np.inf], np.nan)


# --- multi-window distress spreads ---

# Z half-vs-2yr spread (medium vs structural standing)
def f37da_f37_distress_risk_altman_zspread_126v504_base_v121_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _mean(z, 126) - _mean(z, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# leverage short-vs-long spread (recent leverage vs structural)
def f37da_f37_distress_risk_altman_levspread_63v252_base_v122_signal(liabilities, assets):
    lev = _safe_div(liabilities, assets)
    b = _mean(lev, 63) - _mean(lev, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# cash-coverage short-vs-long spread
def f37da_f37_distress_risk_altman_cashspread_63v252_base_v123_signal(cashneq, liabilities):
    cc = _safe_div(cashneq, liabilities)
    b = _mean(cc, 63) - _mean(cc, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- composite survival / quality scores ---

# distress-adjusted quality: EBIT/assets times solvency, ranked (safe-and-profitable)
def f37da_f37_distress_risk_altman_safeprofit_504d_base_v124_signal(ebit, assets, equity, liabilities):
    roa = _f37_ebit_assets(ebit, assets)
    solv = _f37_eq_liab(equity, liabilities)
    score = roa * np.tanh(solv)
    b = _rank(score, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# fragility index: leverage divided by interest-coverage proxy (EBIT/liab)
def f37da_f37_distress_risk_altman_fragility_63d_base_v125_signal(liabilities, assets, ebit):
    lev = _safe_div(liabilities, assets)
    cov = _safe_div(ebit, liabilities)
    b = _mean(lev / (cov.abs() + 0.01), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# survival composite: log-runway plus capitalization minus leverage, smoothed
def f37da_f37_distress_risk_altman_survcomp_126d_base_v126_signal(cashneq, opex, equity, assets, liabilities):
    cov = np.log1p(_safe_div(cashneq, opex).clip(lower=0))
    cap = _safe_div(equity, assets)
    lev = _safe_div(liabilities, assets)
    b = _mean(cov + cap - lev, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# --- additional component ratios ---

# retained-earnings / liabilities (earned cushion vs debt)
def f37da_f37_distress_risk_altman_reliab_63d_base_v127_signal(retearn, liabilities):
    b = _mean(_safe_div(retearn, liabilities), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# working-capital / revenue (operating-liquidity intensity)
def f37da_f37_distress_risk_altman_wcrev_63d_base_v128_signal(workingcapital, revenue):
    b = _mean(_safe_div(workingcapital, revenue), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# opex / assets (operating-burden density)
def f37da_f37_distress_risk_altman_opexassets_63d_base_v129_signal(opex, assets):
    b = _mean(_safe_div(opex, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# cash / revenue (liquidity relative to sales scale)
def f37da_f37_distress_risk_altman_cashrev_63d_base_v130_signal(cashneq, revenue):
    b = _mean(_safe_div(cashneq, revenue), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# ebit / equity (return on book equity, distress-relevant)
def f37da_f37_distress_risk_altman_ebiteq_63d_base_v131_signal(ebit, equity):
    r = _safe_div(ebit, equity)
    b = _mean(np.sign(r) * np.log1p(r.abs()), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- slopes of additional metrics ---

# cash/assets trajectory slope (building/draining liquidity buffer)
def f37da_f37_distress_risk_altman_cashassetsslope_252d_base_v132_signal(cashneq, assets):
    b = _slope(_safe_div(cashneq, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# working-capital/liabilities trajectory slope (short-term solvency direction)
def f37da_f37_distress_risk_altman_wcslope_252d_base_v133_signal(workingcapital, liabilities):
    b = _slope(_safe_div(workingcapital, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# opex/revenue trajectory slope (operating-leverage stress direction)
def f37da_f37_distress_risk_altman_opexrevslope_252d_base_v134_signal(opex, revenue):
    b = _slope(_safe_div(opex, revenue), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# Z'' trajectory slope (private-firm distress direction)
def f37da_f37_distress_risk_altman_zprimeslope_252d_base_v135_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = _slope(z, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- EWMA displacements of additional metrics ---

# leverage displacement: liabilities/assets minus slow EWMA (acute leverage spike)
def f37da_f37_distress_risk_altman_levdisp_base_v136_signal(liabilities, assets):
    lev = _safe_div(liabilities, assets)
    b = lev - lev.ewm(span=126, min_periods=42).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# EBIT/assets displacement vs slow EWMA (acute profitability shock)
def f37da_f37_distress_risk_altman_roadisp_base_v137_signal(ebit, assets):
    roa = _f37_ebit_assets(ebit, assets)
    b = roa - roa.ewm(span=126, min_periods=42).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# cash/liabilities displacement vs slow EWMA (acute coverage shock)
def f37da_f37_distress_risk_altman_covdisp_base_v138_signal(cashneq, liabilities):
    cov = _safe_div(cashneq, liabilities)
    b = cov - cov.ewm(span=63, min_periods=21).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# --- robust / median-based features ---

# Z robust z-score over a year (median/MAD standardized solvency)
def f37da_f37_distress_risk_altman_zrobust_252d_base_v139_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    med = z.rolling(252, min_periods=63).median()
    mad = (z - med).abs().rolling(252, min_periods=63).median()
    b = (z - med) / (1.4826 * mad).replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# runway robust z-score over a year
def f37da_f37_distress_risk_altman_runwayrobust_252d_base_v140_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    med = r.rolling(252, min_periods=63).median()
    mad = (r - med).abs().rolling(252, min_periods=63).median()
    b = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# --- asymmetry / sign features ---

# profitability asymmetry: downside EBIT/assets semi-deviation vs upside (loss skew)
def f37da_f37_distress_risk_altman_roaskew_252d_base_v141_signal(ebit, assets):
    roa = _f37_ebit_assets(ebit, assets)
    d = roa.diff()
    down = d.where(d < 0, 0.0).rolling(252, min_periods=63).std()
    up = d.where(d > 0, 0.0).rolling(252, min_periods=63).std()
    b = (down - up) / (down + up).replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# sign-consistency of EBIT (fraction profitable minus fraction loss-making over a year)
def f37da_f37_distress_risk_altman_ebitsign_252d_base_v142_signal(ebit):
    pos = (ebit > 0).astype(float)
    neg = (ebit < 0).astype(float)
    b = (pos - neg).rolling(252, min_periods=63).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# --- composite deterioration / improvement ---

# weighted deterioration score: magnitude-weighted decline across three pillars
def f37da_f37_distress_risk_altman_wdeteriorate_126d_base_v143_signal(ebit, equity, liabilities, assets):
    roa = _z(_f37_ebit_assets(ebit, assets), 252)
    solv = _z(_f37_eq_liab(equity, liabilities), 252)
    lev = _z(_safe_div(liabilities, assets), 252)
    score = -(roa + solv) + lev
    b = _mean(score, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# turnaround proxy: EBIT/assets recovering off a trailing low (distress inflection)
def f37da_f37_distress_risk_altman_turnaround_252d_base_v144_signal(ebit, assets):
    roa = _f37_ebit_assets(ebit, assets)
    trough = roa.rolling(252, min_periods=63).min()
    b = roa - trough
    return b.replace([np.inf, -np.inf], np.nan)


# --- min/max distress extremes at alternate windows ---

# Z range-position: where current Z sits within its trailing 252d min-max band (0=worst,1=best)
def f37da_f37_distress_risk_altman_zmax_252d_base_v145_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    hi = z.rolling(252, min_periods=63).max()
    lo = z.rolling(252, min_periods=63).min()
    b = (z - lo) / (hi - lo).replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# Z range over a year (solvency volatility envelope: max minus min)
def f37da_f37_distress_risk_altman_zrange_252d_base_v146_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z.rolling(252, min_periods=63).max() - z.rolling(252, min_periods=63).min()
    return b.replace([np.inf, -np.inf], np.nan)


# --- runway/burn composites ---

# burn coverage by operating surplus: (revenue-opex) relative to cash (self-funding inverse-burn)
def f37da_f37_distress_risk_altman_selffund_63d_base_v147_signal(revenue, opex, cashneq):
    b = _mean(_safe_div(revenue - opex, cashneq), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# liquidity-stress index: opex/cash times leverage (combined burn-and-debt pressure)
def f37da_f37_distress_risk_altman_liqstress_63d_base_v148_signal(opex, cashneq, liabilities, assets):
    burn = _safe_div(opex, cashneq)
    lev = _safe_div(liabilities, assets)
    b = _mean(burn * lev, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- final cross-pillar composites ---

# capital-adequacy composite: equity + retained earnings over liabilities (total cushion)
def f37da_f37_distress_risk_altman_capadeq_63d_base_v149_signal(equity, retearn, liabilities):
    b = _mean(_safe_div(equity + retearn, liabilities), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# distress-momentum composite: change in probability-of-distress over a quarter
def f37da_f37_distress_risk_altman_pdistmom_126d_base_v150_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    p = 1.0 / (1.0 + np.exp(2.0 * (z - 1.81)))
    ps = _mean(p, 21)
    b = ps - ps.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37da_f37_distress_risk_altman_wcassets_lvl_126d_base_v076_signal,
    f37da_f37_distress_risk_altman_ebitassets_lvl_252d_base_v077_signal,
    f37da_f37_distress_risk_altman_eqliab_lvl_252d_base_v078_signal,
    f37da_f37_distress_risk_altman_zscore_lvl_252d_base_v079_signal,
    f37da_f37_distress_risk_altman_grayzone_252d_base_v080_signal,
    f37da_f37_distress_risk_altman_pdistress_63d_base_v081_signal,
    f37da_f37_distress_risk_altman_x1x3spread_63d_base_v082_signal,
    f37da_f37_distress_risk_altman_x2x5spread_63d_base_v083_signal,
    f37da_f37_distress_risk_altman_x4x1spread_63d_base_v084_signal,
    f37da_f37_distress_risk_altman_compdisp_63d_base_v085_signal,
    f37da_f37_distress_risk_altman_weaklink_126d_base_v086_signal,
    f37da_f37_distress_risk_altman_oprunway_63d_base_v087_signal,
    f37da_f37_distress_risk_altman_netburn_63d_base_v088_signal,
    f37da_f37_distress_risk_altman_runwayliab_63d_base_v089_signal,
    f37da_f37_distress_risk_altman_runwayaccel_126d_base_v090_signal,
    f37da_f37_distress_risk_altman_netliabslope_252d_base_v091_signal,
    f37da_f37_distress_risk_altman_netdebt_63d_base_v092_signal,
    f37da_f37_distress_risk_altman_eqassets_63d_base_v093_signal,
    f37da_f37_distress_risk_altman_debttoeq_63d_base_v094_signal,
    f37da_f37_distress_risk_altman_eqliabyoy_252d_base_v095_signal,
    f37da_f37_distress_risk_altman_reyoy_252d_base_v096_signal,
    f37da_f37_distress_risk_altman_revassetsyoy_252d_base_v097_signal,
    f37da_f37_distress_risk_altman_assetsgrow_252d_base_v098_signal,
    f37da_f37_distress_risk_altman_liabgrow_252d_base_v099_signal,
    f37da_f37_distress_risk_altman_cashvsopex_126d_base_v100_signal,
    f37da_f37_distress_risk_altman_cashassetsz_126d_base_v101_signal,
    f37da_f37_distress_risk_altman_liabebitz_126d_base_v102_signal,
    f37da_f37_distress_risk_altman_wcliabz_252d_base_v103_signal,
    f37da_f37_distress_risk_altman_opexrevz_252d_base_v104_signal,
    f37da_f37_distress_risk_altman_wcrank_504d_base_v105_signal,
    f37da_f37_distress_risk_altman_netdebtrank_504d_base_v106_signal,
    f37da_f37_distress_risk_altman_cashcovrank_504d_base_v107_signal,
    f37da_f37_distress_risk_altman_severity_63d_base_v108_signal,
    f37da_f37_distress_risk_altman_runwayprofgap_63d_base_v109_signal,
    f37da_f37_distress_risk_altman_solvturn_63d_base_v110_signal,
    f37da_f37_distress_risk_altman_ebitvol_252d_base_v111_signal,
    f37da_f37_distress_risk_altman_solvvol_252d_base_v112_signal,
    f37da_f37_distress_risk_altman_cashcv_126d_base_v113_signal,
    f37da_f37_distress_risk_altman_zdrawdown_504d_base_v114_signal,
    f37da_f37_distress_risk_altman_runwaydraw_504d_base_v115_signal,
    f37da_f37_distress_risk_altman_eqdraw_504d_base_v116_signal,
    f37da_f37_distress_risk_altman_zweakstreak_252d_base_v117_signal,
    f37da_f37_distress_risk_altman_lossdepth_126d_base_v118_signal,
    f37da_f37_distress_risk_altman_solvshock_63d_base_v119_signal,
    f37da_f37_distress_risk_altman_runwayshock_63d_base_v120_signal,
    f37da_f37_distress_risk_altman_zspread_126v504_base_v121_signal,
    f37da_f37_distress_risk_altman_levspread_63v252_base_v122_signal,
    f37da_f37_distress_risk_altman_cashspread_63v252_base_v123_signal,
    f37da_f37_distress_risk_altman_safeprofit_504d_base_v124_signal,
    f37da_f37_distress_risk_altman_fragility_63d_base_v125_signal,
    f37da_f37_distress_risk_altman_survcomp_126d_base_v126_signal,
    f37da_f37_distress_risk_altman_reliab_63d_base_v127_signal,
    f37da_f37_distress_risk_altman_wcrev_63d_base_v128_signal,
    f37da_f37_distress_risk_altman_opexassets_63d_base_v129_signal,
    f37da_f37_distress_risk_altman_cashrev_63d_base_v130_signal,
    f37da_f37_distress_risk_altman_ebiteq_63d_base_v131_signal,
    f37da_f37_distress_risk_altman_cashassetsslope_252d_base_v132_signal,
    f37da_f37_distress_risk_altman_wcslope_252d_base_v133_signal,
    f37da_f37_distress_risk_altman_opexrevslope_252d_base_v134_signal,
    f37da_f37_distress_risk_altman_zprimeslope_252d_base_v135_signal,
    f37da_f37_distress_risk_altman_levdisp_base_v136_signal,
    f37da_f37_distress_risk_altman_roadisp_base_v137_signal,
    f37da_f37_distress_risk_altman_covdisp_base_v138_signal,
    f37da_f37_distress_risk_altman_zrobust_252d_base_v139_signal,
    f37da_f37_distress_risk_altman_runwayrobust_252d_base_v140_signal,
    f37da_f37_distress_risk_altman_roaskew_252d_base_v141_signal,
    f37da_f37_distress_risk_altman_ebitsign_252d_base_v142_signal,
    f37da_f37_distress_risk_altman_wdeteriorate_126d_base_v143_signal,
    f37da_f37_distress_risk_altman_turnaround_252d_base_v144_signal,
    f37da_f37_distress_risk_altman_zmax_252d_base_v145_signal,
    f37da_f37_distress_risk_altman_zrange_252d_base_v146_signal,
    f37da_f37_distress_risk_altman_selffund_63d_base_v147_signal,
    f37da_f37_distress_risk_altman_liqstress_63d_base_v148_signal,
    f37da_f37_distress_risk_altman_capadeq_63d_base_v149_signal,
    f37da_f37_distress_risk_altman_pdistmom_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_DISTRESS_RISK_ALTMAN_REGISTRY_076_150 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    cols = {}
    cols["assets"] = _fund(1, base=1e9, drift=0.0, vol=0.12).rename("assets")
    cols["revenue"] = _fund(2, base=6e8, drift=0.0, vol=0.18).rename("revenue")
    cols["liabilities"] = _fund(3, base=5e8, drift=0.0, vol=0.15).rename("liabilities")
    cols["cashneq"] = _fund(4, base=1.5e8, drift=0.0, vol=0.2).rename("cashneq")
    cols["opex"] = _fund(5, base=5e8, drift=0.0, vol=0.15).rename("opex")
    cols["workingcapital"] = _fund(6, base=2e8, drift=0.0, vol=0.22, allow_neg=True).rename("workingcapital")
    cols["retearn"] = _fund(7, base=3e8, drift=0.0, vol=0.25, allow_neg=True).rename("retearn")
    cols["ebit"] = _fund(8, base=1.2e8, drift=-0.02, vol=0.35, allow_neg=True).rename("ebit")
    cols["equity"] = _fund(9, base=4e8, drift=-0.03, vol=0.35, allow_neg=True).rename("equity")
    return cols


if __name__ == "__main__":
    cols = _build_synth()

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

    print("OK f37_distress_risk_altman_base_076_150_claude: %d features pass" % n_features)
