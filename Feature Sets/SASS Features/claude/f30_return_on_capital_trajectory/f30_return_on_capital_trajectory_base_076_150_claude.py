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
    return s - s.shift(w)


def _f30_logchg(s, w):
    return np.log(s.abs().replace(0, np.nan)) - np.log(s.abs().shift(w).replace(0, np.nan))


def _f30_stability(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f30_updays(s, w):
    up = (s.diff(63) > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean()


def _f30_accel(s, w):
    d = s - s.shift(w)
    return d - d.shift(w)


def _f30_ema_disp(s, span):
    return s - s.ewm(span=span, min_periods=max(2, span // 2)).mean()


def _f30_spread(a, b):
    return a - b


# ============================================================
# ROIC half-year trend (steeper-horizon trajectory)
def f30rc_f30_return_on_capital_trajectory_roictrend_126d_base_v076_signal(roic):
    b = _f30_slope(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE half-year trend
def f30rc_f30_return_on_capital_trajectory_roetrend_126d_base_v077_signal(roe):
    b = _f30_slope(roe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA half-year trend
def f30rc_f30_return_on_capital_trajectory_roatrend_126d_base_v078_signal(roa):
    b = _f30_slope(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS two-year trend (long quality-of-sales trajectory)
def f30rc_f30_return_on_capital_trajectory_rostrend_504d_base_v079_signal(ros):
    b = _f30_slope(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC quarterly improvement (short ROIC-minus-prior)
def f30rc_f30_return_on_capital_trajectory_roicdelta_63d_base_v080_signal(roic):
    b = _f30_delta(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE quarterly improvement
def f30rc_f30_return_on_capital_trajectory_roedelta_63d_base_v081_signal(roe):
    b = _f30_delta(roe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA quarterly improvement
def f30rc_f30_return_on_capital_trajectory_roadelta_63d_base_v082_signal(roa):
    b = _f30_delta(roa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS quarterly improvement
def f30rc_f30_return_on_capital_trajectory_rosdelta_63d_base_v083_signal(ros):
    b = _f30_delta(ros, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC one-year stability (mean/std over 252d)
def f30rc_f30_return_on_capital_trajectory_roicstab_252d_base_v084_signal(roic):
    b = _f30_stability(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA one-year stability
def f30rc_f30_return_on_capital_trajectory_roastab_252d_base_v085_signal(roa):
    b = _f30_stability(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS two-year stability
def f30rc_f30_return_on_capital_trajectory_rosstab_504d_base_v086_signal(ros):
    b = _f30_stability(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC quality of trend: slope ranked vs own two-year history (extremity of improvement)
def f30rc_f30_return_on_capital_trajectory_roicslrank_504d_base_v087_signal(roic):
    sl = _f30_slope(roic, 252)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS slope rank vs own history
def f30rc_f30_return_on_capital_trajectory_rosslrank_504d_base_v088_signal(ros):
    sl = _f30_slope(ros, 252)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC change-of-trend (curvature) over a year, ranked (inflection extremity)
def f30rc_f30_return_on_capital_trajectory_roiccurvrank_504d_base_v089_signal(roic):
    sl = _f30_slope(roic, 126)
    curv = sl - sl.shift(126)
    b = _rank(curv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE curvature as a level (126d-step acceleration of returns)
def f30rc_f30_return_on_capital_trajectory_roeaccel_126d_base_v090_signal(roe):
    b = _f30_accel(roe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS acceleration as a level (126d steps)
def f30rc_f30_return_on_capital_trajectory_rosaccel_126d_base_v091_signal(ros):
    b = _f30_accel(ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC displacement from a faster (half-year) EMA
def f30rc_f30_return_on_capital_trajectory_roicdisp_126d_base_v092_signal(roic):
    b = _f30_ema_disp(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA displacement from its slow EMA
def f30rc_f30_return_on_capital_trajectory_roadisp_252d_base_v093_signal(roa):
    b = _f30_ema_disp(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS displacement from its slow EMA
def f30rc_f30_return_on_capital_trajectory_rosdisp_252d_base_v094_signal(ros):
    b = _f30_ema_disp(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level z-scored vs longer (two-year) history
def f30rc_f30_return_on_capital_trajectory_roicz_504d_base_v095_signal(roic):
    b = _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA level z-scored vs two-year history
def f30rc_f30_return_on_capital_trajectory_roaz_504d_base_v096_signal(roa):
    b = _z(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS level z-scored vs two-year history
def f30rc_f30_return_on_capital_trajectory_rosz_504d_base_v097_signal(ros):
    b = _z(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level percentile vs own multi-year history (durable capital-return)
def f30rc_f30_return_on_capital_trajectory_roicrank_504d_base_v098_signal(roic):
    b = _rank(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA half-year improvement percentile vs own history (rank of asset-return gains)
def f30rc_f30_return_on_capital_trajectory_roadrank_504d_base_v099_signal(roa):
    d = _f30_delta(roa, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROA invested-capital advantage: smoothed spread z-score
def f30rc_f30_return_on_capital_trajectory_roicroazspr_252d_base_v100_signal(roic, roa):
    spr = _f30_spread(roic, roa)
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROS spread trajectory (capital vs margin return drift)
def f30rc_f30_return_on_capital_trajectory_roicrosspr_252d_base_v101_signal(roic, ros):
    spr = _f30_spread(roic, ros)
    b = _f30_slope(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-minus-ROS spread half-year improvement
def f30rc_f30_return_on_capital_trajectory_roerosdspr_126d_base_v102_signal(roe, ros):
    spr = _f30_spread(roe, ros)
    b = _f30_delta(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rebuilt ROIC (netinc/invcap) half-year trend
def f30rc_f30_return_on_capital_trajectory_nioictrend_126d_base_v103_signal(netinc, invcap):
    proxy = _safe_div(netinc, invcap)
    b = _f30_slope(proxy, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rebuilt ROE (netinc/equity) two-year stability
def f30rc_f30_return_on_capital_trajectory_nioestab_504d_base_v104_signal(netinc, equity):
    proxy = _safe_div(netinc, equity)
    b = _f30_stability(proxy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc trajectory relative to invested-capital trajectory (return-base divergence)
def f30rc_f30_return_on_capital_trajectory_nivsinvcap_252d_base_v105_signal(netinc, invcap):
    gn = _f30_logchg(netinc, 252)
    gc = _f30_logchg(invcap, 252)
    b = gn - gc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc trajectory relative to equity trajectory (return-on-equity organic growth)
def f30rc_f30_return_on_capital_trajectory_nivseq_252d_base_v106_signal(netinc, equity):
    gn = _f30_logchg(netinc, 252)
    ge = _f30_logchg(equity, 252)
    b = gn - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital half-year growth (capital-base trajectory)
def f30rc_f30_return_on_capital_trajectory_invcapgro_126d_base_v107_signal(invcap):
    b = _f30_logchg(invcap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity half-year growth
def f30rc_f30_return_on_capital_trajectory_eqgro_126d_base_v108_signal(equity):
    b = _f30_logchg(equity, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-base growth dispersion: do invcap and equity grow in step
def f30rc_f30_return_on_capital_trajectory_capdiverge_252d_base_v109_signal(invcap, equity):
    gi = _f30_logchg(invcap, 252)
    ge = _f30_logchg(equity, 252)
    b = gi - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement funded organically: ROIC delta when equity is growing slowly
def f30rc_f30_return_on_capital_trajectory_roicorgfund_252d_base_v110_signal(roic, equity):
    d = _f30_delta(roic, 252)
    g = _f30_logchg(equity, 252)
    b = d * (1.0 - np.tanh(3.0 * g.clip(lower=0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return-on-capital momentum over half-year (roic/roe/roa avg delta)
def f30rc_f30_return_on_capital_trajectory_compmom_126d_base_v111_signal(roic, roe, roa):
    d = (roic.diff(126) + roe.diff(126) + roa.diff(126)) / 3.0
    b = d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return-on-capital momentum over a year (all four metrics)
def f30rc_f30_return_on_capital_trajectory_compmom_252d_base_v112_signal(roic, roe, roa, ros):
    d = (roic.diff(252) + roe.diff(252) + roa.diff(252) + ros.diff(252)) / 4.0
    b = d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-metric dispersion z-score (quality-profile coherence regime)
def f30rc_f30_return_on_capital_trajectory_xdispz_252d_base_v113_signal(roic, roe, roa, ros):
    stacked = pd.concat([roic, roe, roa, ros], axis=1)
    disp = stacked.std(axis=1)
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-metric mean return-on-capital trajectory (composite level trend)
def f30rc_f30_return_on_capital_trajectory_xmeantrend_252d_base_v114_signal(roic, roe, roa, ros):
    stacked = pd.concat([roic, roe, roa, ros], axis=1)
    comp = stacked.mean(axis=1)
    b = _f30_slope(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from one-year peak (recent quality erosion)
def f30rc_f30_return_on_capital_trajectory_roicdd_252d_base_v115_signal(roic):
    peak = roic.rolling(252, min_periods=63).max()
    b = roic - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA drawdown from one-year peak
def f30rc_f30_return_on_capital_trajectory_roadd_252d_base_v116_signal(roa):
    peak = roa.rolling(252, min_periods=63).max()
    b = roa - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE recovery off two-year trough (return improvement from low base)
def f30rc_f30_return_on_capital_trajectory_roerec_504d_base_v117_signal(roe):
    trough = roe.rolling(504, min_periods=126).min()
    b = roe - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS recovery off two-year trough
def f30rc_f30_return_on_capital_trajectory_rosrec_504d_base_v118_signal(ros):
    trough = ros.rolling(504, min_periods=126).min()
    b = ros - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt magnitude of ROE improvement (compressed quality-improvement direction)
def f30rc_f30_return_on_capital_trajectory_roesignmag_252d_base_v119_signal(roe):
    d = _f30_delta(roe, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt magnitude of ROA improvement
def f30rc_f30_return_on_capital_trajectory_roasignmag_252d_base_v120_signal(roa):
    d = _f30_delta(roa, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement consistency over one year (shorter hit-rate window)
def f30rc_f30_return_on_capital_trajectory_roicupdays_252d_base_v121_signal(roic):
    b = _f30_updays(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS improvement consistency over two years
def f30rc_f30_return_on_capital_trajectory_rosupdays_504d_base_v122_signal(ros):
    b = _f30_updays(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trajectory signal-to-noise over half-year horizon
def f30rc_f30_return_on_capital_trajectory_roictsn_126d_base_v123_signal(roic):
    sl = _f30_slope(roic, 126)
    vol = _std(roic.diff(), 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE trajectory signal-to-noise over half-year horizon
def f30rc_f30_return_on_capital_trajectory_roetsn_126d_base_v124_signal(roe):
    sl = _f30_slope(roe, 126)
    vol = _std(roe.diff(), 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC mid-range position over a year (where in its recent band)
def f30rc_f30_return_on_capital_trajectory_roicmid_252d_base_v125_signal(roic):
    hi = roic.rolling(252, min_periods=63).max()
    lo = roic.rolling(252, min_periods=63).min()
    mid = (hi + lo) / 2.0
    b = (roic - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE range-position over two years
def f30rc_f30_return_on_capital_trajectory_roerngpos_504d_base_v126_signal(roe):
    hi = roe.rolling(504, min_periods=126).max()
    lo = roe.rolling(504, min_periods=126).min()
    b = (roe - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC year-over-year improvement minus its long-run average improvement
def f30rc_f30_return_on_capital_trajectory_roicexcimp_252d_base_v127_signal(roic):
    d = _f30_delta(roic, 252)
    b = d - d.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE improvement minus its long-run average improvement
def f30rc_f30_return_on_capital_trajectory_roeexcimp_252d_base_v128_signal(roe):
    d = _f30_delta(roe, 252)
    b = d - d.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont leverage trajectory: ROE/ROA ratio half-year improvement
def f30rc_f30_return_on_capital_trajectory_levdelta_126d_base_v129_signal(roe, roa):
    lev = _safe_div(roe, roa)
    b = _f30_delta(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-turn proxy trajectory: ROIC/ROS ratio (asset use behind margin) z-score regime
def f30rc_f30_return_on_capital_trajectory_capturn_252d_base_v130_signal(roic, ros):
    turn = _safe_div(roic, ros)
    b = _z(turn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC durable improvement: 252d delta gated by two-year hit-rate consistency
def f30rc_f30_return_on_capital_trajectory_roicdurable_252d_base_v131_signal(roic):
    d = _f30_delta(roic, 252)
    consist = _f30_updays(roic, 504) - 0.5
    b = d * consist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE durable improvement: 252d delta gated by two-year hit-rate consistency
def f30rc_f30_return_on_capital_trajectory_roedurable_252d_base_v132_signal(roe):
    d = _f30_delta(roe, 252)
    consist = _f30_updays(roe, 504) - 0.5
    b = d * consist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC volatility trajectory: is the return base getting noisier (slope of rolling vol)
def f30rc_f30_return_on_capital_trajectory_roicvoltrend_252d_base_v133_signal(roic):
    vol = _std(roic.diff(), 126)
    b = _f30_slope(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE volatility trajectory
def f30rc_f30_return_on_capital_trajectory_roevoltrend_252d_base_v134_signal(roe):
    vol = _std(roe.diff(), 126)
    b = _f30_slope(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trajectory asymmetry over two years (up vs down semi-dev of changes)
def f30rc_f30_return_on_capital_trajectory_roicasym_504d_base_v135_signal(roic):
    d = roic.diff()
    up = d.clip(lower=0).rolling(504, min_periods=126).std()
    dn = (-d.clip(upper=0)).rolling(504, min_periods=126).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trajectory asymmetry over a year
def f30rc_f30_return_on_capital_trajectory_roaasym_252d_base_v136_signal(roa):
    d = roa.diff()
    up = d.clip(lower=0).rolling(252, min_periods=63).std()
    dn = (-d.clip(upper=0)).rolling(252, min_periods=63).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon ROE improvement sign agreement, scaled by magnitude
def f30rc_f30_return_on_capital_trajectory_roeagree_base_v137_signal(roe):
    s1 = np.sign(roe.diff(63))
    s2 = np.sign(roe.diff(126))
    s3 = np.sign(roe.diff(252))
    b = (s1 + s2 + s3) / 3.0 * _f30_delta(roe, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital improvement breadth z-scored (how broad the quality lift is)
def f30rc_f30_return_on_capital_trajectory_breadthz_252d_base_v138_signal(roic, roe, roa, ros):
    up = (roic.diff(126) > 0).astype(float) + (roe.diff(126) > 0).astype(float) \
        + (roa.diff(126) > 0).astype(float) + (ros.diff(126) > 0).astype(float)
    b = _z(up, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rebuilt-ROIC vs reported-ROIC gap trajectory (accounting-quality drift)
def f30rc_f30_return_on_capital_trajectory_roicgaptrend_252d_base_v139_signal(netinc, invcap, roic):
    gap = _safe_div(netinc, invcap) - roic
    b = _f30_slope(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS quality-improvement slope vol-scaled (margin-return signal-to-noise, year)
def f30rc_f30_return_on_capital_trajectory_rostsn_252d_base_v140_signal(ros):
    sl = _f30_slope(ros, 252)
    vol = _std(ros.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC exponentially-weighted trajectory: fast minus very-slow EMA (persistent drift)
def f30rc_f30_return_on_capital_trajectory_roicewtrend_252d_base_v141_signal(roic):
    fast = roic.ewm(span=126, min_periods=42).mean()
    slow = roic.ewm(span=504, min_periods=126).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA exponentially-weighted trajectory
def f30rc_f30_return_on_capital_trajectory_roaewtrend_126d_base_v142_signal(roa):
    fast = roa.ewm(span=63, min_periods=21).mean()
    slow = roa.ewm(span=252, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite improvement persistence: EMA-decayed run of QoQ composite gains
def f30rc_f30_return_on_capital_trajectory_compstreak_504d_base_v143_signal(roic, roe, roa):
    comp = (roic + roe + roa) / 3.0
    up = (comp.diff(63) > 0).astype(float)
    b = up.ewm(span=126, min_periods=42).mean() * up.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC year-over-year second difference (improvement vs improvement a year ago)
def f30rc_f30_return_on_capital_trajectory_roeyoy2_252d_base_v144_signal(roe):
    d = roe.diff(252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted quality slope blend over half-year horizon
def f30rc_f30_return_on_capital_trajectory_qualslope_126d_base_v145_signal(roic, roe, roa):
    b = 0.5 * _f30_slope(roic, 126) + 0.3 * _f30_slope(roe, 126) + 0.2 * _f30_slope(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability spread: ROE steadiness minus ROS steadiness over two years
def f30rc_f30_return_on_capital_trajectory_stabspr_roeros_504d_base_v146_signal(roe, ros):
    b = _f30_stability(roe, 504) - _f30_stability(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital improvement quality score: composite z of slope + breadth, half-year
def f30rc_f30_return_on_capital_trajectory_qualscore_126d_base_v147_signal(roic, roe, roa, ros):
    sl = _z(_f30_slope(roic, 126), 252)
    breadth = (roe.diff(126) > 0).astype(float) + (roa.diff(126) > 0).astype(float) \
        + (ros.diff(126) > 0).astype(float)
    b = sl + (breadth - 1.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC upper-band residence: fraction of last year ROIC held in the top third of its 504d band
def f30rc_f30_return_on_capital_trajectory_roicuppertime_504d_base_v148_signal(roic):
    hi = roic.rolling(504, min_periods=126).max()
    lo = roic.rolling(504, min_periods=126).min()
    rp = (roic - lo) / (hi - lo).replace(0, np.nan)
    upper = (rp >= 0.6667).astype(float)
    b = upper.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-metric mean return-on-capital trajectory vol-scaled (composite signal-to-noise)
def f30rc_f30_return_on_capital_trajectory_allmettsn_126d_base_v149_signal(roic, roe, roa, ros):
    comp = (roic + roe + roa + ros) / 4.0
    sl = _f30_slope(comp, 126)
    vol = _std(comp.diff(), 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rebuilt-ROE (netinc/equity) trajectory percentile vs own history (regime extremity)
def f30rc_f30_return_on_capital_trajectory_nioerank_504d_base_v150_signal(netinc, equity):
    proxy = _safe_div(netinc, equity)
    b = _rank(proxy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rc_f30_return_on_capital_trajectory_roictrend_126d_base_v076_signal,
    f30rc_f30_return_on_capital_trajectory_roetrend_126d_base_v077_signal,
    f30rc_f30_return_on_capital_trajectory_roatrend_126d_base_v078_signal,
    f30rc_f30_return_on_capital_trajectory_rostrend_504d_base_v079_signal,
    f30rc_f30_return_on_capital_trajectory_roicdelta_63d_base_v080_signal,
    f30rc_f30_return_on_capital_trajectory_roedelta_63d_base_v081_signal,
    f30rc_f30_return_on_capital_trajectory_roadelta_63d_base_v082_signal,
    f30rc_f30_return_on_capital_trajectory_rosdelta_63d_base_v083_signal,
    f30rc_f30_return_on_capital_trajectory_roicstab_252d_base_v084_signal,
    f30rc_f30_return_on_capital_trajectory_roastab_252d_base_v085_signal,
    f30rc_f30_return_on_capital_trajectory_rosstab_504d_base_v086_signal,
    f30rc_f30_return_on_capital_trajectory_roicslrank_504d_base_v087_signal,
    f30rc_f30_return_on_capital_trajectory_rosslrank_504d_base_v088_signal,
    f30rc_f30_return_on_capital_trajectory_roiccurvrank_504d_base_v089_signal,
    f30rc_f30_return_on_capital_trajectory_roeaccel_126d_base_v090_signal,
    f30rc_f30_return_on_capital_trajectory_rosaccel_126d_base_v091_signal,
    f30rc_f30_return_on_capital_trajectory_roicdisp_126d_base_v092_signal,
    f30rc_f30_return_on_capital_trajectory_roadisp_252d_base_v093_signal,
    f30rc_f30_return_on_capital_trajectory_rosdisp_252d_base_v094_signal,
    f30rc_f30_return_on_capital_trajectory_roicz_504d_base_v095_signal,
    f30rc_f30_return_on_capital_trajectory_roaz_504d_base_v096_signal,
    f30rc_f30_return_on_capital_trajectory_rosz_504d_base_v097_signal,
    f30rc_f30_return_on_capital_trajectory_roicrank_504d_base_v098_signal,
    f30rc_f30_return_on_capital_trajectory_roadrank_504d_base_v099_signal,
    f30rc_f30_return_on_capital_trajectory_roicroazspr_252d_base_v100_signal,
    f30rc_f30_return_on_capital_trajectory_roicrosspr_252d_base_v101_signal,
    f30rc_f30_return_on_capital_trajectory_roerosdspr_126d_base_v102_signal,
    f30rc_f30_return_on_capital_trajectory_nioictrend_126d_base_v103_signal,
    f30rc_f30_return_on_capital_trajectory_nioestab_504d_base_v104_signal,
    f30rc_f30_return_on_capital_trajectory_nivsinvcap_252d_base_v105_signal,
    f30rc_f30_return_on_capital_trajectory_nivseq_252d_base_v106_signal,
    f30rc_f30_return_on_capital_trajectory_invcapgro_126d_base_v107_signal,
    f30rc_f30_return_on_capital_trajectory_eqgro_126d_base_v108_signal,
    f30rc_f30_return_on_capital_trajectory_capdiverge_252d_base_v109_signal,
    f30rc_f30_return_on_capital_trajectory_roicorgfund_252d_base_v110_signal,
    f30rc_f30_return_on_capital_trajectory_compmom_126d_base_v111_signal,
    f30rc_f30_return_on_capital_trajectory_compmom_252d_base_v112_signal,
    f30rc_f30_return_on_capital_trajectory_xdispz_252d_base_v113_signal,
    f30rc_f30_return_on_capital_trajectory_xmeantrend_252d_base_v114_signal,
    f30rc_f30_return_on_capital_trajectory_roicdd_252d_base_v115_signal,
    f30rc_f30_return_on_capital_trajectory_roadd_252d_base_v116_signal,
    f30rc_f30_return_on_capital_trajectory_roerec_504d_base_v117_signal,
    f30rc_f30_return_on_capital_trajectory_rosrec_504d_base_v118_signal,
    f30rc_f30_return_on_capital_trajectory_roesignmag_252d_base_v119_signal,
    f30rc_f30_return_on_capital_trajectory_roasignmag_252d_base_v120_signal,
    f30rc_f30_return_on_capital_trajectory_roicupdays_252d_base_v121_signal,
    f30rc_f30_return_on_capital_trajectory_rosupdays_504d_base_v122_signal,
    f30rc_f30_return_on_capital_trajectory_roictsn_126d_base_v123_signal,
    f30rc_f30_return_on_capital_trajectory_roetsn_126d_base_v124_signal,
    f30rc_f30_return_on_capital_trajectory_roicmid_252d_base_v125_signal,
    f30rc_f30_return_on_capital_trajectory_roerngpos_504d_base_v126_signal,
    f30rc_f30_return_on_capital_trajectory_roicexcimp_252d_base_v127_signal,
    f30rc_f30_return_on_capital_trajectory_roeexcimp_252d_base_v128_signal,
    f30rc_f30_return_on_capital_trajectory_levdelta_126d_base_v129_signal,
    f30rc_f30_return_on_capital_trajectory_capturn_252d_base_v130_signal,
    f30rc_f30_return_on_capital_trajectory_roicdurable_252d_base_v131_signal,
    f30rc_f30_return_on_capital_trajectory_roedurable_252d_base_v132_signal,
    f30rc_f30_return_on_capital_trajectory_roicvoltrend_252d_base_v133_signal,
    f30rc_f30_return_on_capital_trajectory_roevoltrend_252d_base_v134_signal,
    f30rc_f30_return_on_capital_trajectory_roicasym_504d_base_v135_signal,
    f30rc_f30_return_on_capital_trajectory_roaasym_252d_base_v136_signal,
    f30rc_f30_return_on_capital_trajectory_roeagree_base_v137_signal,
    f30rc_f30_return_on_capital_trajectory_breadthz_252d_base_v138_signal,
    f30rc_f30_return_on_capital_trajectory_roicgaptrend_252d_base_v139_signal,
    f30rc_f30_return_on_capital_trajectory_rostsn_252d_base_v140_signal,
    f30rc_f30_return_on_capital_trajectory_roicewtrend_252d_base_v141_signal,
    f30rc_f30_return_on_capital_trajectory_roaewtrend_126d_base_v142_signal,
    f30rc_f30_return_on_capital_trajectory_compstreak_504d_base_v143_signal,
    f30rc_f30_return_on_capital_trajectory_roeyoy2_252d_base_v144_signal,
    f30rc_f30_return_on_capital_trajectory_qualslope_126d_base_v145_signal,
    f30rc_f30_return_on_capital_trajectory_stabspr_roeros_504d_base_v146_signal,
    f30rc_f30_return_on_capital_trajectory_qualscore_126d_base_v147_signal,
    f30rc_f30_return_on_capital_trajectory_roicuppertime_504d_base_v148_signal,
    f30rc_f30_return_on_capital_trajectory_allmettsn_126d_base_v149_signal,
    f30rc_f30_return_on_capital_trajectory_nioerank_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RETURN_ON_CAPITAL_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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

    print("OK f30_return_on_capital_trajectory_base_076_150_claude: %d features pass" % n_features)
