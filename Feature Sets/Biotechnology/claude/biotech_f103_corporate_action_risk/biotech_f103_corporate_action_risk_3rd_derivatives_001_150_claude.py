"""Family f103 - Corporate action risk from silver DB actions | third derivatives 001-012."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _flag(action, values):
    return globals().get("action_text", action).fillna("").astype(str).str.lower().isin(values).astype(float)


def _contains(action, token):
    return globals().get("action_text", action).fillna("").astype(str).str.lower().str.contains(token, regex=False).astype(float)


def car_f103_corporate_action_risk_bankruptcy_252d_accel_v001_signal(action):
    result = _accel(_sum(_flag(action, {"bankruptcyliquidation"}), 252), 63)
    return _clean(result)


def car_f103_corporate_action_risk_delisting_252d_accel_v002_signal(action):
    base = _sum(_flag(action, {"regulatorydelisting", "voluntarydelisting", "delisted"}), 252)
    result = _accel(base, 63)
    return _clean(result)


def car_f103_corporate_action_risk_distress_504d_accel_v003_signal(action):
    flags = _flag(action, {"bankruptcyliquidation", "regulatorydelisting", "voluntarydelisting", "delisted"})
    result = _accel(_sum(flags, 504), 126)
    return _clean(result)


def car_f103_corporate_action_risk_split_252d_accel_v004_signal(action):
    result = _accel(_sum(_contains(action, "split"), 252), 63)
    return _clean(result)


def car_f103_corporate_action_risk_split_1008d_accel_v005_signal(action):
    result = _accel(_sum(_contains(action, "split"), 1008), 252)
    return _clean(result)


def car_f103_corporate_action_risk_ticker_change_252d_accel_v006_signal(action):
    result = _accel(_sum(_contains(action, "tickerchange"), 252), 63)
    return _clean(result)


def car_f103_corporate_action_risk_ticker_change_1008d_accel_v007_signal(action):
    result = _accel(_sum(_contains(action, "tickerchange"), 1008), 252)
    return _clean(result)


def car_f103_corporate_action_risk_acquisition_504d_accel_v008_signal(action):
    result = _accel(_sum(_contains(action, "acquisition"), 504), 126)
    return _clean(result)


def car_f103_corporate_action_risk_spinoff_504d_accel_v009_signal(action):
    result = _accel(_sum(_contains(action, "spinoff"), 504), 126)
    return _clean(result)


def car_f103_corporate_action_risk_non_dividend_density_252d_accel_v010_signal(action):
    text = action.fillna("").astype(str).str.lower()
    base = _sum((text.ne("") & text.ne("dividend")).astype(float), 252)
    result = _accel(base, 63)
    return _clean(result)


def car_f103_corporate_action_risk_action_value_252d_accel_v011_signal(action, value):
    text = action.fillna("").astype(str).str.lower()
    result = _accel(_sum(value.where(text.ne("dividend")).abs(), 252), 63)
    return _clean(result)


def car_f103_corporate_action_risk_identity_instability_252d_accel_v012_signal(action):
    result = _accel(_sum(_contains(action, "tickerchange") + _contains(action, "split"), 252), 63)
    return _clean(result)
