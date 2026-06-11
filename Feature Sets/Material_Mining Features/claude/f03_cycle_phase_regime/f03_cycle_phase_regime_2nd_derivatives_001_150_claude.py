import inspect
import numpy as np
import pandas as pd


def _f03_trend(c, w):
    return np.log(c.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()


def _f03_regime_state(c, w):
    lp = np.log(c.replace(0, np.nan))
    tr = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sign(lp - tr)


def _f03_runlen(state_bool):
    s = state_bool.astype(float)
    grp = (s != s.shift(1)).cumsum()
    run = s.groupby(grp).cumcount() + 1.0
    return run.where(s == 1, other=0.0)


def _f03_signrun(c):
    r = np.sign(np.log(c.replace(0, np.nan)).diff())
    grp = (r != r.shift(1)).cumsum()
    cnt = r.groupby(grp).cumcount() + 1.0
    return cnt * r


def _f03_above_frac(c, w_state, w_count):
    st = (_f03_regime_state(c, w_state) > 0).astype(float)
    return st.rolling(w_count, min_periods=max(1, w_count // 2)).mean()


def _f03_trans_intensity(c, w_state, w_count):
    lp = np.log(c.replace(0, np.nan))
    tr = lp.rolling(w_state, min_periods=max(1, w_state // 2)).mean()
    gap = lp - tr
    st = np.sign(gap)
    flip = (st != st.shift(1)).astype(float)
    cross_mag = (gap - gap.shift(1)).abs()
    w = (flip * cross_mag).where(st.notna() & st.shift(1).notna(), other=np.nan)
    cnt = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    n = cnt.rolling(w_count, min_periods=max(1, w_count // 2)).sum()
    inten = w.rolling(w_count, min_periods=max(1, w_count // 2)).sum()
    return n + 25.0 * inten


def _f03_updown_asym(c, w):
    r = np.log(c.replace(0, np.nan)).diff()
    up = (r > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).sum()
    dn = (r < 0).astype(float).rolling(w, min_periods=max(1, w // 2)).sum()
    return (up - dn) / float(w)


def f03cp_f03_cycle_phase_regime_statesm_252d_slope_v001_signal(closeadj):
    base = _f03_regime_state(closeadj, 252).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_statesm_252d_slope_v002_signal(closeadj):
    base = _f03_regime_state(closeadj, 252).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_statesm504_504d_slope_v003_signal(closeadj):
    base = _f03_regime_state(closeadj, 504).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_statesm504_504d_slope_v004_signal(closeadj):
    base = _f03_regime_state(closeadj, 504).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_agree_252d_slope_v005_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    base = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_agree_252d_slope_v006_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    base = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dualtrend_252d_slope_v007_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = np.sign(lp.rolling(63, min_periods=21).mean() - lp.rolling(252, min_periods=126).mean()).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dualtrend_252d_slope_v008_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = np.sign(lp.rolling(63, min_periods=21).mean() - lp.rolling(252, min_periods=126).mean()).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfrac_252d_slope_v009_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 252)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfrac_252d_slope_v010_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 252)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfrac126_252d_slope_v011_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 126)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfrac126_252d_slope_v012_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 126)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomrun_252d_slope_v013_signal(closeadj):
    base = np.log1p(_f03_runlen(_f03_regime_state(closeadj, 252) > 0))
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomrun_252d_slope_v014_signal(closeadj):
    base = np.log1p(_f03_runlen(_f03_regime_state(closeadj, 252) > 0))
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_extremephase_504d_slope_v015_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    bm = _f03_runlen(st > 0).rolling(504, min_periods=252).max(); bs = _f03_runlen(st < 0).rolling(504, min_periods=252).max()
    base = np.log1p(bm) - np.log1p(bs)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_extremephase_504d_slope_v016_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    bm = _f03_runlen(st > 0).rolling(504, min_periods=252).max(); bs = _f03_runlen(st < 0).rolling(504, min_periods=252).max()
    base = np.log1p(bm) - np.log1p(bs)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipint_252d_slope_v017_signal(closeadj):
    base = _f03_trans_intensity(closeadj, 252, 252)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipint_252d_slope_v018_signal(closeadj):
    base = _f03_trans_intensity(closeadj, 252, 252)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipint126_252d_slope_v019_signal(closeadj):
    base = _f03_trans_intensity(closeadj, 252, 126)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipint126_252d_slope_v020_signal(closeadj):
    base = _f03_trans_intensity(closeadj, 252, 126)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_entropy_252d_slope_v021_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    p = st.rolling(252, min_periods=126).mean().clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_entropy_252d_slope_v022_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    p = st.rolling(252, min_periods=126).mean().clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_updnasym63_63d_slope_v023_signal(closeadj):
    base = _f03_updown_asym(closeadj, 63).rolling(10, min_periods=5).mean()
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_updnasym63_63d_slope_v024_signal(closeadj):
    base = _f03_updown_asym(closeadj, 63).rolling(10, min_periods=5).mean()
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_updnasym252_252d_slope_v025_signal(closeadj):
    base = _f03_updown_asym(closeadj, 252)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_updnasym252_252d_slope_v026_signal(closeadj):
    base = _f03_updown_asym(closeadj, 252)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runmaturity_252d_slope_v027_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); cur = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = cur / cur.rolling(504, min_periods=126).max().replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runmaturity_252d_slope_v028_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); cur = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = cur / cur.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_conviction_252d_slope_v029_signal(closeadj):
    base = _f03_regime_state(closeadj, 252).rolling(252, min_periods=126).mean().abs()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_conviction_252d_slope_v030_signal(closeadj):
    base = _f03_regime_state(closeadj, 252).rolling(252, min_periods=126).mean().abs()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clockdiverge_252d_slope_v031_signal(closeadj):
    base = (_f03_regime_state(closeadj, 252) - _f03_regime_state(closeadj, 1260)).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clockdiverge_252d_slope_v032_signal(closeadj):
    base = (_f03_regime_state(closeadj, 252) - _f03_regime_state(closeadj, 1260)).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clockconflict_252d_slope_v033_signal(closeadj):
    a = _f03_regime_state(closeadj, 252); bb = _f03_regime_state(closeadj, 504)
    conflict = (a != bb).astype(float).where(a.notna() & bb.notna(), other=np.nan)
    base = conflict.rolling(252, min_periods=126).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clockconflict_252d_slope_v034_signal(closeadj):
    a = _f03_regime_state(closeadj, 252); bb = _f03_regime_state(closeadj, 504)
    conflict = (a != bb).astype(float).where(a.notna() & bb.notna(), other=np.nan)
    base = conflict.rolling(252, min_periods=126).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dirpurity63_63d_slope_v035_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(63, min_periods=21).mean().abs().rolling(10, min_periods=5).mean()
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dirpurity63_63d_slope_v036_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(63, min_periods=21).mean().abs().rolling(10, min_periods=5).mean()
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dirpurity252_252d_slope_v037_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(252, min_periods=126).mean().abs().rolling(10, min_periods=5).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dirpurity252_252d_slope_v038_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(252, min_periods=126).mean().abs().rolling(10, min_periods=5).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_massasym252_252d_slope_v039_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    um = r.clip(lower=0).rolling(252, min_periods=126).sum(); dm = (-r.clip(upper=0)).rolling(252, min_periods=126).sum()
    base = (um - dm) / (um + dm).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_massasym252_252d_slope_v040_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    um = r.clip(lower=0).rolling(252, min_periods=126).sum(); dm = (-r.clip(upper=0)).rolling(252, min_periods=126).sum()
    base = (um - dm) / (um + dm).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_massasym63_63d_slope_v041_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    um = r.clip(lower=0).rolling(63, min_periods=21).sum(); dm = (-r.clip(upper=0)).rolling(63, min_periods=21).sum()
    base = (um - dm) / (um + dm).replace(0, np.nan)
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_massasym63_63d_slope_v042_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    um = r.clip(lower=0).rolling(63, min_periods=21).sum(); dm = (-r.clip(upper=0)).rolling(63, min_periods=21).sum()
    base = (um - dm) / (um + dm).replace(0, np.nan)
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_retskew252_252d_slope_v043_signal(closeadj):
    base = np.log(closeadj.replace(0, np.nan)).diff().rolling(252, min_periods=126).skew()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_retskew252_252d_slope_v044_signal(closeadj):
    base = np.log(closeadj.replace(0, np.nan)).diff().rolling(252, min_periods=126).skew()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_volasym_252d_slope_v045_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    uv = r.where(r > 0).rolling(252, min_periods=63).std(); dv = r.where(r < 0).rolling(252, min_periods=63).std()
    base = (dv - uv) / (dv + uv).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_volasym_252d_slope_v046_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    uv = r.where(r > 0).rolling(252, min_periods=63).std(); dv = r.where(r < 0).rolling(252, min_periods=63).std()
    base = (dv - uv) / (dv + uv).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_efficiency_252d_slope_v047_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(252, min_periods=126).sum(); net = r.rolling(252, min_periods=126).sum().abs()
    base = net / travel.replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_efficiency_252d_slope_v048_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(252, min_periods=126).sum(); net = r.rolling(252, min_periods=126).sum().abs()
    base = net / travel.replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_roughness63_63d_slope_v049_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(63, min_periods=21).sum(); net = r.rolling(63, min_periods=21).sum().abs()
    base = net / travel.replace(0, np.nan)
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_roughness63_63d_slope_v050_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(63, min_periods=21).sum(); net = r.rolling(63, min_periods=21).sum().abs()
    base = net / travel.replace(0, np.nan)
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signtiltspr_252d_slope_v051_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(21, min_periods=10).mean() - sg.rolling(252, min_periods=126).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signtiltspr_252d_slope_v052_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.rolling(21, min_periods=10).mean() - sg.rolling(252, min_periods=126).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_stateprod_252d_slope_v053_signal(closeadj):
    sf = _f03_regime_state(closeadj, 252).rolling(21, min_periods=10).mean(); ssl = _f03_regime_state(closeadj, 1260).rolling(21, min_periods=10).mean()
    base = sf * ssl
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_stateprod_252d_slope_v054_signal(closeadj):
    sf = _f03_regime_state(closeadj, 252).rolling(21, min_periods=10).mean(); ssl = _f03_regime_state(closeadj, 1260).rolling(21, min_periods=10).mean()
    base = sf * ssl
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clocklag_252d_slope_v055_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 126) - _f03_above_frac(closeadj, 1260, 126)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_clocklag_252d_slope_v056_signal(closeadj):
    base = _f03_above_frac(closeadj, 252, 126) - _f03_above_frac(closeadj, 1260, 126)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_medrun_252d_slope_v057_signal(closeadj):
    base = np.log1p(_f03_signrun(closeadj).abs().rolling(252, min_periods=126).mean())
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_medrun_252d_slope_v058_signal(closeadj):
    base = np.log1p(_f03_signrun(closeadj).abs().rolling(252, min_periods=126).mean())
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_fullnet_252d_slope_v059_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    au = ((s1 > 0) & (s2 > 0) & (s3 > 0)).astype(float); ad = ((s1 < 0) & (s2 < 0) & (s3 < 0)).astype(float)
    base = (au - ad).rolling(252, min_periods=126).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_fullnet_252d_slope_v060_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    au = ((s1 > 0) & (s2 > 0) & (s3 > 0)).astype(float); ad = ((s1 < 0) & (s2 < 0) & (s3 < 0)).astype(float)
    base = (au - ad).rolling(252, min_periods=126).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signautocorr63_63d_slope_v061_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); s0 = sg; s1 = sg.shift(1)
    cov = (s0 * s1).rolling(63, min_periods=21).mean() - s0.rolling(63, min_periods=21).mean() * s1.rolling(63, min_periods=21).mean()
    base = cov / s0.rolling(63, min_periods=21).var().replace(0, np.nan)
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signautocorr63_63d_slope_v062_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); s0 = sg; s1 = sg.shift(1)
    cov = (s0 * s1).rolling(63, min_periods=21).mean() - s0.rolling(63, min_periods=21).mean() * s1.rolling(63, min_periods=21).mean()
    base = cov / s0.rolling(63, min_periods=21).var().replace(0, np.nan)
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_mombreadth_252d_slope_v063_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)), np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    base = sig.mean(axis=1).rolling(10, min_periods=5).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_mombreadth_252d_slope_v064_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)), np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    base = sig.mean(axis=1).rolling(10, min_periods=5).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_momdisagree_252d_slope_v065_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)), np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    base = sig.std(axis=1).rolling(10, min_periods=5).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_momdisagree_252d_slope_v066_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)), np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    base = sig.std(axis=1).rolling(10, min_periods=5).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_trendagree252_252d_slope_v067_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff(); trend = np.sign(r.rolling(252, min_periods=126).sum())
    base = (np.sign(r) == trend).astype(float).rolling(252, min_periods=126).mean() - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_trendagree252_252d_slope_v068_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff(); trend = np.sign(r.rolling(252, min_periods=126).sum())
    base = (np.sign(r) == trend).astype(float).rolling(252, min_periods=126).mean() - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_chop63_63d_slope_v069_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    daily = lp.diff().abs().rolling(63, min_periods=21).sum(); wk = lp.diff(5).abs().rolling(63, min_periods=21).sum() / 5.0
    base = daily / wk.replace(0, np.nan)
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_chop63_63d_slope_v070_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    daily = lp.diff().abs().rolling(63, min_periods=21).sum(); wk = lp.diff(5).abs().rolling(63, min_periods=21).sum() / 5.0
    base = daily / wk.replace(0, np.nan)
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signema_21d_slope_v071_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signema_21d_slope_v072_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.ewm(span=21, min_periods=10).mean()
    base = base.ewm(span=5, min_periods=3).mean()
    d = base - base.shift(26)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signemadisp_126d_slope_v073_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.ewm(span=21, min_periods=10).mean() - sg.ewm(span=126, min_periods=42).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_signemadisp_126d_slope_v074_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    base = sg.ewm(span=21, min_periods=10).mean() - sg.ewm(span=126, min_periods=42).mean()
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phasepower_252d_slope_v075_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    tilt = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    purity = np.sign(np.log(closeadj.replace(0, np.nan)).diff()).rolling(126, min_periods=63).mean().abs()
    base = tilt * purity
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phasepower_252d_slope_v076_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252); s2 = _f03_regime_state(closeadj, 504); s3 = _f03_regime_state(closeadj, 1260)
    tilt = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    purity = np.sign(np.log(closeadj.replace(0, np.nan)).diff()).rolling(126, min_periods=63).mean().abs()
    base = tilt * purity
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipburst_252d_slope_v077_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float).where(st.notna() & st.shift(1).notna(), other=np.nan)
    sub = flip.rolling(50, min_periods=25).sum()
    base = sub.rolling(252, min_periods=126).std() / sub.rolling(252, min_periods=126).mean().replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_flipburst_252d_slope_v078_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float).where(st.notna() & st.shift(1).notna(), other=np.nan)
    sub = flip.rolling(50, min_periods=25).sum()
    base = sub.rolling(252, min_periods=126).std() / sub.rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfracslope_252d_slope_v079_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 126)
    base = f - f.shift(21)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomfracslope_252d_slope_v080_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 126)
    base = f - f.shift(21)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phasematurity_252d_slope_v081_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = (run / 252.0).clip(upper=2.0)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phasematurity_252d_slope_v082_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = (run / 252.0).clip(upper=2.0)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_doubleabove_252d_slope_v083_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    af = lp > lp.rolling(63, min_periods=21).mean(); asl = lp > lp.rolling(252, min_periods=126).mean()
    base = (af & asl).astype(float).rolling(252, min_periods=126).mean() - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_doubleabove_252d_slope_v084_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    af = lp > lp.rolling(63, min_periods=21).mean(); asl = lp > lp.rolling(252, min_periods=126).mean()
    base = (af & asl).astype(float).rolling(252, min_periods=126).mean() - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_conflictdwell_252d_slope_v085_signal(closeadj):
    sf = _f03_regime_state(closeadj, 252); ssl = _f03_regime_state(closeadj, 504)
    base = np.log1p(_f03_runlen(sf != ssl))
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_conflictdwell_252d_slope_v086_signal(closeadj):
    sf = _f03_regime_state(closeadj, 252); ssl = _f03_regime_state(closeadj, 504)
    base = np.log1p(_f03_runlen(sf != ssl))
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runskew_252d_slope_v087_signal(closeadj):
    base = _f03_signrun(closeadj).abs().rolling(252, min_periods=126).skew()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runskew_252d_slope_v088_signal(closeadj):
    base = _f03_signrun(closeadj).abs().rolling(252, min_periods=126).skew()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_cycdayasym504_504d_slope_v089_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    bd = (st > 0).astype(float).rolling(504, min_periods=252).sum(); bu = (st < 0).astype(float).rolling(504, min_periods=252).sum()
    bo = ((st > 0) & (st.shift(1) <= 0)).astype(float).rolling(504, min_periods=252).sum(); su = ((st < 0) & (st.shift(1) >= 0)).astype(float).rolling(504, min_periods=252).sum()
    ab = bd / (bo + 1.0); abu = bu / (su + 1.0)
    base = (ab - abu) / (ab + abu).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_cycdayasym504_504d_slope_v090_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    bd = (st > 0).astype(float).rolling(504, min_periods=252).sum(); bu = (st < 0).astype(float).rolling(504, min_periods=252).sum()
    bo = ((st > 0) & (st.shift(1) <= 0)).astype(float).rolling(504, min_periods=252).sum(); su = ((st < 0) & (st.shift(1) >= 0)).astype(float).rolling(504, min_periods=252).sum()
    ab = bd / (bo + 1.0); abu = bu / (su + 1.0)
    base = (ab - abu) / (ab + abu).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_legasym252_252d_slope_v091_signal(closeadj):
    hi = closeadj.shift(1).rolling(21, min_periods=10).max(); lo = closeadj.shift(1).rolling(21, min_periods=10).min()
    u = (closeadj > hi).astype(float).rolling(252, min_periods=126).sum(); d = (closeadj < lo).astype(float).rolling(252, min_periods=126).sum()
    base = (u - d) / (u + d).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_legasym252_252d_slope_v092_signal(closeadj):
    hi = closeadj.shift(1).rolling(21, min_periods=10).max(); lo = closeadj.shift(1).rolling(21, min_periods=10).min()
    u = (closeadj > hi).astype(float).rolling(252, min_periods=126).sum(); d = (closeadj < lo).astype(float).rolling(252, min_periods=126).sum()
    base = (u - d) / (u + d).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_semivarasym_504d_slope_v093_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    usv = (r.clip(lower=0) ** 2).rolling(504, min_periods=252).mean(); dsv = (r.clip(upper=0) ** 2).rolling(504, min_periods=252).mean()
    base = (dsv - usv) / (dsv + usv).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_semivarasym_504d_slope_v094_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    usv = (r.clip(lower=0) ** 2).rolling(504, min_periods=252).mean(); dsv = (r.clip(upper=0) ** 2).rolling(504, min_periods=252).mean()
    base = (dsv - usv) / (dsv + usv).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_fastmoveasym_63d_slope_v095_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5); sd = r5.rolling(252, min_periods=126).std()
    fu = (r5 > sd).astype(float).rolling(63, min_periods=21).mean(); fd = (r5 < -sd).astype(float).rolling(63, min_periods=21).mean()
    base = fu - fd
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_fastmoveasym_63d_slope_v096_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5); sd = r5.rolling(252, min_periods=126).std()
    fu = (r5 > sd).astype(float).rolling(63, min_periods=21).mean(); fd = (r5 < -sd).astype(float).rolling(63, min_periods=21).mean()
    base = fu - fd
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_monthasym_504d_slope_v097_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    u = (mo > 0).astype(float).rolling(504, min_periods=252).mean(); d = (mo < 0).astype(float).rolling(504, min_periods=252).mean()
    base = u - d
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_monthasym_504d_slope_v098_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    u = (mo > 0).astype(float).rolling(504, min_periods=252).mean(); d = (mo < 0).astype(float).rolling(504, min_periods=252).mean()
    base = u - d
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_retzerocross63_63d_slope_v099_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    cross = (np.sign(r) != np.sign(r.shift(1))).astype(float).where(r.notna() & r.shift(1).notna(), other=np.nan)
    base = cross.rolling(63, min_periods=21).mean().rolling(10, min_periods=5).mean()
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_retzerocross63_63d_slope_v100_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    cross = (np.sign(r) != np.sign(r.shift(1))).astype(float).where(r.notna() & r.shift(1).notna(), other=np.nan)
    base = cross.rolling(63, min_periods=21).mean().rolling(10, min_periods=5).mean()
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_zerocrossac_252d_slope_v101_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); g0 = gap; g1 = gap.shift(21)
    cov = (g0 * g1).rolling(252, min_periods=126).mean() - g0.rolling(252, min_periods=126).mean() * g1.rolling(252, min_periods=126).mean()
    base = cov / g0.rolling(252, min_periods=126).var().replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_zerocrossac_252d_slope_v102_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); g0 = gap; g1 = gap.shift(21)
    cov = (g0 * g1).rolling(252, min_periods=126).mean() - g0.rolling(252, min_periods=126).mean() * g1.rolling(252, min_periods=126).mean()
    base = cov / g0.rolling(252, min_periods=126).var().replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_streakthrust_63d_slope_v103_signal(closeadj):
    sr = _f03_signrun(closeadj); vol = np.log(closeadj.replace(0, np.nan)).diff().rolling(63, min_periods=21).std()
    base = sr.rolling(21, min_periods=10).mean() * vol
    d = base - base.shift(5)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_streakthrust_63d_slope_v104_signal(closeadj):
    sr = _f03_signrun(closeadj); vol = np.log(closeadj.replace(0, np.nan)).diff().rolling(63, min_periods=21).std()
    base = sr.rolling(21, min_periods=10).mean() * vol
    base = base.ewm(span=21, min_periods=10).mean()
    d = base - base.shift(42)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_uprunpersist_252d_slope_v105_signal(closeadj):
    sr = _f03_signrun(closeadj)
    lu = (sr >= 5).astype(float).rolling(252, min_periods=126).sum(); ld = (sr <= -5).astype(float).rolling(252, min_periods=126).sum()
    base = (lu - ld) / (lu + ld + 5.0)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_uprunpersist_252d_slope_v106_signal(closeadj):
    sr = _f03_signrun(closeadj)
    lu = (sr >= 5).astype(float).rolling(252, min_periods=126).sum(); ld = (sr <= -5).astype(float).rolling(252, min_periods=126).sum()
    base = (lu - ld) / (lu + ld + 5.0)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_maxrunasym_252d_slope_v107_signal(closeadj):
    sr = _f03_signrun(closeadj)
    um = sr.clip(lower=0).rolling(252, min_periods=126).max(); dm = (-sr.clip(upper=0)).rolling(252, min_periods=126).max()
    base = ((um - dm) / (um + dm).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_maxrunasym_252d_slope_v108_signal(closeadj):
    sr = _f03_signrun(closeadj)
    um = sr.clip(lower=0).rolling(252, min_periods=126).max(); dm = (-sr.clip(upper=0)).rolling(252, min_periods=126).max()
    base = ((um - dm) / (um + dm).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runcountasym_252d_slope_v109_signal(closeadj):
    r = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    us = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(252, min_periods=126).sum(); ds = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(252, min_periods=126).sum()
    base = (us - ds) / (us + ds).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runcountasym_252d_slope_v110_signal(closeadj):
    r = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    us = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(252, min_periods=126).sum(); ds = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(252, min_periods=126).sum()
    base = (us - ds) / (us + ds).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_sinceboom_252d_slope_v111_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); enter = (st > 0) & (st.shift(1) <= 0); grp = enter.cumsum()
    base = np.log1p(enter.groupby(grp).cumcount().astype(float).where(grp > 0, other=np.nan))
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_sinceboom_252d_slope_v112_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); enter = (st > 0) & (st.shift(1) <= 0); grp = enter.cumsum()
    base = np.log1p(enter.groupby(grp).cumcount().astype(float).where(grp > 0, other=np.nan))
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tiltmom_252d_slope_v113_signal(closeadj):
    t = _f03_regime_state(closeadj, 252).rolling(126, min_periods=63).mean()
    base = t - t.shift(63)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tiltmom_252d_slope_v114_signal(closeadj):
    t = _f03_regime_state(closeadj, 252).rolling(126, min_periods=63).mean()
    base = t - t.shift(63)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_nettilt1260_1260d_slope_v115_signal(closeadj):
    tr = _f03_trend(closeadj, 1260)
    u = (tr > tr.shift(21)).astype(float).rolling(504, min_periods=252).mean(); d = (tr < tr.shift(21)).astype(float).rolling(504, min_periods=252).mean()
    base = u - d
    d = base - base.shift(63)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_nettilt1260_1260d_slope_v116_signal(closeadj):
    tr = _f03_trend(closeadj, 1260)
    u = (tr > tr.shift(21)).astype(float).rolling(504, min_periods=252).mean(); d = (tr < tr.shift(21)).astype(float).rolling(504, min_periods=252).mean()
    base = u - d
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_cycdayasym1260_1260d_slope_v117_signal(closeadj):
    st = _f03_regime_state(closeadj, 1260)
    bo = (st > 0).astype(float).rolling(1260, min_periods=504).sum(); bu = (st < 0).astype(float).rolling(1260, min_periods=504).sum()
    base = (bo - bu) / (bo + bu).replace(0, np.nan)
    d = base - base.shift(63)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_cycdayasym1260_1260d_slope_v118_signal(closeadj):
    st = _f03_regime_state(closeadj, 1260)
    bo = (st > 0).astype(float).rolling(1260, min_periods=504).sum(); bu = (st < 0).astype(float).rolling(1260, min_periods=504).sum()
    base = (bo - bu) / (bo + bu).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomshare1260_1260d_slope_v119_signal(closeadj):
    base = (_f03_regime_state(closeadj, 1260) > 0).astype(float).rolling(1260, min_periods=504).mean() - 0.5
    d = base - base.shift(63)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_boomshare1260_1260d_slope_v120_signal(closeadj):
    base = (_f03_regime_state(closeadj, 1260) > 0).astype(float).rolling(1260, min_periods=504).mean() - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_whipsaw_252d_slope_v121_signal(closeadj):
    flips = _f03_trans_intensity(closeadj, 252, 252); tilt = _f03_regime_state(closeadj, 252).rolling(252, min_periods=126).mean().abs()
    base = flips / (1.0 + 10.0 * tilt)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_whipsaw_252d_slope_v122_signal(closeadj):
    flips = _f03_trans_intensity(closeadj, 252, 252); tilt = _f03_regime_state(closeadj, 252).rolling(252, min_periods=126).mean().abs()
    base = flips / (1.0 + 10.0 * tilt)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_persistprob_252d_slope_v123_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    stay = ((st == 1) & (st.shift(1) == 1)).astype(float).rolling(252, min_periods=126).sum(); pri = (st.shift(1) == 1).astype(float).rolling(252, min_periods=126).sum()
    base = stay / pri.replace(0, np.nan) - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_persistprob_252d_slope_v124_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    stay = ((st == 1) & (st.shift(1) == 1)).astype(float).rolling(252, min_periods=126).sum(); pri = (st.shift(1) == 1).astype(float).rolling(252, min_periods=126).sum()
    base = stay / pri.replace(0, np.nan) - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runextrank_252d_slope_v125_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = run.rolling(504, min_periods=126).rank(pct=True) - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_runextrank_252d_slope_v126_signal(closeadj):
    st = _f03_regime_state(closeadj, 252); run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    base = run.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tiltrank_252d_slope_v127_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); tilt = sg.rolling(252, min_periods=126).mean()
    base = tilt.rolling(504, min_periods=126).rank(pct=True) - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tiltrank_252d_slope_v128_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); tilt = sg.rolling(252, min_periods=126).mean()
    base = tilt.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dominance_504d_slope_v129_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    bm = _f03_runlen(st > 0).rolling(504, min_periods=252).max(); bs = _f03_runlen(st < 0).rolling(504, min_periods=252).max()
    base = (bm - bs) / (bm + bs).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_dominance_504d_slope_v130_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    bm = _f03_runlen(st > 0).rolling(504, min_periods=252).max(); bs = _f03_runlen(st < 0).rolling(504, min_periods=252).max()
    base = (bm - bs) / (bm + bs).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tailasym_252d_slope_v131_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff(); thr = r.rolling(252, min_periods=126).std()
    bu = (r > 2.0 * thr).astype(float).rolling(252, min_periods=126).sum(); bd = (r < -2.0 * thr).astype(float).rolling(252, min_periods=126).sum()
    base = (bu - bd) / (bu + bd).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_tailasym_252d_slope_v132_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff(); thr = r.rolling(252, min_periods=126).std()
    bu = (r > 2.0 * thr).astype(float).rolling(252, min_periods=126).sum(); bd = (r < -2.0 * thr).astype(float).rolling(252, min_periods=126).sum()
    base = (bu - bd) / (bu + bd).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_moveasym_252d_slope_v133_signal(closeadj):
    mret = np.log(closeadj.replace(0, np.nan)).diff(21)
    ue = (mret >= 0.05).astype(float).rolling(252, min_periods=126).sum(); de = (mret <= -0.05).astype(float).rolling(252, min_periods=126).sum()
    base = (ue - de) / (ue + de).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_moveasym_252d_slope_v134_signal(closeadj):
    mret = np.log(closeadj.replace(0, np.nan)).diff(21)
    ue = (mret >= 0.05).astype(float).rolling(252, min_periods=126).sum(); de = (mret <= -0.05).astype(float).rolling(252, min_periods=126).sum()
    base = (ue - de) / (ue + de).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_neutralband_252d_slope_v135_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); sd = gap.rolling(252, min_periods=126).std()
    base = (gap.abs() < 0.5 * sd).astype(float).rolling(252, min_periods=126).mean()
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_neutralband_252d_slope_v136_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); sd = gap.rolling(252, min_periods=126).std()
    base = (gap.abs() < 0.5 * sd).astype(float).rolling(252, min_periods=126).mean()
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_turn_252d_slope_v137_signal(closeadj):
    st = _f03_regime_state(closeadj, 252).rolling(42, min_periods=21).mean()
    base = st - st.shift(42)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_turn_252d_slope_v138_signal(closeadj):
    st = _f03_regime_state(closeadj, 252).rolling(42, min_periods=21).mean()
    base = st - st.shift(42)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phaseproxy_252d_slope_v139_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); vel = gap - gap.shift(5)
    base = np.arctan2(vel, gap) / np.pi
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_phaseproxy_252d_slope_v140_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan)); gap = lp - lp.rolling(252, min_periods=126).mean(); vel = gap - gap.shift(5)
    base = np.arctan2(vel, gap) / np.pi
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_intradaybull_252d_slope_v141_signal(closeadj, high, low):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.5).astype(float).rolling(252, min_periods=126).mean() - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_intradaybull_252d_slope_v142_signal(closeadj, high, low):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.5).astype(float).rolling(252, min_periods=126).mean() - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_intraconfirm_252d_slope_v143_signal(closeadj, high, low):
    st = _f03_regime_state(closeadj, 252); pos = (closeadj - low) / (high - low).replace(0, np.nan); isign = np.sign(pos - 0.5)
    agree = (np.sign(st) == isign).astype(float).where(st.notna(), other=np.nan)
    base = agree.rolling(63, min_periods=21).mean() - 0.5
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_intraconfirm_252d_slope_v144_signal(closeadj, high, low):
    st = _f03_regime_state(closeadj, 252); pos = (closeadj - low) / (high - low).replace(0, np.nan); isign = np.sign(pos - 0.5)
    agree = (np.sign(st) == isign).astype(float).where(st.notna(), other=np.nan)
    base = agree.rolling(63, min_periods=21).mean() - 0.5
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_rangeasym_252d_slope_v145_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan); st = _f03_regime_state(closeadj, 252)
    br = rng.where(st > 0).rolling(252, min_periods=63).mean(); ur = rng.where(st < 0).rolling(252, min_periods=63).mean()
    base = (ur - br) / (ur + br).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_rangeasym_252d_slope_v146_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan); st = _f03_regime_state(closeadj, 252)
    br = rng.where(st > 0).rolling(252, min_periods=63).mean(); ur = rng.where(st < 0).rolling(252, min_periods=63).mean()
    base = (ur - br) / (ur + br).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_gapbreakasym_252d_slope_v147_signal(closeadj, high, low):
    ub = (closeadj > high.shift(1)).astype(float).rolling(252, min_periods=126).sum(); db = (closeadj < low.shift(1)).astype(float).rolling(252, min_periods=126).sum()
    base = (ub - db) / (ub + db).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_gapbreakasym_252d_slope_v148_signal(closeadj, high, low):
    ub = (closeadj > high.shift(1)).astype(float).rolling(252, min_periods=126).sum(); db = (closeadj < low.shift(1)).astype(float).rolling(252, min_periods=126).sum()
    base = (ub - db) / (ub + db).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_rangecouple_252d_slope_v149_signal(closeadj, high, low):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); rng = ((high - low) / closeadj.replace(0, np.nan)).shift(-1)
    ms = sg.rolling(252, min_periods=126).mean(); mr = rng.rolling(252, min_periods=126).mean()
    cov = (sg * rng).rolling(252, min_periods=126).mean() - ms * mr
    base = cov / (sg.rolling(252, min_periods=126).std() * rng.rolling(252, min_periods=126).std()).replace(0, np.nan)
    d = base - base.shift(21)
    return d.replace([np.inf, -np.inf], np.nan)

def f03cp_f03_cycle_phase_regime_rangecouple_252d_slope_v150_signal(closeadj, high, low):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff()); rng = ((high - low) / closeadj.replace(0, np.nan)).shift(-1)
    ms = sg.rolling(252, min_periods=126).mean(); mr = rng.rolling(252, min_periods=126).mean()
    cov = (sg * rng).rolling(252, min_periods=126).mean() - ms * mr
    base = cov / (sg.rolling(252, min_periods=126).std() * rng.rolling(252, min_periods=126).std()).replace(0, np.nan)
    base = base.ewm(span=63, min_periods=31).mean()
    d = base - base.shift(84)
    return d.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f03cp_f03_cycle_phase_regime_statesm_252d_slope_v001_signal,
    f03cp_f03_cycle_phase_regime_statesm_252d_slope_v002_signal,
    f03cp_f03_cycle_phase_regime_statesm504_504d_slope_v003_signal,
    f03cp_f03_cycle_phase_regime_statesm504_504d_slope_v004_signal,
    f03cp_f03_cycle_phase_regime_agree_252d_slope_v005_signal,
    f03cp_f03_cycle_phase_regime_agree_252d_slope_v006_signal,
    f03cp_f03_cycle_phase_regime_dualtrend_252d_slope_v007_signal,
    f03cp_f03_cycle_phase_regime_dualtrend_252d_slope_v008_signal,
    f03cp_f03_cycle_phase_regime_boomfrac_252d_slope_v009_signal,
    f03cp_f03_cycle_phase_regime_boomfrac_252d_slope_v010_signal,
    f03cp_f03_cycle_phase_regime_boomfrac126_252d_slope_v011_signal,
    f03cp_f03_cycle_phase_regime_boomfrac126_252d_slope_v012_signal,
    f03cp_f03_cycle_phase_regime_boomrun_252d_slope_v013_signal,
    f03cp_f03_cycle_phase_regime_boomrun_252d_slope_v014_signal,
    f03cp_f03_cycle_phase_regime_extremephase_504d_slope_v015_signal,
    f03cp_f03_cycle_phase_regime_extremephase_504d_slope_v016_signal,
    f03cp_f03_cycle_phase_regime_flipint_252d_slope_v017_signal,
    f03cp_f03_cycle_phase_regime_flipint_252d_slope_v018_signal,
    f03cp_f03_cycle_phase_regime_flipint126_252d_slope_v019_signal,
    f03cp_f03_cycle_phase_regime_flipint126_252d_slope_v020_signal,
    f03cp_f03_cycle_phase_regime_entropy_252d_slope_v021_signal,
    f03cp_f03_cycle_phase_regime_entropy_252d_slope_v022_signal,
    f03cp_f03_cycle_phase_regime_updnasym63_63d_slope_v023_signal,
    f03cp_f03_cycle_phase_regime_updnasym63_63d_slope_v024_signal,
    f03cp_f03_cycle_phase_regime_updnasym252_252d_slope_v025_signal,
    f03cp_f03_cycle_phase_regime_updnasym252_252d_slope_v026_signal,
    f03cp_f03_cycle_phase_regime_runmaturity_252d_slope_v027_signal,
    f03cp_f03_cycle_phase_regime_runmaturity_252d_slope_v028_signal,
    f03cp_f03_cycle_phase_regime_conviction_252d_slope_v029_signal,
    f03cp_f03_cycle_phase_regime_conviction_252d_slope_v030_signal,
    f03cp_f03_cycle_phase_regime_clockdiverge_252d_slope_v031_signal,
    f03cp_f03_cycle_phase_regime_clockdiverge_252d_slope_v032_signal,
    f03cp_f03_cycle_phase_regime_clockconflict_252d_slope_v033_signal,
    f03cp_f03_cycle_phase_regime_clockconflict_252d_slope_v034_signal,
    f03cp_f03_cycle_phase_regime_dirpurity63_63d_slope_v035_signal,
    f03cp_f03_cycle_phase_regime_dirpurity63_63d_slope_v036_signal,
    f03cp_f03_cycle_phase_regime_dirpurity252_252d_slope_v037_signal,
    f03cp_f03_cycle_phase_regime_dirpurity252_252d_slope_v038_signal,
    f03cp_f03_cycle_phase_regime_massasym252_252d_slope_v039_signal,
    f03cp_f03_cycle_phase_regime_massasym252_252d_slope_v040_signal,
    f03cp_f03_cycle_phase_regime_massasym63_63d_slope_v041_signal,
    f03cp_f03_cycle_phase_regime_massasym63_63d_slope_v042_signal,
    f03cp_f03_cycle_phase_regime_retskew252_252d_slope_v043_signal,
    f03cp_f03_cycle_phase_regime_retskew252_252d_slope_v044_signal,
    f03cp_f03_cycle_phase_regime_volasym_252d_slope_v045_signal,
    f03cp_f03_cycle_phase_regime_volasym_252d_slope_v046_signal,
    f03cp_f03_cycle_phase_regime_efficiency_252d_slope_v047_signal,
    f03cp_f03_cycle_phase_regime_efficiency_252d_slope_v048_signal,
    f03cp_f03_cycle_phase_regime_roughness63_63d_slope_v049_signal,
    f03cp_f03_cycle_phase_regime_roughness63_63d_slope_v050_signal,
    f03cp_f03_cycle_phase_regime_signtiltspr_252d_slope_v051_signal,
    f03cp_f03_cycle_phase_regime_signtiltspr_252d_slope_v052_signal,
    f03cp_f03_cycle_phase_regime_stateprod_252d_slope_v053_signal,
    f03cp_f03_cycle_phase_regime_stateprod_252d_slope_v054_signal,
    f03cp_f03_cycle_phase_regime_clocklag_252d_slope_v055_signal,
    f03cp_f03_cycle_phase_regime_clocklag_252d_slope_v056_signal,
    f03cp_f03_cycle_phase_regime_medrun_252d_slope_v057_signal,
    f03cp_f03_cycle_phase_regime_medrun_252d_slope_v058_signal,
    f03cp_f03_cycle_phase_regime_fullnet_252d_slope_v059_signal,
    f03cp_f03_cycle_phase_regime_fullnet_252d_slope_v060_signal,
    f03cp_f03_cycle_phase_regime_signautocorr63_63d_slope_v061_signal,
    f03cp_f03_cycle_phase_regime_signautocorr63_63d_slope_v062_signal,
    f03cp_f03_cycle_phase_regime_mombreadth_252d_slope_v063_signal,
    f03cp_f03_cycle_phase_regime_mombreadth_252d_slope_v064_signal,
    f03cp_f03_cycle_phase_regime_momdisagree_252d_slope_v065_signal,
    f03cp_f03_cycle_phase_regime_momdisagree_252d_slope_v066_signal,
    f03cp_f03_cycle_phase_regime_trendagree252_252d_slope_v067_signal,
    f03cp_f03_cycle_phase_regime_trendagree252_252d_slope_v068_signal,
    f03cp_f03_cycle_phase_regime_chop63_63d_slope_v069_signal,
    f03cp_f03_cycle_phase_regime_chop63_63d_slope_v070_signal,
    f03cp_f03_cycle_phase_regime_signema_21d_slope_v071_signal,
    f03cp_f03_cycle_phase_regime_signema_21d_slope_v072_signal,
    f03cp_f03_cycle_phase_regime_signemadisp_126d_slope_v073_signal,
    f03cp_f03_cycle_phase_regime_signemadisp_126d_slope_v074_signal,
    f03cp_f03_cycle_phase_regime_phasepower_252d_slope_v075_signal,
    f03cp_f03_cycle_phase_regime_phasepower_252d_slope_v076_signal,
    f03cp_f03_cycle_phase_regime_flipburst_252d_slope_v077_signal,
    f03cp_f03_cycle_phase_regime_flipburst_252d_slope_v078_signal,
    f03cp_f03_cycle_phase_regime_boomfracslope_252d_slope_v079_signal,
    f03cp_f03_cycle_phase_regime_boomfracslope_252d_slope_v080_signal,
    f03cp_f03_cycle_phase_regime_phasematurity_252d_slope_v081_signal,
    f03cp_f03_cycle_phase_regime_phasematurity_252d_slope_v082_signal,
    f03cp_f03_cycle_phase_regime_doubleabove_252d_slope_v083_signal,
    f03cp_f03_cycle_phase_regime_doubleabove_252d_slope_v084_signal,
    f03cp_f03_cycle_phase_regime_conflictdwell_252d_slope_v085_signal,
    f03cp_f03_cycle_phase_regime_conflictdwell_252d_slope_v086_signal,
    f03cp_f03_cycle_phase_regime_runskew_252d_slope_v087_signal,
    f03cp_f03_cycle_phase_regime_runskew_252d_slope_v088_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym504_504d_slope_v089_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym504_504d_slope_v090_signal,
    f03cp_f03_cycle_phase_regime_legasym252_252d_slope_v091_signal,
    f03cp_f03_cycle_phase_regime_legasym252_252d_slope_v092_signal,
    f03cp_f03_cycle_phase_regime_semivarasym_504d_slope_v093_signal,
    f03cp_f03_cycle_phase_regime_semivarasym_504d_slope_v094_signal,
    f03cp_f03_cycle_phase_regime_fastmoveasym_63d_slope_v095_signal,
    f03cp_f03_cycle_phase_regime_fastmoveasym_63d_slope_v096_signal,
    f03cp_f03_cycle_phase_regime_monthasym_504d_slope_v097_signal,
    f03cp_f03_cycle_phase_regime_monthasym_504d_slope_v098_signal,
    f03cp_f03_cycle_phase_regime_retzerocross63_63d_slope_v099_signal,
    f03cp_f03_cycle_phase_regime_retzerocross63_63d_slope_v100_signal,
    f03cp_f03_cycle_phase_regime_zerocrossac_252d_slope_v101_signal,
    f03cp_f03_cycle_phase_regime_zerocrossac_252d_slope_v102_signal,
    f03cp_f03_cycle_phase_regime_streakthrust_63d_slope_v103_signal,
    f03cp_f03_cycle_phase_regime_streakthrust_63d_slope_v104_signal,
    f03cp_f03_cycle_phase_regime_uprunpersist_252d_slope_v105_signal,
    f03cp_f03_cycle_phase_regime_uprunpersist_252d_slope_v106_signal,
    f03cp_f03_cycle_phase_regime_maxrunasym_252d_slope_v107_signal,
    f03cp_f03_cycle_phase_regime_maxrunasym_252d_slope_v108_signal,
    f03cp_f03_cycle_phase_regime_runcountasym_252d_slope_v109_signal,
    f03cp_f03_cycle_phase_regime_runcountasym_252d_slope_v110_signal,
    f03cp_f03_cycle_phase_regime_sinceboom_252d_slope_v111_signal,
    f03cp_f03_cycle_phase_regime_sinceboom_252d_slope_v112_signal,
    f03cp_f03_cycle_phase_regime_tiltmom_252d_slope_v113_signal,
    f03cp_f03_cycle_phase_regime_tiltmom_252d_slope_v114_signal,
    f03cp_f03_cycle_phase_regime_nettilt1260_1260d_slope_v115_signal,
    f03cp_f03_cycle_phase_regime_nettilt1260_1260d_slope_v116_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym1260_1260d_slope_v117_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym1260_1260d_slope_v118_signal,
    f03cp_f03_cycle_phase_regime_boomshare1260_1260d_slope_v119_signal,
    f03cp_f03_cycle_phase_regime_boomshare1260_1260d_slope_v120_signal,
    f03cp_f03_cycle_phase_regime_whipsaw_252d_slope_v121_signal,
    f03cp_f03_cycle_phase_regime_whipsaw_252d_slope_v122_signal,
    f03cp_f03_cycle_phase_regime_persistprob_252d_slope_v123_signal,
    f03cp_f03_cycle_phase_regime_persistprob_252d_slope_v124_signal,
    f03cp_f03_cycle_phase_regime_runextrank_252d_slope_v125_signal,
    f03cp_f03_cycle_phase_regime_runextrank_252d_slope_v126_signal,
    f03cp_f03_cycle_phase_regime_tiltrank_252d_slope_v127_signal,
    f03cp_f03_cycle_phase_regime_tiltrank_252d_slope_v128_signal,
    f03cp_f03_cycle_phase_regime_dominance_504d_slope_v129_signal,
    f03cp_f03_cycle_phase_regime_dominance_504d_slope_v130_signal,
    f03cp_f03_cycle_phase_regime_tailasym_252d_slope_v131_signal,
    f03cp_f03_cycle_phase_regime_tailasym_252d_slope_v132_signal,
    f03cp_f03_cycle_phase_regime_moveasym_252d_slope_v133_signal,
    f03cp_f03_cycle_phase_regime_moveasym_252d_slope_v134_signal,
    f03cp_f03_cycle_phase_regime_neutralband_252d_slope_v135_signal,
    f03cp_f03_cycle_phase_regime_neutralband_252d_slope_v136_signal,
    f03cp_f03_cycle_phase_regime_turn_252d_slope_v137_signal,
    f03cp_f03_cycle_phase_regime_turn_252d_slope_v138_signal,
    f03cp_f03_cycle_phase_regime_phaseproxy_252d_slope_v139_signal,
    f03cp_f03_cycle_phase_regime_phaseproxy_252d_slope_v140_signal,
    f03cp_f03_cycle_phase_regime_intradaybull_252d_slope_v141_signal,
    f03cp_f03_cycle_phase_regime_intradaybull_252d_slope_v142_signal,
    f03cp_f03_cycle_phase_regime_intraconfirm_252d_slope_v143_signal,
    f03cp_f03_cycle_phase_regime_intraconfirm_252d_slope_v144_signal,
    f03cp_f03_cycle_phase_regime_rangeasym_252d_slope_v145_signal,
    f03cp_f03_cycle_phase_regime_rangeasym_252d_slope_v146_signal,
    f03cp_f03_cycle_phase_regime_gapbreakasym_252d_slope_v147_signal,
    f03cp_f03_cycle_phase_regime_gapbreakasym_252d_slope_v148_signal,
    f03cp_f03_cycle_phase_regime_rangecouple_252d_slope_v149_signal,
    f03cp_f03_cycle_phase_regime_rangecouple_252d_slope_v150_signal,
]


def _inputs_for(fn):
    return [p.name for p in inspect.signature(fn).parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CYCLE_PHASE_REGIME_REGISTRY_001_150 = REGISTRY


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
    cols = {"closeadj": closeadj, "close": close, "open": openp, "high": high, "low": low}
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
        if y1.iloc[504:].isna().mean() < 0.5:
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
    print("OK f03_cycle_phase_regime_2nd_derivatives_001_150_claude: " + str(n_features) + " features pass")
