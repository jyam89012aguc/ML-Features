import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f12_volume_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f12_growth_acceleration(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f12_growth_durability(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return rg * eg

def f12dtv_f12_diagnostics_test_volume_growth_accema_126d_base_v076_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accema_189d_base_v077_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 189)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accema_252d_base_v078_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 252)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accema_378d_base_v079_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 378)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accema_504d_base_v080_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 504)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_5d_base_v081_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 5)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_10d_base_v082_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 10)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_21d_base_v083_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_42d_base_v084_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_63d_base_v085_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_126d_base_v086_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_189d_base_v087_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_252d_base_v088_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_378d_base_v089_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 378)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_dursq_504d_base_v090_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 504)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_5d_base_v091_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_10d_base_v092_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_21d_base_v093_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_42d_base_v094_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 42)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_63d_base_v095_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_126d_base_v096_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_189d_base_v097_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 189)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_252d_base_v098_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_378d_base_v099_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_durmean_504d_base_v100_signal(revenue, ebitda, closeadj):
    base = _f12_growth_durability(revenue, ebitda, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_5d_base_v101_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 5)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_10d_base_v102_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 10)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_21d_base_v103_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 21)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_42d_base_v104_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 42)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_63d_base_v105_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_126d_base_v106_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 126)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_189d_base_v107_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 189)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_252d_base_v108_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_378d_base_v109_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 378)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwlog_504d_base_v110_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 504)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_5d_base_v111_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 5)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_10d_base_v112_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 10)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_21d_base_v113_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 21)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_42d_base_v114_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 42)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_63d_base_v115_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_126d_base_v116_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 126)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_189d_base_v117_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 189)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_252d_base_v118_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_378d_base_v119_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 378)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxlog_504d_base_v120_signal(revenue, closeadj):
    base = _f12_growth_acceleration(revenue, 504)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_5d_base_v121_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 5)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_10d_base_v122_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 10)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_21d_base_v123_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 21)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_42d_base_v124_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 42)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_63d_base_v125_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 63)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_126d_base_v126_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 126)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_189d_base_v127_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 189)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_252d_base_v128_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 252)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_378d_base_v129_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 378)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwxebir_504d_base_v130_signal(revenue, ebitda, closeadj):
    base = _f12_volume_growth(revenue, 504)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_5d_base_v131_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 5)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_10d_base_v132_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 10)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_21d_base_v133_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 21)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_42d_base_v134_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 42)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_63d_base_v135_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 63)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_126d_base_v136_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 126)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_189d_base_v137_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 189)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_252d_base_v138_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 252)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_378d_base_v139_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 378)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_accxebir_504d_base_v140_signal(revenue, ebitda, closeadj):
    base = _f12_growth_acceleration(revenue, 504)
    ratio = ebitda / revenue.replace(0, np.nan).abs()
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_5d_base_v141_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 5)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_10d_base_v142_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 10)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_21d_base_v143_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_42d_base_v144_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_63d_base_v145_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_126d_base_v146_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_189d_base_v147_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_252d_base_v148_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_378d_base_v149_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 378)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12dtv_f12_diagnostics_test_volume_growth_grwsq_504d_base_v150_signal(revenue, closeadj):
    base = _f12_volume_growth(revenue, 504)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12dtv_f12_diagnostics_test_volume_growth_accema_126d_base_v076_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accema_189d_base_v077_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accema_252d_base_v078_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accema_378d_base_v079_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accema_504d_base_v080_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_5d_base_v081_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_10d_base_v082_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_21d_base_v083_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_42d_base_v084_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_63d_base_v085_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_126d_base_v086_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_189d_base_v087_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_252d_base_v088_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_378d_base_v089_signal,
    f12dtv_f12_diagnostics_test_volume_growth_dursq_504d_base_v090_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_5d_base_v091_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_10d_base_v092_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_21d_base_v093_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_42d_base_v094_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_63d_base_v095_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_126d_base_v096_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_189d_base_v097_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_252d_base_v098_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_378d_base_v099_signal,
    f12dtv_f12_diagnostics_test_volume_growth_durmean_504d_base_v100_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_5d_base_v101_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_10d_base_v102_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_21d_base_v103_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_42d_base_v104_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_63d_base_v105_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_126d_base_v106_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_189d_base_v107_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_252d_base_v108_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_378d_base_v109_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwlog_504d_base_v110_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_5d_base_v111_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_10d_base_v112_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_21d_base_v113_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_42d_base_v114_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_63d_base_v115_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_126d_base_v116_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_189d_base_v117_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_252d_base_v118_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_378d_base_v119_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxlog_504d_base_v120_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_5d_base_v121_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_10d_base_v122_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_21d_base_v123_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_42d_base_v124_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_63d_base_v125_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_126d_base_v126_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_189d_base_v127_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_252d_base_v128_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_378d_base_v129_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwxebir_504d_base_v130_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_5d_base_v131_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_10d_base_v132_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_21d_base_v133_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_42d_base_v134_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_63d_base_v135_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_126d_base_v136_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_189d_base_v137_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_252d_base_v138_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_378d_base_v139_signal,
    f12dtv_f12_diagnostics_test_volume_growth_accxebir_504d_base_v140_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_5d_base_v141_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_10d_base_v142_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_21d_base_v143_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_42d_base_v144_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_63d_base_v145_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_126d_base_v146_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_189d_base_v147_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_252d_base_v148_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_378d_base_v149_signal,
    f12dtv_f12_diagnostics_test_volume_growth_grwsq_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_DIAGNOSTICS_TEST_VOLUME_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_volume_growth", "_f12_growth_acceleration", "_f12_growth_durability",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f12_diagnostics_test_volume_growth_base_076_150_claude: {n_features} features pass")
