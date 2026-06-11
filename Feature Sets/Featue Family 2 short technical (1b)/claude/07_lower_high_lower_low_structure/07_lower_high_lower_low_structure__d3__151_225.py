import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


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


def _pivot_high_event(high, n):
    w = 2 * n + 1
    rm = high.rolling(w, min_periods=w).max()
    return (high.shift(n) == rm) & rm.notna()


def _pivot_low_event(low, n):
    w = 2 * n + 1
    rm = low.rolling(w, min_periods=w).min()
    return (low.shift(n) == rm) & rm.notna()


def _pivot_high_value(high, n):
    return high.shift(n).where(_pivot_high_event(high, n), np.nan)


def _pivot_low_value(low, n):
    return low.shift(n).where(_pivot_low_event(low, n), np.nan)


def _ichimoku(high, low, close):
    tenkan = (high.rolling(9, min_periods=5).max() + low.rolling(9, min_periods=5).min()) / 2
    kijun = (high.rolling(26, min_periods=13).max() + low.rolling(26, min_periods=13).min()) / 2
    span_a = (tenkan + kijun) / 2
    span_b = (high.rolling(52, min_periods=26).max() + low.rolling(52, min_periods=26).min()) / 2
    return tenkan, kijun, span_a, span_b


def _heikin_ashi(open_, high, low, close):
    n = len(close)
    ha_c = ((open_ + high + low + close) / 4.0).values
    o = open_.values; cl = close.values; h = high.values; l = low.values
    ha_o = np.full(n, np.nan)
    if n > 0 and not (np.isnan(o[0]) or np.isnan(cl[0])): ha_o[0] = (o[0] + cl[0]) / 2.0
    for i in range(1, n):
        if np.isnan(ha_o[i - 1]) or np.isnan(ha_c[i - 1]):
            if not (np.isnan(o[i]) or np.isnan(cl[i])): ha_o[i] = (o[i] + cl[i]) / 2.0
        else:
            ha_o[i] = (ha_o[i - 1] + ha_c[i - 1]) / 2.0
    ha_h = np.fmax(np.fmax(h, ha_o), ha_c); ha_l = np.fmin(np.fmin(l, ha_o), ha_c)
    idx = close.index
    return pd.Series(ha_o, index=idx), pd.Series(ha_h, index=idx), pd.Series(ha_l, index=idx), pd.Series(ha_c, index=idx)


def _mcginley(close, period, k=0.6):
    c = close.values; n = len(c); md = np.full(n, np.nan)
    if n >= period:
        seed = c[:period]
        if not np.isnan(seed).any():
            md[period - 1] = float(np.mean(seed))
            for i in range(period, n):
                prev = md[i - 1]; cv = c[i]
                if np.isnan(prev) or np.isnan(cv) or prev <= 0: md[i] = prev; continue
                ratio = cv / prev
                if ratio <= 0: md[i] = prev; continue
                denom = k * float(period) * (ratio ** 4)
                md[i] = prev if denom == 0 else prev + (cv - prev) / denom
    return pd.Series(md, index=close.index)


def _curr_streak_pos(arr):
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    s = 0
    for i in range(n):
        v = arr[i]
        if np.isnan(v):
            s = 0
            out[i] = np.nan
        else:
            s = s + 1 if v > 0.5 else 0
            out[i] = float(s)
    return out


def _bsm(w):
    if np.isnan(w).all():
        return np.nan
    idx = np.where(w > 0.5)[0]
    return float(len(w)) if idx.size == 0 else float((len(w) - 1) - idx[-1])


def f07_lhll_151_wyckoff_psy_event_count_252d(high, low, close, volume):
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    up = close > close.shift(1)
    wide = tr > 1.5 * atr
    vol_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    high_vol = volume > vol_avg
    adv = _safe_log(close) - _safe_log(close.shift(100))
    advanced = adv > 0.20
    psy = (up & wide & high_vol & advanced).astype(float)
    return psy.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume):
    tr = _true_range(high, low, close)
    tr_m = tr.rolling(QDAYS, min_periods=MDAYS).mean()
    tr_sd = tr.rolling(QDAYS, min_periods=MDAYS).std()
    wide2sig = tr > (tr_m + 2.0 * tr_sd)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_252_high = high >= rmax
    vol_q9 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    high_vol = volume >= vol_q9
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    bc = (wide2sig & at_252_high & high_vol & (pos < 0.5)).astype(float)
    return bc.where(rng.notna(), np.nan)


def f07_lhll_153_bars_since_buying_climax_event_504d(high, low, close, volume):
    bc = f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).fillna(0.0)
    return bc.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_bsm, raw=True)


def f07_lhll_154_wyckoff_automatic_reaction_severity_atr(high, low, close, volume):
    bc = f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).fillna(0.0).values
    atr = _atr(high, low, close, MDAYS).values
    h = high.values; l = low.values; n = len(close)
    out = np.full(n, np.nan); last_bc = -1; last_sev = np.nan
    for i in range(n):
        if bc[i] > 0.5: last_bc = i; last_sev = 0.0
        if last_bc >= 0 and i - last_bc <= MDAYS and i > last_bc:
            sh = h[last_bc:i + 1]; sl = l[last_bc:i + 1]
            if not np.isnan(sh).all() and not np.isnan(sl).all():
                rm = np.fmax.accumulate(np.where(np.isnan(sh), -np.inf, sh))
                w = float(np.nanmax(rm - sl)); a = atr[i]
                if not np.isnan(a) and a > 0: last_sev = float(w / a)
        out[i] = last_sev
    return pd.Series(out, index=close.index)


def f07_lhll_155_wyckoff_secondary_test_failed_indicator(high, low, close, volume):
    bc = f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).fillna(0.0).values
    h = high.values; v = volume.values; n = len(close)
    out = np.zeros(n); last_bc = -1; bh = np.nan; bv = np.nan
    for i in range(n):
        if bc[i] > 0.5: last_bc = i; bh = h[i]; bv = v[i]
        if last_bc >= 0 and 5 <= (i - last_bc) <= 60:
            if not (np.isnan(h[i]) or np.isnan(v[i]) or np.isnan(bh) or np.isnan(bv)):
                if (h[i] < bh) and (h[i] >= 0.97 * bh) and (v[i] < 0.8 * bv):
                    out[i:min(n, i + MDAYS + 1)] = 1.0
    return pd.Series(out, index=close.index).where(close.notna(), np.nan)


def f07_lhll_156_wyckoff_utad_event_count_504d(high, low, close, volume):
    tr_hi = high.rolling(QDAYS, min_periods=MDAYS).max().shift(1)
    utad = ((high > tr_hi) & (close < tr_hi)).astype(float)
    return utad.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_157_wyckoff_sow_event_indicator(high, low, close, volume):
    tr_lo = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    atr = _atr(high, low, close, MDAYS)
    tr = _true_range(high, low, close)
    vol_q75 = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    sow_evt = ((close < tr_lo) & (tr > 1.5 * atr) & (volume >= vol_q75)).astype(float)
    prev = sow_evt.shift(1).fillna(0)
    first = ((sow_evt > 0.5) & (prev < 0.5)).astype(float)
    return first.where(close.notna(), np.nan)


def f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d(high, low, close, volume):
    sow = f07_lhll_157_wyckoff_sow_event_indicator(high, low, close, volume).fillna(0.0).values
    pvh = _pivot_high_value(high, 10).ffill().values
    h = high.values; v = volume.values; n = len(close)
    fl = np.zeros(n); last_sow = -1
    for i in range(n):
        if sow[i] > 0.5: last_sow = i
        if last_sow >= 0 and i > last_sow + 3:
            sh = h[max(0, i - 4):i + 1]
            if not np.isnan(sh).all() and h[i] == np.nanmax(sh):
                ph = pvh[i]
                if not np.isnan(ph) and h[i] < ph and i >= 10:
                    a = v[i - 9:i - 4]; b = v[i - 4:i + 1]
                    if not (np.isnan(a).any() or np.isnan(b).any()) and b.mean() < a.mean():
                        fl[i] = 1.0
    return pd.Series(fl, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_159_wyckoff_phase_state_score_pivot10(high, low, close, volume):
    bc = f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    ar_sev = f07_lhll_154_wyckoff_automatic_reaction_severity_atr(high, low, close, volume)
    ar = ((ar_sev.notna()) & (ar_sev > 1.0)).astype(float)
    utad = f07_lhll_156_wyckoff_utad_event_count_504d(high, low, close, volume)
    sow = f07_lhll_157_wyckoff_sow_event_indicator(high, low, close, volume).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    lpsy = f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d(high, low, close, volume)
    score = ((bc > 0).astype(float) + ar - (utad > 0).astype(float)
             - 2.0 * (sow > 0).astype(float) - (lpsy > 0).astype(float))
    return score.clip(-3, 3).where(close.notna(), np.nan)


def f07_lhll_160_vsa_no_demand_bar_count_at_pivot_high_252d(high, low, close, volume):
    tr = _true_range(high, low, close)
    tr_m = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    narrow = tr < 0.7 * tr_m
    up = close > close.shift(1)
    vol_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    low_vol = volume < vol_avg
    nd = (narrow & up & low_vol).astype(float)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(11, min_periods=1).sum() > 0
    return (nd.where(near, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_161_vsa_upthrust_event_count_252d(high, low, close, volume):
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    wide = tr > 1.5 * atr
    new_hi = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    vol_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    ut = (wide & new_hi & (pos < (1.0 / 3.0)) & (volume > 1.5 * vol_avg)).astype(float)
    return ut.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_162_vsa_stopping_volume_event_indicator(high, low, close, volume):
    up = close > close.shift(1)
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    vol_q9 = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    sv = (up & (pos < 0.5) & (volume >= vol_q9)).astype(float)
    return sv.where(rng.notna(), np.nan)


def f07_lhll_163_hh_with_declining_volume_count_pivot10_252d(high, volume):
    pv = _pivot_high_value(high, 10)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    vol_at_pv = vol5.where(pv.notna(), np.nan)
    prev_pv = pv.shift(1).ffill()
    prev_vol = vol_at_pv.ffill().shift(1)
    hh = ((pv.notna()) & (prev_pv.notna()) & (pv > prev_pv))
    hh_dec = (hh & (vol_at_pv < prev_vol)).astype(float)
    return hh_dec.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_164_ll_with_rising_volume_count_pivot10_252d(low, volume):
    pv = _pivot_low_value(low, 10)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    vol_at_pv = vol5.where(pv.notna(), np.nan)
    prev_pv = pv.shift(1).ffill()
    prev_vol = vol_at_pv.ffill().shift(1)
    ll = ((pv.notna()) & (prev_pv.notna()) & (pv < prev_pv))
    ll_rise = (ll & (vol_at_pv > prev_vol)).astype(float)
    return ll_rise.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_165_pivot_high_volume_decay_slope_pivot10_252d(high, volume):
    pv = _pivot_high_value(high, 10)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    vol_at_pv = vol5.where(pv.notna(), np.nan).ffill()
    return _rolling_slope(vol_at_pv, YDAYS)


def f07_lhll_166_pivot_high_to_low_volume_ratio_252d(high, low, volume):
    pvh = _pivot_high_value(high, 10).notna().astype(float)
    pvl = _pivot_low_value(low, 10).notna().astype(float)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    v_at_h = vol5.where(pvh > 0.5, np.nan)
    v_at_l = vol5.where(pvl > 0.5, np.nan)
    num = v_at_h.rolling(YDAYS, min_periods=QDAYS).mean()
    den = v_at_l.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(num, den)


def f07_lhll_167_wide_range_bar_at_pivot_high_count_252d(high, low, close):
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    wrb = (tr > 2.0 * atr).astype(float)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(5, min_periods=1).sum() > 0
    return wrb.where(near, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_168_narrow_range_bar_at_pivot_high_count_252d(high, low):
    rng = (high - low)
    nr4 = (rng == rng.rolling(4, min_periods=4).min())
    nr7 = (rng == rng.rolling(7, min_periods=7).min())
    nr = (nr4 | nr7).astype(float)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(5, min_periods=1).sum() > 0
    return nr.where(near, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_169_nr7_to_wrb_transition_count_252d(high, low, close):
    rng = (high - low)
    nr7 = (rng == rng.rolling(7, min_periods=7).min()).astype(float)
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    wrb_down = ((tr > 2.0 * atr) & (close < close.shift(1))).astype(float)
    nr7_recent = nr7.rolling(6, min_periods=1).sum().shift(1) > 0
    evt = (wrb_down.astype(bool) & nr7_recent).astype(float)
    return evt.rolling(YDAYS, min_periods=QDAYS).sum()


def _renko_pct_state(close, pct):
    c = close.values; n = len(c)
    color = np.full(n, np.nan); streak = np.full(n, np.nan); flips = np.zeros(n)
    lvl = np.nan; col = 0; st = 0; lst_st = np.nan; lst_c = np.nan
    log1p = np.log(1.0 + pct)
    for i in range(n):
        cv = c[i]
        if np.isnan(cv) or cv <= 0:
            color[i] = lst_c; streak[i] = lst_st; continue
        if np.isnan(lvl):
            lvl = cv; color[i] = lst_c; streak[i] = lst_st; continue
        moved = False
        if cv >= lvl * (1.0 + pct):
            b = int(np.floor(np.log(cv / lvl) / log1p))
            if b >= 1:
                if col == 1: st += b
                else:
                    st = b
                    if col == -1: flips[i] = 1.0
                col = 1; lvl *= (1.0 + pct) ** b; moved = True
        elif cv <= lvl * (1.0 - pct):
            b = int(np.floor(np.log(lvl / cv) / log1p))
            if b >= 1:
                if col == -1: st += b
                else:
                    st = b
                    if col == 1: flips[i] = 1.0
                col = -1; lvl *= (1.0 - pct) ** b; moved = True
        if moved:
            lst_c = float(col); lst_st = float(st)
        color[i] = lst_c; streak[i] = lst_st
    return color, streak, flips


def _renko_atr_flips(high, low, close):
    c = close.values; atr = _atr(high, low, close, MDAYS).values; n = len(c)
    flips = np.zeros(n); lvl = np.nan; col = 0
    for i in range(n):
        cv = c[i]; a = atr[i]
        if np.isnan(cv) or np.isnan(a) or a <= 0: continue
        if np.isnan(lvl): lvl = cv; continue
        if cv >= lvl + a:
            b = int((cv - lvl) // a)
            if b >= 1:
                if col == -1: flips[i] = 1.0
                col = 1; lvl += b * a
        elif cv <= lvl - a:
            b = int((lvl - cv) // a)
            if b >= 1:
                if col == 1: flips[i] = 1.0
                col = -1; lvl -= b * a
    return flips


def f07_lhll_170_renko_1pct_consecutive_red_brick_count(close):
    color, streak, _ = _renko_pct_state(close, 0.01)
    out = np.where(color == -1, streak, 0.0)
    out = np.where(np.isnan(color), np.nan, out)
    return pd.Series(out, index=close.index)


def f07_lhll_171_renko_atr_brick_color_flip_count_252d(high, low, close):
    flips = _renko_atr_flips(high, low, close)
    return pd.Series(flips, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_172_renko_1pct_brick_red_to_green_streak_252d(close):
    color, streak, _ = _renko_pct_state(close, 0.01)
    rs = np.where(color == -1, streak, 0.0)
    rs = np.where(np.isnan(color), np.nan, rs)
    return pd.Series(rs, index=close.index).rolling(YDAYS, min_periods=QDAYS).max()


def f07_lhll_173_renko_2pct_first_red_brick_after_long_green_indicator(close):
    color, streak, _ = _renko_pct_state(close, 0.02)
    n = len(close)
    out = np.zeros(n, dtype=float)
    prev_green = 0
    prev_color = np.nan
    for i in range(n):
        ci = color[i]
        si = streak[i] if not np.isnan(streak[i]) else 0.0
        if not np.isnan(ci) and not np.isnan(prev_color):
            if prev_color == 1 and ci == -1 and prev_green >= 8:
                out[i] = 1.0
        if not np.isnan(ci):
            prev_green = int(si) if ci == 1 else 0
            prev_color = ci
    return pd.Series(out, index=close.index).where(close.notna(), np.nan)


def _pnf_atr_state(high, low, close, reversal=3):
    c = close.values; atr = _atr(high, low, close, MDAYS).values; n = len(c)
    cc = np.full(n, np.nan); cl = np.full(n, np.nan); flips = np.zeros(n); cb = np.full(n, np.nan)
    col = 0; ln = 0; top = np.nan; bot = np.nan; box = np.nan; init = False
    for i in range(n):
        cv = c[i]; a = atr[i]
        if np.isnan(cv) or np.isnan(a) or a <= 0:
            cc[i] = col if init else np.nan
            cl[i] = float(ln) if init else np.nan
            cb[i] = bot; continue
        if not init:
            box = a; top = cv; bot = cv; init = True
        if col == 0:
            if cv >= bot + box:
                col = 1; ln = int((cv - bot) / box); top = bot + ln * box
            elif cv <= top - box:
                col = -1; ln = int((top - cv) / box); bot = top - ln * box
        elif col == 1:
            if cv >= top + box:
                add = int((cv - top) / box); ln += add; top = top + add * box
            elif cv <= top - reversal * box:
                flips[i] = 1.0; col = -1
                ln = max(int((top - box - cv) / box) + 1, reversal)
                bot = (top - box) - (ln - 1) * box; top = top - box
        else:
            if cv <= bot - box:
                add = int((bot - cv) / box); ln += add; bot = bot - add * box
            elif cv >= bot + reversal * box:
                flips[i] = 1.0; col = 1
                ln = max(int((cv - (bot + box)) / box) + 1, reversal)
                top = bot + box + (ln - 1) * box; bot = bot + box
        cc[i] = float(col); cl[i] = float(ln); cb[i] = bot
    return cc, cl, flips, cb


def f07_lhll_174_pf_3box_column_reversal_count_atr_box_252d(high, low, close):
    _, _, flips, _ = _pnf_atr_state(high, low, close)
    return pd.Series(flips, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_175_pf_consecutive_o_column_length_atr_box(high, low, close):
    col, ln, _, _ = _pnf_atr_state(high, low, close)
    out = np.where(col == -1, ln, 0.0)
    out = np.where(np.isnan(col), np.nan, out)
    return pd.Series(out, index=close.index)


def f07_lhll_176_pf_x_to_o_transitions_after_alltime_high_504d(high, low, close):
    col, _, flips, _ = _pnf_atr_state(high, low, close)
    xo = ((col == -1) & (flips > 0.5)).astype(float)
    arr_h = high.values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf; cur_max_idx = -1
    cum_xo_at_max = 0.0; cum_xo = 0.0
    for i in range(n):
        cum_xo += xo[i]
        v = arr_h[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v; cur_max_idx = i
                cum_xo_at_max = cum_xo
            if cur_max_idx >= 0:
                out[i] = min(cum_xo - cum_xo_at_max, float(DDAYS_2Y))
    return pd.Series(out, index=close.index)


def f07_lhll_177_pf_double_bottom_breakdown_event_indicator(high, low, close):
    col, _, _, bot = _pnf_atr_state(high, low, close)
    n = len(close)
    out = np.zeros(n, dtype=float)
    last_o_bot = np.nan
    cur_color_prev = np.nan
    cur_o_bot = np.nan
    for i in range(n):
        ci = col[i]; bi = bot[i]
        if np.isnan(ci):
            continue
        if ci == -1:
            cur_o_bot = bi
            if not np.isnan(last_o_bot) and bi < last_o_bot - 1e-12:
                out[i] = 1.0
        else:
            if cur_color_prev == -1 and not np.isnan(cur_o_bot):
                last_o_bot = cur_o_bot
                cur_o_bot = np.nan
        cur_color_prev = ci
    return pd.Series(out, index=close.index).where(close.notna(), np.nan)


def f07_lhll_178_ha_red_bar_count_after_8_green_streak_252d(open_, high, low, close):
    ha_o, _, _, ha_c = _heikin_ashi(open_, high, low, close)
    is_green = (ha_c > ha_o).astype(float)
    is_red = (ha_c < ha_o).astype(float)
    gr = is_green.values
    n = len(close)
    g_streak = np.zeros(n, dtype=float)
    s = 0
    for i in range(n):
        s = s + 1 if gr[i] > 0.5 else 0
        g_streak[i] = float(s)
    streak_evt = (pd.Series(g_streak, index=close.index) >= 8).astype(float)
    near = streak_evt.rolling(MDAYS, min_periods=1).sum() > 0
    return is_red.where(near, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_179_ha_first_red_no_upper_shadow_after_green_streak_indicator(open_, high, low, close):
    ha_o, ha_h, _, ha_c = _heikin_ashi(open_, high, low, close)
    is_green = (ha_c > ha_o)
    is_red = (ha_c < ha_o)
    upper_body = pd.concat([ha_o, ha_c], axis=1).max(axis=1)
    no_upper = (ha_h - upper_body).abs() < 1e-9
    n = len(close)
    out = np.zeros(n, dtype=float)
    gr = is_green.values
    s = 0; prev_streak = 0
    for i in range(n):
        if is_red.iloc[i] and no_upper.iloc[i] and prev_streak >= 6:
            out[i] = 1.0
        s = s + 1 if gr[i] else 0
        prev_streak = s
    return pd.Series(out, index=close.index).where(close.notna(), np.nan)


def f07_lhll_180_ha_green_to_red_state_flip_count_252d(open_, high, low, close):
    ha_o, _, _, ha_c = _heikin_ashi(open_, high, low, close)
    sign = np.sign((ha_c - ha_o).values)
    n = len(close)
    flips = np.zeros(n, dtype=float)
    prev = 0
    for i in range(n):
        s = sign[i]
        if s != 0 and prev != 0 and s != prev:
            flips[i] = 1.0
        if s != 0:
            prev = int(s)
    return pd.Series(flips, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_181_ha_consecutive_red_streak_current(open_, high, low, close):
    ha_o, _, _, ha_c = _heikin_ashi(open_, high, low, close)
    is_red = (ha_c < ha_o).astype(float).values
    return pd.Series(_curr_streak_pos(is_red), index=close.index)


def _atr_trail_states(high, low, close, mult):
    atr = _atr(high, low, close, MDAYS)
    hh22 = high.rolling(22, min_periods=10).max()
    ll22 = low.rolling(22, min_periods=10).min()
    long_stop = hh22 - mult * atr
    short_stop = ll22 + mult * atr
    c = close.values
    ls = long_stop.values; ss = short_stop.values
    n = len(close)
    state = np.full(n, np.nan, dtype=float)
    flips_down = np.zeros(n, dtype=float)
    cur = 0
    for i in range(n):
        if np.isnan(c[i]) or np.isnan(ls[i]) or np.isnan(ss[i]):
            state[i] = float(cur) if cur != 0 else np.nan
            continue
        new = cur
        if cur >= 0 and c[i] < ls[i]:
            new = -1
        elif cur <= 0 and c[i] > ss[i]:
            new = 1
        elif cur == 0:
            new = 1 if c[i] > (ls[i] + ss[i]) / 2 else -1
        if new == -1 and cur == 1:
            flips_down[i] = 1.0
        cur = new
        state[i] = float(cur)
    return state, flips_down


def f07_lhll_182_atr_trail_1x_flip_down_event_count_252d(high, low, close):
    _, fd = _atr_trail_states(high, low, close, 1.0)
    return pd.Series(fd, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_183_atr_trail_3x_flip_down_event_count_504d(high, low, close):
    _, fd = _atr_trail_states(high, low, close, 3.0)
    return pd.Series(fd, index=close.index).rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(close.notna(), np.nan)


def f07_lhll_184_bars_since_atr_trail_2x_flip_down(high, low, close):
    _, fd = _atr_trail_states(high, low, close, 2.0)
    return pd.Series(fd, index=close.index).rolling(DDAYS_2Y, min_periods=QDAYS).apply(_bsm, raw=True)


def f07_lhll_185_atr_trail_multi_horizon_agreement_score(high, low, close):
    s1, _ = _atr_trail_states(high, low, close, 1.0)
    s2, _ = _atr_trail_states(high, low, close, 2.0)
    s3, _ = _atr_trail_states(high, low, close, 3.0)
    return pd.Series(s1 + s2 + s3, index=close.index).where(close.notna(), np.nan)


def f07_lhll_186_ichimoku_tenkan_below_kijun_streak(high, low, close):
    t, k, _, _ = _ichimoku(high, low, close)
    mask = (t < k).astype(float).where(t.notna() & k.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_187_ichimoku_price_below_kijun_streak(high, low, close):
    _, k, _, _ = _ichimoku(high, low, close)
    mask = (close < k).astype(float).where(k.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_188_ichimoku_cloud_color_flip_to_bearish_indicator(high, low, close):
    _, _, sa, sb = _ichimoku(high, low, close)
    bear = (sa < sb)
    bear_prev = bear.shift(1)
    evt = ((bear) & (~bear_prev.fillna(False))).astype(float)
    return evt.where(sa.notna() & sb.notna() & sa.shift(1).notna() & sb.shift(1).notna(), np.nan)


def f07_lhll_189_ichimoku_chikou_below_price_streak_252d(close):
    cb = (close < close.shift(26)).astype(float).where(close.shift(26).notna(), np.nan)
    return cb.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_190_ichimoku_kijun_slope_negative_streak(high, low, close):
    _, k, _, _ = _ichimoku(high, low, close)
    sl = k.diff()
    mask = (sl <= 0).astype(float).where(sl.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_191_diamond_top_range_expand_then_contract_indicator(high, low):
    rng21 = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    sl_early = _rolling_slope(rng21.shift(MDAYS), MDAYS)
    sl_late = _rolling_slope(rng21, MDAYS)
    expand_then_contract = (sl_early > 0) & (sl_late < 0)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(MDAYS, min_periods=1).sum() > 0
    return (expand_then_contract & near).astype(float).where(rng21.notna(), np.nan)


def f07_lhll_192_broadening_top_megaphone_indicator_252d(high, low):
    pvh = _pivot_high_value(high, 10).ffill()
    pvh_1 = pvh.shift(1).ffill()
    pvh_2 = pvh.shift(2).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    pvl_1 = pvl.shift(1).ffill()
    pvl_2 = pvl.shift(2).ffill()
    cond = (pvh_2 < pvh_1) & (pvh_1 < pvh) & (pvl_2 > pvl_1) & (pvl_1 > pvl)
    return cond.astype(float).where(pvh.notna() & pvl.notna(), np.nan)


def f07_lhll_193_rectangle_distribution_breakdown_indicator(high, low, close):
    rmax40 = high.rolling(40, min_periods=MDAYS).max()
    rmin40 = low.rolling(40, min_periods=MDAYS).min()
    width = (rmax40 - rmin40) / rmax40
    tight = (width <= 0.06)
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (rmax40 >= 0.97 * rmax252)
    base_ok = tight & near_top
    base_prev = base_ok.shift(1).fillna(False)
    breakdown = (close < rmin40.shift(1))
    evt = (base_prev & breakdown).astype(float)
    return evt.where(rmax40.notna() & rmin40.notna(), np.nan)


def f07_lhll_194_truncated_swing_coil_at_top_indicator(high, low):
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    no_new_hh = (high <= rmax21)
    no_new_ll = (low >= rmin21)
    both = (no_new_hh & no_new_ll).astype(float)
    five = both.rolling(WDAYS, min_periods=WDAYS).sum() >= WDAYS
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax252
    return (five & near).astype(float).where(rmax252.notna(), np.nan)


def f07_lhll_195_stair_step_decline_5pivot_indicator(high, low):
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    n = len(high)
    tag = np.zeros(n, dtype=int)
    val = np.full(n, np.nan, dtype=float)
    h_arr = pvh.values; l_arr = pvl.values
    for i in range(n):
        if not np.isnan(h_arr[i]):
            tag[i] = 1; val[i] = h_arr[i]
        elif not np.isnan(l_arr[i]):
            tag[i] = -1; val[i] = l_arr[i]
    out = np.zeros(n, dtype=float)
    pivots = []
    for i in range(n):
        if tag[i] != 0:
            pivots.append((tag[i], val[i]))
            if len(pivots) >= 5:
                last5 = pivots[-5:]
                tags = [p[0] for p in last5]
                vals = [p[1] for p in last5]
                if tags == [1, -1, 1, -1, 1]:
                    if vals[0] > vals[2] > vals[4] and vals[1] > vals[3]:
                        out[i] = 1.0
        if i > 0 and tag[i] == 0:
            out[i] = out[i - 1]
    return pd.Series(out, index=high.index).where(high.notna(), np.nan)


def f07_lhll_196_dwell_time_above_minus_below_pivot10_high_252d(high):
    pv = _pivot_high_value(high, 10).ffill()
    above = (high > pv).astype(float)
    below = (high < pv).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).sum()
            - below.rolling(YDAYS, min_periods=QDAYS).sum())


def f07_lhll_197_dwell_time_above_minus_below_pivot10_low_252d(low, high):
    pv = _pivot_low_value(low, 10).ffill()
    above = (low > pv).astype(float)
    below = (low < pv).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).sum()
            - below.rolling(YDAYS, min_periods=QDAYS).sum())


def f07_lhll_198_close_below_pivot21_low_fraction_252d(low, close):
    pv = _pivot_low_value(low, 21).ffill()
    below = (close < pv).astype(float).where(pv.notna(), np.nan)
    return below.rolling(YDAYS, min_periods=QDAYS).mean()


def f07_lhll_199_rolling_cusum_break_on_returns_504d(close):
    r = _safe_log(close).diff()
    def _cusum(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        cs = np.cumsum(v - mu) / sd
        return float(np.max(np.abs(cs)))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cusum, raw=True)


def f07_lhll_200_rolling_chow_ftest_slope_change_63v252(close):
    y_all = _safe_log(close)
    n_total = YDAYS; n2 = QDAYS; n1 = n_total - n2
    def _chow(w):
        v = w[~np.isnan(w)]
        if v.size < n_total:
            return np.nan
        x = np.arange(n_total, dtype=float)
        xm = x.mean(); ym = w.mean()
        denom_p = ((x - xm) ** 2).sum()
        if denom_p == 0:
            return np.nan
        bp = ((x - xm) * (w - ym)).sum() / denom_p
        ap = ym - bp * xm
        rss_p = float(((w - (ap + bp * x)) ** 2).sum())
        x1 = x[:n1]; w1 = w[:n1]; x2 = x[n1:]; w2 = w[n1:]
        denom1 = ((x1 - x1.mean()) ** 2).sum()
        denom2 = ((x2 - x2.mean()) ** 2).sum()
        if denom1 == 0 or denom2 == 0:
            return np.nan
        b1 = ((x1 - x1.mean()) * (w1 - w1.mean())).sum() / denom1
        a1 = w1.mean() - b1 * x1.mean()
        b2 = ((x2 - x2.mean()) * (w2 - w2.mean())).sum() / denom2
        a2 = w2.mean() - b2 * x2.mean()
        rss_u = float(((w1 - (a1 + b1 * x1)) ** 2).sum() + ((w2 - (a2 + b2 * x2)) ** 2).sum())
        if rss_u <= 0:
            return np.nan
        k = 2
        return float(((rss_p - rss_u) / k) / (rss_u / (n_total - 2 * k)))
    return y_all.rolling(n_total, min_periods=n_total).apply(_chow, raw=True)


def f07_lhll_201_variance_ratio_at_recent_pivot10_high(close, high):
    r = _safe_log(close).diff()
    def _vr(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        var1 = float(np.var(v[-20:], ddof=1))
        sums5 = np.array([v[i:i + 5].sum() for i in range(0, 16)], dtype=float)
        if sums5.size < 4:
            return np.nan
        var5 = float(np.var(sums5, ddof=1))
        if var1 == 0:
            return np.nan
        return var5 / (5.0 * var1)
    vr = r.rolling(MDAYS, min_periods=MDAYS).apply(_vr, raw=True)
    pv_evt = _pivot_high_event(high, 10)
    return vr.where(pv_evt, np.nan).ffill()


def f07_lhll_202_hurst_exponent_change_63d_vs_252d(close):
    r = _safe_log(close).diff()
    def _hurst(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        y = np.cumsum(v - mu)
        R = float(y.max() - y.min())
        S = float(v.std(ddof=1))
        if S == 0 or R <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(v.size))
    h63 = r.rolling(QDAYS, min_periods=MDAYS).apply(_hurst, raw=True)
    h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(_hurst, raw=True)
    return h63 - h252


def f07_lhll_203_fractal_dimension_higuchi_252d_change(close):
    y = _safe_log(close)
    def _higuchi(w, kmax=6):
        v = w[~np.isnan(w)]
        N = v.size
        if N < 40:
            return np.nan
        L_k = []
        for k in range(1, kmax + 1):
            Lm_list = []
            for m in range(k):
                count = (N - m - 1) // k
                if count < 1:
                    continue
                idxs = m + np.arange(count + 1) * k
                if idxs[-1] >= N:
                    idxs = idxs[:-1]
                if idxs.size < 2:
                    continue
                seg = v[idxs]
                Lm = np.sum(np.abs(np.diff(seg))) * (N - 1) / (count * k)
                Lm_list.append(Lm)
            if not Lm_list:
                continue
            L_k.append((k, np.mean(Lm_list)))
        if len(L_k) < 3:
            return np.nan
        xs = np.log(np.array([1.0 / x[0] for x in L_k]))
        ys = np.log(np.array([x[1] for x in L_k]))
        return float(np.polyfit(xs, ys, 1)[0])
    fd252 = y.rolling(YDAYS, min_periods=QDAYS).apply(_higuchi, raw=True)
    fd504 = y.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_higuchi, raw=True)
    return fd252 - fd504


def _seq3_pivot_vol(pv, vol5, up):
    pa = pv.values; va = vol5.where(pv.notna(), np.nan).values
    n = len(pv); out = np.zeros(n); seq = []; last = 0.0
    for i in range(n):
        if not np.isnan(pa[i]):
            seq.append((pa[i], va[i]))
            if len(seq) >= 3:
                p = seq[-3:]
                if up:
                    cond = (p[0][0] < p[1][0] < p[2][0] and p[0][1] > p[1][1] > p[2][1])
                else:
                    cond = (p[0][0] > p[1][0] > p[2][0] and p[0][1] < p[1][1] < p[2][1])
                last = 1.0 if (cond and not np.isnan(p[0][1]) and not np.isnan(p[2][1])) else 0.0
        out[i] = last
    return out


def f07_lhll_204_sequential_hh_volume_decay_3in_a_row_indicator(high, volume):
    pv = _pivot_high_value(high, 10)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    return pd.Series(_seq3_pivot_vol(pv, vol5, True), index=high.index).where(high.notna(), np.nan)


def f07_lhll_205_sequential_ll_volume_rising_3in_a_row_indicator(low, volume):
    pv = _pivot_low_value(low, 10)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean()
    return pd.Series(_seq3_pivot_vol(pv, vol5, False), index=low.index).where(low.notna(), np.nan)


def f07_lhll_206_nested_swing_small_inside_big_degradation_score(high, low):
    h21v = _pivot_high_value(high, 21).values
    l21v = _pivot_low_value(low, 21).values
    h5v = _pivot_high_value(high, 5).values
    n = len(high); out = np.full(n, np.nan); lh = -1; ll = -1; cnt = 0; ph = np.nan
    for i in range(n):
        if not np.isnan(h21v[i]): lh = i; ll = -1; cnt = 0; ph = np.nan
        if not np.isnan(l21v[i]) and lh >= 0 and i > lh: ll = i
        if not np.isnan(h5v[i]) and lh >= 0 and (ll < 0 or i <= ll):
            if not np.isnan(ph) and h5v[i] < ph: cnt += 1
            ph = h5v[i]
        if lh >= 0: out[i] = float(cnt)
    return pd.Series(out, index=high.index)


def f07_lhll_207_multi_resolution_swing_disagreement_5_10_21(high, low):
    def _dir(pvh, pvl):
        n = len(pvh)
        d = np.full(n, np.nan, dtype=float)
        last = 0
        for i in range(n):
            if not np.isnan(pvh.iloc[i]):
                last = 1
            elif not np.isnan(pvl.iloc[i]):
                last = -1
            d[i] = float(last) if last != 0 else np.nan
        return pd.Series(d, index=pvh.index)
    d5 = _dir(_pivot_high_value(high, 5), _pivot_low_value(low, 5))
    d10 = _dir(_pivot_high_value(high, 10), _pivot_low_value(low, 10))
    d21 = _dir(_pivot_high_value(high, 21), _pivot_low_value(low, 21))
    disagree = ((d5 != d10) & (d10 != d21) & (d5 != d21)).astype(float)
    return disagree.rolling(QDAYS, min_periods=MDAYS).sum()


def _dmi_adx(high, low, close, n=14):
    up = high.diff()
    dn = -low.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    tr = _true_range(high, low, close)
    atr_n = tr.rolling(n, min_periods=n).mean()
    pdm_n = pd.Series(plus_dm, index=high.index).rolling(n, min_periods=n).mean()
    mdm_n = pd.Series(minus_dm, index=high.index).rolling(n, min_periods=n).mean()
    plus_di = 100.0 * _safe_div(pdm_n, atr_n)
    minus_di = 100.0 * _safe_div(mdm_n, atr_n)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), (plus_di + minus_di))
    adx = dx.rolling(n, min_periods=n).mean()
    return plus_di, minus_di, adx


def f07_lhll_208_dmi_minus_di_above_plus_di_streak(high, low, close):
    p, m, _ = _dmi_adx(high, low, close, 14)
    mask = (m > p).astype(float).where(p.notna() & m.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_209_dmi_adx_rising_with_minus_di_dominant_streak(high, low, close):
    p, m, adx = _dmi_adx(high, low, close, 14)
    rising = (adx.diff() > 0)
    bear = (m > p)
    mask = (rising & bear).astype(float).where(adx.notna() & p.notna() & m.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_210_dominant_cycle_period_shift_ehlers_proxy(close):
    r = _safe_log(close).diff()
    def _dom(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        denom = float(np.dot(v, v))
        if denom == 0:
            return np.nan
        best_lag = np.nan; best_ac = -np.inf
        max_lag = min(60, v.size // 2)
        for lag in range(5, max_lag + 1):
            ac = float(np.dot(v[:-lag], v[lag:])) / denom
            if ac > best_ac:
                best_ac = ac
                best_lag = lag
        return float(best_lag)
    d63 = r.rolling(QDAYS, min_periods=QDAYS).apply(_dom, raw=True)
    d252 = r.rolling(YDAYS, min_periods=YDAYS).apply(_dom, raw=True)
    return d63 - d252


def f07_lhll_211_range_of_range_percentile_63d_in_252d(high, low):
    med = (high + low) / 2.0
    rng = (high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min())
    metric = _safe_div(rng, med.rolling(QDAYS, min_periods=MDAYS).median())
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
    return metric.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f07_lhll_212_range_contraction_then_expansion_at_top_indicator(high, low, close):
    rng63 = (high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min())
    q25 = rng63.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    contracted = (rng63 < q25)
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    expanding = (tr > 1.5 * atr) & (close < close.shift(1))
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (high >= 0.95 * rmax252)
    return (contracted & expanding & near_top).astype(float).where(rmax252.notna(), np.nan)


def f07_lhll_213_first_lower_low_after_alltime_high_indicator(high, low):
    pvl = _pivot_low_value(low, 10)
    pvl_prev = pvl.shift(1).ffill()
    is_ll = ((pvl < pvl_prev) & pvl.notna() & pvl_prev.notna()).values
    rmax = high.expanding(min_periods=QDAYS).max()
    new_ath = (high >= rmax).values
    n = len(high)
    out = np.zeros(n, dtype=float)
    state_seen = False
    for i in range(n):
        if new_ath[i]:
            state_seen = False
        if is_ll[i] and not state_seen:
            out[i] = 1.0
            state_seen = True
        elif state_seen:
            out[i] = 1.0
    return pd.Series(out, index=high.index).where(high.notna(), np.nan)


def f07_lhll_214_bars_between_alltime_high_and_first_dow_breakdown(high, low):
    pvl = _pivot_low_value(low, 10)
    pvl_prev = pvl.shift(1).ffill()
    is_ll = ((pvl < pvl_prev) & pvl.notna() & pvl_prev.notna()).values
    rmax = high.expanding(min_periods=QDAYS).max().values
    h = high.values
    n = len(high)
    out = np.full(n, np.nan, dtype=float)
    last_ath_idx = -1
    last_gap = np.nan
    for i in range(n):
        if not np.isnan(h[i]) and not np.isnan(rmax[i]) and h[i] >= rmax[i]:
            last_ath_idx = i
            last_gap = np.nan
        if is_ll[i] and last_ath_idx >= 0 and np.isnan(last_gap):
            last_gap = float(i - last_ath_idx)
        out[i] = last_gap
    return pd.Series(out, index=high.index)


def f07_lhll_215_pivot10_swing_return_skewness_252d(high, low, close):
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    any_pv = pvh.where(pvh.notna(), pvl)
    pv_filled = any_pv.dropna()
    if pv_filled.empty:
        return pd.Series(np.nan, index=close.index)
    log_pv = np.log(pv_filled.replace(0, np.nan))
    swing_ret = log_pv.diff()
    sr_full = swing_ret.reindex(close.index, method=None).ffill()
    return sr_full.rolling(YDAYS, min_periods=QDAYS).skew()


def f07_lhll_216_pivot10_swing_return_kurtosis_252d(high, low, close):
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    any_pv = pvh.where(pvh.notna(), pvl)
    pv_filled = any_pv.dropna()
    if pv_filled.empty:
        return pd.Series(np.nan, index=close.index)
    log_pv = np.log(pv_filled.replace(0, np.nan))
    swing_ret = log_pv.diff()
    sr_full = swing_ret.reindex(close.index, method=None).ffill()
    return sr_full.rolling(YDAYS, min_periods=QDAYS).kurt()


def f07_lhll_217_mcginley_dynamic_below_close_streak(close):
    md = _mcginley(close, 14, k=0.6)
    mask = (md < close).astype(float).where(md.notna() & close.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_218_mcginley_slope_negative_streak(close):
    md = _mcginley(close, 60, k=0.6)
    sl = md.diff()
    mask = (sl <= 0).astype(float).where(sl.notna(), np.nan).values
    return pd.Series(_curr_streak_pos(mask), index=close.index)


def f07_lhll_219_vsa_eight_signal_state_composite_at_pivot10_high(high, low, close, volume):
    tr = _true_range(high, low, close)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    up = close > close.shift(1)
    down = close < close.shift(1)
    wide = tr > 1.5 * atr
    narrow = tr < 0.7 * atr
    high_vol = volume > 1.5 * vol_avg
    low_vol = volume < 0.7 * vol_avg
    demand = wide & up & high_vol & (pos > 2.0 / 3.0)
    supply = wide & down & high_vol & (pos < 1.0 / 3.0)
    no_demand = narrow & up & low_vol
    no_supply = narrow & down & low_vol
    sv = (down & high_vol & (pos > 0.5)) | (up & high_vol & (pos < 0.5))
    absorp = wide & high_vol & ((close - close.shift(1)).abs() < 0.3 * tr)
    vol_max21 = volume.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    coc = volume > 2.0 * vol_max21
    evr = high_vol & narrow
    score = (demand.astype(float) + supply.astype(float) + no_demand.astype(float)
             + no_supply.astype(float) + sv.astype(float) + absorp.astype(float)
             + coc.astype(float) + evr.astype(float))
    pv_evt = _pivot_high_event(high, 10)
    return score.where(pv_evt, np.nan).ffill()


def f07_lhll_220_truncated_5bar_topping_tail_at_pivot10_high(open_, high, low, close):
    upper_body = pd.concat([open_, close], axis=1).max(axis=1)
    lower_body = pd.concat([open_, close], axis=1).min(axis=1)
    body = (upper_body - lower_body).abs()
    upper_shadow = high - upper_body
    cond = (upper_shadow > 1.5 * body) & (body > 0)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(5, min_periods=1).sum() > 0
    cond_near = (cond & near).astype(float)
    return cond_near.rolling(WDAYS, min_periods=1).max().where(close.notna(), np.nan)


def f07_lhll_221_outside_down_bar_at_252d_high_indicator(high, low, close):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_max = (high.rolling(WDAYS, min_periods=1).max() >= rmax)
    cond = (outside & (pos < (1.0 / 3.0)) & near_max).astype(float)
    return cond.where(rmax.notna() & rng.notna(), np.nan)


def f07_lhll_222_three_black_crows_within_5d_of_pivot10_high(open_, high, low, close):
    down = (close < open_) & (close < close.shift(1))
    three = (down & down.shift(1) & down.shift(2)).astype(float)
    pv_evt = _pivot_high_event(high, 10).astype(float)
    near = pv_evt.rolling(WDAYS, min_periods=1).sum() > 0
    return (three * near.astype(float)).where(close.notna(), np.nan)


def f07_lhll_223_evening_star_proxy_at_252d_high_indicator(open_, high, low, close):
    body = (close - open_).abs()
    atr = _atr(high, low, close, MDAYS)
    big_up = (close > open_) & (body > 1.0 * atr)
    big_down = (close < open_) & (body > 1.0 * atr)
    small_body = body < 0.4 * atr
    seq = (big_up.shift(2) & small_body.shift(1) & big_down).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high.rolling(WDAYS, min_periods=1).max() >= 0.97 * rmax)
    return (seq * near.astype(float)).where(rmax.notna(), np.nan)


def f07_lhll_224_island_reversal_top_indicator_252d(high, low, close):
    gap_up = (low > high.shift(1)).astype(float)
    gap_down = (high < low.shift(1)).astype(float)
    gu_recent = gap_up.shift(1).rolling(WDAYS, min_periods=1).sum() > 0
    evt = (gap_down.astype(bool) & gu_recent).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high.rolling(WDAYS, min_periods=1).max() >= 0.95 * rmax)
    return (evt * near.astype(float)).where(rmax.notna(), np.nan)


def f07_lhll_225_terminal_breakdown_composite_score(high, low, close, volume):
    bc_cnt = f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    bc_flag = (bc_cnt > 0).astype(float)
    ar_sev = f07_lhll_154_wyckoff_automatic_reaction_severity_atr(high, low, close, volume)
    ar_flag = ((ar_sev.notna()) & (ar_sev > 1.0)).astype(float)
    utad_cnt = f07_lhll_156_wyckoff_utad_event_count_504d(high, low, close, volume)
    utad_flag = (utad_cnt > 0).astype(float)
    sow_cnt = f07_lhll_157_wyckoff_sow_event_indicator(high, low, close, volume).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    sow_flag = (sow_cnt > 0).astype(float)
    lpsy_cnt = f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d(high, low, close, volume)
    lpsy_flag = (lpsy_cnt > 0).astype(float)
    first_ll = f07_lhll_213_first_lower_low_after_alltime_high_indicator(high, low)
    ll_flag = (first_ll > 0).astype(float)
    score = bc_flag + ar_flag + utad_flag + sow_flag + lpsy_flag + ll_flag
    return score.where(close.notna(), np.nan)



def f07_lhll_151_wyckoff_psy_event_count_252d_d3(high, low, close, volume): return f07_lhll_151_wyckoff_psy_event_count_252d(high, low, close, volume).diff().diff().diff()

def f07_lhll_152_wyckoff_buying_climax_event_indicator_d3(high, low, close, volume): return f07_lhll_152_wyckoff_buying_climax_event_indicator(high, low, close, volume).diff().diff().diff()

def f07_lhll_153_bars_since_buying_climax_event_504d_d3(high, low, close, volume): return f07_lhll_153_bars_since_buying_climax_event_504d(high, low, close, volume).diff().diff().diff()

def f07_lhll_154_wyckoff_automatic_reaction_severity_atr_d3(high, low, close, volume): return f07_lhll_154_wyckoff_automatic_reaction_severity_atr(high, low, close, volume).diff().diff().diff()

def f07_lhll_155_wyckoff_secondary_test_failed_indicator_d3(high, low, close, volume): return f07_lhll_155_wyckoff_secondary_test_failed_indicator(high, low, close, volume).diff().diff().diff()

def f07_lhll_156_wyckoff_utad_event_count_504d_d3(high, low, close, volume): return f07_lhll_156_wyckoff_utad_event_count_504d(high, low, close, volume).diff().diff().diff()

def f07_lhll_157_wyckoff_sow_event_indicator_d3(high, low, close, volume): return f07_lhll_157_wyckoff_sow_event_indicator(high, low, close, volume).diff().diff().diff()

def f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d_d3(high, low, close, volume): return f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d(high, low, close, volume).diff().diff().diff()

def f07_lhll_159_wyckoff_phase_state_score_pivot10_d3(high, low, close, volume): return f07_lhll_159_wyckoff_phase_state_score_pivot10(high, low, close, volume).diff().diff().diff()

def f07_lhll_160_vsa_no_demand_bar_count_at_pivot_high_252d_d3(high, low, close, volume): return f07_lhll_160_vsa_no_demand_bar_count_at_pivot_high_252d(high, low, close, volume).diff().diff().diff()

def f07_lhll_161_vsa_upthrust_event_count_252d_d3(high, low, close, volume): return f07_lhll_161_vsa_upthrust_event_count_252d(high, low, close, volume).diff().diff().diff()

def f07_lhll_162_vsa_stopping_volume_event_indicator_d3(high, low, close, volume): return f07_lhll_162_vsa_stopping_volume_event_indicator(high, low, close, volume).diff().diff().diff()

def f07_lhll_163_hh_with_declining_volume_count_pivot10_252d_d3(high, volume): return f07_lhll_163_hh_with_declining_volume_count_pivot10_252d(high, volume).diff().diff().diff()

def f07_lhll_164_ll_with_rising_volume_count_pivot10_252d_d3(low, volume): return f07_lhll_164_ll_with_rising_volume_count_pivot10_252d(low, volume).diff().diff().diff()

def f07_lhll_165_pivot_high_volume_decay_slope_pivot10_252d_d3(high, volume): return f07_lhll_165_pivot_high_volume_decay_slope_pivot10_252d(high, volume).diff().diff().diff()

def f07_lhll_166_pivot_high_to_low_volume_ratio_252d_d3(high, low, volume): return f07_lhll_166_pivot_high_to_low_volume_ratio_252d(high, low, volume).diff().diff().diff()

def f07_lhll_167_wide_range_bar_at_pivot_high_count_252d_d3(high, low, close): return f07_lhll_167_wide_range_bar_at_pivot_high_count_252d(high, low, close).diff().diff().diff()

def f07_lhll_168_narrow_range_bar_at_pivot_high_count_252d_d3(high, low): return f07_lhll_168_narrow_range_bar_at_pivot_high_count_252d(high, low).diff().diff().diff()

def f07_lhll_169_nr7_to_wrb_transition_count_252d_d3(high, low, close): return f07_lhll_169_nr7_to_wrb_transition_count_252d(high, low, close).diff().diff().diff()

def f07_lhll_170_renko_1pct_consecutive_red_brick_count_d3(close): return f07_lhll_170_renko_1pct_consecutive_red_brick_count(close).diff().diff().diff()

def f07_lhll_171_renko_atr_brick_color_flip_count_252d_d3(high, low, close): return f07_lhll_171_renko_atr_brick_color_flip_count_252d(high, low, close).diff().diff().diff()

def f07_lhll_172_renko_1pct_brick_red_to_green_streak_252d_d3(close): return f07_lhll_172_renko_1pct_brick_red_to_green_streak_252d(close).diff().diff().diff()

def f07_lhll_173_renko_2pct_first_red_brick_after_long_green_indicator_d3(close): return f07_lhll_173_renko_2pct_first_red_brick_after_long_green_indicator(close).diff().diff().diff()

def f07_lhll_174_pf_3box_column_reversal_count_atr_box_252d_d3(high, low, close): return f07_lhll_174_pf_3box_column_reversal_count_atr_box_252d(high, low, close).diff().diff().diff()

def f07_lhll_175_pf_consecutive_o_column_length_atr_box_d3(high, low, close): return f07_lhll_175_pf_consecutive_o_column_length_atr_box(high, low, close).diff().diff().diff()

def f07_lhll_176_pf_x_to_o_transitions_after_alltime_high_504d_d3(high, low, close): return f07_lhll_176_pf_x_to_o_transitions_after_alltime_high_504d(high, low, close).diff().diff().diff()

def f07_lhll_177_pf_double_bottom_breakdown_event_indicator_d3(high, low, close): return f07_lhll_177_pf_double_bottom_breakdown_event_indicator(high, low, close).diff().diff().diff()

def f07_lhll_178_ha_red_bar_count_after_8_green_streak_252d_d3(open_, high, low, close): return f07_lhll_178_ha_red_bar_count_after_8_green_streak_252d(open_, high, low, close).diff().diff().diff()

def f07_lhll_179_ha_first_red_no_upper_shadow_after_green_streak_indicator_d3(open_, high, low, close): return f07_lhll_179_ha_first_red_no_upper_shadow_after_green_streak_indicator(open_, high, low, close).diff().diff().diff()

def f07_lhll_180_ha_green_to_red_state_flip_count_252d_d3(open_, high, low, close): return f07_lhll_180_ha_green_to_red_state_flip_count_252d(open_, high, low, close).diff().diff().diff()

def f07_lhll_181_ha_consecutive_red_streak_current_d3(open_, high, low, close): return f07_lhll_181_ha_consecutive_red_streak_current(open_, high, low, close).diff().diff().diff()

def f07_lhll_182_atr_trail_1x_flip_down_event_count_252d_d3(high, low, close): return f07_lhll_182_atr_trail_1x_flip_down_event_count_252d(high, low, close).diff().diff().diff()

def f07_lhll_183_atr_trail_3x_flip_down_event_count_504d_d3(high, low, close): return f07_lhll_183_atr_trail_3x_flip_down_event_count_504d(high, low, close).diff().diff().diff()

def f07_lhll_184_bars_since_atr_trail_2x_flip_down_d3(high, low, close): return f07_lhll_184_bars_since_atr_trail_2x_flip_down(high, low, close).diff().diff().diff()

def f07_lhll_185_atr_trail_multi_horizon_agreement_score_d3(high, low, close): return f07_lhll_185_atr_trail_multi_horizon_agreement_score(high, low, close).diff().diff().diff()

def f07_lhll_186_ichimoku_tenkan_below_kijun_streak_d3(high, low, close): return f07_lhll_186_ichimoku_tenkan_below_kijun_streak(high, low, close).diff().diff().diff()

def f07_lhll_187_ichimoku_price_below_kijun_streak_d3(high, low, close): return f07_lhll_187_ichimoku_price_below_kijun_streak(high, low, close).diff().diff().diff()

def f07_lhll_188_ichimoku_cloud_color_flip_to_bearish_indicator_d3(high, low, close): return f07_lhll_188_ichimoku_cloud_color_flip_to_bearish_indicator(high, low, close).diff().diff().diff()

def f07_lhll_189_ichimoku_chikou_below_price_streak_252d_d3(close): return f07_lhll_189_ichimoku_chikou_below_price_streak_252d(close).diff().diff().diff()

def f07_lhll_190_ichimoku_kijun_slope_negative_streak_d3(high, low, close): return f07_lhll_190_ichimoku_kijun_slope_negative_streak(high, low, close).diff().diff().diff()

def f07_lhll_191_diamond_top_range_expand_then_contract_indicator_d3(high, low): return f07_lhll_191_diamond_top_range_expand_then_contract_indicator(high, low).diff().diff().diff()

def f07_lhll_192_broadening_top_megaphone_indicator_252d_d3(high, low): return f07_lhll_192_broadening_top_megaphone_indicator_252d(high, low).diff().diff().diff()

def f07_lhll_193_rectangle_distribution_breakdown_indicator_d3(high, low, close): return f07_lhll_193_rectangle_distribution_breakdown_indicator(high, low, close).diff().diff().diff()

def f07_lhll_194_truncated_swing_coil_at_top_indicator_d3(high, low): return f07_lhll_194_truncated_swing_coil_at_top_indicator(high, low).diff().diff().diff()

def f07_lhll_195_stair_step_decline_5pivot_indicator_d3(high, low): return f07_lhll_195_stair_step_decline_5pivot_indicator(high, low).diff().diff().diff()

def f07_lhll_196_dwell_time_above_minus_below_pivot10_high_252d_d3(high): return f07_lhll_196_dwell_time_above_minus_below_pivot10_high_252d(high).diff().diff().diff()

def f07_lhll_197_dwell_time_above_minus_below_pivot10_low_252d_d3(low, high): return f07_lhll_197_dwell_time_above_minus_below_pivot10_low_252d(low, high).diff().diff().diff()

def f07_lhll_198_close_below_pivot21_low_fraction_252d_d3(low, close): return f07_lhll_198_close_below_pivot21_low_fraction_252d(low, close).diff().diff().diff()

def f07_lhll_199_rolling_cusum_break_on_returns_504d_d3(close): return f07_lhll_199_rolling_cusum_break_on_returns_504d(close).diff().diff().diff()

def f07_lhll_200_rolling_chow_ftest_slope_change_63v252_d3(close): return f07_lhll_200_rolling_chow_ftest_slope_change_63v252(close).diff().diff().diff()

def f07_lhll_201_variance_ratio_at_recent_pivot10_high_d3(close, high): return f07_lhll_201_variance_ratio_at_recent_pivot10_high(close, high).diff().diff().diff()

def f07_lhll_202_hurst_exponent_change_63d_vs_252d_d3(close): return f07_lhll_202_hurst_exponent_change_63d_vs_252d(close).diff().diff().diff()

def f07_lhll_203_fractal_dimension_higuchi_252d_change_d3(close): return f07_lhll_203_fractal_dimension_higuchi_252d_change(close).diff().diff().diff()

def f07_lhll_204_sequential_hh_volume_decay_3in_a_row_indicator_d3(high, volume): return f07_lhll_204_sequential_hh_volume_decay_3in_a_row_indicator(high, volume).diff().diff().diff()

def f07_lhll_205_sequential_ll_volume_rising_3in_a_row_indicator_d3(low, volume): return f07_lhll_205_sequential_ll_volume_rising_3in_a_row_indicator(low, volume).diff().diff().diff()

def f07_lhll_206_nested_swing_small_inside_big_degradation_score_d3(high, low): return f07_lhll_206_nested_swing_small_inside_big_degradation_score(high, low).diff().diff().diff()

def f07_lhll_207_multi_resolution_swing_disagreement_5_10_21_d3(high, low): return f07_lhll_207_multi_resolution_swing_disagreement_5_10_21(high, low).diff().diff().diff()

def f07_lhll_208_dmi_minus_di_above_plus_di_streak_d3(high, low, close): return f07_lhll_208_dmi_minus_di_above_plus_di_streak(high, low, close).diff().diff().diff()

def f07_lhll_209_dmi_adx_rising_with_minus_di_dominant_streak_d3(high, low, close): return f07_lhll_209_dmi_adx_rising_with_minus_di_dominant_streak(high, low, close).diff().diff().diff()

def f07_lhll_210_dominant_cycle_period_shift_ehlers_proxy_d3(close): return f07_lhll_210_dominant_cycle_period_shift_ehlers_proxy(close).diff().diff().diff()

def f07_lhll_211_range_of_range_percentile_63d_in_252d_d3(high, low): return f07_lhll_211_range_of_range_percentile_63d_in_252d(high, low).diff().diff().diff()

def f07_lhll_212_range_contraction_then_expansion_at_top_indicator_d3(high, low, close): return f07_lhll_212_range_contraction_then_expansion_at_top_indicator(high, low, close).diff().diff().diff()

def f07_lhll_213_first_lower_low_after_alltime_high_indicator_d3(high, low): return f07_lhll_213_first_lower_low_after_alltime_high_indicator(high, low).diff().diff().diff()

def f07_lhll_214_bars_between_alltime_high_and_first_dow_breakdown_d3(high, low): return f07_lhll_214_bars_between_alltime_high_and_first_dow_breakdown(high, low).diff().diff().diff()

def f07_lhll_215_pivot10_swing_return_skewness_252d_d3(high, low, close): return f07_lhll_215_pivot10_swing_return_skewness_252d(high, low, close).diff().diff().diff()

def f07_lhll_216_pivot10_swing_return_kurtosis_252d_d3(high, low, close): return f07_lhll_216_pivot10_swing_return_kurtosis_252d(high, low, close).diff().diff().diff()

def f07_lhll_217_mcginley_dynamic_below_close_streak_d3(close): return f07_lhll_217_mcginley_dynamic_below_close_streak(close).diff().diff().diff()

def f07_lhll_218_mcginley_slope_negative_streak_d3(close): return f07_lhll_218_mcginley_slope_negative_streak(close).diff().diff().diff()

def f07_lhll_219_vsa_eight_signal_state_composite_at_pivot10_high_d3(high, low, close, volume): return f07_lhll_219_vsa_eight_signal_state_composite_at_pivot10_high(high, low, close, volume).diff().diff().diff()

def f07_lhll_220_truncated_5bar_topping_tail_at_pivot10_high_d3(open_, high, low, close): return f07_lhll_220_truncated_5bar_topping_tail_at_pivot10_high(open_, high, low, close).diff().diff().diff()

def f07_lhll_221_outside_down_bar_at_252d_high_indicator_d3(high, low, close): return f07_lhll_221_outside_down_bar_at_252d_high_indicator(high, low, close).diff().diff().diff()

def f07_lhll_222_three_black_crows_within_5d_of_pivot10_high_d3(open_, high, low, close): return f07_lhll_222_three_black_crows_within_5d_of_pivot10_high(open_, high, low, close).diff().diff().diff()

def f07_lhll_223_evening_star_proxy_at_252d_high_indicator_d3(open_, high, low, close): return f07_lhll_223_evening_star_proxy_at_252d_high_indicator(open_, high, low, close).diff().diff().diff()

def f07_lhll_224_island_reversal_top_indicator_252d_d3(high, low, close): return f07_lhll_224_island_reversal_top_indicator_252d(high, low, close).diff().diff().diff()

def f07_lhll_225_terminal_breakdown_composite_score_d3(high, low, close, volume): return f07_lhll_225_terminal_breakdown_composite_score(high, low, close, volume).diff().diff().diff()


LOWER_HIGH_LOWER_LOW_STRUCTURE_D3_REGISTRY_151_225 = {
    "f07_lhll_151_wyckoff_psy_event_count_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_151_wyckoff_psy_event_count_252d_d3},
    "f07_lhll_152_wyckoff_buying_climax_event_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_152_wyckoff_buying_climax_event_indicator_d3},
    "f07_lhll_153_bars_since_buying_climax_event_504d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_153_bars_since_buying_climax_event_504d_d3},
    "f07_lhll_154_wyckoff_automatic_reaction_severity_atr_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_154_wyckoff_automatic_reaction_severity_atr_d3},
    "f07_lhll_155_wyckoff_secondary_test_failed_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_155_wyckoff_secondary_test_failed_indicator_d3},
    "f07_lhll_156_wyckoff_utad_event_count_504d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_156_wyckoff_utad_event_count_504d_d3},
    "f07_lhll_157_wyckoff_sow_event_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_157_wyckoff_sow_event_indicator_d3},
    "f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_158_wyckoff_lpsy_failed_rally_count_252d_d3},
    "f07_lhll_159_wyckoff_phase_state_score_pivot10_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_159_wyckoff_phase_state_score_pivot10_d3},
    "f07_lhll_160_vsa_no_demand_bar_count_at_pivot_high_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_160_vsa_no_demand_bar_count_at_pivot_high_252d_d3},
    "f07_lhll_161_vsa_upthrust_event_count_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_161_vsa_upthrust_event_count_252d_d3},
    "f07_lhll_162_vsa_stopping_volume_event_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_162_vsa_stopping_volume_event_indicator_d3},
    "f07_lhll_163_hh_with_declining_volume_count_pivot10_252d_d3": {"inputs": ["high", "volume"], "func": f07_lhll_163_hh_with_declining_volume_count_pivot10_252d_d3},
    "f07_lhll_164_ll_with_rising_volume_count_pivot10_252d_d3": {"inputs": ["low", "volume"], "func": f07_lhll_164_ll_with_rising_volume_count_pivot10_252d_d3},
    "f07_lhll_165_pivot_high_volume_decay_slope_pivot10_252d_d3": {"inputs": ["high", "volume"], "func": f07_lhll_165_pivot_high_volume_decay_slope_pivot10_252d_d3},
    "f07_lhll_166_pivot_high_to_low_volume_ratio_252d_d3": {"inputs": ["high", "low", "volume"], "func": f07_lhll_166_pivot_high_to_low_volume_ratio_252d_d3},
    "f07_lhll_167_wide_range_bar_at_pivot_high_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_167_wide_range_bar_at_pivot_high_count_252d_d3},
    "f07_lhll_168_narrow_range_bar_at_pivot_high_count_252d_d3": {"inputs": ["high", "low"], "func": f07_lhll_168_narrow_range_bar_at_pivot_high_count_252d_d3},
    "f07_lhll_169_nr7_to_wrb_transition_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_169_nr7_to_wrb_transition_count_252d_d3},
    "f07_lhll_170_renko_1pct_consecutive_red_brick_count_d3": {"inputs": ["close"], "func": f07_lhll_170_renko_1pct_consecutive_red_brick_count_d3},
    "f07_lhll_171_renko_atr_brick_color_flip_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_171_renko_atr_brick_color_flip_count_252d_d3},
    "f07_lhll_172_renko_1pct_brick_red_to_green_streak_252d_d3": {"inputs": ["close"], "func": f07_lhll_172_renko_1pct_brick_red_to_green_streak_252d_d3},
    "f07_lhll_173_renko_2pct_first_red_brick_after_long_green_indicator_d3": {"inputs": ["close"], "func": f07_lhll_173_renko_2pct_first_red_brick_after_long_green_indicator_d3},
    "f07_lhll_174_pf_3box_column_reversal_count_atr_box_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_174_pf_3box_column_reversal_count_atr_box_252d_d3},
    "f07_lhll_175_pf_consecutive_o_column_length_atr_box_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_175_pf_consecutive_o_column_length_atr_box_d3},
    "f07_lhll_176_pf_x_to_o_transitions_after_alltime_high_504d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_176_pf_x_to_o_transitions_after_alltime_high_504d_d3},
    "f07_lhll_177_pf_double_bottom_breakdown_event_indicator_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_177_pf_double_bottom_breakdown_event_indicator_d3},
    "f07_lhll_178_ha_red_bar_count_after_8_green_streak_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_178_ha_red_bar_count_after_8_green_streak_252d_d3},
    "f07_lhll_179_ha_first_red_no_upper_shadow_after_green_streak_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_179_ha_first_red_no_upper_shadow_after_green_streak_indicator_d3},
    "f07_lhll_180_ha_green_to_red_state_flip_count_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_180_ha_green_to_red_state_flip_count_252d_d3},
    "f07_lhll_181_ha_consecutive_red_streak_current_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_181_ha_consecutive_red_streak_current_d3},
    "f07_lhll_182_atr_trail_1x_flip_down_event_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_182_atr_trail_1x_flip_down_event_count_252d_d3},
    "f07_lhll_183_atr_trail_3x_flip_down_event_count_504d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_183_atr_trail_3x_flip_down_event_count_504d_d3},
    "f07_lhll_184_bars_since_atr_trail_2x_flip_down_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_184_bars_since_atr_trail_2x_flip_down_d3},
    "f07_lhll_185_atr_trail_multi_horizon_agreement_score_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_185_atr_trail_multi_horizon_agreement_score_d3},
    "f07_lhll_186_ichimoku_tenkan_below_kijun_streak_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_186_ichimoku_tenkan_below_kijun_streak_d3},
    "f07_lhll_187_ichimoku_price_below_kijun_streak_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_187_ichimoku_price_below_kijun_streak_d3},
    "f07_lhll_188_ichimoku_cloud_color_flip_to_bearish_indicator_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_188_ichimoku_cloud_color_flip_to_bearish_indicator_d3},
    "f07_lhll_189_ichimoku_chikou_below_price_streak_252d_d3": {"inputs": ["close"], "func": f07_lhll_189_ichimoku_chikou_below_price_streak_252d_d3},
    "f07_lhll_190_ichimoku_kijun_slope_negative_streak_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_190_ichimoku_kijun_slope_negative_streak_d3},
    "f07_lhll_191_diamond_top_range_expand_then_contract_indicator_d3": {"inputs": ["high", "low"], "func": f07_lhll_191_diamond_top_range_expand_then_contract_indicator_d3},
    "f07_lhll_192_broadening_top_megaphone_indicator_252d_d3": {"inputs": ["high", "low"], "func": f07_lhll_192_broadening_top_megaphone_indicator_252d_d3},
    "f07_lhll_193_rectangle_distribution_breakdown_indicator_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_193_rectangle_distribution_breakdown_indicator_d3},
    "f07_lhll_194_truncated_swing_coil_at_top_indicator_d3": {"inputs": ["high", "low"], "func": f07_lhll_194_truncated_swing_coil_at_top_indicator_d3},
    "f07_lhll_195_stair_step_decline_5pivot_indicator_d3": {"inputs": ["high", "low"], "func": f07_lhll_195_stair_step_decline_5pivot_indicator_d3},
    "f07_lhll_196_dwell_time_above_minus_below_pivot10_high_252d_d3": {"inputs": ["high"], "func": f07_lhll_196_dwell_time_above_minus_below_pivot10_high_252d_d3},
    "f07_lhll_197_dwell_time_above_minus_below_pivot10_low_252d_d3": {"inputs": ["low", "high"], "func": f07_lhll_197_dwell_time_above_minus_below_pivot10_low_252d_d3},
    "f07_lhll_198_close_below_pivot21_low_fraction_252d_d3": {"inputs": ["low", "close"], "func": f07_lhll_198_close_below_pivot21_low_fraction_252d_d3},
    "f07_lhll_199_rolling_cusum_break_on_returns_504d_d3": {"inputs": ["close"], "func": f07_lhll_199_rolling_cusum_break_on_returns_504d_d3},
    "f07_lhll_200_rolling_chow_ftest_slope_change_63v252_d3": {"inputs": ["close"], "func": f07_lhll_200_rolling_chow_ftest_slope_change_63v252_d3},
    "f07_lhll_201_variance_ratio_at_recent_pivot10_high_d3": {"inputs": ["close", "high"], "func": f07_lhll_201_variance_ratio_at_recent_pivot10_high_d3},
    "f07_lhll_202_hurst_exponent_change_63d_vs_252d_d3": {"inputs": ["close"], "func": f07_lhll_202_hurst_exponent_change_63d_vs_252d_d3},
    "f07_lhll_203_fractal_dimension_higuchi_252d_change_d3": {"inputs": ["close"], "func": f07_lhll_203_fractal_dimension_higuchi_252d_change_d3},
    "f07_lhll_204_sequential_hh_volume_decay_3in_a_row_indicator_d3": {"inputs": ["high", "volume"], "func": f07_lhll_204_sequential_hh_volume_decay_3in_a_row_indicator_d3},
    "f07_lhll_205_sequential_ll_volume_rising_3in_a_row_indicator_d3": {"inputs": ["low", "volume"], "func": f07_lhll_205_sequential_ll_volume_rising_3in_a_row_indicator_d3},
    "f07_lhll_206_nested_swing_small_inside_big_degradation_score_d3": {"inputs": ["high", "low"], "func": f07_lhll_206_nested_swing_small_inside_big_degradation_score_d3},
    "f07_lhll_207_multi_resolution_swing_disagreement_5_10_21_d3": {"inputs": ["high", "low"], "func": f07_lhll_207_multi_resolution_swing_disagreement_5_10_21_d3},
    "f07_lhll_208_dmi_minus_di_above_plus_di_streak_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_208_dmi_minus_di_above_plus_di_streak_d3},
    "f07_lhll_209_dmi_adx_rising_with_minus_di_dominant_streak_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_209_dmi_adx_rising_with_minus_di_dominant_streak_d3},
    "f07_lhll_210_dominant_cycle_period_shift_ehlers_proxy_d3": {"inputs": ["close"], "func": f07_lhll_210_dominant_cycle_period_shift_ehlers_proxy_d3},
    "f07_lhll_211_range_of_range_percentile_63d_in_252d_d3": {"inputs": ["high", "low"], "func": f07_lhll_211_range_of_range_percentile_63d_in_252d_d3},
    "f07_lhll_212_range_contraction_then_expansion_at_top_indicator_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_212_range_contraction_then_expansion_at_top_indicator_d3},
    "f07_lhll_213_first_lower_low_after_alltime_high_indicator_d3": {"inputs": ["high", "low"], "func": f07_lhll_213_first_lower_low_after_alltime_high_indicator_d3},
    "f07_lhll_214_bars_between_alltime_high_and_first_dow_breakdown_d3": {"inputs": ["high", "low"], "func": f07_lhll_214_bars_between_alltime_high_and_first_dow_breakdown_d3},
    "f07_lhll_215_pivot10_swing_return_skewness_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_215_pivot10_swing_return_skewness_252d_d3},
    "f07_lhll_216_pivot10_swing_return_kurtosis_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_216_pivot10_swing_return_kurtosis_252d_d3},
    "f07_lhll_217_mcginley_dynamic_below_close_streak_d3": {"inputs": ["close"], "func": f07_lhll_217_mcginley_dynamic_below_close_streak_d3},
    "f07_lhll_218_mcginley_slope_negative_streak_d3": {"inputs": ["close"], "func": f07_lhll_218_mcginley_slope_negative_streak_d3},
    "f07_lhll_219_vsa_eight_signal_state_composite_at_pivot10_high_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_219_vsa_eight_signal_state_composite_at_pivot10_high_d3},
    "f07_lhll_220_truncated_5bar_topping_tail_at_pivot10_high_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_220_truncated_5bar_topping_tail_at_pivot10_high_d3},
    "f07_lhll_221_outside_down_bar_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_221_outside_down_bar_at_252d_high_indicator_d3},
    "f07_lhll_222_three_black_crows_within_5d_of_pivot10_high_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_222_three_black_crows_within_5d_of_pivot10_high_d3},
    "f07_lhll_223_evening_star_proxy_at_252d_high_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f07_lhll_223_evening_star_proxy_at_252d_high_indicator_d3},
    "f07_lhll_224_island_reversal_top_indicator_252d_d3": {"inputs": ["high", "low", "close"], "func": f07_lhll_224_island_reversal_top_indicator_252d_d3},
    "f07_lhll_225_terminal_breakdown_composite_score_d3": {"inputs": ["high", "low", "close", "volume"], "func": f07_lhll_225_terminal_breakdown_composite_score_d3},
}
