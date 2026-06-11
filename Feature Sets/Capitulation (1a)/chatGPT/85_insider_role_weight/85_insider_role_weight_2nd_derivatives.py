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



def irw_151_irw_001_insider_buy_cluster_21_roc_1(irw_001_insider_buy_cluster_21):
    feature = _s(irw_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def irw_152_irw_007_insider_silence_252_roc_42(irw_007_insider_silence_252):
    feature = _s(irw_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def irw_153_irw_013_insider_conviction_1512_roc_126(irw_013_insider_conviction_1512):
    feature = _s(irw_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def irw_154_irw_019_insider_activity_accel_1_roc_378(irw_019_insider_activity_accel_1):
    feature = _s(irw_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def irw_155_irw_025_ceo_cfo_buy_weight_756_roc_4(irw_025_ceo_cfo_buy_weight_756):
    feature = _s(irw_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_ROLE_WEIGHT_REGISTRY_2ND_DERIVATIVES = {
    'irw_151_irw_001_insider_buy_cluster_21_roc_1': {'inputs': ['irw_001_insider_buy_cluster_21'], 'func': irw_151_irw_001_insider_buy_cluster_21_roc_1},
    'irw_152_irw_007_insider_silence_252_roc_42': {'inputs': ['irw_007_insider_silence_252'], 'func': irw_152_irw_007_insider_silence_252_roc_42},
    'irw_153_irw_013_insider_conviction_1512_roc_126': {'inputs': ['irw_013_insider_conviction_1512'], 'func': irw_153_irw_013_insider_conviction_1512_roc_126},
    'irw_154_irw_019_insider_activity_accel_1_roc_378': {'inputs': ['irw_019_insider_activity_accel_1'], 'func': irw_154_irw_019_insider_activity_accel_1_roc_378},
    'irw_155_irw_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['irw_025_ceo_cfo_buy_weight_756'], 'func': irw_155_irw_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def irw_replacement_d2_001(irw_019_insider_activity_accel_1):
    feature = _clean(irw_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_001'] = {'inputs': ['irw_019_insider_activity_accel_1'], 'func': irw_replacement_d2_001}


def irw_replacement_d2_002(irw_replacement_001):
    feature = _clean(irw_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_002'] = {'inputs': ['irw_replacement_001'], 'func': irw_replacement_d2_002}


def irw_replacement_d2_003(irw_replacement_002):
    feature = _clean(irw_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_003'] = {'inputs': ['irw_replacement_002'], 'func': irw_replacement_d2_003}


def irw_replacement_d2_004(irw_replacement_003):
    feature = _clean(irw_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_004'] = {'inputs': ['irw_replacement_003'], 'func': irw_replacement_d2_004}


def irw_replacement_d2_005(irw_replacement_004):
    feature = _clean(irw_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_005'] = {'inputs': ['irw_replacement_004'], 'func': irw_replacement_d2_005}


def irw_replacement_d2_006(irw_replacement_005):
    feature = _clean(irw_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_006'] = {'inputs': ['irw_replacement_005'], 'func': irw_replacement_d2_006}


def irw_replacement_d2_007(irw_replacement_006):
    feature = _clean(irw_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_007'] = {'inputs': ['irw_replacement_006'], 'func': irw_replacement_d2_007}


def irw_replacement_d2_008(irw_replacement_007):
    feature = _clean(irw_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_008'] = {'inputs': ['irw_replacement_007'], 'func': irw_replacement_d2_008}


def irw_replacement_d2_009(irw_replacement_008):
    feature = _clean(irw_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_009'] = {'inputs': ['irw_replacement_008'], 'func': irw_replacement_d2_009}


def irw_replacement_d2_010(irw_replacement_009):
    feature = _clean(irw_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_010'] = {'inputs': ['irw_replacement_009'], 'func': irw_replacement_d2_010}


def irw_replacement_d2_011(irw_replacement_010):
    feature = _clean(irw_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_011'] = {'inputs': ['irw_replacement_010'], 'func': irw_replacement_d2_011}


def irw_replacement_d2_012(irw_replacement_011):
    feature = _clean(irw_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_012'] = {'inputs': ['irw_replacement_011'], 'func': irw_replacement_d2_012}


def irw_replacement_d2_013(irw_replacement_012):
    feature = _clean(irw_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_013'] = {'inputs': ['irw_replacement_012'], 'func': irw_replacement_d2_013}


def irw_replacement_d2_014(irw_replacement_013):
    feature = _clean(irw_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_014'] = {'inputs': ['irw_replacement_013'], 'func': irw_replacement_d2_014}


def irw_replacement_d2_015(irw_replacement_014):
    feature = _clean(irw_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_015'] = {'inputs': ['irw_replacement_014'], 'func': irw_replacement_d2_015}


def irw_replacement_d2_016(irw_replacement_015):
    feature = _clean(irw_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_016'] = {'inputs': ['irw_replacement_015'], 'func': irw_replacement_d2_016}


def irw_replacement_d2_017(irw_replacement_016):
    feature = _clean(irw_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_017'] = {'inputs': ['irw_replacement_016'], 'func': irw_replacement_d2_017}


def irw_replacement_d2_018(irw_replacement_017):
    feature = _clean(irw_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_018'] = {'inputs': ['irw_replacement_017'], 'func': irw_replacement_d2_018}


def irw_replacement_d2_019(irw_replacement_018):
    feature = _clean(irw_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_019'] = {'inputs': ['irw_replacement_018'], 'func': irw_replacement_d2_019}


def irw_replacement_d2_020(irw_replacement_019):
    feature = _clean(irw_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_020'] = {'inputs': ['irw_replacement_019'], 'func': irw_replacement_d2_020}


def irw_replacement_d2_021(irw_replacement_020):
    feature = _clean(irw_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_021'] = {'inputs': ['irw_replacement_020'], 'func': irw_replacement_d2_021}


def irw_replacement_d2_022(irw_replacement_021):
    feature = _clean(irw_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_022'] = {'inputs': ['irw_replacement_021'], 'func': irw_replacement_d2_022}


def irw_replacement_d2_023(irw_replacement_022):
    feature = _clean(irw_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_023'] = {'inputs': ['irw_replacement_022'], 'func': irw_replacement_d2_023}


def irw_replacement_d2_024(irw_replacement_023):
    feature = _clean(irw_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_024'] = {'inputs': ['irw_replacement_023'], 'func': irw_replacement_d2_024}


def irw_replacement_d2_025(irw_replacement_024):
    feature = _clean(irw_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_025'] = {'inputs': ['irw_replacement_024'], 'func': irw_replacement_d2_025}


def irw_replacement_d2_026(irw_replacement_025):
    feature = _clean(irw_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_026'] = {'inputs': ['irw_replacement_025'], 'func': irw_replacement_d2_026}


def irw_replacement_d2_027(irw_replacement_026):
    feature = _clean(irw_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_027'] = {'inputs': ['irw_replacement_026'], 'func': irw_replacement_d2_027}


def irw_replacement_d2_028(irw_replacement_027):
    feature = _clean(irw_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_028'] = {'inputs': ['irw_replacement_027'], 'func': irw_replacement_d2_028}


def irw_replacement_d2_029(irw_replacement_028):
    feature = _clean(irw_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_029'] = {'inputs': ['irw_replacement_028'], 'func': irw_replacement_d2_029}


def irw_replacement_d2_030(irw_replacement_029):
    feature = _clean(irw_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_030'] = {'inputs': ['irw_replacement_029'], 'func': irw_replacement_d2_030}


def irw_replacement_d2_031(irw_replacement_030):
    feature = _clean(irw_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_031'] = {'inputs': ['irw_replacement_030'], 'func': irw_replacement_d2_031}


def irw_replacement_d2_032(irw_replacement_031):
    feature = _clean(irw_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_032'] = {'inputs': ['irw_replacement_031'], 'func': irw_replacement_d2_032}


def irw_replacement_d2_033(irw_replacement_032):
    feature = _clean(irw_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_033'] = {'inputs': ['irw_replacement_032'], 'func': irw_replacement_d2_033}


def irw_replacement_d2_034(irw_replacement_033):
    feature = _clean(irw_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_034'] = {'inputs': ['irw_replacement_033'], 'func': irw_replacement_d2_034}


def irw_replacement_d2_035(irw_replacement_034):
    feature = _clean(irw_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_035'] = {'inputs': ['irw_replacement_034'], 'func': irw_replacement_d2_035}


def irw_replacement_d2_036(irw_replacement_035):
    feature = _clean(irw_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_036'] = {'inputs': ['irw_replacement_035'], 'func': irw_replacement_d2_036}


def irw_replacement_d2_037(irw_replacement_036):
    feature = _clean(irw_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_037'] = {'inputs': ['irw_replacement_036'], 'func': irw_replacement_d2_037}


def irw_replacement_d2_038(irw_replacement_037):
    feature = _clean(irw_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_038'] = {'inputs': ['irw_replacement_037'], 'func': irw_replacement_d2_038}


def irw_replacement_d2_039(irw_replacement_038):
    feature = _clean(irw_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_039'] = {'inputs': ['irw_replacement_038'], 'func': irw_replacement_d2_039}


def irw_replacement_d2_040(irw_replacement_039):
    feature = _clean(irw_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_040'] = {'inputs': ['irw_replacement_039'], 'func': irw_replacement_d2_040}


def irw_replacement_d2_041(irw_replacement_040):
    feature = _clean(irw_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_041'] = {'inputs': ['irw_replacement_040'], 'func': irw_replacement_d2_041}


def irw_replacement_d2_042(irw_replacement_041):
    feature = _clean(irw_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_042'] = {'inputs': ['irw_replacement_041'], 'func': irw_replacement_d2_042}


def irw_replacement_d2_043(irw_replacement_042):
    feature = _clean(irw_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_043'] = {'inputs': ['irw_replacement_042'], 'func': irw_replacement_d2_043}


def irw_replacement_d2_044(irw_replacement_043):
    feature = _clean(irw_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_044'] = {'inputs': ['irw_replacement_043'], 'func': irw_replacement_d2_044}


def irw_replacement_d2_045(irw_replacement_044):
    feature = _clean(irw_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_045'] = {'inputs': ['irw_replacement_044'], 'func': irw_replacement_d2_045}


def irw_replacement_d2_046(irw_replacement_045):
    feature = _clean(irw_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_046'] = {'inputs': ['irw_replacement_045'], 'func': irw_replacement_d2_046}


def irw_replacement_d2_047(irw_replacement_046):
    feature = _clean(irw_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_047'] = {'inputs': ['irw_replacement_046'], 'func': irw_replacement_d2_047}


def irw_replacement_d2_048(irw_replacement_047):
    feature = _clean(irw_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_048'] = {'inputs': ['irw_replacement_047'], 'func': irw_replacement_d2_048}


def irw_replacement_d2_049(irw_replacement_048):
    feature = _clean(irw_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_049'] = {'inputs': ['irw_replacement_048'], 'func': irw_replacement_d2_049}


def irw_replacement_d2_050(irw_replacement_049):
    feature = _clean(irw_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_050'] = {'inputs': ['irw_replacement_049'], 'func': irw_replacement_d2_050}


def irw_replacement_d2_051(irw_replacement_050):
    feature = _clean(irw_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_051'] = {'inputs': ['irw_replacement_050'], 'func': irw_replacement_d2_051}


def irw_replacement_d2_052(irw_replacement_051):
    feature = _clean(irw_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_052'] = {'inputs': ['irw_replacement_051'], 'func': irw_replacement_d2_052}


def irw_replacement_d2_053(irw_replacement_052):
    feature = _clean(irw_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_053'] = {'inputs': ['irw_replacement_052'], 'func': irw_replacement_d2_053}


def irw_replacement_d2_054(irw_replacement_053):
    feature = _clean(irw_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_054'] = {'inputs': ['irw_replacement_053'], 'func': irw_replacement_d2_054}


def irw_replacement_d2_055(irw_replacement_054):
    feature = _clean(irw_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_055'] = {'inputs': ['irw_replacement_054'], 'func': irw_replacement_d2_055}


def irw_replacement_d2_056(irw_replacement_055):
    feature = _clean(irw_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_056'] = {'inputs': ['irw_replacement_055'], 'func': irw_replacement_d2_056}


def irw_replacement_d2_057(irw_replacement_056):
    feature = _clean(irw_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_057'] = {'inputs': ['irw_replacement_056'], 'func': irw_replacement_d2_057}


def irw_replacement_d2_058(irw_replacement_057):
    feature = _clean(irw_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_058'] = {'inputs': ['irw_replacement_057'], 'func': irw_replacement_d2_058}


def irw_replacement_d2_059(irw_replacement_058):
    feature = _clean(irw_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_059'] = {'inputs': ['irw_replacement_058'], 'func': irw_replacement_d2_059}


def irw_replacement_d2_060(irw_replacement_059):
    feature = _clean(irw_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_060'] = {'inputs': ['irw_replacement_059'], 'func': irw_replacement_d2_060}


def irw_replacement_d2_061(irw_replacement_060):
    feature = _clean(irw_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_061'] = {'inputs': ['irw_replacement_060'], 'func': irw_replacement_d2_061}


def irw_replacement_d2_062(irw_replacement_061):
    feature = _clean(irw_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_062'] = {'inputs': ['irw_replacement_061'], 'func': irw_replacement_d2_062}


def irw_replacement_d2_063(irw_replacement_062):
    feature = _clean(irw_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_063'] = {'inputs': ['irw_replacement_062'], 'func': irw_replacement_d2_063}


def irw_replacement_d2_064(irw_replacement_063):
    feature = _clean(irw_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_064'] = {'inputs': ['irw_replacement_063'], 'func': irw_replacement_d2_064}


def irw_replacement_d2_065(irw_replacement_064):
    feature = _clean(irw_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_065'] = {'inputs': ['irw_replacement_064'], 'func': irw_replacement_d2_065}


def irw_replacement_d2_066(irw_replacement_065):
    feature = _clean(irw_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_066'] = {'inputs': ['irw_replacement_065'], 'func': irw_replacement_d2_066}


def irw_replacement_d2_067(irw_replacement_066):
    feature = _clean(irw_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_067'] = {'inputs': ['irw_replacement_066'], 'func': irw_replacement_d2_067}


def irw_replacement_d2_068(irw_replacement_067):
    feature = _clean(irw_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_068'] = {'inputs': ['irw_replacement_067'], 'func': irw_replacement_d2_068}


def irw_replacement_d2_069(irw_replacement_068):
    feature = _clean(irw_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_069'] = {'inputs': ['irw_replacement_068'], 'func': irw_replacement_d2_069}


def irw_replacement_d2_070(irw_replacement_069):
    feature = _clean(irw_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_070'] = {'inputs': ['irw_replacement_069'], 'func': irw_replacement_d2_070}


def irw_replacement_d2_071(irw_replacement_070):
    feature = _clean(irw_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_071'] = {'inputs': ['irw_replacement_070'], 'func': irw_replacement_d2_071}


def irw_replacement_d2_072(irw_replacement_071):
    feature = _clean(irw_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_072'] = {'inputs': ['irw_replacement_071'], 'func': irw_replacement_d2_072}


def irw_replacement_d2_073(irw_replacement_072):
    feature = _clean(irw_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_073'] = {'inputs': ['irw_replacement_072'], 'func': irw_replacement_d2_073}


def irw_replacement_d2_074(irw_replacement_073):
    feature = _clean(irw_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_074'] = {'inputs': ['irw_replacement_073'], 'func': irw_replacement_d2_074}


def irw_replacement_d2_075(irw_replacement_074):
    feature = _clean(irw_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_075'] = {'inputs': ['irw_replacement_074'], 'func': irw_replacement_d2_075}


def irw_replacement_d2_076(irw_replacement_075):
    feature = _clean(irw_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_076'] = {'inputs': ['irw_replacement_075'], 'func': irw_replacement_d2_076}


def irw_replacement_d2_077(irw_replacement_076):
    feature = _clean(irw_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_077'] = {'inputs': ['irw_replacement_076'], 'func': irw_replacement_d2_077}


def irw_replacement_d2_078(irw_replacement_077):
    feature = _clean(irw_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_078'] = {'inputs': ['irw_replacement_077'], 'func': irw_replacement_d2_078}


def irw_replacement_d2_079(irw_replacement_078):
    feature = _clean(irw_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_079'] = {'inputs': ['irw_replacement_078'], 'func': irw_replacement_d2_079}


def irw_replacement_d2_080(irw_replacement_079):
    feature = _clean(irw_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_080'] = {'inputs': ['irw_replacement_079'], 'func': irw_replacement_d2_080}


def irw_replacement_d2_081(irw_replacement_080):
    feature = _clean(irw_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_081'] = {'inputs': ['irw_replacement_080'], 'func': irw_replacement_d2_081}


def irw_replacement_d2_082(irw_replacement_081):
    feature = _clean(irw_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_082'] = {'inputs': ['irw_replacement_081'], 'func': irw_replacement_d2_082}


def irw_replacement_d2_083(irw_replacement_082):
    feature = _clean(irw_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_083'] = {'inputs': ['irw_replacement_082'], 'func': irw_replacement_d2_083}


def irw_replacement_d2_084(irw_replacement_083):
    feature = _clean(irw_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_084'] = {'inputs': ['irw_replacement_083'], 'func': irw_replacement_d2_084}


def irw_replacement_d2_085(irw_replacement_084):
    feature = _clean(irw_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_085'] = {'inputs': ['irw_replacement_084'], 'func': irw_replacement_d2_085}


def irw_replacement_d2_086(irw_replacement_085):
    feature = _clean(irw_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_086'] = {'inputs': ['irw_replacement_085'], 'func': irw_replacement_d2_086}


def irw_replacement_d2_087(irw_replacement_086):
    feature = _clean(irw_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_087'] = {'inputs': ['irw_replacement_086'], 'func': irw_replacement_d2_087}


def irw_replacement_d2_088(irw_replacement_087):
    feature = _clean(irw_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_088'] = {'inputs': ['irw_replacement_087'], 'func': irw_replacement_d2_088}


def irw_replacement_d2_089(irw_replacement_088):
    feature = _clean(irw_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_089'] = {'inputs': ['irw_replacement_088'], 'func': irw_replacement_d2_089}


def irw_replacement_d2_090(irw_replacement_089):
    feature = _clean(irw_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_090'] = {'inputs': ['irw_replacement_089'], 'func': irw_replacement_d2_090}


def irw_replacement_d2_091(irw_replacement_090):
    feature = _clean(irw_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_091'] = {'inputs': ['irw_replacement_090'], 'func': irw_replacement_d2_091}


def irw_replacement_d2_092(irw_replacement_091):
    feature = _clean(irw_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_092'] = {'inputs': ['irw_replacement_091'], 'func': irw_replacement_d2_092}


def irw_replacement_d2_093(irw_replacement_092):
    feature = _clean(irw_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_093'] = {'inputs': ['irw_replacement_092'], 'func': irw_replacement_d2_093}


def irw_replacement_d2_094(irw_replacement_093):
    feature = _clean(irw_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_094'] = {'inputs': ['irw_replacement_093'], 'func': irw_replacement_d2_094}


def irw_replacement_d2_095(irw_replacement_094):
    feature = _clean(irw_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_095'] = {'inputs': ['irw_replacement_094'], 'func': irw_replacement_d2_095}


def irw_replacement_d2_096(irw_replacement_095):
    feature = _clean(irw_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_096'] = {'inputs': ['irw_replacement_095'], 'func': irw_replacement_d2_096}


def irw_replacement_d2_097(irw_replacement_096):
    feature = _clean(irw_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_097'] = {'inputs': ['irw_replacement_096'], 'func': irw_replacement_d2_097}


def irw_replacement_d2_098(irw_replacement_097):
    feature = _clean(irw_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_098'] = {'inputs': ['irw_replacement_097'], 'func': irw_replacement_d2_098}


def irw_replacement_d2_099(irw_replacement_098):
    feature = _clean(irw_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_099'] = {'inputs': ['irw_replacement_098'], 'func': irw_replacement_d2_099}


def irw_replacement_d2_100(irw_replacement_099):
    feature = _clean(irw_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_100'] = {'inputs': ['irw_replacement_099'], 'func': irw_replacement_d2_100}


def irw_replacement_d2_101(irw_replacement_100):
    feature = _clean(irw_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_101'] = {'inputs': ['irw_replacement_100'], 'func': irw_replacement_d2_101}


def irw_replacement_d2_102(irw_replacement_101):
    feature = _clean(irw_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_102'] = {'inputs': ['irw_replacement_101'], 'func': irw_replacement_d2_102}


def irw_replacement_d2_103(irw_replacement_102):
    feature = _clean(irw_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_103'] = {'inputs': ['irw_replacement_102'], 'func': irw_replacement_d2_103}


def irw_replacement_d2_104(irw_replacement_103):
    feature = _clean(irw_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_104'] = {'inputs': ['irw_replacement_103'], 'func': irw_replacement_d2_104}


def irw_replacement_d2_105(irw_replacement_104):
    feature = _clean(irw_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_105'] = {'inputs': ['irw_replacement_104'], 'func': irw_replacement_d2_105}


def irw_replacement_d2_106(irw_replacement_105):
    feature = _clean(irw_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_106'] = {'inputs': ['irw_replacement_105'], 'func': irw_replacement_d2_106}


def irw_replacement_d2_107(irw_replacement_106):
    feature = _clean(irw_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_107'] = {'inputs': ['irw_replacement_106'], 'func': irw_replacement_d2_107}


def irw_replacement_d2_108(irw_replacement_107):
    feature = _clean(irw_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_108'] = {'inputs': ['irw_replacement_107'], 'func': irw_replacement_d2_108}


def irw_replacement_d2_109(irw_replacement_108):
    feature = _clean(irw_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_109'] = {'inputs': ['irw_replacement_108'], 'func': irw_replacement_d2_109}


def irw_replacement_d2_110(irw_replacement_109):
    feature = _clean(irw_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_110'] = {'inputs': ['irw_replacement_109'], 'func': irw_replacement_d2_110}


def irw_replacement_d2_111(irw_replacement_110):
    feature = _clean(irw_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_111'] = {'inputs': ['irw_replacement_110'], 'func': irw_replacement_d2_111}


def irw_replacement_d2_112(irw_replacement_111):
    feature = _clean(irw_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IRW_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['irw_replacement_d2_112'] = {'inputs': ['irw_replacement_111'], 'func': irw_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def irw_base_universe_d2_001_irw_002_insider_net_buy_ratio_42(irw_002_insider_net_buy_ratio_42):
    return _base_universe_d2(irw_002_insider_net_buy_ratio_42, 1)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_001_irw_002_insider_net_buy_ratio_42'] = {'inputs': ['irw_002_insider_net_buy_ratio_42'], 'func': irw_base_universe_d2_001_irw_002_insider_net_buy_ratio_42}


def irw_base_universe_d2_002_irw_003_insider_value_ratio_63(irw_003_insider_value_ratio_63):
    return _base_universe_d2(irw_003_insider_value_ratio_63, 2)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_002_irw_003_insider_value_ratio_63'] = {'inputs': ['irw_003_insider_value_ratio_63'], 'func': irw_base_universe_d2_002_irw_003_insider_value_ratio_63}


def irw_base_universe_d2_003_irw_004_ceo_cfo_buy_weight_84(irw_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(irw_004_ceo_cfo_buy_weight_84, 3)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_003_irw_004_ceo_cfo_buy_weight_84'] = {'inputs': ['irw_004_ceo_cfo_buy_weight_84'], 'func': irw_base_universe_d2_003_irw_004_ceo_cfo_buy_weight_84}


def irw_base_universe_d2_004_irw_006_insider_conviction_189(irw_006_insider_conviction_189):
    return _base_universe_d2(irw_006_insider_conviction_189, 4)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_004_irw_006_insider_conviction_189'] = {'inputs': ['irw_006_insider_conviction_189'], 'func': irw_base_universe_d2_004_irw_006_insider_conviction_189}


def irw_base_universe_d2_005_irw_008_insider_buy_cluster_378(irw_008_insider_buy_cluster_378):
    return _base_universe_d2(irw_008_insider_buy_cluster_378, 5)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_005_irw_008_insider_buy_cluster_378'] = {'inputs': ['irw_008_insider_buy_cluster_378'], 'func': irw_base_universe_d2_005_irw_008_insider_buy_cluster_378}


def irw_base_universe_d2_006_irw_009_insider_net_buy_ratio_504(irw_009_insider_net_buy_ratio_504):
    return _base_universe_d2(irw_009_insider_net_buy_ratio_504, 6)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_006_irw_009_insider_net_buy_ratio_504'] = {'inputs': ['irw_009_insider_net_buy_ratio_504'], 'func': irw_base_universe_d2_006_irw_009_insider_net_buy_ratio_504}


def irw_base_universe_d2_007_irw_010_insider_value_ratio_756(irw_010_insider_value_ratio_756):
    return _base_universe_d2(irw_010_insider_value_ratio_756, 7)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_007_irw_010_insider_value_ratio_756'] = {'inputs': ['irw_010_insider_value_ratio_756'], 'func': irw_base_universe_d2_007_irw_010_insider_value_ratio_756}


def irw_base_universe_d2_008_irw_011_ceo_cfo_buy_weight_1008(irw_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(irw_011_ceo_cfo_buy_weight_1008, 8)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_008_irw_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['irw_011_ceo_cfo_buy_weight_1008'], 'func': irw_base_universe_d2_008_irw_011_ceo_cfo_buy_weight_1008}


def irw_base_universe_d2_009_irw_014_insider_silence_63(irw_014_insider_silence_63):
    return _base_universe_d2(irw_014_insider_silence_63, 9)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_009_irw_014_insider_silence_63'] = {'inputs': ['irw_014_insider_silence_63'], 'func': irw_base_universe_d2_009_irw_014_insider_silence_63}


def irw_base_universe_d2_010_irw_015_insider_buy_cluster_252(irw_015_insider_buy_cluster_252):
    return _base_universe_d2(irw_015_insider_buy_cluster_252, 10)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_010_irw_015_insider_buy_cluster_252'] = {'inputs': ['irw_015_insider_buy_cluster_252'], 'func': irw_base_universe_d2_010_irw_015_insider_buy_cluster_252}


def irw_base_universe_d2_011_irw_016_insider_net_buy_ratio_21(irw_016_insider_net_buy_ratio_21):
    return _base_universe_d2(irw_016_insider_net_buy_ratio_21, 11)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_011_irw_016_insider_net_buy_ratio_21'] = {'inputs': ['irw_016_insider_net_buy_ratio_21'], 'func': irw_base_universe_d2_011_irw_016_insider_net_buy_ratio_21}


def irw_base_universe_d2_012_irw_017_insider_value_ratio_42(irw_017_insider_value_ratio_42):
    return _base_universe_d2(irw_017_insider_value_ratio_42, 12)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_012_irw_017_insider_value_ratio_42'] = {'inputs': ['irw_017_insider_value_ratio_42'], 'func': irw_base_universe_d2_012_irw_017_insider_value_ratio_42}


def irw_base_universe_d2_013_irw_018_ceo_cfo_buy_weight_63(irw_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(irw_018_ceo_cfo_buy_weight_63, 13)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_013_irw_018_ceo_cfo_buy_weight_63'] = {'inputs': ['irw_018_ceo_cfo_buy_weight_63'], 'func': irw_base_universe_d2_013_irw_018_ceo_cfo_buy_weight_63}


def irw_base_universe_d2_014_irw_020_insider_conviction_126(irw_020_insider_conviction_126):
    return _base_universe_d2(irw_020_insider_conviction_126, 14)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_014_irw_020_insider_conviction_126'] = {'inputs': ['irw_020_insider_conviction_126'], 'func': irw_base_universe_d2_014_irw_020_insider_conviction_126}


def irw_base_universe_d2_015_irw_021_insider_silence_189(irw_021_insider_silence_189):
    return _base_universe_d2(irw_021_insider_silence_189, 15)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_015_irw_021_insider_silence_189'] = {'inputs': ['irw_021_insider_silence_189'], 'func': irw_base_universe_d2_015_irw_021_insider_silence_189}


def irw_base_universe_d2_016_irw_023_insider_net_buy_ratio_378(irw_023_insider_net_buy_ratio_378):
    return _base_universe_d2(irw_023_insider_net_buy_ratio_378, 16)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_016_irw_023_insider_net_buy_ratio_378'] = {'inputs': ['irw_023_insider_net_buy_ratio_378'], 'func': irw_base_universe_d2_016_irw_023_insider_net_buy_ratio_378}


def irw_base_universe_d2_017_irw_024_insider_value_ratio_504(irw_024_insider_value_ratio_504):
    return _base_universe_d2(irw_024_insider_value_ratio_504, 17)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_017_irw_024_insider_value_ratio_504'] = {'inputs': ['irw_024_insider_value_ratio_504'], 'func': irw_base_universe_d2_017_irw_024_insider_value_ratio_504}


def irw_base_universe_d2_018_irw_027_insider_conviction_1260(irw_027_insider_conviction_1260):
    return _base_universe_d2(irw_027_insider_conviction_1260, 18)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_018_irw_027_insider_conviction_1260'] = {'inputs': ['irw_027_insider_conviction_1260'], 'func': irw_base_universe_d2_018_irw_027_insider_conviction_1260}


def irw_base_universe_d2_019_irw_028_insider_silence_1512(irw_028_insider_silence_1512):
    return _base_universe_d2(irw_028_insider_silence_1512, 19)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_019_irw_028_insider_silence_1512'] = {'inputs': ['irw_028_insider_silence_1512'], 'func': irw_base_universe_d2_019_irw_028_insider_silence_1512}


def irw_base_universe_d2_020_irw_029_insider_buy_cluster_63(irw_029_insider_buy_cluster_63):
    return _base_universe_d2(irw_029_insider_buy_cluster_63, 20)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_020_irw_029_insider_buy_cluster_63'] = {'inputs': ['irw_029_insider_buy_cluster_63'], 'func': irw_base_universe_d2_020_irw_029_insider_buy_cluster_63}


def irw_base_universe_d2_021_irw_030_insider_net_buy_ratio_252(irw_030_insider_net_buy_ratio_252):
    return _base_universe_d2(irw_030_insider_net_buy_ratio_252, 21)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_021_irw_030_insider_net_buy_ratio_252'] = {'inputs': ['irw_030_insider_net_buy_ratio_252'], 'func': irw_base_universe_d2_021_irw_030_insider_net_buy_ratio_252}


def irw_base_universe_d2_022_irw_031_insider_value_ratio_21(irw_031_insider_value_ratio_21):
    return _base_universe_d2(irw_031_insider_value_ratio_21, 22)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_022_irw_031_insider_value_ratio_21'] = {'inputs': ['irw_031_insider_value_ratio_21'], 'func': irw_base_universe_d2_022_irw_031_insider_value_ratio_21}


def irw_base_universe_d2_023_irw_032_ceo_cfo_buy_weight_42(irw_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(irw_032_ceo_cfo_buy_weight_42, 23)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_023_irw_032_ceo_cfo_buy_weight_42'] = {'inputs': ['irw_032_ceo_cfo_buy_weight_42'], 'func': irw_base_universe_d2_023_irw_032_ceo_cfo_buy_weight_42}


def irw_base_universe_d2_024_irw_034_insider_conviction_84(irw_034_insider_conviction_84):
    return _base_universe_d2(irw_034_insider_conviction_84, 24)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_024_irw_034_insider_conviction_84'] = {'inputs': ['irw_034_insider_conviction_84'], 'func': irw_base_universe_d2_024_irw_034_insider_conviction_84}


def irw_base_universe_d2_025_irw_035_insider_silence_126(irw_035_insider_silence_126):
    return _base_universe_d2(irw_035_insider_silence_126, 25)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_025_irw_035_insider_silence_126'] = {'inputs': ['irw_035_insider_silence_126'], 'func': irw_base_universe_d2_025_irw_035_insider_silence_126}


def irw_base_universe_d2_026_irw_036_insider_buy_cluster_189(irw_036_insider_buy_cluster_189):
    return _base_universe_d2(irw_036_insider_buy_cluster_189, 26)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_026_irw_036_insider_buy_cluster_189'] = {'inputs': ['irw_036_insider_buy_cluster_189'], 'func': irw_base_universe_d2_026_irw_036_insider_buy_cluster_189}


def irw_base_universe_d2_027_irw_038_insider_value_ratio_378(irw_038_insider_value_ratio_378):
    return _base_universe_d2(irw_038_insider_value_ratio_378, 27)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_027_irw_038_insider_value_ratio_378'] = {'inputs': ['irw_038_insider_value_ratio_378'], 'func': irw_base_universe_d2_027_irw_038_insider_value_ratio_378}


def irw_base_universe_d2_028_irw_039_ceo_cfo_buy_weight_504(irw_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(irw_039_ceo_cfo_buy_weight_504, 28)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_028_irw_039_ceo_cfo_buy_weight_504'] = {'inputs': ['irw_039_ceo_cfo_buy_weight_504'], 'func': irw_base_universe_d2_028_irw_039_ceo_cfo_buy_weight_504}


def irw_base_universe_d2_029_irw_041_insider_conviction_1008(irw_041_insider_conviction_1008):
    return _base_universe_d2(irw_041_insider_conviction_1008, 29)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_029_irw_041_insider_conviction_1008'] = {'inputs': ['irw_041_insider_conviction_1008'], 'func': irw_base_universe_d2_029_irw_041_insider_conviction_1008}


def irw_base_universe_d2_030_irw_042_insider_silence_1260(irw_042_insider_silence_1260):
    return _base_universe_d2(irw_042_insider_silence_1260, 30)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_030_irw_042_insider_silence_1260'] = {'inputs': ['irw_042_insider_silence_1260'], 'func': irw_base_universe_d2_030_irw_042_insider_silence_1260}


def irw_base_universe_d2_031_irw_043_insider_buy_cluster_1512(irw_043_insider_buy_cluster_1512):
    return _base_universe_d2(irw_043_insider_buy_cluster_1512, 31)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_031_irw_043_insider_buy_cluster_1512'] = {'inputs': ['irw_043_insider_buy_cluster_1512'], 'func': irw_base_universe_d2_031_irw_043_insider_buy_cluster_1512}


def irw_base_universe_d2_032_irw_044_insider_net_buy_ratio_63(irw_044_insider_net_buy_ratio_63):
    return _base_universe_d2(irw_044_insider_net_buy_ratio_63, 32)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_032_irw_044_insider_net_buy_ratio_63'] = {'inputs': ['irw_044_insider_net_buy_ratio_63'], 'func': irw_base_universe_d2_032_irw_044_insider_net_buy_ratio_63}


def irw_base_universe_d2_033_irw_045_insider_value_ratio_252(irw_045_insider_value_ratio_252):
    return _base_universe_d2(irw_045_insider_value_ratio_252, 33)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_033_irw_045_insider_value_ratio_252'] = {'inputs': ['irw_045_insider_value_ratio_252'], 'func': irw_base_universe_d2_033_irw_045_insider_value_ratio_252}


def irw_base_universe_d2_034_irw_046_ceo_cfo_buy_weight_21(irw_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(irw_046_ceo_cfo_buy_weight_21, 34)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_034_irw_046_ceo_cfo_buy_weight_21'] = {'inputs': ['irw_046_ceo_cfo_buy_weight_21'], 'func': irw_base_universe_d2_034_irw_046_ceo_cfo_buy_weight_21}


def irw_base_universe_d2_035_irw_048_insider_conviction_63(irw_048_insider_conviction_63):
    return _base_universe_d2(irw_048_insider_conviction_63, 35)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_035_irw_048_insider_conviction_63'] = {'inputs': ['irw_048_insider_conviction_63'], 'func': irw_base_universe_d2_035_irw_048_insider_conviction_63}


def irw_base_universe_d2_036_irw_049_insider_silence_84(irw_049_insider_silence_84):
    return _base_universe_d2(irw_049_insider_silence_84, 36)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_036_irw_049_insider_silence_84'] = {'inputs': ['irw_049_insider_silence_84'], 'func': irw_base_universe_d2_036_irw_049_insider_silence_84}


def irw_base_universe_d2_037_irw_050_insider_buy_cluster_126(irw_050_insider_buy_cluster_126):
    return _base_universe_d2(irw_050_insider_buy_cluster_126, 37)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_037_irw_050_insider_buy_cluster_126'] = {'inputs': ['irw_050_insider_buy_cluster_126'], 'func': irw_base_universe_d2_037_irw_050_insider_buy_cluster_126}


def irw_base_universe_d2_038_irw_051_insider_net_buy_ratio_189(irw_051_insider_net_buy_ratio_189):
    return _base_universe_d2(irw_051_insider_net_buy_ratio_189, 38)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_038_irw_051_insider_net_buy_ratio_189'] = {'inputs': ['irw_051_insider_net_buy_ratio_189'], 'func': irw_base_universe_d2_038_irw_051_insider_net_buy_ratio_189}


def irw_base_universe_d2_039_irw_053_ceo_cfo_buy_weight_378(irw_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(irw_053_ceo_cfo_buy_weight_378, 39)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_039_irw_053_ceo_cfo_buy_weight_378'] = {'inputs': ['irw_053_ceo_cfo_buy_weight_378'], 'func': irw_base_universe_d2_039_irw_053_ceo_cfo_buy_weight_378}


def irw_base_universe_d2_040_irw_055_insider_conviction_756(irw_055_insider_conviction_756):
    return _base_universe_d2(irw_055_insider_conviction_756, 40)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_040_irw_055_insider_conviction_756'] = {'inputs': ['irw_055_insider_conviction_756'], 'func': irw_base_universe_d2_040_irw_055_insider_conviction_756}


def irw_base_universe_d2_041_irw_056_insider_silence_1008(irw_056_insider_silence_1008):
    return _base_universe_d2(irw_056_insider_silence_1008, 41)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_041_irw_056_insider_silence_1008'] = {'inputs': ['irw_056_insider_silence_1008'], 'func': irw_base_universe_d2_041_irw_056_insider_silence_1008}


def irw_base_universe_d2_042_irw_057_insider_buy_cluster_1260(irw_057_insider_buy_cluster_1260):
    return _base_universe_d2(irw_057_insider_buy_cluster_1260, 42)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_042_irw_057_insider_buy_cluster_1260'] = {'inputs': ['irw_057_insider_buy_cluster_1260'], 'func': irw_base_universe_d2_042_irw_057_insider_buy_cluster_1260}


def irw_base_universe_d2_043_irw_058_insider_net_buy_ratio_1512(irw_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(irw_058_insider_net_buy_ratio_1512, 43)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_043_irw_058_insider_net_buy_ratio_1512'] = {'inputs': ['irw_058_insider_net_buy_ratio_1512'], 'func': irw_base_universe_d2_043_irw_058_insider_net_buy_ratio_1512}


def irw_base_universe_d2_044_irw_060_ceo_cfo_buy_weight_252(irw_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(irw_060_ceo_cfo_buy_weight_252, 44)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_044_irw_060_ceo_cfo_buy_weight_252'] = {'inputs': ['irw_060_ceo_cfo_buy_weight_252'], 'func': irw_base_universe_d2_044_irw_060_ceo_cfo_buy_weight_252}


def irw_base_universe_d2_045_irw_062_insider_conviction_42(irw_062_insider_conviction_42):
    return _base_universe_d2(irw_062_insider_conviction_42, 45)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_045_irw_062_insider_conviction_42'] = {'inputs': ['irw_062_insider_conviction_42'], 'func': irw_base_universe_d2_045_irw_062_insider_conviction_42}


def irw_base_universe_d2_046_irw_064_insider_buy_cluster_84(irw_064_insider_buy_cluster_84):
    return _base_universe_d2(irw_064_insider_buy_cluster_84, 46)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_046_irw_064_insider_buy_cluster_84'] = {'inputs': ['irw_064_insider_buy_cluster_84'], 'func': irw_base_universe_d2_046_irw_064_insider_buy_cluster_84}


def irw_base_universe_d2_047_irw_065_insider_net_buy_ratio_126(irw_065_insider_net_buy_ratio_126):
    return _base_universe_d2(irw_065_insider_net_buy_ratio_126, 47)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_047_irw_065_insider_net_buy_ratio_126'] = {'inputs': ['irw_065_insider_net_buy_ratio_126'], 'func': irw_base_universe_d2_047_irw_065_insider_net_buy_ratio_126}


def irw_base_universe_d2_048_irw_066_insider_value_ratio_189(irw_066_insider_value_ratio_189):
    return _base_universe_d2(irw_066_insider_value_ratio_189, 48)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_048_irw_066_insider_value_ratio_189'] = {'inputs': ['irw_066_insider_value_ratio_189'], 'func': irw_base_universe_d2_048_irw_066_insider_value_ratio_189}


def irw_base_universe_d2_049_irw_069_insider_conviction_504(irw_069_insider_conviction_504):
    return _base_universe_d2(irw_069_insider_conviction_504, 49)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_049_irw_069_insider_conviction_504'] = {'inputs': ['irw_069_insider_conviction_504'], 'func': irw_base_universe_d2_049_irw_069_insider_conviction_504}


def irw_base_universe_d2_050_irw_070_insider_silence_756(irw_070_insider_silence_756):
    return _base_universe_d2(irw_070_insider_silence_756, 50)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_050_irw_070_insider_silence_756'] = {'inputs': ['irw_070_insider_silence_756'], 'func': irw_base_universe_d2_050_irw_070_insider_silence_756}


def irw_base_universe_d2_051_irw_071_insider_buy_cluster_1008(irw_071_insider_buy_cluster_1008):
    return _base_universe_d2(irw_071_insider_buy_cluster_1008, 51)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_051_irw_071_insider_buy_cluster_1008'] = {'inputs': ['irw_071_insider_buy_cluster_1008'], 'func': irw_base_universe_d2_051_irw_071_insider_buy_cluster_1008}


def irw_base_universe_d2_052_irw_072_insider_net_buy_ratio_1260(irw_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(irw_072_insider_net_buy_ratio_1260, 52)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_052_irw_072_insider_net_buy_ratio_1260'] = {'inputs': ['irw_072_insider_net_buy_ratio_1260'], 'func': irw_base_universe_d2_052_irw_072_insider_net_buy_ratio_1260}


def irw_base_universe_d2_053_irw_073_insider_value_ratio_1512(irw_073_insider_value_ratio_1512):
    return _base_universe_d2(irw_073_insider_value_ratio_1512, 53)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_053_irw_073_insider_value_ratio_1512'] = {'inputs': ['irw_073_insider_value_ratio_1512'], 'func': irw_base_universe_d2_053_irw_073_insider_value_ratio_1512}


def irw_base_universe_d2_054_irw_basefill_005(irw_basefill_005):
    return _base_universe_d2(irw_basefill_005, 54)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_054_irw_basefill_005'] = {'inputs': ['irw_basefill_005'], 'func': irw_base_universe_d2_054_irw_basefill_005}


def irw_base_universe_d2_055_irw_basefill_012(irw_basefill_012):
    return _base_universe_d2(irw_basefill_012, 55)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_055_irw_basefill_012'] = {'inputs': ['irw_basefill_012'], 'func': irw_base_universe_d2_055_irw_basefill_012}


def irw_base_universe_d2_056_irw_basefill_019(irw_basefill_019):
    return _base_universe_d2(irw_basefill_019, 56)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_056_irw_basefill_019'] = {'inputs': ['irw_basefill_019'], 'func': irw_base_universe_d2_056_irw_basefill_019}


def irw_base_universe_d2_057_irw_basefill_022(irw_basefill_022):
    return _base_universe_d2(irw_basefill_022, 57)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_057_irw_basefill_022'] = {'inputs': ['irw_basefill_022'], 'func': irw_base_universe_d2_057_irw_basefill_022}


def irw_base_universe_d2_058_irw_basefill_026(irw_basefill_026):
    return _base_universe_d2(irw_basefill_026, 58)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_058_irw_basefill_026'] = {'inputs': ['irw_basefill_026'], 'func': irw_base_universe_d2_058_irw_basefill_026}


def irw_base_universe_d2_059_irw_basefill_033(irw_basefill_033):
    return _base_universe_d2(irw_basefill_033, 59)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_059_irw_basefill_033'] = {'inputs': ['irw_basefill_033'], 'func': irw_base_universe_d2_059_irw_basefill_033}


def irw_base_universe_d2_060_irw_basefill_037(irw_basefill_037):
    return _base_universe_d2(irw_basefill_037, 60)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_060_irw_basefill_037'] = {'inputs': ['irw_basefill_037'], 'func': irw_base_universe_d2_060_irw_basefill_037}


def irw_base_universe_d2_061_irw_basefill_040(irw_basefill_040):
    return _base_universe_d2(irw_basefill_040, 61)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_061_irw_basefill_040'] = {'inputs': ['irw_basefill_040'], 'func': irw_base_universe_d2_061_irw_basefill_040}


def irw_base_universe_d2_062_irw_basefill_047(irw_basefill_047):
    return _base_universe_d2(irw_basefill_047, 62)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_062_irw_basefill_047'] = {'inputs': ['irw_basefill_047'], 'func': irw_base_universe_d2_062_irw_basefill_047}


def irw_base_universe_d2_063_irw_basefill_052(irw_basefill_052):
    return _base_universe_d2(irw_basefill_052, 63)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_063_irw_basefill_052'] = {'inputs': ['irw_basefill_052'], 'func': irw_base_universe_d2_063_irw_basefill_052}


def irw_base_universe_d2_064_irw_basefill_054(irw_basefill_054):
    return _base_universe_d2(irw_basefill_054, 64)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_064_irw_basefill_054'] = {'inputs': ['irw_basefill_054'], 'func': irw_base_universe_d2_064_irw_basefill_054}


def irw_base_universe_d2_065_irw_basefill_059(irw_basefill_059):
    return _base_universe_d2(irw_basefill_059, 65)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_065_irw_basefill_059'] = {'inputs': ['irw_basefill_059'], 'func': irw_base_universe_d2_065_irw_basefill_059}


def irw_base_universe_d2_066_irw_basefill_061(irw_basefill_061):
    return _base_universe_d2(irw_basefill_061, 66)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_066_irw_basefill_061'] = {'inputs': ['irw_basefill_061'], 'func': irw_base_universe_d2_066_irw_basefill_061}


def irw_base_universe_d2_067_irw_basefill_063(irw_basefill_063):
    return _base_universe_d2(irw_basefill_063, 67)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_067_irw_basefill_063'] = {'inputs': ['irw_basefill_063'], 'func': irw_base_universe_d2_067_irw_basefill_063}


def irw_base_universe_d2_068_irw_basefill_067(irw_basefill_067):
    return _base_universe_d2(irw_basefill_067, 68)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_068_irw_basefill_067'] = {'inputs': ['irw_basefill_067'], 'func': irw_base_universe_d2_068_irw_basefill_067}


def irw_base_universe_d2_069_irw_basefill_068(irw_basefill_068):
    return _base_universe_d2(irw_basefill_068, 69)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_069_irw_basefill_068'] = {'inputs': ['irw_basefill_068'], 'func': irw_base_universe_d2_069_irw_basefill_068}


def irw_base_universe_d2_070_irw_basefill_074(irw_basefill_074):
    return _base_universe_d2(irw_basefill_074, 70)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_070_irw_basefill_074'] = {'inputs': ['irw_basefill_074'], 'func': irw_base_universe_d2_070_irw_basefill_074}


def irw_base_universe_d2_071_irw_basefill_075(irw_basefill_075):
    return _base_universe_d2(irw_basefill_075, 71)
IRW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['irw_base_universe_d2_071_irw_basefill_075'] = {'inputs': ['irw_basefill_075'], 'func': irw_base_universe_d2_071_irw_basefill_075}
