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



def fsp_151_fsp_001_holder_exit_1_roc_1(fsp_001_holder_exit_1):
    feature = _s(fsp_001_holder_exit_1)
    return (_roc(feature, 1)).reindex(feature.index)

def fsp_152_fsp_007_holder_exit_1_roc_42(fsp_007_holder_exit_1):
    feature = _s(fsp_007_holder_exit_1)
    return (_roc(feature, 42)).reindex(feature.index)

def fsp_153_fsp_013_holder_exit_1_roc_126(fsp_013_holder_exit_1):
    feature = _s(fsp_013_holder_exit_1)
    return (_roc(feature, 126)).reindex(feature.index)

def fsp_154_fsp_019_holder_exit_1_roc_378(fsp_019_holder_exit_1):
    feature = _s(fsp_019_holder_exit_1)
    return (_roc(feature, 378)).reindex(feature.index)

def fsp_155_fsp_025_holder_exit_1_roc_4(fsp_025_holder_exit_1):
    feature = _s(fsp_025_holder_exit_1)
    return (_roc(feature, 4)).reindex(feature.index)






















FORCED_SELLING_PROXY_REGISTRY_2ND_DERIVATIVES = {
    'fsp_151_fsp_001_holder_exit_1_roc_1': {'inputs': ['fsp_001_holder_exit_1'], 'func': fsp_151_fsp_001_holder_exit_1_roc_1},
    'fsp_152_fsp_007_holder_exit_1_roc_42': {'inputs': ['fsp_007_holder_exit_1'], 'func': fsp_152_fsp_007_holder_exit_1_roc_42},
    'fsp_153_fsp_013_holder_exit_1_roc_126': {'inputs': ['fsp_013_holder_exit_1'], 'func': fsp_153_fsp_013_holder_exit_1_roc_126},
    'fsp_154_fsp_019_holder_exit_1_roc_378': {'inputs': ['fsp_019_holder_exit_1'], 'func': fsp_154_fsp_019_holder_exit_1_roc_378},
    'fsp_155_fsp_025_holder_exit_1_roc_4': {'inputs': ['fsp_025_holder_exit_1'], 'func': fsp_155_fsp_025_holder_exit_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def fsp_replacement_d2_001(fsp_001_holder_exit_1):
    feature = _clean(fsp_001_holder_exit_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_001'] = {'inputs': ['fsp_001_holder_exit_1'], 'func': fsp_replacement_d2_001}


def fsp_replacement_d2_002(fsp_007_holder_exit_1):
    feature = _clean(fsp_007_holder_exit_1)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_002'] = {'inputs': ['fsp_007_holder_exit_1'], 'func': fsp_replacement_d2_002}


def fsp_replacement_d2_003(fsp_013_holder_exit_1):
    feature = _clean(fsp_013_holder_exit_1)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_003'] = {'inputs': ['fsp_013_holder_exit_1'], 'func': fsp_replacement_d2_003}


def fsp_replacement_d2_004(fsp_019_holder_exit_1):
    feature = _clean(fsp_019_holder_exit_1)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_004'] = {'inputs': ['fsp_019_holder_exit_1'], 'func': fsp_replacement_d2_004}


def fsp_replacement_d2_005(fsp_025_holder_exit_1):
    feature = _clean(fsp_025_holder_exit_1)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_005'] = {'inputs': ['fsp_025_holder_exit_1'], 'func': fsp_replacement_d2_005}


def fsp_replacement_d2_006(fsp_replacement_001):
    feature = _clean(fsp_replacement_001)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_006'] = {'inputs': ['fsp_replacement_001'], 'func': fsp_replacement_d2_006}


def fsp_replacement_d2_007(fsp_replacement_002):
    feature = _clean(fsp_replacement_002)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_007'] = {'inputs': ['fsp_replacement_002'], 'func': fsp_replacement_d2_007}


def fsp_replacement_d2_008(fsp_replacement_003):
    feature = _clean(fsp_replacement_003)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_008'] = {'inputs': ['fsp_replacement_003'], 'func': fsp_replacement_d2_008}


def fsp_replacement_d2_009(fsp_replacement_004):
    feature = _clean(fsp_replacement_004)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_009'] = {'inputs': ['fsp_replacement_004'], 'func': fsp_replacement_d2_009}


def fsp_replacement_d2_010(fsp_replacement_005):
    feature = _clean(fsp_replacement_005)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_010'] = {'inputs': ['fsp_replacement_005'], 'func': fsp_replacement_d2_010}


def fsp_replacement_d2_011(fsp_replacement_006):
    feature = _clean(fsp_replacement_006)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_011'] = {'inputs': ['fsp_replacement_006'], 'func': fsp_replacement_d2_011}


def fsp_replacement_d2_012(fsp_replacement_007):
    feature = _clean(fsp_replacement_007)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_012'] = {'inputs': ['fsp_replacement_007'], 'func': fsp_replacement_d2_012}


def fsp_replacement_d2_013(fsp_replacement_008):
    feature = _clean(fsp_replacement_008)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_013'] = {'inputs': ['fsp_replacement_008'], 'func': fsp_replacement_d2_013}


def fsp_replacement_d2_014(fsp_replacement_009):
    feature = _clean(fsp_replacement_009)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_014'] = {'inputs': ['fsp_replacement_009'], 'func': fsp_replacement_d2_014}


def fsp_replacement_d2_015(fsp_replacement_010):
    feature = _clean(fsp_replacement_010)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_015'] = {'inputs': ['fsp_replacement_010'], 'func': fsp_replacement_d2_015}


def fsp_replacement_d2_016(fsp_replacement_011):
    feature = _clean(fsp_replacement_011)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_016'] = {'inputs': ['fsp_replacement_011'], 'func': fsp_replacement_d2_016}


def fsp_replacement_d2_017(fsp_replacement_012):
    feature = _clean(fsp_replacement_012)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_017'] = {'inputs': ['fsp_replacement_012'], 'func': fsp_replacement_d2_017}


def fsp_replacement_d2_018(fsp_replacement_013):
    feature = _clean(fsp_replacement_013)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_018'] = {'inputs': ['fsp_replacement_013'], 'func': fsp_replacement_d2_018}


def fsp_replacement_d2_019(fsp_replacement_014):
    feature = _clean(fsp_replacement_014)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_019'] = {'inputs': ['fsp_replacement_014'], 'func': fsp_replacement_d2_019}


def fsp_replacement_d2_020(fsp_replacement_015):
    feature = _clean(fsp_replacement_015)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_020'] = {'inputs': ['fsp_replacement_015'], 'func': fsp_replacement_d2_020}


def fsp_replacement_d2_021(fsp_replacement_016):
    feature = _clean(fsp_replacement_016)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_021'] = {'inputs': ['fsp_replacement_016'], 'func': fsp_replacement_d2_021}


def fsp_replacement_d2_022(fsp_replacement_017):
    feature = _clean(fsp_replacement_017)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_022'] = {'inputs': ['fsp_replacement_017'], 'func': fsp_replacement_d2_022}


def fsp_replacement_d2_023(fsp_replacement_018):
    feature = _clean(fsp_replacement_018)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_023'] = {'inputs': ['fsp_replacement_018'], 'func': fsp_replacement_d2_023}


def fsp_replacement_d2_024(fsp_replacement_019):
    feature = _clean(fsp_replacement_019)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_024'] = {'inputs': ['fsp_replacement_019'], 'func': fsp_replacement_d2_024}


def fsp_replacement_d2_025(fsp_replacement_020):
    feature = _clean(fsp_replacement_020)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_025'] = {'inputs': ['fsp_replacement_020'], 'func': fsp_replacement_d2_025}


def fsp_replacement_d2_026(fsp_replacement_021):
    feature = _clean(fsp_replacement_021)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_026'] = {'inputs': ['fsp_replacement_021'], 'func': fsp_replacement_d2_026}


def fsp_replacement_d2_027(fsp_replacement_022):
    feature = _clean(fsp_replacement_022)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_027'] = {'inputs': ['fsp_replacement_022'], 'func': fsp_replacement_d2_027}


def fsp_replacement_d2_028(fsp_replacement_023):
    feature = _clean(fsp_replacement_023)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_028'] = {'inputs': ['fsp_replacement_023'], 'func': fsp_replacement_d2_028}


def fsp_replacement_d2_029(fsp_replacement_024):
    feature = _clean(fsp_replacement_024)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_029'] = {'inputs': ['fsp_replacement_024'], 'func': fsp_replacement_d2_029}


def fsp_replacement_d2_030(fsp_replacement_025):
    feature = _clean(fsp_replacement_025)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_030'] = {'inputs': ['fsp_replacement_025'], 'func': fsp_replacement_d2_030}


def fsp_replacement_d2_031(fsp_replacement_026):
    feature = _clean(fsp_replacement_026)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_031'] = {'inputs': ['fsp_replacement_026'], 'func': fsp_replacement_d2_031}


def fsp_replacement_d2_032(fsp_replacement_027):
    feature = _clean(fsp_replacement_027)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_032'] = {'inputs': ['fsp_replacement_027'], 'func': fsp_replacement_d2_032}


def fsp_replacement_d2_033(fsp_replacement_028):
    feature = _clean(fsp_replacement_028)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_033'] = {'inputs': ['fsp_replacement_028'], 'func': fsp_replacement_d2_033}


def fsp_replacement_d2_034(fsp_replacement_029):
    feature = _clean(fsp_replacement_029)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_034'] = {'inputs': ['fsp_replacement_029'], 'func': fsp_replacement_d2_034}


def fsp_replacement_d2_035(fsp_replacement_030):
    feature = _clean(fsp_replacement_030)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_035'] = {'inputs': ['fsp_replacement_030'], 'func': fsp_replacement_d2_035}


def fsp_replacement_d2_036(fsp_replacement_031):
    feature = _clean(fsp_replacement_031)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_036'] = {'inputs': ['fsp_replacement_031'], 'func': fsp_replacement_d2_036}


def fsp_replacement_d2_037(fsp_replacement_032):
    feature = _clean(fsp_replacement_032)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_037'] = {'inputs': ['fsp_replacement_032'], 'func': fsp_replacement_d2_037}


def fsp_replacement_d2_038(fsp_replacement_033):
    feature = _clean(fsp_replacement_033)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_038'] = {'inputs': ['fsp_replacement_033'], 'func': fsp_replacement_d2_038}


def fsp_replacement_d2_039(fsp_replacement_034):
    feature = _clean(fsp_replacement_034)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_039'] = {'inputs': ['fsp_replacement_034'], 'func': fsp_replacement_d2_039}


def fsp_replacement_d2_040(fsp_replacement_035):
    feature = _clean(fsp_replacement_035)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_040'] = {'inputs': ['fsp_replacement_035'], 'func': fsp_replacement_d2_040}


def fsp_replacement_d2_041(fsp_replacement_036):
    feature = _clean(fsp_replacement_036)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_041'] = {'inputs': ['fsp_replacement_036'], 'func': fsp_replacement_d2_041}


def fsp_replacement_d2_042(fsp_replacement_037):
    feature = _clean(fsp_replacement_037)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_042'] = {'inputs': ['fsp_replacement_037'], 'func': fsp_replacement_d2_042}


def fsp_replacement_d2_043(fsp_replacement_038):
    feature = _clean(fsp_replacement_038)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_043'] = {'inputs': ['fsp_replacement_038'], 'func': fsp_replacement_d2_043}


def fsp_replacement_d2_044(fsp_replacement_039):
    feature = _clean(fsp_replacement_039)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_044'] = {'inputs': ['fsp_replacement_039'], 'func': fsp_replacement_d2_044}


def fsp_replacement_d2_045(fsp_replacement_040):
    feature = _clean(fsp_replacement_040)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_045'] = {'inputs': ['fsp_replacement_040'], 'func': fsp_replacement_d2_045}


def fsp_replacement_d2_046(fsp_replacement_041):
    feature = _clean(fsp_replacement_041)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_046'] = {'inputs': ['fsp_replacement_041'], 'func': fsp_replacement_d2_046}


def fsp_replacement_d2_047(fsp_replacement_042):
    feature = _clean(fsp_replacement_042)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_047'] = {'inputs': ['fsp_replacement_042'], 'func': fsp_replacement_d2_047}


def fsp_replacement_d2_048(fsp_replacement_043):
    feature = _clean(fsp_replacement_043)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_048'] = {'inputs': ['fsp_replacement_043'], 'func': fsp_replacement_d2_048}


def fsp_replacement_d2_049(fsp_replacement_044):
    feature = _clean(fsp_replacement_044)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_049'] = {'inputs': ['fsp_replacement_044'], 'func': fsp_replacement_d2_049}


def fsp_replacement_d2_050(fsp_replacement_045):
    feature = _clean(fsp_replacement_045)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_050'] = {'inputs': ['fsp_replacement_045'], 'func': fsp_replacement_d2_050}


def fsp_replacement_d2_051(fsp_replacement_046):
    feature = _clean(fsp_replacement_046)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_051'] = {'inputs': ['fsp_replacement_046'], 'func': fsp_replacement_d2_051}


def fsp_replacement_d2_052(fsp_replacement_047):
    feature = _clean(fsp_replacement_047)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_052'] = {'inputs': ['fsp_replacement_047'], 'func': fsp_replacement_d2_052}


def fsp_replacement_d2_053(fsp_replacement_048):
    feature = _clean(fsp_replacement_048)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_053'] = {'inputs': ['fsp_replacement_048'], 'func': fsp_replacement_d2_053}


def fsp_replacement_d2_054(fsp_replacement_049):
    feature = _clean(fsp_replacement_049)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_054'] = {'inputs': ['fsp_replacement_049'], 'func': fsp_replacement_d2_054}


def fsp_replacement_d2_055(fsp_replacement_050):
    feature = _clean(fsp_replacement_050)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_055'] = {'inputs': ['fsp_replacement_050'], 'func': fsp_replacement_d2_055}


def fsp_replacement_d2_056(fsp_replacement_051):
    feature = _clean(fsp_replacement_051)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_056'] = {'inputs': ['fsp_replacement_051'], 'func': fsp_replacement_d2_056}


def fsp_replacement_d2_057(fsp_replacement_052):
    feature = _clean(fsp_replacement_052)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_057'] = {'inputs': ['fsp_replacement_052'], 'func': fsp_replacement_d2_057}


def fsp_replacement_d2_058(fsp_replacement_053):
    feature = _clean(fsp_replacement_053)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_058'] = {'inputs': ['fsp_replacement_053'], 'func': fsp_replacement_d2_058}


def fsp_replacement_d2_059(fsp_replacement_054):
    feature = _clean(fsp_replacement_054)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_059'] = {'inputs': ['fsp_replacement_054'], 'func': fsp_replacement_d2_059}


def fsp_replacement_d2_060(fsp_replacement_055):
    feature = _clean(fsp_replacement_055)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_060'] = {'inputs': ['fsp_replacement_055'], 'func': fsp_replacement_d2_060}


def fsp_replacement_d2_061(fsp_replacement_056):
    feature = _clean(fsp_replacement_056)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_061'] = {'inputs': ['fsp_replacement_056'], 'func': fsp_replacement_d2_061}


def fsp_replacement_d2_062(fsp_replacement_057):
    feature = _clean(fsp_replacement_057)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_062'] = {'inputs': ['fsp_replacement_057'], 'func': fsp_replacement_d2_062}


def fsp_replacement_d2_063(fsp_replacement_058):
    feature = _clean(fsp_replacement_058)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_063'] = {'inputs': ['fsp_replacement_058'], 'func': fsp_replacement_d2_063}


def fsp_replacement_d2_064(fsp_replacement_059):
    feature = _clean(fsp_replacement_059)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_064'] = {'inputs': ['fsp_replacement_059'], 'func': fsp_replacement_d2_064}


def fsp_replacement_d2_065(fsp_replacement_060):
    feature = _clean(fsp_replacement_060)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_065'] = {'inputs': ['fsp_replacement_060'], 'func': fsp_replacement_d2_065}


def fsp_replacement_d2_066(fsp_replacement_061):
    feature = _clean(fsp_replacement_061)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_066'] = {'inputs': ['fsp_replacement_061'], 'func': fsp_replacement_d2_066}


def fsp_replacement_d2_067(fsp_replacement_062):
    feature = _clean(fsp_replacement_062)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_067'] = {'inputs': ['fsp_replacement_062'], 'func': fsp_replacement_d2_067}


def fsp_replacement_d2_068(fsp_replacement_063):
    feature = _clean(fsp_replacement_063)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_068'] = {'inputs': ['fsp_replacement_063'], 'func': fsp_replacement_d2_068}


def fsp_replacement_d2_069(fsp_replacement_064):
    feature = _clean(fsp_replacement_064)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_069'] = {'inputs': ['fsp_replacement_064'], 'func': fsp_replacement_d2_069}


def fsp_replacement_d2_070(fsp_replacement_065):
    feature = _clean(fsp_replacement_065)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_070'] = {'inputs': ['fsp_replacement_065'], 'func': fsp_replacement_d2_070}


def fsp_replacement_d2_071(fsp_replacement_066):
    feature = _clean(fsp_replacement_066)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_071'] = {'inputs': ['fsp_replacement_066'], 'func': fsp_replacement_d2_071}


def fsp_replacement_d2_072(fsp_replacement_067):
    feature = _clean(fsp_replacement_067)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_072'] = {'inputs': ['fsp_replacement_067'], 'func': fsp_replacement_d2_072}


def fsp_replacement_d2_073(fsp_replacement_068):
    feature = _clean(fsp_replacement_068)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_073'] = {'inputs': ['fsp_replacement_068'], 'func': fsp_replacement_d2_073}


def fsp_replacement_d2_074(fsp_replacement_069):
    feature = _clean(fsp_replacement_069)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_074'] = {'inputs': ['fsp_replacement_069'], 'func': fsp_replacement_d2_074}


def fsp_replacement_d2_075(fsp_replacement_070):
    feature = _clean(fsp_replacement_070)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_075'] = {'inputs': ['fsp_replacement_070'], 'func': fsp_replacement_d2_075}


def fsp_replacement_d2_076(fsp_replacement_071):
    feature = _clean(fsp_replacement_071)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_076'] = {'inputs': ['fsp_replacement_071'], 'func': fsp_replacement_d2_076}


def fsp_replacement_d2_077(fsp_replacement_072):
    feature = _clean(fsp_replacement_072)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_077'] = {'inputs': ['fsp_replacement_072'], 'func': fsp_replacement_d2_077}


def fsp_replacement_d2_078(fsp_replacement_073):
    feature = _clean(fsp_replacement_073)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_078'] = {'inputs': ['fsp_replacement_073'], 'func': fsp_replacement_d2_078}


def fsp_replacement_d2_079(fsp_replacement_074):
    feature = _clean(fsp_replacement_074)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_079'] = {'inputs': ['fsp_replacement_074'], 'func': fsp_replacement_d2_079}


def fsp_replacement_d2_080(fsp_replacement_075):
    feature = _clean(fsp_replacement_075)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_080'] = {'inputs': ['fsp_replacement_075'], 'func': fsp_replacement_d2_080}


def fsp_replacement_d2_081(fsp_replacement_076):
    feature = _clean(fsp_replacement_076)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_081'] = {'inputs': ['fsp_replacement_076'], 'func': fsp_replacement_d2_081}


def fsp_replacement_d2_082(fsp_replacement_077):
    feature = _clean(fsp_replacement_077)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_082'] = {'inputs': ['fsp_replacement_077'], 'func': fsp_replacement_d2_082}


def fsp_replacement_d2_083(fsp_replacement_078):
    feature = _clean(fsp_replacement_078)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_083'] = {'inputs': ['fsp_replacement_078'], 'func': fsp_replacement_d2_083}


def fsp_replacement_d2_084(fsp_replacement_079):
    feature = _clean(fsp_replacement_079)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_084'] = {'inputs': ['fsp_replacement_079'], 'func': fsp_replacement_d2_084}


def fsp_replacement_d2_085(fsp_replacement_080):
    feature = _clean(fsp_replacement_080)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_085'] = {'inputs': ['fsp_replacement_080'], 'func': fsp_replacement_d2_085}


def fsp_replacement_d2_086(fsp_replacement_081):
    feature = _clean(fsp_replacement_081)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_086'] = {'inputs': ['fsp_replacement_081'], 'func': fsp_replacement_d2_086}


def fsp_replacement_d2_087(fsp_replacement_082):
    feature = _clean(fsp_replacement_082)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_087'] = {'inputs': ['fsp_replacement_082'], 'func': fsp_replacement_d2_087}


def fsp_replacement_d2_088(fsp_replacement_083):
    feature = _clean(fsp_replacement_083)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_088'] = {'inputs': ['fsp_replacement_083'], 'func': fsp_replacement_d2_088}


def fsp_replacement_d2_089(fsp_replacement_084):
    feature = _clean(fsp_replacement_084)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_089'] = {'inputs': ['fsp_replacement_084'], 'func': fsp_replacement_d2_089}


def fsp_replacement_d2_090(fsp_replacement_085):
    feature = _clean(fsp_replacement_085)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_090'] = {'inputs': ['fsp_replacement_085'], 'func': fsp_replacement_d2_090}


def fsp_replacement_d2_091(fsp_replacement_086):
    feature = _clean(fsp_replacement_086)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_091'] = {'inputs': ['fsp_replacement_086'], 'func': fsp_replacement_d2_091}


def fsp_replacement_d2_092(fsp_replacement_087):
    feature = _clean(fsp_replacement_087)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_092'] = {'inputs': ['fsp_replacement_087'], 'func': fsp_replacement_d2_092}


def fsp_replacement_d2_093(fsp_replacement_088):
    feature = _clean(fsp_replacement_088)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_093'] = {'inputs': ['fsp_replacement_088'], 'func': fsp_replacement_d2_093}


def fsp_replacement_d2_094(fsp_replacement_089):
    feature = _clean(fsp_replacement_089)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_094'] = {'inputs': ['fsp_replacement_089'], 'func': fsp_replacement_d2_094}


def fsp_replacement_d2_095(fsp_replacement_090):
    feature = _clean(fsp_replacement_090)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_095'] = {'inputs': ['fsp_replacement_090'], 'func': fsp_replacement_d2_095}


def fsp_replacement_d2_096(fsp_replacement_091):
    feature = _clean(fsp_replacement_091)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_096'] = {'inputs': ['fsp_replacement_091'], 'func': fsp_replacement_d2_096}


def fsp_replacement_d2_097(fsp_replacement_092):
    feature = _clean(fsp_replacement_092)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_097'] = {'inputs': ['fsp_replacement_092'], 'func': fsp_replacement_d2_097}


def fsp_replacement_d2_098(fsp_replacement_093):
    feature = _clean(fsp_replacement_093)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_098'] = {'inputs': ['fsp_replacement_093'], 'func': fsp_replacement_d2_098}


def fsp_replacement_d2_099(fsp_replacement_094):
    feature = _clean(fsp_replacement_094)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_099'] = {'inputs': ['fsp_replacement_094'], 'func': fsp_replacement_d2_099}


def fsp_replacement_d2_100(fsp_replacement_095):
    feature = _clean(fsp_replacement_095)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_100'] = {'inputs': ['fsp_replacement_095'], 'func': fsp_replacement_d2_100}


def fsp_replacement_d2_101(fsp_replacement_096):
    feature = _clean(fsp_replacement_096)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_101'] = {'inputs': ['fsp_replacement_096'], 'func': fsp_replacement_d2_101}


def fsp_replacement_d2_102(fsp_replacement_097):
    feature = _clean(fsp_replacement_097)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_102'] = {'inputs': ['fsp_replacement_097'], 'func': fsp_replacement_d2_102}


def fsp_replacement_d2_103(fsp_replacement_098):
    feature = _clean(fsp_replacement_098)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_103'] = {'inputs': ['fsp_replacement_098'], 'func': fsp_replacement_d2_103}


def fsp_replacement_d2_104(fsp_replacement_099):
    feature = _clean(fsp_replacement_099)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_104'] = {'inputs': ['fsp_replacement_099'], 'func': fsp_replacement_d2_104}


def fsp_replacement_d2_105(fsp_replacement_100):
    feature = _clean(fsp_replacement_100)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_105'] = {'inputs': ['fsp_replacement_100'], 'func': fsp_replacement_d2_105}


def fsp_replacement_d2_106(fsp_replacement_101):
    feature = _clean(fsp_replacement_101)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_106'] = {'inputs': ['fsp_replacement_101'], 'func': fsp_replacement_d2_106}


def fsp_replacement_d2_107(fsp_replacement_102):
    feature = _clean(fsp_replacement_102)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_107'] = {'inputs': ['fsp_replacement_102'], 'func': fsp_replacement_d2_107}


def fsp_replacement_d2_108(fsp_replacement_103):
    feature = _clean(fsp_replacement_103)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_108'] = {'inputs': ['fsp_replacement_103'], 'func': fsp_replacement_d2_108}


def fsp_replacement_d2_109(fsp_replacement_104):
    feature = _clean(fsp_replacement_104)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_109'] = {'inputs': ['fsp_replacement_104'], 'func': fsp_replacement_d2_109}


def fsp_replacement_d2_110(fsp_replacement_105):
    feature = _clean(fsp_replacement_105)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_110'] = {'inputs': ['fsp_replacement_105'], 'func': fsp_replacement_d2_110}


def fsp_replacement_d2_111(fsp_replacement_106):
    feature = _clean(fsp_replacement_106)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_111'] = {'inputs': ['fsp_replacement_106'], 'func': fsp_replacement_d2_111}


def fsp_replacement_d2_112(fsp_replacement_107):
    feature = _clean(fsp_replacement_107)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_112'] = {'inputs': ['fsp_replacement_107'], 'func': fsp_replacement_d2_112}


def fsp_replacement_d2_113(fsp_replacement_108):
    feature = _clean(fsp_replacement_108)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_113'] = {'inputs': ['fsp_replacement_108'], 'func': fsp_replacement_d2_113}


def fsp_replacement_d2_114(fsp_replacement_109):
    feature = _clean(fsp_replacement_109)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_114'] = {'inputs': ['fsp_replacement_109'], 'func': fsp_replacement_d2_114}


def fsp_replacement_d2_115(fsp_replacement_110):
    feature = _clean(fsp_replacement_110)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_115'] = {'inputs': ['fsp_replacement_110'], 'func': fsp_replacement_d2_115}


def fsp_replacement_d2_116(fsp_replacement_111):
    feature = _clean(fsp_replacement_111)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_116'] = {'inputs': ['fsp_replacement_111'], 'func': fsp_replacement_d2_116}


def fsp_replacement_d2_117(fsp_replacement_112):
    feature = _clean(fsp_replacement_112)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_117'] = {'inputs': ['fsp_replacement_112'], 'func': fsp_replacement_d2_117}


def fsp_replacement_d2_118(fsp_replacement_113):
    feature = _clean(fsp_replacement_113)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_118'] = {'inputs': ['fsp_replacement_113'], 'func': fsp_replacement_d2_118}


def fsp_replacement_d2_119(fsp_replacement_114):
    feature = _clean(fsp_replacement_114)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_119'] = {'inputs': ['fsp_replacement_114'], 'func': fsp_replacement_d2_119}


def fsp_replacement_d2_120(fsp_replacement_115):
    feature = _clean(fsp_replacement_115)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_120'] = {'inputs': ['fsp_replacement_115'], 'func': fsp_replacement_d2_120}


def fsp_replacement_d2_121(fsp_replacement_116):
    feature = _clean(fsp_replacement_116)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_121'] = {'inputs': ['fsp_replacement_116'], 'func': fsp_replacement_d2_121}


def fsp_replacement_d2_122(fsp_replacement_117):
    feature = _clean(fsp_replacement_117)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_122'] = {'inputs': ['fsp_replacement_117'], 'func': fsp_replacement_d2_122}


def fsp_replacement_d2_123(fsp_replacement_118):
    feature = _clean(fsp_replacement_118)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_123'] = {'inputs': ['fsp_replacement_118'], 'func': fsp_replacement_d2_123}


def fsp_replacement_d2_124(fsp_replacement_119):
    feature = _clean(fsp_replacement_119)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_124'] = {'inputs': ['fsp_replacement_119'], 'func': fsp_replacement_d2_124}


def fsp_replacement_d2_125(fsp_replacement_120):
    feature = _clean(fsp_replacement_120)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_125'] = {'inputs': ['fsp_replacement_120'], 'func': fsp_replacement_d2_125}


def fsp_replacement_d2_126(fsp_replacement_121):
    feature = _clean(fsp_replacement_121)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_126'] = {'inputs': ['fsp_replacement_121'], 'func': fsp_replacement_d2_126}


def fsp_replacement_d2_127(fsp_replacement_122):
    feature = _clean(fsp_replacement_122)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_127'] = {'inputs': ['fsp_replacement_122'], 'func': fsp_replacement_d2_127}


def fsp_replacement_d2_128(fsp_replacement_123):
    feature = _clean(fsp_replacement_123)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_128'] = {'inputs': ['fsp_replacement_123'], 'func': fsp_replacement_d2_128}


def fsp_replacement_d2_129(fsp_replacement_124):
    feature = _clean(fsp_replacement_124)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_129'] = {'inputs': ['fsp_replacement_124'], 'func': fsp_replacement_d2_129}


def fsp_replacement_d2_130(fsp_replacement_125):
    feature = _clean(fsp_replacement_125)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_130'] = {'inputs': ['fsp_replacement_125'], 'func': fsp_replacement_d2_130}


def fsp_replacement_d2_131(fsp_replacement_126):
    feature = _clean(fsp_replacement_126)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_131'] = {'inputs': ['fsp_replacement_126'], 'func': fsp_replacement_d2_131}


def fsp_replacement_d2_132(fsp_replacement_127):
    feature = _clean(fsp_replacement_127)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_132'] = {'inputs': ['fsp_replacement_127'], 'func': fsp_replacement_d2_132}


def fsp_replacement_d2_133(fsp_replacement_128):
    feature = _clean(fsp_replacement_128)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_133'] = {'inputs': ['fsp_replacement_128'], 'func': fsp_replacement_d2_133}


def fsp_replacement_d2_134(fsp_replacement_129):
    feature = _clean(fsp_replacement_129)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_134'] = {'inputs': ['fsp_replacement_129'], 'func': fsp_replacement_d2_134}


def fsp_replacement_d2_135(fsp_replacement_130):
    feature = _clean(fsp_replacement_130)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_135'] = {'inputs': ['fsp_replacement_130'], 'func': fsp_replacement_d2_135}


def fsp_replacement_d2_136(fsp_replacement_131):
    feature = _clean(fsp_replacement_131)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_136'] = {'inputs': ['fsp_replacement_131'], 'func': fsp_replacement_d2_136}


def fsp_replacement_d2_137(fsp_replacement_132):
    feature = _clean(fsp_replacement_132)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_137'] = {'inputs': ['fsp_replacement_132'], 'func': fsp_replacement_d2_137}


def fsp_replacement_d2_138(fsp_replacement_133):
    feature = _clean(fsp_replacement_133)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_138'] = {'inputs': ['fsp_replacement_133'], 'func': fsp_replacement_d2_138}


def fsp_replacement_d2_139(fsp_replacement_134):
    feature = _clean(fsp_replacement_134)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_139'] = {'inputs': ['fsp_replacement_134'], 'func': fsp_replacement_d2_139}


def fsp_replacement_d2_140(fsp_replacement_135):
    feature = _clean(fsp_replacement_135)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_140'] = {'inputs': ['fsp_replacement_135'], 'func': fsp_replacement_d2_140}


def fsp_replacement_d2_141(fsp_replacement_136):
    feature = _clean(fsp_replacement_136)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_141'] = {'inputs': ['fsp_replacement_136'], 'func': fsp_replacement_d2_141}


def fsp_replacement_d2_142(fsp_replacement_137):
    feature = _clean(fsp_replacement_137)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_142'] = {'inputs': ['fsp_replacement_137'], 'func': fsp_replacement_d2_142}


def fsp_replacement_d2_143(fsp_replacement_138):
    feature = _clean(fsp_replacement_138)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_143'] = {'inputs': ['fsp_replacement_138'], 'func': fsp_replacement_d2_143}


def fsp_replacement_d2_144(fsp_replacement_139):
    feature = _clean(fsp_replacement_139)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_144'] = {'inputs': ['fsp_replacement_139'], 'func': fsp_replacement_d2_144}


def fsp_replacement_d2_145(fsp_replacement_140):
    feature = _clean(fsp_replacement_140)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_145'] = {'inputs': ['fsp_replacement_140'], 'func': fsp_replacement_d2_145}


def fsp_replacement_d2_146(fsp_replacement_141):
    feature = _clean(fsp_replacement_141)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_146'] = {'inputs': ['fsp_replacement_141'], 'func': fsp_replacement_d2_146}


def fsp_replacement_d2_147(fsp_replacement_142):
    feature = _clean(fsp_replacement_142)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_147'] = {'inputs': ['fsp_replacement_142'], 'func': fsp_replacement_d2_147}


def fsp_replacement_d2_148(fsp_replacement_143):
    feature = _clean(fsp_replacement_143)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_148'] = {'inputs': ['fsp_replacement_143'], 'func': fsp_replacement_d2_148}


def fsp_replacement_d2_149(fsp_replacement_144):
    feature = _clean(fsp_replacement_144)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_149'] = {'inputs': ['fsp_replacement_144'], 'func': fsp_replacement_d2_149}


def fsp_replacement_d2_150(fsp_replacement_145):
    feature = _clean(fsp_replacement_145)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_150'] = {'inputs': ['fsp_replacement_145'], 'func': fsp_replacement_d2_150}


def fsp_replacement_d2_151(fsp_replacement_146):
    feature = _clean(fsp_replacement_146)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_151'] = {'inputs': ['fsp_replacement_146'], 'func': fsp_replacement_d2_151}


def fsp_replacement_d2_152(fsp_replacement_147):
    feature = _clean(fsp_replacement_147)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_152'] = {'inputs': ['fsp_replacement_147'], 'func': fsp_replacement_d2_152}


def fsp_replacement_d2_153(fsp_replacement_148):
    feature = _clean(fsp_replacement_148)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_153'] = {'inputs': ['fsp_replacement_148'], 'func': fsp_replacement_d2_153}


def fsp_replacement_d2_154(fsp_replacement_149):
    feature = _clean(fsp_replacement_149)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_154'] = {'inputs': ['fsp_replacement_149'], 'func': fsp_replacement_d2_154}


def fsp_replacement_d2_155(fsp_replacement_150):
    feature = _clean(fsp_replacement_150)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_155'] = {'inputs': ['fsp_replacement_150'], 'func': fsp_replacement_d2_155}


def fsp_replacement_d2_156(fsp_replacement_151):
    feature = _clean(fsp_replacement_151)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_156'] = {'inputs': ['fsp_replacement_151'], 'func': fsp_replacement_d2_156}


def fsp_replacement_d2_157(fsp_replacement_152):
    feature = _clean(fsp_replacement_152)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_157'] = {'inputs': ['fsp_replacement_152'], 'func': fsp_replacement_d2_157}


def fsp_replacement_d2_158(fsp_replacement_153):
    feature = _clean(fsp_replacement_153)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_158'] = {'inputs': ['fsp_replacement_153'], 'func': fsp_replacement_d2_158}


def fsp_replacement_d2_159(fsp_replacement_154):
    feature = _clean(fsp_replacement_154)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_159'] = {'inputs': ['fsp_replacement_154'], 'func': fsp_replacement_d2_159}


def fsp_replacement_d2_160(fsp_replacement_155):
    feature = _clean(fsp_replacement_155)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_160'] = {'inputs': ['fsp_replacement_155'], 'func': fsp_replacement_d2_160}


def fsp_replacement_d2_161(fsp_replacement_156):
    feature = _clean(fsp_replacement_156)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_161'] = {'inputs': ['fsp_replacement_156'], 'func': fsp_replacement_d2_161}


def fsp_replacement_d2_162(fsp_replacement_157):
    feature = _clean(fsp_replacement_157)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_162'] = {'inputs': ['fsp_replacement_157'], 'func': fsp_replacement_d2_162}


def fsp_replacement_d2_163(fsp_replacement_158):
    feature = _clean(fsp_replacement_158)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_163'] = {'inputs': ['fsp_replacement_158'], 'func': fsp_replacement_d2_163}


def fsp_replacement_d2_164(fsp_replacement_159):
    feature = _clean(fsp_replacement_159)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_164'] = {'inputs': ['fsp_replacement_159'], 'func': fsp_replacement_d2_164}


def fsp_replacement_d2_165(fsp_replacement_160):
    feature = _clean(fsp_replacement_160)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_165'] = {'inputs': ['fsp_replacement_160'], 'func': fsp_replacement_d2_165}


def fsp_replacement_d2_166(fsp_replacement_161):
    feature = _clean(fsp_replacement_161)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_166'] = {'inputs': ['fsp_replacement_161'], 'func': fsp_replacement_d2_166}


def fsp_replacement_d2_167(fsp_replacement_162):
    feature = _clean(fsp_replacement_162)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_167'] = {'inputs': ['fsp_replacement_162'], 'func': fsp_replacement_d2_167}


def fsp_replacement_d2_168(fsp_replacement_163):
    feature = _clean(fsp_replacement_163)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_168'] = {'inputs': ['fsp_replacement_163'], 'func': fsp_replacement_d2_168}


def fsp_replacement_d2_169(fsp_replacement_164):
    feature = _clean(fsp_replacement_164)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_169'] = {'inputs': ['fsp_replacement_164'], 'func': fsp_replacement_d2_169}


def fsp_replacement_d2_170(fsp_replacement_165):
    feature = _clean(fsp_replacement_165)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
FSP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fsp_replacement_d2_170'] = {'inputs': ['fsp_replacement_165'], 'func': fsp_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63(fsp_003_top_holder_concentration_63):
    return _base_universe_d2(fsp_003_top_holder_concentration_63, 1)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63'] = {'inputs': ['fsp_003_top_holder_concentration_63'], 'func': fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63}


def fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84(fsp_004_institutional_net_flow_84):
    return _base_universe_d2(fsp_004_institutional_net_flow_84, 2)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84'] = {'inputs': ['fsp_004_institutional_net_flow_84'], 'func': fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84}


def fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126(fsp_005_forced_selling_pressure_126):
    return _base_universe_d2(fsp_005_forced_selling_pressure_126, 3)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126'] = {'inputs': ['fsp_005_forced_selling_pressure_126'], 'func': fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126}


def fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189(fsp_006_holder_base_volatility_189):
    return _base_universe_d2(fsp_006_holder_base_volatility_189, 4)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189'] = {'inputs': ['fsp_006_holder_base_volatility_189'], 'func': fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189}


def fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504(fsp_009_top_holder_concentration_504):
    return _base_universe_d2(fsp_009_top_holder_concentration_504, 5)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504'] = {'inputs': ['fsp_009_top_holder_concentration_504'], 'func': fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504}


def fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756(fsp_010_institutional_net_flow_756):
    return _base_universe_d2(fsp_010_institutional_net_flow_756, 6)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756'] = {'inputs': ['fsp_010_institutional_net_flow_756'], 'func': fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756}


def fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008(fsp_011_forced_selling_pressure_1008):
    return _base_universe_d2(fsp_011_forced_selling_pressure_1008, 7)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008'] = {'inputs': ['fsp_011_forced_selling_pressure_1008'], 'func': fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008}


def fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260(fsp_012_holder_base_volatility_1260):
    return _base_universe_d2(fsp_012_holder_base_volatility_1260, 8)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260'] = {'inputs': ['fsp_012_holder_base_volatility_1260'], 'func': fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260}


def fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252(fsp_015_top_holder_concentration_252):
    return _base_universe_d2(fsp_015_top_holder_concentration_252, 9)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252'] = {'inputs': ['fsp_015_top_holder_concentration_252'], 'func': fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252}


def fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21(fsp_016_institutional_net_flow_21):
    return _base_universe_d2(fsp_016_institutional_net_flow_21, 10)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21'] = {'inputs': ['fsp_016_institutional_net_flow_21'], 'func': fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21}


def fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42(fsp_017_forced_selling_pressure_42):
    return _base_universe_d2(fsp_017_forced_selling_pressure_42, 11)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42'] = {'inputs': ['fsp_017_forced_selling_pressure_42'], 'func': fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42}


def fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63(fsp_018_holder_base_volatility_63):
    return _base_universe_d2(fsp_018_holder_base_volatility_63, 12)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63'] = {'inputs': ['fsp_018_holder_base_volatility_63'], 'func': fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63}


def fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189(fsp_021_top_holder_concentration_189):
    return _base_universe_d2(fsp_021_top_holder_concentration_189, 13)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189'] = {'inputs': ['fsp_021_top_holder_concentration_189'], 'func': fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189}


def fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252(fsp_022_institutional_net_flow_252):
    return _base_universe_d2(fsp_022_institutional_net_flow_252, 14)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252'] = {'inputs': ['fsp_022_institutional_net_flow_252'], 'func': fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252}


def fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378(fsp_023_forced_selling_pressure_378):
    return _base_universe_d2(fsp_023_forced_selling_pressure_378, 15)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378'] = {'inputs': ['fsp_023_forced_selling_pressure_378'], 'func': fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378}


def fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504(fsp_024_holder_base_volatility_504):
    return _base_universe_d2(fsp_024_holder_base_volatility_504, 16)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504'] = {'inputs': ['fsp_024_holder_base_volatility_504'], 'func': fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504}


def fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260(fsp_027_top_holder_concentration_1260):
    return _base_universe_d2(fsp_027_top_holder_concentration_1260, 17)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260'] = {'inputs': ['fsp_027_top_holder_concentration_1260'], 'func': fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260}


def fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512(fsp_028_institutional_net_flow_1512):
    return _base_universe_d2(fsp_028_institutional_net_flow_1512, 18)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512'] = {'inputs': ['fsp_028_institutional_net_flow_1512'], 'func': fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512}


def fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63(fsp_029_forced_selling_pressure_63):
    return _base_universe_d2(fsp_029_forced_selling_pressure_63, 19)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63'] = {'inputs': ['fsp_029_forced_selling_pressure_63'], 'func': fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63}


def fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252(fsp_030_holder_base_volatility_252):
    return _base_universe_d2(fsp_030_holder_base_volatility_252, 20)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252'] = {'inputs': ['fsp_030_holder_base_volatility_252'], 'func': fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252}


def fsp_base_universe_d2_021_fsp_basefill_001(fsp_basefill_001):
    return _base_universe_d2(fsp_basefill_001, 21)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_021_fsp_basefill_001'] = {'inputs': ['fsp_basefill_001'], 'func': fsp_base_universe_d2_021_fsp_basefill_001}


def fsp_base_universe_d2_022_fsp_basefill_002(fsp_basefill_002):
    return _base_universe_d2(fsp_basefill_002, 22)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_022_fsp_basefill_002'] = {'inputs': ['fsp_basefill_002'], 'func': fsp_base_universe_d2_022_fsp_basefill_002}


def fsp_base_universe_d2_023_fsp_basefill_007(fsp_basefill_007):
    return _base_universe_d2(fsp_basefill_007, 23)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_023_fsp_basefill_007'] = {'inputs': ['fsp_basefill_007'], 'func': fsp_base_universe_d2_023_fsp_basefill_007}


def fsp_base_universe_d2_024_fsp_basefill_008(fsp_basefill_008):
    return _base_universe_d2(fsp_basefill_008, 24)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_024_fsp_basefill_008'] = {'inputs': ['fsp_basefill_008'], 'func': fsp_base_universe_d2_024_fsp_basefill_008}


def fsp_base_universe_d2_025_fsp_basefill_013(fsp_basefill_013):
    return _base_universe_d2(fsp_basefill_013, 25)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_025_fsp_basefill_013'] = {'inputs': ['fsp_basefill_013'], 'func': fsp_base_universe_d2_025_fsp_basefill_013}


def fsp_base_universe_d2_026_fsp_basefill_014(fsp_basefill_014):
    return _base_universe_d2(fsp_basefill_014, 26)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_026_fsp_basefill_014'] = {'inputs': ['fsp_basefill_014'], 'func': fsp_base_universe_d2_026_fsp_basefill_014}


def fsp_base_universe_d2_027_fsp_basefill_019(fsp_basefill_019):
    return _base_universe_d2(fsp_basefill_019, 27)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_027_fsp_basefill_019'] = {'inputs': ['fsp_basefill_019'], 'func': fsp_base_universe_d2_027_fsp_basefill_019}


def fsp_base_universe_d2_028_fsp_basefill_020(fsp_basefill_020):
    return _base_universe_d2(fsp_basefill_020, 28)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_028_fsp_basefill_020'] = {'inputs': ['fsp_basefill_020'], 'func': fsp_base_universe_d2_028_fsp_basefill_020}


def fsp_base_universe_d2_029_fsp_basefill_025(fsp_basefill_025):
    return _base_universe_d2(fsp_basefill_025, 29)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_029_fsp_basefill_025'] = {'inputs': ['fsp_basefill_025'], 'func': fsp_base_universe_d2_029_fsp_basefill_025}


def fsp_base_universe_d2_030_fsp_basefill_026(fsp_basefill_026):
    return _base_universe_d2(fsp_basefill_026, 30)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_030_fsp_basefill_026'] = {'inputs': ['fsp_basefill_026'], 'func': fsp_base_universe_d2_030_fsp_basefill_026}


def fsp_base_universe_d2_031_fsp_basefill_031(fsp_basefill_031):
    return _base_universe_d2(fsp_basefill_031, 31)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_031_fsp_basefill_031'] = {'inputs': ['fsp_basefill_031'], 'func': fsp_base_universe_d2_031_fsp_basefill_031}


def fsp_base_universe_d2_032_fsp_basefill_032(fsp_basefill_032):
    return _base_universe_d2(fsp_basefill_032, 32)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_032_fsp_basefill_032'] = {'inputs': ['fsp_basefill_032'], 'func': fsp_base_universe_d2_032_fsp_basefill_032}


def fsp_base_universe_d2_033_fsp_basefill_033(fsp_basefill_033):
    return _base_universe_d2(fsp_basefill_033, 33)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_033_fsp_basefill_033'] = {'inputs': ['fsp_basefill_033'], 'func': fsp_base_universe_d2_033_fsp_basefill_033}


def fsp_base_universe_d2_034_fsp_basefill_034(fsp_basefill_034):
    return _base_universe_d2(fsp_basefill_034, 34)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_034_fsp_basefill_034'] = {'inputs': ['fsp_basefill_034'], 'func': fsp_base_universe_d2_034_fsp_basefill_034}


def fsp_base_universe_d2_035_fsp_basefill_035(fsp_basefill_035):
    return _base_universe_d2(fsp_basefill_035, 35)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_035_fsp_basefill_035'] = {'inputs': ['fsp_basefill_035'], 'func': fsp_base_universe_d2_035_fsp_basefill_035}


def fsp_base_universe_d2_036_fsp_basefill_036(fsp_basefill_036):
    return _base_universe_d2(fsp_basefill_036, 36)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_036_fsp_basefill_036'] = {'inputs': ['fsp_basefill_036'], 'func': fsp_base_universe_d2_036_fsp_basefill_036}


def fsp_base_universe_d2_037_fsp_basefill_037(fsp_basefill_037):
    return _base_universe_d2(fsp_basefill_037, 37)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_037_fsp_basefill_037'] = {'inputs': ['fsp_basefill_037'], 'func': fsp_base_universe_d2_037_fsp_basefill_037}


def fsp_base_universe_d2_038_fsp_basefill_038(fsp_basefill_038):
    return _base_universe_d2(fsp_basefill_038, 38)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_038_fsp_basefill_038'] = {'inputs': ['fsp_basefill_038'], 'func': fsp_base_universe_d2_038_fsp_basefill_038}


def fsp_base_universe_d2_039_fsp_basefill_039(fsp_basefill_039):
    return _base_universe_d2(fsp_basefill_039, 39)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_039_fsp_basefill_039'] = {'inputs': ['fsp_basefill_039'], 'func': fsp_base_universe_d2_039_fsp_basefill_039}


def fsp_base_universe_d2_040_fsp_basefill_040(fsp_basefill_040):
    return _base_universe_d2(fsp_basefill_040, 40)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_040_fsp_basefill_040'] = {'inputs': ['fsp_basefill_040'], 'func': fsp_base_universe_d2_040_fsp_basefill_040}


def fsp_base_universe_d2_041_fsp_basefill_041(fsp_basefill_041):
    return _base_universe_d2(fsp_basefill_041, 41)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_041_fsp_basefill_041'] = {'inputs': ['fsp_basefill_041'], 'func': fsp_base_universe_d2_041_fsp_basefill_041}


def fsp_base_universe_d2_042_fsp_basefill_042(fsp_basefill_042):
    return _base_universe_d2(fsp_basefill_042, 42)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_042_fsp_basefill_042'] = {'inputs': ['fsp_basefill_042'], 'func': fsp_base_universe_d2_042_fsp_basefill_042}


def fsp_base_universe_d2_043_fsp_basefill_043(fsp_basefill_043):
    return _base_universe_d2(fsp_basefill_043, 43)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_043_fsp_basefill_043'] = {'inputs': ['fsp_basefill_043'], 'func': fsp_base_universe_d2_043_fsp_basefill_043}


def fsp_base_universe_d2_044_fsp_basefill_044(fsp_basefill_044):
    return _base_universe_d2(fsp_basefill_044, 44)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_044_fsp_basefill_044'] = {'inputs': ['fsp_basefill_044'], 'func': fsp_base_universe_d2_044_fsp_basefill_044}


def fsp_base_universe_d2_045_fsp_basefill_045(fsp_basefill_045):
    return _base_universe_d2(fsp_basefill_045, 45)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_045_fsp_basefill_045'] = {'inputs': ['fsp_basefill_045'], 'func': fsp_base_universe_d2_045_fsp_basefill_045}


def fsp_base_universe_d2_046_fsp_basefill_046(fsp_basefill_046):
    return _base_universe_d2(fsp_basefill_046, 46)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_046_fsp_basefill_046'] = {'inputs': ['fsp_basefill_046'], 'func': fsp_base_universe_d2_046_fsp_basefill_046}


def fsp_base_universe_d2_047_fsp_basefill_047(fsp_basefill_047):
    return _base_universe_d2(fsp_basefill_047, 47)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_047_fsp_basefill_047'] = {'inputs': ['fsp_basefill_047'], 'func': fsp_base_universe_d2_047_fsp_basefill_047}


def fsp_base_universe_d2_048_fsp_basefill_048(fsp_basefill_048):
    return _base_universe_d2(fsp_basefill_048, 48)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_048_fsp_basefill_048'] = {'inputs': ['fsp_basefill_048'], 'func': fsp_base_universe_d2_048_fsp_basefill_048}


def fsp_base_universe_d2_049_fsp_basefill_049(fsp_basefill_049):
    return _base_universe_d2(fsp_basefill_049, 49)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_049_fsp_basefill_049'] = {'inputs': ['fsp_basefill_049'], 'func': fsp_base_universe_d2_049_fsp_basefill_049}


def fsp_base_universe_d2_050_fsp_basefill_050(fsp_basefill_050):
    return _base_universe_d2(fsp_basefill_050, 50)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_050_fsp_basefill_050'] = {'inputs': ['fsp_basefill_050'], 'func': fsp_base_universe_d2_050_fsp_basefill_050}


def fsp_base_universe_d2_051_fsp_basefill_051(fsp_basefill_051):
    return _base_universe_d2(fsp_basefill_051, 51)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_051_fsp_basefill_051'] = {'inputs': ['fsp_basefill_051'], 'func': fsp_base_universe_d2_051_fsp_basefill_051}


def fsp_base_universe_d2_052_fsp_basefill_052(fsp_basefill_052):
    return _base_universe_d2(fsp_basefill_052, 52)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_052_fsp_basefill_052'] = {'inputs': ['fsp_basefill_052'], 'func': fsp_base_universe_d2_052_fsp_basefill_052}


def fsp_base_universe_d2_053_fsp_basefill_053(fsp_basefill_053):
    return _base_universe_d2(fsp_basefill_053, 53)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_053_fsp_basefill_053'] = {'inputs': ['fsp_basefill_053'], 'func': fsp_base_universe_d2_053_fsp_basefill_053}


def fsp_base_universe_d2_054_fsp_basefill_054(fsp_basefill_054):
    return _base_universe_d2(fsp_basefill_054, 54)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_054_fsp_basefill_054'] = {'inputs': ['fsp_basefill_054'], 'func': fsp_base_universe_d2_054_fsp_basefill_054}


def fsp_base_universe_d2_055_fsp_basefill_055(fsp_basefill_055):
    return _base_universe_d2(fsp_basefill_055, 55)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_055_fsp_basefill_055'] = {'inputs': ['fsp_basefill_055'], 'func': fsp_base_universe_d2_055_fsp_basefill_055}


def fsp_base_universe_d2_056_fsp_basefill_056(fsp_basefill_056):
    return _base_universe_d2(fsp_basefill_056, 56)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_056_fsp_basefill_056'] = {'inputs': ['fsp_basefill_056'], 'func': fsp_base_universe_d2_056_fsp_basefill_056}


def fsp_base_universe_d2_057_fsp_basefill_057(fsp_basefill_057):
    return _base_universe_d2(fsp_basefill_057, 57)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_057_fsp_basefill_057'] = {'inputs': ['fsp_basefill_057'], 'func': fsp_base_universe_d2_057_fsp_basefill_057}


def fsp_base_universe_d2_058_fsp_basefill_058(fsp_basefill_058):
    return _base_universe_d2(fsp_basefill_058, 58)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_058_fsp_basefill_058'] = {'inputs': ['fsp_basefill_058'], 'func': fsp_base_universe_d2_058_fsp_basefill_058}


def fsp_base_universe_d2_059_fsp_basefill_059(fsp_basefill_059):
    return _base_universe_d2(fsp_basefill_059, 59)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_059_fsp_basefill_059'] = {'inputs': ['fsp_basefill_059'], 'func': fsp_base_universe_d2_059_fsp_basefill_059}


def fsp_base_universe_d2_060_fsp_basefill_060(fsp_basefill_060):
    return _base_universe_d2(fsp_basefill_060, 60)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_060_fsp_basefill_060'] = {'inputs': ['fsp_basefill_060'], 'func': fsp_base_universe_d2_060_fsp_basefill_060}


def fsp_base_universe_d2_061_fsp_basefill_061(fsp_basefill_061):
    return _base_universe_d2(fsp_basefill_061, 61)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_061_fsp_basefill_061'] = {'inputs': ['fsp_basefill_061'], 'func': fsp_base_universe_d2_061_fsp_basefill_061}


def fsp_base_universe_d2_062_fsp_basefill_062(fsp_basefill_062):
    return _base_universe_d2(fsp_basefill_062, 62)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_062_fsp_basefill_062'] = {'inputs': ['fsp_basefill_062'], 'func': fsp_base_universe_d2_062_fsp_basefill_062}


def fsp_base_universe_d2_063_fsp_basefill_063(fsp_basefill_063):
    return _base_universe_d2(fsp_basefill_063, 63)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_063_fsp_basefill_063'] = {'inputs': ['fsp_basefill_063'], 'func': fsp_base_universe_d2_063_fsp_basefill_063}


def fsp_base_universe_d2_064_fsp_basefill_064(fsp_basefill_064):
    return _base_universe_d2(fsp_basefill_064, 64)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_064_fsp_basefill_064'] = {'inputs': ['fsp_basefill_064'], 'func': fsp_base_universe_d2_064_fsp_basefill_064}


def fsp_base_universe_d2_065_fsp_basefill_065(fsp_basefill_065):
    return _base_universe_d2(fsp_basefill_065, 65)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_065_fsp_basefill_065'] = {'inputs': ['fsp_basefill_065'], 'func': fsp_base_universe_d2_065_fsp_basefill_065}


def fsp_base_universe_d2_066_fsp_basefill_066(fsp_basefill_066):
    return _base_universe_d2(fsp_basefill_066, 66)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_066_fsp_basefill_066'] = {'inputs': ['fsp_basefill_066'], 'func': fsp_base_universe_d2_066_fsp_basefill_066}


def fsp_base_universe_d2_067_fsp_basefill_067(fsp_basefill_067):
    return _base_universe_d2(fsp_basefill_067, 67)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_067_fsp_basefill_067'] = {'inputs': ['fsp_basefill_067'], 'func': fsp_base_universe_d2_067_fsp_basefill_067}


def fsp_base_universe_d2_068_fsp_basefill_068(fsp_basefill_068):
    return _base_universe_d2(fsp_basefill_068, 68)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_068_fsp_basefill_068'] = {'inputs': ['fsp_basefill_068'], 'func': fsp_base_universe_d2_068_fsp_basefill_068}


def fsp_base_universe_d2_069_fsp_basefill_069(fsp_basefill_069):
    return _base_universe_d2(fsp_basefill_069, 69)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_069_fsp_basefill_069'] = {'inputs': ['fsp_basefill_069'], 'func': fsp_base_universe_d2_069_fsp_basefill_069}


def fsp_base_universe_d2_070_fsp_basefill_070(fsp_basefill_070):
    return _base_universe_d2(fsp_basefill_070, 70)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_070_fsp_basefill_070'] = {'inputs': ['fsp_basefill_070'], 'func': fsp_base_universe_d2_070_fsp_basefill_070}


def fsp_base_universe_d2_071_fsp_basefill_071(fsp_basefill_071):
    return _base_universe_d2(fsp_basefill_071, 71)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_071_fsp_basefill_071'] = {'inputs': ['fsp_basefill_071'], 'func': fsp_base_universe_d2_071_fsp_basefill_071}


def fsp_base_universe_d2_072_fsp_basefill_072(fsp_basefill_072):
    return _base_universe_d2(fsp_basefill_072, 72)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_072_fsp_basefill_072'] = {'inputs': ['fsp_basefill_072'], 'func': fsp_base_universe_d2_072_fsp_basefill_072}


def fsp_base_universe_d2_073_fsp_basefill_073(fsp_basefill_073):
    return _base_universe_d2(fsp_basefill_073, 73)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_073_fsp_basefill_073'] = {'inputs': ['fsp_basefill_073'], 'func': fsp_base_universe_d2_073_fsp_basefill_073}


def fsp_base_universe_d2_074_fsp_basefill_074(fsp_basefill_074):
    return _base_universe_d2(fsp_basefill_074, 74)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_074_fsp_basefill_074'] = {'inputs': ['fsp_basefill_074'], 'func': fsp_base_universe_d2_074_fsp_basefill_074}


def fsp_base_universe_d2_075_fsp_basefill_075(fsp_basefill_075):
    return _base_universe_d2(fsp_basefill_075, 75)
FSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fsp_base_universe_d2_075_fsp_basefill_075'] = {'inputs': ['fsp_basefill_075'], 'func': fsp_base_universe_d2_075_fsp_basefill_075}
