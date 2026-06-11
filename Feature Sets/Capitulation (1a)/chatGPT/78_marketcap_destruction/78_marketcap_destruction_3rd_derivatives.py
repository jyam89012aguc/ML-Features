import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def mcd_176_mcd_001_pe_compression_z_21_accel_1(mcd_151_mcd_001_pe_compression_z_21_roc_1):
    feature = _s(mcd_151_mcd_001_pe_compression_z_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mcd_177_mcd_007_earnings_yield_spike_252_accel_42(mcd_152_mcd_007_earnings_yield_spike_252_roc_42):
    feature = _s(mcd_152_mcd_007_earnings_yield_spike_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mcd_178_mcd_013_ev_marketcap_gap_1512_accel_126(mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126):
    feature = _s(mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mcd_179_mcd_019_ps_compression_z_84_accel_378(mcd_154_mcd_019_ps_compression_z_84_roc_378):
    feature = _s(mcd_154_mcd_019_ps_compression_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def mcd_180_mcd_025_pe_compression_z_756_accel_4(mcd_155_mcd_025_pe_compression_z_756_roc_4):
    feature = _s(mcd_155_mcd_025_pe_compression_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















MARKETCAP_DESTRUCTION_REGISTRY_3RD_DERIVATIVES = {
    'mcd_176_mcd_001_pe_compression_z_21_accel_1': {'inputs': ['mcd_151_mcd_001_pe_compression_z_21_roc_1'], 'func': mcd_176_mcd_001_pe_compression_z_21_accel_1},
    'mcd_177_mcd_007_earnings_yield_spike_252_accel_42': {'inputs': ['mcd_152_mcd_007_earnings_yield_spike_252_roc_42'], 'func': mcd_177_mcd_007_earnings_yield_spike_252_accel_42},
    'mcd_178_mcd_013_ev_marketcap_gap_1512_accel_126': {'inputs': ['mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126'], 'func': mcd_178_mcd_013_ev_marketcap_gap_1512_accel_126},
    'mcd_179_mcd_019_ps_compression_z_84_accel_378': {'inputs': ['mcd_154_mcd_019_ps_compression_z_84_roc_378'], 'func': mcd_179_mcd_019_ps_compression_z_84_accel_378},
    'mcd_180_mcd_025_pe_compression_z_756_accel_4': {'inputs': ['mcd_155_mcd_025_pe_compression_z_756_roc_4'], 'func': mcd_180_mcd_025_pe_compression_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def md_replacement_d3_001(md_replacement_d2_001):
    feature = _clean(md_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_001'] = {'inputs': ['md_replacement_d2_001'], 'func': md_replacement_d3_001}


def md_replacement_d3_002(md_replacement_d2_002):
    feature = _clean(md_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_002'] = {'inputs': ['md_replacement_d2_002'], 'func': md_replacement_d3_002}


def md_replacement_d3_003(md_replacement_d2_003):
    feature = _clean(md_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_003'] = {'inputs': ['md_replacement_d2_003'], 'func': md_replacement_d3_003}


def md_replacement_d3_004(md_replacement_d2_004):
    feature = _clean(md_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_004'] = {'inputs': ['md_replacement_d2_004'], 'func': md_replacement_d3_004}


def md_replacement_d3_005(md_replacement_d2_005):
    feature = _clean(md_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_005'] = {'inputs': ['md_replacement_d2_005'], 'func': md_replacement_d3_005}


def md_replacement_d3_006(md_replacement_d2_006):
    feature = _clean(md_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_006'] = {'inputs': ['md_replacement_d2_006'], 'func': md_replacement_d3_006}


def md_replacement_d3_007(md_replacement_d2_007):
    feature = _clean(md_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_007'] = {'inputs': ['md_replacement_d2_007'], 'func': md_replacement_d3_007}


def md_replacement_d3_008(md_replacement_d2_008):
    feature = _clean(md_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_008'] = {'inputs': ['md_replacement_d2_008'], 'func': md_replacement_d3_008}


def md_replacement_d3_009(md_replacement_d2_009):
    feature = _clean(md_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_009'] = {'inputs': ['md_replacement_d2_009'], 'func': md_replacement_d3_009}


def md_replacement_d3_010(md_replacement_d2_010):
    feature = _clean(md_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_010'] = {'inputs': ['md_replacement_d2_010'], 'func': md_replacement_d3_010}


def md_replacement_d3_011(md_replacement_d2_011):
    feature = _clean(md_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_011'] = {'inputs': ['md_replacement_d2_011'], 'func': md_replacement_d3_011}


def md_replacement_d3_012(md_replacement_d2_012):
    feature = _clean(md_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_012'] = {'inputs': ['md_replacement_d2_012'], 'func': md_replacement_d3_012}


def md_replacement_d3_013(md_replacement_d2_013):
    feature = _clean(md_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_013'] = {'inputs': ['md_replacement_d2_013'], 'func': md_replacement_d3_013}


def md_replacement_d3_014(md_replacement_d2_014):
    feature = _clean(md_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_014'] = {'inputs': ['md_replacement_d2_014'], 'func': md_replacement_d3_014}


def md_replacement_d3_015(md_replacement_d2_015):
    feature = _clean(md_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_015'] = {'inputs': ['md_replacement_d2_015'], 'func': md_replacement_d3_015}


def md_replacement_d3_016(md_replacement_d2_016):
    feature = _clean(md_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_016'] = {'inputs': ['md_replacement_d2_016'], 'func': md_replacement_d3_016}


def md_replacement_d3_017(md_replacement_d2_017):
    feature = _clean(md_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_017'] = {'inputs': ['md_replacement_d2_017'], 'func': md_replacement_d3_017}


def md_replacement_d3_018(md_replacement_d2_018):
    feature = _clean(md_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_018'] = {'inputs': ['md_replacement_d2_018'], 'func': md_replacement_d3_018}


def md_replacement_d3_019(md_replacement_d2_019):
    feature = _clean(md_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_019'] = {'inputs': ['md_replacement_d2_019'], 'func': md_replacement_d3_019}


def md_replacement_d3_020(md_replacement_d2_020):
    feature = _clean(md_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_020'] = {'inputs': ['md_replacement_d2_020'], 'func': md_replacement_d3_020}


def md_replacement_d3_021(md_replacement_d2_021):
    feature = _clean(md_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_021'] = {'inputs': ['md_replacement_d2_021'], 'func': md_replacement_d3_021}


def md_replacement_d3_022(md_replacement_d2_022):
    feature = _clean(md_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_022'] = {'inputs': ['md_replacement_d2_022'], 'func': md_replacement_d3_022}


def md_replacement_d3_023(md_replacement_d2_023):
    feature = _clean(md_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_023'] = {'inputs': ['md_replacement_d2_023'], 'func': md_replacement_d3_023}


def md_replacement_d3_024(md_replacement_d2_024):
    feature = _clean(md_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_024'] = {'inputs': ['md_replacement_d2_024'], 'func': md_replacement_d3_024}


def md_replacement_d3_025(md_replacement_d2_025):
    feature = _clean(md_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_025'] = {'inputs': ['md_replacement_d2_025'], 'func': md_replacement_d3_025}


def md_replacement_d3_026(md_replacement_d2_026):
    feature = _clean(md_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_026'] = {'inputs': ['md_replacement_d2_026'], 'func': md_replacement_d3_026}


def md_replacement_d3_027(md_replacement_d2_027):
    feature = _clean(md_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_027'] = {'inputs': ['md_replacement_d2_027'], 'func': md_replacement_d3_027}


def md_replacement_d3_028(md_replacement_d2_028):
    feature = _clean(md_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_028'] = {'inputs': ['md_replacement_d2_028'], 'func': md_replacement_d3_028}


def md_replacement_d3_029(md_replacement_d2_029):
    feature = _clean(md_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_029'] = {'inputs': ['md_replacement_d2_029'], 'func': md_replacement_d3_029}


def md_replacement_d3_030(md_replacement_d2_030):
    feature = _clean(md_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_030'] = {'inputs': ['md_replacement_d2_030'], 'func': md_replacement_d3_030}


def md_replacement_d3_031(md_replacement_d2_031):
    feature = _clean(md_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_031'] = {'inputs': ['md_replacement_d2_031'], 'func': md_replacement_d3_031}


def md_replacement_d3_032(md_replacement_d2_032):
    feature = _clean(md_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_032'] = {'inputs': ['md_replacement_d2_032'], 'func': md_replacement_d3_032}


def md_replacement_d3_033(md_replacement_d2_033):
    feature = _clean(md_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_033'] = {'inputs': ['md_replacement_d2_033'], 'func': md_replacement_d3_033}


def md_replacement_d3_034(md_replacement_d2_034):
    feature = _clean(md_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_034'] = {'inputs': ['md_replacement_d2_034'], 'func': md_replacement_d3_034}


def md_replacement_d3_035(md_replacement_d2_035):
    feature = _clean(md_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_035'] = {'inputs': ['md_replacement_d2_035'], 'func': md_replacement_d3_035}


def md_replacement_d3_036(md_replacement_d2_036):
    feature = _clean(md_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_036'] = {'inputs': ['md_replacement_d2_036'], 'func': md_replacement_d3_036}


def md_replacement_d3_037(md_replacement_d2_037):
    feature = _clean(md_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_037'] = {'inputs': ['md_replacement_d2_037'], 'func': md_replacement_d3_037}


def md_replacement_d3_038(md_replacement_d2_038):
    feature = _clean(md_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_038'] = {'inputs': ['md_replacement_d2_038'], 'func': md_replacement_d3_038}


def md_replacement_d3_039(md_replacement_d2_039):
    feature = _clean(md_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_039'] = {'inputs': ['md_replacement_d2_039'], 'func': md_replacement_d3_039}


def md_replacement_d3_040(md_replacement_d2_040):
    feature = _clean(md_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_040'] = {'inputs': ['md_replacement_d2_040'], 'func': md_replacement_d3_040}


def md_replacement_d3_041(md_replacement_d2_041):
    feature = _clean(md_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_041'] = {'inputs': ['md_replacement_d2_041'], 'func': md_replacement_d3_041}


def md_replacement_d3_042(md_replacement_d2_042):
    feature = _clean(md_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_042'] = {'inputs': ['md_replacement_d2_042'], 'func': md_replacement_d3_042}


def md_replacement_d3_043(md_replacement_d2_043):
    feature = _clean(md_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_043'] = {'inputs': ['md_replacement_d2_043'], 'func': md_replacement_d3_043}


def md_replacement_d3_044(md_replacement_d2_044):
    feature = _clean(md_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_044'] = {'inputs': ['md_replacement_d2_044'], 'func': md_replacement_d3_044}


def md_replacement_d3_045(md_replacement_d2_045):
    feature = _clean(md_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_045'] = {'inputs': ['md_replacement_d2_045'], 'func': md_replacement_d3_045}


def md_replacement_d3_046(md_replacement_d2_046):
    feature = _clean(md_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_046'] = {'inputs': ['md_replacement_d2_046'], 'func': md_replacement_d3_046}


def md_replacement_d3_047(md_replacement_d2_047):
    feature = _clean(md_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_047'] = {'inputs': ['md_replacement_d2_047'], 'func': md_replacement_d3_047}


def md_replacement_d3_048(md_replacement_d2_048):
    feature = _clean(md_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_048'] = {'inputs': ['md_replacement_d2_048'], 'func': md_replacement_d3_048}


def md_replacement_d3_049(md_replacement_d2_049):
    feature = _clean(md_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_049'] = {'inputs': ['md_replacement_d2_049'], 'func': md_replacement_d3_049}


def md_replacement_d3_050(md_replacement_d2_050):
    feature = _clean(md_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_050'] = {'inputs': ['md_replacement_d2_050'], 'func': md_replacement_d3_050}


def md_replacement_d3_051(md_replacement_d2_051):
    feature = _clean(md_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_051'] = {'inputs': ['md_replacement_d2_051'], 'func': md_replacement_d3_051}


def md_replacement_d3_052(md_replacement_d2_052):
    feature = _clean(md_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_052'] = {'inputs': ['md_replacement_d2_052'], 'func': md_replacement_d3_052}


def md_replacement_d3_053(md_replacement_d2_053):
    feature = _clean(md_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_053'] = {'inputs': ['md_replacement_d2_053'], 'func': md_replacement_d3_053}


def md_replacement_d3_054(md_replacement_d2_054):
    feature = _clean(md_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_054'] = {'inputs': ['md_replacement_d2_054'], 'func': md_replacement_d3_054}


def md_replacement_d3_055(md_replacement_d2_055):
    feature = _clean(md_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_055'] = {'inputs': ['md_replacement_d2_055'], 'func': md_replacement_d3_055}


def md_replacement_d3_056(md_replacement_d2_056):
    feature = _clean(md_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_056'] = {'inputs': ['md_replacement_d2_056'], 'func': md_replacement_d3_056}


def md_replacement_d3_057(md_replacement_d2_057):
    feature = _clean(md_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_057'] = {'inputs': ['md_replacement_d2_057'], 'func': md_replacement_d3_057}


def md_replacement_d3_058(md_replacement_d2_058):
    feature = _clean(md_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_058'] = {'inputs': ['md_replacement_d2_058'], 'func': md_replacement_d3_058}


def md_replacement_d3_059(md_replacement_d2_059):
    feature = _clean(md_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_059'] = {'inputs': ['md_replacement_d2_059'], 'func': md_replacement_d3_059}


def md_replacement_d3_060(md_replacement_d2_060):
    feature = _clean(md_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_060'] = {'inputs': ['md_replacement_d2_060'], 'func': md_replacement_d3_060}


def md_replacement_d3_061(md_replacement_d2_061):
    feature = _clean(md_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_061'] = {'inputs': ['md_replacement_d2_061'], 'func': md_replacement_d3_061}


def md_replacement_d3_062(md_replacement_d2_062):
    feature = _clean(md_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_062'] = {'inputs': ['md_replacement_d2_062'], 'func': md_replacement_d3_062}


def md_replacement_d3_063(md_replacement_d2_063):
    feature = _clean(md_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_063'] = {'inputs': ['md_replacement_d2_063'], 'func': md_replacement_d3_063}


def md_replacement_d3_064(md_replacement_d2_064):
    feature = _clean(md_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_064'] = {'inputs': ['md_replacement_d2_064'], 'func': md_replacement_d3_064}


def md_replacement_d3_065(md_replacement_d2_065):
    feature = _clean(md_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_065'] = {'inputs': ['md_replacement_d2_065'], 'func': md_replacement_d3_065}


def md_replacement_d3_066(md_replacement_d2_066):
    feature = _clean(md_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_066'] = {'inputs': ['md_replacement_d2_066'], 'func': md_replacement_d3_066}


def md_replacement_d3_067(md_replacement_d2_067):
    feature = _clean(md_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_067'] = {'inputs': ['md_replacement_d2_067'], 'func': md_replacement_d3_067}


def md_replacement_d3_068(md_replacement_d2_068):
    feature = _clean(md_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_068'] = {'inputs': ['md_replacement_d2_068'], 'func': md_replacement_d3_068}


def md_replacement_d3_069(md_replacement_d2_069):
    feature = _clean(md_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_069'] = {'inputs': ['md_replacement_d2_069'], 'func': md_replacement_d3_069}


def md_replacement_d3_070(md_replacement_d2_070):
    feature = _clean(md_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_070'] = {'inputs': ['md_replacement_d2_070'], 'func': md_replacement_d3_070}


def md_replacement_d3_071(md_replacement_d2_071):
    feature = _clean(md_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_071'] = {'inputs': ['md_replacement_d2_071'], 'func': md_replacement_d3_071}


def md_replacement_d3_072(md_replacement_d2_072):
    feature = _clean(md_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_072'] = {'inputs': ['md_replacement_d2_072'], 'func': md_replacement_d3_072}


def md_replacement_d3_073(md_replacement_d2_073):
    feature = _clean(md_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_073'] = {'inputs': ['md_replacement_d2_073'], 'func': md_replacement_d3_073}


def md_replacement_d3_074(md_replacement_d2_074):
    feature = _clean(md_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_074'] = {'inputs': ['md_replacement_d2_074'], 'func': md_replacement_d3_074}


def md_replacement_d3_075(md_replacement_d2_075):
    feature = _clean(md_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_075'] = {'inputs': ['md_replacement_d2_075'], 'func': md_replacement_d3_075}


def md_replacement_d3_076(md_replacement_d2_076):
    feature = _clean(md_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_076'] = {'inputs': ['md_replacement_d2_076'], 'func': md_replacement_d3_076}


def md_replacement_d3_077(md_replacement_d2_077):
    feature = _clean(md_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_077'] = {'inputs': ['md_replacement_d2_077'], 'func': md_replacement_d3_077}


def md_replacement_d3_078(md_replacement_d2_078):
    feature = _clean(md_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_078'] = {'inputs': ['md_replacement_d2_078'], 'func': md_replacement_d3_078}


def md_replacement_d3_079(md_replacement_d2_079):
    feature = _clean(md_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_079'] = {'inputs': ['md_replacement_d2_079'], 'func': md_replacement_d3_079}


def md_replacement_d3_080(md_replacement_d2_080):
    feature = _clean(md_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_080'] = {'inputs': ['md_replacement_d2_080'], 'func': md_replacement_d3_080}


def md_replacement_d3_081(md_replacement_d2_081):
    feature = _clean(md_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_081'] = {'inputs': ['md_replacement_d2_081'], 'func': md_replacement_d3_081}


def md_replacement_d3_082(md_replacement_d2_082):
    feature = _clean(md_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_082'] = {'inputs': ['md_replacement_d2_082'], 'func': md_replacement_d3_082}


def md_replacement_d3_083(md_replacement_d2_083):
    feature = _clean(md_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_083'] = {'inputs': ['md_replacement_d2_083'], 'func': md_replacement_d3_083}


def md_replacement_d3_084(md_replacement_d2_084):
    feature = _clean(md_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_084'] = {'inputs': ['md_replacement_d2_084'], 'func': md_replacement_d3_084}


def md_replacement_d3_085(md_replacement_d2_085):
    feature = _clean(md_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_085'] = {'inputs': ['md_replacement_d2_085'], 'func': md_replacement_d3_085}


def md_replacement_d3_086(md_replacement_d2_086):
    feature = _clean(md_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_086'] = {'inputs': ['md_replacement_d2_086'], 'func': md_replacement_d3_086}


def md_replacement_d3_087(md_replacement_d2_087):
    feature = _clean(md_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_087'] = {'inputs': ['md_replacement_d2_087'], 'func': md_replacement_d3_087}


def md_replacement_d3_088(md_replacement_d2_088):
    feature = _clean(md_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_088'] = {'inputs': ['md_replacement_d2_088'], 'func': md_replacement_d3_088}


def md_replacement_d3_089(md_replacement_d2_089):
    feature = _clean(md_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_089'] = {'inputs': ['md_replacement_d2_089'], 'func': md_replacement_d3_089}


def md_replacement_d3_090(md_replacement_d2_090):
    feature = _clean(md_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_090'] = {'inputs': ['md_replacement_d2_090'], 'func': md_replacement_d3_090}


def md_replacement_d3_091(md_replacement_d2_091):
    feature = _clean(md_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_091'] = {'inputs': ['md_replacement_d2_091'], 'func': md_replacement_d3_091}


def md_replacement_d3_092(md_replacement_d2_092):
    feature = _clean(md_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_092'] = {'inputs': ['md_replacement_d2_092'], 'func': md_replacement_d3_092}


def md_replacement_d3_093(md_replacement_d2_093):
    feature = _clean(md_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_093'] = {'inputs': ['md_replacement_d2_093'], 'func': md_replacement_d3_093}


def md_replacement_d3_094(md_replacement_d2_094):
    feature = _clean(md_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_094'] = {'inputs': ['md_replacement_d2_094'], 'func': md_replacement_d3_094}


def md_replacement_d3_095(md_replacement_d2_095):
    feature = _clean(md_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_095'] = {'inputs': ['md_replacement_d2_095'], 'func': md_replacement_d3_095}


def md_replacement_d3_096(md_replacement_d2_096):
    feature = _clean(md_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_096'] = {'inputs': ['md_replacement_d2_096'], 'func': md_replacement_d3_096}


def md_replacement_d3_097(md_replacement_d2_097):
    feature = _clean(md_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_097'] = {'inputs': ['md_replacement_d2_097'], 'func': md_replacement_d3_097}


def md_replacement_d3_098(md_replacement_d2_098):
    feature = _clean(md_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_098'] = {'inputs': ['md_replacement_d2_098'], 'func': md_replacement_d3_098}


def md_replacement_d3_099(md_replacement_d2_099):
    feature = _clean(md_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_099'] = {'inputs': ['md_replacement_d2_099'], 'func': md_replacement_d3_099}


def md_replacement_d3_100(md_replacement_d2_100):
    feature = _clean(md_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_100'] = {'inputs': ['md_replacement_d2_100'], 'func': md_replacement_d3_100}


def md_replacement_d3_101(md_replacement_d2_101):
    feature = _clean(md_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_101'] = {'inputs': ['md_replacement_d2_101'], 'func': md_replacement_d3_101}


def md_replacement_d3_102(md_replacement_d2_102):
    feature = _clean(md_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_102'] = {'inputs': ['md_replacement_d2_102'], 'func': md_replacement_d3_102}


def md_replacement_d3_103(md_replacement_d2_103):
    feature = _clean(md_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_103'] = {'inputs': ['md_replacement_d2_103'], 'func': md_replacement_d3_103}


def md_replacement_d3_104(md_replacement_d2_104):
    feature = _clean(md_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_104'] = {'inputs': ['md_replacement_d2_104'], 'func': md_replacement_d3_104}


def md_replacement_d3_105(md_replacement_d2_105):
    feature = _clean(md_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_105'] = {'inputs': ['md_replacement_d2_105'], 'func': md_replacement_d3_105}


def md_replacement_d3_106(md_replacement_d2_106):
    feature = _clean(md_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_106'] = {'inputs': ['md_replacement_d2_106'], 'func': md_replacement_d3_106}


def md_replacement_d3_107(md_replacement_d2_107):
    feature = _clean(md_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_107'] = {'inputs': ['md_replacement_d2_107'], 'func': md_replacement_d3_107}


def md_replacement_d3_108(md_replacement_d2_108):
    feature = _clean(md_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_108'] = {'inputs': ['md_replacement_d2_108'], 'func': md_replacement_d3_108}


def md_replacement_d3_109(md_replacement_d2_109):
    feature = _clean(md_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_109'] = {'inputs': ['md_replacement_d2_109'], 'func': md_replacement_d3_109}


def md_replacement_d3_110(md_replacement_d2_110):
    feature = _clean(md_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_110'] = {'inputs': ['md_replacement_d2_110'], 'func': md_replacement_d3_110}


def md_replacement_d3_111(md_replacement_d2_111):
    feature = _clean(md_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_111'] = {'inputs': ['md_replacement_d2_111'], 'func': md_replacement_d3_111}


def md_replacement_d3_112(md_replacement_d2_112):
    feature = _clean(md_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_112'] = {'inputs': ['md_replacement_d2_112'], 'func': md_replacement_d3_112}


def md_replacement_d3_113(md_replacement_d2_113):
    feature = _clean(md_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_113'] = {'inputs': ['md_replacement_d2_113'], 'func': md_replacement_d3_113}


def md_replacement_d3_114(md_replacement_d2_114):
    feature = _clean(md_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_114'] = {'inputs': ['md_replacement_d2_114'], 'func': md_replacement_d3_114}


def md_replacement_d3_115(md_replacement_d2_115):
    feature = _clean(md_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_115'] = {'inputs': ['md_replacement_d2_115'], 'func': md_replacement_d3_115}


def md_replacement_d3_116(md_replacement_d2_116):
    feature = _clean(md_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_116'] = {'inputs': ['md_replacement_d2_116'], 'func': md_replacement_d3_116}


def md_replacement_d3_117(md_replacement_d2_117):
    feature = _clean(md_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_117'] = {'inputs': ['md_replacement_d2_117'], 'func': md_replacement_d3_117}


def md_replacement_d3_118(md_replacement_d2_118):
    feature = _clean(md_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_118'] = {'inputs': ['md_replacement_d2_118'], 'func': md_replacement_d3_118}


def md_replacement_d3_119(md_replacement_d2_119):
    feature = _clean(md_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_119'] = {'inputs': ['md_replacement_d2_119'], 'func': md_replacement_d3_119}


def md_replacement_d3_120(md_replacement_d2_120):
    feature = _clean(md_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_120'] = {'inputs': ['md_replacement_d2_120'], 'func': md_replacement_d3_120}


def md_replacement_d3_121(md_replacement_d2_121):
    feature = _clean(md_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_121'] = {'inputs': ['md_replacement_d2_121'], 'func': md_replacement_d3_121}


def md_replacement_d3_122(md_replacement_d2_122):
    feature = _clean(md_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_122'] = {'inputs': ['md_replacement_d2_122'], 'func': md_replacement_d3_122}


def md_replacement_d3_123(md_replacement_d2_123):
    feature = _clean(md_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_123'] = {'inputs': ['md_replacement_d2_123'], 'func': md_replacement_d3_123}


def md_replacement_d3_124(md_replacement_d2_124):
    feature = _clean(md_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_124'] = {'inputs': ['md_replacement_d2_124'], 'func': md_replacement_d3_124}


def md_replacement_d3_125(md_replacement_d2_125):
    feature = _clean(md_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_125'] = {'inputs': ['md_replacement_d2_125'], 'func': md_replacement_d3_125}


def md_replacement_d3_126(md_replacement_d2_126):
    feature = _clean(md_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_126'] = {'inputs': ['md_replacement_d2_126'], 'func': md_replacement_d3_126}


def md_replacement_d3_127(md_replacement_d2_127):
    feature = _clean(md_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_127'] = {'inputs': ['md_replacement_d2_127'], 'func': md_replacement_d3_127}


def md_replacement_d3_128(md_replacement_d2_128):
    feature = _clean(md_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_128'] = {'inputs': ['md_replacement_d2_128'], 'func': md_replacement_d3_128}


def md_replacement_d3_129(md_replacement_d2_129):
    feature = _clean(md_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_129'] = {'inputs': ['md_replacement_d2_129'], 'func': md_replacement_d3_129}


def md_replacement_d3_130(md_replacement_d2_130):
    feature = _clean(md_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_130'] = {'inputs': ['md_replacement_d2_130'], 'func': md_replacement_d3_130}


def md_replacement_d3_131(md_replacement_d2_131):
    feature = _clean(md_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_131'] = {'inputs': ['md_replacement_d2_131'], 'func': md_replacement_d3_131}


def md_replacement_d3_132(md_replacement_d2_132):
    feature = _clean(md_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_132'] = {'inputs': ['md_replacement_d2_132'], 'func': md_replacement_d3_132}


def md_replacement_d3_133(md_replacement_d2_133):
    feature = _clean(md_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_133'] = {'inputs': ['md_replacement_d2_133'], 'func': md_replacement_d3_133}


def md_replacement_d3_134(md_replacement_d2_134):
    feature = _clean(md_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_134'] = {'inputs': ['md_replacement_d2_134'], 'func': md_replacement_d3_134}


def md_replacement_d3_135(md_replacement_d2_135):
    feature = _clean(md_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_135'] = {'inputs': ['md_replacement_d2_135'], 'func': md_replacement_d3_135}


def md_replacement_d3_136(md_replacement_d2_136):
    feature = _clean(md_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_136'] = {'inputs': ['md_replacement_d2_136'], 'func': md_replacement_d3_136}


def md_replacement_d3_137(md_replacement_d2_137):
    feature = _clean(md_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_137'] = {'inputs': ['md_replacement_d2_137'], 'func': md_replacement_d3_137}


def md_replacement_d3_138(md_replacement_d2_138):
    feature = _clean(md_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_138'] = {'inputs': ['md_replacement_d2_138'], 'func': md_replacement_d3_138}


# Third-derivative extensions for repaired first-base features.
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mcd_base_universe_d3_001_mcd_002_pb_compression_z_42(mcd_base_universe_d2_001_mcd_002_pb_compression_z_42):
    return _base_universe_d3(mcd_base_universe_d2_001_mcd_002_pb_compression_z_42, 1)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_001_mcd_002_pb_compression_z_42'] = {'inputs': ['mcd_base_universe_d2_001_mcd_002_pb_compression_z_42'], 'func': mcd_base_universe_d3_001_mcd_002_pb_compression_z_42}


def mcd_base_universe_d3_002_mcd_003_ps_compression_z_63(mcd_base_universe_d2_002_mcd_003_ps_compression_z_63):
    return _base_universe_d3(mcd_base_universe_d2_002_mcd_003_ps_compression_z_63, 2)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_002_mcd_003_ps_compression_z_63'] = {'inputs': ['mcd_base_universe_d2_002_mcd_003_ps_compression_z_63'], 'func': mcd_base_universe_d3_002_mcd_003_ps_compression_z_63}


def mcd_base_universe_d3_003_mcd_005_ev_marketcap_gap_126(mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126):
    return _base_universe_d3(mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126, 3)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_003_mcd_005_ev_marketcap_gap_126'] = {'inputs': ['mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126'], 'func': mcd_base_universe_d3_003_mcd_005_ev_marketcap_gap_126}


def mcd_base_universe_d3_004_mcd_006_dividend_yield_spike_189(mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189):
    return _base_universe_d3(mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189, 4)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_004_mcd_006_dividend_yield_spike_189'] = {'inputs': ['mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189'], 'func': mcd_base_universe_d3_004_mcd_006_dividend_yield_spike_189}


def mcd_base_universe_d3_005_mcd_008_valuation_history_depth_378(mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378):
    return _base_universe_d3(mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378, 5)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_005_mcd_008_valuation_history_depth_378'] = {'inputs': ['mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378'], 'func': mcd_base_universe_d3_005_mcd_008_valuation_history_depth_378}


def mcd_base_universe_d3_006_mcd_009_pe_compression_z_504(mcd_base_universe_d2_006_mcd_009_pe_compression_z_504):
    return _base_universe_d3(mcd_base_universe_d2_006_mcd_009_pe_compression_z_504, 6)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_006_mcd_009_pe_compression_z_504'] = {'inputs': ['mcd_base_universe_d2_006_mcd_009_pe_compression_z_504'], 'func': mcd_base_universe_d3_006_mcd_009_pe_compression_z_504}


def mcd_base_universe_d3_007_mcd_010_pb_compression_z_756(mcd_base_universe_d2_007_mcd_010_pb_compression_z_756):
    return _base_universe_d3(mcd_base_universe_d2_007_mcd_010_pb_compression_z_756, 7)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_007_mcd_010_pb_compression_z_756'] = {'inputs': ['mcd_base_universe_d2_007_mcd_010_pb_compression_z_756'], 'func': mcd_base_universe_d3_007_mcd_010_pb_compression_z_756}


def mcd_base_universe_d3_008_mcd_011_ps_compression_z_1008(mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008):
    return _base_universe_d3(mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008, 8)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_008_mcd_011_ps_compression_z_1008'] = {'inputs': ['mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008'], 'func': mcd_base_universe_d3_008_mcd_011_ps_compression_z_1008}


def mcd_base_universe_d3_009_mcd_014_dividend_yield_spike_63(mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63):
    return _base_universe_d3(mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63, 9)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_009_mcd_014_dividend_yield_spike_63'] = {'inputs': ['mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63'], 'func': mcd_base_universe_d3_009_mcd_014_dividend_yield_spike_63}


def mcd_base_universe_d3_010_mcd_016_valuation_history_depth_21(mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21):
    return _base_universe_d3(mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21, 10)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_010_mcd_016_valuation_history_depth_21'] = {'inputs': ['mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21'], 'func': mcd_base_universe_d3_010_mcd_016_valuation_history_depth_21}


def mcd_base_universe_d3_011_mcd_021_ev_marketcap_gap_189(mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189):
    return _base_universe_d3(mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189, 11)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_011_mcd_021_ev_marketcap_gap_189'] = {'inputs': ['mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189'], 'func': mcd_base_universe_d3_011_mcd_021_ev_marketcap_gap_189}


def mcd_base_universe_d3_012_mcd_023_earnings_yield_spike_378(mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378):
    return _base_universe_d3(mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378, 12)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_012_mcd_023_earnings_yield_spike_378'] = {'inputs': ['mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378'], 'func': mcd_base_universe_d3_012_mcd_023_earnings_yield_spike_378}


def mcd_base_universe_d3_013_mcd_024_valuation_history_depth_504(mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504):
    return _base_universe_d3(mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504, 13)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_013_mcd_024_valuation_history_depth_504'] = {'inputs': ['mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504'], 'func': mcd_base_universe_d3_013_mcd_024_valuation_history_depth_504}


def mcd_base_universe_d3_014_mcd_027_ps_compression_z_1260(mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260):
    return _base_universe_d3(mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260, 14)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_014_mcd_027_ps_compression_z_1260'] = {'inputs': ['mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260'], 'func': mcd_base_universe_d3_014_mcd_027_ps_compression_z_1260}


def mcd_base_universe_d3_015_mcd_029_ev_marketcap_gap_63(mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63):
    return _base_universe_d3(mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63, 15)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_015_mcd_029_ev_marketcap_gap_63'] = {'inputs': ['mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63'], 'func': mcd_base_universe_d3_015_mcd_029_ev_marketcap_gap_63}


def mcd_base_universe_d3_016_mcd_031_earnings_yield_spike_21(mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21):
    return _base_universe_d3(mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21, 16)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_016_mcd_031_earnings_yield_spike_21'] = {'inputs': ['mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21'], 'func': mcd_base_universe_d3_016_mcd_031_earnings_yield_spike_21}


def mcd_base_universe_d3_017_mcd_032_valuation_history_depth_42(mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42):
    return _base_universe_d3(mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42, 17)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_017_mcd_032_valuation_history_depth_42'] = {'inputs': ['mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42'], 'func': mcd_base_universe_d3_017_mcd_032_valuation_history_depth_42}


def mcd_base_universe_d3_018_mcd_035_ps_compression_z_126(mcd_base_universe_d2_018_mcd_035_ps_compression_z_126):
    return _base_universe_d3(mcd_base_universe_d2_018_mcd_035_ps_compression_z_126, 18)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_018_mcd_035_ps_compression_z_126'] = {'inputs': ['mcd_base_universe_d2_018_mcd_035_ps_compression_z_126'], 'func': mcd_base_universe_d3_018_mcd_035_ps_compression_z_126}


def mcd_base_universe_d3_019_mcd_037_ev_marketcap_gap_252(mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252):
    return _base_universe_d3(mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252, 19)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_019_mcd_037_ev_marketcap_gap_252'] = {'inputs': ['mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252'], 'func': mcd_base_universe_d3_019_mcd_037_ev_marketcap_gap_252}


def mcd_base_universe_d3_020_mcd_039_earnings_yield_spike_504(mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504):
    return _base_universe_d3(mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504, 20)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_020_mcd_039_earnings_yield_spike_504'] = {'inputs': ['mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504'], 'func': mcd_base_universe_d3_020_mcd_039_earnings_yield_spike_504}


def mcd_base_universe_d3_021_mcd_040_valuation_history_depth_756(mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756):
    return _base_universe_d3(mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756, 21)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_021_mcd_040_valuation_history_depth_756'] = {'inputs': ['mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756'], 'func': mcd_base_universe_d3_021_mcd_040_valuation_history_depth_756}


def mcd_base_universe_d3_022_mcd_043_ps_compression_z_1512(mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512):
    return _base_universe_d3(mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512, 22)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_022_mcd_043_ps_compression_z_1512'] = {'inputs': ['mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512'], 'func': mcd_base_universe_d3_022_mcd_043_ps_compression_z_1512}


def mcd_base_universe_d3_023_mcd_047_earnings_yield_spike_42(mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42):
    return _base_universe_d3(mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42, 23)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_023_mcd_047_earnings_yield_spike_42'] = {'inputs': ['mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42'], 'func': mcd_base_universe_d3_023_mcd_047_earnings_yield_spike_42}


def mcd_base_universe_d3_024_mcd_048_valuation_history_depth_63(mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63):
    return _base_universe_d3(mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63, 24)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_024_mcd_048_valuation_history_depth_63'] = {'inputs': ['mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63'], 'func': mcd_base_universe_d3_024_mcd_048_valuation_history_depth_63}


def mcd_base_universe_d3_025_mcd_051_ps_compression_z_189(mcd_base_universe_d2_025_mcd_051_ps_compression_z_189):
    return _base_universe_d3(mcd_base_universe_d2_025_mcd_051_ps_compression_z_189, 25)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_025_mcd_051_ps_compression_z_189'] = {'inputs': ['mcd_base_universe_d2_025_mcd_051_ps_compression_z_189'], 'func': mcd_base_universe_d3_025_mcd_051_ps_compression_z_189}


def mcd_base_universe_d3_026_mcd_053_ev_marketcap_gap_378(mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378):
    return _base_universe_d3(mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378, 26)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_026_mcd_053_ev_marketcap_gap_378'] = {'inputs': ['mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378'], 'func': mcd_base_universe_d3_026_mcd_053_ev_marketcap_gap_378}


def mcd_base_universe_d3_027_mcd_055_earnings_yield_spike_756(mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756):
    return _base_universe_d3(mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756, 27)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_027_mcd_055_earnings_yield_spike_756'] = {'inputs': ['mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756'], 'func': mcd_base_universe_d3_027_mcd_055_earnings_yield_spike_756}


def mcd_base_universe_d3_028_mcd_056_valuation_history_depth_1008(mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008):
    return _base_universe_d3(mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008, 28)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_028_mcd_056_valuation_history_depth_1008'] = {'inputs': ['mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008'], 'func': mcd_base_universe_d3_028_mcd_056_valuation_history_depth_1008}


def mcd_base_universe_d3_029_mcd_061_ev_marketcap_gap_21(mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21):
    return _base_universe_d3(mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21, 29)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_029_mcd_061_ev_marketcap_gap_21'] = {'inputs': ['mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21'], 'func': mcd_base_universe_d3_029_mcd_061_ev_marketcap_gap_21}


def mcd_base_universe_d3_030_mcd_064_valuation_history_depth_84(mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84):
    return _base_universe_d3(mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84, 30)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_030_mcd_064_valuation_history_depth_84'] = {'inputs': ['mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84'], 'func': mcd_base_universe_d3_030_mcd_064_valuation_history_depth_84}


def mcd_base_universe_d3_031_mcd_067_ps_compression_z_252(mcd_base_universe_d2_031_mcd_067_ps_compression_z_252):
    return _base_universe_d3(mcd_base_universe_d2_031_mcd_067_ps_compression_z_252, 31)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_031_mcd_067_ps_compression_z_252'] = {'inputs': ['mcd_base_universe_d2_031_mcd_067_ps_compression_z_252'], 'func': mcd_base_universe_d3_031_mcd_067_ps_compression_z_252}


def mcd_base_universe_d3_032_mcd_069_ev_marketcap_gap_504(mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504):
    return _base_universe_d3(mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504, 32)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_032_mcd_069_ev_marketcap_gap_504'] = {'inputs': ['mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504'], 'func': mcd_base_universe_d3_032_mcd_069_ev_marketcap_gap_504}


def mcd_base_universe_d3_033_mcd_071_earnings_yield_spike_1008(mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008):
    return _base_universe_d3(mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008, 33)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_033_mcd_071_earnings_yield_spike_1008'] = {'inputs': ['mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008'], 'func': mcd_base_universe_d3_033_mcd_071_earnings_yield_spike_1008}


def mcd_base_universe_d3_034_mcd_072_valuation_history_depth_1260(mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260):
    return _base_universe_d3(mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260, 34)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_034_mcd_072_valuation_history_depth_1260'] = {'inputs': ['mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260'], 'func': mcd_base_universe_d3_034_mcd_072_valuation_history_depth_1260}


def mcd_base_universe_d3_035_mcd_basefill_004(mcd_base_universe_d2_035_mcd_basefill_004):
    return _base_universe_d3(mcd_base_universe_d2_035_mcd_basefill_004, 35)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_035_mcd_basefill_004'] = {'inputs': ['mcd_base_universe_d2_035_mcd_basefill_004'], 'func': mcd_base_universe_d3_035_mcd_basefill_004}


def mcd_base_universe_d3_036_mcd_basefill_012(mcd_base_universe_d2_036_mcd_basefill_012):
    return _base_universe_d3(mcd_base_universe_d2_036_mcd_basefill_012, 36)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_036_mcd_basefill_012'] = {'inputs': ['mcd_base_universe_d2_036_mcd_basefill_012'], 'func': mcd_base_universe_d3_036_mcd_basefill_012}


def mcd_base_universe_d3_037_mcd_basefill_015(mcd_base_universe_d2_037_mcd_basefill_015):
    return _base_universe_d3(mcd_base_universe_d2_037_mcd_basefill_015, 37)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_037_mcd_basefill_015'] = {'inputs': ['mcd_base_universe_d2_037_mcd_basefill_015'], 'func': mcd_base_universe_d3_037_mcd_basefill_015}


def mcd_base_universe_d3_038_mcd_basefill_017(mcd_base_universe_d2_038_mcd_basefill_017):
    return _base_universe_d3(mcd_base_universe_d2_038_mcd_basefill_017, 38)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_038_mcd_basefill_017'] = {'inputs': ['mcd_base_universe_d2_038_mcd_basefill_017'], 'func': mcd_base_universe_d3_038_mcd_basefill_017}


def mcd_base_universe_d3_039_mcd_basefill_018(mcd_base_universe_d2_039_mcd_basefill_018):
    return _base_universe_d3(mcd_base_universe_d2_039_mcd_basefill_018, 39)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_039_mcd_basefill_018'] = {'inputs': ['mcd_base_universe_d2_039_mcd_basefill_018'], 'func': mcd_base_universe_d3_039_mcd_basefill_018}


def mcd_base_universe_d3_040_mcd_basefill_020(mcd_base_universe_d2_040_mcd_basefill_020):
    return _base_universe_d3(mcd_base_universe_d2_040_mcd_basefill_020, 40)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_040_mcd_basefill_020'] = {'inputs': ['mcd_base_universe_d2_040_mcd_basefill_020'], 'func': mcd_base_universe_d3_040_mcd_basefill_020}


def mcd_base_universe_d3_041_mcd_basefill_022(mcd_base_universe_d2_041_mcd_basefill_022):
    return _base_universe_d3(mcd_base_universe_d2_041_mcd_basefill_022, 41)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_041_mcd_basefill_022'] = {'inputs': ['mcd_base_universe_d2_041_mcd_basefill_022'], 'func': mcd_base_universe_d3_041_mcd_basefill_022}


def mcd_base_universe_d3_042_mcd_basefill_025(mcd_base_universe_d2_042_mcd_basefill_025):
    return _base_universe_d3(mcd_base_universe_d2_042_mcd_basefill_025, 42)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_042_mcd_basefill_025'] = {'inputs': ['mcd_base_universe_d2_042_mcd_basefill_025'], 'func': mcd_base_universe_d3_042_mcd_basefill_025}


def mcd_base_universe_d3_043_mcd_basefill_026(mcd_base_universe_d2_043_mcd_basefill_026):
    return _base_universe_d3(mcd_base_universe_d2_043_mcd_basefill_026, 43)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_043_mcd_basefill_026'] = {'inputs': ['mcd_base_universe_d2_043_mcd_basefill_026'], 'func': mcd_base_universe_d3_043_mcd_basefill_026}


def mcd_base_universe_d3_044_mcd_basefill_028(mcd_base_universe_d2_044_mcd_basefill_028):
    return _base_universe_d3(mcd_base_universe_d2_044_mcd_basefill_028, 44)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_044_mcd_basefill_028'] = {'inputs': ['mcd_base_universe_d2_044_mcd_basefill_028'], 'func': mcd_base_universe_d3_044_mcd_basefill_028}


def mcd_base_universe_d3_045_mcd_basefill_030(mcd_base_universe_d2_045_mcd_basefill_030):
    return _base_universe_d3(mcd_base_universe_d2_045_mcd_basefill_030, 45)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_045_mcd_basefill_030'] = {'inputs': ['mcd_base_universe_d2_045_mcd_basefill_030'], 'func': mcd_base_universe_d3_045_mcd_basefill_030}


def mcd_base_universe_d3_046_mcd_basefill_033(mcd_base_universe_d2_046_mcd_basefill_033):
    return _base_universe_d3(mcd_base_universe_d2_046_mcd_basefill_033, 46)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_046_mcd_basefill_033'] = {'inputs': ['mcd_base_universe_d2_046_mcd_basefill_033'], 'func': mcd_base_universe_d3_046_mcd_basefill_033}


def mcd_base_universe_d3_047_mcd_basefill_034(mcd_base_universe_d2_047_mcd_basefill_034):
    return _base_universe_d3(mcd_base_universe_d2_047_mcd_basefill_034, 47)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_047_mcd_basefill_034'] = {'inputs': ['mcd_base_universe_d2_047_mcd_basefill_034'], 'func': mcd_base_universe_d3_047_mcd_basefill_034}


def mcd_base_universe_d3_048_mcd_basefill_036(mcd_base_universe_d2_048_mcd_basefill_036):
    return _base_universe_d3(mcd_base_universe_d2_048_mcd_basefill_036, 48)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_048_mcd_basefill_036'] = {'inputs': ['mcd_base_universe_d2_048_mcd_basefill_036'], 'func': mcd_base_universe_d3_048_mcd_basefill_036}


def mcd_base_universe_d3_049_mcd_basefill_038(mcd_base_universe_d2_049_mcd_basefill_038):
    return _base_universe_d3(mcd_base_universe_d2_049_mcd_basefill_038, 49)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_049_mcd_basefill_038'] = {'inputs': ['mcd_base_universe_d2_049_mcd_basefill_038'], 'func': mcd_base_universe_d3_049_mcd_basefill_038}


def mcd_base_universe_d3_050_mcd_basefill_041(mcd_base_universe_d2_050_mcd_basefill_041):
    return _base_universe_d3(mcd_base_universe_d2_050_mcd_basefill_041, 50)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_050_mcd_basefill_041'] = {'inputs': ['mcd_base_universe_d2_050_mcd_basefill_041'], 'func': mcd_base_universe_d3_050_mcd_basefill_041}


def mcd_base_universe_d3_051_mcd_basefill_042(mcd_base_universe_d2_051_mcd_basefill_042):
    return _base_universe_d3(mcd_base_universe_d2_051_mcd_basefill_042, 51)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_051_mcd_basefill_042'] = {'inputs': ['mcd_base_universe_d2_051_mcd_basefill_042'], 'func': mcd_base_universe_d3_051_mcd_basefill_042}


def mcd_base_universe_d3_052_mcd_basefill_044(mcd_base_universe_d2_052_mcd_basefill_044):
    return _base_universe_d3(mcd_base_universe_d2_052_mcd_basefill_044, 52)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_052_mcd_basefill_044'] = {'inputs': ['mcd_base_universe_d2_052_mcd_basefill_044'], 'func': mcd_base_universe_d3_052_mcd_basefill_044}


def mcd_base_universe_d3_053_mcd_basefill_045(mcd_base_universe_d2_053_mcd_basefill_045):
    return _base_universe_d3(mcd_base_universe_d2_053_mcd_basefill_045, 53)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_053_mcd_basefill_045'] = {'inputs': ['mcd_base_universe_d2_053_mcd_basefill_045'], 'func': mcd_base_universe_d3_053_mcd_basefill_045}


def mcd_base_universe_d3_054_mcd_basefill_046(mcd_base_universe_d2_054_mcd_basefill_046):
    return _base_universe_d3(mcd_base_universe_d2_054_mcd_basefill_046, 54)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_054_mcd_basefill_046'] = {'inputs': ['mcd_base_universe_d2_054_mcd_basefill_046'], 'func': mcd_base_universe_d3_054_mcd_basefill_046}


def mcd_base_universe_d3_055_mcd_basefill_049(mcd_base_universe_d2_055_mcd_basefill_049):
    return _base_universe_d3(mcd_base_universe_d2_055_mcd_basefill_049, 55)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_055_mcd_basefill_049'] = {'inputs': ['mcd_base_universe_d2_055_mcd_basefill_049'], 'func': mcd_base_universe_d3_055_mcd_basefill_049}


def mcd_base_universe_d3_056_mcd_basefill_050(mcd_base_universe_d2_056_mcd_basefill_050):
    return _base_universe_d3(mcd_base_universe_d2_056_mcd_basefill_050, 56)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_056_mcd_basefill_050'] = {'inputs': ['mcd_base_universe_d2_056_mcd_basefill_050'], 'func': mcd_base_universe_d3_056_mcd_basefill_050}


def mcd_base_universe_d3_057_mcd_basefill_052(mcd_base_universe_d2_057_mcd_basefill_052):
    return _base_universe_d3(mcd_base_universe_d2_057_mcd_basefill_052, 57)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_057_mcd_basefill_052'] = {'inputs': ['mcd_base_universe_d2_057_mcd_basefill_052'], 'func': mcd_base_universe_d3_057_mcd_basefill_052}


def mcd_base_universe_d3_058_mcd_basefill_054(mcd_base_universe_d2_058_mcd_basefill_054):
    return _base_universe_d3(mcd_base_universe_d2_058_mcd_basefill_054, 58)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_058_mcd_basefill_054'] = {'inputs': ['mcd_base_universe_d2_058_mcd_basefill_054'], 'func': mcd_base_universe_d3_058_mcd_basefill_054}


def mcd_base_universe_d3_059_mcd_basefill_057(mcd_base_universe_d2_059_mcd_basefill_057):
    return _base_universe_d3(mcd_base_universe_d2_059_mcd_basefill_057, 59)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_059_mcd_basefill_057'] = {'inputs': ['mcd_base_universe_d2_059_mcd_basefill_057'], 'func': mcd_base_universe_d3_059_mcd_basefill_057}


def mcd_base_universe_d3_060_mcd_basefill_058(mcd_base_universe_d2_060_mcd_basefill_058):
    return _base_universe_d3(mcd_base_universe_d2_060_mcd_basefill_058, 60)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_060_mcd_basefill_058'] = {'inputs': ['mcd_base_universe_d2_060_mcd_basefill_058'], 'func': mcd_base_universe_d3_060_mcd_basefill_058}


def mcd_base_universe_d3_061_mcd_basefill_059(mcd_base_universe_d2_061_mcd_basefill_059):
    return _base_universe_d3(mcd_base_universe_d2_061_mcd_basefill_059, 61)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_061_mcd_basefill_059'] = {'inputs': ['mcd_base_universe_d2_061_mcd_basefill_059'], 'func': mcd_base_universe_d3_061_mcd_basefill_059}


def mcd_base_universe_d3_062_mcd_basefill_060(mcd_base_universe_d2_062_mcd_basefill_060):
    return _base_universe_d3(mcd_base_universe_d2_062_mcd_basefill_060, 62)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_062_mcd_basefill_060'] = {'inputs': ['mcd_base_universe_d2_062_mcd_basefill_060'], 'func': mcd_base_universe_d3_062_mcd_basefill_060}


def mcd_base_universe_d3_063_mcd_basefill_062(mcd_base_universe_d2_063_mcd_basefill_062):
    return _base_universe_d3(mcd_base_universe_d2_063_mcd_basefill_062, 63)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_063_mcd_basefill_062'] = {'inputs': ['mcd_base_universe_d2_063_mcd_basefill_062'], 'func': mcd_base_universe_d3_063_mcd_basefill_062}


def mcd_base_universe_d3_064_mcd_basefill_063(mcd_base_universe_d2_064_mcd_basefill_063):
    return _base_universe_d3(mcd_base_universe_d2_064_mcd_basefill_063, 64)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_064_mcd_basefill_063'] = {'inputs': ['mcd_base_universe_d2_064_mcd_basefill_063'], 'func': mcd_base_universe_d3_064_mcd_basefill_063}


def mcd_base_universe_d3_065_mcd_basefill_065(mcd_base_universe_d2_065_mcd_basefill_065):
    return _base_universe_d3(mcd_base_universe_d2_065_mcd_basefill_065, 65)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_065_mcd_basefill_065'] = {'inputs': ['mcd_base_universe_d2_065_mcd_basefill_065'], 'func': mcd_base_universe_d3_065_mcd_basefill_065}


def mcd_base_universe_d3_066_mcd_basefill_066(mcd_base_universe_d2_066_mcd_basefill_066):
    return _base_universe_d3(mcd_base_universe_d2_066_mcd_basefill_066, 66)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_066_mcd_basefill_066'] = {'inputs': ['mcd_base_universe_d2_066_mcd_basefill_066'], 'func': mcd_base_universe_d3_066_mcd_basefill_066}


def mcd_base_universe_d3_067_mcd_basefill_068(mcd_base_universe_d2_067_mcd_basefill_068):
    return _base_universe_d3(mcd_base_universe_d2_067_mcd_basefill_068, 67)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_067_mcd_basefill_068'] = {'inputs': ['mcd_base_universe_d2_067_mcd_basefill_068'], 'func': mcd_base_universe_d3_067_mcd_basefill_068}


def mcd_base_universe_d3_068_mcd_basefill_070(mcd_base_universe_d2_068_mcd_basefill_070):
    return _base_universe_d3(mcd_base_universe_d2_068_mcd_basefill_070, 68)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_068_mcd_basefill_070'] = {'inputs': ['mcd_base_universe_d2_068_mcd_basefill_070'], 'func': mcd_base_universe_d3_068_mcd_basefill_070}


def mcd_base_universe_d3_069_mcd_basefill_073(mcd_base_universe_d2_069_mcd_basefill_073):
    return _base_universe_d3(mcd_base_universe_d2_069_mcd_basefill_073, 69)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_069_mcd_basefill_073'] = {'inputs': ['mcd_base_universe_d2_069_mcd_basefill_073'], 'func': mcd_base_universe_d3_069_mcd_basefill_073}


def mcd_base_universe_d3_070_mcd_basefill_074(mcd_base_universe_d2_070_mcd_basefill_074):
    return _base_universe_d3(mcd_base_universe_d2_070_mcd_basefill_074, 70)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_070_mcd_basefill_074'] = {'inputs': ['mcd_base_universe_d2_070_mcd_basefill_074'], 'func': mcd_base_universe_d3_070_mcd_basefill_074}


def mcd_base_universe_d3_071_mcd_basefill_075(mcd_base_universe_d2_071_mcd_basefill_075):
    return _base_universe_d3(mcd_base_universe_d2_071_mcd_basefill_075, 71)
MCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mcd_base_universe_d3_071_mcd_basefill_075'] = {'inputs': ['mcd_base_universe_d2_071_mcd_basefill_075'], 'func': mcd_base_universe_d3_071_mcd_basefill_075}
