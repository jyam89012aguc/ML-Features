"""volume_blowoff_climax d3 features 151-225 — Pipeline 1b-technical.

75 additional distinct hypotheses extending the 150 in __base__001_075.py /
__base__076_150.py. Themes: VROC, VPT, NVI/PVI, TMF/DMD/TVI, VWAP-band,
CDV, VSA effort/result, log-vol Hurst/AR/jumps, Karpoff, IBD distribution,
Wyckoff/VSA composites, volume-at-price profile, ARCH(1), Geweke-Porter long
memory.

Inputs: SEP OHLCV. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _rolling_vwap(close, volume, n):
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    v = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, v)


def _cdv(open_, close, volume):
    sgn = np.sign(close - open_).fillna(0)
    return (sgn * volume).cumsum()


# ============================================================
# 151-153: Volume Rate-of-Change
# ============================================================

def f19_vblc_151_vroc_21d(volume: pd.Series) -> pd.Series:
    v_prev = volume.shift(21)
    return _safe_div(volume - v_prev, v_prev)


def f19_vblc_152_vroc_63d(volume: pd.Series) -> pd.Series:
    v_prev = volume.shift(63)
    return _safe_div(volume - v_prev, v_prev)


def f19_vblc_153_vroc_acceleration_21d_vs_63d(volume: pd.Series) -> pd.Series:
    v21 = _safe_div(volume - volume.shift(21), volume.shift(21))
    v63 = _safe_div(volume - volume.shift(63), volume.shift(63))
    return v21 - v63


# ============================================================
# 154-155: Ease of Movement
# ============================================================

def f19_vblc_154_ease_of_movement_arms_14d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    mid_change = mid.diff()
    box = _safe_div(volume, (high - low).replace(0, np.nan))
    eom = _safe_div(mid_change, box)
    return eom.rolling(14, min_periods=5).mean()


def f19_vblc_155_ease_of_movement_zscore_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    mid_change = mid.diff()
    box = _safe_div(volume, (high - low).replace(0, np.nan))
    eom = _safe_div(mid_change, box)
    return _rolling_zscore(eom, 63, min_periods=21)


# ============================================================
# 156-157: Volume Price Trend
# ============================================================

def f19_vblc_156_vpt_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    vpt = (ret * volume).cumsum()
    return _rolling_slope(vpt, 21, min_periods=7)


def f19_vblc_157_vpt_close_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    vpt = (ret * volume).cumsum()
    pmax = close.rolling(63, min_periods=21).max()
    vmax = vpt.rolling(63, min_periods=21).max()
    p_at = (close >= pmax).astype(float)
    v_below = (vpt < vmax).astype(float)
    return (p_at * v_below).where(pmax.notna() & vmax.notna(), np.nan)


# ============================================================
# 158-160: NVI / PVI
# ============================================================

def f19_vblc_158_nvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    down_vol = volume < volume.shift(1)
    inc = np.where(down_vol & ret.notna(), ret, 0.0)
    nvi = pd.Series(np.cumsum(inc), index=close.index)
    return _rolling_slope(nvi, 63, min_periods=21)


def f19_vblc_159_pvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    up_vol = volume > volume.shift(1)
    inc = np.where(up_vol & ret.notna(), ret, 0.0)
    pvi = pd.Series(np.cumsum(inc), index=close.index)
    return _rolling_slope(pvi, 63, min_periods=21)


def f19_vblc_160_nvi_pvi_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    dv = volume < volume.shift(1)
    uv = volume > volume.shift(1)
    nvi = pd.Series(np.cumsum(np.where(dv & ret.notna(), ret, 0.0)), index=close.index)
    pvi = pd.Series(np.cumsum(np.where(uv & ret.notna(), ret, 0.0)), index=close.index)
    return _rolling_slope(nvi, 63, min_periods=21) - _rolling_slope(pvi, 63, min_periods=21)


# ============================================================
# 161-164: TMF / DMD / TVI / VW-MACD
# ============================================================

def f19_vblc_161_twiggs_money_flow_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    ad = (2 * close - high - low) / tr.replace(0, np.nan)
    adv = ad * volume
    return _safe_div(_ema(adv, 21), _ema(volume, 21))


def f19_vblc_162_demand_index_sibbet_14d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    ret = close.pct_change()
    p = (ret * volume) / rng
    bp = p.where(p > 0, 0.0)
    sp = (-p).where(p < 0, 0.0)
    bp_s = bp.rolling(14, min_periods=5).sum()
    sp_s = sp.rolling(14, min_periods=5).sum()
    return _safe_div(bp_s - sp_s, bp_s + sp_s)


def f19_vblc_163_tvi_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    sgn = np.sign(close - mid).fillna(0)
    tvi = (sgn * volume).cumsum()
    return _rolling_slope(tvi, 21, min_periods=7)


def f19_vblc_164_vw_macd_signal_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = close * volume
    f12 = _safe_div(_ema(pv, 12), _ema(volume, 12))
    f26 = _safe_div(_ema(pv, 26), _ema(volume, 26))
    macd = f12 - f26
    signal = _ema(macd, 9)
    cross = ((macd.shift(1) >= signal.shift(1)) & (macd < signal)).astype(float)
    return cross.rolling(63, min_periods=21).sum()


# ============================================================
# 165-166: VWAP bands
# ============================================================

def f19_vblc_165_vwap_band_upper_breach_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwap = _rolling_vwap(close, volume, 63)
    sd = close.rolling(63, min_periods=21).std()
    upper = vwap + 2.0 * sd
    breach = (close > upper).astype(float).where(upper.notna(), np.nan)
    return breach.rolling(63, min_periods=21).sum()


def f19_vblc_166_bars_above_vwap_upper_band_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwap = _rolling_vwap(close, volume, 63)
    sd = close.rolling(63, min_periods=21).std()
    upper = vwap + 2.0 * sd
    above = (close > upper).astype(float).where(upper.notna(), np.nan)
    return above.rolling(63, min_periods=21).sum()


# ============================================================
# 167-169: Cumulative Volume Delta proxy
# ============================================================

def f19_vblc_167_cdv_proxy_slope_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cdv = _cdv(open, close, volume)
    return _rolling_slope(cdv, 21, min_periods=7)


def f19_vblc_168_cdv_price_bearish_divergence_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cdv = _cdv(open, close, volume)
    pmax = close.rolling(63, min_periods=21).max()
    cmax = cdv.rolling(63, min_periods=21).max()
    p_new = (close >= pmax).astype(float)
    c_below = (cdv < cmax).astype(float)
    return (p_new * c_below).where(pmax.notna() & cmax.notna(), np.nan)


def f19_vblc_169_cdv_drawdown_from_63d_peak(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cdv = _cdv(open, close, volume)
    cmax = cdv.rolling(63, min_periods=21).max()
    return cdv - cmax


# ============================================================
# 170-171: VSA effort vs result
# ============================================================

def f19_vblc_170_effort_vs_result_ratio_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = _safe_log(close).diff().abs()
    er = _safe_div(volume, ret.replace(0, np.nan))
    return er.rolling(21, min_periods=7).mean()


def f19_vblc_171_effort_no_result_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    med_v = volume.rolling(21, min_periods=7).median()
    big_v = volume > 1.5 * med_v
    ret = close.pct_change().abs()
    atr_r = _atr(high, low, close, n=21) / close.replace(0, np.nan)
    small_r = ret < 0.3 * atr_r
    flag = (big_v & small_r).astype(float).where(med_v.notna() & atr_r.notna(), np.nan)
    return flag.rolling(21, min_periods=7).sum()


# ============================================================
# 172-173: Vol of vol
# ============================================================

def f19_vblc_172_vol_of_vol_63d(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(63, min_periods=21).std()


def f19_vblc_173_vol_of_vol_zscore_63d_in_252d(volume: pd.Series) -> pd.Series:
    vov = _safe_log(volume).rolling(63, min_periods=21).std()
    return _rolling_zscore(vov, 252, min_periods=84)


# ============================================================
# 174-178: Log-vol autocorr / Hurst / ARCH-LM
# ============================================================

def f19_vblc_174_arch_lm_stat_log_vol_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    r = lv.diff()
    r2 = r * r
    def _lm(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        y = v[1:]; x = v[:-1]
        if y.size < 10:
            return np.nan
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((x - xm) * (y - ym)).sum() / sxx
        a = ym - b * xm
        pred = a + b * x
        ss_res = ((y - pred) ** 2).sum()
        ss_tot = ((y - ym) ** 2).sum()
        if ss_tot <= 0:
            return np.nan
        r2_stat = 1.0 - ss_res / ss_tot
        return float(y.size * r2_stat)
    return r2.rolling(63, min_periods=21).apply(_lm, raw=True)


def f19_vblc_175_log_vol_hurst_exponent_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _hurst(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 64:
            return np.nan
        lags = [4, 8, 16, 32, 64]
        rs_vals = []
        for L in lags:
            if L >= n:
                break
            chunks = n // L
            if chunks < 2:
                continue
            rs_list = []
            for k in range(chunks):
                seg = v[k * L:(k + 1) * L]
                mu = seg.mean()
                dev = seg - mu
                cs = np.cumsum(dev)
                R = cs.max() - cs.min()
                S = seg.std(ddof=1)
                if S > 0:
                    rs_list.append(R / S)
            if rs_list:
                rs_vals.append((L, np.mean(rs_list)))
        if len(rs_vals) < 3:
            return np.nan
        xs = np.log([p[0] for p in rs_vals])
        ys = np.log([p[1] for p in rs_vals])
        xm = xs.mean(); ym = ys.mean()
        den = ((xs - xm) ** 2).sum()
        if den <= 0:
            return np.nan
        return float(((xs - xm) * (ys - ym)).sum() / den)
    return lv.rolling(252, min_periods=84).apply(_hurst, raw=True)


def f19_vblc_176_log_vol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        y = v[1:]; x = v[:-1]
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((y - ym) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(num / den)
    return lv.rolling(63, min_periods=21).apply(_ac, raw=True)


def f19_vblc_177_log_vol_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 15:
            return np.nan
        y = v[5:]; x = v[:-5]
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((y - ym) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(num / den)
    return lv.rolling(63, min_periods=21).apply(_ac, raw=True)


def f19_vblc_178_log_vol_autocorr_change_21d_vs_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        y = v[1:]; x = v[:-1]
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((y - ym) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(num / den)
    a21 = lv.rolling(21, min_periods=10).apply(_ac, raw=True)
    a63 = lv.rolling(63, min_periods=21).apply(_ac, raw=True)
    return a21 - a63


# ============================================================
# 179-181: Jump detection on log-vol
# ============================================================

def f19_vblc_179_lee_mykland_vol_jump_count_63d(volume: pd.Series) -> pd.Series:
    r = _safe_log(volume).diff()
    rv_loc = (r.abs()).rolling(21, min_periods=7).mean()
    stat = (r.abs() / rv_loc.replace(0, np.nan))
    jump = (stat > 3.0).astype(float).where(rv_loc.notna(), np.nan)
    return jump.rolling(63, min_periods=21).sum()


def f19_vblc_180_bns_jump_variance_share_vol_63d(volume: pd.Series) -> pd.Series:
    r = _safe_log(volume).diff()
    rv = (r * r).rolling(63, min_periods=21).sum()
    bv_term = (r.abs() * r.shift(1).abs())
    bv = (np.pi / 2.0) * bv_term.rolling(63, min_periods=21).sum()
    return _safe_div(rv - bv, rv.replace(0, np.nan))


def f19_vblc_181_bipower_variation_log_vol_63d(volume: pd.Series) -> pd.Series:
    r = _safe_log(volume).diff()
    bv_term = (r.abs() * r.shift(1).abs())
    return (np.pi / 2.0) * bv_term.rolling(63, min_periods=21).sum()


# ============================================================
# 182-183: Karpoff vol-absret correlation
# ============================================================

def f19_vblc_182_karpoff_vol_absret_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    ar = _safe_log(close).diff().abs()
    return lv.rolling(63, min_periods=21).corr(ar)


def f19_vblc_183_karpoff_corr_change_21d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    ar = _safe_log(close).diff().abs()
    c21 = lv.rolling(21, min_periods=10).corr(ar)
    c63 = lv.rolling(63, min_periods=21).corr(ar)
    return c21 - c63


# ============================================================
# 184-185: Block trade signatures
# ============================================================

def f19_vblc_184_block_trade_signature_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    vz = _rolling_zscore(lv, 63, min_periods=21)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=21)
    big_v = (vz > 3.0).astype(float)
    narrow = (tr < 0.5 * atr).astype(float)
    sig = (big_v * narrow).where(vz.notna() & atr.notna(), np.nan)
    return sig.rolling(63, min_periods=21).sum()


def f19_vblc_185_block_trade_signature_intensity_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    vz = _rolling_zscore(lv, 63, min_periods=21)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=21)
    narrow = tr < 0.5 * atr
    big = vz > 3.0
    mag = vz.where(big & narrow, 0.0)
    return mag.rolling(252, min_periods=84).sum()


# ============================================================
# 186: Price-mom vs vol-trend divergence
# ============================================================

def f19_vblc_186_price_mom_vs_vol_trend_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    sl_v = _rolling_slope(lv, 63, min_periods=21)
    sl_p = _rolling_slope(_safe_log(close), 63, min_periods=21)
    z_v = _rolling_zscore(sl_v, 252, min_periods=84)
    z_p = _rolling_zscore(sl_p, 252, min_periods=84)
    return z_v - z_p


# ============================================================
# 187-191: IBD-style distribution / churn days
# ============================================================

def f19_vblc_187_stalling_day_ibd_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    ret = close.pct_change()
    cond = (pos < 0.5) & (volume > volume.shift(1)) & (ret > 0)
    flag = cond.astype(float).where(volume.notna() & pos.notna() & ret.notna(), np.nan)
    return flag.rolling(21, min_periods=7).sum()


def f19_vblc_188_distribution_day_ibd_strict_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    cond = (ret <= -0.002) & (volume > volume.shift(1))
    flag = cond.astype(float).where(ret.notna() & volume.notna(), np.nan)
    return flag.rolling(21, min_periods=7).sum()


def f19_vblc_189_distribution_day_ibd_strict_count_25d_window(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    cond = (ret <= -0.002) & (volume > volume.shift(1))
    flag = cond.astype(float).where(ret.notna() & volume.notna(), np.nan)
    return flag.rolling(25, min_periods=8).sum()


def f19_vblc_190_five_distribution_days_in_25d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    cond = (ret <= -0.002) & (volume > volume.shift(1))
    flag = cond.astype(float).where(ret.notna() & volume.notna(), np.nan)
    cnt = flag.rolling(25, min_periods=8).sum()
    return (cnt >= 5).astype(float).where(cnt.notna(), np.nan)


def f19_vblc_191_churn_day_ibd_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    med_v = volume.rolling(21, min_periods=7).median()
    cond = (ret.abs() < 0.002) & (volume > 1.5 * med_v)
    flag = cond.astype(float).where(ret.notna() & med_v.notna(), np.nan)
    return flag.rolling(21, min_periods=7).sum()


# ============================================================
# 192-193: Climax bar vol pct-rank in 504/1260 d
# ============================================================

def f19_vblc_192_climax_vol_pct_rank_504d(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 100:
            return np.nan
        idx_pk = int(np.nanargmax(w))
        peak_v = w[idx_pk]
        if np.isnan(peak_v):
            return np.nan
        return float((v <= peak_v).sum()) / float(v.size)
    return volume.rolling(504, min_periods=168).apply(_f, raw=True)


def f19_vblc_193_climax_vol_pct_rank_1260d(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 252:
            return np.nan
        idx_pk = int(np.nanargmax(w))
        peak_v = w[idx_pk]
        if np.isnan(peak_v):
            return np.nan
        return float((v <= peak_v).sum()) / float(v.size)
    return volume.rolling(1260, min_periods=252).apply(_f, raw=True)


# ============================================================
# 194-195: MAD of log-vol
# ============================================================

def f19_vblc_194_log_vol_mad_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    med = lv.rolling(63, min_periods=21).median()
    return (lv - med).abs().rolling(63, min_periods=21).median()


def f19_vblc_195_log_vol_mad_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    med = lv.rolling(252, min_periods=84).median()
    return (lv - med).abs().rolling(252, min_periods=84).median()


# ============================================================
# 196-197: Yule-Bowley skewness
# ============================================================

def _yb_skew(w):
    v = w[~np.isnan(w)]
    if v.size < 10:
        return np.nan
    q1 = np.percentile(v, 25)
    q2 = np.percentile(v, 50)
    q3 = np.percentile(v, 75)
    den = q3 - q1
    if den <= 0:
        return np.nan
    return float((q3 + q1 - 2 * q2) / den)


def f19_vblc_196_log_vol_yule_bowley_skew_63d(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(63, min_periods=21).apply(_yb_skew, raw=True)


def f19_vblc_197_log_vol_yule_bowley_skew_252d(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(252, min_periods=84).apply(_yb_skew, raw=True)


# ============================================================
# 198-199: Pareto tail
# ============================================================

def _hill_alpha(w, frac=0.1):
    v = w[~np.isnan(w)]
    v = v[v > 0]
    if v.size < 50:
        return np.nan
    k = max(5, int(v.size * frac))
    if k >= v.size:
        return np.nan
    s = np.sort(v)[-k - 1:]
    thr = s[0]
    if thr <= 0:
        return np.nan
    tail = s[1:]
    lr = np.log(tail / thr)
    m = lr.mean()
    if m <= 0:
        return np.nan
    return float(1.0 / m)


def f19_vblc_198_vol_pareto_tail_exponent_252d(volume: pd.Series) -> pd.Series:
    return volume.rolling(252, min_periods=84).apply(_hill_alpha, raw=True)


def f19_vblc_199_vol_pareto_tail_alpha_change_63_vs_252(volume: pd.Series) -> pd.Series:
    a63 = volume.rolling(63, min_periods=21).apply(_hill_alpha, raw=True)
    a252 = volume.rolling(252, min_periods=84).apply(_hill_alpha, raw=True)
    return a63 - a252


# ============================================================
# 200-202: HHI of vol-shares
# ============================================================

def _hhi(w):
    v = w[~np.isnan(w)]
    v = v[v >= 0]
    s = v.sum()
    if s <= 0 or v.size < 5:
        return np.nan
    shares = v / s
    return float((shares * shares).sum())


def f19_vblc_200_vol_herfindahl_concentration_63d(volume: pd.Series) -> pd.Series:
    return volume.rolling(63, min_periods=21).apply(_hhi, raw=True)


def f19_vblc_201_vol_herfindahl_concentration_252d(volume: pd.Series) -> pd.Series:
    return volume.rolling(252, min_periods=84).apply(_hhi, raw=True)


def f19_vblc_202_vol_herfindahl_change_63d_in_252d(volume: pd.Series) -> pd.Series:
    h63 = volume.rolling(63, min_periods=21).apply(_hhi, raw=True)
    h252 = volume.rolling(252, min_periods=84).apply(_hhi, raw=True)
    return h63 - h252


# ============================================================
# 203-206: Post-peak vol re-entry / decay fit
# ============================================================

def f19_vblc_203_post_peak_vol_reentry_speed_63d(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        pk = int(np.nanargmax(w))
        med = np.nanmedian(w)
        if np.isnan(med):
            return np.nan
        for j in range(pk + 1, w.size):
            if not np.isnan(w[j]) and w[j] <= med:
                return float(j - pk)
        return float(w.size - pk)
    return volume.rolling(63, min_periods=21).apply(_f, raw=True)


def f19_vblc_204_post_peak_oscillation_count_63d(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 22 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        med = np.nanmedian(w)
        if np.isnan(med):
            return np.nan
        end = min(w.size, pk + 22)
        seg = w[pk + 1:end]
        if seg.size < 3:
            return 0.0
        above = (seg > med).astype(int)
        crossings = int(np.sum(np.diff(above) != 0))
        return float(crossings)
    return volume.rolling(63, min_periods=21).apply(_f, raw=True)


def f19_vblc_205_post_peak_decay_residual_variance_63d(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 22 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        seg = w[pk:min(w.size, pk + 22)]
        valid = ~np.isnan(seg) & (seg > 0)
        if valid.sum() < 5:
            return np.nan
        x = np.arange(seg.size, dtype=float)[valid]
        y = np.log(seg[valid])
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den <= 0:
            return np.nan
        b = ((x - xm) * (y - ym)).sum() / den
        a = ym - b * xm
        pred = a + b * x
        res = y - pred
        return float(np.var(res, ddof=1)) if res.size > 1 else np.nan
    return volume.rolling(63, min_periods=21).apply(_f, raw=True)


def f19_vblc_206_post_peak_decay_r2_63d(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 22 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        seg = w[pk:min(w.size, pk + 22)]
        valid = ~np.isnan(seg) & (seg > 0)
        if valid.sum() < 5:
            return np.nan
        x = np.arange(seg.size, dtype=float)[valid]
        y = np.log(seg[valid])
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den <= 0:
            return np.nan
        b = ((x - xm) * (y - ym)).sum() / den
        a = ym - b * xm
        pred = a + b * x
        ss_res = ((y - pred) ** 2).sum()
        ss_tot = ((y - ym) ** 2).sum()
        if ss_tot <= 0:
            return np.nan
        return float(1.0 - ss_res / ss_tot)
    return volume.rolling(63, min_periods=21).apply(_f, raw=True)


# ============================================================
# 207-208: Float rotation / cum excess
# ============================================================

def f19_vblc_207_float_rotation_proxy_252d(volume: pd.Series) -> pd.Series:
    m = volume.rolling(252, min_periods=84).mean()
    return _safe_div(volume, m)


def f19_vblc_208_cum_excess_vol_over_252d_mean_63d(volume: pd.Series) -> pd.Series:
    m = volume.rolling(252, min_periods=84).mean()
    exc = (volume - m).fillna(0)
    return exc.rolling(63, min_periods=21).sum().where(m.notna(), np.nan)


# ============================================================
# 209: Strict climax triple-criteria
# ============================================================

def f19_vblc_209_strict_climax_triple_criteria_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 252, min_periods=84)
    tr = _true_range(high, low, close)
    tz = _rolling_zscore(tr, 252, min_periods=84)
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    cond = (vz > 3.0) & (tz > 2.0) & (pos < 0.5)
    flag = cond.astype(float).where(vz.notna() & tz.notna() & pos.notna(), np.nan)
    return flag.rolling(252, min_periods=84).sum()


# ============================================================
# 210-211: VSA test / UTAD
# ============================================================

def f19_vblc_210_vsa_test_bar_after_climax_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_v = volume.rolling(63, min_periods=21).max()
    climax = (volume >= 0.9 * rmax_v).astype(int)
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    med_v = volume.rolling(21, min_periods=7).median()
    low_v = volume < med_v
    down = close < close.shift(1)
    upper_half = pos > 0.5
    test = (low_v & down & upper_half).astype(int)
    recent_climax = climax.shift(1).rolling(10, min_periods=1).max().fillna(0)
    out = (test * recent_climax).astype(float).where(med_v.notna() & pos.notna() & rmax_v.notna(), np.nan)
    return out


def f19_vblc_211_vsa_upthrust_after_distribution_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_h = high.rolling(21, min_periods=7).max()
    new_h = high >= rmax_h
    rev = close < close.shift(1)
    med_v = volume.rolling(21, min_periods=7).median()
    big_v = volume > 1.5 * med_v
    utad = (new_h & rev & big_v).astype(float).where(med_v.notna() & rmax_h.notna(), np.nan)
    return utad.rolling(63, min_periods=21).sum()


# ============================================================
# 212-214: Wyckoff composites
# ============================================================

def f19_vblc_212_wyckoff_buying_climax_signature_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = volume.rolling(252, min_periods=84).apply(_rk, raw=True)
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    rmax_h = high.rolling(63, min_periods=21).max()
    cond = (rk > 0.95) & (pos < (1.0 / 3.0)) & (high >= rmax_h)
    return cond.astype(float).where(rk.notna() & pos.notna() & rmax_h.notna(), np.nan)


def f19_vblc_213_wyckoff_automatic_reaction_depth_after_bc(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    def _f(arr):
        n = arr.shape[0]
        if n < 22:
            return np.nan
        v_col = arr[:, 0]
        l_col = arr[:, 1]
        h_col = arr[:, 2]
        atr_col = arr[:, 3]
        pk = int(np.nanargmax(v_col))
        if pk >= n - 10:
            return np.nan
        bc_high = h_col[pk]
        atr_v = atr_col[pk]
        if np.isnan(bc_high) or np.isnan(atr_v) or atr_v <= 0:
            return np.nan
        post = l_col[pk + 1:pk + 11]
        if np.isnan(post).all():
            return np.nan
        return float((bc_high - np.nanmin(post)) / atr_v)
    atr_s = _atr(high, low, close, n=21)
    df = pd.concat([volume.rename('v'), low.rename('l'), high.rename('h'), atr_s.rename('a')], axis=1)
    n = len(df)
    out = np.full(n, np.nan)
    arr_all = df.values
    win = 63
    for i in range(n):
        if i < 21:
            continue
        lo = max(0, i - win + 1)
        seg = arr_all[lo:i + 1]
        out[i] = _f(seg)
    return pd.Series(out, index=high.index)


def f19_vblc_214_preliminary_supply_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    vz = _rolling_zscore(lv, 63, min_periods=21)
    ma50 = close.rolling(50, min_periods=20).mean()
    above = (close > ma50).astype(int)
    streak = above.rolling(50, min_periods=20).sum()
    in_trend = streak >= 40
    spike = (vz > 2.0).astype(float)
    flag = (spike * in_trend.astype(float)).where(vz.notna() & in_trend.notna(), np.nan)
    return flag.rolling(63, min_periods=21).sum()


# ============================================================
# 215-217: Volume at price profile
# ============================================================

def _vap_stats(close_arr, vol_arr, n_bins=20):
    valid = ~np.isnan(close_arr) & ~np.isnan(vol_arr)
    if valid.sum() < 50:
        return np.nan, np.nan, np.nan, np.nan
    c = close_arr[valid]
    v = vol_arr[valid]
    lo = c.min(); hi = c.max()
    if hi <= lo:
        return np.nan, np.nan, np.nan, np.nan
    edges = np.linspace(lo, hi, n_bins + 1)
    idx = np.clip(np.searchsorted(edges, c, side='right') - 1, 0, n_bins - 1)
    bin_vol = np.zeros(n_bins)
    for k in range(c.size):
        bin_vol[idx[k]] += v[k]
    top_bin = int(np.argmax(bin_vol))
    top_price = (edges[top_bin] + edges[top_bin + 1]) / 2.0
    current = close_arr[-1] if not np.isnan(close_arr[-1]) else c[-1]
    cur_bin = int(np.clip(np.searchsorted(edges, current, side='right') - 1, 0, n_bins - 1))
    med_v = np.median(bin_vol[bin_vol > 0]) if (bin_vol > 0).any() else 0.0
    hvn_thresh = 2.0 * med_v
    above_hvn = int(np.sum((bin_vol[cur_bin + 1:] > hvn_thresh))) if cur_bin + 1 < n_bins else 0
    below_hvn = int(np.sum((bin_vol[:cur_bin] > hvn_thresh))) if cur_bin > 0 else 0
    return top_price, current, above_hvn, below_hvn


def f19_vblc_215_volume_at_price_top_node_distance(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr_s = _atr(high, low, close, n=21)
    c_arr = close.values
    v_arr = volume.values
    a_arr = atr_s.values
    n = len(close)
    out = np.full(n, np.nan)
    win = 252
    for i in range(n):
        if i < 84:
            continue
        lo = max(0, i - win + 1)
        tp, cur, _, _ = _vap_stats(c_arr[lo:i + 1], v_arr[lo:i + 1])
        if np.isnan(tp) or np.isnan(cur):
            continue
        atr_v = a_arr[i]
        if np.isnan(atr_v) or atr_v <= 0:
            continue
        out[i] = float((cur - tp) / atr_v)
    return pd.Series(out, index=close.index)


def f19_vblc_216_volume_at_price_node_above_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    c_arr = close.values
    v_arr = volume.values
    n = len(close)
    out = np.full(n, np.nan)
    win = 252
    for i in range(n):
        if i < 84:
            continue
        lo = max(0, i - win + 1)
        _, _, above, _ = _vap_stats(c_arr[lo:i + 1], v_arr[lo:i + 1])
        if np.isnan(above) if isinstance(above, float) else False:
            continue
        out[i] = float(above)
    return pd.Series(out, index=close.index)


def f19_vblc_217_hvn_lvn_ratio_above_below_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    c_arr = close.values
    v_arr = volume.values
    n = len(close)
    out = np.full(n, np.nan)
    win = 252
    for i in range(n):
        if i < 84:
            continue
        lo = max(0, i - win + 1)
        _, _, above, below = _vap_stats(c_arr[lo:i + 1], v_arr[lo:i + 1])
        if isinstance(above, float) and np.isnan(above):
            continue
        if below <= 0:
            out[i] = np.nan if above == 0 else float(above + 1)
        else:
            out[i] = float(above) / float(below)
    return pd.Series(out, index=close.index)


# ============================================================
# 218-220: Entropy diff / kurt regime break
# ============================================================

def _entropy_window(w, bins=10):
    v = w[~np.isnan(w)]
    if v.size < 10:
        return np.nan
    h, _ = np.histogram(v, bins=bins)
    s = h.sum()
    if s <= 0:
        return np.nan
    p = h[h > 0] / s
    return float(-(p * np.log(p)).sum())


def f19_vblc_218_vol_entropy_diff_21d_vs_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    e21 = lv.rolling(21, min_periods=10).apply(_entropy_window, raw=True)
    e252 = lv.rolling(252, min_periods=84).apply(_entropy_window, raw=True)
    return e21 - e252


def f19_vblc_219_vol_entropy_diff_63d_vs_504d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    e63 = lv.rolling(63, min_periods=21).apply(_entropy_window, raw=True)
    e504 = lv.rolling(504, min_periods=168).apply(_entropy_window, raw=True)
    return e63 - e504


def _kurt_window(w):
    v = w[~np.isnan(w)]
    if v.size < 10:
        return np.nan
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    return float(np.mean(((v - m) / sd) ** 4) - 3.0)


def f19_vblc_220_vol_kurtosis_regime_break_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    k63 = lv.rolling(63, min_periods=21).apply(_kurt_window, raw=True)
    k252 = lv.rolling(252, min_periods=84).apply(_kurt_window, raw=True)
    diff = k63 - k252
    sd = diff.rolling(252, min_periods=84).std()
    return (diff.abs() > 2.0 * sd).astype(float).where(diff.notna() & sd.notna(), np.nan)


# ============================================================
# 221-223: sign-vol corr / reach-back rank / decay speed
# ============================================================

def f19_vblc_221_sign_vol_return_correlation_breakdown_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0)
    return sgn.rolling(63, min_periods=21).corr(volume)


def f19_vblc_222_reach_back_vol_rank_lifetime(volume: pd.Series) -> pd.Series:
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return volume.expanding(min_periods=63).apply(_rk, raw=True)


def f19_vblc_223_vol_pct_rank_decay_speed_after_peak(volume: pd.Series) -> pd.Series:
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    r = volume.rolling(63, min_periods=21).apply(_rk, raw=True)
    arr = r.values
    n = arr.size
    out = np.full(n, np.nan)
    last_peak_idx = -1
    for i in range(n):
        if not np.isnan(arr[i]) and arr[i] >= 1.0:
            last_peak_idx = i
        if last_peak_idx >= 0 and not np.isnan(arr[i]) and arr[i] < 0.5:
            out[i] = float(i - last_peak_idx)
            last_peak_idx = -1
    return pd.Series(out, index=volume.index)


# ============================================================
# 224-225: ARCH(1) coeff / Geweke-Porter-Hudak
# ============================================================

def f19_vblc_224_vol_arch1_coefficient_252d(volume: pd.Series) -> pd.Series:
    r = _safe_log(volume).diff()
    r2 = r * r
    def _ar1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        y = v[1:]; x = v[:-1]
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / sxx)
    return r2.rolling(252, min_periods=84).apply(_ar1, raw=True)


def f19_vblc_225_vol_long_memory_geweke_porter_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _gph(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 128:
            return np.nan
        vd = v - v.mean()
        # periodogram via real FFT
        f = np.fft.rfft(vd)
        per = (np.abs(f) ** 2) / n
        m = int(np.floor(n ** 0.5))
        if m < 8:
            return np.nan
        # frequencies 1..m
        freqs = (2.0 * np.pi * np.arange(1, m + 1)) / n
        y = np.log(per[1:m + 1] + 1e-30)
        x = np.log(2.0 * np.sin(freqs / 2.0) ** 2 + 1e-30)
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den <= 0:
            return np.nan
        slope = ((x - xm) * (y - ym)).sum() / den
        return float(-slope)
    return lv.rolling(252, min_periods=128).apply(_gph, raw=True)


# ============================================================
#                  REGISTRY 151_225 (base)
# ============================================================



def f19_vblc_151_vroc_21d_d3(volume):
    return f19_vblc_151_vroc_21d(volume).diff().diff().diff()


def f19_vblc_152_vroc_63d_d3(volume):
    return f19_vblc_152_vroc_63d(volume).diff().diff().diff()


def f19_vblc_153_vroc_acceleration_21d_vs_63d_d3(volume):
    return f19_vblc_153_vroc_acceleration_21d_vs_63d(volume).diff().diff().diff()


def f19_vblc_154_ease_of_movement_arms_14d_d3(high, low, volume):
    return f19_vblc_154_ease_of_movement_arms_14d(high, low, volume).diff().diff().diff()


def f19_vblc_155_ease_of_movement_zscore_63d_d3(high, low, volume):
    return f19_vblc_155_ease_of_movement_zscore_63d(high, low, volume).diff().diff().diff()


def f19_vblc_156_vpt_slope_21d_d3(close, volume):
    return f19_vblc_156_vpt_slope_21d(close, volume).diff().diff().diff()


def f19_vblc_157_vpt_close_divergence_63d_d3(close, volume):
    return f19_vblc_157_vpt_close_divergence_63d(close, volume).diff().diff().diff()


def f19_vblc_158_nvi_slope_63d_d3(close, volume):
    return f19_vblc_158_nvi_slope_63d(close, volume).diff().diff().diff()


def f19_vblc_159_pvi_slope_63d_d3(close, volume):
    return f19_vblc_159_pvi_slope_63d(close, volume).diff().diff().diff()


def f19_vblc_160_nvi_pvi_divergence_63d_d3(close, volume):
    return f19_vblc_160_nvi_pvi_divergence_63d(close, volume).diff().diff().diff()


def f19_vblc_161_twiggs_money_flow_21d_d3(high, low, close, volume):
    return f19_vblc_161_twiggs_money_flow_21d(high, low, close, volume).diff().diff().diff()


def f19_vblc_162_demand_index_sibbet_14d_d3(high, low, close, volume):
    return f19_vblc_162_demand_index_sibbet_14d(high, low, close, volume).diff().diff().diff()


def f19_vblc_163_tvi_slope_21d_d3(high, low, close, volume):
    return f19_vblc_163_tvi_slope_21d(high, low, close, volume).diff().diff().diff()


def f19_vblc_164_vw_macd_signal_63d_d3(close, volume):
    return f19_vblc_164_vw_macd_signal_63d(close, volume).diff().diff().diff()


def f19_vblc_165_vwap_band_upper_breach_63d_d3(close, volume):
    return f19_vblc_165_vwap_band_upper_breach_63d(close, volume).diff().diff().diff()


def f19_vblc_166_bars_above_vwap_upper_band_63d_d3(close, volume):
    return f19_vblc_166_bars_above_vwap_upper_band_63d(close, volume).diff().diff().diff()


def f19_vblc_167_cdv_proxy_slope_21d_d3(open, close, volume):
    return f19_vblc_167_cdv_proxy_slope_21d(open, close, volume).diff().diff().diff()


def f19_vblc_168_cdv_price_bearish_divergence_63d_d3(open, close, volume):
    return f19_vblc_168_cdv_price_bearish_divergence_63d(open, close, volume).diff().diff().diff()


def f19_vblc_169_cdv_drawdown_from_63d_peak_d3(open, close, volume):
    return f19_vblc_169_cdv_drawdown_from_63d_peak(open, close, volume).diff().diff().diff()


def f19_vblc_170_effort_vs_result_ratio_21d_mean_d3(close, volume):
    return f19_vblc_170_effort_vs_result_ratio_21d_mean(close, volume).diff().diff().diff()


def f19_vblc_171_effort_no_result_count_21d_d3(high, low, close, volume):
    return f19_vblc_171_effort_no_result_count_21d(high, low, close, volume).diff().diff().diff()


def f19_vblc_172_vol_of_vol_63d_d3(volume):
    return f19_vblc_172_vol_of_vol_63d(volume).diff().diff().diff()


def f19_vblc_173_vol_of_vol_zscore_63d_in_252d_d3(volume):
    return f19_vblc_173_vol_of_vol_zscore_63d_in_252d(volume).diff().diff().diff()


def f19_vblc_174_arch_lm_stat_log_vol_63d_d3(volume):
    return f19_vblc_174_arch_lm_stat_log_vol_63d(volume).diff().diff().diff()


def f19_vblc_175_log_vol_hurst_exponent_252d_d3(volume):
    return f19_vblc_175_log_vol_hurst_exponent_252d(volume).diff().diff().diff()


def f19_vblc_176_log_vol_autocorr_lag1_63d_d3(volume):
    return f19_vblc_176_log_vol_autocorr_lag1_63d(volume).diff().diff().diff()


def f19_vblc_177_log_vol_autocorr_lag5_63d_d3(volume):
    return f19_vblc_177_log_vol_autocorr_lag5_63d(volume).diff().diff().diff()


def f19_vblc_178_log_vol_autocorr_change_21d_vs_63d_d3(volume):
    return f19_vblc_178_log_vol_autocorr_change_21d_vs_63d(volume).diff().diff().diff()


def f19_vblc_179_lee_mykland_vol_jump_count_63d_d3(volume):
    return f19_vblc_179_lee_mykland_vol_jump_count_63d(volume).diff().diff().diff()


def f19_vblc_180_bns_jump_variance_share_vol_63d_d3(volume):
    return f19_vblc_180_bns_jump_variance_share_vol_63d(volume).diff().diff().diff()


def f19_vblc_181_bipower_variation_log_vol_63d_d3(volume):
    return f19_vblc_181_bipower_variation_log_vol_63d(volume).diff().diff().diff()


def f19_vblc_182_karpoff_vol_absret_corr_63d_d3(close, volume):
    return f19_vblc_182_karpoff_vol_absret_corr_63d(close, volume).diff().diff().diff()


def f19_vblc_183_karpoff_corr_change_21d_vs_63d_d3(close, volume):
    return f19_vblc_183_karpoff_corr_change_21d_vs_63d(close, volume).diff().diff().diff()


def f19_vblc_184_block_trade_signature_count_63d_d3(high, low, close, volume):
    return f19_vblc_184_block_trade_signature_count_63d(high, low, close, volume).diff().diff().diff()


def f19_vblc_185_block_trade_signature_intensity_252d_d3(high, low, close, volume):
    return f19_vblc_185_block_trade_signature_intensity_252d(high, low, close, volume).diff().diff().diff()


def f19_vblc_186_price_mom_vs_vol_trend_divergence_63d_d3(close, volume):
    return f19_vblc_186_price_mom_vs_vol_trend_divergence_63d(close, volume).diff().diff().diff()


def f19_vblc_187_stalling_day_ibd_count_21d_d3(high, low, close, volume):
    return f19_vblc_187_stalling_day_ibd_count_21d(high, low, close, volume).diff().diff().diff()


def f19_vblc_188_distribution_day_ibd_strict_count_21d_d3(close, volume):
    return f19_vblc_188_distribution_day_ibd_strict_count_21d(close, volume).diff().diff().diff()


def f19_vblc_189_distribution_day_ibd_strict_count_25d_window_d3(close, volume):
    return f19_vblc_189_distribution_day_ibd_strict_count_25d_window(close, volume).diff().diff().diff()


def f19_vblc_190_five_distribution_days_in_25d_indicator_d3(close, volume):
    return f19_vblc_190_five_distribution_days_in_25d_indicator(close, volume).diff().diff().diff()


def f19_vblc_191_churn_day_ibd_count_21d_d3(close, volume):
    return f19_vblc_191_churn_day_ibd_count_21d(close, volume).diff().diff().diff()


def f19_vblc_192_climax_vol_pct_rank_504d_d3(volume):
    return f19_vblc_192_climax_vol_pct_rank_504d(volume).diff().diff().diff()


def f19_vblc_193_climax_vol_pct_rank_1260d_d3(volume):
    return f19_vblc_193_climax_vol_pct_rank_1260d(volume).diff().diff().diff()


def f19_vblc_194_log_vol_mad_63d_d3(volume):
    return f19_vblc_194_log_vol_mad_63d(volume).diff().diff().diff()


def f19_vblc_195_log_vol_mad_252d_d3(volume):
    return f19_vblc_195_log_vol_mad_252d(volume).diff().diff().diff()


def f19_vblc_196_log_vol_yule_bowley_skew_63d_d3(volume):
    return f19_vblc_196_log_vol_yule_bowley_skew_63d(volume).diff().diff().diff()


def f19_vblc_197_log_vol_yule_bowley_skew_252d_d3(volume):
    return f19_vblc_197_log_vol_yule_bowley_skew_252d(volume).diff().diff().diff()


def f19_vblc_198_vol_pareto_tail_exponent_252d_d3(volume):
    return f19_vblc_198_vol_pareto_tail_exponent_252d(volume).diff().diff().diff()


def f19_vblc_199_vol_pareto_tail_alpha_change_63_vs_252_d3(volume):
    return f19_vblc_199_vol_pareto_tail_alpha_change_63_vs_252(volume).diff().diff().diff()


def f19_vblc_200_vol_herfindahl_concentration_63d_d3(volume):
    return f19_vblc_200_vol_herfindahl_concentration_63d(volume).diff().diff().diff()


def f19_vblc_201_vol_herfindahl_concentration_252d_d3(volume):
    return f19_vblc_201_vol_herfindahl_concentration_252d(volume).diff().diff().diff()


def f19_vblc_202_vol_herfindahl_change_63d_in_252d_d3(volume):
    return f19_vblc_202_vol_herfindahl_change_63d_in_252d(volume).diff().diff().diff()


def f19_vblc_203_post_peak_vol_reentry_speed_63d_d3(volume):
    return f19_vblc_203_post_peak_vol_reentry_speed_63d(volume).diff().diff().diff()


def f19_vblc_204_post_peak_oscillation_count_63d_d3(volume):
    return f19_vblc_204_post_peak_oscillation_count_63d(volume).diff().diff().diff()


def f19_vblc_205_post_peak_decay_residual_variance_63d_d3(volume):
    return f19_vblc_205_post_peak_decay_residual_variance_63d(volume).diff().diff().diff()


def f19_vblc_206_post_peak_decay_r2_63d_d3(volume):
    return f19_vblc_206_post_peak_decay_r2_63d(volume).diff().diff().diff()


def f19_vblc_207_float_rotation_proxy_252d_d3(volume):
    return f19_vblc_207_float_rotation_proxy_252d(volume).diff().diff().diff()


def f19_vblc_208_cum_excess_vol_over_252d_mean_63d_d3(volume):
    return f19_vblc_208_cum_excess_vol_over_252d_mean_63d(volume).diff().diff().diff()


def f19_vblc_209_strict_climax_triple_criteria_count_252d_d3(high, low, close, volume):
    return f19_vblc_209_strict_climax_triple_criteria_count_252d(high, low, close, volume).diff().diff().diff()


def f19_vblc_210_vsa_test_bar_after_climax_indicator_d3(high, low, close, volume):
    return f19_vblc_210_vsa_test_bar_after_climax_indicator(high, low, close, volume).diff().diff().diff()


def f19_vblc_211_vsa_upthrust_after_distribution_count_63d_d3(high, close, volume):
    return f19_vblc_211_vsa_upthrust_after_distribution_count_63d(high, close, volume).diff().diff().diff()


def f19_vblc_212_wyckoff_buying_climax_signature_indicator_d3(high, low, close, volume):
    return f19_vblc_212_wyckoff_buying_climax_signature_indicator(high, low, close, volume).diff().diff().diff()


def f19_vblc_213_wyckoff_automatic_reaction_depth_after_bc_d3(high, low, close, volume):
    return f19_vblc_213_wyckoff_automatic_reaction_depth_after_bc(high, low, close, volume).diff().diff().diff()


def f19_vblc_214_preliminary_supply_count_63d_d3(close, volume):
    return f19_vblc_214_preliminary_supply_count_63d(close, volume).diff().diff().diff()


def f19_vblc_215_volume_at_price_top_node_distance_d3(high, low, close, volume):
    return f19_vblc_215_volume_at_price_top_node_distance(high, low, close, volume).diff().diff().diff()


def f19_vblc_216_volume_at_price_node_above_count_d3(close, volume):
    return f19_vblc_216_volume_at_price_node_above_count(close, volume).diff().diff().diff()


def f19_vblc_217_hvn_lvn_ratio_above_below_252d_d3(close, volume):
    return f19_vblc_217_hvn_lvn_ratio_above_below_252d(close, volume).diff().diff().diff()


def f19_vblc_218_vol_entropy_diff_21d_vs_252d_d3(volume):
    return f19_vblc_218_vol_entropy_diff_21d_vs_252d(volume).diff().diff().diff()


def f19_vblc_219_vol_entropy_diff_63d_vs_504d_d3(volume):
    return f19_vblc_219_vol_entropy_diff_63d_vs_504d(volume).diff().diff().diff()


def f19_vblc_220_vol_kurtosis_regime_break_252d_d3(volume):
    return f19_vblc_220_vol_kurtosis_regime_break_252d(volume).diff().diff().diff()


def f19_vblc_221_sign_vol_return_correlation_breakdown_63d_d3(close, volume):
    return f19_vblc_221_sign_vol_return_correlation_breakdown_63d(close, volume).diff().diff().diff()


def f19_vblc_222_reach_back_vol_rank_lifetime_d3(volume):
    return f19_vblc_222_reach_back_vol_rank_lifetime(volume).diff().diff().diff()


def f19_vblc_223_vol_pct_rank_decay_speed_after_peak_d3(volume):
    return f19_vblc_223_vol_pct_rank_decay_speed_after_peak(volume).diff().diff().diff()


def f19_vblc_224_vol_arch1_coefficient_252d_d3(volume):
    return f19_vblc_224_vol_arch1_coefficient_252d(volume).diff().diff().diff()


def f19_vblc_225_vol_long_memory_geweke_porter_252d_d3(volume):
    return f19_vblc_225_vol_long_memory_geweke_porter_252d(volume).diff().diff().diff()


VOLUME_BLOWOFF_CLIMAX_D3_REGISTRY_151_225 = {
    "f19_vblc_151_vroc_21d_d3": {"inputs": ["volume"], "func": f19_vblc_151_vroc_21d_d3},
    "f19_vblc_152_vroc_63d_d3": {"inputs": ["volume"], "func": f19_vblc_152_vroc_63d_d3},
    "f19_vblc_153_vroc_acceleration_21d_vs_63d_d3": {"inputs": ["volume"], "func": f19_vblc_153_vroc_acceleration_21d_vs_63d_d3},
    "f19_vblc_154_ease_of_movement_arms_14d_d3": {"inputs": ["high", "low", "volume"], "func": f19_vblc_154_ease_of_movement_arms_14d_d3},
    "f19_vblc_155_ease_of_movement_zscore_63d_d3": {"inputs": ["high", "low", "volume"], "func": f19_vblc_155_ease_of_movement_zscore_63d_d3},
    "f19_vblc_156_vpt_slope_21d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_156_vpt_slope_21d_d3},
    "f19_vblc_157_vpt_close_divergence_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_157_vpt_close_divergence_63d_d3},
    "f19_vblc_158_nvi_slope_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_158_nvi_slope_63d_d3},
    "f19_vblc_159_pvi_slope_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_159_pvi_slope_63d_d3},
    "f19_vblc_160_nvi_pvi_divergence_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_160_nvi_pvi_divergence_63d_d3},
    "f19_vblc_161_twiggs_money_flow_21d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_161_twiggs_money_flow_21d_d3},
    "f19_vblc_162_demand_index_sibbet_14d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_162_demand_index_sibbet_14d_d3},
    "f19_vblc_163_tvi_slope_21d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_163_tvi_slope_21d_d3},
    "f19_vblc_164_vw_macd_signal_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_164_vw_macd_signal_63d_d3},
    "f19_vblc_165_vwap_band_upper_breach_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_165_vwap_band_upper_breach_63d_d3},
    "f19_vblc_166_bars_above_vwap_upper_band_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_166_bars_above_vwap_upper_band_63d_d3},
    "f19_vblc_167_cdv_proxy_slope_21d_d3": {"inputs": ["open", "close", "volume"], "func": f19_vblc_167_cdv_proxy_slope_21d_d3},
    "f19_vblc_168_cdv_price_bearish_divergence_63d_d3": {"inputs": ["open", "close", "volume"], "func": f19_vblc_168_cdv_price_bearish_divergence_63d_d3},
    "f19_vblc_169_cdv_drawdown_from_63d_peak_d3": {"inputs": ["open", "close", "volume"], "func": f19_vblc_169_cdv_drawdown_from_63d_peak_d3},
    "f19_vblc_170_effort_vs_result_ratio_21d_mean_d3": {"inputs": ["close", "volume"], "func": f19_vblc_170_effort_vs_result_ratio_21d_mean_d3},
    "f19_vblc_171_effort_no_result_count_21d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_171_effort_no_result_count_21d_d3},
    "f19_vblc_172_vol_of_vol_63d_d3": {"inputs": ["volume"], "func": f19_vblc_172_vol_of_vol_63d_d3},
    "f19_vblc_173_vol_of_vol_zscore_63d_in_252d_d3": {"inputs": ["volume"], "func": f19_vblc_173_vol_of_vol_zscore_63d_in_252d_d3},
    "f19_vblc_174_arch_lm_stat_log_vol_63d_d3": {"inputs": ["volume"], "func": f19_vblc_174_arch_lm_stat_log_vol_63d_d3},
    "f19_vblc_175_log_vol_hurst_exponent_252d_d3": {"inputs": ["volume"], "func": f19_vblc_175_log_vol_hurst_exponent_252d_d3},
    "f19_vblc_176_log_vol_autocorr_lag1_63d_d3": {"inputs": ["volume"], "func": f19_vblc_176_log_vol_autocorr_lag1_63d_d3},
    "f19_vblc_177_log_vol_autocorr_lag5_63d_d3": {"inputs": ["volume"], "func": f19_vblc_177_log_vol_autocorr_lag5_63d_d3},
    "f19_vblc_178_log_vol_autocorr_change_21d_vs_63d_d3": {"inputs": ["volume"], "func": f19_vblc_178_log_vol_autocorr_change_21d_vs_63d_d3},
    "f19_vblc_179_lee_mykland_vol_jump_count_63d_d3": {"inputs": ["volume"], "func": f19_vblc_179_lee_mykland_vol_jump_count_63d_d3},
    "f19_vblc_180_bns_jump_variance_share_vol_63d_d3": {"inputs": ["volume"], "func": f19_vblc_180_bns_jump_variance_share_vol_63d_d3},
    "f19_vblc_181_bipower_variation_log_vol_63d_d3": {"inputs": ["volume"], "func": f19_vblc_181_bipower_variation_log_vol_63d_d3},
    "f19_vblc_182_karpoff_vol_absret_corr_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_182_karpoff_vol_absret_corr_63d_d3},
    "f19_vblc_183_karpoff_corr_change_21d_vs_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_183_karpoff_corr_change_21d_vs_63d_d3},
    "f19_vblc_184_block_trade_signature_count_63d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_184_block_trade_signature_count_63d_d3},
    "f19_vblc_185_block_trade_signature_intensity_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_185_block_trade_signature_intensity_252d_d3},
    "f19_vblc_186_price_mom_vs_vol_trend_divergence_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_186_price_mom_vs_vol_trend_divergence_63d_d3},
    "f19_vblc_187_stalling_day_ibd_count_21d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_187_stalling_day_ibd_count_21d_d3},
    "f19_vblc_188_distribution_day_ibd_strict_count_21d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_188_distribution_day_ibd_strict_count_21d_d3},
    "f19_vblc_189_distribution_day_ibd_strict_count_25d_window_d3": {"inputs": ["close", "volume"], "func": f19_vblc_189_distribution_day_ibd_strict_count_25d_window_d3},
    "f19_vblc_190_five_distribution_days_in_25d_indicator_d3": {"inputs": ["close", "volume"], "func": f19_vblc_190_five_distribution_days_in_25d_indicator_d3},
    "f19_vblc_191_churn_day_ibd_count_21d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_191_churn_day_ibd_count_21d_d3},
    "f19_vblc_192_climax_vol_pct_rank_504d_d3": {"inputs": ["volume"], "func": f19_vblc_192_climax_vol_pct_rank_504d_d3},
    "f19_vblc_193_climax_vol_pct_rank_1260d_d3": {"inputs": ["volume"], "func": f19_vblc_193_climax_vol_pct_rank_1260d_d3},
    "f19_vblc_194_log_vol_mad_63d_d3": {"inputs": ["volume"], "func": f19_vblc_194_log_vol_mad_63d_d3},
    "f19_vblc_195_log_vol_mad_252d_d3": {"inputs": ["volume"], "func": f19_vblc_195_log_vol_mad_252d_d3},
    "f19_vblc_196_log_vol_yule_bowley_skew_63d_d3": {"inputs": ["volume"], "func": f19_vblc_196_log_vol_yule_bowley_skew_63d_d3},
    "f19_vblc_197_log_vol_yule_bowley_skew_252d_d3": {"inputs": ["volume"], "func": f19_vblc_197_log_vol_yule_bowley_skew_252d_d3},
    "f19_vblc_198_vol_pareto_tail_exponent_252d_d3": {"inputs": ["volume"], "func": f19_vblc_198_vol_pareto_tail_exponent_252d_d3},
    "f19_vblc_199_vol_pareto_tail_alpha_change_63_vs_252_d3": {"inputs": ["volume"], "func": f19_vblc_199_vol_pareto_tail_alpha_change_63_vs_252_d3},
    "f19_vblc_200_vol_herfindahl_concentration_63d_d3": {"inputs": ["volume"], "func": f19_vblc_200_vol_herfindahl_concentration_63d_d3},
    "f19_vblc_201_vol_herfindahl_concentration_252d_d3": {"inputs": ["volume"], "func": f19_vblc_201_vol_herfindahl_concentration_252d_d3},
    "f19_vblc_202_vol_herfindahl_change_63d_in_252d_d3": {"inputs": ["volume"], "func": f19_vblc_202_vol_herfindahl_change_63d_in_252d_d3},
    "f19_vblc_203_post_peak_vol_reentry_speed_63d_d3": {"inputs": ["volume"], "func": f19_vblc_203_post_peak_vol_reentry_speed_63d_d3},
    "f19_vblc_204_post_peak_oscillation_count_63d_d3": {"inputs": ["volume"], "func": f19_vblc_204_post_peak_oscillation_count_63d_d3},
    "f19_vblc_205_post_peak_decay_residual_variance_63d_d3": {"inputs": ["volume"], "func": f19_vblc_205_post_peak_decay_residual_variance_63d_d3},
    "f19_vblc_206_post_peak_decay_r2_63d_d3": {"inputs": ["volume"], "func": f19_vblc_206_post_peak_decay_r2_63d_d3},
    "f19_vblc_207_float_rotation_proxy_252d_d3": {"inputs": ["volume"], "func": f19_vblc_207_float_rotation_proxy_252d_d3},
    "f19_vblc_208_cum_excess_vol_over_252d_mean_63d_d3": {"inputs": ["volume"], "func": f19_vblc_208_cum_excess_vol_over_252d_mean_63d_d3},
    "f19_vblc_209_strict_climax_triple_criteria_count_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_209_strict_climax_triple_criteria_count_252d_d3},
    "f19_vblc_210_vsa_test_bar_after_climax_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_210_vsa_test_bar_after_climax_indicator_d3},
    "f19_vblc_211_vsa_upthrust_after_distribution_count_63d_d3": {"inputs": ["high", "close", "volume"], "func": f19_vblc_211_vsa_upthrust_after_distribution_count_63d_d3},
    "f19_vblc_212_wyckoff_buying_climax_signature_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_212_wyckoff_buying_climax_signature_indicator_d3},
    "f19_vblc_213_wyckoff_automatic_reaction_depth_after_bc_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_213_wyckoff_automatic_reaction_depth_after_bc_d3},
    "f19_vblc_214_preliminary_supply_count_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_214_preliminary_supply_count_63d_d3},
    "f19_vblc_215_volume_at_price_top_node_distance_d3": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_215_volume_at_price_top_node_distance_d3},
    "f19_vblc_216_volume_at_price_node_above_count_d3": {"inputs": ["close", "volume"], "func": f19_vblc_216_volume_at_price_node_above_count_d3},
    "f19_vblc_217_hvn_lvn_ratio_above_below_252d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_217_hvn_lvn_ratio_above_below_252d_d3},
    "f19_vblc_218_vol_entropy_diff_21d_vs_252d_d3": {"inputs": ["volume"], "func": f19_vblc_218_vol_entropy_diff_21d_vs_252d_d3},
    "f19_vblc_219_vol_entropy_diff_63d_vs_504d_d3": {"inputs": ["volume"], "func": f19_vblc_219_vol_entropy_diff_63d_vs_504d_d3},
    "f19_vblc_220_vol_kurtosis_regime_break_252d_d3": {"inputs": ["volume"], "func": f19_vblc_220_vol_kurtosis_regime_break_252d_d3},
    "f19_vblc_221_sign_vol_return_correlation_breakdown_63d_d3": {"inputs": ["close", "volume"], "func": f19_vblc_221_sign_vol_return_correlation_breakdown_63d_d3},
    "f19_vblc_222_reach_back_vol_rank_lifetime_d3": {"inputs": ["volume"], "func": f19_vblc_222_reach_back_vol_rank_lifetime_d3},
    "f19_vblc_223_vol_pct_rank_decay_speed_after_peak_d3": {"inputs": ["volume"], "func": f19_vblc_223_vol_pct_rank_decay_speed_after_peak_d3},
    "f19_vblc_224_vol_arch1_coefficient_252d_d3": {"inputs": ["volume"], "func": f19_vblc_224_vol_arch1_coefficient_252d_d3},
    "f19_vblc_225_vol_long_memory_geweke_porter_252d_d3": {"inputs": ["volume"], "func": f19_vblc_225_vol_long_memory_geweke_porter_252d_d3},
}
