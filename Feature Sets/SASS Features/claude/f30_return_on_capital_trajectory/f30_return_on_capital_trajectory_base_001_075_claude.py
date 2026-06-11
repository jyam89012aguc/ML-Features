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


# ===== folder domain primitives (return-on-capital trajectory) =====
def _f30_slope(s, w):
    # OLS slope of s vs time over window w (per-step trajectory of the ratio)
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xm = x.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        am = a.mean()
        return ((x - xm) * (a - am)).sum() / denom

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _f30_delta(s, w):
    # change vs prior window (improvement / ROIC-minus-prior)
    return s - s.shift(w)


def _f30_logchg(s, w):
    return np.log(s.abs().replace(0, np.nan)) - np.log(s.abs().shift(w).replace(0, np.nan))


def _f30_stability(s, w):
    # inverse coefficient of variation: high = stable & high return-on-capital
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f30_updays(s, w):
    # hit-rate of quarter-over-quarter improvement (improvement consistency)
    up = (s.diff(63) > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean()


def _f30_accel(s, w):
    # change-of-change as a level (improvement is accelerating)
    d = s - s.shift(w)
    return d - d.shift(w)


def _f30_ema_disp(s, span):
    return s - s.ewm(span=span, min_periods=max(2, span // 2)).mean()


def _f30_spread(a, b):
    return a - b


# ============================================================
# ROIC trend: OLS slope of ROIC over a year (improvement rate)
def f30rc_f30_return_on_capital_trajectory_roictrend_252d_base_v001_signal(roic):
    b = _f30_slope(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement vs prior year (ROIC-minus-prior, 252d)
def f30rc_f30_return_on_capital_trajectory_roicdelta_252d_base_v002_signal(roic):
    b = _f30_delta(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability over two years (mean / std)
def f30rc_f30_return_on_capital_trajectory_roicstab_504d_base_v003_signal(roic):
    b = _f30_stability(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE trend: OLS slope of ROE over a year
def f30rc_f30_return_on_capital_trajectory_roetrend_252d_base_v004_signal(roe):
    b = _f30_slope(roe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE improvement vs prior half-year
def f30rc_f30_return_on_capital_trajectory_roedelta_126d_base_v005_signal(roe):
    b = _f30_delta(roe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trend: OLS slope of ROA over a year
def f30rc_f30_return_on_capital_trajectory_roatrend_252d_base_v006_signal(roa):
    b = _f30_slope(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA improvement vs prior year
def f30rc_f30_return_on_capital_trajectory_roadelta_252d_base_v007_signal(roa):
    b = _f30_delta(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS (return on sales) trend over a year
def f30rc_f30_return_on_capital_trajectory_rostrend_252d_base_v008_signal(ros):
    b = _f30_slope(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS improvement vs prior half-year
def f30rc_f30_return_on_capital_trajectory_rosdelta_126d_base_v009_signal(ros):
    b = _f30_delta(ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trajectory normalized by its own volatility (signal-to-noise of the trend)
def f30rc_f30_return_on_capital_trajectory_roictsn_252d_base_v010_signal(roic):
    sl = _f30_slope(roic, 252)
    vol = _std(roic.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE stability over two years
def f30rc_f30_return_on_capital_trajectory_roestab_504d_base_v011_signal(roe):
    b = _f30_stability(roe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA stability over two years
def f30rc_f30_return_on_capital_trajectory_roastab_504d_base_v012_signal(roa):
    b = _f30_stability(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS stability over a year
def f30rc_f30_return_on_capital_trajectory_rosstab_252d_base_v013_signal(ros):
    b = _f30_stability(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-improvement consistency: hit-rate of QoQ ROIC gains over two years
def f30rc_f30_return_on_capital_trajectory_roicupdays_504d_base_v014_signal(roic):
    b = _f30_updays(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE improvement consistency over two years
def f30rc_f30_return_on_capital_trajectory_roeupdays_504d_base_v015_signal(roe):
    b = _f30_updays(roe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC acceleration as a level (improvement is accelerating, 126d steps)
def f30rc_f30_return_on_capital_trajectory_roicaccel_126d_base_v016_signal(roic):
    b = _f30_accel(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA acceleration as a level (126d steps)
def f30rc_f30_return_on_capital_trajectory_roaaccel_126d_base_v017_signal(roa):
    b = _f30_accel(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC displacement from its slow EMA (trajectory deviation)
def f30rc_f30_return_on_capital_trajectory_roicdisp_252d_base_v018_signal(roic):
    b = _f30_ema_disp(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE displacement from its slow EMA
def f30rc_f30_return_on_capital_trajectory_roedisp_252d_base_v019_signal(roe):
    b = _f30_ema_disp(roe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend rank vs its own two-year history (percentile of current slope)
def f30rc_f30_return_on_capital_trajectory_roictrank_504d_base_v020_signal(roic):
    sl = _f30_slope(roic, 126)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level z-scored vs own history (de-trended return-on-capital trajectory)
def f30rc_f30_return_on_capital_trajectory_roicz_252d_base_v021_signal(roic):
    b = _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE level z-scored vs own two-year history
def f30rc_f30_return_on_capital_trajectory_roez_504d_base_v022_signal(roe):
    b = _z(roe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA level z-scored vs own history
def f30rc_f30_return_on_capital_trajectory_roaz_252d_base_v023_signal(roa):
    b = _z(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROE spread trend (capital-structure quality drift)
def f30rc_f30_return_on_capital_trajectory_roicroespr_252d_base_v024_signal(roic, roe):
    spr = _f30_spread(roic, roe)
    b = _f30_slope(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-multiplier (ROE/ROA) trajectory z-score: is financial leverage uplift drifting
def f30rc_f30_return_on_capital_trajectory_levmult_252d_base_v025_signal(roe, roa):
    lev = _safe_div(roe, roa)
    b = _z(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROA spread level, smoothed (invested-capital advantage)
def f30rc_f30_return_on_capital_trajectory_roicroaspr_126d_base_v026_signal(roic, roa):
    spr = _f30_spread(roic, roa)
    b = _mean(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc-on-invcap ROIC proxy trend (rebuilt return-on-capital from raw inputs)
def f30rc_f30_return_on_capital_trajectory_nioic_252d_base_v027_signal(netinc, invcap):
    proxy = _safe_div(netinc, invcap)
    b = _f30_slope(proxy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc-on-equity ROE proxy trajectory z-scored vs own history (rebuilt ROE regime)
def f30rc_f30_return_on_capital_trajectory_nioe_252d_base_v028_signal(netinc, equity):
    proxy = _safe_div(netinc, equity)
    b = _z(proxy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth alongside ROIC (does capital base scale while returns hold)
def f30rc_f30_return_on_capital_trajectory_invcapgro_252d_base_v029_signal(invcap):
    b = _f30_logchg(invcap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth (capital base trajectory) over a year
def f30rc_f30_return_on_capital_trajectory_eqgro_252d_base_v030_signal(equity):
    b = _f30_logchg(equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital improvement funded by capital: ROIC delta x invcap growth sign
def f30rc_f30_return_on_capital_trajectory_roicfund_252d_base_v031_signal(roic, invcap):
    d = _f30_delta(roic, 252)
    g = _f30_logchg(invcap, 252)
    b = d * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS trend in volatility units (signal-to-noise of margin-return trajectory)
def f30rc_f30_return_on_capital_trajectory_rostsn_252d_base_v032_signal(ros):
    sl = _f30_slope(ros, 252)
    vol = _std(ros.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC short-vs-long slope spread (is the recent trajectory steeper than the long one)
def f30rc_f30_return_on_capital_trajectory_roicslspr_126v504_base_v033_signal(roic):
    s = _f30_slope(roic, 126)
    l = _f30_slope(roic, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE short-vs-long slope spread
def f30rc_f30_return_on_capital_trajectory_roeslspr_126v504_base_v034_signal(roe):
    s = _f30_slope(roe, 126)
    l = _f30_slope(roe, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return-on-capital momentum: avg of ROIC/ROE/ROA quarterly deltas
def f30rc_f30_return_on_capital_trajectory_compmom_63d_base_v035_signal(roic, roe, roa):
    d = (roic.diff(63) + roe.diff(63) + roa.diff(63)) / 3.0
    b = d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-metric return-on-capital dispersion (disagreement across roic/roe/roa/ros)
def f30rc_f30_return_on_capital_trajectory_xdisp_base_v036_signal(roic, roe, roa, ros):
    stacked = pd.concat([roic, roe, roa, ros], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature of cross-metric dispersion (is the quality profile convergence accelerating)
def f30rc_f30_return_on_capital_trajectory_xdispcurv_252d_base_v037_signal(roic, roe, roa, ros):
    stacked = pd.concat([roic, roe, roa, ros], axis=1)
    disp = stacked.std(axis=1)
    sl = _f30_slope(disp, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from its own trailing two-year peak (quality erosion)
def f30rc_f30_return_on_capital_trajectory_roicdd_504d_base_v038_signal(roic):
    peak = roic.rolling(504, min_periods=126).max()
    b = roic - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE drawdown from trailing two-year peak
def f30rc_f30_return_on_capital_trajectory_roedd_504d_base_v039_signal(roe):
    peak = roe.rolling(504, min_periods=126).max()
    b = roe - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC recovery off its trailing two-year trough (improvement from low base)
def f30rc_f30_return_on_capital_trajectory_roicrec_504d_base_v040_signal(roic):
    trough = roic.rolling(504, min_periods=126).min()
    b = roic - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of ROIC improvement (compress big moves, keep direction)
def f30rc_f30_return_on_capital_trajectory_roicsignmag_252d_base_v041_signal(roic):
    d = _f30_delta(roic, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE improvement percentile vs own history (rank of half-year quality-improvement)
def f30rc_f30_return_on_capital_trajectory_roedrank_504d_base_v042_signal(roe):
    d = _f30_delta(roe, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA improvement consistency over two years
def f30rc_f30_return_on_capital_trajectory_roaupdays_504d_base_v043_signal(roa):
    b = _f30_updays(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS improvement consistency over a year
def f30rc_f30_return_on_capital_trajectory_rosupdays_252d_base_v044_signal(ros):
    b = _f30_updays(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trajectory curvature: slope-of-slope (second-order quality trend, as level)
def f30rc_f30_return_on_capital_trajectory_roiccurv_126d_base_v045_signal(roic):
    sl = _f30_slope(roic, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC half-year improvement ranked vs own history
def f30rc_f30_return_on_capital_trajectory_roicdrank_504d_base_v046_signal(roic):
    d = _f30_delta(roic, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE level percentile vs own multi-year history (durable high-quality)
def f30rc_f30_return_on_capital_trajectory_roerank_504d_base_v047_signal(roe):
    b = _rank(roe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC year-over-year second difference (improvement vs improvement a year ago)
def f30rc_f30_return_on_capital_trajectory_roicyoy2_252d_base_v048_signal(roic):
    d = roic.diff(252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital quality slope: weighted blend of roic/roe/roa slopes
def f30rc_f30_return_on_capital_trajectory_qualslope_252d_base_v049_signal(roic, roe, roa):
    b = 0.5 * _f30_slope(roic, 252) + 0.3 * _f30_slope(roe, 252) + 0.2 * _f30_slope(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability minus ROA stability (which return base is steadier)
def f30rc_f30_return_on_capital_trajectory_stabspr_504d_base_v050_signal(roic, roa):
    b = _f30_stability(roic, 504) - _f30_stability(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc-on-invcap proxy minus reported roic (accounting-quality gap trajectory)
def f30rc_f30_return_on_capital_trajectory_roicgap_126d_base_v051_signal(netinc, invcap, roic):
    proxy = _safe_div(netinc, invcap)
    gap = proxy - roic
    b = _mean(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital efficiency drift: trend of (netinc / invcap) minus invcap growth (organic ROIC lift)
def f30rc_f30_return_on_capital_trajectory_roicorganic_252d_base_v052_signal(roic, invcap):
    g = _f30_logchg(invcap, 252)
    rsl = _f30_slope(roic, 126)
    b = np.sign(rsl) * rsl.abs() - 0.05 * g
    b = _rank(b, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE improvement net of equity growth (return improvement not from retained capital)
def f30rc_f30_return_on_capital_trajectory_roeexeq_252d_base_v053_signal(roe, equity):
    d = _f30_delta(roe, 252)
    g = _f30_logchg(equity, 252)
    b = d - 0.1 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS-vs-ROA spread trend (margin-driven vs asset-driven return shift)
def f30rc_f30_return_on_capital_trajectory_rosroaspr_252d_base_v054_signal(ros, roa):
    spr = _f30_spread(ros, roa)
    b = _f30_slope(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-weighted ROIC trend (recent quarters weighted more)
def f30rc_f30_return_on_capital_trajectory_roicewtrend_126d_base_v055_signal(roic):
    fast = roic.ewm(span=63, min_periods=21).mean()
    slow = roic.ewm(span=252, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE exponentially-weighted trend (fast minus slow EMA)
def f30rc_f30_return_on_capital_trajectory_roeewtrend_126d_base_v056_signal(roe):
    fast = roe.ewm(span=63, min_periods=21).mean()
    slow = roe.ewm(span=252, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement breadth: smoothed count of roic/roe/roa/ros rising over the year
def f30rc_f30_return_on_capital_trajectory_breadth_252d_base_v057_signal(roic, roe, roa, ros):
    up = (roic.diff(252) > 0).astype(float) + (roe.diff(252) > 0).astype(float) \
        + (roa.diff(252) > 0).astype(float) + (ros.diff(252) > 0).astype(float)
    b = (up - 2.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trajectory signal-to-noise
def f30rc_f30_return_on_capital_trajectory_roatsn_252d_base_v058_signal(roa):
    sl = _f30_slope(roa, 252)
    vol = _std(roa.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-equity volatility-of-volatility (instability of quality regime)
def f30rc_f30_return_on_capital_trajectory_roevov_252d_base_v059_signal(roe):
    vol = _std(roe.diff(), 126)
    b = _std(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC convexity: how much current ROIC exceeds the midpoint of its 504d range
def f30rc_f30_return_on_capital_trajectory_roicmid_504d_base_v060_signal(roic):
    hi = roic.rolling(504, min_periods=126).max()
    lo = roic.rolling(504, min_periods=126).min()
    mid = (hi + lo) / 2.0
    b = (roic - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont-style: ROE explained by ROA times leverage proxy (equity-driven uplift) trend
def f30rc_f30_return_on_capital_trajectory_dupont_252d_base_v061_signal(roe, roa):
    lev = _safe_div(roe, roa)
    b = _f30_slope(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement quality: 126d delta gated by improvement-consistency hit-rate
def f30rc_f30_return_on_capital_trajectory_roicdurable_504d_base_v062_signal(roic):
    d = _f30_delta(roic, 126)
    consist = _f30_updays(roic, 504) - 0.5
    b = d * consist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS level z-score (margin-return regime vs own history)
def f30rc_f30_return_on_capital_trajectory_rosz_252d_base_v063_signal(ros):
    b = _z(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC mean-reversion gap: level minus its long EMA, ranked
def f30rc_f30_return_on_capital_trajectory_roicmrgap_252d_base_v064_signal(roic):
    disp = _f30_ema_disp(roic, 252)
    b = _rank(disp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital trajectory asymmetry: upside vs downside semi-deviation of ROIC changes
def f30rc_f30_return_on_capital_trajectory_roicasym_252d_base_v065_signal(roic):
    d = roic.diff()
    up = d.clip(lower=0).rolling(252, min_periods=63).std()
    dn = (-d.clip(upper=0)).rolling(252, min_periods=63).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE trajectory asymmetry (improving vs deteriorating volatility)
def f30rc_f30_return_on_capital_trajectory_roeasym_252d_base_v066_signal(roe):
    d = roe.diff()
    up = d.clip(lower=0).rolling(252, min_periods=63).std()
    dn = (-d.clip(upper=0)).rolling(252, min_periods=63).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital-scaled netinc trajectory stability (rebuilt ROIC steadiness)
def f30rc_f30_return_on_capital_trajectory_nioicstab_504d_base_v067_signal(netinc, invcap):
    proxy = _safe_div(netinc, invcap)
    b = _f30_stability(proxy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS-on-ROIC trajectory ratio: is margin-return improving faster than capital-return
def f30rc_f30_return_on_capital_trajectory_rosoroicsl_252d_base_v068_signal(ros, roic):
    rsl = _f30_slope(ros, 252)
    csl = _f30_slope(roic, 252)
    b = np.tanh(rsl - csl) + 0.5 * np.sign(rsl) * np.sign(csl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite quality-improvement score: blend of breadth, ROIC slope, stability
def f30rc_f30_return_on_capital_trajectory_qualscore_252d_base_v069_signal(roic, roe, roa):
    sl = _z(_f30_slope(roic, 252), 252)
    breadth = (roic.diff(126) > 0).astype(float) + (roe.diff(126) > 0).astype(float) \
        + (roa.diff(126) > 0).astype(float)
    b = sl + (breadth - 1.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA improvement vs prior half-year, vol-normalized
def f30rc_f30_return_on_capital_trajectory_roadeltasn_126d_base_v070_signal(roa):
    d = _f30_delta(roa, 126)
    vol = _std(roa.diff(), 252)
    b = d / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS curvature (slope-of-slope of margin-return)
def f30rc_f30_return_on_capital_trajectory_roscurv_126d_base_v071_signal(ros):
    sl = _f30_slope(ros, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital improvement persistence: longest-run proxy of consecutive QoQ gains
def f30rc_f30_return_on_capital_trajectory_roicstreak_504d_base_v072_signal(roic):
    up = (roic.diff(63) > 0).astype(float)
    # exponentially decayed run intensity
    streak = up.ewm(span=126, min_periods=42).mean() * up.rolling(252, min_periods=63).sum()
    b = streak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-on-ROIC efficiency-of-improvement: do equity returns track invested-capital returns
def f30rc_f30_return_on_capital_trajectory_roeoroic_252d_base_v073_signal(roe, roic):
    ratio = _safe_div(roe, roic)
    b = _f30_delta(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon ROIC improvement agreement (sign agreement of 63/126/252 deltas)
def f30rc_f30_return_on_capital_trajectory_roicagree_base_v074_signal(roic):
    s1 = np.sign(roic.diff(63))
    s2 = np.sign(roic.diff(126))
    s3 = np.sign(roic.diff(252))
    b = (s1 + s2 + s3) / 3.0 * _f30_delta(roic, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital quality-improvement slope across all four metrics, vol-scaled
def f30rc_f30_return_on_capital_trajectory_allmetslope_252d_base_v075_signal(roic, roe, roa, ros):
    comp = (roic + roe + roa + ros) / 4.0
    sl = _f30_slope(comp, 252)
    vol = _std(comp.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rc_f30_return_on_capital_trajectory_roictrend_252d_base_v001_signal,
    f30rc_f30_return_on_capital_trajectory_roicdelta_252d_base_v002_signal,
    f30rc_f30_return_on_capital_trajectory_roicstab_504d_base_v003_signal,
    f30rc_f30_return_on_capital_trajectory_roetrend_252d_base_v004_signal,
    f30rc_f30_return_on_capital_trajectory_roedelta_126d_base_v005_signal,
    f30rc_f30_return_on_capital_trajectory_roatrend_252d_base_v006_signal,
    f30rc_f30_return_on_capital_trajectory_roadelta_252d_base_v007_signal,
    f30rc_f30_return_on_capital_trajectory_rostrend_252d_base_v008_signal,
    f30rc_f30_return_on_capital_trajectory_rosdelta_126d_base_v009_signal,
    f30rc_f30_return_on_capital_trajectory_roictsn_252d_base_v010_signal,
    f30rc_f30_return_on_capital_trajectory_roestab_504d_base_v011_signal,
    f30rc_f30_return_on_capital_trajectory_roastab_504d_base_v012_signal,
    f30rc_f30_return_on_capital_trajectory_rosstab_252d_base_v013_signal,
    f30rc_f30_return_on_capital_trajectory_roicupdays_504d_base_v014_signal,
    f30rc_f30_return_on_capital_trajectory_roeupdays_504d_base_v015_signal,
    f30rc_f30_return_on_capital_trajectory_roicaccel_126d_base_v016_signal,
    f30rc_f30_return_on_capital_trajectory_roaaccel_126d_base_v017_signal,
    f30rc_f30_return_on_capital_trajectory_roicdisp_252d_base_v018_signal,
    f30rc_f30_return_on_capital_trajectory_roedisp_252d_base_v019_signal,
    f30rc_f30_return_on_capital_trajectory_roictrank_504d_base_v020_signal,
    f30rc_f30_return_on_capital_trajectory_roicz_252d_base_v021_signal,
    f30rc_f30_return_on_capital_trajectory_roez_504d_base_v022_signal,
    f30rc_f30_return_on_capital_trajectory_roaz_252d_base_v023_signal,
    f30rc_f30_return_on_capital_trajectory_roicroespr_252d_base_v024_signal,
    f30rc_f30_return_on_capital_trajectory_levmult_252d_base_v025_signal,
    f30rc_f30_return_on_capital_trajectory_roicroaspr_126d_base_v026_signal,
    f30rc_f30_return_on_capital_trajectory_nioic_252d_base_v027_signal,
    f30rc_f30_return_on_capital_trajectory_nioe_252d_base_v028_signal,
    f30rc_f30_return_on_capital_trajectory_invcapgro_252d_base_v029_signal,
    f30rc_f30_return_on_capital_trajectory_eqgro_252d_base_v030_signal,
    f30rc_f30_return_on_capital_trajectory_roicfund_252d_base_v031_signal,
    f30rc_f30_return_on_capital_trajectory_rostsn_252d_base_v032_signal,
    f30rc_f30_return_on_capital_trajectory_roicslspr_126v504_base_v033_signal,
    f30rc_f30_return_on_capital_trajectory_roeslspr_126v504_base_v034_signal,
    f30rc_f30_return_on_capital_trajectory_compmom_63d_base_v035_signal,
    f30rc_f30_return_on_capital_trajectory_xdisp_base_v036_signal,
    f30rc_f30_return_on_capital_trajectory_xdispcurv_252d_base_v037_signal,
    f30rc_f30_return_on_capital_trajectory_roicdd_504d_base_v038_signal,
    f30rc_f30_return_on_capital_trajectory_roedd_504d_base_v039_signal,
    f30rc_f30_return_on_capital_trajectory_roicrec_504d_base_v040_signal,
    f30rc_f30_return_on_capital_trajectory_roicsignmag_252d_base_v041_signal,
    f30rc_f30_return_on_capital_trajectory_roedrank_504d_base_v042_signal,
    f30rc_f30_return_on_capital_trajectory_roaupdays_504d_base_v043_signal,
    f30rc_f30_return_on_capital_trajectory_rosupdays_252d_base_v044_signal,
    f30rc_f30_return_on_capital_trajectory_roiccurv_126d_base_v045_signal,
    f30rc_f30_return_on_capital_trajectory_roicdrank_504d_base_v046_signal,
    f30rc_f30_return_on_capital_trajectory_roerank_504d_base_v047_signal,
    f30rc_f30_return_on_capital_trajectory_roicyoy2_252d_base_v048_signal,
    f30rc_f30_return_on_capital_trajectory_qualslope_252d_base_v049_signal,
    f30rc_f30_return_on_capital_trajectory_stabspr_504d_base_v050_signal,
    f30rc_f30_return_on_capital_trajectory_roicgap_126d_base_v051_signal,
    f30rc_f30_return_on_capital_trajectory_roicorganic_252d_base_v052_signal,
    f30rc_f30_return_on_capital_trajectory_roeexeq_252d_base_v053_signal,
    f30rc_f30_return_on_capital_trajectory_rosroaspr_252d_base_v054_signal,
    f30rc_f30_return_on_capital_trajectory_roicewtrend_126d_base_v055_signal,
    f30rc_f30_return_on_capital_trajectory_roeewtrend_126d_base_v056_signal,
    f30rc_f30_return_on_capital_trajectory_breadth_252d_base_v057_signal,
    f30rc_f30_return_on_capital_trajectory_roatsn_252d_base_v058_signal,
    f30rc_f30_return_on_capital_trajectory_roevov_252d_base_v059_signal,
    f30rc_f30_return_on_capital_trajectory_roicmid_504d_base_v060_signal,
    f30rc_f30_return_on_capital_trajectory_dupont_252d_base_v061_signal,
    f30rc_f30_return_on_capital_trajectory_roicdurable_504d_base_v062_signal,
    f30rc_f30_return_on_capital_trajectory_rosz_252d_base_v063_signal,
    f30rc_f30_return_on_capital_trajectory_roicmrgap_252d_base_v064_signal,
    f30rc_f30_return_on_capital_trajectory_roicasym_252d_base_v065_signal,
    f30rc_f30_return_on_capital_trajectory_roeasym_252d_base_v066_signal,
    f30rc_f30_return_on_capital_trajectory_nioicstab_504d_base_v067_signal,
    f30rc_f30_return_on_capital_trajectory_rosoroicsl_252d_base_v068_signal,
    f30rc_f30_return_on_capital_trajectory_qualscore_252d_base_v069_signal,
    f30rc_f30_return_on_capital_trajectory_roadeltasn_126d_base_v070_signal,
    f30rc_f30_return_on_capital_trajectory_roscurv_126d_base_v071_signal,
    f30rc_f30_return_on_capital_trajectory_roicstreak_504d_base_v072_signal,
    f30rc_f30_return_on_capital_trajectory_roeoroic_252d_base_v073_signal,
    f30rc_f30_return_on_capital_trajectory_roicagree_base_v074_signal,
    f30rc_f30_return_on_capital_trajectory_allmetslope_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RETURN_ON_CAPITAL_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    roic = _fund(101, n, base=0.12, drift=0.01, vol=0.04, allow_neg=True).rename("roic")
    roe = _fund(102, n, base=0.15, drift=0.01, vol=0.05, allow_neg=True).rename("roe")
    roa = _fund(103, n, base=0.07, drift=0.01, vol=0.03, allow_neg=True).rename("roa")
    ros = _fund(104, n, base=0.10, drift=0.01, vol=0.04, allow_neg=True).rename("ros")
    invcap = _fund(105, n, base=1e9, drift=0.02, vol=0.05).rename("invcap")
    netinc = _fund(106, n, base=1e8, drift=0.02, vol=0.08, allow_neg=True).rename("netinc")
    equity = _fund(107, n, base=8e8, drift=0.02, vol=0.05).rename("equity")

    cols = {"roic": roic, "roe": roe, "roa": roa, "ros": ros,
            "invcap": invcap, "netinc": netinc, "equity": equity}

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

    print("OK f30_return_on_capital_trajectory_base_001_075_claude: %d features pass" % n_features)
