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



def ibf_151_ibf_001_holder_exit_1_roc_1(ibf_001_holder_exit_1):
    feature = _s(ibf_001_holder_exit_1)
    return (_roc(feature, 1)).reindex(feature.index)

def ibf_152_ibf_007_holder_exit_1_roc_42(ibf_007_holder_exit_1):
    feature = _s(ibf_007_holder_exit_1)
    return (_roc(feature, 42)).reindex(feature.index)

def ibf_153_ibf_013_holder_exit_1_roc_126(ibf_013_holder_exit_1):
    feature = _s(ibf_013_holder_exit_1)
    return (_roc(feature, 126)).reindex(feature.index)

def ibf_154_ibf_019_holder_exit_1_roc_378(ibf_019_holder_exit_1):
    feature = _s(ibf_019_holder_exit_1)
    return (_roc(feature, 378)).reindex(feature.index)

def ibf_155_ibf_025_holder_exit_1_roc_4(ibf_025_holder_exit_1):
    feature = _s(ibf_025_holder_exit_1)
    return (_roc(feature, 4)).reindex(feature.index)






















INSTITUTIONAL_BOTTOM_FISH_REGISTRY_2ND_DERIVATIVES = {
    'ibf_151_ibf_001_holder_exit_1_roc_1': {'inputs': ['ibf_001_holder_exit_1'], 'func': ibf_151_ibf_001_holder_exit_1_roc_1},
    'ibf_152_ibf_007_holder_exit_1_roc_42': {'inputs': ['ibf_007_holder_exit_1'], 'func': ibf_152_ibf_007_holder_exit_1_roc_42},
    'ibf_153_ibf_013_holder_exit_1_roc_126': {'inputs': ['ibf_013_holder_exit_1'], 'func': ibf_153_ibf_013_holder_exit_1_roc_126},
    'ibf_154_ibf_019_holder_exit_1_roc_378': {'inputs': ['ibf_019_holder_exit_1'], 'func': ibf_154_ibf_019_holder_exit_1_roc_378},
    'ibf_155_ibf_025_holder_exit_1_roc_4': {'inputs': ['ibf_025_holder_exit_1'], 'func': ibf_155_ibf_025_holder_exit_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ibf_replacement_d2_001(ibf_001_holder_exit_1):
    feature = _clean(ibf_001_holder_exit_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_001'] = {'inputs': ['ibf_001_holder_exit_1'], 'func': ibf_replacement_d2_001}


def ibf_replacement_d2_002(ibf_007_holder_exit_1):
    feature = _clean(ibf_007_holder_exit_1)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_002'] = {'inputs': ['ibf_007_holder_exit_1'], 'func': ibf_replacement_d2_002}


def ibf_replacement_d2_003(ibf_013_holder_exit_1):
    feature = _clean(ibf_013_holder_exit_1)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_003'] = {'inputs': ['ibf_013_holder_exit_1'], 'func': ibf_replacement_d2_003}


def ibf_replacement_d2_004(ibf_019_holder_exit_1):
    feature = _clean(ibf_019_holder_exit_1)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_004'] = {'inputs': ['ibf_019_holder_exit_1'], 'func': ibf_replacement_d2_004}


def ibf_replacement_d2_005(ibf_025_holder_exit_1):
    feature = _clean(ibf_025_holder_exit_1)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_005'] = {'inputs': ['ibf_025_holder_exit_1'], 'func': ibf_replacement_d2_005}


def ibf_replacement_d2_006(ibf_replacement_001):
    feature = _clean(ibf_replacement_001)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_006'] = {'inputs': ['ibf_replacement_001'], 'func': ibf_replacement_d2_006}


def ibf_replacement_d2_007(ibf_replacement_002):
    feature = _clean(ibf_replacement_002)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_007'] = {'inputs': ['ibf_replacement_002'], 'func': ibf_replacement_d2_007}


def ibf_replacement_d2_008(ibf_replacement_003):
    feature = _clean(ibf_replacement_003)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_008'] = {'inputs': ['ibf_replacement_003'], 'func': ibf_replacement_d2_008}


def ibf_replacement_d2_009(ibf_replacement_004):
    feature = _clean(ibf_replacement_004)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_009'] = {'inputs': ['ibf_replacement_004'], 'func': ibf_replacement_d2_009}


def ibf_replacement_d2_010(ibf_replacement_005):
    feature = _clean(ibf_replacement_005)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_010'] = {'inputs': ['ibf_replacement_005'], 'func': ibf_replacement_d2_010}


def ibf_replacement_d2_011(ibf_replacement_006):
    feature = _clean(ibf_replacement_006)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_011'] = {'inputs': ['ibf_replacement_006'], 'func': ibf_replacement_d2_011}


def ibf_replacement_d2_012(ibf_replacement_007):
    feature = _clean(ibf_replacement_007)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_012'] = {'inputs': ['ibf_replacement_007'], 'func': ibf_replacement_d2_012}


def ibf_replacement_d2_013(ibf_replacement_008):
    feature = _clean(ibf_replacement_008)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_013'] = {'inputs': ['ibf_replacement_008'], 'func': ibf_replacement_d2_013}


def ibf_replacement_d2_014(ibf_replacement_009):
    feature = _clean(ibf_replacement_009)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_014'] = {'inputs': ['ibf_replacement_009'], 'func': ibf_replacement_d2_014}


def ibf_replacement_d2_015(ibf_replacement_010):
    feature = _clean(ibf_replacement_010)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_015'] = {'inputs': ['ibf_replacement_010'], 'func': ibf_replacement_d2_015}


def ibf_replacement_d2_016(ibf_replacement_011):
    feature = _clean(ibf_replacement_011)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_016'] = {'inputs': ['ibf_replacement_011'], 'func': ibf_replacement_d2_016}


def ibf_replacement_d2_017(ibf_replacement_012):
    feature = _clean(ibf_replacement_012)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_017'] = {'inputs': ['ibf_replacement_012'], 'func': ibf_replacement_d2_017}


def ibf_replacement_d2_018(ibf_replacement_013):
    feature = _clean(ibf_replacement_013)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_018'] = {'inputs': ['ibf_replacement_013'], 'func': ibf_replacement_d2_018}


def ibf_replacement_d2_019(ibf_replacement_014):
    feature = _clean(ibf_replacement_014)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_019'] = {'inputs': ['ibf_replacement_014'], 'func': ibf_replacement_d2_019}


def ibf_replacement_d2_020(ibf_replacement_015):
    feature = _clean(ibf_replacement_015)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_020'] = {'inputs': ['ibf_replacement_015'], 'func': ibf_replacement_d2_020}


def ibf_replacement_d2_021(ibf_replacement_016):
    feature = _clean(ibf_replacement_016)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_021'] = {'inputs': ['ibf_replacement_016'], 'func': ibf_replacement_d2_021}


def ibf_replacement_d2_022(ibf_replacement_017):
    feature = _clean(ibf_replacement_017)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_022'] = {'inputs': ['ibf_replacement_017'], 'func': ibf_replacement_d2_022}


def ibf_replacement_d2_023(ibf_replacement_018):
    feature = _clean(ibf_replacement_018)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_023'] = {'inputs': ['ibf_replacement_018'], 'func': ibf_replacement_d2_023}


def ibf_replacement_d2_024(ibf_replacement_019):
    feature = _clean(ibf_replacement_019)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_024'] = {'inputs': ['ibf_replacement_019'], 'func': ibf_replacement_d2_024}


def ibf_replacement_d2_025(ibf_replacement_020):
    feature = _clean(ibf_replacement_020)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_025'] = {'inputs': ['ibf_replacement_020'], 'func': ibf_replacement_d2_025}


def ibf_replacement_d2_026(ibf_replacement_021):
    feature = _clean(ibf_replacement_021)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_026'] = {'inputs': ['ibf_replacement_021'], 'func': ibf_replacement_d2_026}


def ibf_replacement_d2_027(ibf_replacement_022):
    feature = _clean(ibf_replacement_022)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_027'] = {'inputs': ['ibf_replacement_022'], 'func': ibf_replacement_d2_027}


def ibf_replacement_d2_028(ibf_replacement_023):
    feature = _clean(ibf_replacement_023)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_028'] = {'inputs': ['ibf_replacement_023'], 'func': ibf_replacement_d2_028}


def ibf_replacement_d2_029(ibf_replacement_024):
    feature = _clean(ibf_replacement_024)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_029'] = {'inputs': ['ibf_replacement_024'], 'func': ibf_replacement_d2_029}


def ibf_replacement_d2_030(ibf_replacement_025):
    feature = _clean(ibf_replacement_025)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_030'] = {'inputs': ['ibf_replacement_025'], 'func': ibf_replacement_d2_030}


def ibf_replacement_d2_031(ibf_replacement_026):
    feature = _clean(ibf_replacement_026)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_031'] = {'inputs': ['ibf_replacement_026'], 'func': ibf_replacement_d2_031}


def ibf_replacement_d2_032(ibf_replacement_027):
    feature = _clean(ibf_replacement_027)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_032'] = {'inputs': ['ibf_replacement_027'], 'func': ibf_replacement_d2_032}


def ibf_replacement_d2_033(ibf_replacement_028):
    feature = _clean(ibf_replacement_028)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_033'] = {'inputs': ['ibf_replacement_028'], 'func': ibf_replacement_d2_033}


def ibf_replacement_d2_034(ibf_replacement_029):
    feature = _clean(ibf_replacement_029)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_034'] = {'inputs': ['ibf_replacement_029'], 'func': ibf_replacement_d2_034}


def ibf_replacement_d2_035(ibf_replacement_030):
    feature = _clean(ibf_replacement_030)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_035'] = {'inputs': ['ibf_replacement_030'], 'func': ibf_replacement_d2_035}


def ibf_replacement_d2_036(ibf_replacement_031):
    feature = _clean(ibf_replacement_031)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_036'] = {'inputs': ['ibf_replacement_031'], 'func': ibf_replacement_d2_036}


def ibf_replacement_d2_037(ibf_replacement_032):
    feature = _clean(ibf_replacement_032)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_037'] = {'inputs': ['ibf_replacement_032'], 'func': ibf_replacement_d2_037}


def ibf_replacement_d2_038(ibf_replacement_033):
    feature = _clean(ibf_replacement_033)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_038'] = {'inputs': ['ibf_replacement_033'], 'func': ibf_replacement_d2_038}


def ibf_replacement_d2_039(ibf_replacement_034):
    feature = _clean(ibf_replacement_034)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_039'] = {'inputs': ['ibf_replacement_034'], 'func': ibf_replacement_d2_039}


def ibf_replacement_d2_040(ibf_replacement_035):
    feature = _clean(ibf_replacement_035)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_040'] = {'inputs': ['ibf_replacement_035'], 'func': ibf_replacement_d2_040}


def ibf_replacement_d2_041(ibf_replacement_036):
    feature = _clean(ibf_replacement_036)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_041'] = {'inputs': ['ibf_replacement_036'], 'func': ibf_replacement_d2_041}


def ibf_replacement_d2_042(ibf_replacement_037):
    feature = _clean(ibf_replacement_037)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_042'] = {'inputs': ['ibf_replacement_037'], 'func': ibf_replacement_d2_042}


def ibf_replacement_d2_043(ibf_replacement_038):
    feature = _clean(ibf_replacement_038)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_043'] = {'inputs': ['ibf_replacement_038'], 'func': ibf_replacement_d2_043}


def ibf_replacement_d2_044(ibf_replacement_039):
    feature = _clean(ibf_replacement_039)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_044'] = {'inputs': ['ibf_replacement_039'], 'func': ibf_replacement_d2_044}


def ibf_replacement_d2_045(ibf_replacement_040):
    feature = _clean(ibf_replacement_040)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_045'] = {'inputs': ['ibf_replacement_040'], 'func': ibf_replacement_d2_045}


def ibf_replacement_d2_046(ibf_replacement_041):
    feature = _clean(ibf_replacement_041)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_046'] = {'inputs': ['ibf_replacement_041'], 'func': ibf_replacement_d2_046}


def ibf_replacement_d2_047(ibf_replacement_042):
    feature = _clean(ibf_replacement_042)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_047'] = {'inputs': ['ibf_replacement_042'], 'func': ibf_replacement_d2_047}


def ibf_replacement_d2_048(ibf_replacement_043):
    feature = _clean(ibf_replacement_043)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_048'] = {'inputs': ['ibf_replacement_043'], 'func': ibf_replacement_d2_048}


def ibf_replacement_d2_049(ibf_replacement_044):
    feature = _clean(ibf_replacement_044)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_049'] = {'inputs': ['ibf_replacement_044'], 'func': ibf_replacement_d2_049}


def ibf_replacement_d2_050(ibf_replacement_045):
    feature = _clean(ibf_replacement_045)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_050'] = {'inputs': ['ibf_replacement_045'], 'func': ibf_replacement_d2_050}


def ibf_replacement_d2_051(ibf_replacement_046):
    feature = _clean(ibf_replacement_046)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_051'] = {'inputs': ['ibf_replacement_046'], 'func': ibf_replacement_d2_051}


def ibf_replacement_d2_052(ibf_replacement_047):
    feature = _clean(ibf_replacement_047)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_052'] = {'inputs': ['ibf_replacement_047'], 'func': ibf_replacement_d2_052}


def ibf_replacement_d2_053(ibf_replacement_048):
    feature = _clean(ibf_replacement_048)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_053'] = {'inputs': ['ibf_replacement_048'], 'func': ibf_replacement_d2_053}


def ibf_replacement_d2_054(ibf_replacement_049):
    feature = _clean(ibf_replacement_049)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_054'] = {'inputs': ['ibf_replacement_049'], 'func': ibf_replacement_d2_054}


def ibf_replacement_d2_055(ibf_replacement_050):
    feature = _clean(ibf_replacement_050)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_055'] = {'inputs': ['ibf_replacement_050'], 'func': ibf_replacement_d2_055}


def ibf_replacement_d2_056(ibf_replacement_051):
    feature = _clean(ibf_replacement_051)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_056'] = {'inputs': ['ibf_replacement_051'], 'func': ibf_replacement_d2_056}


def ibf_replacement_d2_057(ibf_replacement_052):
    feature = _clean(ibf_replacement_052)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_057'] = {'inputs': ['ibf_replacement_052'], 'func': ibf_replacement_d2_057}


def ibf_replacement_d2_058(ibf_replacement_053):
    feature = _clean(ibf_replacement_053)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_058'] = {'inputs': ['ibf_replacement_053'], 'func': ibf_replacement_d2_058}


def ibf_replacement_d2_059(ibf_replacement_054):
    feature = _clean(ibf_replacement_054)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_059'] = {'inputs': ['ibf_replacement_054'], 'func': ibf_replacement_d2_059}


def ibf_replacement_d2_060(ibf_replacement_055):
    feature = _clean(ibf_replacement_055)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_060'] = {'inputs': ['ibf_replacement_055'], 'func': ibf_replacement_d2_060}


def ibf_replacement_d2_061(ibf_replacement_056):
    feature = _clean(ibf_replacement_056)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_061'] = {'inputs': ['ibf_replacement_056'], 'func': ibf_replacement_d2_061}


def ibf_replacement_d2_062(ibf_replacement_057):
    feature = _clean(ibf_replacement_057)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_062'] = {'inputs': ['ibf_replacement_057'], 'func': ibf_replacement_d2_062}


def ibf_replacement_d2_063(ibf_replacement_058):
    feature = _clean(ibf_replacement_058)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_063'] = {'inputs': ['ibf_replacement_058'], 'func': ibf_replacement_d2_063}


def ibf_replacement_d2_064(ibf_replacement_059):
    feature = _clean(ibf_replacement_059)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_064'] = {'inputs': ['ibf_replacement_059'], 'func': ibf_replacement_d2_064}


def ibf_replacement_d2_065(ibf_replacement_060):
    feature = _clean(ibf_replacement_060)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_065'] = {'inputs': ['ibf_replacement_060'], 'func': ibf_replacement_d2_065}


def ibf_replacement_d2_066(ibf_replacement_061):
    feature = _clean(ibf_replacement_061)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_066'] = {'inputs': ['ibf_replacement_061'], 'func': ibf_replacement_d2_066}


def ibf_replacement_d2_067(ibf_replacement_062):
    feature = _clean(ibf_replacement_062)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_067'] = {'inputs': ['ibf_replacement_062'], 'func': ibf_replacement_d2_067}


def ibf_replacement_d2_068(ibf_replacement_063):
    feature = _clean(ibf_replacement_063)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_068'] = {'inputs': ['ibf_replacement_063'], 'func': ibf_replacement_d2_068}


def ibf_replacement_d2_069(ibf_replacement_064):
    feature = _clean(ibf_replacement_064)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_069'] = {'inputs': ['ibf_replacement_064'], 'func': ibf_replacement_d2_069}


def ibf_replacement_d2_070(ibf_replacement_065):
    feature = _clean(ibf_replacement_065)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_070'] = {'inputs': ['ibf_replacement_065'], 'func': ibf_replacement_d2_070}


def ibf_replacement_d2_071(ibf_replacement_066):
    feature = _clean(ibf_replacement_066)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_071'] = {'inputs': ['ibf_replacement_066'], 'func': ibf_replacement_d2_071}


def ibf_replacement_d2_072(ibf_replacement_067):
    feature = _clean(ibf_replacement_067)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_072'] = {'inputs': ['ibf_replacement_067'], 'func': ibf_replacement_d2_072}


def ibf_replacement_d2_073(ibf_replacement_068):
    feature = _clean(ibf_replacement_068)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_073'] = {'inputs': ['ibf_replacement_068'], 'func': ibf_replacement_d2_073}


def ibf_replacement_d2_074(ibf_replacement_069):
    feature = _clean(ibf_replacement_069)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_074'] = {'inputs': ['ibf_replacement_069'], 'func': ibf_replacement_d2_074}


def ibf_replacement_d2_075(ibf_replacement_070):
    feature = _clean(ibf_replacement_070)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_075'] = {'inputs': ['ibf_replacement_070'], 'func': ibf_replacement_d2_075}


def ibf_replacement_d2_076(ibf_replacement_071):
    feature = _clean(ibf_replacement_071)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_076'] = {'inputs': ['ibf_replacement_071'], 'func': ibf_replacement_d2_076}


def ibf_replacement_d2_077(ibf_replacement_072):
    feature = _clean(ibf_replacement_072)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_077'] = {'inputs': ['ibf_replacement_072'], 'func': ibf_replacement_d2_077}


def ibf_replacement_d2_078(ibf_replacement_073):
    feature = _clean(ibf_replacement_073)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_078'] = {'inputs': ['ibf_replacement_073'], 'func': ibf_replacement_d2_078}


def ibf_replacement_d2_079(ibf_replacement_074):
    feature = _clean(ibf_replacement_074)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_079'] = {'inputs': ['ibf_replacement_074'], 'func': ibf_replacement_d2_079}


def ibf_replacement_d2_080(ibf_replacement_075):
    feature = _clean(ibf_replacement_075)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_080'] = {'inputs': ['ibf_replacement_075'], 'func': ibf_replacement_d2_080}


def ibf_replacement_d2_081(ibf_replacement_076):
    feature = _clean(ibf_replacement_076)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_081'] = {'inputs': ['ibf_replacement_076'], 'func': ibf_replacement_d2_081}


def ibf_replacement_d2_082(ibf_replacement_077):
    feature = _clean(ibf_replacement_077)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_082'] = {'inputs': ['ibf_replacement_077'], 'func': ibf_replacement_d2_082}


def ibf_replacement_d2_083(ibf_replacement_078):
    feature = _clean(ibf_replacement_078)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_083'] = {'inputs': ['ibf_replacement_078'], 'func': ibf_replacement_d2_083}


def ibf_replacement_d2_084(ibf_replacement_079):
    feature = _clean(ibf_replacement_079)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_084'] = {'inputs': ['ibf_replacement_079'], 'func': ibf_replacement_d2_084}


def ibf_replacement_d2_085(ibf_replacement_080):
    feature = _clean(ibf_replacement_080)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_085'] = {'inputs': ['ibf_replacement_080'], 'func': ibf_replacement_d2_085}


def ibf_replacement_d2_086(ibf_replacement_081):
    feature = _clean(ibf_replacement_081)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_086'] = {'inputs': ['ibf_replacement_081'], 'func': ibf_replacement_d2_086}


def ibf_replacement_d2_087(ibf_replacement_082):
    feature = _clean(ibf_replacement_082)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_087'] = {'inputs': ['ibf_replacement_082'], 'func': ibf_replacement_d2_087}


def ibf_replacement_d2_088(ibf_replacement_083):
    feature = _clean(ibf_replacement_083)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_088'] = {'inputs': ['ibf_replacement_083'], 'func': ibf_replacement_d2_088}


def ibf_replacement_d2_089(ibf_replacement_084):
    feature = _clean(ibf_replacement_084)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_089'] = {'inputs': ['ibf_replacement_084'], 'func': ibf_replacement_d2_089}


def ibf_replacement_d2_090(ibf_replacement_085):
    feature = _clean(ibf_replacement_085)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_090'] = {'inputs': ['ibf_replacement_085'], 'func': ibf_replacement_d2_090}


def ibf_replacement_d2_091(ibf_replacement_086):
    feature = _clean(ibf_replacement_086)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_091'] = {'inputs': ['ibf_replacement_086'], 'func': ibf_replacement_d2_091}


def ibf_replacement_d2_092(ibf_replacement_087):
    feature = _clean(ibf_replacement_087)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_092'] = {'inputs': ['ibf_replacement_087'], 'func': ibf_replacement_d2_092}


def ibf_replacement_d2_093(ibf_replacement_088):
    feature = _clean(ibf_replacement_088)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_093'] = {'inputs': ['ibf_replacement_088'], 'func': ibf_replacement_d2_093}


def ibf_replacement_d2_094(ibf_replacement_089):
    feature = _clean(ibf_replacement_089)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_094'] = {'inputs': ['ibf_replacement_089'], 'func': ibf_replacement_d2_094}


def ibf_replacement_d2_095(ibf_replacement_090):
    feature = _clean(ibf_replacement_090)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_095'] = {'inputs': ['ibf_replacement_090'], 'func': ibf_replacement_d2_095}


def ibf_replacement_d2_096(ibf_replacement_091):
    feature = _clean(ibf_replacement_091)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_096'] = {'inputs': ['ibf_replacement_091'], 'func': ibf_replacement_d2_096}


def ibf_replacement_d2_097(ibf_replacement_092):
    feature = _clean(ibf_replacement_092)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_097'] = {'inputs': ['ibf_replacement_092'], 'func': ibf_replacement_d2_097}


def ibf_replacement_d2_098(ibf_replacement_093):
    feature = _clean(ibf_replacement_093)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_098'] = {'inputs': ['ibf_replacement_093'], 'func': ibf_replacement_d2_098}


def ibf_replacement_d2_099(ibf_replacement_094):
    feature = _clean(ibf_replacement_094)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_099'] = {'inputs': ['ibf_replacement_094'], 'func': ibf_replacement_d2_099}


def ibf_replacement_d2_100(ibf_replacement_095):
    feature = _clean(ibf_replacement_095)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_100'] = {'inputs': ['ibf_replacement_095'], 'func': ibf_replacement_d2_100}


def ibf_replacement_d2_101(ibf_replacement_096):
    feature = _clean(ibf_replacement_096)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_101'] = {'inputs': ['ibf_replacement_096'], 'func': ibf_replacement_d2_101}


def ibf_replacement_d2_102(ibf_replacement_097):
    feature = _clean(ibf_replacement_097)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_102'] = {'inputs': ['ibf_replacement_097'], 'func': ibf_replacement_d2_102}


def ibf_replacement_d2_103(ibf_replacement_098):
    feature = _clean(ibf_replacement_098)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_103'] = {'inputs': ['ibf_replacement_098'], 'func': ibf_replacement_d2_103}


def ibf_replacement_d2_104(ibf_replacement_099):
    feature = _clean(ibf_replacement_099)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_104'] = {'inputs': ['ibf_replacement_099'], 'func': ibf_replacement_d2_104}


def ibf_replacement_d2_105(ibf_replacement_100):
    feature = _clean(ibf_replacement_100)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_105'] = {'inputs': ['ibf_replacement_100'], 'func': ibf_replacement_d2_105}


def ibf_replacement_d2_106(ibf_replacement_101):
    feature = _clean(ibf_replacement_101)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_106'] = {'inputs': ['ibf_replacement_101'], 'func': ibf_replacement_d2_106}


def ibf_replacement_d2_107(ibf_replacement_102):
    feature = _clean(ibf_replacement_102)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_107'] = {'inputs': ['ibf_replacement_102'], 'func': ibf_replacement_d2_107}


def ibf_replacement_d2_108(ibf_replacement_103):
    feature = _clean(ibf_replacement_103)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_108'] = {'inputs': ['ibf_replacement_103'], 'func': ibf_replacement_d2_108}


def ibf_replacement_d2_109(ibf_replacement_104):
    feature = _clean(ibf_replacement_104)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_109'] = {'inputs': ['ibf_replacement_104'], 'func': ibf_replacement_d2_109}


def ibf_replacement_d2_110(ibf_replacement_105):
    feature = _clean(ibf_replacement_105)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_110'] = {'inputs': ['ibf_replacement_105'], 'func': ibf_replacement_d2_110}


def ibf_replacement_d2_111(ibf_replacement_106):
    feature = _clean(ibf_replacement_106)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_111'] = {'inputs': ['ibf_replacement_106'], 'func': ibf_replacement_d2_111}


def ibf_replacement_d2_112(ibf_replacement_107):
    feature = _clean(ibf_replacement_107)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_112'] = {'inputs': ['ibf_replacement_107'], 'func': ibf_replacement_d2_112}


def ibf_replacement_d2_113(ibf_replacement_108):
    feature = _clean(ibf_replacement_108)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_113'] = {'inputs': ['ibf_replacement_108'], 'func': ibf_replacement_d2_113}


def ibf_replacement_d2_114(ibf_replacement_109):
    feature = _clean(ibf_replacement_109)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_114'] = {'inputs': ['ibf_replacement_109'], 'func': ibf_replacement_d2_114}


def ibf_replacement_d2_115(ibf_replacement_110):
    feature = _clean(ibf_replacement_110)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_115'] = {'inputs': ['ibf_replacement_110'], 'func': ibf_replacement_d2_115}


def ibf_replacement_d2_116(ibf_replacement_111):
    feature = _clean(ibf_replacement_111)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_116'] = {'inputs': ['ibf_replacement_111'], 'func': ibf_replacement_d2_116}


def ibf_replacement_d2_117(ibf_replacement_112):
    feature = _clean(ibf_replacement_112)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_117'] = {'inputs': ['ibf_replacement_112'], 'func': ibf_replacement_d2_117}


def ibf_replacement_d2_118(ibf_replacement_113):
    feature = _clean(ibf_replacement_113)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_118'] = {'inputs': ['ibf_replacement_113'], 'func': ibf_replacement_d2_118}


def ibf_replacement_d2_119(ibf_replacement_114):
    feature = _clean(ibf_replacement_114)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_119'] = {'inputs': ['ibf_replacement_114'], 'func': ibf_replacement_d2_119}


def ibf_replacement_d2_120(ibf_replacement_115):
    feature = _clean(ibf_replacement_115)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_120'] = {'inputs': ['ibf_replacement_115'], 'func': ibf_replacement_d2_120}


def ibf_replacement_d2_121(ibf_replacement_116):
    feature = _clean(ibf_replacement_116)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_121'] = {'inputs': ['ibf_replacement_116'], 'func': ibf_replacement_d2_121}


def ibf_replacement_d2_122(ibf_replacement_117):
    feature = _clean(ibf_replacement_117)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_122'] = {'inputs': ['ibf_replacement_117'], 'func': ibf_replacement_d2_122}


def ibf_replacement_d2_123(ibf_replacement_118):
    feature = _clean(ibf_replacement_118)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_123'] = {'inputs': ['ibf_replacement_118'], 'func': ibf_replacement_d2_123}


def ibf_replacement_d2_124(ibf_replacement_119):
    feature = _clean(ibf_replacement_119)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_124'] = {'inputs': ['ibf_replacement_119'], 'func': ibf_replacement_d2_124}


def ibf_replacement_d2_125(ibf_replacement_120):
    feature = _clean(ibf_replacement_120)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_125'] = {'inputs': ['ibf_replacement_120'], 'func': ibf_replacement_d2_125}


def ibf_replacement_d2_126(ibf_replacement_121):
    feature = _clean(ibf_replacement_121)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_126'] = {'inputs': ['ibf_replacement_121'], 'func': ibf_replacement_d2_126}


def ibf_replacement_d2_127(ibf_replacement_122):
    feature = _clean(ibf_replacement_122)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_127'] = {'inputs': ['ibf_replacement_122'], 'func': ibf_replacement_d2_127}


def ibf_replacement_d2_128(ibf_replacement_123):
    feature = _clean(ibf_replacement_123)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_128'] = {'inputs': ['ibf_replacement_123'], 'func': ibf_replacement_d2_128}


def ibf_replacement_d2_129(ibf_replacement_124):
    feature = _clean(ibf_replacement_124)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_129'] = {'inputs': ['ibf_replacement_124'], 'func': ibf_replacement_d2_129}


def ibf_replacement_d2_130(ibf_replacement_125):
    feature = _clean(ibf_replacement_125)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_130'] = {'inputs': ['ibf_replacement_125'], 'func': ibf_replacement_d2_130}


def ibf_replacement_d2_131(ibf_replacement_126):
    feature = _clean(ibf_replacement_126)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_131'] = {'inputs': ['ibf_replacement_126'], 'func': ibf_replacement_d2_131}


def ibf_replacement_d2_132(ibf_replacement_127):
    feature = _clean(ibf_replacement_127)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_132'] = {'inputs': ['ibf_replacement_127'], 'func': ibf_replacement_d2_132}


def ibf_replacement_d2_133(ibf_replacement_128):
    feature = _clean(ibf_replacement_128)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_133'] = {'inputs': ['ibf_replacement_128'], 'func': ibf_replacement_d2_133}


def ibf_replacement_d2_134(ibf_replacement_129):
    feature = _clean(ibf_replacement_129)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_134'] = {'inputs': ['ibf_replacement_129'], 'func': ibf_replacement_d2_134}


def ibf_replacement_d2_135(ibf_replacement_130):
    feature = _clean(ibf_replacement_130)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_135'] = {'inputs': ['ibf_replacement_130'], 'func': ibf_replacement_d2_135}


def ibf_replacement_d2_136(ibf_replacement_131):
    feature = _clean(ibf_replacement_131)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_136'] = {'inputs': ['ibf_replacement_131'], 'func': ibf_replacement_d2_136}


def ibf_replacement_d2_137(ibf_replacement_132):
    feature = _clean(ibf_replacement_132)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_137'] = {'inputs': ['ibf_replacement_132'], 'func': ibf_replacement_d2_137}


def ibf_replacement_d2_138(ibf_replacement_133):
    feature = _clean(ibf_replacement_133)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_138'] = {'inputs': ['ibf_replacement_133'], 'func': ibf_replacement_d2_138}


def ibf_replacement_d2_139(ibf_replacement_134):
    feature = _clean(ibf_replacement_134)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_139'] = {'inputs': ['ibf_replacement_134'], 'func': ibf_replacement_d2_139}


def ibf_replacement_d2_140(ibf_replacement_135):
    feature = _clean(ibf_replacement_135)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_140'] = {'inputs': ['ibf_replacement_135'], 'func': ibf_replacement_d2_140}


def ibf_replacement_d2_141(ibf_replacement_136):
    feature = _clean(ibf_replacement_136)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_141'] = {'inputs': ['ibf_replacement_136'], 'func': ibf_replacement_d2_141}


def ibf_replacement_d2_142(ibf_replacement_137):
    feature = _clean(ibf_replacement_137)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_142'] = {'inputs': ['ibf_replacement_137'], 'func': ibf_replacement_d2_142}


def ibf_replacement_d2_143(ibf_replacement_138):
    feature = _clean(ibf_replacement_138)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_143'] = {'inputs': ['ibf_replacement_138'], 'func': ibf_replacement_d2_143}


def ibf_replacement_d2_144(ibf_replacement_139):
    feature = _clean(ibf_replacement_139)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_144'] = {'inputs': ['ibf_replacement_139'], 'func': ibf_replacement_d2_144}


def ibf_replacement_d2_145(ibf_replacement_140):
    feature = _clean(ibf_replacement_140)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_145'] = {'inputs': ['ibf_replacement_140'], 'func': ibf_replacement_d2_145}


def ibf_replacement_d2_146(ibf_replacement_141):
    feature = _clean(ibf_replacement_141)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_146'] = {'inputs': ['ibf_replacement_141'], 'func': ibf_replacement_d2_146}


def ibf_replacement_d2_147(ibf_replacement_142):
    feature = _clean(ibf_replacement_142)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_147'] = {'inputs': ['ibf_replacement_142'], 'func': ibf_replacement_d2_147}


def ibf_replacement_d2_148(ibf_replacement_143):
    feature = _clean(ibf_replacement_143)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_148'] = {'inputs': ['ibf_replacement_143'], 'func': ibf_replacement_d2_148}


def ibf_replacement_d2_149(ibf_replacement_144):
    feature = _clean(ibf_replacement_144)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_149'] = {'inputs': ['ibf_replacement_144'], 'func': ibf_replacement_d2_149}


def ibf_replacement_d2_150(ibf_replacement_145):
    feature = _clean(ibf_replacement_145)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_150'] = {'inputs': ['ibf_replacement_145'], 'func': ibf_replacement_d2_150}


def ibf_replacement_d2_151(ibf_replacement_146):
    feature = _clean(ibf_replacement_146)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_151'] = {'inputs': ['ibf_replacement_146'], 'func': ibf_replacement_d2_151}


def ibf_replacement_d2_152(ibf_replacement_147):
    feature = _clean(ibf_replacement_147)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_152'] = {'inputs': ['ibf_replacement_147'], 'func': ibf_replacement_d2_152}


def ibf_replacement_d2_153(ibf_replacement_148):
    feature = _clean(ibf_replacement_148)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_153'] = {'inputs': ['ibf_replacement_148'], 'func': ibf_replacement_d2_153}


def ibf_replacement_d2_154(ibf_replacement_149):
    feature = _clean(ibf_replacement_149)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_154'] = {'inputs': ['ibf_replacement_149'], 'func': ibf_replacement_d2_154}


def ibf_replacement_d2_155(ibf_replacement_150):
    feature = _clean(ibf_replacement_150)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_155'] = {'inputs': ['ibf_replacement_150'], 'func': ibf_replacement_d2_155}


def ibf_replacement_d2_156(ibf_replacement_151):
    feature = _clean(ibf_replacement_151)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_156'] = {'inputs': ['ibf_replacement_151'], 'func': ibf_replacement_d2_156}


def ibf_replacement_d2_157(ibf_replacement_152):
    feature = _clean(ibf_replacement_152)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_157'] = {'inputs': ['ibf_replacement_152'], 'func': ibf_replacement_d2_157}


def ibf_replacement_d2_158(ibf_replacement_153):
    feature = _clean(ibf_replacement_153)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_158'] = {'inputs': ['ibf_replacement_153'], 'func': ibf_replacement_d2_158}


def ibf_replacement_d2_159(ibf_replacement_154):
    feature = _clean(ibf_replacement_154)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_159'] = {'inputs': ['ibf_replacement_154'], 'func': ibf_replacement_d2_159}


def ibf_replacement_d2_160(ibf_replacement_155):
    feature = _clean(ibf_replacement_155)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_160'] = {'inputs': ['ibf_replacement_155'], 'func': ibf_replacement_d2_160}


def ibf_replacement_d2_161(ibf_replacement_156):
    feature = _clean(ibf_replacement_156)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_161'] = {'inputs': ['ibf_replacement_156'], 'func': ibf_replacement_d2_161}


def ibf_replacement_d2_162(ibf_replacement_157):
    feature = _clean(ibf_replacement_157)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_162'] = {'inputs': ['ibf_replacement_157'], 'func': ibf_replacement_d2_162}


def ibf_replacement_d2_163(ibf_replacement_158):
    feature = _clean(ibf_replacement_158)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_163'] = {'inputs': ['ibf_replacement_158'], 'func': ibf_replacement_d2_163}


def ibf_replacement_d2_164(ibf_replacement_159):
    feature = _clean(ibf_replacement_159)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_164'] = {'inputs': ['ibf_replacement_159'], 'func': ibf_replacement_d2_164}


def ibf_replacement_d2_165(ibf_replacement_160):
    feature = _clean(ibf_replacement_160)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_165'] = {'inputs': ['ibf_replacement_160'], 'func': ibf_replacement_d2_165}


def ibf_replacement_d2_166(ibf_replacement_161):
    feature = _clean(ibf_replacement_161)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_166'] = {'inputs': ['ibf_replacement_161'], 'func': ibf_replacement_d2_166}


def ibf_replacement_d2_167(ibf_replacement_162):
    feature = _clean(ibf_replacement_162)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_167'] = {'inputs': ['ibf_replacement_162'], 'func': ibf_replacement_d2_167}


def ibf_replacement_d2_168(ibf_replacement_163):
    feature = _clean(ibf_replacement_163)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_168'] = {'inputs': ['ibf_replacement_163'], 'func': ibf_replacement_d2_168}


def ibf_replacement_d2_169(ibf_replacement_164):
    feature = _clean(ibf_replacement_164)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_169'] = {'inputs': ['ibf_replacement_164'], 'func': ibf_replacement_d2_169}


def ibf_replacement_d2_170(ibf_replacement_165):
    feature = _clean(ibf_replacement_165)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
IBF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibf_replacement_d2_170'] = {'inputs': ['ibf_replacement_165'], 'func': ibf_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63(ibf_003_top_holder_concentration_63):
    return _base_universe_d2(ibf_003_top_holder_concentration_63, 1)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63'] = {'inputs': ['ibf_003_top_holder_concentration_63'], 'func': ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63}


def ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84(ibf_004_institutional_net_flow_84):
    return _base_universe_d2(ibf_004_institutional_net_flow_84, 2)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84'] = {'inputs': ['ibf_004_institutional_net_flow_84'], 'func': ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84}


def ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126(ibf_005_forced_selling_pressure_126):
    return _base_universe_d2(ibf_005_forced_selling_pressure_126, 3)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126'] = {'inputs': ['ibf_005_forced_selling_pressure_126'], 'func': ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126}


def ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189(ibf_006_holder_base_volatility_189):
    return _base_universe_d2(ibf_006_holder_base_volatility_189, 4)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189'] = {'inputs': ['ibf_006_holder_base_volatility_189'], 'func': ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189}


def ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504(ibf_009_top_holder_concentration_504):
    return _base_universe_d2(ibf_009_top_holder_concentration_504, 5)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504'] = {'inputs': ['ibf_009_top_holder_concentration_504'], 'func': ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504}


def ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756(ibf_010_institutional_net_flow_756):
    return _base_universe_d2(ibf_010_institutional_net_flow_756, 6)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756'] = {'inputs': ['ibf_010_institutional_net_flow_756'], 'func': ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756}


def ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008(ibf_011_forced_selling_pressure_1008):
    return _base_universe_d2(ibf_011_forced_selling_pressure_1008, 7)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008'] = {'inputs': ['ibf_011_forced_selling_pressure_1008'], 'func': ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008}


def ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260(ibf_012_holder_base_volatility_1260):
    return _base_universe_d2(ibf_012_holder_base_volatility_1260, 8)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260'] = {'inputs': ['ibf_012_holder_base_volatility_1260'], 'func': ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260}


def ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252(ibf_015_top_holder_concentration_252):
    return _base_universe_d2(ibf_015_top_holder_concentration_252, 9)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252'] = {'inputs': ['ibf_015_top_holder_concentration_252'], 'func': ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252}


def ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21(ibf_016_institutional_net_flow_21):
    return _base_universe_d2(ibf_016_institutional_net_flow_21, 10)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21'] = {'inputs': ['ibf_016_institutional_net_flow_21'], 'func': ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21}


def ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42(ibf_017_forced_selling_pressure_42):
    return _base_universe_d2(ibf_017_forced_selling_pressure_42, 11)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42'] = {'inputs': ['ibf_017_forced_selling_pressure_42'], 'func': ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42}


def ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63(ibf_018_holder_base_volatility_63):
    return _base_universe_d2(ibf_018_holder_base_volatility_63, 12)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63'] = {'inputs': ['ibf_018_holder_base_volatility_63'], 'func': ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63}


def ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189(ibf_021_top_holder_concentration_189):
    return _base_universe_d2(ibf_021_top_holder_concentration_189, 13)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189'] = {'inputs': ['ibf_021_top_holder_concentration_189'], 'func': ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189}


def ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252(ibf_022_institutional_net_flow_252):
    return _base_universe_d2(ibf_022_institutional_net_flow_252, 14)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252'] = {'inputs': ['ibf_022_institutional_net_flow_252'], 'func': ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252}


def ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378(ibf_023_forced_selling_pressure_378):
    return _base_universe_d2(ibf_023_forced_selling_pressure_378, 15)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378'] = {'inputs': ['ibf_023_forced_selling_pressure_378'], 'func': ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378}


def ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504(ibf_024_holder_base_volatility_504):
    return _base_universe_d2(ibf_024_holder_base_volatility_504, 16)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504'] = {'inputs': ['ibf_024_holder_base_volatility_504'], 'func': ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504}


def ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260(ibf_027_top_holder_concentration_1260):
    return _base_universe_d2(ibf_027_top_holder_concentration_1260, 17)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260'] = {'inputs': ['ibf_027_top_holder_concentration_1260'], 'func': ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260}


def ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512(ibf_028_institutional_net_flow_1512):
    return _base_universe_d2(ibf_028_institutional_net_flow_1512, 18)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512'] = {'inputs': ['ibf_028_institutional_net_flow_1512'], 'func': ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512}


def ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63(ibf_029_forced_selling_pressure_63):
    return _base_universe_d2(ibf_029_forced_selling_pressure_63, 19)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63'] = {'inputs': ['ibf_029_forced_selling_pressure_63'], 'func': ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63}


def ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252(ibf_030_holder_base_volatility_252):
    return _base_universe_d2(ibf_030_holder_base_volatility_252, 20)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252'] = {'inputs': ['ibf_030_holder_base_volatility_252'], 'func': ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252}


def ibf_base_universe_d2_021_ibf_basefill_001(ibf_basefill_001):
    return _base_universe_d2(ibf_basefill_001, 21)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_021_ibf_basefill_001'] = {'inputs': ['ibf_basefill_001'], 'func': ibf_base_universe_d2_021_ibf_basefill_001}


def ibf_base_universe_d2_022_ibf_basefill_002(ibf_basefill_002):
    return _base_universe_d2(ibf_basefill_002, 22)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_022_ibf_basefill_002'] = {'inputs': ['ibf_basefill_002'], 'func': ibf_base_universe_d2_022_ibf_basefill_002}


def ibf_base_universe_d2_023_ibf_basefill_007(ibf_basefill_007):
    return _base_universe_d2(ibf_basefill_007, 23)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_023_ibf_basefill_007'] = {'inputs': ['ibf_basefill_007'], 'func': ibf_base_universe_d2_023_ibf_basefill_007}


def ibf_base_universe_d2_024_ibf_basefill_008(ibf_basefill_008):
    return _base_universe_d2(ibf_basefill_008, 24)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_024_ibf_basefill_008'] = {'inputs': ['ibf_basefill_008'], 'func': ibf_base_universe_d2_024_ibf_basefill_008}


def ibf_base_universe_d2_025_ibf_basefill_013(ibf_basefill_013):
    return _base_universe_d2(ibf_basefill_013, 25)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_025_ibf_basefill_013'] = {'inputs': ['ibf_basefill_013'], 'func': ibf_base_universe_d2_025_ibf_basefill_013}


def ibf_base_universe_d2_026_ibf_basefill_014(ibf_basefill_014):
    return _base_universe_d2(ibf_basefill_014, 26)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_026_ibf_basefill_014'] = {'inputs': ['ibf_basefill_014'], 'func': ibf_base_universe_d2_026_ibf_basefill_014}


def ibf_base_universe_d2_027_ibf_basefill_019(ibf_basefill_019):
    return _base_universe_d2(ibf_basefill_019, 27)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_027_ibf_basefill_019'] = {'inputs': ['ibf_basefill_019'], 'func': ibf_base_universe_d2_027_ibf_basefill_019}


def ibf_base_universe_d2_028_ibf_basefill_020(ibf_basefill_020):
    return _base_universe_d2(ibf_basefill_020, 28)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_028_ibf_basefill_020'] = {'inputs': ['ibf_basefill_020'], 'func': ibf_base_universe_d2_028_ibf_basefill_020}


def ibf_base_universe_d2_029_ibf_basefill_025(ibf_basefill_025):
    return _base_universe_d2(ibf_basefill_025, 29)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_029_ibf_basefill_025'] = {'inputs': ['ibf_basefill_025'], 'func': ibf_base_universe_d2_029_ibf_basefill_025}


def ibf_base_universe_d2_030_ibf_basefill_026(ibf_basefill_026):
    return _base_universe_d2(ibf_basefill_026, 30)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_030_ibf_basefill_026'] = {'inputs': ['ibf_basefill_026'], 'func': ibf_base_universe_d2_030_ibf_basefill_026}


def ibf_base_universe_d2_031_ibf_basefill_031(ibf_basefill_031):
    return _base_universe_d2(ibf_basefill_031, 31)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_031_ibf_basefill_031'] = {'inputs': ['ibf_basefill_031'], 'func': ibf_base_universe_d2_031_ibf_basefill_031}


def ibf_base_universe_d2_032_ibf_basefill_032(ibf_basefill_032):
    return _base_universe_d2(ibf_basefill_032, 32)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_032_ibf_basefill_032'] = {'inputs': ['ibf_basefill_032'], 'func': ibf_base_universe_d2_032_ibf_basefill_032}


def ibf_base_universe_d2_033_ibf_basefill_033(ibf_basefill_033):
    return _base_universe_d2(ibf_basefill_033, 33)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_033_ibf_basefill_033'] = {'inputs': ['ibf_basefill_033'], 'func': ibf_base_universe_d2_033_ibf_basefill_033}


def ibf_base_universe_d2_034_ibf_basefill_034(ibf_basefill_034):
    return _base_universe_d2(ibf_basefill_034, 34)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_034_ibf_basefill_034'] = {'inputs': ['ibf_basefill_034'], 'func': ibf_base_universe_d2_034_ibf_basefill_034}


def ibf_base_universe_d2_035_ibf_basefill_035(ibf_basefill_035):
    return _base_universe_d2(ibf_basefill_035, 35)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_035_ibf_basefill_035'] = {'inputs': ['ibf_basefill_035'], 'func': ibf_base_universe_d2_035_ibf_basefill_035}


def ibf_base_universe_d2_036_ibf_basefill_036(ibf_basefill_036):
    return _base_universe_d2(ibf_basefill_036, 36)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_036_ibf_basefill_036'] = {'inputs': ['ibf_basefill_036'], 'func': ibf_base_universe_d2_036_ibf_basefill_036}


def ibf_base_universe_d2_037_ibf_basefill_037(ibf_basefill_037):
    return _base_universe_d2(ibf_basefill_037, 37)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_037_ibf_basefill_037'] = {'inputs': ['ibf_basefill_037'], 'func': ibf_base_universe_d2_037_ibf_basefill_037}


def ibf_base_universe_d2_038_ibf_basefill_038(ibf_basefill_038):
    return _base_universe_d2(ibf_basefill_038, 38)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_038_ibf_basefill_038'] = {'inputs': ['ibf_basefill_038'], 'func': ibf_base_universe_d2_038_ibf_basefill_038}


def ibf_base_universe_d2_039_ibf_basefill_039(ibf_basefill_039):
    return _base_universe_d2(ibf_basefill_039, 39)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_039_ibf_basefill_039'] = {'inputs': ['ibf_basefill_039'], 'func': ibf_base_universe_d2_039_ibf_basefill_039}


def ibf_base_universe_d2_040_ibf_basefill_040(ibf_basefill_040):
    return _base_universe_d2(ibf_basefill_040, 40)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_040_ibf_basefill_040'] = {'inputs': ['ibf_basefill_040'], 'func': ibf_base_universe_d2_040_ibf_basefill_040}


def ibf_base_universe_d2_041_ibf_basefill_041(ibf_basefill_041):
    return _base_universe_d2(ibf_basefill_041, 41)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_041_ibf_basefill_041'] = {'inputs': ['ibf_basefill_041'], 'func': ibf_base_universe_d2_041_ibf_basefill_041}


def ibf_base_universe_d2_042_ibf_basefill_042(ibf_basefill_042):
    return _base_universe_d2(ibf_basefill_042, 42)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_042_ibf_basefill_042'] = {'inputs': ['ibf_basefill_042'], 'func': ibf_base_universe_d2_042_ibf_basefill_042}


def ibf_base_universe_d2_043_ibf_basefill_043(ibf_basefill_043):
    return _base_universe_d2(ibf_basefill_043, 43)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_043_ibf_basefill_043'] = {'inputs': ['ibf_basefill_043'], 'func': ibf_base_universe_d2_043_ibf_basefill_043}


def ibf_base_universe_d2_044_ibf_basefill_044(ibf_basefill_044):
    return _base_universe_d2(ibf_basefill_044, 44)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_044_ibf_basefill_044'] = {'inputs': ['ibf_basefill_044'], 'func': ibf_base_universe_d2_044_ibf_basefill_044}


def ibf_base_universe_d2_045_ibf_basefill_045(ibf_basefill_045):
    return _base_universe_d2(ibf_basefill_045, 45)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_045_ibf_basefill_045'] = {'inputs': ['ibf_basefill_045'], 'func': ibf_base_universe_d2_045_ibf_basefill_045}


def ibf_base_universe_d2_046_ibf_basefill_046(ibf_basefill_046):
    return _base_universe_d2(ibf_basefill_046, 46)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_046_ibf_basefill_046'] = {'inputs': ['ibf_basefill_046'], 'func': ibf_base_universe_d2_046_ibf_basefill_046}


def ibf_base_universe_d2_047_ibf_basefill_047(ibf_basefill_047):
    return _base_universe_d2(ibf_basefill_047, 47)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_047_ibf_basefill_047'] = {'inputs': ['ibf_basefill_047'], 'func': ibf_base_universe_d2_047_ibf_basefill_047}


def ibf_base_universe_d2_048_ibf_basefill_048(ibf_basefill_048):
    return _base_universe_d2(ibf_basefill_048, 48)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_048_ibf_basefill_048'] = {'inputs': ['ibf_basefill_048'], 'func': ibf_base_universe_d2_048_ibf_basefill_048}


def ibf_base_universe_d2_049_ibf_basefill_049(ibf_basefill_049):
    return _base_universe_d2(ibf_basefill_049, 49)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_049_ibf_basefill_049'] = {'inputs': ['ibf_basefill_049'], 'func': ibf_base_universe_d2_049_ibf_basefill_049}


def ibf_base_universe_d2_050_ibf_basefill_050(ibf_basefill_050):
    return _base_universe_d2(ibf_basefill_050, 50)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_050_ibf_basefill_050'] = {'inputs': ['ibf_basefill_050'], 'func': ibf_base_universe_d2_050_ibf_basefill_050}


def ibf_base_universe_d2_051_ibf_basefill_051(ibf_basefill_051):
    return _base_universe_d2(ibf_basefill_051, 51)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_051_ibf_basefill_051'] = {'inputs': ['ibf_basefill_051'], 'func': ibf_base_universe_d2_051_ibf_basefill_051}


def ibf_base_universe_d2_052_ibf_basefill_052(ibf_basefill_052):
    return _base_universe_d2(ibf_basefill_052, 52)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_052_ibf_basefill_052'] = {'inputs': ['ibf_basefill_052'], 'func': ibf_base_universe_d2_052_ibf_basefill_052}


def ibf_base_universe_d2_053_ibf_basefill_053(ibf_basefill_053):
    return _base_universe_d2(ibf_basefill_053, 53)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_053_ibf_basefill_053'] = {'inputs': ['ibf_basefill_053'], 'func': ibf_base_universe_d2_053_ibf_basefill_053}


def ibf_base_universe_d2_054_ibf_basefill_054(ibf_basefill_054):
    return _base_universe_d2(ibf_basefill_054, 54)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_054_ibf_basefill_054'] = {'inputs': ['ibf_basefill_054'], 'func': ibf_base_universe_d2_054_ibf_basefill_054}


def ibf_base_universe_d2_055_ibf_basefill_055(ibf_basefill_055):
    return _base_universe_d2(ibf_basefill_055, 55)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_055_ibf_basefill_055'] = {'inputs': ['ibf_basefill_055'], 'func': ibf_base_universe_d2_055_ibf_basefill_055}


def ibf_base_universe_d2_056_ibf_basefill_056(ibf_basefill_056):
    return _base_universe_d2(ibf_basefill_056, 56)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_056_ibf_basefill_056'] = {'inputs': ['ibf_basefill_056'], 'func': ibf_base_universe_d2_056_ibf_basefill_056}


def ibf_base_universe_d2_057_ibf_basefill_057(ibf_basefill_057):
    return _base_universe_d2(ibf_basefill_057, 57)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_057_ibf_basefill_057'] = {'inputs': ['ibf_basefill_057'], 'func': ibf_base_universe_d2_057_ibf_basefill_057}


def ibf_base_universe_d2_058_ibf_basefill_058(ibf_basefill_058):
    return _base_universe_d2(ibf_basefill_058, 58)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_058_ibf_basefill_058'] = {'inputs': ['ibf_basefill_058'], 'func': ibf_base_universe_d2_058_ibf_basefill_058}


def ibf_base_universe_d2_059_ibf_basefill_059(ibf_basefill_059):
    return _base_universe_d2(ibf_basefill_059, 59)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_059_ibf_basefill_059'] = {'inputs': ['ibf_basefill_059'], 'func': ibf_base_universe_d2_059_ibf_basefill_059}


def ibf_base_universe_d2_060_ibf_basefill_060(ibf_basefill_060):
    return _base_universe_d2(ibf_basefill_060, 60)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_060_ibf_basefill_060'] = {'inputs': ['ibf_basefill_060'], 'func': ibf_base_universe_d2_060_ibf_basefill_060}


def ibf_base_universe_d2_061_ibf_basefill_061(ibf_basefill_061):
    return _base_universe_d2(ibf_basefill_061, 61)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_061_ibf_basefill_061'] = {'inputs': ['ibf_basefill_061'], 'func': ibf_base_universe_d2_061_ibf_basefill_061}


def ibf_base_universe_d2_062_ibf_basefill_062(ibf_basefill_062):
    return _base_universe_d2(ibf_basefill_062, 62)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_062_ibf_basefill_062'] = {'inputs': ['ibf_basefill_062'], 'func': ibf_base_universe_d2_062_ibf_basefill_062}


def ibf_base_universe_d2_063_ibf_basefill_063(ibf_basefill_063):
    return _base_universe_d2(ibf_basefill_063, 63)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_063_ibf_basefill_063'] = {'inputs': ['ibf_basefill_063'], 'func': ibf_base_universe_d2_063_ibf_basefill_063}


def ibf_base_universe_d2_064_ibf_basefill_064(ibf_basefill_064):
    return _base_universe_d2(ibf_basefill_064, 64)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_064_ibf_basefill_064'] = {'inputs': ['ibf_basefill_064'], 'func': ibf_base_universe_d2_064_ibf_basefill_064}


def ibf_base_universe_d2_065_ibf_basefill_065(ibf_basefill_065):
    return _base_universe_d2(ibf_basefill_065, 65)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_065_ibf_basefill_065'] = {'inputs': ['ibf_basefill_065'], 'func': ibf_base_universe_d2_065_ibf_basefill_065}


def ibf_base_universe_d2_066_ibf_basefill_066(ibf_basefill_066):
    return _base_universe_d2(ibf_basefill_066, 66)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_066_ibf_basefill_066'] = {'inputs': ['ibf_basefill_066'], 'func': ibf_base_universe_d2_066_ibf_basefill_066}


def ibf_base_universe_d2_067_ibf_basefill_067(ibf_basefill_067):
    return _base_universe_d2(ibf_basefill_067, 67)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_067_ibf_basefill_067'] = {'inputs': ['ibf_basefill_067'], 'func': ibf_base_universe_d2_067_ibf_basefill_067}


def ibf_base_universe_d2_068_ibf_basefill_068(ibf_basefill_068):
    return _base_universe_d2(ibf_basefill_068, 68)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_068_ibf_basefill_068'] = {'inputs': ['ibf_basefill_068'], 'func': ibf_base_universe_d2_068_ibf_basefill_068}


def ibf_base_universe_d2_069_ibf_basefill_069(ibf_basefill_069):
    return _base_universe_d2(ibf_basefill_069, 69)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_069_ibf_basefill_069'] = {'inputs': ['ibf_basefill_069'], 'func': ibf_base_universe_d2_069_ibf_basefill_069}


def ibf_base_universe_d2_070_ibf_basefill_070(ibf_basefill_070):
    return _base_universe_d2(ibf_basefill_070, 70)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_070_ibf_basefill_070'] = {'inputs': ['ibf_basefill_070'], 'func': ibf_base_universe_d2_070_ibf_basefill_070}


def ibf_base_universe_d2_071_ibf_basefill_071(ibf_basefill_071):
    return _base_universe_d2(ibf_basefill_071, 71)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_071_ibf_basefill_071'] = {'inputs': ['ibf_basefill_071'], 'func': ibf_base_universe_d2_071_ibf_basefill_071}


def ibf_base_universe_d2_072_ibf_basefill_072(ibf_basefill_072):
    return _base_universe_d2(ibf_basefill_072, 72)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_072_ibf_basefill_072'] = {'inputs': ['ibf_basefill_072'], 'func': ibf_base_universe_d2_072_ibf_basefill_072}


def ibf_base_universe_d2_073_ibf_basefill_073(ibf_basefill_073):
    return _base_universe_d2(ibf_basefill_073, 73)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_073_ibf_basefill_073'] = {'inputs': ['ibf_basefill_073'], 'func': ibf_base_universe_d2_073_ibf_basefill_073}


def ibf_base_universe_d2_074_ibf_basefill_074(ibf_basefill_074):
    return _base_universe_d2(ibf_basefill_074, 74)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_074_ibf_basefill_074'] = {'inputs': ['ibf_basefill_074'], 'func': ibf_base_universe_d2_074_ibf_basefill_074}


def ibf_base_universe_d2_075_ibf_basefill_075(ibf_basefill_075):
    return _base_universe_d2(ibf_basefill_075, 75)
IBF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibf_base_universe_d2_075_ibf_basefill_075'] = {'inputs': ['ibf_basefill_075'], 'func': ibf_base_universe_d2_075_ibf_basefill_075}
