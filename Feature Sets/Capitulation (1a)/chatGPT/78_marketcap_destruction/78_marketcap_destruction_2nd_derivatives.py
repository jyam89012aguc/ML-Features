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



def mcd_151_mcd_001_pe_compression_z_21_roc_1(mcd_001_pe_compression_z_21):
    feature = _s(mcd_001_pe_compression_z_21)
    return (_roc(feature, 1)).reindex(feature.index)

def mcd_152_mcd_007_earnings_yield_spike_252_roc_42(mcd_007_earnings_yield_spike_252):
    feature = _s(mcd_007_earnings_yield_spike_252)
    return (_roc(feature, 42)).reindex(feature.index)

def mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126(mcd_013_ev_marketcap_gap_1512):
    feature = _s(mcd_013_ev_marketcap_gap_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def mcd_154_mcd_019_ps_compression_z_84_roc_378(mcd_019_ps_compression_z_84):
    feature = _s(mcd_019_ps_compression_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def mcd_155_mcd_025_pe_compression_z_756_roc_4(mcd_025_pe_compression_z_756):
    feature = _s(mcd_025_pe_compression_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















MARKETCAP_DESTRUCTION_REGISTRY_2ND_DERIVATIVES = {
    'mcd_151_mcd_001_pe_compression_z_21_roc_1': {'inputs': ['mcd_001_pe_compression_z_21'], 'func': mcd_151_mcd_001_pe_compression_z_21_roc_1},
    'mcd_152_mcd_007_earnings_yield_spike_252_roc_42': {'inputs': ['mcd_007_earnings_yield_spike_252'], 'func': mcd_152_mcd_007_earnings_yield_spike_252_roc_42},
    'mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126': {'inputs': ['mcd_013_ev_marketcap_gap_1512'], 'func': mcd_153_mcd_013_ev_marketcap_gap_1512_roc_126},
    'mcd_154_mcd_019_ps_compression_z_84_roc_378': {'inputs': ['mcd_019_ps_compression_z_84'], 'func': mcd_154_mcd_019_ps_compression_z_84_roc_378},
    'mcd_155_mcd_025_pe_compression_z_756_roc_4': {'inputs': ['mcd_025_pe_compression_z_756'], 'func': mcd_155_mcd_025_pe_compression_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def md_replacement_d2_001(mcd_025_pe_compression_z_756):
    feature = _clean(mcd_025_pe_compression_z_756)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_001'] = {'inputs': ['mcd_025_pe_compression_z_756'], 'func': md_replacement_d2_001}


def md_replacement_d2_002(md_replacement_001):
    feature = _clean(md_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_002'] = {'inputs': ['md_replacement_001'], 'func': md_replacement_d2_002}


def md_replacement_d2_003(md_replacement_002):
    feature = _clean(md_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_003'] = {'inputs': ['md_replacement_002'], 'func': md_replacement_d2_003}


def md_replacement_d2_004(md_replacement_003):
    feature = _clean(md_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_004'] = {'inputs': ['md_replacement_003'], 'func': md_replacement_d2_004}


def md_replacement_d2_005(md_replacement_004):
    feature = _clean(md_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_005'] = {'inputs': ['md_replacement_004'], 'func': md_replacement_d2_005}


def md_replacement_d2_006(md_replacement_005):
    feature = _clean(md_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_006'] = {'inputs': ['md_replacement_005'], 'func': md_replacement_d2_006}


def md_replacement_d2_007(md_replacement_006):
    feature = _clean(md_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_007'] = {'inputs': ['md_replacement_006'], 'func': md_replacement_d2_007}


def md_replacement_d2_008(md_replacement_007):
    feature = _clean(md_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_008'] = {'inputs': ['md_replacement_007'], 'func': md_replacement_d2_008}


def md_replacement_d2_009(md_replacement_008):
    feature = _clean(md_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_009'] = {'inputs': ['md_replacement_008'], 'func': md_replacement_d2_009}


def md_replacement_d2_010(md_replacement_009):
    feature = _clean(md_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_010'] = {'inputs': ['md_replacement_009'], 'func': md_replacement_d2_010}


def md_replacement_d2_011(md_replacement_010):
    feature = _clean(md_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_011'] = {'inputs': ['md_replacement_010'], 'func': md_replacement_d2_011}


def md_replacement_d2_012(md_replacement_011):
    feature = _clean(md_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_012'] = {'inputs': ['md_replacement_011'], 'func': md_replacement_d2_012}


def md_replacement_d2_013(md_replacement_012):
    feature = _clean(md_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_013'] = {'inputs': ['md_replacement_012'], 'func': md_replacement_d2_013}


def md_replacement_d2_014(md_replacement_013):
    feature = _clean(md_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_014'] = {'inputs': ['md_replacement_013'], 'func': md_replacement_d2_014}


def md_replacement_d2_015(md_replacement_014):
    feature = _clean(md_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_015'] = {'inputs': ['md_replacement_014'], 'func': md_replacement_d2_015}


def md_replacement_d2_016(md_replacement_015):
    feature = _clean(md_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_016'] = {'inputs': ['md_replacement_015'], 'func': md_replacement_d2_016}


def md_replacement_d2_017(md_replacement_016):
    feature = _clean(md_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_017'] = {'inputs': ['md_replacement_016'], 'func': md_replacement_d2_017}


def md_replacement_d2_018(md_replacement_017):
    feature = _clean(md_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_018'] = {'inputs': ['md_replacement_017'], 'func': md_replacement_d2_018}


def md_replacement_d2_019(md_replacement_018):
    feature = _clean(md_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_019'] = {'inputs': ['md_replacement_018'], 'func': md_replacement_d2_019}


def md_replacement_d2_020(md_replacement_019):
    feature = _clean(md_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_020'] = {'inputs': ['md_replacement_019'], 'func': md_replacement_d2_020}


def md_replacement_d2_021(md_replacement_020):
    feature = _clean(md_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_021'] = {'inputs': ['md_replacement_020'], 'func': md_replacement_d2_021}


def md_replacement_d2_022(md_replacement_021):
    feature = _clean(md_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_022'] = {'inputs': ['md_replacement_021'], 'func': md_replacement_d2_022}


def md_replacement_d2_023(md_replacement_022):
    feature = _clean(md_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_023'] = {'inputs': ['md_replacement_022'], 'func': md_replacement_d2_023}


def md_replacement_d2_024(md_replacement_023):
    feature = _clean(md_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_024'] = {'inputs': ['md_replacement_023'], 'func': md_replacement_d2_024}


def md_replacement_d2_025(md_replacement_024):
    feature = _clean(md_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_025'] = {'inputs': ['md_replacement_024'], 'func': md_replacement_d2_025}


def md_replacement_d2_026(md_replacement_025):
    feature = _clean(md_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_026'] = {'inputs': ['md_replacement_025'], 'func': md_replacement_d2_026}


def md_replacement_d2_027(md_replacement_026):
    feature = _clean(md_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_027'] = {'inputs': ['md_replacement_026'], 'func': md_replacement_d2_027}


def md_replacement_d2_028(md_replacement_027):
    feature = _clean(md_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_028'] = {'inputs': ['md_replacement_027'], 'func': md_replacement_d2_028}


def md_replacement_d2_029(md_replacement_028):
    feature = _clean(md_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_029'] = {'inputs': ['md_replacement_028'], 'func': md_replacement_d2_029}


def md_replacement_d2_030(md_replacement_029):
    feature = _clean(md_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_030'] = {'inputs': ['md_replacement_029'], 'func': md_replacement_d2_030}


def md_replacement_d2_031(md_replacement_030):
    feature = _clean(md_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_031'] = {'inputs': ['md_replacement_030'], 'func': md_replacement_d2_031}


def md_replacement_d2_032(md_replacement_031):
    feature = _clean(md_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_032'] = {'inputs': ['md_replacement_031'], 'func': md_replacement_d2_032}


def md_replacement_d2_033(md_replacement_032):
    feature = _clean(md_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_033'] = {'inputs': ['md_replacement_032'], 'func': md_replacement_d2_033}


def md_replacement_d2_034(md_replacement_033):
    feature = _clean(md_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_034'] = {'inputs': ['md_replacement_033'], 'func': md_replacement_d2_034}


def md_replacement_d2_035(md_replacement_034):
    feature = _clean(md_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_035'] = {'inputs': ['md_replacement_034'], 'func': md_replacement_d2_035}


def md_replacement_d2_036(md_replacement_035):
    feature = _clean(md_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_036'] = {'inputs': ['md_replacement_035'], 'func': md_replacement_d2_036}


def md_replacement_d2_037(md_replacement_036):
    feature = _clean(md_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_037'] = {'inputs': ['md_replacement_036'], 'func': md_replacement_d2_037}


def md_replacement_d2_038(md_replacement_037):
    feature = _clean(md_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_038'] = {'inputs': ['md_replacement_037'], 'func': md_replacement_d2_038}


def md_replacement_d2_039(md_replacement_038):
    feature = _clean(md_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_039'] = {'inputs': ['md_replacement_038'], 'func': md_replacement_d2_039}


def md_replacement_d2_040(md_replacement_039):
    feature = _clean(md_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_040'] = {'inputs': ['md_replacement_039'], 'func': md_replacement_d2_040}


def md_replacement_d2_041(md_replacement_040):
    feature = _clean(md_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_041'] = {'inputs': ['md_replacement_040'], 'func': md_replacement_d2_041}


def md_replacement_d2_042(md_replacement_041):
    feature = _clean(md_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_042'] = {'inputs': ['md_replacement_041'], 'func': md_replacement_d2_042}


def md_replacement_d2_043(md_replacement_042):
    feature = _clean(md_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_043'] = {'inputs': ['md_replacement_042'], 'func': md_replacement_d2_043}


def md_replacement_d2_044(md_replacement_043):
    feature = _clean(md_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_044'] = {'inputs': ['md_replacement_043'], 'func': md_replacement_d2_044}


def md_replacement_d2_045(md_replacement_044):
    feature = _clean(md_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_045'] = {'inputs': ['md_replacement_044'], 'func': md_replacement_d2_045}


def md_replacement_d2_046(md_replacement_045):
    feature = _clean(md_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_046'] = {'inputs': ['md_replacement_045'], 'func': md_replacement_d2_046}


def md_replacement_d2_047(md_replacement_046):
    feature = _clean(md_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_047'] = {'inputs': ['md_replacement_046'], 'func': md_replacement_d2_047}


def md_replacement_d2_048(md_replacement_047):
    feature = _clean(md_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_048'] = {'inputs': ['md_replacement_047'], 'func': md_replacement_d2_048}


def md_replacement_d2_049(md_replacement_048):
    feature = _clean(md_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_049'] = {'inputs': ['md_replacement_048'], 'func': md_replacement_d2_049}


def md_replacement_d2_050(md_replacement_049):
    feature = _clean(md_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_050'] = {'inputs': ['md_replacement_049'], 'func': md_replacement_d2_050}


def md_replacement_d2_051(md_replacement_050):
    feature = _clean(md_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_051'] = {'inputs': ['md_replacement_050'], 'func': md_replacement_d2_051}


def md_replacement_d2_052(md_replacement_051):
    feature = _clean(md_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_052'] = {'inputs': ['md_replacement_051'], 'func': md_replacement_d2_052}


def md_replacement_d2_053(md_replacement_052):
    feature = _clean(md_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_053'] = {'inputs': ['md_replacement_052'], 'func': md_replacement_d2_053}


def md_replacement_d2_054(md_replacement_053):
    feature = _clean(md_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_054'] = {'inputs': ['md_replacement_053'], 'func': md_replacement_d2_054}


def md_replacement_d2_055(md_replacement_054):
    feature = _clean(md_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_055'] = {'inputs': ['md_replacement_054'], 'func': md_replacement_d2_055}


def md_replacement_d2_056(md_replacement_055):
    feature = _clean(md_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_056'] = {'inputs': ['md_replacement_055'], 'func': md_replacement_d2_056}


def md_replacement_d2_057(md_replacement_056):
    feature = _clean(md_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_057'] = {'inputs': ['md_replacement_056'], 'func': md_replacement_d2_057}


def md_replacement_d2_058(md_replacement_057):
    feature = _clean(md_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_058'] = {'inputs': ['md_replacement_057'], 'func': md_replacement_d2_058}


def md_replacement_d2_059(md_replacement_058):
    feature = _clean(md_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_059'] = {'inputs': ['md_replacement_058'], 'func': md_replacement_d2_059}


def md_replacement_d2_060(md_replacement_059):
    feature = _clean(md_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_060'] = {'inputs': ['md_replacement_059'], 'func': md_replacement_d2_060}


def md_replacement_d2_061(md_replacement_060):
    feature = _clean(md_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_061'] = {'inputs': ['md_replacement_060'], 'func': md_replacement_d2_061}


def md_replacement_d2_062(md_replacement_061):
    feature = _clean(md_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_062'] = {'inputs': ['md_replacement_061'], 'func': md_replacement_d2_062}


def md_replacement_d2_063(md_replacement_062):
    feature = _clean(md_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_063'] = {'inputs': ['md_replacement_062'], 'func': md_replacement_d2_063}


def md_replacement_d2_064(md_replacement_063):
    feature = _clean(md_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_064'] = {'inputs': ['md_replacement_063'], 'func': md_replacement_d2_064}


def md_replacement_d2_065(md_replacement_064):
    feature = _clean(md_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_065'] = {'inputs': ['md_replacement_064'], 'func': md_replacement_d2_065}


def md_replacement_d2_066(md_replacement_065):
    feature = _clean(md_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_066'] = {'inputs': ['md_replacement_065'], 'func': md_replacement_d2_066}


def md_replacement_d2_067(md_replacement_066):
    feature = _clean(md_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_067'] = {'inputs': ['md_replacement_066'], 'func': md_replacement_d2_067}


def md_replacement_d2_068(md_replacement_067):
    feature = _clean(md_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_068'] = {'inputs': ['md_replacement_067'], 'func': md_replacement_d2_068}


def md_replacement_d2_069(md_replacement_068):
    feature = _clean(md_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_069'] = {'inputs': ['md_replacement_068'], 'func': md_replacement_d2_069}


def md_replacement_d2_070(md_replacement_069):
    feature = _clean(md_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_070'] = {'inputs': ['md_replacement_069'], 'func': md_replacement_d2_070}


def md_replacement_d2_071(md_replacement_070):
    feature = _clean(md_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_071'] = {'inputs': ['md_replacement_070'], 'func': md_replacement_d2_071}


def md_replacement_d2_072(md_replacement_071):
    feature = _clean(md_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_072'] = {'inputs': ['md_replacement_071'], 'func': md_replacement_d2_072}


def md_replacement_d2_073(md_replacement_072):
    feature = _clean(md_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_073'] = {'inputs': ['md_replacement_072'], 'func': md_replacement_d2_073}


def md_replacement_d2_074(md_replacement_073):
    feature = _clean(md_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_074'] = {'inputs': ['md_replacement_073'], 'func': md_replacement_d2_074}


def md_replacement_d2_075(md_replacement_074):
    feature = _clean(md_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_075'] = {'inputs': ['md_replacement_074'], 'func': md_replacement_d2_075}


def md_replacement_d2_076(md_replacement_075):
    feature = _clean(md_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_076'] = {'inputs': ['md_replacement_075'], 'func': md_replacement_d2_076}


def md_replacement_d2_077(md_replacement_076):
    feature = _clean(md_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_077'] = {'inputs': ['md_replacement_076'], 'func': md_replacement_d2_077}


def md_replacement_d2_078(md_replacement_077):
    feature = _clean(md_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_078'] = {'inputs': ['md_replacement_077'], 'func': md_replacement_d2_078}


def md_replacement_d2_079(md_replacement_078):
    feature = _clean(md_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_079'] = {'inputs': ['md_replacement_078'], 'func': md_replacement_d2_079}


def md_replacement_d2_080(md_replacement_079):
    feature = _clean(md_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_080'] = {'inputs': ['md_replacement_079'], 'func': md_replacement_d2_080}


def md_replacement_d2_081(md_replacement_080):
    feature = _clean(md_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_081'] = {'inputs': ['md_replacement_080'], 'func': md_replacement_d2_081}


def md_replacement_d2_082(md_replacement_081):
    feature = _clean(md_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_082'] = {'inputs': ['md_replacement_081'], 'func': md_replacement_d2_082}


def md_replacement_d2_083(md_replacement_082):
    feature = _clean(md_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_083'] = {'inputs': ['md_replacement_082'], 'func': md_replacement_d2_083}


def md_replacement_d2_084(md_replacement_083):
    feature = _clean(md_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_084'] = {'inputs': ['md_replacement_083'], 'func': md_replacement_d2_084}


def md_replacement_d2_085(md_replacement_084):
    feature = _clean(md_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_085'] = {'inputs': ['md_replacement_084'], 'func': md_replacement_d2_085}


def md_replacement_d2_086(md_replacement_085):
    feature = _clean(md_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_086'] = {'inputs': ['md_replacement_085'], 'func': md_replacement_d2_086}


def md_replacement_d2_087(md_replacement_086):
    feature = _clean(md_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_087'] = {'inputs': ['md_replacement_086'], 'func': md_replacement_d2_087}


def md_replacement_d2_088(md_replacement_087):
    feature = _clean(md_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_088'] = {'inputs': ['md_replacement_087'], 'func': md_replacement_d2_088}


def md_replacement_d2_089(md_replacement_088):
    feature = _clean(md_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_089'] = {'inputs': ['md_replacement_088'], 'func': md_replacement_d2_089}


def md_replacement_d2_090(md_replacement_089):
    feature = _clean(md_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_090'] = {'inputs': ['md_replacement_089'], 'func': md_replacement_d2_090}


def md_replacement_d2_091(md_replacement_090):
    feature = _clean(md_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_091'] = {'inputs': ['md_replacement_090'], 'func': md_replacement_d2_091}


def md_replacement_d2_092(md_replacement_091):
    feature = _clean(md_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_092'] = {'inputs': ['md_replacement_091'], 'func': md_replacement_d2_092}


def md_replacement_d2_093(md_replacement_092):
    feature = _clean(md_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_093'] = {'inputs': ['md_replacement_092'], 'func': md_replacement_d2_093}


def md_replacement_d2_094(md_replacement_093):
    feature = _clean(md_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_094'] = {'inputs': ['md_replacement_093'], 'func': md_replacement_d2_094}


def md_replacement_d2_095(md_replacement_094):
    feature = _clean(md_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_095'] = {'inputs': ['md_replacement_094'], 'func': md_replacement_d2_095}


def md_replacement_d2_096(md_replacement_095):
    feature = _clean(md_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_096'] = {'inputs': ['md_replacement_095'], 'func': md_replacement_d2_096}


def md_replacement_d2_097(md_replacement_096):
    feature = _clean(md_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_097'] = {'inputs': ['md_replacement_096'], 'func': md_replacement_d2_097}


def md_replacement_d2_098(md_replacement_097):
    feature = _clean(md_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_098'] = {'inputs': ['md_replacement_097'], 'func': md_replacement_d2_098}


def md_replacement_d2_099(md_replacement_098):
    feature = _clean(md_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_099'] = {'inputs': ['md_replacement_098'], 'func': md_replacement_d2_099}


def md_replacement_d2_100(md_replacement_099):
    feature = _clean(md_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_100'] = {'inputs': ['md_replacement_099'], 'func': md_replacement_d2_100}


def md_replacement_d2_101(md_replacement_100):
    feature = _clean(md_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_101'] = {'inputs': ['md_replacement_100'], 'func': md_replacement_d2_101}


def md_replacement_d2_102(md_replacement_101):
    feature = _clean(md_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_102'] = {'inputs': ['md_replacement_101'], 'func': md_replacement_d2_102}


def md_replacement_d2_103(md_replacement_102):
    feature = _clean(md_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_103'] = {'inputs': ['md_replacement_102'], 'func': md_replacement_d2_103}


def md_replacement_d2_104(md_replacement_103):
    feature = _clean(md_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_104'] = {'inputs': ['md_replacement_103'], 'func': md_replacement_d2_104}


def md_replacement_d2_105(md_replacement_104):
    feature = _clean(md_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_105'] = {'inputs': ['md_replacement_104'], 'func': md_replacement_d2_105}


def md_replacement_d2_106(md_replacement_105):
    feature = _clean(md_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_106'] = {'inputs': ['md_replacement_105'], 'func': md_replacement_d2_106}


def md_replacement_d2_107(md_replacement_106):
    feature = _clean(md_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_107'] = {'inputs': ['md_replacement_106'], 'func': md_replacement_d2_107}


def md_replacement_d2_108(md_replacement_107):
    feature = _clean(md_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_108'] = {'inputs': ['md_replacement_107'], 'func': md_replacement_d2_108}


def md_replacement_d2_109(md_replacement_108):
    feature = _clean(md_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_109'] = {'inputs': ['md_replacement_108'], 'func': md_replacement_d2_109}


def md_replacement_d2_110(md_replacement_109):
    feature = _clean(md_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_110'] = {'inputs': ['md_replacement_109'], 'func': md_replacement_d2_110}


def md_replacement_d2_111(md_replacement_110):
    feature = _clean(md_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_111'] = {'inputs': ['md_replacement_110'], 'func': md_replacement_d2_111}


def md_replacement_d2_112(md_replacement_111):
    feature = _clean(md_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_112'] = {'inputs': ['md_replacement_111'], 'func': md_replacement_d2_112}


def md_replacement_d2_113(md_replacement_112):
    feature = _clean(md_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_113'] = {'inputs': ['md_replacement_112'], 'func': md_replacement_d2_113}


def md_replacement_d2_114(md_replacement_113):
    feature = _clean(md_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_114'] = {'inputs': ['md_replacement_113'], 'func': md_replacement_d2_114}


def md_replacement_d2_115(md_replacement_114):
    feature = _clean(md_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_115'] = {'inputs': ['md_replacement_114'], 'func': md_replacement_d2_115}


def md_replacement_d2_116(md_replacement_115):
    feature = _clean(md_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_116'] = {'inputs': ['md_replacement_115'], 'func': md_replacement_d2_116}


def md_replacement_d2_117(md_replacement_116):
    feature = _clean(md_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_117'] = {'inputs': ['md_replacement_116'], 'func': md_replacement_d2_117}


def md_replacement_d2_118(md_replacement_117):
    feature = _clean(md_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_118'] = {'inputs': ['md_replacement_117'], 'func': md_replacement_d2_118}


def md_replacement_d2_119(md_replacement_118):
    feature = _clean(md_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_119'] = {'inputs': ['md_replacement_118'], 'func': md_replacement_d2_119}


def md_replacement_d2_120(md_replacement_119):
    feature = _clean(md_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_120'] = {'inputs': ['md_replacement_119'], 'func': md_replacement_d2_120}


def md_replacement_d2_121(md_replacement_120):
    feature = _clean(md_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_121'] = {'inputs': ['md_replacement_120'], 'func': md_replacement_d2_121}


def md_replacement_d2_122(md_replacement_121):
    feature = _clean(md_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_122'] = {'inputs': ['md_replacement_121'], 'func': md_replacement_d2_122}


def md_replacement_d2_123(md_replacement_122):
    feature = _clean(md_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_123'] = {'inputs': ['md_replacement_122'], 'func': md_replacement_d2_123}


def md_replacement_d2_124(md_replacement_123):
    feature = _clean(md_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_124'] = {'inputs': ['md_replacement_123'], 'func': md_replacement_d2_124}


def md_replacement_d2_125(md_replacement_124):
    feature = _clean(md_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_125'] = {'inputs': ['md_replacement_124'], 'func': md_replacement_d2_125}


def md_replacement_d2_126(md_replacement_125):
    feature = _clean(md_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_126'] = {'inputs': ['md_replacement_125'], 'func': md_replacement_d2_126}


def md_replacement_d2_127(md_replacement_126):
    feature = _clean(md_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_127'] = {'inputs': ['md_replacement_126'], 'func': md_replacement_d2_127}


def md_replacement_d2_128(md_replacement_127):
    feature = _clean(md_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_128'] = {'inputs': ['md_replacement_127'], 'func': md_replacement_d2_128}


def md_replacement_d2_129(md_replacement_128):
    feature = _clean(md_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_129'] = {'inputs': ['md_replacement_128'], 'func': md_replacement_d2_129}


def md_replacement_d2_130(md_replacement_129):
    feature = _clean(md_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_130'] = {'inputs': ['md_replacement_129'], 'func': md_replacement_d2_130}


def md_replacement_d2_131(md_replacement_130):
    feature = _clean(md_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_131'] = {'inputs': ['md_replacement_130'], 'func': md_replacement_d2_131}


def md_replacement_d2_132(md_replacement_131):
    feature = _clean(md_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_132'] = {'inputs': ['md_replacement_131'], 'func': md_replacement_d2_132}


def md_replacement_d2_133(md_replacement_132):
    feature = _clean(md_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_133'] = {'inputs': ['md_replacement_132'], 'func': md_replacement_d2_133}


def md_replacement_d2_134(md_replacement_133):
    feature = _clean(md_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_134'] = {'inputs': ['md_replacement_133'], 'func': md_replacement_d2_134}


def md_replacement_d2_135(md_replacement_134):
    feature = _clean(md_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_135'] = {'inputs': ['md_replacement_134'], 'func': md_replacement_d2_135}


def md_replacement_d2_136(md_replacement_135):
    feature = _clean(md_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_136'] = {'inputs': ['md_replacement_135'], 'func': md_replacement_d2_136}


def md_replacement_d2_137(md_replacement_136):
    feature = _clean(md_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_137'] = {'inputs': ['md_replacement_136'], 'func': md_replacement_d2_137}


def md_replacement_d2_138(md_replacement_137):
    feature = _clean(md_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_138'] = {'inputs': ['md_replacement_137'], 'func': md_replacement_d2_138}


# Base-universe derivative extensions for repaired first-base features.
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mcd_base_universe_d2_001_mcd_002_pb_compression_z_42(mcd_002_pb_compression_z_42):
    return _base_universe_d2(mcd_002_pb_compression_z_42, 1)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_001_mcd_002_pb_compression_z_42'] = {'inputs': ['mcd_002_pb_compression_z_42'], 'func': mcd_base_universe_d2_001_mcd_002_pb_compression_z_42}


def mcd_base_universe_d2_002_mcd_003_ps_compression_z_63(mcd_003_ps_compression_z_63):
    return _base_universe_d2(mcd_003_ps_compression_z_63, 2)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_002_mcd_003_ps_compression_z_63'] = {'inputs': ['mcd_003_ps_compression_z_63'], 'func': mcd_base_universe_d2_002_mcd_003_ps_compression_z_63}


def mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126(mcd_005_ev_marketcap_gap_126):
    return _base_universe_d2(mcd_005_ev_marketcap_gap_126, 3)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126'] = {'inputs': ['mcd_005_ev_marketcap_gap_126'], 'func': mcd_base_universe_d2_003_mcd_005_ev_marketcap_gap_126}


def mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189(mcd_006_dividend_yield_spike_189):
    return _base_universe_d2(mcd_006_dividend_yield_spike_189, 4)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189'] = {'inputs': ['mcd_006_dividend_yield_spike_189'], 'func': mcd_base_universe_d2_004_mcd_006_dividend_yield_spike_189}


def mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378(mcd_008_valuation_history_depth_378):
    return _base_universe_d2(mcd_008_valuation_history_depth_378, 5)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378'] = {'inputs': ['mcd_008_valuation_history_depth_378'], 'func': mcd_base_universe_d2_005_mcd_008_valuation_history_depth_378}


def mcd_base_universe_d2_006_mcd_009_pe_compression_z_504(mcd_009_pe_compression_z_504):
    return _base_universe_d2(mcd_009_pe_compression_z_504, 6)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_006_mcd_009_pe_compression_z_504'] = {'inputs': ['mcd_009_pe_compression_z_504'], 'func': mcd_base_universe_d2_006_mcd_009_pe_compression_z_504}


def mcd_base_universe_d2_007_mcd_010_pb_compression_z_756(mcd_010_pb_compression_z_756):
    return _base_universe_d2(mcd_010_pb_compression_z_756, 7)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_007_mcd_010_pb_compression_z_756'] = {'inputs': ['mcd_010_pb_compression_z_756'], 'func': mcd_base_universe_d2_007_mcd_010_pb_compression_z_756}


def mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008(mcd_011_ps_compression_z_1008):
    return _base_universe_d2(mcd_011_ps_compression_z_1008, 8)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008'] = {'inputs': ['mcd_011_ps_compression_z_1008'], 'func': mcd_base_universe_d2_008_mcd_011_ps_compression_z_1008}


def mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63(mcd_014_dividend_yield_spike_63):
    return _base_universe_d2(mcd_014_dividend_yield_spike_63, 9)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63'] = {'inputs': ['mcd_014_dividend_yield_spike_63'], 'func': mcd_base_universe_d2_009_mcd_014_dividend_yield_spike_63}


def mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21(mcd_016_valuation_history_depth_21):
    return _base_universe_d2(mcd_016_valuation_history_depth_21, 10)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21'] = {'inputs': ['mcd_016_valuation_history_depth_21'], 'func': mcd_base_universe_d2_010_mcd_016_valuation_history_depth_21}


def mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189(mcd_021_ev_marketcap_gap_189):
    return _base_universe_d2(mcd_021_ev_marketcap_gap_189, 11)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189'] = {'inputs': ['mcd_021_ev_marketcap_gap_189'], 'func': mcd_base_universe_d2_011_mcd_021_ev_marketcap_gap_189}


def mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378(mcd_023_earnings_yield_spike_378):
    return _base_universe_d2(mcd_023_earnings_yield_spike_378, 12)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378'] = {'inputs': ['mcd_023_earnings_yield_spike_378'], 'func': mcd_base_universe_d2_012_mcd_023_earnings_yield_spike_378}


def mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504(mcd_024_valuation_history_depth_504):
    return _base_universe_d2(mcd_024_valuation_history_depth_504, 13)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504'] = {'inputs': ['mcd_024_valuation_history_depth_504'], 'func': mcd_base_universe_d2_013_mcd_024_valuation_history_depth_504}


def mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260(mcd_027_ps_compression_z_1260):
    return _base_universe_d2(mcd_027_ps_compression_z_1260, 14)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260'] = {'inputs': ['mcd_027_ps_compression_z_1260'], 'func': mcd_base_universe_d2_014_mcd_027_ps_compression_z_1260}


def mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63(mcd_029_ev_marketcap_gap_63):
    return _base_universe_d2(mcd_029_ev_marketcap_gap_63, 15)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63'] = {'inputs': ['mcd_029_ev_marketcap_gap_63'], 'func': mcd_base_universe_d2_015_mcd_029_ev_marketcap_gap_63}


def mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21(mcd_031_earnings_yield_spike_21):
    return _base_universe_d2(mcd_031_earnings_yield_spike_21, 16)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21'] = {'inputs': ['mcd_031_earnings_yield_spike_21'], 'func': mcd_base_universe_d2_016_mcd_031_earnings_yield_spike_21}


def mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42(mcd_032_valuation_history_depth_42):
    return _base_universe_d2(mcd_032_valuation_history_depth_42, 17)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42'] = {'inputs': ['mcd_032_valuation_history_depth_42'], 'func': mcd_base_universe_d2_017_mcd_032_valuation_history_depth_42}


def mcd_base_universe_d2_018_mcd_035_ps_compression_z_126(mcd_035_ps_compression_z_126):
    return _base_universe_d2(mcd_035_ps_compression_z_126, 18)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_018_mcd_035_ps_compression_z_126'] = {'inputs': ['mcd_035_ps_compression_z_126'], 'func': mcd_base_universe_d2_018_mcd_035_ps_compression_z_126}


def mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252(mcd_037_ev_marketcap_gap_252):
    return _base_universe_d2(mcd_037_ev_marketcap_gap_252, 19)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252'] = {'inputs': ['mcd_037_ev_marketcap_gap_252'], 'func': mcd_base_universe_d2_019_mcd_037_ev_marketcap_gap_252}


def mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504(mcd_039_earnings_yield_spike_504):
    return _base_universe_d2(mcd_039_earnings_yield_spike_504, 20)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504'] = {'inputs': ['mcd_039_earnings_yield_spike_504'], 'func': mcd_base_universe_d2_020_mcd_039_earnings_yield_spike_504}


def mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756(mcd_040_valuation_history_depth_756):
    return _base_universe_d2(mcd_040_valuation_history_depth_756, 21)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756'] = {'inputs': ['mcd_040_valuation_history_depth_756'], 'func': mcd_base_universe_d2_021_mcd_040_valuation_history_depth_756}


def mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512(mcd_043_ps_compression_z_1512):
    return _base_universe_d2(mcd_043_ps_compression_z_1512, 22)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512'] = {'inputs': ['mcd_043_ps_compression_z_1512'], 'func': mcd_base_universe_d2_022_mcd_043_ps_compression_z_1512}


def mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42(mcd_047_earnings_yield_spike_42):
    return _base_universe_d2(mcd_047_earnings_yield_spike_42, 23)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42'] = {'inputs': ['mcd_047_earnings_yield_spike_42'], 'func': mcd_base_universe_d2_023_mcd_047_earnings_yield_spike_42}


def mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63(mcd_048_valuation_history_depth_63):
    return _base_universe_d2(mcd_048_valuation_history_depth_63, 24)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63'] = {'inputs': ['mcd_048_valuation_history_depth_63'], 'func': mcd_base_universe_d2_024_mcd_048_valuation_history_depth_63}


def mcd_base_universe_d2_025_mcd_051_ps_compression_z_189(mcd_051_ps_compression_z_189):
    return _base_universe_d2(mcd_051_ps_compression_z_189, 25)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_025_mcd_051_ps_compression_z_189'] = {'inputs': ['mcd_051_ps_compression_z_189'], 'func': mcd_base_universe_d2_025_mcd_051_ps_compression_z_189}


def mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378(mcd_053_ev_marketcap_gap_378):
    return _base_universe_d2(mcd_053_ev_marketcap_gap_378, 26)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378'] = {'inputs': ['mcd_053_ev_marketcap_gap_378'], 'func': mcd_base_universe_d2_026_mcd_053_ev_marketcap_gap_378}


def mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756(mcd_055_earnings_yield_spike_756):
    return _base_universe_d2(mcd_055_earnings_yield_spike_756, 27)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756'] = {'inputs': ['mcd_055_earnings_yield_spike_756'], 'func': mcd_base_universe_d2_027_mcd_055_earnings_yield_spike_756}


def mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008(mcd_056_valuation_history_depth_1008):
    return _base_universe_d2(mcd_056_valuation_history_depth_1008, 28)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008'] = {'inputs': ['mcd_056_valuation_history_depth_1008'], 'func': mcd_base_universe_d2_028_mcd_056_valuation_history_depth_1008}


def mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21(mcd_061_ev_marketcap_gap_21):
    return _base_universe_d2(mcd_061_ev_marketcap_gap_21, 29)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21'] = {'inputs': ['mcd_061_ev_marketcap_gap_21'], 'func': mcd_base_universe_d2_029_mcd_061_ev_marketcap_gap_21}


def mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84(mcd_064_valuation_history_depth_84):
    return _base_universe_d2(mcd_064_valuation_history_depth_84, 30)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84'] = {'inputs': ['mcd_064_valuation_history_depth_84'], 'func': mcd_base_universe_d2_030_mcd_064_valuation_history_depth_84}


def mcd_base_universe_d2_031_mcd_067_ps_compression_z_252(mcd_067_ps_compression_z_252):
    return _base_universe_d2(mcd_067_ps_compression_z_252, 31)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_031_mcd_067_ps_compression_z_252'] = {'inputs': ['mcd_067_ps_compression_z_252'], 'func': mcd_base_universe_d2_031_mcd_067_ps_compression_z_252}


def mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504(mcd_069_ev_marketcap_gap_504):
    return _base_universe_d2(mcd_069_ev_marketcap_gap_504, 32)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504'] = {'inputs': ['mcd_069_ev_marketcap_gap_504'], 'func': mcd_base_universe_d2_032_mcd_069_ev_marketcap_gap_504}


def mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008(mcd_071_earnings_yield_spike_1008):
    return _base_universe_d2(mcd_071_earnings_yield_spike_1008, 33)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008'] = {'inputs': ['mcd_071_earnings_yield_spike_1008'], 'func': mcd_base_universe_d2_033_mcd_071_earnings_yield_spike_1008}


def mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260(mcd_072_valuation_history_depth_1260):
    return _base_universe_d2(mcd_072_valuation_history_depth_1260, 34)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260'] = {'inputs': ['mcd_072_valuation_history_depth_1260'], 'func': mcd_base_universe_d2_034_mcd_072_valuation_history_depth_1260}


def mcd_base_universe_d2_035_mcd_basefill_004(mcd_basefill_004):
    return _base_universe_d2(mcd_basefill_004, 35)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_035_mcd_basefill_004'] = {'inputs': ['mcd_basefill_004'], 'func': mcd_base_universe_d2_035_mcd_basefill_004}


def mcd_base_universe_d2_036_mcd_basefill_012(mcd_basefill_012):
    return _base_universe_d2(mcd_basefill_012, 36)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_036_mcd_basefill_012'] = {'inputs': ['mcd_basefill_012'], 'func': mcd_base_universe_d2_036_mcd_basefill_012}


def mcd_base_universe_d2_037_mcd_basefill_015(mcd_basefill_015):
    return _base_universe_d2(mcd_basefill_015, 37)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_037_mcd_basefill_015'] = {'inputs': ['mcd_basefill_015'], 'func': mcd_base_universe_d2_037_mcd_basefill_015}


def mcd_base_universe_d2_038_mcd_basefill_017(mcd_basefill_017):
    return _base_universe_d2(mcd_basefill_017, 38)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_038_mcd_basefill_017'] = {'inputs': ['mcd_basefill_017'], 'func': mcd_base_universe_d2_038_mcd_basefill_017}


def mcd_base_universe_d2_039_mcd_basefill_018(mcd_basefill_018):
    return _base_universe_d2(mcd_basefill_018, 39)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_039_mcd_basefill_018'] = {'inputs': ['mcd_basefill_018'], 'func': mcd_base_universe_d2_039_mcd_basefill_018}


def mcd_base_universe_d2_040_mcd_basefill_020(mcd_basefill_020):
    return _base_universe_d2(mcd_basefill_020, 40)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_040_mcd_basefill_020'] = {'inputs': ['mcd_basefill_020'], 'func': mcd_base_universe_d2_040_mcd_basefill_020}


def mcd_base_universe_d2_041_mcd_basefill_022(mcd_basefill_022):
    return _base_universe_d2(mcd_basefill_022, 41)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_041_mcd_basefill_022'] = {'inputs': ['mcd_basefill_022'], 'func': mcd_base_universe_d2_041_mcd_basefill_022}


def mcd_base_universe_d2_042_mcd_basefill_025(mcd_basefill_025):
    return _base_universe_d2(mcd_basefill_025, 42)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_042_mcd_basefill_025'] = {'inputs': ['mcd_basefill_025'], 'func': mcd_base_universe_d2_042_mcd_basefill_025}


def mcd_base_universe_d2_043_mcd_basefill_026(mcd_basefill_026):
    return _base_universe_d2(mcd_basefill_026, 43)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_043_mcd_basefill_026'] = {'inputs': ['mcd_basefill_026'], 'func': mcd_base_universe_d2_043_mcd_basefill_026}


def mcd_base_universe_d2_044_mcd_basefill_028(mcd_basefill_028):
    return _base_universe_d2(mcd_basefill_028, 44)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_044_mcd_basefill_028'] = {'inputs': ['mcd_basefill_028'], 'func': mcd_base_universe_d2_044_mcd_basefill_028}


def mcd_base_universe_d2_045_mcd_basefill_030(mcd_basefill_030):
    return _base_universe_d2(mcd_basefill_030, 45)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_045_mcd_basefill_030'] = {'inputs': ['mcd_basefill_030'], 'func': mcd_base_universe_d2_045_mcd_basefill_030}


def mcd_base_universe_d2_046_mcd_basefill_033(mcd_basefill_033):
    return _base_universe_d2(mcd_basefill_033, 46)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_046_mcd_basefill_033'] = {'inputs': ['mcd_basefill_033'], 'func': mcd_base_universe_d2_046_mcd_basefill_033}


def mcd_base_universe_d2_047_mcd_basefill_034(mcd_basefill_034):
    return _base_universe_d2(mcd_basefill_034, 47)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_047_mcd_basefill_034'] = {'inputs': ['mcd_basefill_034'], 'func': mcd_base_universe_d2_047_mcd_basefill_034}


def mcd_base_universe_d2_048_mcd_basefill_036(mcd_basefill_036):
    return _base_universe_d2(mcd_basefill_036, 48)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_048_mcd_basefill_036'] = {'inputs': ['mcd_basefill_036'], 'func': mcd_base_universe_d2_048_mcd_basefill_036}


def mcd_base_universe_d2_049_mcd_basefill_038(mcd_basefill_038):
    return _base_universe_d2(mcd_basefill_038, 49)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_049_mcd_basefill_038'] = {'inputs': ['mcd_basefill_038'], 'func': mcd_base_universe_d2_049_mcd_basefill_038}


def mcd_base_universe_d2_050_mcd_basefill_041(mcd_basefill_041):
    return _base_universe_d2(mcd_basefill_041, 50)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_050_mcd_basefill_041'] = {'inputs': ['mcd_basefill_041'], 'func': mcd_base_universe_d2_050_mcd_basefill_041}


def mcd_base_universe_d2_051_mcd_basefill_042(mcd_basefill_042):
    return _base_universe_d2(mcd_basefill_042, 51)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_051_mcd_basefill_042'] = {'inputs': ['mcd_basefill_042'], 'func': mcd_base_universe_d2_051_mcd_basefill_042}


def mcd_base_universe_d2_052_mcd_basefill_044(mcd_basefill_044):
    return _base_universe_d2(mcd_basefill_044, 52)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_052_mcd_basefill_044'] = {'inputs': ['mcd_basefill_044'], 'func': mcd_base_universe_d2_052_mcd_basefill_044}


def mcd_base_universe_d2_053_mcd_basefill_045(mcd_basefill_045):
    return _base_universe_d2(mcd_basefill_045, 53)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_053_mcd_basefill_045'] = {'inputs': ['mcd_basefill_045'], 'func': mcd_base_universe_d2_053_mcd_basefill_045}


def mcd_base_universe_d2_054_mcd_basefill_046(mcd_basefill_046):
    return _base_universe_d2(mcd_basefill_046, 54)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_054_mcd_basefill_046'] = {'inputs': ['mcd_basefill_046'], 'func': mcd_base_universe_d2_054_mcd_basefill_046}


def mcd_base_universe_d2_055_mcd_basefill_049(mcd_basefill_049):
    return _base_universe_d2(mcd_basefill_049, 55)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_055_mcd_basefill_049'] = {'inputs': ['mcd_basefill_049'], 'func': mcd_base_universe_d2_055_mcd_basefill_049}


def mcd_base_universe_d2_056_mcd_basefill_050(mcd_basefill_050):
    return _base_universe_d2(mcd_basefill_050, 56)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_056_mcd_basefill_050'] = {'inputs': ['mcd_basefill_050'], 'func': mcd_base_universe_d2_056_mcd_basefill_050}


def mcd_base_universe_d2_057_mcd_basefill_052(mcd_basefill_052):
    return _base_universe_d2(mcd_basefill_052, 57)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_057_mcd_basefill_052'] = {'inputs': ['mcd_basefill_052'], 'func': mcd_base_universe_d2_057_mcd_basefill_052}


def mcd_base_universe_d2_058_mcd_basefill_054(mcd_basefill_054):
    return _base_universe_d2(mcd_basefill_054, 58)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_058_mcd_basefill_054'] = {'inputs': ['mcd_basefill_054'], 'func': mcd_base_universe_d2_058_mcd_basefill_054}


def mcd_base_universe_d2_059_mcd_basefill_057(mcd_basefill_057):
    return _base_universe_d2(mcd_basefill_057, 59)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_059_mcd_basefill_057'] = {'inputs': ['mcd_basefill_057'], 'func': mcd_base_universe_d2_059_mcd_basefill_057}


def mcd_base_universe_d2_060_mcd_basefill_058(mcd_basefill_058):
    return _base_universe_d2(mcd_basefill_058, 60)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_060_mcd_basefill_058'] = {'inputs': ['mcd_basefill_058'], 'func': mcd_base_universe_d2_060_mcd_basefill_058}


def mcd_base_universe_d2_061_mcd_basefill_059(mcd_basefill_059):
    return _base_universe_d2(mcd_basefill_059, 61)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_061_mcd_basefill_059'] = {'inputs': ['mcd_basefill_059'], 'func': mcd_base_universe_d2_061_mcd_basefill_059}


def mcd_base_universe_d2_062_mcd_basefill_060(mcd_basefill_060):
    return _base_universe_d2(mcd_basefill_060, 62)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_062_mcd_basefill_060'] = {'inputs': ['mcd_basefill_060'], 'func': mcd_base_universe_d2_062_mcd_basefill_060}


def mcd_base_universe_d2_063_mcd_basefill_062(mcd_basefill_062):
    return _base_universe_d2(mcd_basefill_062, 63)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_063_mcd_basefill_062'] = {'inputs': ['mcd_basefill_062'], 'func': mcd_base_universe_d2_063_mcd_basefill_062}


def mcd_base_universe_d2_064_mcd_basefill_063(mcd_basefill_063):
    return _base_universe_d2(mcd_basefill_063, 64)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_064_mcd_basefill_063'] = {'inputs': ['mcd_basefill_063'], 'func': mcd_base_universe_d2_064_mcd_basefill_063}


def mcd_base_universe_d2_065_mcd_basefill_065(mcd_basefill_065):
    return _base_universe_d2(mcd_basefill_065, 65)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_065_mcd_basefill_065'] = {'inputs': ['mcd_basefill_065'], 'func': mcd_base_universe_d2_065_mcd_basefill_065}


def mcd_base_universe_d2_066_mcd_basefill_066(mcd_basefill_066):
    return _base_universe_d2(mcd_basefill_066, 66)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_066_mcd_basefill_066'] = {'inputs': ['mcd_basefill_066'], 'func': mcd_base_universe_d2_066_mcd_basefill_066}


def mcd_base_universe_d2_067_mcd_basefill_068(mcd_basefill_068):
    return _base_universe_d2(mcd_basefill_068, 67)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_067_mcd_basefill_068'] = {'inputs': ['mcd_basefill_068'], 'func': mcd_base_universe_d2_067_mcd_basefill_068}


def mcd_base_universe_d2_068_mcd_basefill_070(mcd_basefill_070):
    return _base_universe_d2(mcd_basefill_070, 68)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_068_mcd_basefill_070'] = {'inputs': ['mcd_basefill_070'], 'func': mcd_base_universe_d2_068_mcd_basefill_070}


def mcd_base_universe_d2_069_mcd_basefill_073(mcd_basefill_073):
    return _base_universe_d2(mcd_basefill_073, 69)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_069_mcd_basefill_073'] = {'inputs': ['mcd_basefill_073'], 'func': mcd_base_universe_d2_069_mcd_basefill_073}


def mcd_base_universe_d2_070_mcd_basefill_074(mcd_basefill_074):
    return _base_universe_d2(mcd_basefill_074, 70)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_070_mcd_basefill_074'] = {'inputs': ['mcd_basefill_074'], 'func': mcd_base_universe_d2_070_mcd_basefill_074}


def mcd_base_universe_d2_071_mcd_basefill_075(mcd_basefill_075):
    return _base_universe_d2(mcd_basefill_075, 71)
MCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mcd_base_universe_d2_071_mcd_basefill_075'] = {'inputs': ['mcd_basefill_075'], 'func': mcd_base_universe_d2_071_mcd_basefill_075}
