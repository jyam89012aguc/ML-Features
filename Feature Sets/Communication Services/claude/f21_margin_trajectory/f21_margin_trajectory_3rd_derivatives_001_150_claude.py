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

# jerk of 'gm' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gm_rawdiff_021d_jerk_v001_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (rawdiff,21d)
def f21mt_f21_margin_trajectory_nm_rawdiff_021d_jerk_v002_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (rawdiff,21d)
def f21mt_f21_margin_trajectory_em_rawdiff_021d_jerk_v003_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (rawdiff,21d)
def f21mt_f21_margin_trajectory_om_rawdiff_021d_jerk_v004_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_021d_jerk_v005_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_021d_jerk_v006_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_021d_jerk_v007_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_021d_jerk_v008_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_021d_jerk_v009_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_021d_jerk_v010_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (rawdiff,21d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_021d_jerk_v011_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (rawdiff,21d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_021d_jerk_v012_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (rawdiff,21d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_021d_jerk_v013_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (rawdiff,21d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_021d_jerk_v014_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gm_rawdiff_042d_jerk_v015_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (rawdiff,42d)
def f21mt_f21_margin_trajectory_nm_rawdiff_042d_jerk_v016_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (rawdiff,42d)
def f21mt_f21_margin_trajectory_em_rawdiff_042d_jerk_v017_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (rawdiff,42d)
def f21mt_f21_margin_trajectory_om_rawdiff_042d_jerk_v018_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_042d_jerk_v019_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_042d_jerk_v020_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_042d_jerk_v021_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_042d_jerk_v022_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_042d_jerk_v023_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_042d_jerk_v024_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (rawdiff,42d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_042d_jerk_v025_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (rawdiff,42d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_042d_jerk_v026_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (rawdiff,42d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_042d_jerk_v027_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (rawdiff,42d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_042d_jerk_v028_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gm_rawdiff_063d_jerk_v029_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (rawdiff,63d)
def f21mt_f21_margin_trajectory_nm_rawdiff_063d_jerk_v030_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (rawdiff,63d)
def f21mt_f21_margin_trajectory_em_rawdiff_063d_jerk_v031_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (rawdiff,63d)
def f21mt_f21_margin_trajectory_om_rawdiff_063d_jerk_v032_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_063d_jerk_v033_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gesp_rawdiff_063d_jerk_v034_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_063d_jerk_v035_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_063d_jerk_v036_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (rawdiff,63d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_063d_jerk_v037_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_063d_jerk_v038_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (rawdiff,63d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_063d_jerk_v039_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (rawdiff,63d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_063d_jerk_v040_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (rawdiff,63d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_063d_jerk_v041_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (rawdiff,63d)
def f21mt_f21_margin_trajectory_profmin_rawdiff_063d_jerk_v042_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gm_rawdiff_126d_jerk_v043_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (rawdiff,126d)
def f21mt_f21_margin_trajectory_nm_rawdiff_126d_jerk_v044_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (rawdiff,126d)
def f21mt_f21_margin_trajectory_em_rawdiff_126d_jerk_v045_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (rawdiff,126d)
def f21mt_f21_margin_trajectory_om_rawdiff_126d_jerk_v046_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_126d_jerk_v047_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_126d_jerk_v048_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_126d_jerk_v049_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_126d_jerk_v050_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_126d_jerk_v051_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_126d_jerk_v052_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gosp_rawdiff_126d_jerk_v053_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (rawdiff,126d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_126d_jerk_v054_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (rawdiff,126d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_126d_jerk_v055_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(126)) / float(126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gm_rawdiff_252d_jerk_v056_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (rawdiff,252d)
def f21mt_f21_margin_trajectory_nm_rawdiff_252d_jerk_v057_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (rawdiff,252d)
def f21mt_f21_margin_trajectory_em_rawdiff_252d_jerk_v058_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (rawdiff,252d)
def f21mt_f21_margin_trajectory_om_rawdiff_252d_jerk_v059_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gnsp_rawdiff_252d_jerk_v060_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_ensp_rawdiff_252d_jerk_v061_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gnconv_rawdiff_252d_jerk_v062_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_geconv_rawdiff_252d_jerk_v063_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_onsp_rawdiff_252d_jerk_v064_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (rawdiff,252d)
def f21mt_f21_margin_trajectory_oesp_rawdiff_252d_jerk_v065_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (rawdiff,252d)
def f21mt_f21_margin_trajectory_ogconv_rawdiff_252d_jerk_v066_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (rawdiff,252d)
def f21mt_f21_margin_trajectory_gpdoll_rawdiff_252d_jerk_v067_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = (m - m.shift(252)) / float(252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (ols,63d)
def f21mt_f21_margin_trajectory_gosp_ols_063d_jerk_v068_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (ols,126d)
def f21mt_f21_margin_trajectory_em_ols_126d_jerk_v069_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (ols,126d)
def f21mt_f21_margin_trajectory_gesp_ols_126d_jerk_v070_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (ols,126d)
def f21mt_f21_margin_trajectory_profmin_ols_126d_jerk_v071_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 126)
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (ols,252d)
def f21mt_f21_margin_trajectory_nm_ols_252d_jerk_v072_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (ols,252d)
def f21mt_f21_margin_trajectory_em_ols_252d_jerk_v073_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (ols,252d)
def f21mt_f21_margin_trajectory_gnsp_ols_252d_jerk_v074_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (ols,252d)
def f21mt_f21_margin_trajectory_gesp_ols_252d_jerk_v075_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (ols,252d)
def f21mt_f21_margin_trajectory_gnconv_ols_252d_jerk_v076_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (ols,252d)
def f21mt_f21_margin_trajectory_onsp_ols_252d_jerk_v077_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (ols,252d)
def f21mt_f21_margin_trajectory_oesp_ols_252d_jerk_v078_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (ols,252d)
def f21mt_f21_margin_trajectory_gpdoll_ols_252d_jerk_v079_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    d1 = _slope(m, 252)
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (snr,21d)
def f21mt_f21_margin_trajectory_gm_snr_021d_jerk_v080_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (snr,21d)
def f21mt_f21_margin_trajectory_nm_snr_021d_jerk_v081_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (snr,21d)
def f21mt_f21_margin_trajectory_em_snr_021d_jerk_v082_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (snr,21d)
def f21mt_f21_margin_trajectory_om_snr_021d_jerk_v083_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (snr,21d)
def f21mt_f21_margin_trajectory_gnsp_snr_021d_jerk_v084_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (snr,21d)
def f21mt_f21_margin_trajectory_gesp_snr_021d_jerk_v085_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (snr,21d)
def f21mt_f21_margin_trajectory_ensp_snr_021d_jerk_v086_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (snr,21d)
def f21mt_f21_margin_trajectory_gnconv_snr_021d_jerk_v087_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (snr,21d)
def f21mt_f21_margin_trajectory_geconv_snr_021d_jerk_v088_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'enconv' (snr,21d)
def f21mt_f21_margin_trajectory_enconv_snr_021d_jerk_v089_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (snr,21d)
def f21mt_f21_margin_trajectory_onsp_snr_021d_jerk_v090_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (snr,21d)
def f21mt_f21_margin_trajectory_oesp_snr_021d_jerk_v091_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (snr,21d)
def f21mt_f21_margin_trajectory_gosp_snr_021d_jerk_v092_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (snr,21d)
def f21mt_f21_margin_trajectory_ogconv_snr_021d_jerk_v093_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (snr,21d)
def f21mt_f21_margin_trajectory_gpdoll_snr_021d_jerk_v094_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'emrev' (snr,21d)
def f21mt_f21_margin_trajectory_emrev_snr_021d_jerk_v095_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gmrev' (snr,21d)
def f21mt_f21_margin_trajectory_gmrev_snr_021d_jerk_v096_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (snr,21d)
def f21mt_f21_margin_trajectory_profmin_snr_021d_jerk_v097_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 21)
    sd = _std(m, 21).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (snr,42d)
def f21mt_f21_margin_trajectory_gm_snr_042d_jerk_v098_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (snr,42d)
def f21mt_f21_margin_trajectory_nm_snr_042d_jerk_v099_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (snr,42d)
def f21mt_f21_margin_trajectory_em_snr_042d_jerk_v100_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (snr,42d)
def f21mt_f21_margin_trajectory_om_snr_042d_jerk_v101_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (snr,42d)
def f21mt_f21_margin_trajectory_gnsp_snr_042d_jerk_v102_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (snr,42d)
def f21mt_f21_margin_trajectory_gesp_snr_042d_jerk_v103_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (snr,42d)
def f21mt_f21_margin_trajectory_ensp_snr_042d_jerk_v104_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (snr,42d)
def f21mt_f21_margin_trajectory_gnconv_snr_042d_jerk_v105_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (snr,42d)
def f21mt_f21_margin_trajectory_geconv_snr_042d_jerk_v106_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'enconv' (snr,42d)
def f21mt_f21_margin_trajectory_enconv_snr_042d_jerk_v107_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (snr,42d)
def f21mt_f21_margin_trajectory_onsp_snr_042d_jerk_v108_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (snr,42d)
def f21mt_f21_margin_trajectory_oesp_snr_042d_jerk_v109_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (snr,42d)
def f21mt_f21_margin_trajectory_gosp_snr_042d_jerk_v110_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (snr,42d)
def f21mt_f21_margin_trajectory_ogconv_snr_042d_jerk_v111_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (snr,42d)
def f21mt_f21_margin_trajectory_gpdoll_snr_042d_jerk_v112_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'emrev' (snr,42d)
def f21mt_f21_margin_trajectory_emrev_snr_042d_jerk_v113_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gmrev' (snr,42d)
def f21mt_f21_margin_trajectory_gmrev_snr_042d_jerk_v114_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (snr,42d)
def f21mt_f21_margin_trajectory_profmin_snr_042d_jerk_v115_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 42)
    sd = _std(m, 42).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (snr,63d)
def f21mt_f21_margin_trajectory_gm_snr_063d_jerk_v116_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (snr,63d)
def f21mt_f21_margin_trajectory_nm_snr_063d_jerk_v117_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (snr,63d)
def f21mt_f21_margin_trajectory_em_snr_063d_jerk_v118_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (snr,63d)
def f21mt_f21_margin_trajectory_om_snr_063d_jerk_v119_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (snr,63d)
def f21mt_f21_margin_trajectory_gnsp_snr_063d_jerk_v120_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (snr,63d)
def f21mt_f21_margin_trajectory_gesp_snr_063d_jerk_v121_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (snr,63d)
def f21mt_f21_margin_trajectory_ensp_snr_063d_jerk_v122_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (snr,63d)
def f21mt_f21_margin_trajectory_gnconv_snr_063d_jerk_v123_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (snr,63d)
def f21mt_f21_margin_trajectory_geconv_snr_063d_jerk_v124_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'enconv' (snr,63d)
def f21mt_f21_margin_trajectory_enconv_snr_063d_jerk_v125_signal(ebitdamargin, netmargin):
    m = netmargin / ebitdamargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (snr,63d)
def f21mt_f21_margin_trajectory_onsp_snr_063d_jerk_v126_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (snr,63d)
def f21mt_f21_margin_trajectory_oesp_snr_063d_jerk_v127_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (snr,63d)
def f21mt_f21_margin_trajectory_gosp_snr_063d_jerk_v128_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (snr,63d)
def f21mt_f21_margin_trajectory_ogconv_snr_063d_jerk_v129_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (snr,63d)
def f21mt_f21_margin_trajectory_gpdoll_snr_063d_jerk_v130_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'emrev' (snr,63d)
def f21mt_f21_margin_trajectory_emrev_snr_063d_jerk_v131_signal(ebitdamargin, revenue):
    m = ebitdamargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gmrev' (snr,63d)
def f21mt_f21_margin_trajectory_gmrev_snr_063d_jerk_v132_signal(grossmargin, revenue):
    m = grossmargin * np.log(revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'profmin' (snr,63d)
def f21mt_f21_margin_trajectory_profmin_snr_063d_jerk_v133_signal(grossmargin, netmargin, ebitdamargin):
    m = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1).min(axis=1)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 63)
    sd = _std(m, 63).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (snr,126d)
def f21mt_f21_margin_trajectory_gm_snr_126d_jerk_v134_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (snr,126d)
def f21mt_f21_margin_trajectory_nm_snr_126d_jerk_v135_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (snr,126d)
def f21mt_f21_margin_trajectory_em_snr_126d_jerk_v136_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'om' (snr,126d)
def f21mt_f21_margin_trajectory_om_snr_126d_jerk_v137_signal(opinc, revenue):
    m = opinc / revenue.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnsp' (snr,126d)
def f21mt_f21_margin_trajectory_gnsp_snr_126d_jerk_v138_signal(grossmargin, netmargin):
    m = grossmargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gesp' (snr,126d)
def f21mt_f21_margin_trajectory_gesp_snr_126d_jerk_v139_signal(grossmargin, ebitdamargin):
    m = grossmargin - ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ensp' (snr,126d)
def f21mt_f21_margin_trajectory_ensp_snr_126d_jerk_v140_signal(ebitdamargin, netmargin):
    m = ebitdamargin - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gnconv' (snr,126d)
def f21mt_f21_margin_trajectory_gnconv_snr_126d_jerk_v141_signal(grossmargin, netmargin):
    m = netmargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'geconv' (snr,126d)
def f21mt_f21_margin_trajectory_geconv_snr_126d_jerk_v142_signal(grossmargin, ebitdamargin):
    m = ebitdamargin / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'onsp' (snr,126d)
def f21mt_f21_margin_trajectory_onsp_snr_126d_jerk_v143_signal(opinc, revenue, netmargin):
    m = (opinc / revenue.replace(0, np.nan)) - netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'oesp' (snr,126d)
def f21mt_f21_margin_trajectory_oesp_snr_126d_jerk_v144_signal(opinc, revenue, ebitdamargin):
    m = ebitdamargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gosp' (snr,126d)
def f21mt_f21_margin_trajectory_gosp_snr_126d_jerk_v145_signal(grossmargin, opinc, revenue):
    m = grossmargin - (opinc / revenue.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'ogconv' (snr,126d)
def f21mt_f21_margin_trajectory_ogconv_snr_126d_jerk_v146_signal(grossmargin, opinc, revenue):
    m = (opinc / revenue.replace(0, np.nan)) / grossmargin.replace(0, np.nan)
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gpdoll' (snr,126d)
def f21mt_f21_margin_trajectory_gpdoll_snr_126d_jerk_v147_signal(gp):
    m = np.log(gp.replace(0, np.nan))
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 126)
    sd = _std(m, 126).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(126)) / float(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'gm' (snr,252d)
def f21mt_f21_margin_trajectory_gm_snr_252d_jerk_v148_signal(grossmargin):
    m = grossmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'nm' (snr,252d)
def f21mt_f21_margin_trajectory_nm_snr_252d_jerk_v149_signal(netmargin):
    m = netmargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk of 'em' (snr,252d)
def f21mt_f21_margin_trajectory_em_snr_252d_jerk_v150_signal(ebitdamargin):
    m = ebitdamargin
    m = m.replace([np.inf, -np.inf], np.nan)
    sl = _slope(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    d1 = sl / sd
    d2 = (d1 - d1.shift(252)) / float(252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f21mt_f21_margin_trajectory_gm_rawdiff_021d_jerk_v001_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_021d_jerk_v002_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_021d_jerk_v003_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_021d_jerk_v004_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_021d_jerk_v005_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_021d_jerk_v006_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_021d_jerk_v007_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_021d_jerk_v008_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_021d_jerk_v009_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_021d_jerk_v010_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_021d_jerk_v011_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_021d_jerk_v012_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_021d_jerk_v013_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_021d_jerk_v014_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_042d_jerk_v015_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_042d_jerk_v016_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_042d_jerk_v017_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_042d_jerk_v018_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_042d_jerk_v019_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_042d_jerk_v020_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_042d_jerk_v021_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_042d_jerk_v022_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_042d_jerk_v023_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_042d_jerk_v024_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_042d_jerk_v025_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_042d_jerk_v026_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_042d_jerk_v027_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_042d_jerk_v028_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_063d_jerk_v029_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_063d_jerk_v030_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_063d_jerk_v031_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_063d_jerk_v032_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_063d_jerk_v033_signal,
    f21mt_f21_margin_trajectory_gesp_rawdiff_063d_jerk_v034_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_063d_jerk_v035_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_063d_jerk_v036_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_063d_jerk_v037_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_063d_jerk_v038_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_063d_jerk_v039_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_063d_jerk_v040_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_063d_jerk_v041_signal,
    f21mt_f21_margin_trajectory_profmin_rawdiff_063d_jerk_v042_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_126d_jerk_v043_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_126d_jerk_v044_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_126d_jerk_v045_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_126d_jerk_v046_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_126d_jerk_v047_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_126d_jerk_v048_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_126d_jerk_v049_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_126d_jerk_v050_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_126d_jerk_v051_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_126d_jerk_v052_signal,
    f21mt_f21_margin_trajectory_gosp_rawdiff_126d_jerk_v053_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_126d_jerk_v054_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_126d_jerk_v055_signal,
    f21mt_f21_margin_trajectory_gm_rawdiff_252d_jerk_v056_signal,
    f21mt_f21_margin_trajectory_nm_rawdiff_252d_jerk_v057_signal,
    f21mt_f21_margin_trajectory_em_rawdiff_252d_jerk_v058_signal,
    f21mt_f21_margin_trajectory_om_rawdiff_252d_jerk_v059_signal,
    f21mt_f21_margin_trajectory_gnsp_rawdiff_252d_jerk_v060_signal,
    f21mt_f21_margin_trajectory_ensp_rawdiff_252d_jerk_v061_signal,
    f21mt_f21_margin_trajectory_gnconv_rawdiff_252d_jerk_v062_signal,
    f21mt_f21_margin_trajectory_geconv_rawdiff_252d_jerk_v063_signal,
    f21mt_f21_margin_trajectory_onsp_rawdiff_252d_jerk_v064_signal,
    f21mt_f21_margin_trajectory_oesp_rawdiff_252d_jerk_v065_signal,
    f21mt_f21_margin_trajectory_ogconv_rawdiff_252d_jerk_v066_signal,
    f21mt_f21_margin_trajectory_gpdoll_rawdiff_252d_jerk_v067_signal,
    f21mt_f21_margin_trajectory_gosp_ols_063d_jerk_v068_signal,
    f21mt_f21_margin_trajectory_em_ols_126d_jerk_v069_signal,
    f21mt_f21_margin_trajectory_gesp_ols_126d_jerk_v070_signal,
    f21mt_f21_margin_trajectory_profmin_ols_126d_jerk_v071_signal,
    f21mt_f21_margin_trajectory_nm_ols_252d_jerk_v072_signal,
    f21mt_f21_margin_trajectory_em_ols_252d_jerk_v073_signal,
    f21mt_f21_margin_trajectory_gnsp_ols_252d_jerk_v074_signal,
    f21mt_f21_margin_trajectory_gesp_ols_252d_jerk_v075_signal,
    f21mt_f21_margin_trajectory_gnconv_ols_252d_jerk_v076_signal,
    f21mt_f21_margin_trajectory_onsp_ols_252d_jerk_v077_signal,
    f21mt_f21_margin_trajectory_oesp_ols_252d_jerk_v078_signal,
    f21mt_f21_margin_trajectory_gpdoll_ols_252d_jerk_v079_signal,
    f21mt_f21_margin_trajectory_gm_snr_021d_jerk_v080_signal,
    f21mt_f21_margin_trajectory_nm_snr_021d_jerk_v081_signal,
    f21mt_f21_margin_trajectory_em_snr_021d_jerk_v082_signal,
    f21mt_f21_margin_trajectory_om_snr_021d_jerk_v083_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_021d_jerk_v084_signal,
    f21mt_f21_margin_trajectory_gesp_snr_021d_jerk_v085_signal,
    f21mt_f21_margin_trajectory_ensp_snr_021d_jerk_v086_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_021d_jerk_v087_signal,
    f21mt_f21_margin_trajectory_geconv_snr_021d_jerk_v088_signal,
    f21mt_f21_margin_trajectory_enconv_snr_021d_jerk_v089_signal,
    f21mt_f21_margin_trajectory_onsp_snr_021d_jerk_v090_signal,
    f21mt_f21_margin_trajectory_oesp_snr_021d_jerk_v091_signal,
    f21mt_f21_margin_trajectory_gosp_snr_021d_jerk_v092_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_021d_jerk_v093_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_021d_jerk_v094_signal,
    f21mt_f21_margin_trajectory_emrev_snr_021d_jerk_v095_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_021d_jerk_v096_signal,
    f21mt_f21_margin_trajectory_profmin_snr_021d_jerk_v097_signal,
    f21mt_f21_margin_trajectory_gm_snr_042d_jerk_v098_signal,
    f21mt_f21_margin_trajectory_nm_snr_042d_jerk_v099_signal,
    f21mt_f21_margin_trajectory_em_snr_042d_jerk_v100_signal,
    f21mt_f21_margin_trajectory_om_snr_042d_jerk_v101_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_042d_jerk_v102_signal,
    f21mt_f21_margin_trajectory_gesp_snr_042d_jerk_v103_signal,
    f21mt_f21_margin_trajectory_ensp_snr_042d_jerk_v104_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_042d_jerk_v105_signal,
    f21mt_f21_margin_trajectory_geconv_snr_042d_jerk_v106_signal,
    f21mt_f21_margin_trajectory_enconv_snr_042d_jerk_v107_signal,
    f21mt_f21_margin_trajectory_onsp_snr_042d_jerk_v108_signal,
    f21mt_f21_margin_trajectory_oesp_snr_042d_jerk_v109_signal,
    f21mt_f21_margin_trajectory_gosp_snr_042d_jerk_v110_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_042d_jerk_v111_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_042d_jerk_v112_signal,
    f21mt_f21_margin_trajectory_emrev_snr_042d_jerk_v113_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_042d_jerk_v114_signal,
    f21mt_f21_margin_trajectory_profmin_snr_042d_jerk_v115_signal,
    f21mt_f21_margin_trajectory_gm_snr_063d_jerk_v116_signal,
    f21mt_f21_margin_trajectory_nm_snr_063d_jerk_v117_signal,
    f21mt_f21_margin_trajectory_em_snr_063d_jerk_v118_signal,
    f21mt_f21_margin_trajectory_om_snr_063d_jerk_v119_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_063d_jerk_v120_signal,
    f21mt_f21_margin_trajectory_gesp_snr_063d_jerk_v121_signal,
    f21mt_f21_margin_trajectory_ensp_snr_063d_jerk_v122_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_063d_jerk_v123_signal,
    f21mt_f21_margin_trajectory_geconv_snr_063d_jerk_v124_signal,
    f21mt_f21_margin_trajectory_enconv_snr_063d_jerk_v125_signal,
    f21mt_f21_margin_trajectory_onsp_snr_063d_jerk_v126_signal,
    f21mt_f21_margin_trajectory_oesp_snr_063d_jerk_v127_signal,
    f21mt_f21_margin_trajectory_gosp_snr_063d_jerk_v128_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_063d_jerk_v129_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_063d_jerk_v130_signal,
    f21mt_f21_margin_trajectory_emrev_snr_063d_jerk_v131_signal,
    f21mt_f21_margin_trajectory_gmrev_snr_063d_jerk_v132_signal,
    f21mt_f21_margin_trajectory_profmin_snr_063d_jerk_v133_signal,
    f21mt_f21_margin_trajectory_gm_snr_126d_jerk_v134_signal,
    f21mt_f21_margin_trajectory_nm_snr_126d_jerk_v135_signal,
    f21mt_f21_margin_trajectory_em_snr_126d_jerk_v136_signal,
    f21mt_f21_margin_trajectory_om_snr_126d_jerk_v137_signal,
    f21mt_f21_margin_trajectory_gnsp_snr_126d_jerk_v138_signal,
    f21mt_f21_margin_trajectory_gesp_snr_126d_jerk_v139_signal,
    f21mt_f21_margin_trajectory_ensp_snr_126d_jerk_v140_signal,
    f21mt_f21_margin_trajectory_gnconv_snr_126d_jerk_v141_signal,
    f21mt_f21_margin_trajectory_geconv_snr_126d_jerk_v142_signal,
    f21mt_f21_margin_trajectory_onsp_snr_126d_jerk_v143_signal,
    f21mt_f21_margin_trajectory_oesp_snr_126d_jerk_v144_signal,
    f21mt_f21_margin_trajectory_gosp_snr_126d_jerk_v145_signal,
    f21mt_f21_margin_trajectory_ogconv_snr_126d_jerk_v146_signal,
    f21mt_f21_margin_trajectory_gpdoll_snr_126d_jerk_v147_signal,
    f21mt_f21_margin_trajectory_gm_snr_252d_jerk_v148_signal,
    f21mt_f21_margin_trajectory_nm_snr_252d_jerk_v149_signal,
    f21mt_f21_margin_trajectory_em_snr_252d_jerk_v150_signal,
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

    print("OK f21_margin_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
