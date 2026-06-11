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
        x = np.arange(m, dtype=float)
        xm = x.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        am = a.mean()
        return ((x - xm) * (a - am)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _stability(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _roc(s, w):
    # math 1st derivative proxy: change over w normalized by w (per-step rate)
    return (s - s.shift(w)) / float(w)

# slope of ROIC level (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roiclvl_21d_slope_v001_signal(roic):
    b = roic
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE level (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roelvl_21d_slope_v002_signal(roe):
    b = roe
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA level (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roalvl_21d_slope_v003_signal(roa):
    b = roa
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS level (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roslvl_21d_slope_v004_signal(ros):
    b = ros
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicz_21d_slope_v005_signal(roic):
    b = _z(roic, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roez_21d_slope_v006_signal(roe):
    b = _z(roe, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roaz_21d_slope_v007_signal(roa):
    b = _z(roa, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rosz_21d_slope_v008_signal(ros):
    b = _z(ros, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC rank (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicrank_21d_slope_v009_signal(roic):
    b = _rank(roic, 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE rank (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roerank_21d_slope_v010_signal(roe):
    b = _rank(roe, 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA rank (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roarank_21d_slope_v011_signal(roa):
    b = _rank(roa, 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS rank (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rosrank_21d_slope_v012_signal(ros):
    b = _rank(ros, 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC fast/slow EMA ratio (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicema_21d_slope_v013_signal(roic):
    fast = roic.ewm(span=42, min_periods=15).mean()
    slow = roic.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z fast/slow EMA ratio (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roeema_21d_slope_v014_signal(roe):
    fast = roe.ewm(span=21, min_periods=8).mean()
    slow = roe.ewm(span=126, min_periods=42).mean()
    b = _z(_safe_div(fast, slow), 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA fast/slow EMA ratio (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roaema_21d_slope_v015_signal(roa):
    fast = roa.ewm(span=42, min_periods=15).mean()
    slow = roa.ewm(span=126, min_periods=42).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS fast/slow EMA ratio (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rosema_21d_slope_v016_signal(ros):
    fast = ros.ewm(span=42, min_periods=15).mean()
    slow = ros.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC stability (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicstab_21d_slope_v017_signal(roic):
    b = _stability(roic, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE stability (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roestab_21d_slope_v018_signal(roe):
    b = _stability(roe, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA stability (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roastab_21d_slope_v019_signal(roa):
    b = _stability(roa, 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS stability (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rosstab_21d_slope_v020_signal(ros):
    b = _stability(ros, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC mid (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicmid_21d_slope_v021_signal(roic):
    hi = roic.rolling(504, min_periods=126).max()
    lo = roic.rolling(504, min_periods=126).min()
    b = (roic - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE mid (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roemid_21d_slope_v022_signal(roe):
    hi = roe.rolling(504, min_periods=126).max()
    lo = roe.rolling(504, min_periods=126).min()
    b = (roe - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA range-pos (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roarngpos_21d_slope_v023_signal(roa):
    hi = roa.rolling(252, min_periods=63).max()
    lo = roa.rolling(252, min_periods=63).min()
    b = (roa - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS range-pos (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rosrngpos_21d_slope_v024_signal(ros):
    hi = ros.rolling(252, min_periods=63).max()
    lo = ros.rolling(252, min_periods=63).min()
    b = (ros - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROA ratio (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicroaspr_21d_slope_v025_signal(roic, roa):
    b = _safe_div(roic, roa.abs() + 0.01)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROA z-spread (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roeroaspr_21d_slope_v026_signal(roe, roa):
    b = _z(roe, 252) - _z(roa, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROS z-spread (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicrosspr_21d_slope_v027_signal(roic, ros):
    b = _z(roic, 252) - _z(ros, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roerosspr_21d_slope_v028_signal(roe, ros):
    b = roe - ros
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROA leverage (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_levmult_21d_slope_v029_signal(roe, roa):
    b = _safe_div(roe, roa)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROS turn (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_capturn_21d_slope_v030_signal(roic, ros):
    b = _safe_div(roic, ros)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROIC (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roeoroic_21d_slope_v031_signal(roe, roic):
    b = _safe_div(roe, roic)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROA spread z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicroazspr_21d_slope_v032_signal(roic, roa):
    b = _z(roic - roa, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roerosz_21d_slope_v033_signal(roe, ros):
    b = _z(roe - ros, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite mean (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_compmean_21d_slope_v034_signal(roic, roe, roa, ros):
    b = (roic + roe + roa + ros) / 4.0
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 3-metric mean (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_compq_21d_slope_v035_signal(roic, roe, roa):
    b = (roic + roe + roa) / 3.0
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross range (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_xdisp_21d_slope_v036_signal(roic, roa, ros):
    st = pd.concat([roic, roa, ros], axis=1)
    b = st.max(axis=1) - st.min(axis=1)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_compz_21d_slope_v037_signal(roic, roe, roa, ros):
    b = _z((roic + roe + roa + ros) / 4.0, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_nioic_21d_slope_v038_signal(netinc, invcap):
    b = _safe_div(netinc, invcap)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_nioe_21d_slope_v039_signal(netinc, equity):
    b = _safe_div(netinc, equity)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap z (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_nioicz_21d_slope_v040_signal(netinc, invcap):
    b = _z(_safe_div(netinc, invcap), 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity rank (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_nioerank_21d_slope_v041_signal(netinc, equity):
    b = _rank(_safe_div(netinc, equity), 504)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log invcap (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_invcaplog_21d_slope_v042_signal(invcap):
    b = np.log(invcap.replace(0, np.nan))
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log equity (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_eqlog_21d_slope_v043_signal(equity):
    b = np.log(equity.replace(0, np.nan))
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC x invcap-growth (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicpercap_21d_slope_v044_signal(roic, invcap):
    g = (np.log(invcap.replace(0, np.nan)) - np.log(invcap.shift(126).replace(0, np.nan)))
    b = roic * np.tanh(5.0 * g)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE x equity-growth (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roeperq_21d_slope_v045_signal(roe, equity):
    g = (np.log(equity.replace(0, np.nan)) - np.log(equity.shift(126).replace(0, np.nan)))
    b = roe * np.tanh(5.0 * g)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC 126 slope (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicsl126_21d_slope_v046_signal(roic):
    b = _slope(roic, 126)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE 126 slope (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roesl126_21d_slope_v047_signal(roe):
    b = _slope(roe, 126)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA 252 slope (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roasl252_21d_slope_v048_signal(roa):
    b = _slope(roa, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS 252 slope (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_rossl252_21d_slope_v049_signal(ros):
    b = _slope(ros, 252)
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC accounting gap (ROC window 21d)
def f30rc_f30_return_on_capital_trajectory_roicgap_21d_slope_v050_signal(netinc, invcap, roic):
    b = _safe_div(netinc, invcap) - roic
    d = (b - b.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC level (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roiclvl_63d_slope_v051_signal(roic):
    b = roic
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE level (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roelvl_63d_slope_v052_signal(roe):
    b = roe
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA level (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roalvl_63d_slope_v053_signal(roa):
    b = roa
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS level (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roslvl_63d_slope_v054_signal(ros):
    b = ros
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicz_63d_slope_v055_signal(roic):
    b = _z(roic, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roez_63d_slope_v056_signal(roe):
    b = _z(roe, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roaz_63d_slope_v057_signal(roa):
    b = _z(roa, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rosz_63d_slope_v058_signal(ros):
    b = _z(ros, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC rank (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicrank_63d_slope_v059_signal(roic):
    b = _rank(roic, 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE rank (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roerank_63d_slope_v060_signal(roe):
    b = _rank(roe, 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA rank (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roarank_63d_slope_v061_signal(roa):
    b = _rank(roa, 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS rank (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rosrank_63d_slope_v062_signal(ros):
    b = _rank(ros, 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC fast/slow EMA ratio (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicema_63d_slope_v063_signal(roic):
    fast = roic.ewm(span=42, min_periods=15).mean()
    slow = roic.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z fast/slow EMA ratio (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roeema_63d_slope_v064_signal(roe):
    fast = roe.ewm(span=21, min_periods=8).mean()
    slow = roe.ewm(span=126, min_periods=42).mean()
    b = _z(_safe_div(fast, slow), 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA fast/slow EMA ratio (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roaema_63d_slope_v065_signal(roa):
    fast = roa.ewm(span=42, min_periods=15).mean()
    slow = roa.ewm(span=126, min_periods=42).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS fast/slow EMA ratio (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rosema_63d_slope_v066_signal(ros):
    fast = ros.ewm(span=42, min_periods=15).mean()
    slow = ros.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC stability (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicstab_63d_slope_v067_signal(roic):
    b = _stability(roic, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE stability (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roestab_63d_slope_v068_signal(roe):
    b = _stability(roe, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA stability (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roastab_63d_slope_v069_signal(roa):
    b = _stability(roa, 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS stability (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rosstab_63d_slope_v070_signal(ros):
    b = _stability(ros, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC mid (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicmid_63d_slope_v071_signal(roic):
    hi = roic.rolling(504, min_periods=126).max()
    lo = roic.rolling(504, min_periods=126).min()
    b = (roic - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE mid (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roemid_63d_slope_v072_signal(roe):
    hi = roe.rolling(504, min_periods=126).max()
    lo = roe.rolling(504, min_periods=126).min()
    b = (roe - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA range-pos (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roarngpos_63d_slope_v073_signal(roa):
    hi = roa.rolling(252, min_periods=63).max()
    lo = roa.rolling(252, min_periods=63).min()
    b = (roa - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS range-pos (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rosrngpos_63d_slope_v074_signal(ros):
    hi = ros.rolling(252, min_periods=63).max()
    lo = ros.rolling(252, min_periods=63).min()
    b = (ros - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROA ratio (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicroaspr_63d_slope_v075_signal(roic, roa):
    b = _safe_div(roic, roa.abs() + 0.01)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROA z-spread (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roeroaspr_63d_slope_v076_signal(roe, roa):
    b = _z(roe, 252) - _z(roa, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROS z-spread (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicrosspr_63d_slope_v077_signal(roic, ros):
    b = _z(roic, 252) - _z(ros, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roerosspr_63d_slope_v078_signal(roe, ros):
    b = roe - ros
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROA leverage (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_levmult_63d_slope_v079_signal(roe, roa):
    b = _safe_div(roe, roa)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROS turn (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_capturn_63d_slope_v080_signal(roic, ros):
    b = _safe_div(roic, ros)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROIC (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roeoroic_63d_slope_v081_signal(roe, roic):
    b = _safe_div(roe, roic)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROA spread z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicroazspr_63d_slope_v082_signal(roic, roa):
    b = _z(roic - roa, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roerosz_63d_slope_v083_signal(roe, ros):
    b = _z(roe - ros, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite mean (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_compmean_63d_slope_v084_signal(roic, roe, roa, ros):
    b = (roic + roe + roa + ros) / 4.0
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 3-metric mean (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_compq_63d_slope_v085_signal(roic, roe, roa):
    b = (roic + roe + roa) / 3.0
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross range (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_xdisp_63d_slope_v086_signal(roic, roa, ros):
    st = pd.concat([roic, roa, ros], axis=1)
    b = st.max(axis=1) - st.min(axis=1)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_compz_63d_slope_v087_signal(roic, roe, roa, ros):
    b = _z((roic + roe + roa + ros) / 4.0, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_nioic_63d_slope_v088_signal(netinc, invcap):
    b = _safe_div(netinc, invcap)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_nioe_63d_slope_v089_signal(netinc, equity):
    b = _safe_div(netinc, equity)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap z (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_nioicz_63d_slope_v090_signal(netinc, invcap):
    b = _z(_safe_div(netinc, invcap), 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity rank (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_nioerank_63d_slope_v091_signal(netinc, equity):
    b = _rank(_safe_div(netinc, equity), 504)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log invcap (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_invcaplog_63d_slope_v092_signal(invcap):
    b = np.log(invcap.replace(0, np.nan))
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log equity (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_eqlog_63d_slope_v093_signal(equity):
    b = np.log(equity.replace(0, np.nan))
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC x invcap-growth (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicpercap_63d_slope_v094_signal(roic, invcap):
    g = (np.log(invcap.replace(0, np.nan)) - np.log(invcap.shift(126).replace(0, np.nan)))
    b = roic * np.tanh(5.0 * g)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE x equity-growth (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roeperq_63d_slope_v095_signal(roe, equity):
    g = (np.log(equity.replace(0, np.nan)) - np.log(equity.shift(126).replace(0, np.nan)))
    b = roe * np.tanh(5.0 * g)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC 126 slope (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicsl126_63d_slope_v096_signal(roic):
    b = _slope(roic, 126)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE 126 slope (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roesl126_63d_slope_v097_signal(roe):
    b = _slope(roe, 126)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA 252 slope (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roasl252_63d_slope_v098_signal(roa):
    b = _slope(roa, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS 252 slope (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_rossl252_63d_slope_v099_signal(ros):
    b = _slope(ros, 252)
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC accounting gap (ROC window 63d)
def f30rc_f30_return_on_capital_trajectory_roicgap_63d_slope_v100_signal(netinc, invcap, roic):
    b = _safe_div(netinc, invcap) - roic
    d = (b - b.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC level (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roiclvl_126d_slope_v101_signal(roic):
    b = roic
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE level (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roelvl_126d_slope_v102_signal(roe):
    b = roe
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA level (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roalvl_126d_slope_v103_signal(roa):
    b = roa
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS level (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roslvl_126d_slope_v104_signal(ros):
    b = ros
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicz_126d_slope_v105_signal(roic):
    b = _z(roic, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roez_126d_slope_v106_signal(roe):
    b = _z(roe, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roaz_126d_slope_v107_signal(roa):
    b = _z(roa, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rosz_126d_slope_v108_signal(ros):
    b = _z(ros, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC rank (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicrank_126d_slope_v109_signal(roic):
    b = _rank(roic, 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE rank (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roerank_126d_slope_v110_signal(roe):
    b = _rank(roe, 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA rank (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roarank_126d_slope_v111_signal(roa):
    b = _rank(roa, 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS rank (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rosrank_126d_slope_v112_signal(ros):
    b = _rank(ros, 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC fast/slow EMA ratio (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicema_126d_slope_v113_signal(roic):
    fast = roic.ewm(span=42, min_periods=15).mean()
    slow = roic.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE z fast/slow EMA ratio (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roeema_126d_slope_v114_signal(roe):
    fast = roe.ewm(span=21, min_periods=8).mean()
    slow = roe.ewm(span=126, min_periods=42).mean()
    b = _z(_safe_div(fast, slow), 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA fast/slow EMA ratio (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roaema_126d_slope_v115_signal(roa):
    fast = roa.ewm(span=42, min_periods=15).mean()
    slow = roa.ewm(span=126, min_periods=42).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS fast/slow EMA ratio (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rosema_126d_slope_v116_signal(ros):
    fast = ros.ewm(span=42, min_periods=15).mean()
    slow = ros.ewm(span=252, min_periods=63).mean()
    b = _safe_div(fast, slow)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC stability (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicstab_126d_slope_v117_signal(roic):
    b = _stability(roic, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE stability (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roestab_126d_slope_v118_signal(roe):
    b = _stability(roe, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA stability (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roastab_126d_slope_v119_signal(roa):
    b = _stability(roa, 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS stability (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rosstab_126d_slope_v120_signal(ros):
    b = _stability(ros, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC mid (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicmid_126d_slope_v121_signal(roic):
    hi = roic.rolling(504, min_periods=126).max()
    lo = roic.rolling(504, min_periods=126).min()
    b = (roic - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE mid (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roemid_126d_slope_v122_signal(roe):
    hi = roe.rolling(504, min_periods=126).max()
    lo = roe.rolling(504, min_periods=126).min()
    b = (roe - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA range-pos (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roarngpos_126d_slope_v123_signal(roa):
    hi = roa.rolling(252, min_periods=63).max()
    lo = roa.rolling(252, min_periods=63).min()
    b = (roa - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS range-pos (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rosrngpos_126d_slope_v124_signal(ros):
    hi = ros.rolling(252, min_periods=63).max()
    lo = ros.rolling(252, min_periods=63).min()
    b = (ros - lo) / (hi - lo).replace(0, np.nan)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROA ratio (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicroaspr_126d_slope_v125_signal(roic, roa):
    b = _safe_div(roic, roa.abs() + 0.01)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROA z-spread (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roeroaspr_126d_slope_v126_signal(roe, roa):
    b = _z(roe, 252) - _z(roa, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROS z-spread (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicrosspr_126d_slope_v127_signal(roic, ros):
    b = _z(roic, 252) - _z(ros, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roerosspr_126d_slope_v128_signal(roe, ros):
    b = roe - ros
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROA leverage (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_levmult_126d_slope_v129_signal(roe, roa):
    b = _safe_div(roe, roa)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC/ROS turn (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_capturn_126d_slope_v130_signal(roic, ros):
    b = _safe_div(roic, ros)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE/ROIC (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roeoroic_126d_slope_v131_signal(roe, roic):
    b = _safe_div(roe, roic)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC-ROA spread z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicroazspr_126d_slope_v132_signal(roic, roa):
    b = _z(roic - roa, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE-ROS spread z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roerosz_126d_slope_v133_signal(roe, ros):
    b = _z(roe - ros, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite mean (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_compmean_126d_slope_v134_signal(roic, roe, roa, ros):
    b = (roic + roe + roa + ros) / 4.0
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 3-metric mean (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_compq_126d_slope_v135_signal(roic, roe, roa):
    b = (roic + roe + roa) / 3.0
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross range (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_xdisp_126d_slope_v136_signal(roic, roa, ros):
    st = pd.concat([roic, roa, ros], axis=1)
    b = st.max(axis=1) - st.min(axis=1)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_compz_126d_slope_v137_signal(roic, roe, roa, ros):
    b = _z((roic + roe + roa + ros) / 4.0, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_nioic_126d_slope_v138_signal(netinc, invcap):
    b = _safe_div(netinc, invcap)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_nioe_126d_slope_v139_signal(netinc, equity):
    b = _safe_div(netinc, equity)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/invcap z (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_nioicz_126d_slope_v140_signal(netinc, invcap):
    b = _z(_safe_div(netinc, invcap), 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of netinc/equity rank (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_nioerank_126d_slope_v141_signal(netinc, equity):
    b = _rank(_safe_div(netinc, equity), 504)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log invcap (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_invcaplog_126d_slope_v142_signal(invcap):
    b = np.log(invcap.replace(0, np.nan))
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log equity (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_eqlog_126d_slope_v143_signal(equity):
    b = np.log(equity.replace(0, np.nan))
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC x invcap-growth (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicpercap_126d_slope_v144_signal(roic, invcap):
    g = (np.log(invcap.replace(0, np.nan)) - np.log(invcap.shift(126).replace(0, np.nan)))
    b = roic * np.tanh(5.0 * g)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE x equity-growth (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roeperq_126d_slope_v145_signal(roe, equity):
    g = (np.log(equity.replace(0, np.nan)) - np.log(equity.shift(126).replace(0, np.nan)))
    b = roe * np.tanh(5.0 * g)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC 126 slope (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicsl126_126d_slope_v146_signal(roic):
    b = _slope(roic, 126)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROE 126 slope (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roesl126_126d_slope_v147_signal(roe):
    b = _slope(roe, 126)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROA 252 slope (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roasl252_126d_slope_v148_signal(roa):
    b = _slope(roa, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROS 252 slope (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_rossl252_126d_slope_v149_signal(ros):
    b = _slope(ros, 252)
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ROIC accounting gap (ROC window 126d)
def f30rc_f30_return_on_capital_trajectory_roicgap_126d_slope_v150_signal(netinc, invcap, roic):
    b = _safe_div(netinc, invcap) - roic
    d = (b - b.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rc_f30_return_on_capital_trajectory_roiclvl_21d_slope_v001_signal,
    f30rc_f30_return_on_capital_trajectory_roelvl_21d_slope_v002_signal,
    f30rc_f30_return_on_capital_trajectory_roalvl_21d_slope_v003_signal,
    f30rc_f30_return_on_capital_trajectory_roslvl_21d_slope_v004_signal,
    f30rc_f30_return_on_capital_trajectory_roicz_21d_slope_v005_signal,
    f30rc_f30_return_on_capital_trajectory_roez_21d_slope_v006_signal,
    f30rc_f30_return_on_capital_trajectory_roaz_21d_slope_v007_signal,
    f30rc_f30_return_on_capital_trajectory_rosz_21d_slope_v008_signal,
    f30rc_f30_return_on_capital_trajectory_roicrank_21d_slope_v009_signal,
    f30rc_f30_return_on_capital_trajectory_roerank_21d_slope_v010_signal,
    f30rc_f30_return_on_capital_trajectory_roarank_21d_slope_v011_signal,
    f30rc_f30_return_on_capital_trajectory_rosrank_21d_slope_v012_signal,
    f30rc_f30_return_on_capital_trajectory_roicema_21d_slope_v013_signal,
    f30rc_f30_return_on_capital_trajectory_roeema_21d_slope_v014_signal,
    f30rc_f30_return_on_capital_trajectory_roaema_21d_slope_v015_signal,
    f30rc_f30_return_on_capital_trajectory_rosema_21d_slope_v016_signal,
    f30rc_f30_return_on_capital_trajectory_roicstab_21d_slope_v017_signal,
    f30rc_f30_return_on_capital_trajectory_roestab_21d_slope_v018_signal,
    f30rc_f30_return_on_capital_trajectory_roastab_21d_slope_v019_signal,
    f30rc_f30_return_on_capital_trajectory_rosstab_21d_slope_v020_signal,
    f30rc_f30_return_on_capital_trajectory_roicmid_21d_slope_v021_signal,
    f30rc_f30_return_on_capital_trajectory_roemid_21d_slope_v022_signal,
    f30rc_f30_return_on_capital_trajectory_roarngpos_21d_slope_v023_signal,
    f30rc_f30_return_on_capital_trajectory_rosrngpos_21d_slope_v024_signal,
    f30rc_f30_return_on_capital_trajectory_roicroaspr_21d_slope_v025_signal,
    f30rc_f30_return_on_capital_trajectory_roeroaspr_21d_slope_v026_signal,
    f30rc_f30_return_on_capital_trajectory_roicrosspr_21d_slope_v027_signal,
    f30rc_f30_return_on_capital_trajectory_roerosspr_21d_slope_v028_signal,
    f30rc_f30_return_on_capital_trajectory_levmult_21d_slope_v029_signal,
    f30rc_f30_return_on_capital_trajectory_capturn_21d_slope_v030_signal,
    f30rc_f30_return_on_capital_trajectory_roeoroic_21d_slope_v031_signal,
    f30rc_f30_return_on_capital_trajectory_roicroazspr_21d_slope_v032_signal,
    f30rc_f30_return_on_capital_trajectory_roerosz_21d_slope_v033_signal,
    f30rc_f30_return_on_capital_trajectory_compmean_21d_slope_v034_signal,
    f30rc_f30_return_on_capital_trajectory_compq_21d_slope_v035_signal,
    f30rc_f30_return_on_capital_trajectory_xdisp_21d_slope_v036_signal,
    f30rc_f30_return_on_capital_trajectory_compz_21d_slope_v037_signal,
    f30rc_f30_return_on_capital_trajectory_nioic_21d_slope_v038_signal,
    f30rc_f30_return_on_capital_trajectory_nioe_21d_slope_v039_signal,
    f30rc_f30_return_on_capital_trajectory_nioicz_21d_slope_v040_signal,
    f30rc_f30_return_on_capital_trajectory_nioerank_21d_slope_v041_signal,
    f30rc_f30_return_on_capital_trajectory_invcaplog_21d_slope_v042_signal,
    f30rc_f30_return_on_capital_trajectory_eqlog_21d_slope_v043_signal,
    f30rc_f30_return_on_capital_trajectory_roicpercap_21d_slope_v044_signal,
    f30rc_f30_return_on_capital_trajectory_roeperq_21d_slope_v045_signal,
    f30rc_f30_return_on_capital_trajectory_roicsl126_21d_slope_v046_signal,
    f30rc_f30_return_on_capital_trajectory_roesl126_21d_slope_v047_signal,
    f30rc_f30_return_on_capital_trajectory_roasl252_21d_slope_v048_signal,
    f30rc_f30_return_on_capital_trajectory_rossl252_21d_slope_v049_signal,
    f30rc_f30_return_on_capital_trajectory_roicgap_21d_slope_v050_signal,
    f30rc_f30_return_on_capital_trajectory_roiclvl_63d_slope_v051_signal,
    f30rc_f30_return_on_capital_trajectory_roelvl_63d_slope_v052_signal,
    f30rc_f30_return_on_capital_trajectory_roalvl_63d_slope_v053_signal,
    f30rc_f30_return_on_capital_trajectory_roslvl_63d_slope_v054_signal,
    f30rc_f30_return_on_capital_trajectory_roicz_63d_slope_v055_signal,
    f30rc_f30_return_on_capital_trajectory_roez_63d_slope_v056_signal,
    f30rc_f30_return_on_capital_trajectory_roaz_63d_slope_v057_signal,
    f30rc_f30_return_on_capital_trajectory_rosz_63d_slope_v058_signal,
    f30rc_f30_return_on_capital_trajectory_roicrank_63d_slope_v059_signal,
    f30rc_f30_return_on_capital_trajectory_roerank_63d_slope_v060_signal,
    f30rc_f30_return_on_capital_trajectory_roarank_63d_slope_v061_signal,
    f30rc_f30_return_on_capital_trajectory_rosrank_63d_slope_v062_signal,
    f30rc_f30_return_on_capital_trajectory_roicema_63d_slope_v063_signal,
    f30rc_f30_return_on_capital_trajectory_roeema_63d_slope_v064_signal,
    f30rc_f30_return_on_capital_trajectory_roaema_63d_slope_v065_signal,
    f30rc_f30_return_on_capital_trajectory_rosema_63d_slope_v066_signal,
    f30rc_f30_return_on_capital_trajectory_roicstab_63d_slope_v067_signal,
    f30rc_f30_return_on_capital_trajectory_roestab_63d_slope_v068_signal,
    f30rc_f30_return_on_capital_trajectory_roastab_63d_slope_v069_signal,
    f30rc_f30_return_on_capital_trajectory_rosstab_63d_slope_v070_signal,
    f30rc_f30_return_on_capital_trajectory_roicmid_63d_slope_v071_signal,
    f30rc_f30_return_on_capital_trajectory_roemid_63d_slope_v072_signal,
    f30rc_f30_return_on_capital_trajectory_roarngpos_63d_slope_v073_signal,
    f30rc_f30_return_on_capital_trajectory_rosrngpos_63d_slope_v074_signal,
    f30rc_f30_return_on_capital_trajectory_roicroaspr_63d_slope_v075_signal,
    f30rc_f30_return_on_capital_trajectory_roeroaspr_63d_slope_v076_signal,
    f30rc_f30_return_on_capital_trajectory_roicrosspr_63d_slope_v077_signal,
    f30rc_f30_return_on_capital_trajectory_roerosspr_63d_slope_v078_signal,
    f30rc_f30_return_on_capital_trajectory_levmult_63d_slope_v079_signal,
    f30rc_f30_return_on_capital_trajectory_capturn_63d_slope_v080_signal,
    f30rc_f30_return_on_capital_trajectory_roeoroic_63d_slope_v081_signal,
    f30rc_f30_return_on_capital_trajectory_roicroazspr_63d_slope_v082_signal,
    f30rc_f30_return_on_capital_trajectory_roerosz_63d_slope_v083_signal,
    f30rc_f30_return_on_capital_trajectory_compmean_63d_slope_v084_signal,
    f30rc_f30_return_on_capital_trajectory_compq_63d_slope_v085_signal,
    f30rc_f30_return_on_capital_trajectory_xdisp_63d_slope_v086_signal,
    f30rc_f30_return_on_capital_trajectory_compz_63d_slope_v087_signal,
    f30rc_f30_return_on_capital_trajectory_nioic_63d_slope_v088_signal,
    f30rc_f30_return_on_capital_trajectory_nioe_63d_slope_v089_signal,
    f30rc_f30_return_on_capital_trajectory_nioicz_63d_slope_v090_signal,
    f30rc_f30_return_on_capital_trajectory_nioerank_63d_slope_v091_signal,
    f30rc_f30_return_on_capital_trajectory_invcaplog_63d_slope_v092_signal,
    f30rc_f30_return_on_capital_trajectory_eqlog_63d_slope_v093_signal,
    f30rc_f30_return_on_capital_trajectory_roicpercap_63d_slope_v094_signal,
    f30rc_f30_return_on_capital_trajectory_roeperq_63d_slope_v095_signal,
    f30rc_f30_return_on_capital_trajectory_roicsl126_63d_slope_v096_signal,
    f30rc_f30_return_on_capital_trajectory_roesl126_63d_slope_v097_signal,
    f30rc_f30_return_on_capital_trajectory_roasl252_63d_slope_v098_signal,
    f30rc_f30_return_on_capital_trajectory_rossl252_63d_slope_v099_signal,
    f30rc_f30_return_on_capital_trajectory_roicgap_63d_slope_v100_signal,
    f30rc_f30_return_on_capital_trajectory_roiclvl_126d_slope_v101_signal,
    f30rc_f30_return_on_capital_trajectory_roelvl_126d_slope_v102_signal,
    f30rc_f30_return_on_capital_trajectory_roalvl_126d_slope_v103_signal,
    f30rc_f30_return_on_capital_trajectory_roslvl_126d_slope_v104_signal,
    f30rc_f30_return_on_capital_trajectory_roicz_126d_slope_v105_signal,
    f30rc_f30_return_on_capital_trajectory_roez_126d_slope_v106_signal,
    f30rc_f30_return_on_capital_trajectory_roaz_126d_slope_v107_signal,
    f30rc_f30_return_on_capital_trajectory_rosz_126d_slope_v108_signal,
    f30rc_f30_return_on_capital_trajectory_roicrank_126d_slope_v109_signal,
    f30rc_f30_return_on_capital_trajectory_roerank_126d_slope_v110_signal,
    f30rc_f30_return_on_capital_trajectory_roarank_126d_slope_v111_signal,
    f30rc_f30_return_on_capital_trajectory_rosrank_126d_slope_v112_signal,
    f30rc_f30_return_on_capital_trajectory_roicema_126d_slope_v113_signal,
    f30rc_f30_return_on_capital_trajectory_roeema_126d_slope_v114_signal,
    f30rc_f30_return_on_capital_trajectory_roaema_126d_slope_v115_signal,
    f30rc_f30_return_on_capital_trajectory_rosema_126d_slope_v116_signal,
    f30rc_f30_return_on_capital_trajectory_roicstab_126d_slope_v117_signal,
    f30rc_f30_return_on_capital_trajectory_roestab_126d_slope_v118_signal,
    f30rc_f30_return_on_capital_trajectory_roastab_126d_slope_v119_signal,
    f30rc_f30_return_on_capital_trajectory_rosstab_126d_slope_v120_signal,
    f30rc_f30_return_on_capital_trajectory_roicmid_126d_slope_v121_signal,
    f30rc_f30_return_on_capital_trajectory_roemid_126d_slope_v122_signal,
    f30rc_f30_return_on_capital_trajectory_roarngpos_126d_slope_v123_signal,
    f30rc_f30_return_on_capital_trajectory_rosrngpos_126d_slope_v124_signal,
    f30rc_f30_return_on_capital_trajectory_roicroaspr_126d_slope_v125_signal,
    f30rc_f30_return_on_capital_trajectory_roeroaspr_126d_slope_v126_signal,
    f30rc_f30_return_on_capital_trajectory_roicrosspr_126d_slope_v127_signal,
    f30rc_f30_return_on_capital_trajectory_roerosspr_126d_slope_v128_signal,
    f30rc_f30_return_on_capital_trajectory_levmult_126d_slope_v129_signal,
    f30rc_f30_return_on_capital_trajectory_capturn_126d_slope_v130_signal,
    f30rc_f30_return_on_capital_trajectory_roeoroic_126d_slope_v131_signal,
    f30rc_f30_return_on_capital_trajectory_roicroazspr_126d_slope_v132_signal,
    f30rc_f30_return_on_capital_trajectory_roerosz_126d_slope_v133_signal,
    f30rc_f30_return_on_capital_trajectory_compmean_126d_slope_v134_signal,
    f30rc_f30_return_on_capital_trajectory_compq_126d_slope_v135_signal,
    f30rc_f30_return_on_capital_trajectory_xdisp_126d_slope_v136_signal,
    f30rc_f30_return_on_capital_trajectory_compz_126d_slope_v137_signal,
    f30rc_f30_return_on_capital_trajectory_nioic_126d_slope_v138_signal,
    f30rc_f30_return_on_capital_trajectory_nioe_126d_slope_v139_signal,
    f30rc_f30_return_on_capital_trajectory_nioicz_126d_slope_v140_signal,
    f30rc_f30_return_on_capital_trajectory_nioerank_126d_slope_v141_signal,
    f30rc_f30_return_on_capital_trajectory_invcaplog_126d_slope_v142_signal,
    f30rc_f30_return_on_capital_trajectory_eqlog_126d_slope_v143_signal,
    f30rc_f30_return_on_capital_trajectory_roicpercap_126d_slope_v144_signal,
    f30rc_f30_return_on_capital_trajectory_roeperq_126d_slope_v145_signal,
    f30rc_f30_return_on_capital_trajectory_roicsl126_126d_slope_v146_signal,
    f30rc_f30_return_on_capital_trajectory_roesl126_126d_slope_v147_signal,
    f30rc_f30_return_on_capital_trajectory_roasl252_126d_slope_v148_signal,
    f30rc_f30_return_on_capital_trajectory_rossl252_126d_slope_v149_signal,
    f30rc_f30_return_on_capital_trajectory_roicgap_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RETURN_ON_CAPITAL_TRAJECTORY_REGISTRY_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f30_return_on_capital_trajectory_2nd_derivatives_001_150_claude: %d features pass" % n_features)
