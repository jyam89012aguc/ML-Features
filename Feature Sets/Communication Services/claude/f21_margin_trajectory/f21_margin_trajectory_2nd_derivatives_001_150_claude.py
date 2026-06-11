import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

ALLOWLIST = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
    "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
    "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
    "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
    "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
    "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
    "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
    "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
    "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
    "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx * idx).sum())

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum()) / denom
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ==========================================================

# slope of 'gm' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gm_rawdiff_021d_slope_v001_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (rawdiff,21d)
def f21mt_f21_margin_trajectory_nm_rawdiff_021d_slope_v002_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (rawdiff,21d)
def f21mt_f21_margin_trajectory_em_rawdiff_021d_slope_v003_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (rawdiff,21d)
def f21mt_f21_margin_trajectory_om_rawdiff_021d_slope_v004_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_021d_slope_v005_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_021d_slope_v006_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_021d_slope_v007_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_021d_slope_v008_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_021d_slope_v009_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_021d_slope_v010_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_021d_slope_v011_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gosp_rawdiff_021d_slope_v012_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_021d_slope_v013_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_021d_slope_v014_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (rawdiff,21d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_021d_slope_v015_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gm_rawdiff_042d_slope_v016_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (rawdiff,42d)
def f21mt_f21_margin_trajectory_nm_rawdiff_042d_slope_v017_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (rawdiff,42d)
def f21mt_f21_margin_trajectory_em_rawdiff_042d_slope_v018_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (rawdiff,42d)
def f21mt_f21_margin_trajectory_om_rawdiff_042d_slope_v019_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_042d_slope_v020_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_042d_slope_v021_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_042d_slope_v022_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_042d_slope_v023_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_042d_slope_v024_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_042d_slope_v025_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_042d_slope_v026_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gosp_rawdiff_042d_slope_v027_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_042d_slope_v028_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_042d_slope_v029_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (rawdiff,42d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_042d_slope_v030_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gm_rawdiff_063d_slope_v031_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (rawdiff,63d)
def f21mt_f21_margin_trajectory_nm_rawdiff_063d_slope_v032_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (rawdiff,63d)
def f21mt_f21_margin_trajectory_em_rawdiff_063d_slope_v033_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_063d_slope_v034_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_063d_slope_v035_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_063d_slope_v036_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_063d_slope_v037_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (rawdiff,63d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_063d_slope_v038_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_063d_slope_v039_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_063d_slope_v040_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gosp_rawdiff_063d_slope_v041_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_063d_slope_v042_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (rawdiff,63d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_063d_slope_v043_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gm_rawdiff_126d_slope_v044_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (rawdiff,126d)
def f21mt_f21_margin_trajectory_nm_rawdiff_126d_slope_v045_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (rawdiff,126d)
def f21mt_f21_margin_trajectory_em_rawdiff_126d_slope_v046_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (rawdiff,126d)
def f21mt_f21_margin_trajectory_om_rawdiff_126d_slope_v047_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_126d_slope_v048_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_126d_slope_v049_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_126d_slope_v050_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_126d_slope_v051_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_126d_slope_v052_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_126d_slope_v053_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gosp_rawdiff_126d_slope_v054_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_126d_slope_v055_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_126d_slope_v056_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gm_rawdiff_252d_slope_v057_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (rawdiff,252d)
def f21mt_f21_margin_trajectory_nm_rawdiff_252d_slope_v058_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (rawdiff,252d)
def f21mt_f21_margin_trajectory_em_rawdiff_252d_slope_v059_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (rawdiff,252d)
def f21mt_f21_margin_trajectory_om_rawdiff_252d_slope_v060_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_252d_slope_v061_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_252d_slope_v062_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_252d_slope_v063_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_252d_slope_v064_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_252d_slope_v065_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_252d_slope_v066_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_252d_slope_v067_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (ols,126d)
def f21mt_f21_margin_trajectory_nm_ols_126d_slope_v068_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (ols,126d)
def f21mt_f21_margin_trajectory_em_ols_126d_slope_v069_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (ols,126d)
def f21mt_f21_margin_trajectory_gesp_ols_126d_slope_v070_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (ols,126d)
def f21mt_f21_margin_trajectory_oesp_ols_126d_slope_v071_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (ols,126d)
def f21mt_f21_margin_trajectory_gpdoll_ols_126d_slope_v072_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (ols,252d)
def f21mt_f21_margin_trajectory_gm_ols_252d_slope_v073_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (ols,252d)
def f21mt_f21_margin_trajectory_nm_ols_252d_slope_v074_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (ols,252d)
def f21mt_f21_margin_trajectory_em_ols_252d_slope_v075_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (ols,252d)
def f21mt_f21_margin_trajectory_om_ols_252d_slope_v076_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (ols,252d)
def f21mt_f21_margin_trajectory_gnsp_ols_252d_slope_v077_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (ols,252d)
def f21mt_f21_margin_trajectory_gnconv_ols_252d_slope_v078_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (ols,252d)
def f21mt_f21_margin_trajectory_geconv_ols_252d_slope_v079_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'enconv' (ols,252d)
def f21mt_f21_margin_trajectory_enconv_ols_252d_slope_v080_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (ols,252d)
def f21mt_f21_margin_trajectory_onsp_ols_252d_slope_v081_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (ols,252d)
def f21mt_f21_margin_trajectory_oesp_ols_252d_slope_v082_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (ols,252d)
def f21mt_f21_margin_trajectory_gpdoll_ols_252d_slope_v083_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (snr,21d)
def f21mt_f21_margin_trajectory_gm_snr_021d_slope_v084_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (snr,21d)
def f21mt_f21_margin_trajectory_nm_snr_021d_slope_v085_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (snr,21d)
def f21mt_f21_margin_trajectory_em_snr_021d_slope_v086_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (snr,21d)
def f21mt_f21_margin_trajectory_om_snr_021d_slope_v087_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (snr,21d)
def f21mt_f21_margin_trajectory_gnsp_snr_021d_slope_v088_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (snr,21d)
def f21mt_f21_margin_trajectory_gesp_snr_021d_slope_v089_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (snr,21d)
def f21mt_f21_margin_trajectory_ensp_snr_021d_slope_v090_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (snr,21d)
def f21mt_f21_margin_trajectory_gnconv_snr_021d_slope_v091_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (snr,21d)
def f21mt_f21_margin_trajectory_geconv_snr_021d_slope_v092_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'enconv' (snr,21d)
def f21mt_f21_margin_trajectory_enconv_snr_021d_slope_v093_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (snr,21d)
def f21mt_f21_margin_trajectory_onsp_snr_021d_slope_v094_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (snr,21d)
def f21mt_f21_margin_trajectory_oesp_snr_021d_slope_v095_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (snr,21d)
def f21mt_f21_margin_trajectory_gosp_snr_021d_slope_v096_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (snr,21d)
def f21mt_f21_margin_trajectory_ogconv_snr_021d_slope_v097_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (snr,21d)
def f21mt_f21_margin_trajectory_gpdoll_snr_021d_slope_v098_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'emrev' (snr,21d)
def f21mt_f21_margin_trajectory_emrev_snr_021d_slope_v099_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gmrev' (snr,21d)
def f21mt_f21_margin_trajectory_gmrev_snr_021d_slope_v100_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (snr,21d)
def f21mt_f21_margin_trajectory_profmin_snr_021d_slope_v101_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (snr,42d)
def f21mt_f21_margin_trajectory_gm_snr_042d_slope_v102_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (snr,42d)
def f21mt_f21_margin_trajectory_nm_snr_042d_slope_v103_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (snr,42d)
def f21mt_f21_margin_trajectory_em_snr_042d_slope_v104_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (snr,42d)
def f21mt_f21_margin_trajectory_om_snr_042d_slope_v105_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (snr,42d)
def f21mt_f21_margin_trajectory_gnsp_snr_042d_slope_v106_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (snr,42d)
def f21mt_f21_margin_trajectory_gesp_snr_042d_slope_v107_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (snr,42d)
def f21mt_f21_margin_trajectory_ensp_snr_042d_slope_v108_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (snr,42d)
def f21mt_f21_margin_trajectory_gnconv_snr_042d_slope_v109_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (snr,42d)
def f21mt_f21_margin_trajectory_geconv_snr_042d_slope_v110_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'enconv' (snr,42d)
def f21mt_f21_margin_trajectory_enconv_snr_042d_slope_v111_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (snr,42d)
def f21mt_f21_margin_trajectory_onsp_snr_042d_slope_v112_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (snr,42d)
def f21mt_f21_margin_trajectory_oesp_snr_042d_slope_v113_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (snr,42d)
def f21mt_f21_margin_trajectory_gosp_snr_042d_slope_v114_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (snr,42d)
def f21mt_f21_margin_trajectory_ogconv_snr_042d_slope_v115_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (snr,42d)
def f21mt_f21_margin_trajectory_gpdoll_snr_042d_slope_v116_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'emrev' (snr,42d)
def f21mt_f21_margin_trajectory_emrev_snr_042d_slope_v117_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gmrev' (snr,42d)
def f21mt_f21_margin_trajectory_gmrev_snr_042d_slope_v118_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (snr,42d)
def f21mt_f21_margin_trajectory_profmin_snr_042d_slope_v119_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (snr,63d)
def f21mt_f21_margin_trajectory_gm_snr_063d_slope_v120_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (snr,63d)
def f21mt_f21_margin_trajectory_nm_snr_063d_slope_v121_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (snr,63d)
def f21mt_f21_margin_trajectory_em_snr_063d_slope_v122_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (snr,63d)
def f21mt_f21_margin_trajectory_gnsp_snr_063d_slope_v123_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (snr,63d)
def f21mt_f21_margin_trajectory_gesp_snr_063d_slope_v124_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (snr,63d)
def f21mt_f21_margin_trajectory_ensp_snr_063d_slope_v125_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (snr,63d)
def f21mt_f21_margin_trajectory_gnconv_snr_063d_slope_v126_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (snr,63d)
def f21mt_f21_margin_trajectory_geconv_snr_063d_slope_v127_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'enconv' (snr,63d)
def f21mt_f21_margin_trajectory_enconv_snr_063d_slope_v128_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (snr,63d)
def f21mt_f21_margin_trajectory_onsp_snr_063d_slope_v129_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (snr,63d)
def f21mt_f21_margin_trajectory_oesp_snr_063d_slope_v130_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (snr,63d)
def f21mt_f21_margin_trajectory_gosp_snr_063d_slope_v131_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (snr,63d)
def f21mt_f21_margin_trajectory_ogconv_snr_063d_slope_v132_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (snr,63d)
def f21mt_f21_margin_trajectory_gpdoll_snr_063d_slope_v133_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'emrev' (snr,63d)
def f21mt_f21_margin_trajectory_emrev_snr_063d_slope_v134_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gmrev' (snr,63d)
def f21mt_f21_margin_trajectory_gmrev_snr_063d_slope_v135_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'profmin' (snr,63d)
def f21mt_f21_margin_trajectory_profmin_snr_063d_slope_v136_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gm' (snr,126d)
def f21mt_f21_margin_trajectory_gm_snr_126d_slope_v137_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'nm' (snr,126d)
def f21mt_f21_margin_trajectory_nm_snr_126d_slope_v138_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'em' (snr,126d)
def f21mt_f21_margin_trajectory_em_snr_126d_slope_v139_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'om' (snr,126d)
def f21mt_f21_margin_trajectory_om_snr_126d_slope_v140_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnsp' (snr,126d)
def f21mt_f21_margin_trajectory_gnsp_snr_126d_slope_v141_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gesp' (snr,126d)
def f21mt_f21_margin_trajectory_gesp_snr_126d_slope_v142_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ensp' (snr,126d)
def f21mt_f21_margin_trajectory_ensp_snr_126d_slope_v143_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gnconv' (snr,126d)
def f21mt_f21_margin_trajectory_gnconv_snr_126d_slope_v144_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'geconv' (snr,126d)
def f21mt_f21_margin_trajectory_geconv_snr_126d_slope_v145_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'onsp' (snr,126d)
def f21mt_f21_margin_trajectory_onsp_snr_126d_slope_v146_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'oesp' (snr,126d)
def f21mt_f21_margin_trajectory_oesp_snr_126d_slope_v147_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gosp' (snr,126d)
def f21mt_f21_margin_trajectory_gosp_snr_126d_slope_v148_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'ogconv' (snr,126d)
def f21mt_f21_margin_trajectory_ogconv_snr_126d_slope_v149_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 'gpdoll' (snr,126d)
def f21mt_f21_margin_trajectory_gpdoll_snr_126d_slope_v150_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f21mt_f21_margin_trajectory_gm_rawdiff_021d_slope_v001_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_021d_slope_v002_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_021d_slope_v003_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_021d_slope_v004_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_021d_slope_v005_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_021d_slope_v006_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_021d_slope_v007_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_021d_slope_v008_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_021d_slope_v009_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_021d_slope_v010_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_021d_slope_v011_signal,
    f21mt_f21_margin_trajectory_gosp_rawdiff_021d_slope_v012_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_021d_slope_v013_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_021d_slope_v014_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_021d_slope_v015_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_042d_slope_v016_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_042d_slope_v017_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_042d_slope_v018_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_042d_slope_v019_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_042d_slope_v020_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_042d_slope_v021_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_042d_slope_v022_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_042d_slope_v023_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_042d_slope_v024_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_042d_slope_v025_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_042d_slope_v026_signal,
    f21mt_f21_margin_trajectory_gosp_rawdiff_042d_slope_v027_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_042d_slope_v028_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_042d_slope_v029_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_042d_slope_v030_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_063d_slope_v031_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_063d_slope_v032_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_063d_slope_v033_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_063d_slope_v034_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_063d_slope_v035_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_063d_slope_v036_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_063d_slope_v037_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_063d_slope_v038_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_063d_slope_v039_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_063d_slope_v040_signal,
    f21mt_f21_margin_trajectory_gosp_rawdiff_063d_slope_v041_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_063d_slope_v042_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_063d_slope_v043_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_126d_slope_v044_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_126d_slope_v045_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_126d_slope_v046_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_126d_slope_v047_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_126d_slope_v048_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_126d_slope_v049_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_126d_slope_v050_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_126d_slope_v051_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_126d_slope_v052_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_126d_slope_v053_signal,
    f21mt_f21_margin_trajectory_gosp_rawdiff_126d_slope_v054_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_126d_slope_v055_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_126d_slope_v056_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_252d_slope_v057_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_252d_slope_v058_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_252d_slope_v059_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_252d_slope_v060_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_252d_slope_v061_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_252d_slope_v062_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_252d_slope_v063_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_252d_slope_v064_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_252d_slope_v065_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_252d_slope_v066_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_252d_slope_v067_signal,
    f21mt_f21_margin_trajectory_nm_ols_126d_slope_v068_signal,
    f21mt_f21_margin_trajectory_em_ols_126d_slope_v069_signal,
    f21mt_f21_margin_trajectory_gesp_ols_126d_slope_v070_signal,
    f21mt_f21_margin_trajectory_oesp_ols_126d_slope_v071_signal,
    f21mt_f21_margin_trajectory_gpdoll_ols_126d_slope_v072_signal,
    f21mt_f21_margin_trajectory_gm_ols_252d_slope_v073_signal,
    f21mt_f21_margin_trajectory_nm_ols_252d_slope_v074_signal,
    f21mt_f21_margin_trajectory_em_ols_252d_slope_v075_signal,
    f21mt_f21_margin_trajectory_om_ols_252d_slope_v076_signal,
    f21mt_f21_margin_trajectory_gnsp_ols_252d_slope_v077_signal,
    f21mt_f21_margin_trajectory_gnconv_ols_252d_slope_v078_signal,
    f21mt_f21_margin_trajectory_geconv_ols_252d_slope_v079_signal,
    f21mt_f21_margin_trajectory_enconv_ols_252d_slope_v080_signal,
    f21mt_f21_margin_trajectory_onsp_ols_252d_slope_v081_signal,
    f21mt_f21_margin_trajectory_oesp_ols_252d_slope_v082_signal,
    f21mt_f21_margin_trajectory_gpdoll_ols_252d_slope_v083_signal,
    f21mt_f21_margin_trajectory_gm_snr_021d_slope_v084_signal,
    f21mt_f21_margin_trajectory_nm_snr_021d_slope_v085_signal,
    f21mt_f21_margin_trajectory_em_snr_021d_slope_v086_signal,
    f21mt_f21_margin_trajectory_om_snr_021d_slope_v087_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_021d_slope_v088_signal,
    f21mt_f21_margin_trajectory_gesp_snr_021d_slope_v089_signal,
    f21mt_f21_margin_trajectory_ensp_snr_021d_slope_v090_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_021d_slope_v091_signal,
    f21mt_f21_margin_trajectory_geconv_snr_021d_slope_v092_signal,
    f21mt_f21_margin_trajectory_enconv_snr_021d_slope_v093_signal,
    f21mt_f21_margin_trajectory_onsp_snr_021d_slope_v094_signal,
    f21mt_f21_margin_trajectory_oesp_snr_021d_slope_v095_signal,
    f21mt_f21_margin_trajectory_gosp_snr_021d_slope_v096_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_021d_slope_v097_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_021d_slope_v098_signal,
    f21mt_f21_margin_trajectory_emrev_snr_021d_slope_v099_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_021d_slope_v100_signal,
    f21mt_f21_margin_trajectory_profmin_snr_021d_slope_v101_signal,
    f21mt_f21_margin_trajectory_gm_snr_042d_slope_v102_signal,
    f21mt_f21_margin_trajectory_nm_snr_042d_slope_v103_signal,
    f21mt_f21_margin_trajectory_em_snr_042d_slope_v104_signal,
    f21mt_f21_margin_trajectory_om_snr_042d_slope_v105_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_042d_slope_v106_signal,
    f21mt_f21_margin_trajectory_gesp_snr_042d_slope_v107_signal,
    f21mt_f21_margin_trajectory_ensp_snr_042d_slope_v108_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_042d_slope_v109_signal,
    f21mt_f21_margin_trajectory_geconv_snr_042d_slope_v110_signal,
    f21mt_f21_margin_trajectory_enconv_snr_042d_slope_v111_signal,
    f21mt_f21_margin_trajectory_onsp_snr_042d_slope_v112_signal,
    f21mt_f21_margin_trajectory_oesp_snr_042d_slope_v113_signal,
    f21mt_f21_margin_trajectory_gosp_snr_042d_slope_v114_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_042d_slope_v115_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_042d_slope_v116_signal,
    f21mt_f21_margin_trajectory_emrev_snr_042d_slope_v117_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_042d_slope_v118_signal,
    f21mt_f21_margin_trajectory_profmin_snr_042d_slope_v119_signal,
    f21mt_f21_margin_trajectory_gm_snr_063d_slope_v120_signal,
    f21mt_f21_margin_trajectory_nm_snr_063d_slope_v121_signal,
    f21mt_f21_margin_trajectory_em_snr_063d_slope_v122_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_063d_slope_v123_signal,
    f21mt_f21_margin_trajectory_gesp_snr_063d_slope_v124_signal,
    f21mt_f21_margin_trajectory_ensp_snr_063d_slope_v125_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_063d_slope_v126_signal,
    f21mt_f21_margin_trajectory_geconv_snr_063d_slope_v127_signal,
    f21mt_f21_margin_trajectory_enconv_snr_063d_slope_v128_signal,
    f21mt_f21_margin_trajectory_onsp_snr_063d_slope_v129_signal,
    f21mt_f21_margin_trajectory_oesp_snr_063d_slope_v130_signal,
    f21mt_f21_margin_trajectory_gosp_snr_063d_slope_v131_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_063d_slope_v132_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_063d_slope_v133_signal,
    f21mt_f21_margin_trajectory_emrev_snr_063d_slope_v134_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_063d_slope_v135_signal,
    f21mt_f21_margin_trajectory_profmin_snr_063d_slope_v136_signal,
    f21mt_f21_margin_trajectory_gm_snr_126d_slope_v137_signal,
    f21mt_f21_margin_trajectory_nm_snr_126d_slope_v138_signal,
    f21mt_f21_margin_trajectory_em_snr_126d_slope_v139_signal,
    f21mt_f21_margin_trajectory_om_snr_126d_slope_v140_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_126d_slope_v141_signal,
    f21mt_f21_margin_trajectory_gesp_snr_126d_slope_v142_signal,
    f21mt_f21_margin_trajectory_ensp_snr_126d_slope_v143_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_126d_slope_v144_signal,
    f21mt_f21_margin_trajectory_geconv_snr_126d_slope_v145_signal,
    f21mt_f21_margin_trajectory_onsp_snr_126d_slope_v146_signal,
    f21mt_f21_margin_trajectory_oesp_snr_126d_slope_v147_signal,
    f21mt_f21_margin_trajectory_gosp_snr_126d_slope_v148_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_126d_slope_v149_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_MARGIN_TRAJECTORY_REGISTRY_001_150 = REGISTRY


def _build_inputs(n=1500):
    np.random.seed(42)

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    grossmargin = _fund(101, base=0.45, drift=0.0, vol=0.05).clip(0.05, 0.85).rename("grossmargin")
    netmargin = _fund(102, base=0.12, drift=0.0, vol=0.06).clip(-0.2, 0.5).rename("netmargin")
    ebitdamargin = _fund(103, base=0.22, drift=0.0, vol=0.05).clip(-0.1, 0.6).rename("ebitdamargin")
    revenue = _fund(104, base=1.5e8, drift=0.03, vol=0.06).rename("revenue")
    gp = (revenue * grossmargin).rename("gp")
    opinc = _fund(106, base=2.0e7, drift=0.02, vol=0.09, allow_neg=True).rename("opinc")
    return {"grossmargin": grossmargin, "netmargin": netmargin, "ebitdamargin": ebitdamargin,
            "revenue": revenue, "gp": gp, "opinc": opinc}


if __name__ == "__main__":
    cols = _build_inputs(1500)

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOWLIST, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOWLIST)
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

    print("OK f21_margin_trajectory_2nd_derivatives_001_150_claude: %d features pass" % n_features)
