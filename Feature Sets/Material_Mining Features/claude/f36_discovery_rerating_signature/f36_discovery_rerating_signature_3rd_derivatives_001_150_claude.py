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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _jerk(s, w):
    # 2nd math derivative (jerk): acceleration of the rate of change over w days
    # = (s - s.shift(w)) - (s.shift(w) - s.shift(2w)) = s - 2*s.shift(w) + s.shift(2w)
    return s - 2.0 * s.shift(w) + s.shift(2 * w)


# ===== folder domain primitives: discovery / re-rating signature =====
def _f36_dollar_vol(closeadj, volume):
    return (closeadj * volume).astype(float)


def _f36_breakout(closeadj, w):
    prior_hi = closeadj.shift(1).rolling(w, min_periods=max(2, w // 2)).max()
    return closeadj / prior_hi.replace(0, np.nan) - 1.0


def _f36_base_pos(closeadj, w):
    hi = _rmax(closeadj, w)
    lo = _rmin(closeadj, w)
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f36_vol_surge(closeadj, volume, w):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(w, min_periods=max(2, w // 2)).mean()
    return np.log(dv.replace(0, np.nan) / base.replace(0, np.nan))


def _f36_ret_vol(closeadj, w):
    return closeadj.pct_change().rolling(w, min_periods=max(2, w // 2)).std()


def _f36_vol_expand(closeadj, short, long):
    vs = _f36_ret_vol(closeadj, short)
    vl = _f36_ret_vol(closeadj, long)
    return vs / vl.replace(0, np.nan)


def _f36_range_atr(high, low, closeadj, w):
    rng = (high - low)
    return (rng.rolling(w, min_periods=max(2, w // 2)).mean()) / closeadj.replace(0, np.nan)


def _f36_thrust(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


# ============================================================
# JERK features = 2nd math derivative (acceleration of the rate) of a base
# signature. Each def computes its base quantity inline, then applies _jerk
# over an ROC window appropriate to the base window. Facets diversified so
# in-file pairwise corr stays <= 0.97.

# --- jerks of breakout-from-base ---

def f36dr_f36_discovery_rerating_signature_brk63_21d_jerk_v001_signal(closeadj):
    base = _f36_breakout(closeadj, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk126_21d_jerk_v002_signal(closeadj):
    base = _f36_breakout(closeadj, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk252_63d_jerk_v003_signal(closeadj):
    base = _f36_breakout(closeadj, 252)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk21_5d_jerk_v004_signal(closeadj):
    base = _f36_breakout(closeadj, 21)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkz126_21d_jerk_v005_signal(closeadj):
    base = _z(_f36_breakout(closeadj, 126), 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkrnk63_21d_jerk_v006_signal(closeadj):
    base = _rank(_f36_breakout(closeadj, 63), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos63_21d_jerk_v007_signal(closeadj):
    base = _f36_base_pos(closeadj, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos126_21d_jerk_v008_signal(closeadj):
    base = _f36_base_pos(closeadj, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos252_63d_jerk_v009_signal(closeadj):
    base = _f36_base_pos(closeadj, 252)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_baseposspr_21d_jerk_v010_signal(closeadj):
    base = _f36_base_pos(closeadj, 63) - _f36_base_pos(closeadj, 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of volume surge / liquidity ---

def f36dr_f36_discovery_rerating_signature_vsurge63_21d_jerk_v011_signal(closeadj, volume):
    base = _f36_vol_surge(closeadj, volume, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvz63_21d_jerk_v012_signal(closeadj, volume):
    base = _z(_f36_dollar_vol(closeadj, volume), 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvmom252_21d_jerk_v013_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                  / dv.rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvrank252_21d_jerk_v014_signal(closeadj, volume):
    base = _rank(_f36_dollar_vol(closeadj, volume), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_liqstep_21d_jerk_v015_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
                  / dv.shift(63).rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_turnaccel_21d_jerk_v016_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(63, min_periods=21).mean()
    base = _z(short / long.replace(0, np.nan), 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_amihud_21d_jerk_v017_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    illiq = closeadj.pct_change().abs() / dv.replace(0, np.nan)
    base = -np.log(illiq.rolling(21, min_periods=10).mean().replace(0, np.nan)
                   / illiq.rolling(126, min_periods=63).mean().replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvcv_21d_jerk_v018_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(63, min_periods=21).std() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of volatility expansion ---

def f36dr_f36_discovery_rerating_signature_volexp21v126_21d_jerk_v019_signal(closeadj):
    base = _f36_vol_expand(closeadj, 21, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexp5v63_5d_jerk_v020_signal(closeadj):
    base = _f36_vol_expand(closeadj, 5, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_rngexp21v126_21d_jerk_v021_signal(high, low, closeadj):
    base = _f36_range_atr(high, low, closeadj, 21) / _f36_range_atr(high, low, closeadj, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volregime_21d_jerk_v022_signal(closeadj):
    base = _rank(_f36_ret_vol(closeadj, 21), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_parkexp_21d_jerk_v023_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    base = np.sqrt(hl.rolling(21, min_periods=10).mean()) / np.sqrt(hl.rolling(126, min_periods=63).mean()).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volasym_21d_jerk_v024_signal(closeadj):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0).rolling(63, min_periods=21).std()
    dn = ret.where(ret < 0).rolling(63, min_periods=21).std()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volofvol_21d_jerk_v025_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    base = v.rolling(63, min_periods=21).std() / v.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of price thrust / momentum ---

def f36dr_f36_discovery_rerating_signature_thrust63_21d_jerk_v026_signal(closeadj):
    base = _f36_thrust(closeadj, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust126_21d_jerk_v027_signal(closeadj):
    base = _f36_thrust(closeadj, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust21_5d_jerk_v028_signal(closeadj):
    base = _f36_thrust(closeadj, 21)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust252_63d_jerk_v029_signal(closeadj):
    base = _f36_thrust(closeadj, 252)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_newhirate_21d_jerk_v030_signal(closeadj):
    hi = _rmax(closeadj, 63)
    base = np.log(hi.replace(0, np.nan) / hi.shift(21).replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_staircase_21d_jerk_v031_signal(closeadj):
    hi = _rmax(closeadj, 126)
    base = np.log(hi.replace(0, np.nan) / hi.shift(63).replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dsh252_21d_jerk_v032_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = closeadj.rolling(252, min_periods=126).apply(_f, raw=True)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of composite signatures ---

def f36dr_f36_discovery_rerating_signature_tripleblend_21d_jerk_v033_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = np.tanh((brk + vs + ve) / 3.0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_wcomp_21d_jerk_v034_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = 0.5 * brk + 0.3 * vs + 0.2 * ve
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_spike63_21d_jerk_v035_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    base = brk * vs * ve
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_minlink_21d_jerk_v036_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = pd.concat([brk, vs, ve], axis=1).min(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_maxlink_21d_jerk_v037_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = pd.concat([brk, vs, ve], axis=1).max(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_breadth_21d_jerk_v038_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 63), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 126), 126)
    ve = _z(_f36_vol_expand(closeadj, 5, 63), 126)
    base = pd.concat([brk, vs, ve], axis=1).mean(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_agree_21d_jerk_v039_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = pd.concat([brk, vs, ve], axis=1).std(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkvol63_21d_jerk_v040_signal(closeadj, volume):
    base = _f36_breakout(closeadj, 63) * _f36_vol_surge(closeadj, volume, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkvolat126_21d_jerk_v041_signal(closeadj):
    base = _f36_breakout(closeadj, 126) * (_f36_vol_expand(closeadj, 21, 126) - 1.0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volvolat63_21d_jerk_v042_signal(closeadj, volume):
    base = _f36_vol_surge(closeadj, volume, 63) * (_f36_vol_expand(closeadj, 5, 63) - 1.0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_geomtriple_21d_jerk_v043_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-6
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-6
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-6
    base = (brk * vs * ve) ** (1.0 / 3.0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_harmcomp_21d_jerk_v044_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-4
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-4
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-4
    base = 3.0 / (1.0 / brk + 1.0 / vs + 1.0 / ve)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of confirmed thrust / sustained re-rating ---

def f36dr_f36_discovery_rerating_signature_thrustconf63_21d_jerk_v045_signal(closeadj, volume):
    base = _f36_thrust(closeadj, 63) * (1.0 + _f36_vol_surge(closeadj, volume, 126).clip(lower=0))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustqual126_21d_jerk_v046_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    hi = _rmax(closeadj, 126)
    pain = ((hi - closeadj) / hi.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    base = thr / (pain + 0.05)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_efficiency_21d_jerk_v047_signal(closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    base = net / path.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_smoothrise_21d_jerk_v048_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    dd = (_rmax(closeadj, 126) - _rmin(closeadj, 126)) / _rmax(closeadj, 126).replace(0, np.nan)
    base = thr / (dd + 0.05)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustagree_21d_jerk_v049_signal(closeadj):
    t1 = np.sign(_f36_thrust(closeadj, 21))
    t2 = np.sign(_f36_thrust(closeadj, 63))
    t3 = np.sign(_f36_thrust(closeadj, 126))
    base = (t1 + t2 + t3) / 3.0 * _f36_thrust(closeadj, 63).abs()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- jerks of interactions ---

def f36dr_f36_discovery_rerating_signature_coilbreak_21d_jerk_v050_signal(closeadj):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    width = (hi - lo) / closeadj.replace(0, np.nan)
    tight = 1.0 / (width + 0.02)
    base = tight * _f36_breakout(closeadj, 63).clip(lower=0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_accumthrust_21d_jerk_v051_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    base = _f36_thrust(closeadj, 63) * (0.5 + bal)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_updownvol_21d_jerk_v052_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    base = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_vwbreak126_21d_jerk_v053_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 126) + 0.5
    base = brk * dvr
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_stealth_21d_jerk_v054_signal(closeadj, volume):
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    base = vs * (1.0 - _f36_base_pos(closeadj, 126)).clip(lower=0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkliq_21d_jerk_v055_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
                 / dv.rolling(252, min_periods=126).mean().replace(0, np.nan)).clip(lower=0)
    base = brk * liq
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_coilexp_21d_jerk_v056_signal(closeadj):
    base = _f36_base_pos(closeadj, 63) * (_f36_vol_expand(closeadj, 5, 63) - 1.0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_amp252_21d_jerk_v057_signal(closeadj):
    base = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_headroom252_21d_jerk_v058_signal(closeadj):
    base = np.log(_rmax(closeadj, 252).replace(0, np.nan) / closeadj.replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_rngatr5_5d_jerk_v059_signal(high, low, closeadj):
    base = _f36_range_atr(high, low, closeadj, 5)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_intraenergy_21d_jerk_v060_signal(high, low, closeadj):
    base = _f36_range_atr(high, low, closeadj, 21) / _f36_ret_vol(closeadj, 21).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# --- more diversified jerks (continue to 150) ---

def f36dr_f36_discovery_rerating_signature_brk63_5d_jerk_v061_signal(closeadj):
    base = _f36_breakout(closeadj, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk126_63d_jerk_v062_signal(closeadj):
    base = _f36_breakout(closeadj, 126)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_vsurge63_5d_jerk_v063_signal(closeadj, volume):
    base = _f36_vol_surge(closeadj, volume, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexp21v126_5d_jerk_v064_signal(closeadj):
    base = _f36_vol_expand(closeadj, 21, 126)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust63_5d_jerk_v065_signal(closeadj):
    base = _f36_thrust(closeadj, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos63_5d_jerk_v066_signal(closeadj):
    base = _f36_base_pos(closeadj, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvrank252_5d_jerk_v067_signal(closeadj, volume):
    base = _rank(_f36_dollar_vol(closeadj, volume), 252)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_ampratio_63d_jerk_v068_signal(closeadj):
    amp252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    amp504 = (_rmax(closeadj, 504) - _rmin(closeadj, 504)) / closeadj.replace(0, np.nan)
    base = amp252 / amp504.replace(0, np.nan)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_wcomp_5d_jerk_v069_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = 0.5 * brk + 0.3 * vs + 0.2 * ve
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_parkexp_5d_jerk_v070_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    base = np.sqrt(hl.rolling(21, min_periods=10).mean()) / np.sqrt(hl.rolling(126, min_periods=63).mean()).replace(0, np.nan)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volconc_21d_jerk_v071_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    total = dv.rolling(63, min_periods=21).sum()
    top5 = dv.rolling(63, min_periods=21).apply(
        lambda a: np.sort(a)[-5:].sum() if len(a) >= 5 else np.nan, raw=True)
    base = top5 / total.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexprnk_21d_jerk_v072_signal(closeadj):
    base = _rank(_f36_vol_expand(closeadj, 21, 63), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexpmom_21d_jerk_v073_signal(closeadj):
    ratio = _f36_vol_expand(closeadj, 21, 126)
    base = ratio - ratio.shift(63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_leadgap_21d_jerk_v074_signal(closeadj, volume):
    base = _rank(_f36_dollar_vol(closeadj, volume), 252) - _rank(_f36_breakout(closeadj, 126), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkamp_21d_jerk_v075_signal(closeadj):
    amp = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    base = _f36_breakout(closeadj, 126) / amp.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkdecay_21d_jerk_v076_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    base = brk - brk.rolling(63, min_periods=21).max()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_surgerange_21d_jerk_v077_signal(closeadj, volume, high, low):
    vs = _f36_vol_surge(closeadj, volume, 63)
    rexp = _f36_range_atr(high, low, closeadj, 5) / _f36_range_atr(high, low, closeadj, 63).replace(0, np.nan) - 1.0
    base = vs * rexp
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkpark_21d_jerk_v078_signal(closeadj, high, low):
    brk = _f36_breakout(closeadj, 126)
    hl = np.sqrt(((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(21, min_periods=10).mean())
    base = brk / hl.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_climax_21d_jerk_v079_signal(closeadj, volume):
    thr = _rank(_f36_thrust(closeadj, 21), 252) + 0.5
    vs = _rank(_f36_vol_surge(closeadj, volume, 63), 252) + 0.5
    ve = _rank(_f36_vol_expand(closeadj, 5, 63), 252) + 0.5
    base = thr * vs * ve
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_energybudget_21d_jerk_v080_signal(closeadj):
    base = closeadj.pct_change().rolling(63, min_periods=21).skew()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_excesssurge_21d_jerk_v081_signal(closeadj, volume):
    base = _f36_vol_surge(closeadj, volume, 63) - 20.0 * _f36_thrust(closeadj, 5).abs()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust126_63d_jerk_v082_signal(closeadj):
    base = _f36_thrust(closeadj, 126)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkbreadth_21d_jerk_v083_signal(closeadj):
    b1 = _f36_breakout(closeadj, 21)
    b2 = _f36_breakout(closeadj, 63)
    b3 = _f36_breakout(closeadj, 126)
    b4 = _f36_breakout(closeadj, 252)
    base = pd.concat([b1, b2, b3, b4], axis=1).mean(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkdisp_21d_jerk_v084_signal(closeadj):
    b1 = _f36_breakout(closeadj, 21)
    b2 = _f36_breakout(closeadj, 63)
    b3 = _f36_breakout(closeadj, 126)
    b4 = _f36_breakout(closeadj, 252)
    base = pd.concat([b1, b2, b3, b4], axis=1).std(axis=1)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_engine_21d_jerk_v085_signal(closeadj, volume):
    thr = _f36_thrust(closeadj, 63).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
                 / dv.rolling(252, min_periods=126).mean().replace(0, np.nan)).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    base = thr * (1.0 + liq) * (1.0 + ve)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_tripthrust_21d_jerk_v086_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    thr = _f36_thrust(closeadj, 63).clip(lower=0)
    base = brk * vs * thr
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_fullscore_21d_jerk_v087_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-4
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-4
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-4
    thr = _f36_thrust(closeadj, 63).clip(lower=0) + 1e-4
    base = (brk * vs * ve * thr) ** 0.25
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_vebrkz_21d_jerk_v088_signal(closeadj):
    raw = _f36_breakout(closeadj, 126) * (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    base = _z(raw, 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_confrank_21d_jerk_v089_signal(closeadj):
    base = _rank(_f36_thrust(closeadj, 21) * _f36_vol_expand(closeadj, 5, 63), 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_durability_21d_jerk_v090_signal(closeadj):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    decay = (brk.shift(21) - brk).clip(lower=0) + 0.01
    base = brk / decay
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_headline_21d_jerk_v091_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = np.tanh((brk + vs + ve) / 3.0).ewm(span=10, min_periods=5).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk21_21d_jerk_v092_signal(closeadj):
    base = _f36_breakout(closeadj, 21)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brk504_63d_jerk_v093_signal(closeadj):
    base = _f36_breakout(closeadj, 504)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos252_21d_jerk_v094_signal(closeadj):
    base = _f36_base_pos(closeadj, 252)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvz63_5d_jerk_v095_signal(closeadj, volume):
    base = _z(_f36_dollar_vol(closeadj, volume), 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexp5v63_21d_jerk_v096_signal(closeadj):
    base = _f36_vol_expand(closeadj, 5, 63)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust21_21d_jerk_v097_signal(closeadj):
    base = _f36_thrust(closeadj, 21)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_spike126_21d_jerk_v098_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 252).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 126).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 5, 63) - 1.0).clip(lower=0)
    base = brk * vs * ve
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkvol126_21d_jerk_v099_signal(closeadj, volume):
    base = _f36_breakout(closeadj, 126) * _f36_vol_surge(closeadj, volume, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_accumbreak_21d_jerk_v100_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    base = bal * _f36_breakout(closeadj, 126).clip(lower=0)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustconf21_5d_jerk_v101_signal(closeadj, volume):
    base = _f36_thrust(closeadj, 21) * (1.0 + _f36_vol_surge(closeadj, volume, 63).clip(lower=0))
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_loaded_21d_jerk_v102_signal(closeadj, volume):
    bp = _f36_base_pos(closeadj, 63)
    vr = _rank(_f36_dollar_vol(closeadj, volume), 126) + 0.5
    ver = _rank(_f36_vol_expand(closeadj, 21, 126), 126) + 0.5
    base = bp * vr * ver
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volliq_21d_jerk_v103_signal(closeadj, volume):
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / dv.rolling(126, min_periods=63).mean().replace(0, np.nan)).clip(lower=0)
    base = ve * liq
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_pullback_21d_jerk_v104_signal(closeadj):
    pull = closeadj / _rmax(closeadj, 21).replace(0, np.nan) - 1.0
    base = pull * _f36_base_pos(closeadj, 126)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkqual_21d_jerk_v105_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(126, min_periods=63).max()
    brk = (closeadj / prior_hi.replace(0, np.nan) - 1.0).clip(lower=0)
    held = (closeadj > prior_hi).astype(float).rolling(21, min_periods=10).mean()
    base = brk * held
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_baseposspr_5d_jerk_v106_signal(closeadj):
    base = _f36_base_pos(closeadj, 63) - _f36_base_pos(closeadj, 252)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_liqexp_21d_jerk_v107_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = (dv.rolling(63, min_periods=21).mean()
            / dv.rolling(252, min_periods=126).mean().replace(0, np.nan)).ewm(span=10, min_periods=5).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_voltrend_21d_jerk_v108_signal(closeadj, volume):
    ldv = np.log(_f36_dollar_vol(closeadj, volume).replace(0, np.nan))
    idx = pd.Series(np.arange(len(ldv), dtype=float), index=ldv.index)
    w = 63
    mx = idx.rolling(w, min_periods=21).mean()
    my = ldv.rolling(w, min_periods=21).mean()
    cov = (idx * ldv).rolling(w, min_periods=21).mean() - mx * my
    varx = (idx * idx).rolling(w, min_periods=21).mean() - mx * mx
    base = cov / varx.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_rngblow_21d_jerk_v109_signal(high, low, closeadj):
    amp = _f36_range_atr(high, low, closeadj, 5)
    typ = amp.rolling(252, min_periods=126).median()
    base = (amp / typ.replace(0, np.nan) - 1.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_proxmom_5d_jerk_v110_signal(closeadj):
    base = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_vwnewhi_21d_jerk_v111_signal(closeadj, volume):
    hi = _rmax(closeadj, 63)
    at_hi = (closeadj >= hi * 0.999).astype(float)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 126) + 0.5
    base = (at_hi * dvr).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dirvol63_21d_jerk_v112_signal(closeadj, volume):
    base = _z(_f36_dollar_vol(closeadj, volume), 63) * np.sign(_f36_thrust(closeadj, 5))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_obvslope_21d_jerk_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    obv = (np.sign(ret) * dv).cumsum()
    base = (obv - obv.shift(21)) / (21.0 * dv.rolling(63, min_periods=21).mean().replace(0, np.nan))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_upenergy_21d_jerk_v114_signal(closeadj):
    ret = closeadj.pct_change()
    base = ret.clip(lower=0).rolling(21, min_periods=10).mean() / _f36_ret_vol(closeadj, 63).replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dirvolat21_21d_jerk_v115_signal(closeadj):
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    thr = _f36_thrust(closeadj, 21)
    base = ve * np.sign(thr) * thr.abs() ** 0.5
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_coil63_21d_jerk_v116_signal(closeadj):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    width = (hi - lo) / closeadj.replace(0, np.nan)
    base = 1.0 / (width + 0.02)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkwidth_21d_jerk_v117_signal(closeadj, high, low):
    prior_hi = closeadj.shift(1).rolling(126, min_periods=63).max()
    atr = (high - low).rolling(21, min_periods=10).mean()
    base = (closeadj - prior_hi) / atr.replace(0, np.nan)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustcoil_21d_jerk_v118_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    hi = closeadj.shift(126).rolling(63, min_periods=21).max()
    lo = closeadj.shift(126).rolling(63, min_periods=21).min()
    width = (hi - lo) / hi.replace(0, np.nan)
    base = thr / (width + 0.05)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexp21v126_63d_jerk_v119_signal(closeadj):
    base = _f36_vol_expand(closeadj, 21, 126)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_vsurge63_63d_jerk_v120_signal(closeadj, volume):
    base = _f36_vol_surge(closeadj, volume, 63)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos63_63d_jerk_v121_signal(closeadj):
    base = _f36_base_pos(closeadj, 63)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_parkregime_63d_jerk_v122_signal(high, low):
    hl = np.sqrt(((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(63, min_periods=21).mean())
    med = hl.rolling(252, min_periods=126).median()
    base = _rank((hl - med) / med.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_intraenergy_5d_jerk_v123_signal(high, low, closeadj):
    base = _f36_range_atr(high, low, closeadj, 21) / _f36_ret_vol(closeadj, 21).replace(0, np.nan)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_streakliq_21d_jerk_v124_signal(closeadj, volume):
    hi = _rmax(closeadj, 126)
    near = (closeadj >= hi * 0.97).astype(float)
    streak = near.rolling(21, min_periods=10).sum()
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252) + 0.5
    base = streak * dvr
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustzconf_21d_jerk_v125_signal(closeadj, volume):
    thrz = _z(_f36_thrust(closeadj, 63), 252)
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    base = thrz * (0.5 + bal)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_rngthrust_21d_jerk_v126_signal(high, low, closeadj):
    short = _f36_range_atr(high, low, closeadj, 21)
    long = _f36_range_atr(high, low, closeadj, 126)
    base = (short / long.replace(0, np.nan) - 1.0) * np.sign(_f36_thrust(closeadj, 5))
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_sigdelta_21d_jerk_v127_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    comp = (brk + vs + ve) / 3.0
    base = comp - comp.shift(21)
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_impulse_21d_jerk_v128_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    comp = (brk + vs + ve) / 3.0
    base = comp - comp.ewm(span=42, min_periods=21).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_leadership_21d_jerk_v129_signal(closeadj, volume):
    hi = _rmax(closeadj, 252)
    fresh = (closeadj >= hi * 0.999).astype(float)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252) + 0.5
    base = (fresh * dvr).rolling(126, min_periods=63).mean()
    b = _jerk(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkrnk63_5d_jerk_v130_signal(closeadj):
    base = _rank(_f36_breakout(closeadj, 63), 252)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volasym_5d_jerk_v131_signal(closeadj):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0).rolling(63, min_periods=21).std()
    dn = ret.where(ret < 0).rolling(63, min_periods=21).std()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_squeezerel_63d_jerk_v132_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    floor = v.rolling(252, min_periods=126).min()
    base = np.log(v.replace(0, np.nan) / floor.replace(0, np.nan))
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkvolat126_5d_jerk_v133_signal(closeadj):
    base = _f36_breakout(closeadj, 126) * (_f36_vol_expand(closeadj, 21, 126) - 1.0)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_geomtriple_5d_jerk_v134_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-6
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-6
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-6
    base = (brk * vs * ve) ** (1.0 / 3.0)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_newhirate_63d_jerk_v135_signal(closeadj):
    hi = _rmax(closeadj, 63)
    base = np.log(hi.replace(0, np.nan) / hi.shift(21).replace(0, np.nan))
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_sustain252_63d_jerk_v136_signal(closeadj):
    base = _f36_thrust(closeadj, 252) * _f36_base_pos(closeadj, 252)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvmom252_5d_jerk_v137_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                  / dv.rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volexprnk_5d_jerk_v138_signal(closeadj):
    base = _rank(_f36_vol_expand(closeadj, 21, 63), 252)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrustagree_63d_jerk_v139_signal(closeadj):
    t1 = np.sign(_f36_thrust(closeadj, 21))
    t2 = np.sign(_f36_thrust(closeadj, 63))
    t3 = np.sign(_f36_thrust(closeadj, 126))
    base = (t1 + t2 + t3) / 3.0 * _f36_thrust(closeadj, 63).abs()
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_minlink_5d_jerk_v140_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = pd.concat([brk, vs, ve], axis=1).min(axis=1)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_maxlink_5d_jerk_v141_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = pd.concat([brk, vs, ve], axis=1).max(axis=1)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_spike63_5d_jerk_v142_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 5, 63) - 1.0).clip(lower=0)
    base = brk * vs * ve
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_brkvol63_5d_jerk_v143_signal(closeadj, volume):
    base = _f36_breakout(closeadj, 63) * _f36_vol_surge(closeadj, volume, 63)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_thrust126_5d_jerk_v144_signal(closeadj):
    base = _f36_thrust(closeadj, 126)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_basepos126_5d_jerk_v145_signal(closeadj):
    base = _f36_base_pos(closeadj, 126)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_volregime_5d_jerk_v146_signal(closeadj):
    base = _rank(_f36_ret_vol(closeadj, 21), 252)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_amp252_63d_jerk_v147_signal(closeadj):
    base = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_headroom252_63d_jerk_v148_signal(closeadj):
    base = np.log(_rmax(closeadj, 252).replace(0, np.nan) / closeadj.replace(0, np.nan))
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_dvcv_5d_jerk_v149_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(63, min_periods=21).std() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = _jerk(base, 5)
    return b.replace([np.inf, -np.inf], np.nan)


def f36dr_f36_discovery_rerating_signature_tripleblend_63d_jerk_v150_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    base = np.tanh((brk + vs + ve) / 3.0)
    b = _jerk(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36dr_f36_discovery_rerating_signature_brk63_21d_jerk_v001_signal,
    f36dr_f36_discovery_rerating_signature_brk126_21d_jerk_v002_signal,
    f36dr_f36_discovery_rerating_signature_brk252_63d_jerk_v003_signal,
    f36dr_f36_discovery_rerating_signature_brk21_5d_jerk_v004_signal,
    f36dr_f36_discovery_rerating_signature_brkz126_21d_jerk_v005_signal,
    f36dr_f36_discovery_rerating_signature_brkrnk63_21d_jerk_v006_signal,
    f36dr_f36_discovery_rerating_signature_basepos63_21d_jerk_v007_signal,
    f36dr_f36_discovery_rerating_signature_basepos126_21d_jerk_v008_signal,
    f36dr_f36_discovery_rerating_signature_basepos252_63d_jerk_v009_signal,
    f36dr_f36_discovery_rerating_signature_baseposspr_21d_jerk_v010_signal,
    f36dr_f36_discovery_rerating_signature_vsurge63_21d_jerk_v011_signal,
    f36dr_f36_discovery_rerating_signature_dvz63_21d_jerk_v012_signal,
    f36dr_f36_discovery_rerating_signature_dvmom252_21d_jerk_v013_signal,
    f36dr_f36_discovery_rerating_signature_dvrank252_21d_jerk_v014_signal,
    f36dr_f36_discovery_rerating_signature_liqstep_21d_jerk_v015_signal,
    f36dr_f36_discovery_rerating_signature_turnaccel_21d_jerk_v016_signal,
    f36dr_f36_discovery_rerating_signature_amihud_21d_jerk_v017_signal,
    f36dr_f36_discovery_rerating_signature_dvcv_21d_jerk_v018_signal,
    f36dr_f36_discovery_rerating_signature_volexp21v126_21d_jerk_v019_signal,
    f36dr_f36_discovery_rerating_signature_volexp5v63_5d_jerk_v020_signal,
    f36dr_f36_discovery_rerating_signature_rngexp21v126_21d_jerk_v021_signal,
    f36dr_f36_discovery_rerating_signature_volregime_21d_jerk_v022_signal,
    f36dr_f36_discovery_rerating_signature_parkexp_21d_jerk_v023_signal,
    f36dr_f36_discovery_rerating_signature_volasym_21d_jerk_v024_signal,
    f36dr_f36_discovery_rerating_signature_volofvol_21d_jerk_v025_signal,
    f36dr_f36_discovery_rerating_signature_thrust63_21d_jerk_v026_signal,
    f36dr_f36_discovery_rerating_signature_thrust126_21d_jerk_v027_signal,
    f36dr_f36_discovery_rerating_signature_thrust21_5d_jerk_v028_signal,
    f36dr_f36_discovery_rerating_signature_thrust252_63d_jerk_v029_signal,
    f36dr_f36_discovery_rerating_signature_newhirate_21d_jerk_v030_signal,
    f36dr_f36_discovery_rerating_signature_staircase_21d_jerk_v031_signal,
    f36dr_f36_discovery_rerating_signature_dsh252_21d_jerk_v032_signal,
    f36dr_f36_discovery_rerating_signature_tripleblend_21d_jerk_v033_signal,
    f36dr_f36_discovery_rerating_signature_wcomp_21d_jerk_v034_signal,
    f36dr_f36_discovery_rerating_signature_spike63_21d_jerk_v035_signal,
    f36dr_f36_discovery_rerating_signature_minlink_21d_jerk_v036_signal,
    f36dr_f36_discovery_rerating_signature_maxlink_21d_jerk_v037_signal,
    f36dr_f36_discovery_rerating_signature_breadth_21d_jerk_v038_signal,
    f36dr_f36_discovery_rerating_signature_agree_21d_jerk_v039_signal,
    f36dr_f36_discovery_rerating_signature_brkvol63_21d_jerk_v040_signal,
    f36dr_f36_discovery_rerating_signature_brkvolat126_21d_jerk_v041_signal,
    f36dr_f36_discovery_rerating_signature_volvolat63_21d_jerk_v042_signal,
    f36dr_f36_discovery_rerating_signature_geomtriple_21d_jerk_v043_signal,
    f36dr_f36_discovery_rerating_signature_harmcomp_21d_jerk_v044_signal,
    f36dr_f36_discovery_rerating_signature_thrustconf63_21d_jerk_v045_signal,
    f36dr_f36_discovery_rerating_signature_thrustqual126_21d_jerk_v046_signal,
    f36dr_f36_discovery_rerating_signature_efficiency_21d_jerk_v047_signal,
    f36dr_f36_discovery_rerating_signature_smoothrise_21d_jerk_v048_signal,
    f36dr_f36_discovery_rerating_signature_thrustagree_21d_jerk_v049_signal,
    f36dr_f36_discovery_rerating_signature_coilbreak_21d_jerk_v050_signal,
    f36dr_f36_discovery_rerating_signature_accumthrust_21d_jerk_v051_signal,
    f36dr_f36_discovery_rerating_signature_updownvol_21d_jerk_v052_signal,
    f36dr_f36_discovery_rerating_signature_vwbreak126_21d_jerk_v053_signal,
    f36dr_f36_discovery_rerating_signature_stealth_21d_jerk_v054_signal,
    f36dr_f36_discovery_rerating_signature_brkliq_21d_jerk_v055_signal,
    f36dr_f36_discovery_rerating_signature_coilexp_21d_jerk_v056_signal,
    f36dr_f36_discovery_rerating_signature_amp252_21d_jerk_v057_signal,
    f36dr_f36_discovery_rerating_signature_headroom252_21d_jerk_v058_signal,
    f36dr_f36_discovery_rerating_signature_rngatr5_5d_jerk_v059_signal,
    f36dr_f36_discovery_rerating_signature_intraenergy_21d_jerk_v060_signal,
    f36dr_f36_discovery_rerating_signature_brk63_5d_jerk_v061_signal,
    f36dr_f36_discovery_rerating_signature_brk126_63d_jerk_v062_signal,
    f36dr_f36_discovery_rerating_signature_vsurge63_5d_jerk_v063_signal,
    f36dr_f36_discovery_rerating_signature_volexp21v126_5d_jerk_v064_signal,
    f36dr_f36_discovery_rerating_signature_thrust63_5d_jerk_v065_signal,
    f36dr_f36_discovery_rerating_signature_basepos63_5d_jerk_v066_signal,
    f36dr_f36_discovery_rerating_signature_dvrank252_5d_jerk_v067_signal,
    f36dr_f36_discovery_rerating_signature_ampratio_63d_jerk_v068_signal,
    f36dr_f36_discovery_rerating_signature_wcomp_5d_jerk_v069_signal,
    f36dr_f36_discovery_rerating_signature_parkexp_5d_jerk_v070_signal,
    f36dr_f36_discovery_rerating_signature_volconc_21d_jerk_v071_signal,
    f36dr_f36_discovery_rerating_signature_volexprnk_21d_jerk_v072_signal,
    f36dr_f36_discovery_rerating_signature_volexpmom_21d_jerk_v073_signal,
    f36dr_f36_discovery_rerating_signature_leadgap_21d_jerk_v074_signal,
    f36dr_f36_discovery_rerating_signature_brkamp_21d_jerk_v075_signal,
    f36dr_f36_discovery_rerating_signature_brkdecay_21d_jerk_v076_signal,
    f36dr_f36_discovery_rerating_signature_surgerange_21d_jerk_v077_signal,
    f36dr_f36_discovery_rerating_signature_brkpark_21d_jerk_v078_signal,
    f36dr_f36_discovery_rerating_signature_climax_21d_jerk_v079_signal,
    f36dr_f36_discovery_rerating_signature_energybudget_21d_jerk_v080_signal,
    f36dr_f36_discovery_rerating_signature_excesssurge_21d_jerk_v081_signal,
    f36dr_f36_discovery_rerating_signature_thrust126_63d_jerk_v082_signal,
    f36dr_f36_discovery_rerating_signature_brkbreadth_21d_jerk_v083_signal,
    f36dr_f36_discovery_rerating_signature_brkdisp_21d_jerk_v084_signal,
    f36dr_f36_discovery_rerating_signature_engine_21d_jerk_v085_signal,
    f36dr_f36_discovery_rerating_signature_tripthrust_21d_jerk_v086_signal,
    f36dr_f36_discovery_rerating_signature_fullscore_21d_jerk_v087_signal,
    f36dr_f36_discovery_rerating_signature_vebrkz_21d_jerk_v088_signal,
    f36dr_f36_discovery_rerating_signature_confrank_21d_jerk_v089_signal,
    f36dr_f36_discovery_rerating_signature_durability_21d_jerk_v090_signal,
    f36dr_f36_discovery_rerating_signature_headline_21d_jerk_v091_signal,
    f36dr_f36_discovery_rerating_signature_brk21_21d_jerk_v092_signal,
    f36dr_f36_discovery_rerating_signature_brk504_63d_jerk_v093_signal,
    f36dr_f36_discovery_rerating_signature_basepos252_21d_jerk_v094_signal,
    f36dr_f36_discovery_rerating_signature_dvz63_5d_jerk_v095_signal,
    f36dr_f36_discovery_rerating_signature_volexp5v63_21d_jerk_v096_signal,
    f36dr_f36_discovery_rerating_signature_thrust21_21d_jerk_v097_signal,
    f36dr_f36_discovery_rerating_signature_spike126_21d_jerk_v098_signal,
    f36dr_f36_discovery_rerating_signature_brkvol126_21d_jerk_v099_signal,
    f36dr_f36_discovery_rerating_signature_accumbreak_21d_jerk_v100_signal,
    f36dr_f36_discovery_rerating_signature_thrustconf21_5d_jerk_v101_signal,
    f36dr_f36_discovery_rerating_signature_loaded_21d_jerk_v102_signal,
    f36dr_f36_discovery_rerating_signature_volliq_21d_jerk_v103_signal,
    f36dr_f36_discovery_rerating_signature_pullback_21d_jerk_v104_signal,
    f36dr_f36_discovery_rerating_signature_brkqual_21d_jerk_v105_signal,
    f36dr_f36_discovery_rerating_signature_baseposspr_5d_jerk_v106_signal,
    f36dr_f36_discovery_rerating_signature_liqexp_21d_jerk_v107_signal,
    f36dr_f36_discovery_rerating_signature_voltrend_21d_jerk_v108_signal,
    f36dr_f36_discovery_rerating_signature_rngblow_21d_jerk_v109_signal,
    f36dr_f36_discovery_rerating_signature_proxmom_5d_jerk_v110_signal,
    f36dr_f36_discovery_rerating_signature_vwnewhi_21d_jerk_v111_signal,
    f36dr_f36_discovery_rerating_signature_dirvol63_21d_jerk_v112_signal,
    f36dr_f36_discovery_rerating_signature_obvslope_21d_jerk_v113_signal,
    f36dr_f36_discovery_rerating_signature_upenergy_21d_jerk_v114_signal,
    f36dr_f36_discovery_rerating_signature_dirvolat21_21d_jerk_v115_signal,
    f36dr_f36_discovery_rerating_signature_coil63_21d_jerk_v116_signal,
    f36dr_f36_discovery_rerating_signature_brkwidth_21d_jerk_v117_signal,
    f36dr_f36_discovery_rerating_signature_thrustcoil_21d_jerk_v118_signal,
    f36dr_f36_discovery_rerating_signature_volexp21v126_63d_jerk_v119_signal,
    f36dr_f36_discovery_rerating_signature_vsurge63_63d_jerk_v120_signal,
    f36dr_f36_discovery_rerating_signature_basepos63_63d_jerk_v121_signal,
    f36dr_f36_discovery_rerating_signature_parkregime_63d_jerk_v122_signal,
    f36dr_f36_discovery_rerating_signature_intraenergy_5d_jerk_v123_signal,
    f36dr_f36_discovery_rerating_signature_streakliq_21d_jerk_v124_signal,
    f36dr_f36_discovery_rerating_signature_thrustzconf_21d_jerk_v125_signal,
    f36dr_f36_discovery_rerating_signature_rngthrust_21d_jerk_v126_signal,
    f36dr_f36_discovery_rerating_signature_sigdelta_21d_jerk_v127_signal,
    f36dr_f36_discovery_rerating_signature_impulse_21d_jerk_v128_signal,
    f36dr_f36_discovery_rerating_signature_leadership_21d_jerk_v129_signal,
    f36dr_f36_discovery_rerating_signature_brkrnk63_5d_jerk_v130_signal,
    f36dr_f36_discovery_rerating_signature_volasym_5d_jerk_v131_signal,
    f36dr_f36_discovery_rerating_signature_squeezerel_63d_jerk_v132_signal,
    f36dr_f36_discovery_rerating_signature_brkvolat126_5d_jerk_v133_signal,
    f36dr_f36_discovery_rerating_signature_geomtriple_5d_jerk_v134_signal,
    f36dr_f36_discovery_rerating_signature_newhirate_63d_jerk_v135_signal,
    f36dr_f36_discovery_rerating_signature_sustain252_63d_jerk_v136_signal,
    f36dr_f36_discovery_rerating_signature_dvmom252_5d_jerk_v137_signal,
    f36dr_f36_discovery_rerating_signature_volexprnk_5d_jerk_v138_signal,
    f36dr_f36_discovery_rerating_signature_thrustagree_63d_jerk_v139_signal,
    f36dr_f36_discovery_rerating_signature_minlink_5d_jerk_v140_signal,
    f36dr_f36_discovery_rerating_signature_maxlink_5d_jerk_v141_signal,
    f36dr_f36_discovery_rerating_signature_spike63_5d_jerk_v142_signal,
    f36dr_f36_discovery_rerating_signature_brkvol63_5d_jerk_v143_signal,
    f36dr_f36_discovery_rerating_signature_thrust126_5d_jerk_v144_signal,
    f36dr_f36_discovery_rerating_signature_basepos126_5d_jerk_v145_signal,
    f36dr_f36_discovery_rerating_signature_volregime_5d_jerk_v146_signal,
    f36dr_f36_discovery_rerating_signature_amp252_63d_jerk_v147_signal,
    f36dr_f36_discovery_rerating_signature_headroom252_63d_jerk_v148_signal,
    f36dr_f36_discovery_rerating_signature_dvcv_5d_jerk_v149_signal,
    f36dr_f36_discovery_rerating_signature_tripleblend_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_DISCOVERY_RERATING_SIGNATURE_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f36_discovery_rerating_signature_3rd_derivatives_001_150_claude: %d features pass" % n_features)
