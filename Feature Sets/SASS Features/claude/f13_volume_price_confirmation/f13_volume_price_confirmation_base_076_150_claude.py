import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (volume-price confirmation) =====
def _f13_obv(close, volume):
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f13_clv(close, high, low):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f13_ad_line(close, high, low, volume):
    mfv = _f13_clv(close, high, low) * volume
    return mfv.fillna(0.0).cumsum()


def _f13_cmf(close, high, low, volume, w):
    mfv = _f13_clv(close, high, low) * volume
    return _sum(mfv, w) / _sum(volume, w).replace(0, np.nan)


def _f13_typical(close, high, low):
    return (high + low + close) / 3.0


def _f13_mfi(close, high, low, volume, w):
    tp = _f13_typical(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pmf = _sum(up, w)
    nmf = _sum(dn, w)
    ratio = pmf / nmf.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + ratio))


def _f13_force(close, volume, w):
    raw = close.diff() * volume
    return raw.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f13_eom(high, low, volume, w):
    mid = (high + low) / 2.0
    dist = mid.diff()
    box = volume / (high - low).replace(0, np.nan)
    raw = dist / box.replace(0, np.nan)
    return _mean(raw, w)


def _f13_pvt(close, volume):
    return (close.pct_change() * volume).fillna(0.0).cumsum()


# ============================================================
# --- OBV variants (file 2) ---
# OBV vs price-level 63d rolling beta (volume confirmation strength of price trend)
def f13vc_f13_volume_price_confirmation_obvbeta_63d_base_v076_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    cov = obv.rolling(63, min_periods=21).cov(np.log(closeadj.replace(0, np.nan)))
    var = np.log(closeadj.replace(0, np.nan)).rolling(63, min_periods=21).var()
    b = cov / var.replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV efficiency: net OBV change vs gross volume traded over 63d (accumulation efficiency)
def f13vc_f13_volume_price_confirmation_obveff_63d_base_v077_signal(close, volume):
    obv = _f13_obv(close, volume)
    net = (obv - obv.shift(63)).abs()
    b = net / _sum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope minus price slope (volume-trend leading/lagging price-trend, 126d)
def f13vc_f13_volume_price_confirmation_obvlead_126d_base_v078_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    obvsl = _slope(obv, 126) / _mean(volume, 126).replace(0, np.nan)
    pxsl = _slope(np.log(closeadj.replace(0, np.nan)), 126) * 100.0
    b = obvsl - pxsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV 126d momentum risk-adjusted by OBV diff volatility
def f13vc_f13_volume_price_confirmation_obvmomra_126d_base_v079_signal(close, volume):
    obv = _f13_obv(close, volume)
    chg = obv - obv.shift(126)
    vol = _std(obv.diff(), 126) * np.sqrt(126.0)
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV new-high rate: fraction of last 63d OBV set a 126d high (accumulation breakouts)
def f13vc_f13_volume_price_confirmation_obvnewhi_63d_base_v080_signal(close, volume):
    obv = _f13_obv(close, volume)
    roll_hi = obv.rolling(126, min_periods=63).max()
    is_hi = (obv >= roll_hi - 1e-9).astype(float)
    freq = _mean(is_hi, 63)
    depth = (obv - obv.rolling(126, min_periods=63).min()) / _sum(volume, 126).replace(0, np.nan)
    b = freq + 0.1 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D line variants ---
# A/D slope risk-adjusted by A/D diff volatility (clean accumulation trend, 63d)
def f13vc_f13_volume_price_confirmation_adslopera_63d_base_v081_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    sl = _slope(ad, 63)
    vol = _std(ad.diff(), 63) * np.sqrt(63.0)
    b = sl * 63.0 / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line vs price log-level beta over 126d (long accumulation confirmation)
def f13vc_f13_volume_price_confirmation_adbeta_126d_base_v082_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    cov = ad.rolling(126, min_periods=63).cov(np.log(closeadj.replace(0, np.nan)))
    var = np.log(closeadj.replace(0, np.nan)).rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan) / _mean(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator momentum: oscillator change over 21d
def f13vc_f13_volume_price_confirmation_chaikmom_21d_base_v083_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    b = oscn - oscn.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator sign-persistence (fraction positive over 63d)
def f13vc_f13_volume_price_confirmation_chaikpersist_63d_base_v084_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    b = np.sign(osc).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D efficiency: net A/D travel vs total absolute daily MFV over 63d
def f13vc_f13_volume_price_confirmation_adeff_63d_base_v085_signal(close, high, low, volume):
    mfv = _f13_clv(close, high, low) * volume
    net = _sum(mfv, 63).abs()
    gross = _sum(mfv.abs(), 63)
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF variants ---
# CMF over 126d (long money-flow pressure)
def f13vc_f13_volume_price_confirmation_cmf_126d_base_v086_signal(close, high, low, volume):
    b = _f13_cmf(close, high, low, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration: 21d-CMF momentum minus 63d-CMF momentum
def f13vc_f13_volume_price_confirmation_cmfaccel_base_v087_signal(close, high, low, volume):
    c21 = _f13_cmf(close, high, low, volume, 21)
    c63 = _f13_cmf(close, high, low, volume, 63)
    b = (c21 - c21.shift(21)) - (c63 - c63.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF interacted with price momentum sign (money-flow confirms price, 63d)
def f13vc_f13_volume_price_confirmation_cmfpxconf_63d_base_v088_signal(closeadj, close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    b = c * pxm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF crossing rate: flip frequency blended with mean |CMF| magnitude (indecision)
def f13vc_f13_volume_price_confirmation_cmfcross_63d_base_v089_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    flip = (np.sign(c) != np.sign(c.shift(1))).astype(float)
    b = _mean(flip, 63) - _mean(c.abs(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF amplitude: rolling max-minus-min of CMF21 over 63d (pressure swing range)
def f13vc_f13_volume_price_confirmation_cmfamp_63d_base_v090_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    hi = c.rolling(63, min_periods=21).max()
    lo = c.rolling(63, min_periods=21).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MFI variants ---
# MFI over 63d, centered
def f13vc_f13_volume_price_confirmation_mfi_63d_base_v091_signal(close, high, low, volume):
    b = _f13_mfi(close, high, low, volume, 63) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI vs price RSI-direction divergence over 21d (money-flow not confirming)
def f13vc_f13_volume_price_confirmation_mfidiv_21d_base_v092_signal(closeadj, close, high, low, volume):
    mfi = _f13_mfi(close, high, low, volume, 21) - 50.0
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    b = mfi - pxm * mfi.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI slope over 63d (money-flow-index trend)
def f13vc_f13_volume_price_confirmation_mfislope_63d_base_v093_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    b = _slope(m, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI rank vs 252d history
def f13vc_f13_volume_price_confirmation_mfirank_252d_base_v094_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 21)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI dispersion: std of MFI(14) over 63d (money-flow volatility)
def f13vc_f13_volume_price_confirmation_mfidisp_63d_base_v095_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    b = _std(m, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force / EOM variants ---
# Force index 21d normalized, z vs 126d (impulse regime)
def f13vc_f13_volume_price_confirmation_forcez21_126d_base_v096_signal(close, volume):
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    f = _f13_force(close, volume, 21) / nrm
    b = _z(f, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Raw (unsmoothed) force index rank vs 252d (single-bar conviction)
def f13vc_f13_volume_price_confirmation_forceraw_252d_base_v097_signal(close, volume):
    raw = close.diff() * volume
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    b = _rank(raw / nrm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force-index up/down asymmetry: mean positive force vs mean negative force (63d)
def f13vc_f13_volume_price_confirmation_forceasym_63d_base_v098_signal(close, volume):
    raw = close.diff() * volume
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    rn = raw / nrm
    pos = _mean(rn.clip(lower=0), 63)
    neg = _mean((-rn).clip(lower=0), 63)
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM slope over 63d (ease-of-movement trend)
def f13vc_f13_volume_price_confirmation_eomslope_63d_base_v099_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    b = _slope(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM rank vs 252d history
def f13vc_f13_volume_price_confirmation_eomrank_252d_base_v100_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    b = _rank(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM momentum: 21d-EOM change over a month
def f13vc_f13_volume_price_confirmation_eommom_21d_base_v101_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 21) * 1e6
    b = e - e.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM dispersion over 63d (volatility of ease-of-movement)
def f13vc_f13_volume_price_confirmation_eomdisp_63d_base_v102_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    b = _std(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Divergence / confirmation variants ---
# Price-volume rank correlation over 63d (Spearman-ish via ranked series)
def f13vc_f13_volume_price_confirmation_pvrankcorr_63d_base_v103_signal(closeadj, volume):
    pr = closeadj.pct_change().rolling(63, min_periods=21).rank(pct=True)
    vr = volume.rolling(63, min_periods=21).rank(pct=True)
    b = pr.rolling(63, min_periods=21).corr(vr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed trend: sign(price 63d ret) times relative-volume trend
def f13vc_f13_volume_price_confirmation_voltrendconf_63d_base_v104_signal(closeadj, volume):
    pxdir = np.sign(closeadj / closeadj.shift(63) - 1.0)
    voltrend = _slope(np.log(volume.replace(0, np.nan)), 63)
    b = pxdir * voltrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rising-price-falling-volume warning over 21d (weak rally), depth-weighted
def f13vc_f13_volume_price_confirmation_weakrally_21d_base_v105_signal(closeadj, volume):
    px_up = (closeadj.diff() > 0).astype(float)
    vol_dn = (volume.diff() < 0).astype(float)
    weak = px_up * vol_dn * closeadj.pct_change().abs()
    b = _mean(weak, 21) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Falling-price-rising-volume capitulation over 21d (heavy selling)
def f13vc_f13_volume_price_confirmation_capit_21d_base_v106_signal(closeadj, volume):
    px_dn = (closeadj.diff() < 0).astype(float)
    vol_up = (volume.diff() > 0).astype(float)
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    cap = px_dn * vol_up * relv
    b = _mean(cap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Effort efficiency: 21d abs return per unit relative volume (price elasticity)
def f13vc_f13_volume_price_confirmation_priceelast_21d_base_v107_signal(closeadj, volume):
    move = (closeadj / closeadj.shift(21) - 1.0).abs()
    relv = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    b = move / relv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Up/down volume & PVI/NVI variants ---
# Up-volume share over 63d (buying breadth)
def f13vc_f13_volume_price_confirmation_upvolshare_63d_base_v108_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    b = _sum(up, 63) / _sum(volume, 63).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up vs down volume momentum: 21d balance change over a month
def f13vc_f13_volume_price_confirmation_updnmom_21d_base_v109_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    bal = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    b = bal - bal.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume concentration: share of 63d volume occurring on the 5 largest-move days
def f13vc_f13_volume_price_confirmation_volretasym_63d_base_v110_signal(closeadj, volume):
    absret = closeadj.pct_change().abs()
    rank = absret.rolling(63, min_periods=21).rank(pct=True)
    big = (rank > 0.92).astype(float)
    b = _sum(big * volume, 63) / _sum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NVI proxy over 63d (smart-money on quiet days)
def f13vc_f13_volume_price_confirmation_nvi_63d_base_v111_signal(closeadj, volume):
    quiet = (volume < volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * quiet
    b = _sum(contrib, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVI proxy over 63d (crowd on loud days)
def f13vc_f13_volume_price_confirmation_pvi_63d_base_v112_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * loud
    b = _sum(contrib, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Dollar-volume confirmation variants (>21d use closeadj) ---
# Dollar-OBV slope over 63d (value-weighted accumulation)
def f13vc_f13_volume_price_confirmation_dvobvslope_63d_base_v113_signal(closeadj, volume):
    direction = np.sign(closeadj.diff())
    dvobv = (direction * closeadj * volume).fillna(0.0).cumsum()
    b = _slope(dvobv, 63) / _mean(closeadj * volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI smoothing displacement: MFI(14) minus its own 21d EMA (overbought impulse)
def f13vc_f13_volume_price_confirmation_dvmfi_21d_base_v114_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    b = m - m.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar-force index drawdown: distance below its 126d peak (impulse give-back)
def f13vc_f13_volume_price_confirmation_dvforcez_126d_base_v115_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    f = raw.ewm(span=21, min_periods=10).mean()
    fn = f / _mean(closeadj * volume, 126).replace(0, np.nan)
    peak = fn.rolling(126, min_periods=63).max()
    b = fn - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Accumulation regime / streak variants ---
# Money-flow trend strength: |CMF63 slope| over 126d (developing pressure)
def f13vc_f13_volume_price_confirmation_cmftrend_126d_base_v116_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line drawdown: distance of A/D from its trailing 126d peak (distribution stress)
def f13vc_f13_volume_price_confirmation_addrawdown_126d_base_v117_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    peak = ad.rolling(126, min_periods=63).max()
    b = (ad - peak) / _sum(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV drawdown: OBV distance below its 126d peak normalized (accumulation give-back)
def f13vc_f13_volume_price_confirmation_obvdrawdown_126d_base_v118_signal(close, volume):
    obv = _f13_obv(close, volume)
    peak = obv.rolling(126, min_periods=63).max()
    b = (obv - peak) / _sum(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow breadth asymmetry: magnitude-weighted positive vs negative CLV share (63d)
def f13vc_f13_volume_price_confirmation_mfvbreadth_63d_base_v119_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    pos = _sum(clv.clip(lower=0), 63)
    neg = _sum((-clv).clip(lower=0), 63)
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume thrust on up days over 63d (relative-volume premium on advances)
def f13vc_f13_volume_price_confirmation_volthrust_63d_base_v120_signal(closeadj, volume):
    relv = volume / _mean(volume, 126).replace(0, np.nan)
    up = relv.where(closeadj.diff() > 0)
    dn = relv.where(closeadj.diff() < 0)
    b = _mean(up, 63) - _mean(dn, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV-weighted return: intrabar-strength-weighted forward effort over 21d
def f13vc_f13_volume_price_confirmation_clvret_21d_base_v121_signal(closeadj, close, high, low):
    clv = _f13_clv(close, high, low)
    b = _mean(clv * closeadj.pct_change(), 21) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Typical-price money-flow ratio over 21d (raw positive/negative money-flow tilt)
def f13vc_f13_volume_price_confirmation_mfratio_21d_base_v122_signal(close, high, low, volume):
    tp = _f13_typical(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    b = (_sum(up, 21) - _sum(dn, 21)) / (_sum(up, 21) + _sum(dn, 21)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Decisive-close intensity: mean |CLV| over 63d (how often closes hug bar extremes)
def f13vc_f13_volume_price_confirmation_clvabove_63d_base_v123_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    b = _mean(clv.abs(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted CLV trend: slope of CMF21 normalized (developing accumulation, 63d)
def f13vc_f13_volume_price_confirmation_cmf21slope_63d_base_v124_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = _slope(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Effort-result divergence: 63d up/down vol balance minus price 63d return sign
def f13vc_f13_volume_price_confirmation_effdiv_63d_base_v125_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    bal = (_sum(up, 63) - _sum(dn, 63)) / _sum(volume, 63).replace(0, np.nan)
    pxret = np.tanh((closeadj / closeadj.shift(63) - 1.0) * 5.0)
    b = bal - pxret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow stability: 1 minus normalized swing range over 126d
def f13vc_f13_volume_price_confirmation_cmfstab_126d_base_v126_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    sw = c.rolling(126, min_periods=63).max() - c.rolling(126, min_periods=63).min()
    lvl = _mean(c, 126).abs()
    b = lvl / sw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-to-PVT divergence: normalized OBV trend minus normalized PVT trend (63d)
def f13vc_f13_volume_price_confirmation_obvpvtdiv_63d_base_v127_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    pvt = _f13_pvt(closeadj, volume)
    obvn = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    pvtn = (pvt - pvt.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    b = obvn - pvtn * 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow momentum confirmation: CMF21 momentum times price 21d momentum sign
def f13vc_f13_volume_price_confirmation_cmfmompx_21d_base_v128_signal(closeadj, close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    cmom = c - c.shift(21)
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    b = cmom * pxm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Distribution days count: heavy-volume down closes in lower-half-of-range (21d)
def f13vc_f13_volume_price_confirmation_distdays_21d_base_v129_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    dist = ((closeadj.diff() < 0) & (relv > 1.2) & (clv < 0)).astype(float) * relv
    b = _sum(dist, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Accumulation days count: heavy-volume up closes in upper-half-of-range (21d)
def f13vc_f13_volume_price_confirmation_accdays_21d_base_v130_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    acc = ((closeadj.diff() > 0) & (relv > 1.2) & (clv > 0)).astype(float) * relv
    b = _sum(acc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Net accumulation-minus-distribution day pressure over 63d
def f13vc_f13_volume_price_confirmation_netaccdist_63d_base_v131_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    acc = ((closeadj.diff() > 0) & (relv > 1.0) & (clv > 0)).astype(float) * relv
    dist = ((closeadj.diff() < 0) & (relv > 1.0) & (clv < 0)).astype(float) * relv
    b = (_sum(acc, 63) - _sum(dist, 63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI-OBV agreement: MFI magnitude weighted by sign-agreement with OBV momentum (63d)
def f13vc_f13_volume_price_confirmation_mfiobvagree_63d_base_v132_signal(close, high, low, volume):
    mfi = _f13_mfi(close, high, low, volume, 21) - 50.0
    obv = _f13_obv(close, volume)
    obvm = (obv - obv.shift(63))
    agree = np.sign(mfi) * np.sign(obvm) * mfi.abs()
    b = _mean(agree, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted price-acceleration confirmation (force-of-acceleration, 21d)
def f13vc_f13_volume_price_confirmation_volaccel_21d_base_v133_signal(close, volume):
    accel = close.diff().diff()
    raw = accel * volume
    f = raw.ewm(span=21, min_periods=10).mean()
    b = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow trend confirmation: net signed daily CMF63 change over 126d (drift)
def f13vc_f13_volume_price_confirmation_cmfrising_126d_base_v134_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    up = _sum(c.diff().clip(lower=0), 126)
    dn = _sum((-c.diff()).clip(lower=0), 126)
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D oscillator vs price-momentum divergence: chaikin osc minus price ROC sign (63d)
def f13vc_f13_volume_price_confirmation_adoscdiv_63d_base_v135_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    b = oscn - pxm * oscn.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed momentum quality: 63d return scaled by volume-trend agreement
def f13vc_f13_volume_price_confirmation_momquality_63d_base_v136_signal(closeadj, volume):
    ret = np.tanh((closeadj / closeadj.shift(63) - 1.0) * 3.0)
    voltrend = _slope(np.log(volume.replace(0, np.nan)), 63)
    voltrend_n = np.tanh(voltrend * 200.0)
    b = ret * (1.0 + voltrend_n) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM-force composite: ease times force-direction agreement (21d)
def f13vc_f13_volume_price_confirmation_eomforce_21d_base_v137_signal(close, high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    f = _f13_force(close, volume, 13)
    fn = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    b = np.sign(e) * np.sign(fn) * (e.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price-impact (Amihud-style but confirmation): signed return per dollar-vol over 21d
def f13vc_f13_volume_price_confirmation_signedimpact_21d_base_v138_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = closeadj * volume
    impact = ret / dv.replace(0, np.nan)
    b = _mean(impact, 21) * 1e12
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV oscillator: OBV minus its 21d mean, normalized (short accumulation impulse)
def f13vc_f13_volume_price_confirmation_obvosc_21d_base_v139_signal(close, volume):
    obv = _f13_obv(close, volume)
    osc = obv - _mean(obv, 21)
    b = osc / _sum(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF-vol interaction: CMF21 times relative-volume level (pressure x participation)
def f13vc_f13_volume_price_confirmation_cmfvolint_21d_base_v140_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    relv = _mean(volume, 21) / _mean(volume, 126).replace(0, np.nan)
    b = c * relv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow reversal: CMF21 now vs CMF21 a quarter ago (regime turn)
def f13vc_f13_volume_price_confirmation_cmfreversal_63d_base_v141_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index efficiency: net force vs gross |force| over 63d (directional purity)
def f13vc_f13_volume_price_confirmation_forcecum_63d_base_v142_signal(close, volume):
    raw = close.diff() * volume
    net = _sum(raw, 63).abs()
    gross = _sum(raw.abs(), 63)
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price elasticity trend: slope of |ret|/relvol over 63d (impact regime shift)
def f13vc_f13_volume_price_confirmation_elasttrend_63d_base_v143_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    impact = closeadj.pct_change().abs() / relv.replace(0, np.nan)
    b = _slope(impact.rolling(5, min_periods=3).mean(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Typical-price OBV (uses HLC) slope over 63d
def f13vc_f13_volume_price_confirmation_tpobvslope_63d_base_v144_signal(close, high, low, volume):
    tp = _f13_typical(close, high, low)
    direction = np.sign(tp.diff())
    tpobv = (direction * volume).fillna(0.0).cumsum()
    b = _slope(tpobv, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Accumulation acceleration: A/D 2nd-difference flow over 21d windows
def f13vc_f13_volume_price_confirmation_adaccel_base_v145_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    flow = (ad - ad.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    b = flow - 2.0 * flow.shift(21) + flow.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed breakout strength: 21d high-break times relative volume
def f13vc_f13_volume_price_confirmation_breakvol_21d_base_v146_signal(closeadj, volume):
    hi = closeadj.shift(1).rolling(21, min_periods=10).max()
    brk = (closeadj / hi.replace(0, np.nan) - 1.0).clip(lower=0)
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    b = _mean(brk * relv, 21) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow vs OBV scale spread (two accumulation gauges disagreement, 63d)
def f13vc_f13_volume_price_confirmation_mfobvspr_63d_base_v147_signal(close, high, low, volume):
    cmf = _f13_cmf(close, high, low, volume, 63)
    obv = _f13_obv(close, volume)
    obvn = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    b = cmf - obvn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Quiet-accumulation: CLV strength on below-average-volume days (stealth buying, 63d)
def f13vc_f13_volume_price_confirmation_stealth_63d_base_v148_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    quiet = (volume < _mean(volume, 63)).astype(float)
    b = _sum(clv * quiet, 63) / _sum(quiet, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Loud-distribution: CLV weakness on above-average-volume days (heavy selling, 63d)
def f13vc_f13_volume_price_confirmation_loud_63d_base_v149_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    loud = (volume > _mean(volume, 63)).astype(float)
    b = -_sum(clv * loud, 63) / _sum(loud, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Stealth-vs-loud spread: quiet-accumulation minus loud-day strength (smart-money tilt)
def f13vc_f13_volume_price_confirmation_stealthspr_63d_base_v150_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    quiet = (volume < _mean(volume, 63)).astype(float)
    loud = (volume >= _mean(volume, 63)).astype(float)
    qa = _sum(clv * quiet, 63) / _sum(quiet, 63).replace(0, np.nan)
    la = _sum(clv * loud, 63) / _sum(loud, 63).replace(0, np.nan)
    b = qa - la
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13vc_f13_volume_price_confirmation_obvbeta_63d_base_v076_signal,
    f13vc_f13_volume_price_confirmation_obveff_63d_base_v077_signal,
    f13vc_f13_volume_price_confirmation_obvlead_126d_base_v078_signal,
    f13vc_f13_volume_price_confirmation_obvmomra_126d_base_v079_signal,
    f13vc_f13_volume_price_confirmation_obvnewhi_63d_base_v080_signal,
    f13vc_f13_volume_price_confirmation_adslopera_63d_base_v081_signal,
    f13vc_f13_volume_price_confirmation_adbeta_126d_base_v082_signal,
    f13vc_f13_volume_price_confirmation_chaikmom_21d_base_v083_signal,
    f13vc_f13_volume_price_confirmation_chaikpersist_63d_base_v084_signal,
    f13vc_f13_volume_price_confirmation_adeff_63d_base_v085_signal,
    f13vc_f13_volume_price_confirmation_cmf_126d_base_v086_signal,
    f13vc_f13_volume_price_confirmation_cmfaccel_base_v087_signal,
    f13vc_f13_volume_price_confirmation_cmfpxconf_63d_base_v088_signal,
    f13vc_f13_volume_price_confirmation_cmfcross_63d_base_v089_signal,
    f13vc_f13_volume_price_confirmation_cmfamp_63d_base_v090_signal,
    f13vc_f13_volume_price_confirmation_mfi_63d_base_v091_signal,
    f13vc_f13_volume_price_confirmation_mfidiv_21d_base_v092_signal,
    f13vc_f13_volume_price_confirmation_mfislope_63d_base_v093_signal,
    f13vc_f13_volume_price_confirmation_mfirank_252d_base_v094_signal,
    f13vc_f13_volume_price_confirmation_mfidisp_63d_base_v095_signal,
    f13vc_f13_volume_price_confirmation_forcez21_126d_base_v096_signal,
    f13vc_f13_volume_price_confirmation_forceraw_252d_base_v097_signal,
    f13vc_f13_volume_price_confirmation_forceasym_63d_base_v098_signal,
    f13vc_f13_volume_price_confirmation_eomslope_63d_base_v099_signal,
    f13vc_f13_volume_price_confirmation_eomrank_252d_base_v100_signal,
    f13vc_f13_volume_price_confirmation_eommom_21d_base_v101_signal,
    f13vc_f13_volume_price_confirmation_eomdisp_63d_base_v102_signal,
    f13vc_f13_volume_price_confirmation_pvrankcorr_63d_base_v103_signal,
    f13vc_f13_volume_price_confirmation_voltrendconf_63d_base_v104_signal,
    f13vc_f13_volume_price_confirmation_weakrally_21d_base_v105_signal,
    f13vc_f13_volume_price_confirmation_capit_21d_base_v106_signal,
    f13vc_f13_volume_price_confirmation_priceelast_21d_base_v107_signal,
    f13vc_f13_volume_price_confirmation_upvolshare_63d_base_v108_signal,
    f13vc_f13_volume_price_confirmation_updnmom_21d_base_v109_signal,
    f13vc_f13_volume_price_confirmation_volretasym_63d_base_v110_signal,
    f13vc_f13_volume_price_confirmation_nvi_63d_base_v111_signal,
    f13vc_f13_volume_price_confirmation_pvi_63d_base_v112_signal,
    f13vc_f13_volume_price_confirmation_dvobvslope_63d_base_v113_signal,
    f13vc_f13_volume_price_confirmation_dvmfi_21d_base_v114_signal,
    f13vc_f13_volume_price_confirmation_dvforcez_126d_base_v115_signal,
    f13vc_f13_volume_price_confirmation_cmftrend_126d_base_v116_signal,
    f13vc_f13_volume_price_confirmation_addrawdown_126d_base_v117_signal,
    f13vc_f13_volume_price_confirmation_obvdrawdown_126d_base_v118_signal,
    f13vc_f13_volume_price_confirmation_mfvbreadth_63d_base_v119_signal,
    f13vc_f13_volume_price_confirmation_volthrust_63d_base_v120_signal,
    f13vc_f13_volume_price_confirmation_clvret_21d_base_v121_signal,
    f13vc_f13_volume_price_confirmation_mfratio_21d_base_v122_signal,
    f13vc_f13_volume_price_confirmation_clvabove_63d_base_v123_signal,
    f13vc_f13_volume_price_confirmation_cmf21slope_63d_base_v124_signal,
    f13vc_f13_volume_price_confirmation_effdiv_63d_base_v125_signal,
    f13vc_f13_volume_price_confirmation_cmfstab_126d_base_v126_signal,
    f13vc_f13_volume_price_confirmation_obvpvtdiv_63d_base_v127_signal,
    f13vc_f13_volume_price_confirmation_cmfmompx_21d_base_v128_signal,
    f13vc_f13_volume_price_confirmation_distdays_21d_base_v129_signal,
    f13vc_f13_volume_price_confirmation_accdays_21d_base_v130_signal,
    f13vc_f13_volume_price_confirmation_netaccdist_63d_base_v131_signal,
    f13vc_f13_volume_price_confirmation_mfiobvagree_63d_base_v132_signal,
    f13vc_f13_volume_price_confirmation_volaccel_21d_base_v133_signal,
    f13vc_f13_volume_price_confirmation_cmfrising_126d_base_v134_signal,
    f13vc_f13_volume_price_confirmation_adoscdiv_63d_base_v135_signal,
    f13vc_f13_volume_price_confirmation_momquality_63d_base_v136_signal,
    f13vc_f13_volume_price_confirmation_eomforce_21d_base_v137_signal,
    f13vc_f13_volume_price_confirmation_signedimpact_21d_base_v138_signal,
    f13vc_f13_volume_price_confirmation_obvosc_21d_base_v139_signal,
    f13vc_f13_volume_price_confirmation_cmfvolint_21d_base_v140_signal,
    f13vc_f13_volume_price_confirmation_cmfreversal_63d_base_v141_signal,
    f13vc_f13_volume_price_confirmation_forcecum_63d_base_v142_signal,
    f13vc_f13_volume_price_confirmation_elasttrend_63d_base_v143_signal,
    f13vc_f13_volume_price_confirmation_tpobvslope_63d_base_v144_signal,
    f13vc_f13_volume_price_confirmation_adaccel_base_v145_signal,
    f13vc_f13_volume_price_confirmation_breakvol_21d_base_v146_signal,
    f13vc_f13_volume_price_confirmation_mfobvspr_63d_base_v147_signal,
    f13vc_f13_volume_price_confirmation_stealth_63d_base_v148_signal,
    f13vc_f13_volume_price_confirmation_loud_63d_base_v149_signal,
    f13vc_f13_volume_price_confirmation_stealthspr_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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

    print("OK f13_volume_price_confirmation_base_076_150_claude: %d features pass" % n_features)
