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



def itf_151_itf_001_insider_buy_cluster_21_roc_1(itf_001_insider_buy_cluster_21):
    feature = _s(itf_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def itf_152_itf_007_insider_silence_252_roc_42(itf_007_insider_silence_252):
    feature = _s(itf_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def itf_153_itf_013_insider_conviction_1512_roc_126(itf_013_insider_conviction_1512):
    feature = _s(itf_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def itf_154_itf_019_insider_activity_accel_1_roc_378(itf_019_insider_activity_accel_1):
    feature = _s(itf_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4(itf_025_ceo_cfo_buy_weight_756):
    feature = _s(itf_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_TRANSACTION_FREQ_REGISTRY_2ND_DERIVATIVES = {
    'itf_151_itf_001_insider_buy_cluster_21_roc_1': {'inputs': ['itf_001_insider_buy_cluster_21'], 'func': itf_151_itf_001_insider_buy_cluster_21_roc_1},
    'itf_152_itf_007_insider_silence_252_roc_42': {'inputs': ['itf_007_insider_silence_252'], 'func': itf_152_itf_007_insider_silence_252_roc_42},
    'itf_153_itf_013_insider_conviction_1512_roc_126': {'inputs': ['itf_013_insider_conviction_1512'], 'func': itf_153_itf_013_insider_conviction_1512_roc_126},
    'itf_154_itf_019_insider_activity_accel_1_roc_378': {'inputs': ['itf_019_insider_activity_accel_1'], 'func': itf_154_itf_019_insider_activity_accel_1_roc_378},
    'itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['itf_025_ceo_cfo_buy_weight_756'], 'func': itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def itf_replacement_d2_001(itf_019_insider_activity_accel_1):
    feature = _clean(itf_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_001'] = {'inputs': ['itf_019_insider_activity_accel_1'], 'func': itf_replacement_d2_001}


def itf_replacement_d2_002(itf_replacement_001):
    feature = _clean(itf_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_002'] = {'inputs': ['itf_replacement_001'], 'func': itf_replacement_d2_002}


def itf_replacement_d2_003(itf_replacement_002):
    feature = _clean(itf_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_003'] = {'inputs': ['itf_replacement_002'], 'func': itf_replacement_d2_003}


def itf_replacement_d2_004(itf_replacement_003):
    feature = _clean(itf_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_004'] = {'inputs': ['itf_replacement_003'], 'func': itf_replacement_d2_004}


def itf_replacement_d2_005(itf_replacement_004):
    feature = _clean(itf_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_005'] = {'inputs': ['itf_replacement_004'], 'func': itf_replacement_d2_005}


def itf_replacement_d2_006(itf_replacement_005):
    feature = _clean(itf_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_006'] = {'inputs': ['itf_replacement_005'], 'func': itf_replacement_d2_006}


def itf_replacement_d2_007(itf_replacement_006):
    feature = _clean(itf_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_007'] = {'inputs': ['itf_replacement_006'], 'func': itf_replacement_d2_007}


def itf_replacement_d2_008(itf_replacement_007):
    feature = _clean(itf_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_008'] = {'inputs': ['itf_replacement_007'], 'func': itf_replacement_d2_008}


def itf_replacement_d2_009(itf_replacement_008):
    feature = _clean(itf_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_009'] = {'inputs': ['itf_replacement_008'], 'func': itf_replacement_d2_009}


def itf_replacement_d2_010(itf_replacement_009):
    feature = _clean(itf_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_010'] = {'inputs': ['itf_replacement_009'], 'func': itf_replacement_d2_010}


def itf_replacement_d2_011(itf_replacement_010):
    feature = _clean(itf_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_011'] = {'inputs': ['itf_replacement_010'], 'func': itf_replacement_d2_011}


def itf_replacement_d2_012(itf_replacement_011):
    feature = _clean(itf_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_012'] = {'inputs': ['itf_replacement_011'], 'func': itf_replacement_d2_012}


def itf_replacement_d2_013(itf_replacement_012):
    feature = _clean(itf_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_013'] = {'inputs': ['itf_replacement_012'], 'func': itf_replacement_d2_013}


def itf_replacement_d2_014(itf_replacement_013):
    feature = _clean(itf_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_014'] = {'inputs': ['itf_replacement_013'], 'func': itf_replacement_d2_014}


def itf_replacement_d2_015(itf_replacement_014):
    feature = _clean(itf_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_015'] = {'inputs': ['itf_replacement_014'], 'func': itf_replacement_d2_015}


def itf_replacement_d2_016(itf_replacement_015):
    feature = _clean(itf_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_016'] = {'inputs': ['itf_replacement_015'], 'func': itf_replacement_d2_016}


def itf_replacement_d2_017(itf_replacement_016):
    feature = _clean(itf_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_017'] = {'inputs': ['itf_replacement_016'], 'func': itf_replacement_d2_017}


def itf_replacement_d2_018(itf_replacement_017):
    feature = _clean(itf_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_018'] = {'inputs': ['itf_replacement_017'], 'func': itf_replacement_d2_018}


def itf_replacement_d2_019(itf_replacement_018):
    feature = _clean(itf_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_019'] = {'inputs': ['itf_replacement_018'], 'func': itf_replacement_d2_019}


def itf_replacement_d2_020(itf_replacement_019):
    feature = _clean(itf_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_020'] = {'inputs': ['itf_replacement_019'], 'func': itf_replacement_d2_020}


def itf_replacement_d2_021(itf_replacement_020):
    feature = _clean(itf_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_021'] = {'inputs': ['itf_replacement_020'], 'func': itf_replacement_d2_021}


def itf_replacement_d2_022(itf_replacement_021):
    feature = _clean(itf_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_022'] = {'inputs': ['itf_replacement_021'], 'func': itf_replacement_d2_022}


def itf_replacement_d2_023(itf_replacement_022):
    feature = _clean(itf_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_023'] = {'inputs': ['itf_replacement_022'], 'func': itf_replacement_d2_023}


def itf_replacement_d2_024(itf_replacement_023):
    feature = _clean(itf_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_024'] = {'inputs': ['itf_replacement_023'], 'func': itf_replacement_d2_024}


def itf_replacement_d2_025(itf_replacement_024):
    feature = _clean(itf_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_025'] = {'inputs': ['itf_replacement_024'], 'func': itf_replacement_d2_025}


def itf_replacement_d2_026(itf_replacement_025):
    feature = _clean(itf_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_026'] = {'inputs': ['itf_replacement_025'], 'func': itf_replacement_d2_026}


def itf_replacement_d2_027(itf_replacement_026):
    feature = _clean(itf_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_027'] = {'inputs': ['itf_replacement_026'], 'func': itf_replacement_d2_027}


def itf_replacement_d2_028(itf_replacement_027):
    feature = _clean(itf_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_028'] = {'inputs': ['itf_replacement_027'], 'func': itf_replacement_d2_028}


def itf_replacement_d2_029(itf_replacement_028):
    feature = _clean(itf_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_029'] = {'inputs': ['itf_replacement_028'], 'func': itf_replacement_d2_029}


def itf_replacement_d2_030(itf_replacement_029):
    feature = _clean(itf_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_030'] = {'inputs': ['itf_replacement_029'], 'func': itf_replacement_d2_030}


def itf_replacement_d2_031(itf_replacement_030):
    feature = _clean(itf_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_031'] = {'inputs': ['itf_replacement_030'], 'func': itf_replacement_d2_031}


def itf_replacement_d2_032(itf_replacement_031):
    feature = _clean(itf_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_032'] = {'inputs': ['itf_replacement_031'], 'func': itf_replacement_d2_032}


def itf_replacement_d2_033(itf_replacement_032):
    feature = _clean(itf_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_033'] = {'inputs': ['itf_replacement_032'], 'func': itf_replacement_d2_033}


def itf_replacement_d2_034(itf_replacement_033):
    feature = _clean(itf_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_034'] = {'inputs': ['itf_replacement_033'], 'func': itf_replacement_d2_034}


def itf_replacement_d2_035(itf_replacement_034):
    feature = _clean(itf_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_035'] = {'inputs': ['itf_replacement_034'], 'func': itf_replacement_d2_035}


def itf_replacement_d2_036(itf_replacement_035):
    feature = _clean(itf_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_036'] = {'inputs': ['itf_replacement_035'], 'func': itf_replacement_d2_036}


def itf_replacement_d2_037(itf_replacement_036):
    feature = _clean(itf_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_037'] = {'inputs': ['itf_replacement_036'], 'func': itf_replacement_d2_037}


def itf_replacement_d2_038(itf_replacement_037):
    feature = _clean(itf_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_038'] = {'inputs': ['itf_replacement_037'], 'func': itf_replacement_d2_038}


def itf_replacement_d2_039(itf_replacement_038):
    feature = _clean(itf_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_039'] = {'inputs': ['itf_replacement_038'], 'func': itf_replacement_d2_039}


def itf_replacement_d2_040(itf_replacement_039):
    feature = _clean(itf_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_040'] = {'inputs': ['itf_replacement_039'], 'func': itf_replacement_d2_040}


def itf_replacement_d2_041(itf_replacement_040):
    feature = _clean(itf_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_041'] = {'inputs': ['itf_replacement_040'], 'func': itf_replacement_d2_041}


def itf_replacement_d2_042(itf_replacement_041):
    feature = _clean(itf_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_042'] = {'inputs': ['itf_replacement_041'], 'func': itf_replacement_d2_042}


def itf_replacement_d2_043(itf_replacement_042):
    feature = _clean(itf_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_043'] = {'inputs': ['itf_replacement_042'], 'func': itf_replacement_d2_043}


def itf_replacement_d2_044(itf_replacement_043):
    feature = _clean(itf_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_044'] = {'inputs': ['itf_replacement_043'], 'func': itf_replacement_d2_044}


def itf_replacement_d2_045(itf_replacement_044):
    feature = _clean(itf_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_045'] = {'inputs': ['itf_replacement_044'], 'func': itf_replacement_d2_045}


def itf_replacement_d2_046(itf_replacement_045):
    feature = _clean(itf_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_046'] = {'inputs': ['itf_replacement_045'], 'func': itf_replacement_d2_046}


def itf_replacement_d2_047(itf_replacement_046):
    feature = _clean(itf_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_047'] = {'inputs': ['itf_replacement_046'], 'func': itf_replacement_d2_047}


def itf_replacement_d2_048(itf_replacement_047):
    feature = _clean(itf_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_048'] = {'inputs': ['itf_replacement_047'], 'func': itf_replacement_d2_048}


def itf_replacement_d2_049(itf_replacement_048):
    feature = _clean(itf_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_049'] = {'inputs': ['itf_replacement_048'], 'func': itf_replacement_d2_049}


def itf_replacement_d2_050(itf_replacement_049):
    feature = _clean(itf_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_050'] = {'inputs': ['itf_replacement_049'], 'func': itf_replacement_d2_050}


def itf_replacement_d2_051(itf_replacement_050):
    feature = _clean(itf_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_051'] = {'inputs': ['itf_replacement_050'], 'func': itf_replacement_d2_051}


def itf_replacement_d2_052(itf_replacement_051):
    feature = _clean(itf_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_052'] = {'inputs': ['itf_replacement_051'], 'func': itf_replacement_d2_052}


def itf_replacement_d2_053(itf_replacement_052):
    feature = _clean(itf_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_053'] = {'inputs': ['itf_replacement_052'], 'func': itf_replacement_d2_053}


def itf_replacement_d2_054(itf_replacement_053):
    feature = _clean(itf_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_054'] = {'inputs': ['itf_replacement_053'], 'func': itf_replacement_d2_054}


def itf_replacement_d2_055(itf_replacement_054):
    feature = _clean(itf_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_055'] = {'inputs': ['itf_replacement_054'], 'func': itf_replacement_d2_055}


def itf_replacement_d2_056(itf_replacement_055):
    feature = _clean(itf_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_056'] = {'inputs': ['itf_replacement_055'], 'func': itf_replacement_d2_056}


def itf_replacement_d2_057(itf_replacement_056):
    feature = _clean(itf_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_057'] = {'inputs': ['itf_replacement_056'], 'func': itf_replacement_d2_057}


def itf_replacement_d2_058(itf_replacement_057):
    feature = _clean(itf_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_058'] = {'inputs': ['itf_replacement_057'], 'func': itf_replacement_d2_058}


def itf_replacement_d2_059(itf_replacement_058):
    feature = _clean(itf_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_059'] = {'inputs': ['itf_replacement_058'], 'func': itf_replacement_d2_059}


def itf_replacement_d2_060(itf_replacement_059):
    feature = _clean(itf_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_060'] = {'inputs': ['itf_replacement_059'], 'func': itf_replacement_d2_060}


def itf_replacement_d2_061(itf_replacement_060):
    feature = _clean(itf_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_061'] = {'inputs': ['itf_replacement_060'], 'func': itf_replacement_d2_061}


def itf_replacement_d2_062(itf_replacement_061):
    feature = _clean(itf_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_062'] = {'inputs': ['itf_replacement_061'], 'func': itf_replacement_d2_062}


def itf_replacement_d2_063(itf_replacement_062):
    feature = _clean(itf_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_063'] = {'inputs': ['itf_replacement_062'], 'func': itf_replacement_d2_063}


def itf_replacement_d2_064(itf_replacement_063):
    feature = _clean(itf_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_064'] = {'inputs': ['itf_replacement_063'], 'func': itf_replacement_d2_064}


def itf_replacement_d2_065(itf_replacement_064):
    feature = _clean(itf_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_065'] = {'inputs': ['itf_replacement_064'], 'func': itf_replacement_d2_065}


def itf_replacement_d2_066(itf_replacement_065):
    feature = _clean(itf_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_066'] = {'inputs': ['itf_replacement_065'], 'func': itf_replacement_d2_066}


def itf_replacement_d2_067(itf_replacement_066):
    feature = _clean(itf_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_067'] = {'inputs': ['itf_replacement_066'], 'func': itf_replacement_d2_067}


def itf_replacement_d2_068(itf_replacement_067):
    feature = _clean(itf_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_068'] = {'inputs': ['itf_replacement_067'], 'func': itf_replacement_d2_068}


def itf_replacement_d2_069(itf_replacement_068):
    feature = _clean(itf_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_069'] = {'inputs': ['itf_replacement_068'], 'func': itf_replacement_d2_069}


def itf_replacement_d2_070(itf_replacement_069):
    feature = _clean(itf_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_070'] = {'inputs': ['itf_replacement_069'], 'func': itf_replacement_d2_070}


def itf_replacement_d2_071(itf_replacement_070):
    feature = _clean(itf_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_071'] = {'inputs': ['itf_replacement_070'], 'func': itf_replacement_d2_071}


def itf_replacement_d2_072(itf_replacement_071):
    feature = _clean(itf_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_072'] = {'inputs': ['itf_replacement_071'], 'func': itf_replacement_d2_072}


def itf_replacement_d2_073(itf_replacement_072):
    feature = _clean(itf_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_073'] = {'inputs': ['itf_replacement_072'], 'func': itf_replacement_d2_073}


def itf_replacement_d2_074(itf_replacement_073):
    feature = _clean(itf_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_074'] = {'inputs': ['itf_replacement_073'], 'func': itf_replacement_d2_074}


def itf_replacement_d2_075(itf_replacement_074):
    feature = _clean(itf_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_075'] = {'inputs': ['itf_replacement_074'], 'func': itf_replacement_d2_075}


def itf_replacement_d2_076(itf_replacement_075):
    feature = _clean(itf_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_076'] = {'inputs': ['itf_replacement_075'], 'func': itf_replacement_d2_076}


def itf_replacement_d2_077(itf_replacement_076):
    feature = _clean(itf_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_077'] = {'inputs': ['itf_replacement_076'], 'func': itf_replacement_d2_077}


def itf_replacement_d2_078(itf_replacement_077):
    feature = _clean(itf_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_078'] = {'inputs': ['itf_replacement_077'], 'func': itf_replacement_d2_078}


def itf_replacement_d2_079(itf_replacement_078):
    feature = _clean(itf_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_079'] = {'inputs': ['itf_replacement_078'], 'func': itf_replacement_d2_079}


def itf_replacement_d2_080(itf_replacement_079):
    feature = _clean(itf_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_080'] = {'inputs': ['itf_replacement_079'], 'func': itf_replacement_d2_080}


def itf_replacement_d2_081(itf_replacement_080):
    feature = _clean(itf_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_081'] = {'inputs': ['itf_replacement_080'], 'func': itf_replacement_d2_081}


def itf_replacement_d2_082(itf_replacement_081):
    feature = _clean(itf_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_082'] = {'inputs': ['itf_replacement_081'], 'func': itf_replacement_d2_082}


def itf_replacement_d2_083(itf_replacement_082):
    feature = _clean(itf_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_083'] = {'inputs': ['itf_replacement_082'], 'func': itf_replacement_d2_083}


def itf_replacement_d2_084(itf_replacement_083):
    feature = _clean(itf_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_084'] = {'inputs': ['itf_replacement_083'], 'func': itf_replacement_d2_084}


def itf_replacement_d2_085(itf_replacement_084):
    feature = _clean(itf_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_085'] = {'inputs': ['itf_replacement_084'], 'func': itf_replacement_d2_085}


def itf_replacement_d2_086(itf_replacement_085):
    feature = _clean(itf_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_086'] = {'inputs': ['itf_replacement_085'], 'func': itf_replacement_d2_086}


def itf_replacement_d2_087(itf_replacement_086):
    feature = _clean(itf_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_087'] = {'inputs': ['itf_replacement_086'], 'func': itf_replacement_d2_087}


def itf_replacement_d2_088(itf_replacement_087):
    feature = _clean(itf_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_088'] = {'inputs': ['itf_replacement_087'], 'func': itf_replacement_d2_088}


def itf_replacement_d2_089(itf_replacement_088):
    feature = _clean(itf_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_089'] = {'inputs': ['itf_replacement_088'], 'func': itf_replacement_d2_089}


def itf_replacement_d2_090(itf_replacement_089):
    feature = _clean(itf_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_090'] = {'inputs': ['itf_replacement_089'], 'func': itf_replacement_d2_090}


def itf_replacement_d2_091(itf_replacement_090):
    feature = _clean(itf_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_091'] = {'inputs': ['itf_replacement_090'], 'func': itf_replacement_d2_091}


def itf_replacement_d2_092(itf_replacement_091):
    feature = _clean(itf_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_092'] = {'inputs': ['itf_replacement_091'], 'func': itf_replacement_d2_092}


def itf_replacement_d2_093(itf_replacement_092):
    feature = _clean(itf_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_093'] = {'inputs': ['itf_replacement_092'], 'func': itf_replacement_d2_093}


def itf_replacement_d2_094(itf_replacement_093):
    feature = _clean(itf_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_094'] = {'inputs': ['itf_replacement_093'], 'func': itf_replacement_d2_094}


def itf_replacement_d2_095(itf_replacement_094):
    feature = _clean(itf_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_095'] = {'inputs': ['itf_replacement_094'], 'func': itf_replacement_d2_095}


def itf_replacement_d2_096(itf_replacement_095):
    feature = _clean(itf_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_096'] = {'inputs': ['itf_replacement_095'], 'func': itf_replacement_d2_096}


def itf_replacement_d2_097(itf_replacement_096):
    feature = _clean(itf_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_097'] = {'inputs': ['itf_replacement_096'], 'func': itf_replacement_d2_097}


def itf_replacement_d2_098(itf_replacement_097):
    feature = _clean(itf_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_098'] = {'inputs': ['itf_replacement_097'], 'func': itf_replacement_d2_098}


def itf_replacement_d2_099(itf_replacement_098):
    feature = _clean(itf_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_099'] = {'inputs': ['itf_replacement_098'], 'func': itf_replacement_d2_099}


def itf_replacement_d2_100(itf_replacement_099):
    feature = _clean(itf_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_100'] = {'inputs': ['itf_replacement_099'], 'func': itf_replacement_d2_100}


def itf_replacement_d2_101(itf_replacement_100):
    feature = _clean(itf_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_101'] = {'inputs': ['itf_replacement_100'], 'func': itf_replacement_d2_101}


def itf_replacement_d2_102(itf_replacement_101):
    feature = _clean(itf_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_102'] = {'inputs': ['itf_replacement_101'], 'func': itf_replacement_d2_102}


def itf_replacement_d2_103(itf_replacement_102):
    feature = _clean(itf_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_103'] = {'inputs': ['itf_replacement_102'], 'func': itf_replacement_d2_103}


def itf_replacement_d2_104(itf_replacement_103):
    feature = _clean(itf_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_104'] = {'inputs': ['itf_replacement_103'], 'func': itf_replacement_d2_104}


def itf_replacement_d2_105(itf_replacement_104):
    feature = _clean(itf_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_105'] = {'inputs': ['itf_replacement_104'], 'func': itf_replacement_d2_105}


def itf_replacement_d2_106(itf_replacement_105):
    feature = _clean(itf_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_106'] = {'inputs': ['itf_replacement_105'], 'func': itf_replacement_d2_106}


def itf_replacement_d2_107(itf_replacement_106):
    feature = _clean(itf_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_107'] = {'inputs': ['itf_replacement_106'], 'func': itf_replacement_d2_107}


def itf_replacement_d2_108(itf_replacement_107):
    feature = _clean(itf_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_108'] = {'inputs': ['itf_replacement_107'], 'func': itf_replacement_d2_108}


def itf_replacement_d2_109(itf_replacement_108):
    feature = _clean(itf_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_109'] = {'inputs': ['itf_replacement_108'], 'func': itf_replacement_d2_109}


def itf_replacement_d2_110(itf_replacement_109):
    feature = _clean(itf_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_110'] = {'inputs': ['itf_replacement_109'], 'func': itf_replacement_d2_110}


def itf_replacement_d2_111(itf_replacement_110):
    feature = _clean(itf_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_111'] = {'inputs': ['itf_replacement_110'], 'func': itf_replacement_d2_111}


def itf_replacement_d2_112(itf_replacement_111):
    feature = _clean(itf_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
ITF_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['itf_replacement_d2_112'] = {'inputs': ['itf_replacement_111'], 'func': itf_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42(itf_002_insider_net_buy_ratio_42):
    return _base_universe_d2(itf_002_insider_net_buy_ratio_42, 1)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42'] = {'inputs': ['itf_002_insider_net_buy_ratio_42'], 'func': itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42}


def itf_base_universe_d2_002_itf_003_insider_value_ratio_63(itf_003_insider_value_ratio_63):
    return _base_universe_d2(itf_003_insider_value_ratio_63, 2)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_002_itf_003_insider_value_ratio_63'] = {'inputs': ['itf_003_insider_value_ratio_63'], 'func': itf_base_universe_d2_002_itf_003_insider_value_ratio_63}


def itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84(itf_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(itf_004_ceo_cfo_buy_weight_84, 3)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84'] = {'inputs': ['itf_004_ceo_cfo_buy_weight_84'], 'func': itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84}


def itf_base_universe_d2_004_itf_006_insider_conviction_189(itf_006_insider_conviction_189):
    return _base_universe_d2(itf_006_insider_conviction_189, 4)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_004_itf_006_insider_conviction_189'] = {'inputs': ['itf_006_insider_conviction_189'], 'func': itf_base_universe_d2_004_itf_006_insider_conviction_189}


def itf_base_universe_d2_005_itf_008_insider_buy_cluster_378(itf_008_insider_buy_cluster_378):
    return _base_universe_d2(itf_008_insider_buy_cluster_378, 5)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_005_itf_008_insider_buy_cluster_378'] = {'inputs': ['itf_008_insider_buy_cluster_378'], 'func': itf_base_universe_d2_005_itf_008_insider_buy_cluster_378}


def itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504(itf_009_insider_net_buy_ratio_504):
    return _base_universe_d2(itf_009_insider_net_buy_ratio_504, 6)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504'] = {'inputs': ['itf_009_insider_net_buy_ratio_504'], 'func': itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504}


def itf_base_universe_d2_007_itf_010_insider_value_ratio_756(itf_010_insider_value_ratio_756):
    return _base_universe_d2(itf_010_insider_value_ratio_756, 7)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_007_itf_010_insider_value_ratio_756'] = {'inputs': ['itf_010_insider_value_ratio_756'], 'func': itf_base_universe_d2_007_itf_010_insider_value_ratio_756}


def itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008(itf_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(itf_011_ceo_cfo_buy_weight_1008, 8)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['itf_011_ceo_cfo_buy_weight_1008'], 'func': itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008}


def itf_base_universe_d2_009_itf_014_insider_silence_63(itf_014_insider_silence_63):
    return _base_universe_d2(itf_014_insider_silence_63, 9)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_009_itf_014_insider_silence_63'] = {'inputs': ['itf_014_insider_silence_63'], 'func': itf_base_universe_d2_009_itf_014_insider_silence_63}


def itf_base_universe_d2_010_itf_015_insider_buy_cluster_252(itf_015_insider_buy_cluster_252):
    return _base_universe_d2(itf_015_insider_buy_cluster_252, 10)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_010_itf_015_insider_buy_cluster_252'] = {'inputs': ['itf_015_insider_buy_cluster_252'], 'func': itf_base_universe_d2_010_itf_015_insider_buy_cluster_252}


def itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21(itf_016_insider_net_buy_ratio_21):
    return _base_universe_d2(itf_016_insider_net_buy_ratio_21, 11)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21'] = {'inputs': ['itf_016_insider_net_buy_ratio_21'], 'func': itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21}


def itf_base_universe_d2_012_itf_017_insider_value_ratio_42(itf_017_insider_value_ratio_42):
    return _base_universe_d2(itf_017_insider_value_ratio_42, 12)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_012_itf_017_insider_value_ratio_42'] = {'inputs': ['itf_017_insider_value_ratio_42'], 'func': itf_base_universe_d2_012_itf_017_insider_value_ratio_42}


def itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63(itf_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(itf_018_ceo_cfo_buy_weight_63, 13)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63'] = {'inputs': ['itf_018_ceo_cfo_buy_weight_63'], 'func': itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63}


def itf_base_universe_d2_014_itf_020_insider_conviction_126(itf_020_insider_conviction_126):
    return _base_universe_d2(itf_020_insider_conviction_126, 14)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_014_itf_020_insider_conviction_126'] = {'inputs': ['itf_020_insider_conviction_126'], 'func': itf_base_universe_d2_014_itf_020_insider_conviction_126}


def itf_base_universe_d2_015_itf_021_insider_silence_189(itf_021_insider_silence_189):
    return _base_universe_d2(itf_021_insider_silence_189, 15)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_015_itf_021_insider_silence_189'] = {'inputs': ['itf_021_insider_silence_189'], 'func': itf_base_universe_d2_015_itf_021_insider_silence_189}


def itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378(itf_023_insider_net_buy_ratio_378):
    return _base_universe_d2(itf_023_insider_net_buy_ratio_378, 16)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378'] = {'inputs': ['itf_023_insider_net_buy_ratio_378'], 'func': itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378}


def itf_base_universe_d2_017_itf_024_insider_value_ratio_504(itf_024_insider_value_ratio_504):
    return _base_universe_d2(itf_024_insider_value_ratio_504, 17)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_017_itf_024_insider_value_ratio_504'] = {'inputs': ['itf_024_insider_value_ratio_504'], 'func': itf_base_universe_d2_017_itf_024_insider_value_ratio_504}


def itf_base_universe_d2_018_itf_027_insider_conviction_1260(itf_027_insider_conviction_1260):
    return _base_universe_d2(itf_027_insider_conviction_1260, 18)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_018_itf_027_insider_conviction_1260'] = {'inputs': ['itf_027_insider_conviction_1260'], 'func': itf_base_universe_d2_018_itf_027_insider_conviction_1260}


def itf_base_universe_d2_019_itf_028_insider_silence_1512(itf_028_insider_silence_1512):
    return _base_universe_d2(itf_028_insider_silence_1512, 19)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_019_itf_028_insider_silence_1512'] = {'inputs': ['itf_028_insider_silence_1512'], 'func': itf_base_universe_d2_019_itf_028_insider_silence_1512}


def itf_base_universe_d2_020_itf_029_insider_buy_cluster_63(itf_029_insider_buy_cluster_63):
    return _base_universe_d2(itf_029_insider_buy_cluster_63, 20)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_020_itf_029_insider_buy_cluster_63'] = {'inputs': ['itf_029_insider_buy_cluster_63'], 'func': itf_base_universe_d2_020_itf_029_insider_buy_cluster_63}


def itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252(itf_030_insider_net_buy_ratio_252):
    return _base_universe_d2(itf_030_insider_net_buy_ratio_252, 21)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252'] = {'inputs': ['itf_030_insider_net_buy_ratio_252'], 'func': itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252}


def itf_base_universe_d2_022_itf_031_insider_value_ratio_21(itf_031_insider_value_ratio_21):
    return _base_universe_d2(itf_031_insider_value_ratio_21, 22)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_022_itf_031_insider_value_ratio_21'] = {'inputs': ['itf_031_insider_value_ratio_21'], 'func': itf_base_universe_d2_022_itf_031_insider_value_ratio_21}


def itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42(itf_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(itf_032_ceo_cfo_buy_weight_42, 23)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42'] = {'inputs': ['itf_032_ceo_cfo_buy_weight_42'], 'func': itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42}


def itf_base_universe_d2_024_itf_034_insider_conviction_84(itf_034_insider_conviction_84):
    return _base_universe_d2(itf_034_insider_conviction_84, 24)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_024_itf_034_insider_conviction_84'] = {'inputs': ['itf_034_insider_conviction_84'], 'func': itf_base_universe_d2_024_itf_034_insider_conviction_84}


def itf_base_universe_d2_025_itf_035_insider_silence_126(itf_035_insider_silence_126):
    return _base_universe_d2(itf_035_insider_silence_126, 25)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_025_itf_035_insider_silence_126'] = {'inputs': ['itf_035_insider_silence_126'], 'func': itf_base_universe_d2_025_itf_035_insider_silence_126}


def itf_base_universe_d2_026_itf_036_insider_buy_cluster_189(itf_036_insider_buy_cluster_189):
    return _base_universe_d2(itf_036_insider_buy_cluster_189, 26)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_026_itf_036_insider_buy_cluster_189'] = {'inputs': ['itf_036_insider_buy_cluster_189'], 'func': itf_base_universe_d2_026_itf_036_insider_buy_cluster_189}


def itf_base_universe_d2_027_itf_038_insider_value_ratio_378(itf_038_insider_value_ratio_378):
    return _base_universe_d2(itf_038_insider_value_ratio_378, 27)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_027_itf_038_insider_value_ratio_378'] = {'inputs': ['itf_038_insider_value_ratio_378'], 'func': itf_base_universe_d2_027_itf_038_insider_value_ratio_378}


def itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504(itf_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(itf_039_ceo_cfo_buy_weight_504, 28)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504'] = {'inputs': ['itf_039_ceo_cfo_buy_weight_504'], 'func': itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504}


def itf_base_universe_d2_029_itf_041_insider_conviction_1008(itf_041_insider_conviction_1008):
    return _base_universe_d2(itf_041_insider_conviction_1008, 29)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_029_itf_041_insider_conviction_1008'] = {'inputs': ['itf_041_insider_conviction_1008'], 'func': itf_base_universe_d2_029_itf_041_insider_conviction_1008}


def itf_base_universe_d2_030_itf_042_insider_silence_1260(itf_042_insider_silence_1260):
    return _base_universe_d2(itf_042_insider_silence_1260, 30)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_030_itf_042_insider_silence_1260'] = {'inputs': ['itf_042_insider_silence_1260'], 'func': itf_base_universe_d2_030_itf_042_insider_silence_1260}


def itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512(itf_043_insider_buy_cluster_1512):
    return _base_universe_d2(itf_043_insider_buy_cluster_1512, 31)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512'] = {'inputs': ['itf_043_insider_buy_cluster_1512'], 'func': itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512}


def itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63(itf_044_insider_net_buy_ratio_63):
    return _base_universe_d2(itf_044_insider_net_buy_ratio_63, 32)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63'] = {'inputs': ['itf_044_insider_net_buy_ratio_63'], 'func': itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63}


def itf_base_universe_d2_033_itf_045_insider_value_ratio_252(itf_045_insider_value_ratio_252):
    return _base_universe_d2(itf_045_insider_value_ratio_252, 33)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_033_itf_045_insider_value_ratio_252'] = {'inputs': ['itf_045_insider_value_ratio_252'], 'func': itf_base_universe_d2_033_itf_045_insider_value_ratio_252}


def itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21(itf_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(itf_046_ceo_cfo_buy_weight_21, 34)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21'] = {'inputs': ['itf_046_ceo_cfo_buy_weight_21'], 'func': itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21}


def itf_base_universe_d2_035_itf_048_insider_conviction_63(itf_048_insider_conviction_63):
    return _base_universe_d2(itf_048_insider_conviction_63, 35)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_035_itf_048_insider_conviction_63'] = {'inputs': ['itf_048_insider_conviction_63'], 'func': itf_base_universe_d2_035_itf_048_insider_conviction_63}


def itf_base_universe_d2_036_itf_049_insider_silence_84(itf_049_insider_silence_84):
    return _base_universe_d2(itf_049_insider_silence_84, 36)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_036_itf_049_insider_silence_84'] = {'inputs': ['itf_049_insider_silence_84'], 'func': itf_base_universe_d2_036_itf_049_insider_silence_84}


def itf_base_universe_d2_037_itf_050_insider_buy_cluster_126(itf_050_insider_buy_cluster_126):
    return _base_universe_d2(itf_050_insider_buy_cluster_126, 37)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_037_itf_050_insider_buy_cluster_126'] = {'inputs': ['itf_050_insider_buy_cluster_126'], 'func': itf_base_universe_d2_037_itf_050_insider_buy_cluster_126}


def itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189(itf_051_insider_net_buy_ratio_189):
    return _base_universe_d2(itf_051_insider_net_buy_ratio_189, 38)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189'] = {'inputs': ['itf_051_insider_net_buy_ratio_189'], 'func': itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189}


def itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378(itf_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(itf_053_ceo_cfo_buy_weight_378, 39)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378'] = {'inputs': ['itf_053_ceo_cfo_buy_weight_378'], 'func': itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378}


def itf_base_universe_d2_040_itf_055_insider_conviction_756(itf_055_insider_conviction_756):
    return _base_universe_d2(itf_055_insider_conviction_756, 40)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_040_itf_055_insider_conviction_756'] = {'inputs': ['itf_055_insider_conviction_756'], 'func': itf_base_universe_d2_040_itf_055_insider_conviction_756}


def itf_base_universe_d2_041_itf_056_insider_silence_1008(itf_056_insider_silence_1008):
    return _base_universe_d2(itf_056_insider_silence_1008, 41)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_041_itf_056_insider_silence_1008'] = {'inputs': ['itf_056_insider_silence_1008'], 'func': itf_base_universe_d2_041_itf_056_insider_silence_1008}


def itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260(itf_057_insider_buy_cluster_1260):
    return _base_universe_d2(itf_057_insider_buy_cluster_1260, 42)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260'] = {'inputs': ['itf_057_insider_buy_cluster_1260'], 'func': itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260}


def itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512(itf_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(itf_058_insider_net_buy_ratio_1512, 43)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512'] = {'inputs': ['itf_058_insider_net_buy_ratio_1512'], 'func': itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512}


def itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252(itf_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(itf_060_ceo_cfo_buy_weight_252, 44)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252'] = {'inputs': ['itf_060_ceo_cfo_buy_weight_252'], 'func': itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252}


def itf_base_universe_d2_045_itf_062_insider_conviction_42(itf_062_insider_conviction_42):
    return _base_universe_d2(itf_062_insider_conviction_42, 45)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_045_itf_062_insider_conviction_42'] = {'inputs': ['itf_062_insider_conviction_42'], 'func': itf_base_universe_d2_045_itf_062_insider_conviction_42}


def itf_base_universe_d2_046_itf_064_insider_buy_cluster_84(itf_064_insider_buy_cluster_84):
    return _base_universe_d2(itf_064_insider_buy_cluster_84, 46)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_046_itf_064_insider_buy_cluster_84'] = {'inputs': ['itf_064_insider_buy_cluster_84'], 'func': itf_base_universe_d2_046_itf_064_insider_buy_cluster_84}


def itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126(itf_065_insider_net_buy_ratio_126):
    return _base_universe_d2(itf_065_insider_net_buy_ratio_126, 47)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126'] = {'inputs': ['itf_065_insider_net_buy_ratio_126'], 'func': itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126}


def itf_base_universe_d2_048_itf_066_insider_value_ratio_189(itf_066_insider_value_ratio_189):
    return _base_universe_d2(itf_066_insider_value_ratio_189, 48)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_048_itf_066_insider_value_ratio_189'] = {'inputs': ['itf_066_insider_value_ratio_189'], 'func': itf_base_universe_d2_048_itf_066_insider_value_ratio_189}


def itf_base_universe_d2_049_itf_069_insider_conviction_504(itf_069_insider_conviction_504):
    return _base_universe_d2(itf_069_insider_conviction_504, 49)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_049_itf_069_insider_conviction_504'] = {'inputs': ['itf_069_insider_conviction_504'], 'func': itf_base_universe_d2_049_itf_069_insider_conviction_504}


def itf_base_universe_d2_050_itf_070_insider_silence_756(itf_070_insider_silence_756):
    return _base_universe_d2(itf_070_insider_silence_756, 50)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_050_itf_070_insider_silence_756'] = {'inputs': ['itf_070_insider_silence_756'], 'func': itf_base_universe_d2_050_itf_070_insider_silence_756}


def itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008(itf_071_insider_buy_cluster_1008):
    return _base_universe_d2(itf_071_insider_buy_cluster_1008, 51)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008'] = {'inputs': ['itf_071_insider_buy_cluster_1008'], 'func': itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008}


def itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260(itf_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(itf_072_insider_net_buy_ratio_1260, 52)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260'] = {'inputs': ['itf_072_insider_net_buy_ratio_1260'], 'func': itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260}


def itf_base_universe_d2_053_itf_073_insider_value_ratio_1512(itf_073_insider_value_ratio_1512):
    return _base_universe_d2(itf_073_insider_value_ratio_1512, 53)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_053_itf_073_insider_value_ratio_1512'] = {'inputs': ['itf_073_insider_value_ratio_1512'], 'func': itf_base_universe_d2_053_itf_073_insider_value_ratio_1512}


def itf_base_universe_d2_054_itf_basefill_005(itf_basefill_005):
    return _base_universe_d2(itf_basefill_005, 54)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_054_itf_basefill_005'] = {'inputs': ['itf_basefill_005'], 'func': itf_base_universe_d2_054_itf_basefill_005}


def itf_base_universe_d2_055_itf_basefill_012(itf_basefill_012):
    return _base_universe_d2(itf_basefill_012, 55)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_055_itf_basefill_012'] = {'inputs': ['itf_basefill_012'], 'func': itf_base_universe_d2_055_itf_basefill_012}


def itf_base_universe_d2_056_itf_basefill_019(itf_basefill_019):
    return _base_universe_d2(itf_basefill_019, 56)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_056_itf_basefill_019'] = {'inputs': ['itf_basefill_019'], 'func': itf_base_universe_d2_056_itf_basefill_019}


def itf_base_universe_d2_057_itf_basefill_022(itf_basefill_022):
    return _base_universe_d2(itf_basefill_022, 57)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_057_itf_basefill_022'] = {'inputs': ['itf_basefill_022'], 'func': itf_base_universe_d2_057_itf_basefill_022}


def itf_base_universe_d2_058_itf_basefill_026(itf_basefill_026):
    return _base_universe_d2(itf_basefill_026, 58)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_058_itf_basefill_026'] = {'inputs': ['itf_basefill_026'], 'func': itf_base_universe_d2_058_itf_basefill_026}


def itf_base_universe_d2_059_itf_basefill_033(itf_basefill_033):
    return _base_universe_d2(itf_basefill_033, 59)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_059_itf_basefill_033'] = {'inputs': ['itf_basefill_033'], 'func': itf_base_universe_d2_059_itf_basefill_033}


def itf_base_universe_d2_060_itf_basefill_037(itf_basefill_037):
    return _base_universe_d2(itf_basefill_037, 60)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_060_itf_basefill_037'] = {'inputs': ['itf_basefill_037'], 'func': itf_base_universe_d2_060_itf_basefill_037}


def itf_base_universe_d2_061_itf_basefill_040(itf_basefill_040):
    return _base_universe_d2(itf_basefill_040, 61)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_061_itf_basefill_040'] = {'inputs': ['itf_basefill_040'], 'func': itf_base_universe_d2_061_itf_basefill_040}


def itf_base_universe_d2_062_itf_basefill_047(itf_basefill_047):
    return _base_universe_d2(itf_basefill_047, 62)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_062_itf_basefill_047'] = {'inputs': ['itf_basefill_047'], 'func': itf_base_universe_d2_062_itf_basefill_047}


def itf_base_universe_d2_063_itf_basefill_052(itf_basefill_052):
    return _base_universe_d2(itf_basefill_052, 63)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_063_itf_basefill_052'] = {'inputs': ['itf_basefill_052'], 'func': itf_base_universe_d2_063_itf_basefill_052}


def itf_base_universe_d2_064_itf_basefill_054(itf_basefill_054):
    return _base_universe_d2(itf_basefill_054, 64)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_064_itf_basefill_054'] = {'inputs': ['itf_basefill_054'], 'func': itf_base_universe_d2_064_itf_basefill_054}


def itf_base_universe_d2_065_itf_basefill_059(itf_basefill_059):
    return _base_universe_d2(itf_basefill_059, 65)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_065_itf_basefill_059'] = {'inputs': ['itf_basefill_059'], 'func': itf_base_universe_d2_065_itf_basefill_059}


def itf_base_universe_d2_066_itf_basefill_061(itf_basefill_061):
    return _base_universe_d2(itf_basefill_061, 66)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_066_itf_basefill_061'] = {'inputs': ['itf_basefill_061'], 'func': itf_base_universe_d2_066_itf_basefill_061}


def itf_base_universe_d2_067_itf_basefill_063(itf_basefill_063):
    return _base_universe_d2(itf_basefill_063, 67)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_067_itf_basefill_063'] = {'inputs': ['itf_basefill_063'], 'func': itf_base_universe_d2_067_itf_basefill_063}


def itf_base_universe_d2_068_itf_basefill_067(itf_basefill_067):
    return _base_universe_d2(itf_basefill_067, 68)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_068_itf_basefill_067'] = {'inputs': ['itf_basefill_067'], 'func': itf_base_universe_d2_068_itf_basefill_067}


def itf_base_universe_d2_069_itf_basefill_068(itf_basefill_068):
    return _base_universe_d2(itf_basefill_068, 69)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_069_itf_basefill_068'] = {'inputs': ['itf_basefill_068'], 'func': itf_base_universe_d2_069_itf_basefill_068}


def itf_base_universe_d2_070_itf_basefill_074(itf_basefill_074):
    return _base_universe_d2(itf_basefill_074, 70)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_070_itf_basefill_074'] = {'inputs': ['itf_basefill_074'], 'func': itf_base_universe_d2_070_itf_basefill_074}


def itf_base_universe_d2_071_itf_basefill_075(itf_basefill_075):
    return _base_universe_d2(itf_basefill_075, 71)
ITF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itf_base_universe_d2_071_itf_basefill_075'] = {'inputs': ['itf_basefill_075'], 'func': itf_base_universe_d2_071_itf_basefill_075}
