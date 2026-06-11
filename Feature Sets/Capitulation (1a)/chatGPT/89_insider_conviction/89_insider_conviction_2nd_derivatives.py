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



def icn_151_icn_001_insider_buy_cluster_21_roc_1(icn_001_insider_buy_cluster_21):
    feature = _s(icn_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def icn_152_icn_007_insider_silence_252_roc_42(icn_007_insider_silence_252):
    feature = _s(icn_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def icn_153_icn_013_insider_conviction_1512_roc_126(icn_013_insider_conviction_1512):
    feature = _s(icn_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def icn_154_icn_019_insider_activity_accel_1_roc_378(icn_019_insider_activity_accel_1):
    feature = _s(icn_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4(icn_025_ceo_cfo_buy_weight_756):
    feature = _s(icn_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_CONVICTION_REGISTRY_2ND_DERIVATIVES = {
    'icn_151_icn_001_insider_buy_cluster_21_roc_1': {'inputs': ['icn_001_insider_buy_cluster_21'], 'func': icn_151_icn_001_insider_buy_cluster_21_roc_1},
    'icn_152_icn_007_insider_silence_252_roc_42': {'inputs': ['icn_007_insider_silence_252'], 'func': icn_152_icn_007_insider_silence_252_roc_42},
    'icn_153_icn_013_insider_conviction_1512_roc_126': {'inputs': ['icn_013_insider_conviction_1512'], 'func': icn_153_icn_013_insider_conviction_1512_roc_126},
    'icn_154_icn_019_insider_activity_accel_1_roc_378': {'inputs': ['icn_019_insider_activity_accel_1'], 'func': icn_154_icn_019_insider_activity_accel_1_roc_378},
    'icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['icn_025_ceo_cfo_buy_weight_756'], 'func': icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ic_replacement_d2_001(icn_019_insider_activity_accel_1):
    feature = _clean(icn_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_001'] = {'inputs': ['icn_019_insider_activity_accel_1'], 'func': ic_replacement_d2_001}


def ic_replacement_d2_002(ic_replacement_001):
    feature = _clean(ic_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_002'] = {'inputs': ['ic_replacement_001'], 'func': ic_replacement_d2_002}


def ic_replacement_d2_003(ic_replacement_002):
    feature = _clean(ic_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_003'] = {'inputs': ['ic_replacement_002'], 'func': ic_replacement_d2_003}


def ic_replacement_d2_004(ic_replacement_003):
    feature = _clean(ic_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_004'] = {'inputs': ['ic_replacement_003'], 'func': ic_replacement_d2_004}


def ic_replacement_d2_005(ic_replacement_004):
    feature = _clean(ic_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_005'] = {'inputs': ['ic_replacement_004'], 'func': ic_replacement_d2_005}


def ic_replacement_d2_006(ic_replacement_005):
    feature = _clean(ic_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_006'] = {'inputs': ['ic_replacement_005'], 'func': ic_replacement_d2_006}


def ic_replacement_d2_007(ic_replacement_006):
    feature = _clean(ic_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_007'] = {'inputs': ['ic_replacement_006'], 'func': ic_replacement_d2_007}


def ic_replacement_d2_008(ic_replacement_007):
    feature = _clean(ic_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_008'] = {'inputs': ['ic_replacement_007'], 'func': ic_replacement_d2_008}


def ic_replacement_d2_009(ic_replacement_008):
    feature = _clean(ic_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_009'] = {'inputs': ['ic_replacement_008'], 'func': ic_replacement_d2_009}


def ic_replacement_d2_010(ic_replacement_009):
    feature = _clean(ic_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_010'] = {'inputs': ['ic_replacement_009'], 'func': ic_replacement_d2_010}


def ic_replacement_d2_011(ic_replacement_010):
    feature = _clean(ic_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_011'] = {'inputs': ['ic_replacement_010'], 'func': ic_replacement_d2_011}


def ic_replacement_d2_012(ic_replacement_011):
    feature = _clean(ic_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_012'] = {'inputs': ['ic_replacement_011'], 'func': ic_replacement_d2_012}


def ic_replacement_d2_013(ic_replacement_012):
    feature = _clean(ic_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_013'] = {'inputs': ['ic_replacement_012'], 'func': ic_replacement_d2_013}


def ic_replacement_d2_014(ic_replacement_013):
    feature = _clean(ic_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_014'] = {'inputs': ['ic_replacement_013'], 'func': ic_replacement_d2_014}


def ic_replacement_d2_015(ic_replacement_014):
    feature = _clean(ic_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_015'] = {'inputs': ['ic_replacement_014'], 'func': ic_replacement_d2_015}


def ic_replacement_d2_016(ic_replacement_015):
    feature = _clean(ic_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_016'] = {'inputs': ['ic_replacement_015'], 'func': ic_replacement_d2_016}


def ic_replacement_d2_017(ic_replacement_016):
    feature = _clean(ic_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_017'] = {'inputs': ['ic_replacement_016'], 'func': ic_replacement_d2_017}


def ic_replacement_d2_018(ic_replacement_017):
    feature = _clean(ic_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_018'] = {'inputs': ['ic_replacement_017'], 'func': ic_replacement_d2_018}


def ic_replacement_d2_019(ic_replacement_018):
    feature = _clean(ic_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_019'] = {'inputs': ['ic_replacement_018'], 'func': ic_replacement_d2_019}


def ic_replacement_d2_020(ic_replacement_019):
    feature = _clean(ic_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_020'] = {'inputs': ['ic_replacement_019'], 'func': ic_replacement_d2_020}


def ic_replacement_d2_021(ic_replacement_020):
    feature = _clean(ic_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_021'] = {'inputs': ['ic_replacement_020'], 'func': ic_replacement_d2_021}


def ic_replacement_d2_022(ic_replacement_021):
    feature = _clean(ic_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_022'] = {'inputs': ['ic_replacement_021'], 'func': ic_replacement_d2_022}


def ic_replacement_d2_023(ic_replacement_022):
    feature = _clean(ic_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_023'] = {'inputs': ['ic_replacement_022'], 'func': ic_replacement_d2_023}


def ic_replacement_d2_024(ic_replacement_023):
    feature = _clean(ic_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_024'] = {'inputs': ['ic_replacement_023'], 'func': ic_replacement_d2_024}


def ic_replacement_d2_025(ic_replacement_024):
    feature = _clean(ic_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_025'] = {'inputs': ['ic_replacement_024'], 'func': ic_replacement_d2_025}


def ic_replacement_d2_026(ic_replacement_025):
    feature = _clean(ic_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_026'] = {'inputs': ['ic_replacement_025'], 'func': ic_replacement_d2_026}


def ic_replacement_d2_027(ic_replacement_026):
    feature = _clean(ic_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_027'] = {'inputs': ['ic_replacement_026'], 'func': ic_replacement_d2_027}


def ic_replacement_d2_028(ic_replacement_027):
    feature = _clean(ic_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_028'] = {'inputs': ['ic_replacement_027'], 'func': ic_replacement_d2_028}


def ic_replacement_d2_029(ic_replacement_028):
    feature = _clean(ic_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_029'] = {'inputs': ['ic_replacement_028'], 'func': ic_replacement_d2_029}


def ic_replacement_d2_030(ic_replacement_029):
    feature = _clean(ic_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_030'] = {'inputs': ['ic_replacement_029'], 'func': ic_replacement_d2_030}


def ic_replacement_d2_031(ic_replacement_030):
    feature = _clean(ic_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_031'] = {'inputs': ['ic_replacement_030'], 'func': ic_replacement_d2_031}


def ic_replacement_d2_032(ic_replacement_031):
    feature = _clean(ic_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_032'] = {'inputs': ['ic_replacement_031'], 'func': ic_replacement_d2_032}


def ic_replacement_d2_033(ic_replacement_032):
    feature = _clean(ic_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_033'] = {'inputs': ['ic_replacement_032'], 'func': ic_replacement_d2_033}


def ic_replacement_d2_034(ic_replacement_033):
    feature = _clean(ic_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_034'] = {'inputs': ['ic_replacement_033'], 'func': ic_replacement_d2_034}


def ic_replacement_d2_035(ic_replacement_034):
    feature = _clean(ic_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_035'] = {'inputs': ['ic_replacement_034'], 'func': ic_replacement_d2_035}


def ic_replacement_d2_036(ic_replacement_035):
    feature = _clean(ic_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_036'] = {'inputs': ['ic_replacement_035'], 'func': ic_replacement_d2_036}


def ic_replacement_d2_037(ic_replacement_036):
    feature = _clean(ic_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_037'] = {'inputs': ['ic_replacement_036'], 'func': ic_replacement_d2_037}


def ic_replacement_d2_038(ic_replacement_037):
    feature = _clean(ic_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_038'] = {'inputs': ['ic_replacement_037'], 'func': ic_replacement_d2_038}


def ic_replacement_d2_039(ic_replacement_038):
    feature = _clean(ic_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_039'] = {'inputs': ['ic_replacement_038'], 'func': ic_replacement_d2_039}


def ic_replacement_d2_040(ic_replacement_039):
    feature = _clean(ic_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_040'] = {'inputs': ['ic_replacement_039'], 'func': ic_replacement_d2_040}


def ic_replacement_d2_041(ic_replacement_040):
    feature = _clean(ic_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_041'] = {'inputs': ['ic_replacement_040'], 'func': ic_replacement_d2_041}


def ic_replacement_d2_042(ic_replacement_041):
    feature = _clean(ic_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_042'] = {'inputs': ['ic_replacement_041'], 'func': ic_replacement_d2_042}


def ic_replacement_d2_043(ic_replacement_042):
    feature = _clean(ic_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_043'] = {'inputs': ['ic_replacement_042'], 'func': ic_replacement_d2_043}


def ic_replacement_d2_044(ic_replacement_043):
    feature = _clean(ic_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_044'] = {'inputs': ['ic_replacement_043'], 'func': ic_replacement_d2_044}


def ic_replacement_d2_045(ic_replacement_044):
    feature = _clean(ic_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_045'] = {'inputs': ['ic_replacement_044'], 'func': ic_replacement_d2_045}


def ic_replacement_d2_046(ic_replacement_045):
    feature = _clean(ic_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_046'] = {'inputs': ['ic_replacement_045'], 'func': ic_replacement_d2_046}


def ic_replacement_d2_047(ic_replacement_046):
    feature = _clean(ic_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_047'] = {'inputs': ['ic_replacement_046'], 'func': ic_replacement_d2_047}


def ic_replacement_d2_048(ic_replacement_047):
    feature = _clean(ic_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_048'] = {'inputs': ['ic_replacement_047'], 'func': ic_replacement_d2_048}


def ic_replacement_d2_049(ic_replacement_048):
    feature = _clean(ic_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_049'] = {'inputs': ['ic_replacement_048'], 'func': ic_replacement_d2_049}


def ic_replacement_d2_050(ic_replacement_049):
    feature = _clean(ic_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_050'] = {'inputs': ['ic_replacement_049'], 'func': ic_replacement_d2_050}


def ic_replacement_d2_051(ic_replacement_050):
    feature = _clean(ic_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_051'] = {'inputs': ['ic_replacement_050'], 'func': ic_replacement_d2_051}


def ic_replacement_d2_052(ic_replacement_051):
    feature = _clean(ic_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_052'] = {'inputs': ['ic_replacement_051'], 'func': ic_replacement_d2_052}


def ic_replacement_d2_053(ic_replacement_052):
    feature = _clean(ic_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_053'] = {'inputs': ['ic_replacement_052'], 'func': ic_replacement_d2_053}


def ic_replacement_d2_054(ic_replacement_053):
    feature = _clean(ic_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_054'] = {'inputs': ['ic_replacement_053'], 'func': ic_replacement_d2_054}


def ic_replacement_d2_055(ic_replacement_054):
    feature = _clean(ic_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_055'] = {'inputs': ['ic_replacement_054'], 'func': ic_replacement_d2_055}


def ic_replacement_d2_056(ic_replacement_055):
    feature = _clean(ic_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_056'] = {'inputs': ['ic_replacement_055'], 'func': ic_replacement_d2_056}


def ic_replacement_d2_057(ic_replacement_056):
    feature = _clean(ic_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_057'] = {'inputs': ['ic_replacement_056'], 'func': ic_replacement_d2_057}


def ic_replacement_d2_058(ic_replacement_057):
    feature = _clean(ic_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_058'] = {'inputs': ['ic_replacement_057'], 'func': ic_replacement_d2_058}


def ic_replacement_d2_059(ic_replacement_058):
    feature = _clean(ic_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_059'] = {'inputs': ['ic_replacement_058'], 'func': ic_replacement_d2_059}


def ic_replacement_d2_060(ic_replacement_059):
    feature = _clean(ic_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_060'] = {'inputs': ['ic_replacement_059'], 'func': ic_replacement_d2_060}


def ic_replacement_d2_061(ic_replacement_060):
    feature = _clean(ic_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_061'] = {'inputs': ['ic_replacement_060'], 'func': ic_replacement_d2_061}


def ic_replacement_d2_062(ic_replacement_061):
    feature = _clean(ic_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_062'] = {'inputs': ['ic_replacement_061'], 'func': ic_replacement_d2_062}


def ic_replacement_d2_063(ic_replacement_062):
    feature = _clean(ic_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_063'] = {'inputs': ['ic_replacement_062'], 'func': ic_replacement_d2_063}


def ic_replacement_d2_064(ic_replacement_063):
    feature = _clean(ic_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_064'] = {'inputs': ['ic_replacement_063'], 'func': ic_replacement_d2_064}


def ic_replacement_d2_065(ic_replacement_064):
    feature = _clean(ic_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_065'] = {'inputs': ['ic_replacement_064'], 'func': ic_replacement_d2_065}


def ic_replacement_d2_066(ic_replacement_065):
    feature = _clean(ic_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_066'] = {'inputs': ['ic_replacement_065'], 'func': ic_replacement_d2_066}


def ic_replacement_d2_067(ic_replacement_066):
    feature = _clean(ic_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_067'] = {'inputs': ['ic_replacement_066'], 'func': ic_replacement_d2_067}


def ic_replacement_d2_068(ic_replacement_067):
    feature = _clean(ic_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_068'] = {'inputs': ['ic_replacement_067'], 'func': ic_replacement_d2_068}


def ic_replacement_d2_069(ic_replacement_068):
    feature = _clean(ic_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_069'] = {'inputs': ['ic_replacement_068'], 'func': ic_replacement_d2_069}


def ic_replacement_d2_070(ic_replacement_069):
    feature = _clean(ic_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_070'] = {'inputs': ['ic_replacement_069'], 'func': ic_replacement_d2_070}


def ic_replacement_d2_071(ic_replacement_070):
    feature = _clean(ic_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_071'] = {'inputs': ['ic_replacement_070'], 'func': ic_replacement_d2_071}


def ic_replacement_d2_072(ic_replacement_071):
    feature = _clean(ic_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_072'] = {'inputs': ['ic_replacement_071'], 'func': ic_replacement_d2_072}


def ic_replacement_d2_073(ic_replacement_072):
    feature = _clean(ic_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_073'] = {'inputs': ['ic_replacement_072'], 'func': ic_replacement_d2_073}


def ic_replacement_d2_074(ic_replacement_073):
    feature = _clean(ic_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_074'] = {'inputs': ['ic_replacement_073'], 'func': ic_replacement_d2_074}


def ic_replacement_d2_075(ic_replacement_074):
    feature = _clean(ic_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_075'] = {'inputs': ['ic_replacement_074'], 'func': ic_replacement_d2_075}


def ic_replacement_d2_076(ic_replacement_075):
    feature = _clean(ic_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_076'] = {'inputs': ['ic_replacement_075'], 'func': ic_replacement_d2_076}


def ic_replacement_d2_077(ic_replacement_076):
    feature = _clean(ic_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_077'] = {'inputs': ['ic_replacement_076'], 'func': ic_replacement_d2_077}


def ic_replacement_d2_078(ic_replacement_077):
    feature = _clean(ic_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_078'] = {'inputs': ['ic_replacement_077'], 'func': ic_replacement_d2_078}


def ic_replacement_d2_079(ic_replacement_078):
    feature = _clean(ic_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_079'] = {'inputs': ['ic_replacement_078'], 'func': ic_replacement_d2_079}


def ic_replacement_d2_080(ic_replacement_079):
    feature = _clean(ic_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_080'] = {'inputs': ['ic_replacement_079'], 'func': ic_replacement_d2_080}


def ic_replacement_d2_081(ic_replacement_080):
    feature = _clean(ic_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_081'] = {'inputs': ['ic_replacement_080'], 'func': ic_replacement_d2_081}


def ic_replacement_d2_082(ic_replacement_081):
    feature = _clean(ic_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_082'] = {'inputs': ['ic_replacement_081'], 'func': ic_replacement_d2_082}


def ic_replacement_d2_083(ic_replacement_082):
    feature = _clean(ic_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_083'] = {'inputs': ['ic_replacement_082'], 'func': ic_replacement_d2_083}


def ic_replacement_d2_084(ic_replacement_083):
    feature = _clean(ic_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_084'] = {'inputs': ['ic_replacement_083'], 'func': ic_replacement_d2_084}


def ic_replacement_d2_085(ic_replacement_084):
    feature = _clean(ic_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_085'] = {'inputs': ['ic_replacement_084'], 'func': ic_replacement_d2_085}


def ic_replacement_d2_086(ic_replacement_085):
    feature = _clean(ic_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_086'] = {'inputs': ['ic_replacement_085'], 'func': ic_replacement_d2_086}


def ic_replacement_d2_087(ic_replacement_086):
    feature = _clean(ic_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_087'] = {'inputs': ['ic_replacement_086'], 'func': ic_replacement_d2_087}


def ic_replacement_d2_088(ic_replacement_087):
    feature = _clean(ic_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_088'] = {'inputs': ['ic_replacement_087'], 'func': ic_replacement_d2_088}


def ic_replacement_d2_089(ic_replacement_088):
    feature = _clean(ic_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_089'] = {'inputs': ['ic_replacement_088'], 'func': ic_replacement_d2_089}


def ic_replacement_d2_090(ic_replacement_089):
    feature = _clean(ic_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_090'] = {'inputs': ['ic_replacement_089'], 'func': ic_replacement_d2_090}


def ic_replacement_d2_091(ic_replacement_090):
    feature = _clean(ic_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_091'] = {'inputs': ['ic_replacement_090'], 'func': ic_replacement_d2_091}


def ic_replacement_d2_092(ic_replacement_091):
    feature = _clean(ic_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_092'] = {'inputs': ['ic_replacement_091'], 'func': ic_replacement_d2_092}


def ic_replacement_d2_093(ic_replacement_092):
    feature = _clean(ic_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_093'] = {'inputs': ['ic_replacement_092'], 'func': ic_replacement_d2_093}


def ic_replacement_d2_094(ic_replacement_093):
    feature = _clean(ic_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_094'] = {'inputs': ['ic_replacement_093'], 'func': ic_replacement_d2_094}


def ic_replacement_d2_095(ic_replacement_094):
    feature = _clean(ic_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_095'] = {'inputs': ['ic_replacement_094'], 'func': ic_replacement_d2_095}


def ic_replacement_d2_096(ic_replacement_095):
    feature = _clean(ic_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_096'] = {'inputs': ['ic_replacement_095'], 'func': ic_replacement_d2_096}


def ic_replacement_d2_097(ic_replacement_096):
    feature = _clean(ic_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_097'] = {'inputs': ['ic_replacement_096'], 'func': ic_replacement_d2_097}


def ic_replacement_d2_098(ic_replacement_097):
    feature = _clean(ic_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_098'] = {'inputs': ['ic_replacement_097'], 'func': ic_replacement_d2_098}


def ic_replacement_d2_099(ic_replacement_098):
    feature = _clean(ic_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_099'] = {'inputs': ['ic_replacement_098'], 'func': ic_replacement_d2_099}


def ic_replacement_d2_100(ic_replacement_099):
    feature = _clean(ic_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_100'] = {'inputs': ['ic_replacement_099'], 'func': ic_replacement_d2_100}


def ic_replacement_d2_101(ic_replacement_100):
    feature = _clean(ic_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_101'] = {'inputs': ['ic_replacement_100'], 'func': ic_replacement_d2_101}


def ic_replacement_d2_102(ic_replacement_101):
    feature = _clean(ic_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_102'] = {'inputs': ['ic_replacement_101'], 'func': ic_replacement_d2_102}


def ic_replacement_d2_103(ic_replacement_102):
    feature = _clean(ic_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_103'] = {'inputs': ['ic_replacement_102'], 'func': ic_replacement_d2_103}


def ic_replacement_d2_104(ic_replacement_103):
    feature = _clean(ic_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_104'] = {'inputs': ['ic_replacement_103'], 'func': ic_replacement_d2_104}


def ic_replacement_d2_105(ic_replacement_104):
    feature = _clean(ic_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_105'] = {'inputs': ['ic_replacement_104'], 'func': ic_replacement_d2_105}


def ic_replacement_d2_106(ic_replacement_105):
    feature = _clean(ic_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_106'] = {'inputs': ['ic_replacement_105'], 'func': ic_replacement_d2_106}


def ic_replacement_d2_107(ic_replacement_106):
    feature = _clean(ic_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_107'] = {'inputs': ['ic_replacement_106'], 'func': ic_replacement_d2_107}


def ic_replacement_d2_108(ic_replacement_107):
    feature = _clean(ic_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_108'] = {'inputs': ['ic_replacement_107'], 'func': ic_replacement_d2_108}


def ic_replacement_d2_109(ic_replacement_108):
    feature = _clean(ic_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_109'] = {'inputs': ['ic_replacement_108'], 'func': ic_replacement_d2_109}


def ic_replacement_d2_110(ic_replacement_109):
    feature = _clean(ic_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_110'] = {'inputs': ['ic_replacement_109'], 'func': ic_replacement_d2_110}


def ic_replacement_d2_111(ic_replacement_110):
    feature = _clean(ic_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_111'] = {'inputs': ['ic_replacement_110'], 'func': ic_replacement_d2_111}


def ic_replacement_d2_112(ic_replacement_111):
    feature = _clean(ic_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_112'] = {'inputs': ['ic_replacement_111'], 'func': ic_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42(icn_002_insider_net_buy_ratio_42):
    return _base_universe_d2(icn_002_insider_net_buy_ratio_42, 1)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42'] = {'inputs': ['icn_002_insider_net_buy_ratio_42'], 'func': icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42}


def icn_base_universe_d2_002_icn_003_insider_value_ratio_63(icn_003_insider_value_ratio_63):
    return _base_universe_d2(icn_003_insider_value_ratio_63, 2)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_002_icn_003_insider_value_ratio_63'] = {'inputs': ['icn_003_insider_value_ratio_63'], 'func': icn_base_universe_d2_002_icn_003_insider_value_ratio_63}


def icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84(icn_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(icn_004_ceo_cfo_buy_weight_84, 3)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84'] = {'inputs': ['icn_004_ceo_cfo_buy_weight_84'], 'func': icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84}


def icn_base_universe_d2_004_icn_006_insider_conviction_189(icn_006_insider_conviction_189):
    return _base_universe_d2(icn_006_insider_conviction_189, 4)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_004_icn_006_insider_conviction_189'] = {'inputs': ['icn_006_insider_conviction_189'], 'func': icn_base_universe_d2_004_icn_006_insider_conviction_189}


def icn_base_universe_d2_005_icn_008_insider_buy_cluster_378(icn_008_insider_buy_cluster_378):
    return _base_universe_d2(icn_008_insider_buy_cluster_378, 5)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_005_icn_008_insider_buy_cluster_378'] = {'inputs': ['icn_008_insider_buy_cluster_378'], 'func': icn_base_universe_d2_005_icn_008_insider_buy_cluster_378}


def icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504(icn_009_insider_net_buy_ratio_504):
    return _base_universe_d2(icn_009_insider_net_buy_ratio_504, 6)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504'] = {'inputs': ['icn_009_insider_net_buy_ratio_504'], 'func': icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504}


def icn_base_universe_d2_007_icn_010_insider_value_ratio_756(icn_010_insider_value_ratio_756):
    return _base_universe_d2(icn_010_insider_value_ratio_756, 7)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_007_icn_010_insider_value_ratio_756'] = {'inputs': ['icn_010_insider_value_ratio_756'], 'func': icn_base_universe_d2_007_icn_010_insider_value_ratio_756}


def icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008(icn_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(icn_011_ceo_cfo_buy_weight_1008, 8)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['icn_011_ceo_cfo_buy_weight_1008'], 'func': icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008}


def icn_base_universe_d2_009_icn_014_insider_silence_63(icn_014_insider_silence_63):
    return _base_universe_d2(icn_014_insider_silence_63, 9)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_009_icn_014_insider_silence_63'] = {'inputs': ['icn_014_insider_silence_63'], 'func': icn_base_universe_d2_009_icn_014_insider_silence_63}


def icn_base_universe_d2_010_icn_015_insider_buy_cluster_252(icn_015_insider_buy_cluster_252):
    return _base_universe_d2(icn_015_insider_buy_cluster_252, 10)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_010_icn_015_insider_buy_cluster_252'] = {'inputs': ['icn_015_insider_buy_cluster_252'], 'func': icn_base_universe_d2_010_icn_015_insider_buy_cluster_252}


def icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21(icn_016_insider_net_buy_ratio_21):
    return _base_universe_d2(icn_016_insider_net_buy_ratio_21, 11)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21'] = {'inputs': ['icn_016_insider_net_buy_ratio_21'], 'func': icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21}


def icn_base_universe_d2_012_icn_017_insider_value_ratio_42(icn_017_insider_value_ratio_42):
    return _base_universe_d2(icn_017_insider_value_ratio_42, 12)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_012_icn_017_insider_value_ratio_42'] = {'inputs': ['icn_017_insider_value_ratio_42'], 'func': icn_base_universe_d2_012_icn_017_insider_value_ratio_42}


def icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63(icn_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(icn_018_ceo_cfo_buy_weight_63, 13)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63'] = {'inputs': ['icn_018_ceo_cfo_buy_weight_63'], 'func': icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63}


def icn_base_universe_d2_014_icn_020_insider_conviction_126(icn_020_insider_conviction_126):
    return _base_universe_d2(icn_020_insider_conviction_126, 14)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_014_icn_020_insider_conviction_126'] = {'inputs': ['icn_020_insider_conviction_126'], 'func': icn_base_universe_d2_014_icn_020_insider_conviction_126}


def icn_base_universe_d2_015_icn_021_insider_silence_189(icn_021_insider_silence_189):
    return _base_universe_d2(icn_021_insider_silence_189, 15)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_015_icn_021_insider_silence_189'] = {'inputs': ['icn_021_insider_silence_189'], 'func': icn_base_universe_d2_015_icn_021_insider_silence_189}


def icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378(icn_023_insider_net_buy_ratio_378):
    return _base_universe_d2(icn_023_insider_net_buy_ratio_378, 16)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378'] = {'inputs': ['icn_023_insider_net_buy_ratio_378'], 'func': icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378}


def icn_base_universe_d2_017_icn_024_insider_value_ratio_504(icn_024_insider_value_ratio_504):
    return _base_universe_d2(icn_024_insider_value_ratio_504, 17)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_017_icn_024_insider_value_ratio_504'] = {'inputs': ['icn_024_insider_value_ratio_504'], 'func': icn_base_universe_d2_017_icn_024_insider_value_ratio_504}


def icn_base_universe_d2_018_icn_027_insider_conviction_1260(icn_027_insider_conviction_1260):
    return _base_universe_d2(icn_027_insider_conviction_1260, 18)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_018_icn_027_insider_conviction_1260'] = {'inputs': ['icn_027_insider_conviction_1260'], 'func': icn_base_universe_d2_018_icn_027_insider_conviction_1260}


def icn_base_universe_d2_019_icn_028_insider_silence_1512(icn_028_insider_silence_1512):
    return _base_universe_d2(icn_028_insider_silence_1512, 19)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_019_icn_028_insider_silence_1512'] = {'inputs': ['icn_028_insider_silence_1512'], 'func': icn_base_universe_d2_019_icn_028_insider_silence_1512}


def icn_base_universe_d2_020_icn_029_insider_buy_cluster_63(icn_029_insider_buy_cluster_63):
    return _base_universe_d2(icn_029_insider_buy_cluster_63, 20)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_020_icn_029_insider_buy_cluster_63'] = {'inputs': ['icn_029_insider_buy_cluster_63'], 'func': icn_base_universe_d2_020_icn_029_insider_buy_cluster_63}


def icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252(icn_030_insider_net_buy_ratio_252):
    return _base_universe_d2(icn_030_insider_net_buy_ratio_252, 21)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252'] = {'inputs': ['icn_030_insider_net_buy_ratio_252'], 'func': icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252}


def icn_base_universe_d2_022_icn_031_insider_value_ratio_21(icn_031_insider_value_ratio_21):
    return _base_universe_d2(icn_031_insider_value_ratio_21, 22)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_022_icn_031_insider_value_ratio_21'] = {'inputs': ['icn_031_insider_value_ratio_21'], 'func': icn_base_universe_d2_022_icn_031_insider_value_ratio_21}


def icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42(icn_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(icn_032_ceo_cfo_buy_weight_42, 23)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42'] = {'inputs': ['icn_032_ceo_cfo_buy_weight_42'], 'func': icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42}


def icn_base_universe_d2_024_icn_034_insider_conviction_84(icn_034_insider_conviction_84):
    return _base_universe_d2(icn_034_insider_conviction_84, 24)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_024_icn_034_insider_conviction_84'] = {'inputs': ['icn_034_insider_conviction_84'], 'func': icn_base_universe_d2_024_icn_034_insider_conviction_84}


def icn_base_universe_d2_025_icn_035_insider_silence_126(icn_035_insider_silence_126):
    return _base_universe_d2(icn_035_insider_silence_126, 25)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_025_icn_035_insider_silence_126'] = {'inputs': ['icn_035_insider_silence_126'], 'func': icn_base_universe_d2_025_icn_035_insider_silence_126}


def icn_base_universe_d2_026_icn_036_insider_buy_cluster_189(icn_036_insider_buy_cluster_189):
    return _base_universe_d2(icn_036_insider_buy_cluster_189, 26)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_026_icn_036_insider_buy_cluster_189'] = {'inputs': ['icn_036_insider_buy_cluster_189'], 'func': icn_base_universe_d2_026_icn_036_insider_buy_cluster_189}


def icn_base_universe_d2_027_icn_038_insider_value_ratio_378(icn_038_insider_value_ratio_378):
    return _base_universe_d2(icn_038_insider_value_ratio_378, 27)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_027_icn_038_insider_value_ratio_378'] = {'inputs': ['icn_038_insider_value_ratio_378'], 'func': icn_base_universe_d2_027_icn_038_insider_value_ratio_378}


def icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504(icn_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(icn_039_ceo_cfo_buy_weight_504, 28)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504'] = {'inputs': ['icn_039_ceo_cfo_buy_weight_504'], 'func': icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504}


def icn_base_universe_d2_029_icn_041_insider_conviction_1008(icn_041_insider_conviction_1008):
    return _base_universe_d2(icn_041_insider_conviction_1008, 29)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_029_icn_041_insider_conviction_1008'] = {'inputs': ['icn_041_insider_conviction_1008'], 'func': icn_base_universe_d2_029_icn_041_insider_conviction_1008}


def icn_base_universe_d2_030_icn_042_insider_silence_1260(icn_042_insider_silence_1260):
    return _base_universe_d2(icn_042_insider_silence_1260, 30)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_030_icn_042_insider_silence_1260'] = {'inputs': ['icn_042_insider_silence_1260'], 'func': icn_base_universe_d2_030_icn_042_insider_silence_1260}


def icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512(icn_043_insider_buy_cluster_1512):
    return _base_universe_d2(icn_043_insider_buy_cluster_1512, 31)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512'] = {'inputs': ['icn_043_insider_buy_cluster_1512'], 'func': icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512}


def icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63(icn_044_insider_net_buy_ratio_63):
    return _base_universe_d2(icn_044_insider_net_buy_ratio_63, 32)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63'] = {'inputs': ['icn_044_insider_net_buy_ratio_63'], 'func': icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63}


def icn_base_universe_d2_033_icn_045_insider_value_ratio_252(icn_045_insider_value_ratio_252):
    return _base_universe_d2(icn_045_insider_value_ratio_252, 33)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_033_icn_045_insider_value_ratio_252'] = {'inputs': ['icn_045_insider_value_ratio_252'], 'func': icn_base_universe_d2_033_icn_045_insider_value_ratio_252}


def icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21(icn_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(icn_046_ceo_cfo_buy_weight_21, 34)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21'] = {'inputs': ['icn_046_ceo_cfo_buy_weight_21'], 'func': icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21}


def icn_base_universe_d2_035_icn_048_insider_conviction_63(icn_048_insider_conviction_63):
    return _base_universe_d2(icn_048_insider_conviction_63, 35)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_035_icn_048_insider_conviction_63'] = {'inputs': ['icn_048_insider_conviction_63'], 'func': icn_base_universe_d2_035_icn_048_insider_conviction_63}


def icn_base_universe_d2_036_icn_049_insider_silence_84(icn_049_insider_silence_84):
    return _base_universe_d2(icn_049_insider_silence_84, 36)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_036_icn_049_insider_silence_84'] = {'inputs': ['icn_049_insider_silence_84'], 'func': icn_base_universe_d2_036_icn_049_insider_silence_84}


def icn_base_universe_d2_037_icn_050_insider_buy_cluster_126(icn_050_insider_buy_cluster_126):
    return _base_universe_d2(icn_050_insider_buy_cluster_126, 37)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_037_icn_050_insider_buy_cluster_126'] = {'inputs': ['icn_050_insider_buy_cluster_126'], 'func': icn_base_universe_d2_037_icn_050_insider_buy_cluster_126}


def icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189(icn_051_insider_net_buy_ratio_189):
    return _base_universe_d2(icn_051_insider_net_buy_ratio_189, 38)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189'] = {'inputs': ['icn_051_insider_net_buy_ratio_189'], 'func': icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189}


def icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378(icn_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(icn_053_ceo_cfo_buy_weight_378, 39)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378'] = {'inputs': ['icn_053_ceo_cfo_buy_weight_378'], 'func': icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378}


def icn_base_universe_d2_040_icn_055_insider_conviction_756(icn_055_insider_conviction_756):
    return _base_universe_d2(icn_055_insider_conviction_756, 40)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_040_icn_055_insider_conviction_756'] = {'inputs': ['icn_055_insider_conviction_756'], 'func': icn_base_universe_d2_040_icn_055_insider_conviction_756}


def icn_base_universe_d2_041_icn_056_insider_silence_1008(icn_056_insider_silence_1008):
    return _base_universe_d2(icn_056_insider_silence_1008, 41)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_041_icn_056_insider_silence_1008'] = {'inputs': ['icn_056_insider_silence_1008'], 'func': icn_base_universe_d2_041_icn_056_insider_silence_1008}


def icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260(icn_057_insider_buy_cluster_1260):
    return _base_universe_d2(icn_057_insider_buy_cluster_1260, 42)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260'] = {'inputs': ['icn_057_insider_buy_cluster_1260'], 'func': icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260}


def icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512(icn_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(icn_058_insider_net_buy_ratio_1512, 43)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512'] = {'inputs': ['icn_058_insider_net_buy_ratio_1512'], 'func': icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512}


def icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252(icn_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(icn_060_ceo_cfo_buy_weight_252, 44)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252'] = {'inputs': ['icn_060_ceo_cfo_buy_weight_252'], 'func': icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252}


def icn_base_universe_d2_045_icn_062_insider_conviction_42(icn_062_insider_conviction_42):
    return _base_universe_d2(icn_062_insider_conviction_42, 45)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_045_icn_062_insider_conviction_42'] = {'inputs': ['icn_062_insider_conviction_42'], 'func': icn_base_universe_d2_045_icn_062_insider_conviction_42}


def icn_base_universe_d2_046_icn_064_insider_buy_cluster_84(icn_064_insider_buy_cluster_84):
    return _base_universe_d2(icn_064_insider_buy_cluster_84, 46)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_046_icn_064_insider_buy_cluster_84'] = {'inputs': ['icn_064_insider_buy_cluster_84'], 'func': icn_base_universe_d2_046_icn_064_insider_buy_cluster_84}


def icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126(icn_065_insider_net_buy_ratio_126):
    return _base_universe_d2(icn_065_insider_net_buy_ratio_126, 47)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126'] = {'inputs': ['icn_065_insider_net_buy_ratio_126'], 'func': icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126}


def icn_base_universe_d2_048_icn_066_insider_value_ratio_189(icn_066_insider_value_ratio_189):
    return _base_universe_d2(icn_066_insider_value_ratio_189, 48)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_048_icn_066_insider_value_ratio_189'] = {'inputs': ['icn_066_insider_value_ratio_189'], 'func': icn_base_universe_d2_048_icn_066_insider_value_ratio_189}


def icn_base_universe_d2_049_icn_069_insider_conviction_504(icn_069_insider_conviction_504):
    return _base_universe_d2(icn_069_insider_conviction_504, 49)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_049_icn_069_insider_conviction_504'] = {'inputs': ['icn_069_insider_conviction_504'], 'func': icn_base_universe_d2_049_icn_069_insider_conviction_504}


def icn_base_universe_d2_050_icn_070_insider_silence_756(icn_070_insider_silence_756):
    return _base_universe_d2(icn_070_insider_silence_756, 50)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_050_icn_070_insider_silence_756'] = {'inputs': ['icn_070_insider_silence_756'], 'func': icn_base_universe_d2_050_icn_070_insider_silence_756}


def icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008(icn_071_insider_buy_cluster_1008):
    return _base_universe_d2(icn_071_insider_buy_cluster_1008, 51)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008'] = {'inputs': ['icn_071_insider_buy_cluster_1008'], 'func': icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008}


def icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260(icn_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(icn_072_insider_net_buy_ratio_1260, 52)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260'] = {'inputs': ['icn_072_insider_net_buy_ratio_1260'], 'func': icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260}


def icn_base_universe_d2_053_icn_073_insider_value_ratio_1512(icn_073_insider_value_ratio_1512):
    return _base_universe_d2(icn_073_insider_value_ratio_1512, 53)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_053_icn_073_insider_value_ratio_1512'] = {'inputs': ['icn_073_insider_value_ratio_1512'], 'func': icn_base_universe_d2_053_icn_073_insider_value_ratio_1512}


def icn_base_universe_d2_054_icn_basefill_005(icn_basefill_005):
    return _base_universe_d2(icn_basefill_005, 54)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_054_icn_basefill_005'] = {'inputs': ['icn_basefill_005'], 'func': icn_base_universe_d2_054_icn_basefill_005}


def icn_base_universe_d2_055_icn_basefill_012(icn_basefill_012):
    return _base_universe_d2(icn_basefill_012, 55)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_055_icn_basefill_012'] = {'inputs': ['icn_basefill_012'], 'func': icn_base_universe_d2_055_icn_basefill_012}


def icn_base_universe_d2_056_icn_basefill_019(icn_basefill_019):
    return _base_universe_d2(icn_basefill_019, 56)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_056_icn_basefill_019'] = {'inputs': ['icn_basefill_019'], 'func': icn_base_universe_d2_056_icn_basefill_019}


def icn_base_universe_d2_057_icn_basefill_022(icn_basefill_022):
    return _base_universe_d2(icn_basefill_022, 57)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_057_icn_basefill_022'] = {'inputs': ['icn_basefill_022'], 'func': icn_base_universe_d2_057_icn_basefill_022}


def icn_base_universe_d2_058_icn_basefill_026(icn_basefill_026):
    return _base_universe_d2(icn_basefill_026, 58)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_058_icn_basefill_026'] = {'inputs': ['icn_basefill_026'], 'func': icn_base_universe_d2_058_icn_basefill_026}


def icn_base_universe_d2_059_icn_basefill_033(icn_basefill_033):
    return _base_universe_d2(icn_basefill_033, 59)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_059_icn_basefill_033'] = {'inputs': ['icn_basefill_033'], 'func': icn_base_universe_d2_059_icn_basefill_033}


def icn_base_universe_d2_060_icn_basefill_037(icn_basefill_037):
    return _base_universe_d2(icn_basefill_037, 60)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_060_icn_basefill_037'] = {'inputs': ['icn_basefill_037'], 'func': icn_base_universe_d2_060_icn_basefill_037}


def icn_base_universe_d2_061_icn_basefill_040(icn_basefill_040):
    return _base_universe_d2(icn_basefill_040, 61)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_061_icn_basefill_040'] = {'inputs': ['icn_basefill_040'], 'func': icn_base_universe_d2_061_icn_basefill_040}


def icn_base_universe_d2_062_icn_basefill_047(icn_basefill_047):
    return _base_universe_d2(icn_basefill_047, 62)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_062_icn_basefill_047'] = {'inputs': ['icn_basefill_047'], 'func': icn_base_universe_d2_062_icn_basefill_047}


def icn_base_universe_d2_063_icn_basefill_052(icn_basefill_052):
    return _base_universe_d2(icn_basefill_052, 63)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_063_icn_basefill_052'] = {'inputs': ['icn_basefill_052'], 'func': icn_base_universe_d2_063_icn_basefill_052}


def icn_base_universe_d2_064_icn_basefill_054(icn_basefill_054):
    return _base_universe_d2(icn_basefill_054, 64)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_064_icn_basefill_054'] = {'inputs': ['icn_basefill_054'], 'func': icn_base_universe_d2_064_icn_basefill_054}


def icn_base_universe_d2_065_icn_basefill_059(icn_basefill_059):
    return _base_universe_d2(icn_basefill_059, 65)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_065_icn_basefill_059'] = {'inputs': ['icn_basefill_059'], 'func': icn_base_universe_d2_065_icn_basefill_059}


def icn_base_universe_d2_066_icn_basefill_061(icn_basefill_061):
    return _base_universe_d2(icn_basefill_061, 66)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_066_icn_basefill_061'] = {'inputs': ['icn_basefill_061'], 'func': icn_base_universe_d2_066_icn_basefill_061}


def icn_base_universe_d2_067_icn_basefill_063(icn_basefill_063):
    return _base_universe_d2(icn_basefill_063, 67)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_067_icn_basefill_063'] = {'inputs': ['icn_basefill_063'], 'func': icn_base_universe_d2_067_icn_basefill_063}


def icn_base_universe_d2_068_icn_basefill_067(icn_basefill_067):
    return _base_universe_d2(icn_basefill_067, 68)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_068_icn_basefill_067'] = {'inputs': ['icn_basefill_067'], 'func': icn_base_universe_d2_068_icn_basefill_067}


def icn_base_universe_d2_069_icn_basefill_068(icn_basefill_068):
    return _base_universe_d2(icn_basefill_068, 69)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_069_icn_basefill_068'] = {'inputs': ['icn_basefill_068'], 'func': icn_base_universe_d2_069_icn_basefill_068}


def icn_base_universe_d2_070_icn_basefill_074(icn_basefill_074):
    return _base_universe_d2(icn_basefill_074, 70)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_070_icn_basefill_074'] = {'inputs': ['icn_basefill_074'], 'func': icn_base_universe_d2_070_icn_basefill_074}


def icn_base_universe_d2_071_icn_basefill_075(icn_basefill_075):
    return _base_universe_d2(icn_basefill_075, 71)
ICN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icn_base_universe_d2_071_icn_basefill_075'] = {'inputs': ['icn_basefill_075'], 'func': icn_base_universe_d2_071_icn_basefill_075}
