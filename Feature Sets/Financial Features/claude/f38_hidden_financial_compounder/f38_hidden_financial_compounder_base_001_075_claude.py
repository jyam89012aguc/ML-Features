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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()

# ===== folder domain primitives =====
def _f38_undervalued_proxy(pb, w):
    m = pb.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m - pb) * pb


def _f38_low_attention_growth(volume, eps, w):
    inv_attn = _safe_div(eps, volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))
    return inv_attn * volume


def _f38_hidden_compounder_score(pb, roe, w):
    m = pb.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m - pb) * roe * pb

def f38hfc_f38_hidden_financial_compounder_undervp_5d_base_v001_signal(pb):
    result = _f38_undervalued_proxy(pb, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_10d_base_v002_signal(pb):
    result = _f38_undervalued_proxy(pb, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_21d_base_v003_signal(pb):
    result = _f38_undervalued_proxy(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_42d_base_v004_signal(pb):
    result = _f38_undervalued_proxy(pb, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_63d_base_v005_signal(pb):
    result = _f38_undervalued_proxy(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_126d_base_v006_signal(pb):
    result = _f38_undervalued_proxy(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_189d_base_v007_signal(pb):
    result = _f38_undervalued_proxy(pb, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_252d_base_v008_signal(pb):
    result = _f38_undervalued_proxy(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_378d_base_v009_signal(pb):
    result = _f38_undervalued_proxy(pb, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervp_504d_base_v010_signal(pb):
    result = _f38_undervalued_proxy(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_5d_base_v011_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_10d_base_v012_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_21d_base_v013_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_42d_base_v014_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_63d_base_v015_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_126d_base_v016_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_189d_base_v017_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_252d_base_v018_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_378d_base_v019_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loaattn_504d_base_v020_signal(volume, eps):
    result = _f38_low_attention_growth(volume, eps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_5d_base_v021_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_10d_base_v022_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_21d_base_v023_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_42d_base_v024_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_63d_base_v025_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_126d_base_v026_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_189d_base_v027_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_252d_base_v028_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_378d_base_v029_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidcomp_504d_base_v030_signal(pb, roe):
    result = _f38_hidden_compounder_score(pb, roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxca_21d_base_v031_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxca_63d_base_v032_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxca_126d_base_v033_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxca_252d_base_v034_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervema_21d_base_v035_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervema_63d_base_v036_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervema_126d_base_v037_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervema_252d_base_v038_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervz_21d_base_v039_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervz_63d_base_v040_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervz_126d_base_v041_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervz_252d_base_v042_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loxca_21d_base_v043_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loxca_63d_base_v044_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loxca_126d_base_v045_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loxca_252d_base_v046_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loz_21d_base_v047_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loz_63d_base_v048_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loz_126d_base_v049_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_loz_252d_base_v050_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxca_21d_base_v051_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxca_63d_base_v052_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxca_126d_base_v053_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxca_252d_base_v054_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidz_21d_base_v055_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidz_63d_base_v056_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidz_126d_base_v057_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidz_252d_base_v058_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxvol_21d_base_v059_signal(pb, volume, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxvol_63d_base_v060_signal(pb, volume, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxvol_126d_base_v061_signal(pb, volume, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervxvol_252d_base_v062_signal(pb, volume, closeadj):
    base = _f38_undervalued_proxy(pb, 252)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxvol_21d_base_v063_signal(pb, roe, volume, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxvol_63d_base_v064_signal(pb, roe, volume, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxvol_126d_base_v065_signal(pb, roe, volume, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidxvol_252d_base_v066_signal(pb, roe, volume, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 252)
    result = base * _mean(volume, 21) / 1e6 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstd_21d_base_v067_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstd_63d_base_v068_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_undervstd_126d_base_v069_signal(pb, closeadj):
    base = _f38_undervalued_proxy(pb, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdA_21d_base_v070_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdA_63d_base_v071_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_hidstdA_126d_base_v072_signal(pb, roe, closeadj):
    base = _f38_hidden_compounder_score(pb, roe, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lostd_21d_base_v073_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 21)
    result = _std(base, 21) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lostd_63d_base_v074_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 63)
    result = _std(base, 63) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hfc_f38_hidden_financial_compounder_lostd_126d_base_v075_signal(volume, eps, closeadj):
    base = _f38_low_attention_growth(volume, eps, 126)
    result = _std(base, 126) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hfc_f38_hidden_financial_compounder_undervp_5d_base_v001_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_10d_base_v002_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_21d_base_v003_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_42d_base_v004_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_63d_base_v005_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_126d_base_v006_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_189d_base_v007_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_252d_base_v008_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_378d_base_v009_signal,
    f38hfc_f38_hidden_financial_compounder_undervp_504d_base_v010_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_5d_base_v011_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_10d_base_v012_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_21d_base_v013_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_42d_base_v014_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_63d_base_v015_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_126d_base_v016_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_189d_base_v017_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_252d_base_v018_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_378d_base_v019_signal,
    f38hfc_f38_hidden_financial_compounder_loaattn_504d_base_v020_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_5d_base_v021_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_10d_base_v022_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_21d_base_v023_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_42d_base_v024_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_63d_base_v025_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_126d_base_v026_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_189d_base_v027_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_252d_base_v028_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_378d_base_v029_signal,
    f38hfc_f38_hidden_financial_compounder_hidcomp_504d_base_v030_signal,
    f38hfc_f38_hidden_financial_compounder_undervxca_21d_base_v031_signal,
    f38hfc_f38_hidden_financial_compounder_undervxca_63d_base_v032_signal,
    f38hfc_f38_hidden_financial_compounder_undervxca_126d_base_v033_signal,
    f38hfc_f38_hidden_financial_compounder_undervxca_252d_base_v034_signal,
    f38hfc_f38_hidden_financial_compounder_undervema_21d_base_v035_signal,
    f38hfc_f38_hidden_financial_compounder_undervema_63d_base_v036_signal,
    f38hfc_f38_hidden_financial_compounder_undervema_126d_base_v037_signal,
    f38hfc_f38_hidden_financial_compounder_undervema_252d_base_v038_signal,
    f38hfc_f38_hidden_financial_compounder_undervz_21d_base_v039_signal,
    f38hfc_f38_hidden_financial_compounder_undervz_63d_base_v040_signal,
    f38hfc_f38_hidden_financial_compounder_undervz_126d_base_v041_signal,
    f38hfc_f38_hidden_financial_compounder_undervz_252d_base_v042_signal,
    f38hfc_f38_hidden_financial_compounder_loxca_21d_base_v043_signal,
    f38hfc_f38_hidden_financial_compounder_loxca_63d_base_v044_signal,
    f38hfc_f38_hidden_financial_compounder_loxca_126d_base_v045_signal,
    f38hfc_f38_hidden_financial_compounder_loxca_252d_base_v046_signal,
    f38hfc_f38_hidden_financial_compounder_loz_21d_base_v047_signal,
    f38hfc_f38_hidden_financial_compounder_loz_63d_base_v048_signal,
    f38hfc_f38_hidden_financial_compounder_loz_126d_base_v049_signal,
    f38hfc_f38_hidden_financial_compounder_loz_252d_base_v050_signal,
    f38hfc_f38_hidden_financial_compounder_hidxca_21d_base_v051_signal,
    f38hfc_f38_hidden_financial_compounder_hidxca_63d_base_v052_signal,
    f38hfc_f38_hidden_financial_compounder_hidxca_126d_base_v053_signal,
    f38hfc_f38_hidden_financial_compounder_hidxca_252d_base_v054_signal,
    f38hfc_f38_hidden_financial_compounder_hidz_21d_base_v055_signal,
    f38hfc_f38_hidden_financial_compounder_hidz_63d_base_v056_signal,
    f38hfc_f38_hidden_financial_compounder_hidz_126d_base_v057_signal,
    f38hfc_f38_hidden_financial_compounder_hidz_252d_base_v058_signal,
    f38hfc_f38_hidden_financial_compounder_undervxvol_21d_base_v059_signal,
    f38hfc_f38_hidden_financial_compounder_undervxvol_63d_base_v060_signal,
    f38hfc_f38_hidden_financial_compounder_undervxvol_126d_base_v061_signal,
    f38hfc_f38_hidden_financial_compounder_undervxvol_252d_base_v062_signal,
    f38hfc_f38_hidden_financial_compounder_hidxvol_21d_base_v063_signal,
    f38hfc_f38_hidden_financial_compounder_hidxvol_63d_base_v064_signal,
    f38hfc_f38_hidden_financial_compounder_hidxvol_126d_base_v065_signal,
    f38hfc_f38_hidden_financial_compounder_hidxvol_252d_base_v066_signal,
    f38hfc_f38_hidden_financial_compounder_undervstd_21d_base_v067_signal,
    f38hfc_f38_hidden_financial_compounder_undervstd_63d_base_v068_signal,
    f38hfc_f38_hidden_financial_compounder_undervstd_126d_base_v069_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdA_21d_base_v070_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdA_63d_base_v071_signal,
    f38hfc_f38_hidden_financial_compounder_hidstdA_126d_base_v072_signal,
    f38hfc_f38_hidden_financial_compounder_lostd_21d_base_v073_signal,
    f38hfc_f38_hidden_financial_compounder_lostd_63d_base_v074_signal,
    f38hfc_f38_hidden_financial_compounder_lostd_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_HIDDEN_FINANCIAL_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f38_undervalued_proxy", "_f38_low_attention_growth", "_f38_hidden_compounder_score")
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
    print(f"OK f38_hidden_financial_compounder_base_001_075_claude: {n_features} features pass")
