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

HURDLE = 0.08  # fixed cost-of-capital / hurdle rate for value-creation spreads


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


def _pctrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, k):
    return s.diff(k) / float(k)


# ===== folder domain primitives (capital-returns quality) =====
def _f50_roic_spread(roic):
    # value creation: ROIC above/below the fixed hurdle
    return roic - HURDLE


def _f50_tangible_roic(ebit, tangibles):
    # return on tangible capital only (excludes intangible goodwill bloat)
    return ebit / tangibles.replace(0, np.nan)


def _f50_assetturn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f50_equityturn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _f50_invcap_turn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _f50_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f50_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f50_returns_disp(roic, roa, ros):
    stacked = pd.concat([roic, roa, ros], axis=1)
    return stacked.std(axis=1)


def _f50_returns_mean(roic, roa, ros):
    stacked = pd.concat([roic, roa, ros], axis=1)
    return stacked.mean(axis=1)


def _f50_sink_flag(roic, w):
    # persistent value destruction: ROIC below the cost-of-capital hurdle over the window
    below = (roic < HURDLE).astype(float)
    return below.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- ROIC level / spread / percentile / trend (v001-v015) ---

# ROIC level vs hurdle (raw value-creation spread)
def f50rq_f50_capital_returns_quality_roicspr_base_v001_signal(roic):
    b = _f50_roic_spread(roic)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level, z-scored vs its own 252d history (de-meaned quality)
def f50rq_f50_capital_returns_quality_roicz_252d_base_v002_signal(roic):
    b = _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC percentile vs its own 504d history (where in the cycle of returns)
def f50rq_f50_capital_returns_quality_roicpct_504d_base_v003_signal(roic):
    b = _pctrank(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC smoothed level (persistent return-on-capital, 126d EMA)
def f50rq_f50_capital_returns_quality_roicema_126d_base_v004_signal(roic):
    b = roic.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-creation spread momentum, squashed: change in above-hurdle excess return over a quarter (compounder acceleration)
def f50rq_f50_capital_returns_quality_roicsprtanh_base_v005_signal(roic):
    spr = _f50_roic_spread(roic)
    chg = spr - spr.shift(63)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year ROIC clears the hurdle (durable value-creation regime)
def f50rq_f50_capital_returns_quality_roicabovehurd_252d_base_v006_signal(roic):
    above = (roic >= HURDLE).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend: 63d change in the smoothed ROIC level
def f50rq_f50_capital_returns_quality_roictrend_63d_base_v007_signal(roic):
    sm = roic.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend over a year (252d change of level)
def f50rq_f50_capital_returns_quality_roictrend_252d_base_v008_signal(roic):
    b = roic - roic.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-creation spread scaled by its own volatility (risk-adjusted excess return)
def f50rq_f50_capital_returns_quality_roicsprrisk_base_v009_signal(roic):
    spr = _f50_roic_spread(roic)
    vol = _std(roic, 126)
    b = spr / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC displacement from its slow EMA (acceleration of capital quality)
def f50rq_f50_capital_returns_quality_roicdisp_base_v010_signal(roic):
    b = roic - roic.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-destruction depth: how far below hurdle, clipped (capital-sink magnitude)
def f50rq_f50_capital_returns_quality_roicdestroy_base_v011_signal(roic):
    b = (HURDLE - roic).clip(lower=0.0).ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level relative to its 252d min (recovery of capital quality off the trough)
def f50rq_f50_capital_returns_quality_roicrecov_252d_base_v012_signal(roic):
    lo = roic.rolling(252, min_periods=126).min()
    b = roic - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC erosion from its 504d peak, normalized by its own volatility (return-quality drawdown in sigma units)
def f50rq_f50_capital_returns_quality_roicerode_504d_base_v013_signal(roic):
    hi = roic.rolling(504, min_periods=252).max()
    vol = _std(roic, 126)
    b = (roic - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC mid-band convex skew within its 252d range (return-quality positioning, sign x magnitude squared)
def f50rq_f50_capital_returns_quality_roicrngpos_504d_base_v014_signal(roic):
    hi = roic.rolling(252, min_periods=126).max()
    lo = roic.rolling(252, min_periods=126).min()
    pos = (roic - lo) / (hi - lo).replace(0, np.nan) - 0.5
    conv = np.sign(pos) * (pos ** 2) * 4.0
    b = conv - conv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC year-over-year acceleration: trend now vs trend a year ago
def f50rq_f50_capital_returns_quality_roicaccel_base_v015_signal(roic):
    tr = roic - roic.shift(126)
    b = tr - tr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROA level / spread / percentile / trend (v016-v028) ---

# ROA level, smoothed (asset-level profitability)
def f50rq_f50_capital_returns_quality_roaema_126d_base_v016_signal(roa):
    b = roa.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA z-scored vs its own 252d history
def f50rq_f50_capital_returns_quality_roaz_252d_base_v017_signal(roa):
    b = _z(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA percentile vs its own 504d history
def f50rq_f50_capital_returns_quality_roapct_504d_base_v018_signal(roa):
    b = _pctrank(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA above its own 504d median frequency (durable above-trend asset profitability regime)
def f50rq_f50_capital_returns_quality_roaabove_252d_base_v019_signal(roa):
    med = roa.rolling(504, min_periods=126).median()
    above = (roa >= med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trend over a year (level change)
def f50rq_f50_capital_returns_quality_roatrend_252d_base_v020_signal(roa):
    b = roa - roa.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trend over a quarter (smoothed change)
def f50rq_f50_capital_returns_quality_roatrend_63d_base_v021_signal(roa):
    sm = roa.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA weak-regime persistence: fraction of last year ROA below its 504d lower-quartile (asset capital-sink)
def f50rq_f50_capital_returns_quality_roaneg_252d_base_v022_signal(roa):
    q1 = roa.rolling(504, min_periods=126).quantile(0.25)
    weak = (roa < q1).astype(float)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA risk-adjusted level (mean over its own dispersion, asset-return Sharpe-like)
def f50rq_f50_capital_returns_quality_roasharpe_base_v023_signal(roa):
    m = _mean(roa, 252)
    sd = _std(roa, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA displacement from slow EMA (asset-return acceleration)
def f50rq_f50_capital_returns_quality_roadisp_base_v024_signal(roa):
    b = roa - roa.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA erosion from its 504d peak, normalized by its own volatility (asset-return drawdown in sigma units)
def f50rq_f50_capital_returns_quality_roaerode_504d_base_v025_signal(roa):
    hi = roa.rolling(504, min_periods=252).max()
    vol = _std(roa, 126)
    b = (roa - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA mid-band convex skew within its 252d range, monthly change (asset-return positioning momentum)
def f50rq_f50_capital_returns_quality_roarngpos_504d_base_v026_signal(roa):
    hi = roa.rolling(252, min_periods=126).max()
    lo = roa.rolling(252, min_periods=126).min()
    pos = (roa - lo) / (hi - lo).replace(0, np.nan) - 0.5
    conv = np.sign(pos) * (pos ** 2) * 4.0
    b = conv - conv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA squashed level (bounded asset profitability)
def f50rq_f50_capital_returns_quality_roatanh_base_v027_signal(roa):
    sm = roa.ewm(span=63, min_periods=21).mean()
    b = np.tanh(12.0 * sm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA recovery off its 252d trough
def f50rq_f50_capital_returns_quality_roarecov_252d_base_v028_signal(roa):
    lo = roa.rolling(252, min_periods=126).min()
    b = roa - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROS level / spread / percentile / trend (v029-v039) ---

# ROS level, smoothed (margin-side return quality)
def f50rq_f50_capital_returns_quality_rosema_126d_base_v029_signal(ros):
    b = ros.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS z-scored vs its own 252d history
def f50rq_f50_capital_returns_quality_rosz_252d_base_v030_signal(ros):
    b = _z(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS percentile vs its own 504d history
def f50rq_f50_capital_returns_quality_rospct_504d_base_v031_signal(ros):
    b = _pctrank(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS trend over a year
def f50rq_f50_capital_returns_quality_rostrend_252d_base_v032_signal(ros):
    b = ros - ros.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS trend over a quarter (smoothed)
def f50rq_f50_capital_returns_quality_rostrend_63d_base_v033_signal(ros):
    sm = ros.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS weak-margin persistence: fraction of last year ROS below its 504d lower-quartile (margin distress)
def f50rq_f50_capital_returns_quality_rosneg_252d_base_v034_signal(ros):
    q1 = ros.rolling(504, min_periods=126).quantile(0.25)
    weak = (ros < q1).astype(float)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS risk-adjusted level (margin stability quality)
def f50rq_f50_capital_returns_quality_rossharpe_base_v035_signal(ros):
    m = _mean(ros, 252)
    sd = _std(ros, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS erosion from its 504d peak, normalized by its own volatility (margin drawdown in sigma units)
def f50rq_f50_capital_returns_quality_roserode_504d_base_v036_signal(ros):
    hi = ros.rolling(504, min_periods=252).max()
    vol = _std(ros, 126)
    b = (ros - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS mid-band convex skew within its 252d range, monthly change (margin positioning momentum)
def f50rq_f50_capital_returns_quality_rosrngpos_504d_base_v037_signal(ros):
    hi = ros.rolling(252, min_periods=126).max()
    lo = ros.rolling(252, min_periods=126).min()
    pos = (ros - lo) / (hi - lo).replace(0, np.nan) - 0.5
    conv = np.sign(pos) * (pos ** 2) * 4.0
    b = conv - conv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS squashed level (bounded margin quality)
def f50rq_f50_capital_returns_quality_rostanh_base_v038_signal(ros):
    sm = ros.ewm(span=63, min_periods=21).mean()
    b = np.tanh(10.0 * sm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS displacement from slow EMA (margin-return acceleration)
def f50rq_f50_capital_returns_quality_rosdisp_base_v039_signal(ros):
    b = ros - ros.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- asset turnover (revenue/assets) level & trend (v040-v047) ---

# asset turnover level (revenue per dollar of assets)
def f50rq_f50_capital_returns_quality_assetturn_base_v040_signal(revenue, assets):
    b = _f50_assetturn(revenue, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover displacement from its slow EMA (capital-efficiency acceleration)
def f50rq_f50_capital_returns_quality_assetturnema_base_v041_signal(revenue, assets):
    at = _f50_assetturn(revenue, assets)
    b = at - at.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover z-scored vs its own 252d history
def f50rq_f50_capital_returns_quality_assetturnz_252d_base_v042_signal(revenue, assets):
    at = _f50_assetturn(revenue, assets)
    b = _z(at, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover percentile vs its 504d history
def f50rq_f50_capital_returns_quality_assetturnpct_504d_base_v043_signal(revenue, assets):
    at = _f50_assetturn(revenue, assets)
    b = _pctrank(at, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover trend over a year
def f50rq_f50_capital_returns_quality_assetturntrend_252d_base_v044_signal(revenue, assets):
    at = _f50_assetturn(revenue, assets)
    b = at - at.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover trend over a quarter (smoothed)
def f50rq_f50_capital_returns_quality_assetturntrend_63d_base_v045_signal(revenue, assets):
    at = _f50_assetturn(revenue, assets)
    sm = at.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported asset-turnover column z-scored (uses the unused assetturnover input directly)
def f50rq_f50_capital_returns_quality_atcolz_252d_base_v046_signal(assetturnover):
    b = _z(assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap between reported assetturnover and computed revenue/assets (capital-base drift)
def f50rq_f50_capital_returns_quality_atgap_base_v047_signal(assetturnover, revenue, assets):
    computed = _f50_assetturn(revenue, assets)
    b = assetturnover - computed
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DuPont-style return decomposition (ros x turnover) (v048-v052) ---

# DuPont ROA reconstruction: ROS x asset turnover (margin x efficiency)
def f50rq_f50_capital_returns_quality_dupont_base_v048_signal(ros, revenue, assets):
    at = _f50_assetturn(revenue, assets)
    b = ros * at
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont gap: reconstructed ROA vs reported ROA (quality-of-returns consistency)
def f50rq_f50_capital_returns_quality_dupontgap_base_v049_signal(ros, revenue, assets, roa):
    at = _f50_assetturn(revenue, assets)
    recon = ros * at
    b = recon - roa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-vs-turnover tilt: is return driven by margin or by capital churn?
def f50rq_f50_capital_returns_quality_marginturntilt_base_v050_signal(ros, assetturnover):
    rs = _z(ros, 252)
    at = _z(assetturnover, 252)
    b = rs - at
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont turnover-driver contribution: ROA change attributable to asset-turnover change (capital-efficiency driver isolated)
def f50rq_f50_capital_returns_quality_duponttrend_base_v051_signal(ros, assetturnover):
    at_chg = assetturnover - assetturnover.shift(252)
    b = ros * at_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont reconstructed-ROA percentile vs 504d history
def f50rq_f50_capital_returns_quality_dupontpct_base_v052_signal(ros, assetturnover):
    recon = ros * assetturnover
    b = _pctrank(recon, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tangible-ROIC (ebit/tangibles, excl intangibles) (v053-v060) ---

# tangible return on capital level (ebit per tangible asset)
def f50rq_f50_capital_returns_quality_tangroic_base_v053_signal(ebit, tangibles):
    b = _f50_tangible_roic(ebit, tangibles)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC smoothed
def f50rq_f50_capital_returns_quality_tangroicema_base_v054_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = tr.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC above its own 504d median frequency (durable hard-asset return regime)
def f50rq_f50_capital_returns_quality_tangroicabove_base_v055_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    med = tr.rolling(504, min_periods=126).median()
    above = (tr >= med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC minus reported ROIC (intangible-return premium/drag)
def f50rq_f50_capital_returns_quality_tangvsroic_base_v056_signal(ebit, tangibles, roic):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = tr - roic
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC z-scored vs its 252d history
def f50rq_f50_capital_returns_quality_tangroicz_base_v057_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = _z(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC trend over a year
def f50rq_f50_capital_returns_quality_tangroictrend_base_v058_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = tr - tr.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin level (ebit/revenue) — operating return per sales dollar
def f50rq_f50_capital_returns_quality_ebitmargin_base_v059_signal(ebit, revenue):
    b = ebit / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-return leverage tilt: EBIT-on-equity minus EBIT-on-invested-capital (financial-leverage return premium)
def f50rq_f50_capital_returns_quality_ebitoneq_base_v060_signal(ebit, equity, invcap):
    roe_op = ebit / equity.replace(0, np.nan)
    roic_op = ebit / invcap.replace(0, np.nan)
    b = roe_op - roic_op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- equity turnover & invested-capital turnover (v061-v066) ---

# equity turnover level (revenue per dollar of equity)
def f50rq_f50_capital_returns_quality_eqturn_base_v061_signal(revenue, equity):
    b = _f50_equityturn(revenue, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover z-scored vs its 252d history
def f50rq_f50_capital_returns_quality_eqturnz_base_v062_signal(revenue, equity):
    et = _f50_equityturn(revenue, equity)
    b = _z(et, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover trend over a year
def f50rq_f50_capital_returns_quality_eqturntrend_base_v063_signal(revenue, equity):
    et = _f50_equityturn(revenue, equity)
    b = et - et.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover level (revenue per dollar of invested capital)
def f50rq_f50_capital_returns_quality_invcapturn_base_v064_signal(revenue, invcap):
    b = _f50_invcap_turn(revenue, invcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover percentile vs 504d history
def f50rq_f50_capital_returns_quality_invcapturnpct_base_v065_signal(revenue, invcap):
    it = _f50_invcap_turn(revenue, invcap)
    b = _pctrank(it, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-asset turnover spread (leverage tilt in capital churn)
def f50rq_f50_capital_returns_quality_eqassetturnspr_base_v066_signal(revenue, equity, assets):
    et = _f50_equityturn(revenue, equity)
    at = _f50_assetturn(revenue, assets)
    b = et - at
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- capital-sink flag & returns dispersion & intangible drag (v067-v075) ---

# capital-sink flag: persistent ROIC<hurdle AND rising invested capital (value destruction funded by more capital)
def f50rq_f50_capital_returns_quality_capsink_base_v067_signal(roic, invcap):
    sink = _f50_sink_flag(roic, 252)
    invtrend = (invcap / invcap.shift(252).replace(0, np.nan) - 1.0).clip(lower=0)
    b = sink * invtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink severity: depth below hurdle x invested-capital growth
def f50rq_f50_capital_returns_quality_capsinksev_base_v068_signal(roic, invcap):
    deficit = (HURDLE - roic).clip(lower=0)
    invgrow = (invcap / invcap.shift(126).replace(0, np.nan) - 1.0)
    b = deficit * invgrow.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns dispersion across roic/roa/ros (disagreement among return measures)
def f50rq_f50_capital_returns_quality_retdisp_base_v069_signal(roic, roa, ros):
    b = _f50_returns_disp(roic, roa, ros)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns dispersion smoothed (instability of return-quality signal)
def f50rq_f50_capital_returns_quality_retdispema_base_v070_signal(roic, roa, ros):
    d = _f50_returns_disp(roic, roa, ros)
    b = d.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return level: mean of roic/roa/ros, z-scored (overall quality factor)
def f50rq_f50_capital_returns_quality_retcompz_base_v071_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return spread above hurdle, squashed (overall compounder strength)
def f50rq_f50_capital_returns_quality_retcompspr_base_v072_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = np.tanh(8.0 * (m - HURDLE).ewm(span=63, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness drag: rising intangible share coinciding with deteriorating ROIC
# (interaction of intangible-share trend and ROIC trend — goodwill bloat masking declining returns)
def f50rq_f50_capital_returns_quality_intangdrag_base_v073_signal(intangibles, assets, roic):
    share = _f50_intang_share(intangibles, assets)
    share_trend = share - share.shift(126)
    roic_trend = roic - roic.shift(126)
    b = share_trend * (-roic_trend)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share level z-scored (asset-mix bloat vs hard assets)
def f50rq_f50_capital_returns_quality_intangsharez_base_v074_signal(intangibles, assets):
    share = _f50_intang_share(intangibles, assets)
    b = _z(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share weighted by ROA (hard-asset earning power)
def f50rq_f50_capital_returns_quality_tangearn_base_v075_signal(tangibles, assets, roa):
    share = _f50_tang_share(tangibles, assets)
    b = share * roa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50rq_f50_capital_returns_quality_roicspr_base_v001_signal,
    f50rq_f50_capital_returns_quality_roicz_252d_base_v002_signal,
    f50rq_f50_capital_returns_quality_roicpct_504d_base_v003_signal,
    f50rq_f50_capital_returns_quality_roicema_126d_base_v004_signal,
    f50rq_f50_capital_returns_quality_roicsprtanh_base_v005_signal,
    f50rq_f50_capital_returns_quality_roicabovehurd_252d_base_v006_signal,
    f50rq_f50_capital_returns_quality_roictrend_63d_base_v007_signal,
    f50rq_f50_capital_returns_quality_roictrend_252d_base_v008_signal,
    f50rq_f50_capital_returns_quality_roicsprrisk_base_v009_signal,
    f50rq_f50_capital_returns_quality_roicdisp_base_v010_signal,
    f50rq_f50_capital_returns_quality_roicdestroy_base_v011_signal,
    f50rq_f50_capital_returns_quality_roicrecov_252d_base_v012_signal,
    f50rq_f50_capital_returns_quality_roicerode_504d_base_v013_signal,
    f50rq_f50_capital_returns_quality_roicrngpos_504d_base_v014_signal,
    f50rq_f50_capital_returns_quality_roicaccel_base_v015_signal,
    f50rq_f50_capital_returns_quality_roaema_126d_base_v016_signal,
    f50rq_f50_capital_returns_quality_roaz_252d_base_v017_signal,
    f50rq_f50_capital_returns_quality_roapct_504d_base_v018_signal,
    f50rq_f50_capital_returns_quality_roaabove_252d_base_v019_signal,
    f50rq_f50_capital_returns_quality_roatrend_252d_base_v020_signal,
    f50rq_f50_capital_returns_quality_roatrend_63d_base_v021_signal,
    f50rq_f50_capital_returns_quality_roaneg_252d_base_v022_signal,
    f50rq_f50_capital_returns_quality_roasharpe_base_v023_signal,
    f50rq_f50_capital_returns_quality_roadisp_base_v024_signal,
    f50rq_f50_capital_returns_quality_roaerode_504d_base_v025_signal,
    f50rq_f50_capital_returns_quality_roarngpos_504d_base_v026_signal,
    f50rq_f50_capital_returns_quality_roatanh_base_v027_signal,
    f50rq_f50_capital_returns_quality_roarecov_252d_base_v028_signal,
    f50rq_f50_capital_returns_quality_rosema_126d_base_v029_signal,
    f50rq_f50_capital_returns_quality_rosz_252d_base_v030_signal,
    f50rq_f50_capital_returns_quality_rospct_504d_base_v031_signal,
    f50rq_f50_capital_returns_quality_rostrend_252d_base_v032_signal,
    f50rq_f50_capital_returns_quality_rostrend_63d_base_v033_signal,
    f50rq_f50_capital_returns_quality_rosneg_252d_base_v034_signal,
    f50rq_f50_capital_returns_quality_rossharpe_base_v035_signal,
    f50rq_f50_capital_returns_quality_roserode_504d_base_v036_signal,
    f50rq_f50_capital_returns_quality_rosrngpos_504d_base_v037_signal,
    f50rq_f50_capital_returns_quality_rostanh_base_v038_signal,
    f50rq_f50_capital_returns_quality_rosdisp_base_v039_signal,
    f50rq_f50_capital_returns_quality_assetturn_base_v040_signal,
    f50rq_f50_capital_returns_quality_assetturnema_base_v041_signal,
    f50rq_f50_capital_returns_quality_assetturnz_252d_base_v042_signal,
    f50rq_f50_capital_returns_quality_assetturnpct_504d_base_v043_signal,
    f50rq_f50_capital_returns_quality_assetturntrend_252d_base_v044_signal,
    f50rq_f50_capital_returns_quality_assetturntrend_63d_base_v045_signal,
    f50rq_f50_capital_returns_quality_atcolz_252d_base_v046_signal,
    f50rq_f50_capital_returns_quality_atgap_base_v047_signal,
    f50rq_f50_capital_returns_quality_dupont_base_v048_signal,
    f50rq_f50_capital_returns_quality_dupontgap_base_v049_signal,
    f50rq_f50_capital_returns_quality_marginturntilt_base_v050_signal,
    f50rq_f50_capital_returns_quality_duponttrend_base_v051_signal,
    f50rq_f50_capital_returns_quality_dupontpct_base_v052_signal,
    f50rq_f50_capital_returns_quality_tangroic_base_v053_signal,
    f50rq_f50_capital_returns_quality_tangroicema_base_v054_signal,
    f50rq_f50_capital_returns_quality_tangroicabove_base_v055_signal,
    f50rq_f50_capital_returns_quality_tangvsroic_base_v056_signal,
    f50rq_f50_capital_returns_quality_tangroicz_base_v057_signal,
    f50rq_f50_capital_returns_quality_tangroictrend_base_v058_signal,
    f50rq_f50_capital_returns_quality_ebitmargin_base_v059_signal,
    f50rq_f50_capital_returns_quality_ebitoneq_base_v060_signal,
    f50rq_f50_capital_returns_quality_eqturn_base_v061_signal,
    f50rq_f50_capital_returns_quality_eqturnz_base_v062_signal,
    f50rq_f50_capital_returns_quality_eqturntrend_base_v063_signal,
    f50rq_f50_capital_returns_quality_invcapturn_base_v064_signal,
    f50rq_f50_capital_returns_quality_invcapturnpct_base_v065_signal,
    f50rq_f50_capital_returns_quality_eqassetturnspr_base_v066_signal,
    f50rq_f50_capital_returns_quality_capsink_base_v067_signal,
    f50rq_f50_capital_returns_quality_capsinksev_base_v068_signal,
    f50rq_f50_capital_returns_quality_retdisp_base_v069_signal,
    f50rq_f50_capital_returns_quality_retdispema_base_v070_signal,
    f50rq_f50_capital_returns_quality_retcompz_base_v071_signal,
    f50rq_f50_capital_returns_quality_retcompspr_base_v072_signal,
    f50rq_f50_capital_returns_quality_intangdrag_base_v073_signal,
    f50rq_f50_capital_returns_quality_intangsharez_base_v074_signal,
    f50rq_f50_capital_returns_quality_tangearn_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CAPITAL_RETURNS_QUALITY_REGISTRY_001_075 = REGISTRY


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

    roic = _fund(1, base=0.12, drift=0.0, vol=0.10, allow_neg=True).rename("roic")
    roa = _fund(2, base=0.08, drift=0.0, vol=0.09, allow_neg=True).rename("roa")
    ros = _fund(3, base=0.10, drift=0.0, vol=0.11, allow_neg=True).rename("ros")
    ebit = _fund(4, base=5e7, drift=0.0, vol=0.12, allow_neg=True).rename("ebit")
    assetturnover = (_fund(5, base=0.7, drift=0.0, vol=0.07) + 0.1).rename("assetturnover")
    invcap = _fund(6, base=8e8, drift=0.01, vol=0.05).rename("invcap")
    equity = _fund(7, base=6e8, drift=0.01, vol=0.05).rename("equity")
    intangibles = _fund(8, base=2e8, drift=0.0, vol=0.06).rename("intangibles")
    tangibles = _fund(9, base=7e8, drift=0.005, vol=0.05).rename("tangibles")
    revenue = _fund(10, base=9e8, drift=0.01, vol=0.06).rename("revenue")
    assets = _fund(11, base=1.2e9, drift=0.01, vol=0.05).rename("assets")

    cols = {"roic": roic, "roa": roa, "ros": ros, "ebit": ebit,
            "assetturnover": assetturnover, "invcap": invcap, "equity": equity,
            "intangibles": intangibles, "tangibles": tangibles,
            "revenue": revenue, "assets": assets}

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

    print("OK f50_capital_returns_quality_base_001_075_claude: %d features pass" % n_features)
