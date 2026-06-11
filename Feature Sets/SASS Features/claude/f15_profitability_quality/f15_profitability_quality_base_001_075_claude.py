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


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


# ===== folder domain primitives (profitability quality levels) =====
def _f15_gross_margin(revenue, gp):
    return gp / revenue.replace(0, np.nan)


def _f15_op_margin(revenue, opinc):
    return opinc / revenue.replace(0, np.nan)


def _f15_net_margin(revenue, netinc):
    return netinc / revenue.replace(0, np.nan)


def _f15_ebitda_margin(revenue, ebitda):
    return ebitda / revenue.replace(0, np.nan)


def _f15_ebit_margin(revenue, ebit):
    return ebit / revenue.replace(0, np.nan)


def _f15_roe(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _f15_roa(netinc, assets):
    return netinc / assets.replace(0, np.nan)


def _f15_roic_proxy(opinc, equity, assets):
    # NOPAT-ish (opinc as operating return) over invested capital proxy (equity + 0.5*assets-equity-ish)
    invcap = (equity + 0.4 * (assets - equity)).replace(0, np.nan)
    return opinc / invcap


def _f15_gp_to_assets(gp, assets):
    # Novy-Marx gross profitability
    return gp / assets.replace(0, np.nan)


def _f15_ros(revenue, opinc):
    return opinc / revenue.replace(0, np.nan)


def _f15_asset_turn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


# ============================================================
# --- gross margin level family ---
def f15pq_f15_profitability_quality_gm_lvl_63d_base_v001_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = _mean(gm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gm_z_252d_base_v002_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = _z(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gm_rank_504d_base_v003_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = _rank(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating margin level family ---
def f15pq_f15_profitability_quality_om_lvl_63d_base_v004_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    b = _mean(om, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_om_z_252d_base_v005_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    b = _z(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_om_rank_504d_base_v006_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    b = _rank(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net margin level family ---
def f15pq_f15_profitability_quality_nm_lvl_63d_base_v007_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = _mean(nm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nm_z_252d_base_v008_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = _z(nm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nm_rank_504d_base_v009_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = _rank(nm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin level family ---
def f15pq_f15_profitability_quality_em_lvl_63d_base_v010_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    b = _mean(em, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_em_z_252d_base_v011_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    b = _z(em, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emdisp_126d_base_v012_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    b = em - _ewm(em, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit margin level family ---
def f15pq_f15_profitability_quality_ebm_lvl_63d_base_v013_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    b = _mean(ebm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebm_z_252d_base_v014_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    b = _z(ebm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebm_rank_252d_base_v015_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    b = _rank(ebm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE family ---
def f15pq_f15_profitability_quality_roe_lvl_63d_base_v016_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    b = _mean(roe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roe_z_252d_base_v017_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    b = _z(roe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roe_rank_504d_base_v018_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    b = _rank(roe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROA family ---
def f15pq_f15_profitability_quality_roa_lvl_63d_base_v019_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _mean(roa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roa_z_252d_base_v020_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _z(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roa_ewm_126d_base_v021_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _ewm(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROIC proxy family ---
# ROIC level relative to its own deviation from trailing mean (de-trended capital return)
def f15pq_f15_profitability_quality_roic_lvl_63d_base_v022_signal(opinc, equity, assets):
    roic = _f15_roic_proxy(opinc, equity, assets)
    b = roic - roic.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-based ROIC z-score (pretax return on invested capital, distinct numerator)
def f15pq_f15_profitability_quality_ebitroic_z_252d_base_v023_signal(ebit, equity, assets):
    invcap = (equity + 0.4 * (assets - equity)).replace(0, np.nan)
    roic = ebit / invcap
    b = _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-based ROIC percentile (cash return on invested capital)
def f15pq_f15_profitability_quality_ebitdaroic_rank_504d_base_v024_signal(ebitda, equity, assets):
    invcap = (equity + 0.4 * (assets - equity)).replace(0, np.nan)
    roic = ebitda / invcap
    b = _rank(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profitability (gp/assets) family ---
def f15pq_f15_profitability_quality_gpa_lvl_63d_base_v025_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    b = _mean(gpa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpa_z_252d_base_v026_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    b = _z(gpa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpa_rank_504d_base_v027_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    b = _rank(gpa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-income retention of EBITDA (bottom-line capture of cash earnings) ---
def f15pq_f15_profitability_quality_niebitdacap_63d_base_v028_signal(netinc, ebitda):
    cap = netinc / ebitda.replace(0, np.nan)
    b = _ewm(cap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROS dispersion: rolling spread of operating return on sales (margin instability) ---
def f15pq_f15_profitability_quality_rosdisp_126d_base_v029_signal(revenue, opinc):
    ros = _f15_ros(revenue, opinc)
    hi = ros.rolling(126, min_periods=63).quantile(0.75)
    lo = ros.rolling(126, min_periods=63).quantile(0.25)
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin dispersion across types ---
def f15pq_f15_profitability_quality_mgndisp_63d_base_v030_signal(revenue, gp, opinc, netinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    stacked = pd.concat([gm, om, nm], axis=1)
    b = stacked.std(axis=1).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgndisp4_63d_base_v031_signal(revenue, gp, opinc, ebitda):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    em = _f15_ebitda_margin(revenue, ebitda)
    stacked = pd.concat([gm, om, em], axis=1)
    rng = stacked.max(axis=1) - stacked.min(axis=1)
    b = rng.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-to-net margin spread (cost discipline below the line) ---
def f15pq_f15_profitability_quality_gmnmspr_63d_base_v032_signal(revenue, gp, netinc):
    gm = _f15_gross_margin(revenue, gp)
    nm = _f15_net_margin(revenue, netinc)
    b = (gm - nm).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating-to-net margin spread (below operating line leakage) ---
def f15pq_f15_profitability_quality_omnmspr_z_252d_base_v033_signal(revenue, opinc, netinc):
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    b = _z(om - nm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- depreciation rate on asset base: (ebitda-ebit)/assets, de-trended (capital-consumption) ---
def f15pq_f15_profitability_quality_darate_252d_base_v034_signal(ebitda, ebit, assets):
    da = (ebitda - ebit) / assets.replace(0, np.nan)
    b = _z(da, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin stability (inverse coefficient of variation) ---
def f15pq_f15_profitability_quality_gmstab_252d_base_v035_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    m = _mean(gm, 252)
    sd = _std(gm, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omstab_252d_base_v036_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    m = _mean(om, 252)
    sd = _std(om, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roestab_252d_base_v037_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    m = _mean(roe, 252)
    sd = _std(roe, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin volatility (penalty) ---
def f15pq_f15_profitability_quality_nmvol_126d_base_v038_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = _std(nm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roavol_126d_base_v039_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _std(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DuPont leverage contribution: equity multiplier trend (capital-structure lever on ROE) ---
def f15pq_f15_profitability_quality_dupontlev_63d_base_v040_signal(netinc, assets, equity):
    nm_on_assets = netinc / assets.replace(0, np.nan)
    lev = assets / equity.replace(0, np.nan)
    contrib = nm_on_assets * (lev - 1.0)
    b = _z(contrib, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-to-operating conversion stability (inverse CV of opinc/gp pass-through) ---
def f15pq_f15_profitability_quality_opgpstab_252d_base_v041_signal(gp, opinc):
    conv = opinc / gp.replace(0, np.nan)
    m = _mean(conv, 252)
    sd = _std(conv, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-operating pass-through momentum (quarter-over-quarter change in opinc/gp)
def f15pq_f15_profitability_quality_opgpmom_63d_base_v042_signal(gp, opinc):
    conv = opinc / gp.replace(0, np.nan)
    sm = _mean(conv, 63)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-to-operating conversion (netinc/opinc) ---
def f15pq_f15_profitability_quality_netopconv_63d_base_v043_signal(opinc, netinc):
    conv = netinc / opinc.replace(0, np.nan)
    b = _mean(conv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profit per dollar of equity (capital-efficient gross profit) ---
def f15pq_f15_profitability_quality_gpequ_63d_base_v044_signal(gp, equity):
    r = gp / equity.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda return on assets ---
def f15pq_f15_profitability_quality_ebitdaroa_63d_base_v045_signal(ebitda, assets):
    r = ebitda / assets.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroa_z_252d_base_v046_signal(ebitda, assets):
    r = ebitda / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit return on equity ---
def f15pq_f15_profitability_quality_ebitroe_63d_base_v047_signal(ebit, equity):
    r = ebit / equity.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating income return on assets (ROA pre-tax) ---
def f15pq_f15_profitability_quality_oproa_63d_base_v048_signal(opinc, assets):
    r = opinc / assets.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproa_rank_504d_base_v049_signal(opinc, assets):
    r = opinc / assets.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- leverage amplification ratio: ROE / ROA (how much leverage multiplies asset returns) ---
def f15pq_f15_profitability_quality_levamp_252d_base_v050_signal(netinc, equity, assets):
    roe = _f15_roe(netinc, equity)
    roa = _f15_roa(netinc, assets)
    amp = roe / roa.replace(0, np.nan)
    b = _rank(amp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin breadth: count of margins above their own median ---
def f15pq_f15_profitability_quality_mgnbreadth_252d_base_v051_signal(revenue, gp, opinc, netinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    bg = (gm > gm.rolling(252, min_periods=126).median()).astype(float)
    bo = (om > om.rolling(252, min_periods=126).median()).astype(float)
    bn = (nm > nm.rolling(252, min_periods=126).median()).astype(float)
    raw = (bg + bo + bn) - 1.5
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite quality score: average rank of roe, roa, gpa ---
def f15pq_f15_profitability_quality_qualcomp_504d_base_v052_signal(netinc, equity, assets, gp):
    roe = _f15_roe(netinc, equity)
    roa = _f15_roa(netinc, assets)
    gpa = _f15_gp_to_assets(gp, assets)
    b = (_rank(roe, 504) + _rank(roa, 504) + _rank(gpa, 504)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profitability cushion: how far net margin sits above the breakeven line, smoothed ---
def f15pq_f15_profitability_quality_netcushion_252d_base_v053_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    cushion = np.sign(nm) * np.log1p(nm.abs())
    b = cushion.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin level x stability (quality-weighted margin) ---
def f15pq_f15_profitability_quality_gmqual_252d_base_v054_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    lvl = _mean(gm, 252)
    sd = _std(gm, 252)
    b = lvl / (1.0 + sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omqual_252d_base_v055_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    lvl = _mean(om, 252)
    sd = _std(om, 252)
    b = lvl / (1.0 + sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin level relative to its own 5y range position ---
def f15pq_f15_profitability_quality_gmrangepos_1260d_base_v056_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    hi = gm.rolling(1260, min_periods=504).max()
    lo = gm.rolling(1260, min_periods=504).min()
    b = (gm - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roerangepos_1260d_base_v057_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    hi = roe.rolling(1260, min_periods=504).max()
    lo = roe.rolling(1260, min_periods=504).min()
    b = (roe - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin stability (inverse cv) ---
def f15pq_f15_profitability_quality_emstab_252d_base_v058_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    m = _mean(em, 252)
    sd = _std(em, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-margin skewness over the trailing year (asymmetry of profitability) ---
def f15pq_f15_profitability_quality_nmskew_252d_base_v059_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = nm.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE excess over ROA, tanh-bounded (financial-leverage quality, decoupled from level) ---
def f15pq_f15_profitability_quality_roeexcesstanh_63d_base_v060_signal(netinc, equity, assets):
    roe = _f15_roe(netinc, equity)
    roa = _f15_roa(netinc, assets)
    spread = roe - roa
    detr = spread - spread.rolling(252, min_periods=126).mean()
    b = np.tanh(15.0 * detr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-profitability vs asset-turnover divergence (margin-led vs volume-led quality) ---
def f15pq_f15_profitability_quality_gpaturndiv_504d_base_v061_signal(gp, assets, revenue):
    gpa = _f15_gp_to_assets(gp, assets)
    at = _f15_asset_turn(revenue, assets)
    b = _rank(gpa, 504) - _rank(at, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating-expense load volatility: instability of below-gross cost burden ---
def f15pq_f15_profitability_quality_opexloadvol_126d_base_v062_signal(revenue, gp, opinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    load = (gm - om) / gm.replace(0, np.nan)
    b = _std(load, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net income return on invested capital proxy ---
def f15pq_f15_profitability_quality_niroic_63d_base_v063_signal(netinc, equity, assets):
    invcap = (equity + 0.4 * (assets - equity)).replace(0, np.nan)
    r = netinc / invcap
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income ROIC momentum (year-over-year change in return on invested capital)
def f15pq_f15_profitability_quality_niroicmom_252d_base_v064_signal(netinc, equity, assets):
    invcap = (equity + 0.4 * (assets - equity)).replace(0, np.nan)
    roic = netinc / invcap
    sm = _mean(roic, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin convexity: upper-vs-lower deviation of op margin ---
def f15pq_f15_profitability_quality_omconvex_252d_base_v065_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    med = om.rolling(252, min_periods=126).median()
    b = np.sign(om - med) * (om - med) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit return on assets (pretax operating quality) ---
def f15pq_f15_profitability_quality_ebitroa_63d_base_v066_signal(ebit, assets):
    r = ebit / assets.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroa_rank_504d_base_v067_signal(ebit, assets):
    r = ebit / assets.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- equity productivity momentum: de-trended revenue-per-equity (capital turnover shift) ---
def f15pq_f15_profitability_quality_revequz_252d_base_v068_signal(revenue, equity):
    r = revenue / equity.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite margin index (equal-weight of 5 margins) ---
def f15pq_f15_profitability_quality_mgnindex_63d_base_v069_signal(revenue, gp, opinc, netinc, ebitda):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    em = _f15_ebitda_margin(revenue, ebitda)
    idx = (gm + om + nm + em) / 4.0
    b = _mean(idx, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin-waterfall curvature: convexity of the gm->om->nm descent (cost concentration) ---
def f15pq_f15_profitability_quality_mgncurv_63d_base_v070_signal(revenue, gp, opinc, netinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    curv = (gm - 2.0 * om + nm)
    b = _z(curv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- roa driver mix shift: de-trended log-ratio of margin vs turnover drivers ---
def f15pq_f15_profitability_quality_roadrvshift_252d_base_v071_signal(revenue, netinc, assets):
    nm = _f15_net_margin(revenue, netinc)
    at = _f15_asset_turn(revenue, assets)
    bal = np.log(nm.abs().replace(0, np.nan)) - np.log(at.replace(0, np.nan))
    b = bal - bal.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-margin short-vs-long normal gap (recent margin vs structural margin) ---
def f15pq_f15_profitability_quality_gmnormgap_base_v072_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    short_norm = gm.rolling(63, min_periods=21).mean()
    long_norm = gm.rolling(504, min_periods=252).mean()
    b = (short_norm - long_norm) / long_norm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin percentile in 5y history ---
def f15pq_f15_profitability_quality_emrank_1260d_base_v073_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    b = _rank(em, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profitability quality gap: roic proxy minus net margin (capital vs sales quality) ---
def f15pq_f15_profitability_quality_roicvsnm_63d_base_v074_signal(revenue, opinc, netinc, equity, assets):
    roic = _f15_roic_proxy(opinc, equity, assets)
    nm = _f15_net_margin(revenue, netinc)
    b = (roic - nm).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside margin semi-deviation (penalize negative-margin episodes) ---
def f15pq_f15_profitability_quality_nmsemidev_252d_base_v075_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    med = nm.rolling(252, min_periods=126).median()
    downside = (nm - med).clip(upper=0)
    b = np.sqrt((downside ** 2).rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15pq_f15_profitability_quality_gm_lvl_63d_base_v001_signal,
    f15pq_f15_profitability_quality_gm_z_252d_base_v002_signal,
    f15pq_f15_profitability_quality_gm_rank_504d_base_v003_signal,
    f15pq_f15_profitability_quality_om_lvl_63d_base_v004_signal,
    f15pq_f15_profitability_quality_om_z_252d_base_v005_signal,
    f15pq_f15_profitability_quality_om_rank_504d_base_v006_signal,
    f15pq_f15_profitability_quality_nm_lvl_63d_base_v007_signal,
    f15pq_f15_profitability_quality_nm_z_252d_base_v008_signal,
    f15pq_f15_profitability_quality_nm_rank_504d_base_v009_signal,
    f15pq_f15_profitability_quality_em_lvl_63d_base_v010_signal,
    f15pq_f15_profitability_quality_em_z_252d_base_v011_signal,
    f15pq_f15_profitability_quality_emdisp_126d_base_v012_signal,
    f15pq_f15_profitability_quality_ebm_lvl_63d_base_v013_signal,
    f15pq_f15_profitability_quality_ebm_z_252d_base_v014_signal,
    f15pq_f15_profitability_quality_ebm_rank_252d_base_v015_signal,
    f15pq_f15_profitability_quality_roe_lvl_63d_base_v016_signal,
    f15pq_f15_profitability_quality_roe_z_252d_base_v017_signal,
    f15pq_f15_profitability_quality_roe_rank_504d_base_v018_signal,
    f15pq_f15_profitability_quality_roa_lvl_63d_base_v019_signal,
    f15pq_f15_profitability_quality_roa_z_252d_base_v020_signal,
    f15pq_f15_profitability_quality_roa_ewm_126d_base_v021_signal,
    f15pq_f15_profitability_quality_roic_lvl_63d_base_v022_signal,
    f15pq_f15_profitability_quality_ebitroic_z_252d_base_v023_signal,
    f15pq_f15_profitability_quality_ebitdaroic_rank_504d_base_v024_signal,
    f15pq_f15_profitability_quality_gpa_lvl_63d_base_v025_signal,
    f15pq_f15_profitability_quality_gpa_z_252d_base_v026_signal,
    f15pq_f15_profitability_quality_gpa_rank_504d_base_v027_signal,
    f15pq_f15_profitability_quality_niebitdacap_63d_base_v028_signal,
    f15pq_f15_profitability_quality_rosdisp_126d_base_v029_signal,
    f15pq_f15_profitability_quality_mgndisp_63d_base_v030_signal,
    f15pq_f15_profitability_quality_mgndisp4_63d_base_v031_signal,
    f15pq_f15_profitability_quality_gmnmspr_63d_base_v032_signal,
    f15pq_f15_profitability_quality_omnmspr_z_252d_base_v033_signal,
    f15pq_f15_profitability_quality_darate_252d_base_v034_signal,
    f15pq_f15_profitability_quality_gmstab_252d_base_v035_signal,
    f15pq_f15_profitability_quality_omstab_252d_base_v036_signal,
    f15pq_f15_profitability_quality_roestab_252d_base_v037_signal,
    f15pq_f15_profitability_quality_nmvol_126d_base_v038_signal,
    f15pq_f15_profitability_quality_roavol_126d_base_v039_signal,
    f15pq_f15_profitability_quality_dupontlev_63d_base_v040_signal,
    f15pq_f15_profitability_quality_opgpstab_252d_base_v041_signal,
    f15pq_f15_profitability_quality_opgpmom_63d_base_v042_signal,
    f15pq_f15_profitability_quality_netopconv_63d_base_v043_signal,
    f15pq_f15_profitability_quality_gpequ_63d_base_v044_signal,
    f15pq_f15_profitability_quality_ebitdaroa_63d_base_v045_signal,
    f15pq_f15_profitability_quality_ebitdaroa_z_252d_base_v046_signal,
    f15pq_f15_profitability_quality_ebitroe_63d_base_v047_signal,
    f15pq_f15_profitability_quality_oproa_63d_base_v048_signal,
    f15pq_f15_profitability_quality_oproa_rank_504d_base_v049_signal,
    f15pq_f15_profitability_quality_levamp_252d_base_v050_signal,
    f15pq_f15_profitability_quality_mgnbreadth_252d_base_v051_signal,
    f15pq_f15_profitability_quality_qualcomp_504d_base_v052_signal,
    f15pq_f15_profitability_quality_netcushion_252d_base_v053_signal,
    f15pq_f15_profitability_quality_gmqual_252d_base_v054_signal,
    f15pq_f15_profitability_quality_omqual_252d_base_v055_signal,
    f15pq_f15_profitability_quality_gmrangepos_1260d_base_v056_signal,
    f15pq_f15_profitability_quality_roerangepos_1260d_base_v057_signal,
    f15pq_f15_profitability_quality_emstab_252d_base_v058_signal,
    f15pq_f15_profitability_quality_nmskew_252d_base_v059_signal,
    f15pq_f15_profitability_quality_roeexcesstanh_63d_base_v060_signal,
    f15pq_f15_profitability_quality_gpaturndiv_504d_base_v061_signal,
    f15pq_f15_profitability_quality_opexloadvol_126d_base_v062_signal,
    f15pq_f15_profitability_quality_niroic_63d_base_v063_signal,
    f15pq_f15_profitability_quality_niroicmom_252d_base_v064_signal,
    f15pq_f15_profitability_quality_omconvex_252d_base_v065_signal,
    f15pq_f15_profitability_quality_ebitroa_63d_base_v066_signal,
    f15pq_f15_profitability_quality_ebitroa_rank_504d_base_v067_signal,
    f15pq_f15_profitability_quality_revequz_252d_base_v068_signal,
    f15pq_f15_profitability_quality_mgnindex_63d_base_v069_signal,
    f15pq_f15_profitability_quality_mgncurv_63d_base_v070_signal,
    f15pq_f15_profitability_quality_roadrvshift_252d_base_v071_signal,
    f15pq_f15_profitability_quality_gmnormgap_base_v072_signal,
    f15pq_f15_profitability_quality_emrank_1260d_base_v073_signal,
    f15pq_f15_profitability_quality_roicvsnm_63d_base_v074_signal,
    f15pq_f15_profitability_quality_nmsemidev_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_PROFITABILITY_QUALITY_REGISTRY_001_075 = REGISTRY


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
    revenue = _fund(1, n, base=1e9, drift=0.02, vol=0.04).rename("revenue")
    gp = _fund(2, n, base=4e8, drift=0.02, vol=0.05).rename("gp")
    opinc = _fund(3, n, base=2e8, drift=0.02, vol=0.06, allow_neg=True).rename("opinc")
    netinc = _fund(4, n, base=1.5e8, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")
    ebitda = _fund(5, n, base=3e8, drift=0.02, vol=0.05).rename("ebitda")
    ebit = _fund(6, n, base=2.2e8, drift=0.02, vol=0.06).rename("ebit")
    equity = _fund(7, n, base=2e9, drift=0.015, vol=0.04).rename("equity")
    assets = _fund(8, n, base=5e9, drift=0.015, vol=0.03).rename("assets")

    cols = {"revenue": revenue, "gp": gp, "opinc": opinc, "netinc": netinc,
            "ebitda": ebitda, "ebit": ebit, "equity": equity, "assets": assets}

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

    print("OK f15_profitability_quality_base_001_075_claude: %d features pass" % n_features)
