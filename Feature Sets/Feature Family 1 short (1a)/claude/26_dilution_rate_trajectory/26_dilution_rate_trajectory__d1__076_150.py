"""dilution_rate_trajectory d1 features 076-150 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _ttm(s):
    return s.rolling(4, min_periods=1).sum()

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

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
    return s.ewm(span=span, min_periods=max(span // 3, 2), adjust=False).mean()

def f26_drtj_076_sharesbas_split_adjusted_qoq_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    return _safe_div(sa.diff(), sa.shift(1).abs()).diff()

def f26_drtj_077_sharesbas_split_adjusted_yoy_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    return _safe_div(sa - sa.shift(4), sa.shift(4).abs()).diff()

def f26_drtj_078_sharesbas_split_adjusted_8q_pct_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    return _safe_div(sa - sa.shift(8), sa.shift(8).abs()).diff()

def f26_drtj_079_sharefactor_change_flag_d1(sharefactor):
    return (sharefactor.diff().abs() > 1e-09).astype(float).diff()

def f26_drtj_080_sharefactor_recent_change_8q_d1(sharefactor):
    return (sharefactor.diff().abs() > 1e-09).astype(float).rolling(8, min_periods=1).sum().diff()

def f26_drtj_081_sharesbas_reverse_split_adjusted_growth_d1(sharesbas, sharefactor):
    reverse = (sharefactor.diff() > 1e-09).astype(float)
    raw = _yoy_pct(sharesbas)
    return (raw + 0.5 * reverse).diff()

def f26_drtj_082_sharesbas_div_sharefactor_qoq_d1(sharesbas, sharefactor):
    return _qoq_pct(_safe_div(sharesbas, sharefactor.replace(0, np.nan))).diff()

def f26_drtj_083_organic_dilution_qoq_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    factor_chg = sharefactor.diff().abs() > 1e-09
    raw = _safe_div(sa.diff(), sa.shift(1).abs())
    return raw.where(~factor_chg, np.nan).diff()

def f26_drtj_084_organic_dilution_yoy_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    factor_chg = (sharefactor.diff().abs() > 1e-09).rolling(4, min_periods=1).sum() > 0
    raw = _safe_div(sa - sa.shift(4), sa.shift(4).abs())
    return raw.where(~factor_chg, np.nan).diff()

def f26_drtj_085_organic_dilution_8q_d1(sharesbas, sharefactor):
    sa = sharesbas * sharefactor
    factor_chg = (sharefactor.diff().abs() > 1e-09).rolling(8, min_periods=1).sum() > 0
    raw = _safe_div(sa - sa.shift(8), sa.shift(8).abs())
    return raw.where(~factor_chg, np.nan).diff()

def f26_drtj_086_sharesbas_x_price_yoy_d1(sharesbas, close):
    iss = sharesbas - sharesbas.shift(4)
    return (iss * close).diff()

def f26_drtj_087_sharesbas_growth_x_marketcap_yoy_d1(sharesbas, marketcap):
    return (_yoy_pct(sharesbas) * marketcap).diff()

def f26_drtj_088_dilution_value_to_mcap_4q_d1(sharesbas, marketcap, close):
    iss = sharesbas - sharesbas.shift(4)
    return _safe_div(iss * close, marketcap).diff()

def f26_drtj_089_dilution_value_to_mcap_8q_d1(sharesbas, marketcap, close):
    iss = sharesbas - sharesbas.shift(8)
    return _safe_div(iss * close, marketcap).diff()

def f26_drtj_090_ncfcommon_to_ncfi_ttm_d1(ncfcommon, ncfi):
    return _safe_div(_ttm(ncfcommon), _ttm(ncfi).abs()).diff()

def f26_drtj_091_buyback_to_dilution_ratio_8q_d1(ncfcommon):
    buy = (-ncfcommon.clip(upper=0)).rolling(8, min_periods=3).sum()
    iss = ncfcommon.clip(lower=0).rolling(8, min_periods=3).sum()
    return _safe_div(buy, iss).diff()

def f26_drtj_092_net_share_change_qoq_pct_d1(sharesbas):
    return _qoq_pct(sharesbas).diff()

def f26_drtj_093_net_share_change_8q_pct_d1(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(8), sharesbas.shift(8).abs()).diff()

def f26_drtj_094_buyback_count_8q_d1(ncfcommon):
    return (ncfcommon < 0).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_095_buyback_dollar_8q_d1(ncfcommon):
    return (-ncfcommon.clip(upper=0)).rolling(8, min_periods=3).sum().diff()

def f26_drtj_096_share_repurchase_vs_dilution_4q_d1(ncfcommon):
    buy = (-ncfcommon.clip(upper=0)).rolling(4, min_periods=2).sum()
    iss = ncfcommon.clip(lower=0).rolling(4, min_periods=2).sum()
    return (buy - iss).diff()

def f26_drtj_097_net_issuance_dollar_8q_d1(ncfcommon):
    return ncfcommon.rolling(8, min_periods=3).sum().diff()

def f26_drtj_098_buyback_streak_break_flag_d1(ncfcommon):
    buyback = (ncfcommon < 0).astype(int)
    prev_buy = buyback.shift(1)
    return ((prev_buy == 1) & (buyback == 0)).astype(float).diff()

def f26_drtj_099_ncfcommon_minus_buybacks_pct_d1(ncfcommon, marketcap):
    iss = ncfcommon.clip(lower=0)
    buy = -ncfcommon.clip(upper=0)
    return _safe_div(_ttm(iss) - _ttm(buy), marketcap).diff()

def f26_drtj_100_share_issuance_intensity_score_d1(ncfcommon, marketcap):
    cnt = (ncfcommon > 0).astype(float).rolling(8, min_periods=3).sum()
    sz = _safe_div(_ttm(ncfcommon.clip(lower=0)), marketcap)
    return (cnt * sz).diff()

def f26_drtj_101_dilution_during_distress_flag_d1(sharesbas, fcf):
    dil = _qoq_pct(sharesbas) > 0
    burn = fcf < 0
    return (dil & burn).astype(float).diff()

def f26_drtj_102_dilution_during_distress_count_8q_d1(sharesbas, fcf):
    dil = _qoq_pct(sharesbas) > 0
    burn = fcf < 0
    return (dil & burn).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_103_dilution_during_loss_count_8q_d1(sharesbas, netinc):
    dil = _qoq_pct(sharesbas) > 0
    loss = netinc < 0
    return (dil & loss).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_104_dilution_during_burn_8q_d1(sharesbas, ncfo):
    dil = _qoq_pct(sharesbas) > 0
    burn = ncfo < 0
    return (dil & burn).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_105_cumulative_distress_dilution_8q_d1(sharesbas, fcf):
    dil = _qoq_pct(sharesbas).clip(lower=0)
    burn = (fcf < 0).astype(float)
    return (dil * burn).rolling(8, min_periods=3).sum().diff()

def f26_drtj_106_dilution_to_cashneq_ratio_d1(ncfcommon, cashneq):
    return _safe_div(ncfcommon, cashneq).diff()

def f26_drtj_107_dilution_to_runway_ratio_d1(ncfcommon, fcf, cashneq):
    burn = (-fcf).clip(lower=1e-06)
    runway = _safe_div(cashneq, burn)
    return _safe_div(ncfcommon, runway.replace(0, np.nan)).diff()

def f26_drtj_108_dilution_replaces_fcf_proxy_d1(ncfcommon, fcf):
    return _safe_div(-_ttm(fcf), _ttm(ncfcommon)).diff()

def f26_drtj_109_dilution_when_pe_high_proxy_d1(sharesbas, marketcap, netinc):
    pe = _safe_div(marketcap, _ttm(netinc))
    dil = _qoq_pct(sharesbas)
    high = pe > pe.rolling(8, min_periods=3).median()
    return dil.where(high, 0.0).diff()

def f26_drtj_110_dilution_efficiency_proxy_d1(sharesbas, revenue):
    return _safe_div(_yoy_pct(_ttm(revenue)), _yoy_pct(sharesbas).abs()).diff()

def f26_drtj_111_sharesbas_qoq_volatility_4q_d1(sharesbas):
    return _qoq_pct(sharesbas).rolling(4, min_periods=2).std().diff()

def f26_drtj_112_sharesbas_qoq_volatility_8q_d1(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).std().diff()

def f26_drtj_113_sharesbas_qoq_volatility_12q_d1(sharesbas):
    return _qoq_pct(sharesbas).rolling(12, min_periods=4).std().diff()

def f26_drtj_114_dilution_rate_cv_8q_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    m = q.rolling(8, min_periods=3).mean()
    sd = q.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs()).diff()

def f26_drtj_115_dilution_acceleration_4q_d1(sharesbas):
    return _yoy_pct(sharesbas).diff().diff()

def f26_drtj_116_dilution_cliff_detector_8q_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    sd = q.rolling(8, min_periods=3).std().shift(1)
    return (q > 2.0 * sd).astype(float).diff()

def f26_drtj_117_dilution_jump_detector_8q_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    p95 = q.rolling(8, min_periods=3).quantile(0.95).shift(1)
    return (q > p95).astype(float).diff()

def f26_drtj_118_dilution_regime_break_8q_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    recent = q.rolling(4, min_periods=2).mean()
    prior = q.shift(4).rolling(4, min_periods=2).mean()
    return (recent - prior).diff()

def f26_drtj_119_dilution_trend_slope_8q_d1(sharesbas):
    return _rolling_slope(_safe_log(sharesbas), 8).diff()

def f26_drtj_120_dilution_trend_slope_change_8q_d1(sharesbas):
    return _rolling_slope(_safe_log(sharesbas), 8).diff(8).diff()

def f26_drtj_121_dilution_trend_acceleration_12q_d1(sharesbas):
    return _rolling_slope(_safe_log(sharesbas), 12).diff(4).diff()

def f26_drtj_122_dilution_structural_break_chow_8q_d1(sharesbas):
    s = _safe_log(sharesbas)
    rec_var = s.diff().rolling(4, min_periods=2).var()
    full_var = s.diff().rolling(8, min_periods=3).var()
    return _safe_div(rec_var, full_var).diff()

def f26_drtj_123_dilution_log_trend_residual_volatility_8q_d1(sharesbas):
    s = _safe_log(sharesbas)
    trend = s.rolling(8, min_periods=3).mean()
    return (s - trend).rolling(8, min_periods=3).std().diff()

def f26_drtj_124_dilution_rate_smoothed_minus_raw_d1(sharesbas):
    y = _yoy_pct(sharesbas)
    return (_ema(y, 4) - y).diff()

def f26_drtj_125_dilution_inflection_detector_d1(sharesbas):
    d2 = sharesbas.diff().diff()
    sign = np.sign(d2)
    return (sign != sign.shift(1)).astype(float).diff()

def f26_drtj_126_dilution_inflection_count_12q_d1(sharesbas):
    d2 = sharesbas.diff().diff()
    sign = np.sign(d2)
    flips = (sign != sign.shift(1)).astype(float)
    return flips.rolling(12, min_periods=4).sum().diff()

def f26_drtj_127_dilution_drawdown_recovery_inverse_d1(sharesbas):
    lo = sharesbas.rolling(20, min_periods=6).min()
    return _safe_div(sharesbas - lo, lo.abs()).diff()

def f26_drtj_128_sharesbas_above_8q_max_flag_d1(sharesbas):
    return (sharesbas >= sharesbas.rolling(8, min_periods=3).max()).astype(float).diff()

def f26_drtj_129_sharesbas_above_12q_max_flag_d1(sharesbas):
    return (sharesbas >= sharesbas.rolling(12, min_periods=4).max()).astype(float).diff()

def f26_drtj_130_sharesbas_above_20q_max_flag_d1(sharesbas):
    return (sharesbas >= sharesbas.rolling(20, min_periods=6).max()).astype(float).diff()

def f26_drtj_131_dilution_per_revenue_dollar_8q_d1(sharesbas, revenue):
    iss = sharesbas - sharesbas.shift(8)
    return _safe_div(iss, _ttm(revenue)).diff()

def f26_drtj_132_dilution_per_equity_dollar_8q_d1(sharesbas, equity):
    iss = sharesbas - sharesbas.shift(8)
    return _safe_div(iss, equity).diff()

def f26_drtj_133_dilution_per_marketcap_dollar_8q_d1(sharesbas, marketcap):
    iss = sharesbas - sharesbas.shift(8)
    return _safe_div(iss, marketcap).diff()

def f26_drtj_134_sharesbas_yoy_minus_industry_proxy_d1(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.rolling(12, min_periods=4).median()).diff()

def f26_drtj_135_sharesbas_log_yoy_normalized_by_volatility_d1(sharesbas):
    y = _safe_log(sharesbas) - _safe_log(sharesbas.shift(4))
    sd = y.rolling(8, min_periods=3).std()
    return _safe_div(y, sd).diff()

def f26_drtj_136_issuance_episode_intensity_d1(sharesbas):
    big = (_qoq_pct(sharesbas) > 0.02).astype(int)
    grp = (big != big.shift()).cumsum()
    return big.groupby(grp).cumsum().diff()

def f26_drtj_137_issuance_burst_frequency_d1(sharesbas):
    big = (_qoq_pct(sharesbas) > 0.05).astype(float)
    return big.rolling(8, min_periods=3).sum().diff()

def f26_drtj_138_dilution_kink_count_8q_d1(sharesbas):
    d2 = sharesbas.diff().diff()
    sign = np.sign(d2)
    return (sign != sign.shift(1)).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_139_dilution_persistence_score_d1(sharesbas):
    freq = (_qoq_pct(sharesbas) > 0).astype(float).rolling(8, min_periods=3).mean()
    mag = _qoq_pct(sharesbas).clip(lower=0).rolling(8, min_periods=3).mean()
    return (freq * mag).diff()

def f26_drtj_140_dilution_terminal_signal_d1(sharesbas):
    return (_qoq_pct(sharesbas) > 0.5).astype(float).diff()

def f26_drtj_141_dilution_terminal_signal_count_8q_d1(sharesbas):
    return (_qoq_pct(sharesbas) > 0.5).astype(float).rolling(8, min_periods=3).sum().diff()

def f26_drtj_142_sharesbas_log_residual_8q_d1(sharesbas):
    s = _safe_log(sharesbas)
    return (s - s.rolling(8, min_periods=3).mean()).diff()

def f26_drtj_143_sharesbas_growth_to_avg_growth_4q_d1(sharesbas):
    y = _yoy_pct(sharesbas)
    return _safe_div(y, y.rolling(4, min_periods=2).mean().abs()).diff()

def f26_drtj_144_sharesbas_acceleration_yoy_4q_d1(sharesbas):
    y = _yoy_pct(sharesbas)
    return (y - y.shift(4)).diff()

def f26_drtj_145_sharesbas_growth_step_change_8q_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    return (q.rolling(4, min_periods=2).mean() - q.shift(4).rolling(4, min_periods=2).mean()).diff()

def f26_drtj_146_sharesbas_qoq_minus_yoy_quarterized_d1(sharesbas):
    q = _qoq_pct(sharesbas)
    y_quart = _yoy_pct(sharesbas) / 4.0
    return (q - y_quart).diff()

def f26_drtj_147_sharesbas_growth_smoothed_ema_8q_d1(sharesbas):
    return _ema(_yoy_pct(sharesbas), 8).diff()

def f26_drtj_148_sharesbas_growth_smoothed_minus_raw_d1(sharesbas):
    y = _yoy_pct(sharesbas)
    return (_ema(y, 4) - y).diff()

def f26_drtj_149_sharesbas_quarterly_pace_zscore_8q_d1(sharesbas):
    return _rolling_zscore(_qoq_pct(sharesbas), 8).diff()

def f26_drtj_150_sharesbas_long_term_dilution_ratio_d1(sharesbas):
    return _safe_div(sharesbas, sharesbas.shift(20)).diff()
DILUTION_RATE_TRAJECTORY_D1_REGISTRY_076_150 = {'f26_drtj_076_sharesbas_split_adjusted_qoq_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_076_sharesbas_split_adjusted_qoq_d1}, 'f26_drtj_077_sharesbas_split_adjusted_yoy_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_077_sharesbas_split_adjusted_yoy_d1}, 'f26_drtj_078_sharesbas_split_adjusted_8q_pct_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_078_sharesbas_split_adjusted_8q_pct_d1}, 'f26_drtj_079_sharefactor_change_flag_d1': {'inputs': ['sharefactor'], 'func': f26_drtj_079_sharefactor_change_flag_d1}, 'f26_drtj_080_sharefactor_recent_change_8q_d1': {'inputs': ['sharefactor'], 'func': f26_drtj_080_sharefactor_recent_change_8q_d1}, 'f26_drtj_081_sharesbas_reverse_split_adjusted_growth_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_081_sharesbas_reverse_split_adjusted_growth_d1}, 'f26_drtj_082_sharesbas_div_sharefactor_qoq_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_082_sharesbas_div_sharefactor_qoq_d1}, 'f26_drtj_083_organic_dilution_qoq_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_083_organic_dilution_qoq_d1}, 'f26_drtj_084_organic_dilution_yoy_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_084_organic_dilution_yoy_d1}, 'f26_drtj_085_organic_dilution_8q_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f26_drtj_085_organic_dilution_8q_d1}, 'f26_drtj_086_sharesbas_x_price_yoy_d1': {'inputs': ['sharesbas', 'close'], 'func': f26_drtj_086_sharesbas_x_price_yoy_d1}, 'f26_drtj_087_sharesbas_growth_x_marketcap_yoy_d1': {'inputs': ['sharesbas', 'marketcap'], 'func': f26_drtj_087_sharesbas_growth_x_marketcap_yoy_d1}, 'f26_drtj_088_dilution_value_to_mcap_4q_d1': {'inputs': ['sharesbas', 'marketcap', 'close'], 'func': f26_drtj_088_dilution_value_to_mcap_4q_d1}, 'f26_drtj_089_dilution_value_to_mcap_8q_d1': {'inputs': ['sharesbas', 'marketcap', 'close'], 'func': f26_drtj_089_dilution_value_to_mcap_8q_d1}, 'f26_drtj_090_ncfcommon_to_ncfi_ttm_d1': {'inputs': ['ncfcommon', 'ncfi'], 'func': f26_drtj_090_ncfcommon_to_ncfi_ttm_d1}, 'f26_drtj_091_buyback_to_dilution_ratio_8q_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_091_buyback_to_dilution_ratio_8q_d1}, 'f26_drtj_092_net_share_change_qoq_pct_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_092_net_share_change_qoq_pct_d1}, 'f26_drtj_093_net_share_change_8q_pct_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_093_net_share_change_8q_pct_d1}, 'f26_drtj_094_buyback_count_8q_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_094_buyback_count_8q_d1}, 'f26_drtj_095_buyback_dollar_8q_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_095_buyback_dollar_8q_d1}, 'f26_drtj_096_share_repurchase_vs_dilution_4q_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_096_share_repurchase_vs_dilution_4q_d1}, 'f26_drtj_097_net_issuance_dollar_8q_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_097_net_issuance_dollar_8q_d1}, 'f26_drtj_098_buyback_streak_break_flag_d1': {'inputs': ['ncfcommon'], 'func': f26_drtj_098_buyback_streak_break_flag_d1}, 'f26_drtj_099_ncfcommon_minus_buybacks_pct_d1': {'inputs': ['ncfcommon', 'marketcap'], 'func': f26_drtj_099_ncfcommon_minus_buybacks_pct_d1}, 'f26_drtj_100_share_issuance_intensity_score_d1': {'inputs': ['ncfcommon', 'marketcap'], 'func': f26_drtj_100_share_issuance_intensity_score_d1}, 'f26_drtj_101_dilution_during_distress_flag_d1': {'inputs': ['sharesbas', 'fcf'], 'func': f26_drtj_101_dilution_during_distress_flag_d1}, 'f26_drtj_102_dilution_during_distress_count_8q_d1': {'inputs': ['sharesbas', 'fcf'], 'func': f26_drtj_102_dilution_during_distress_count_8q_d1}, 'f26_drtj_103_dilution_during_loss_count_8q_d1': {'inputs': ['sharesbas', 'netinc'], 'func': f26_drtj_103_dilution_during_loss_count_8q_d1}, 'f26_drtj_104_dilution_during_burn_8q_d1': {'inputs': ['sharesbas', 'ncfo'], 'func': f26_drtj_104_dilution_during_burn_8q_d1}, 'f26_drtj_105_cumulative_distress_dilution_8q_d1': {'inputs': ['sharesbas', 'fcf'], 'func': f26_drtj_105_cumulative_distress_dilution_8q_d1}, 'f26_drtj_106_dilution_to_cashneq_ratio_d1': {'inputs': ['ncfcommon', 'cashneq'], 'func': f26_drtj_106_dilution_to_cashneq_ratio_d1}, 'f26_drtj_107_dilution_to_runway_ratio_d1': {'inputs': ['ncfcommon', 'fcf', 'cashneq'], 'func': f26_drtj_107_dilution_to_runway_ratio_d1}, 'f26_drtj_108_dilution_replaces_fcf_proxy_d1': {'inputs': ['ncfcommon', 'fcf'], 'func': f26_drtj_108_dilution_replaces_fcf_proxy_d1}, 'f26_drtj_109_dilution_when_pe_high_proxy_d1': {'inputs': ['sharesbas', 'marketcap', 'netinc'], 'func': f26_drtj_109_dilution_when_pe_high_proxy_d1}, 'f26_drtj_110_dilution_efficiency_proxy_d1': {'inputs': ['sharesbas', 'revenue'], 'func': f26_drtj_110_dilution_efficiency_proxy_d1}, 'f26_drtj_111_sharesbas_qoq_volatility_4q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_111_sharesbas_qoq_volatility_4q_d1}, 'f26_drtj_112_sharesbas_qoq_volatility_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_112_sharesbas_qoq_volatility_8q_d1}, 'f26_drtj_113_sharesbas_qoq_volatility_12q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_113_sharesbas_qoq_volatility_12q_d1}, 'f26_drtj_114_dilution_rate_cv_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_114_dilution_rate_cv_8q_d1}, 'f26_drtj_115_dilution_acceleration_4q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_115_dilution_acceleration_4q_d1}, 'f26_drtj_116_dilution_cliff_detector_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_116_dilution_cliff_detector_8q_d1}, 'f26_drtj_117_dilution_jump_detector_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_117_dilution_jump_detector_8q_d1}, 'f26_drtj_118_dilution_regime_break_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_118_dilution_regime_break_8q_d1}, 'f26_drtj_119_dilution_trend_slope_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_119_dilution_trend_slope_8q_d1}, 'f26_drtj_120_dilution_trend_slope_change_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_120_dilution_trend_slope_change_8q_d1}, 'f26_drtj_121_dilution_trend_acceleration_12q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_121_dilution_trend_acceleration_12q_d1}, 'f26_drtj_122_dilution_structural_break_chow_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_122_dilution_structural_break_chow_8q_d1}, 'f26_drtj_123_dilution_log_trend_residual_volatility_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_123_dilution_log_trend_residual_volatility_8q_d1}, 'f26_drtj_124_dilution_rate_smoothed_minus_raw_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_124_dilution_rate_smoothed_minus_raw_d1}, 'f26_drtj_125_dilution_inflection_detector_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_125_dilution_inflection_detector_d1}, 'f26_drtj_126_dilution_inflection_count_12q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_126_dilution_inflection_count_12q_d1}, 'f26_drtj_127_dilution_drawdown_recovery_inverse_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_127_dilution_drawdown_recovery_inverse_d1}, 'f26_drtj_128_sharesbas_above_8q_max_flag_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_128_sharesbas_above_8q_max_flag_d1}, 'f26_drtj_129_sharesbas_above_12q_max_flag_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_129_sharesbas_above_12q_max_flag_d1}, 'f26_drtj_130_sharesbas_above_20q_max_flag_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_130_sharesbas_above_20q_max_flag_d1}, 'f26_drtj_131_dilution_per_revenue_dollar_8q_d1': {'inputs': ['sharesbas', 'revenue'], 'func': f26_drtj_131_dilution_per_revenue_dollar_8q_d1}, 'f26_drtj_132_dilution_per_equity_dollar_8q_d1': {'inputs': ['sharesbas', 'equity'], 'func': f26_drtj_132_dilution_per_equity_dollar_8q_d1}, 'f26_drtj_133_dilution_per_marketcap_dollar_8q_d1': {'inputs': ['sharesbas', 'marketcap'], 'func': f26_drtj_133_dilution_per_marketcap_dollar_8q_d1}, 'f26_drtj_134_sharesbas_yoy_minus_industry_proxy_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_134_sharesbas_yoy_minus_industry_proxy_d1}, 'f26_drtj_135_sharesbas_log_yoy_normalized_by_volatility_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_135_sharesbas_log_yoy_normalized_by_volatility_d1}, 'f26_drtj_136_issuance_episode_intensity_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_136_issuance_episode_intensity_d1}, 'f26_drtj_137_issuance_burst_frequency_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_137_issuance_burst_frequency_d1}, 'f26_drtj_138_dilution_kink_count_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_138_dilution_kink_count_8q_d1}, 'f26_drtj_139_dilution_persistence_score_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_139_dilution_persistence_score_d1}, 'f26_drtj_140_dilution_terminal_signal_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_140_dilution_terminal_signal_d1}, 'f26_drtj_141_dilution_terminal_signal_count_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_141_dilution_terminal_signal_count_8q_d1}, 'f26_drtj_142_sharesbas_log_residual_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_142_sharesbas_log_residual_8q_d1}, 'f26_drtj_143_sharesbas_growth_to_avg_growth_4q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_143_sharesbas_growth_to_avg_growth_4q_d1}, 'f26_drtj_144_sharesbas_acceleration_yoy_4q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_144_sharesbas_acceleration_yoy_4q_d1}, 'f26_drtj_145_sharesbas_growth_step_change_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_145_sharesbas_growth_step_change_8q_d1}, 'f26_drtj_146_sharesbas_qoq_minus_yoy_quarterized_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_146_sharesbas_qoq_minus_yoy_quarterized_d1}, 'f26_drtj_147_sharesbas_growth_smoothed_ema_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_147_sharesbas_growth_smoothed_ema_8q_d1}, 'f26_drtj_148_sharesbas_growth_smoothed_minus_raw_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_148_sharesbas_growth_smoothed_minus_raw_d1}, 'f26_drtj_149_sharesbas_quarterly_pace_zscore_8q_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_149_sharesbas_quarterly_pace_zscore_8q_d1}, 'f26_drtj_150_sharesbas_long_term_dilution_ratio_d1': {'inputs': ['sharesbas'], 'func': f26_drtj_150_sharesbas_long_term_dilution_ratio_d1}}