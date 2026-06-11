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



def itf_176_itf_001_insider_buy_cluster_21_accel_1(itf_151_itf_001_insider_buy_cluster_21_roc_1):
    feature = _s(itf_151_itf_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def itf_177_itf_007_insider_silence_252_accel_42(itf_152_itf_007_insider_silence_252_roc_42):
    feature = _s(itf_152_itf_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def itf_178_itf_013_insider_conviction_1512_accel_126(itf_153_itf_013_insider_conviction_1512_roc_126):
    feature = _s(itf_153_itf_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def itf_179_itf_019_insider_activity_accel_1_accel_378(itf_154_itf_019_insider_activity_accel_1_roc_378):
    feature = _s(itf_154_itf_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def itf_180_itf_025_ceo_cfo_buy_weight_756_accel_4(itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_TRANSACTION_FREQ_REGISTRY_3RD_DERIVATIVES = {
    'itf_176_itf_001_insider_buy_cluster_21_accel_1': {'inputs': ['itf_151_itf_001_insider_buy_cluster_21_roc_1'], 'func': itf_176_itf_001_insider_buy_cluster_21_accel_1},
    'itf_177_itf_007_insider_silence_252_accel_42': {'inputs': ['itf_152_itf_007_insider_silence_252_roc_42'], 'func': itf_177_itf_007_insider_silence_252_accel_42},
    'itf_178_itf_013_insider_conviction_1512_accel_126': {'inputs': ['itf_153_itf_013_insider_conviction_1512_roc_126'], 'func': itf_178_itf_013_insider_conviction_1512_accel_126},
    'itf_179_itf_019_insider_activity_accel_1_accel_378': {'inputs': ['itf_154_itf_019_insider_activity_accel_1_roc_378'], 'func': itf_179_itf_019_insider_activity_accel_1_accel_378},
    'itf_180_itf_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['itf_155_itf_025_ceo_cfo_buy_weight_756_roc_4'], 'func': itf_180_itf_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def itf_replacement_d3_001(itf_replacement_d2_001):
    feature = _clean(itf_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_001'] = {'inputs': ['itf_replacement_d2_001'], 'func': itf_replacement_d3_001}


def itf_replacement_d3_002(itf_replacement_d2_002):
    feature = _clean(itf_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_002'] = {'inputs': ['itf_replacement_d2_002'], 'func': itf_replacement_d3_002}


def itf_replacement_d3_003(itf_replacement_d2_003):
    feature = _clean(itf_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_003'] = {'inputs': ['itf_replacement_d2_003'], 'func': itf_replacement_d3_003}


def itf_replacement_d3_004(itf_replacement_d2_004):
    feature = _clean(itf_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_004'] = {'inputs': ['itf_replacement_d2_004'], 'func': itf_replacement_d3_004}


def itf_replacement_d3_005(itf_replacement_d2_005):
    feature = _clean(itf_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_005'] = {'inputs': ['itf_replacement_d2_005'], 'func': itf_replacement_d3_005}


def itf_replacement_d3_006(itf_replacement_d2_006):
    feature = _clean(itf_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_006'] = {'inputs': ['itf_replacement_d2_006'], 'func': itf_replacement_d3_006}


def itf_replacement_d3_007(itf_replacement_d2_007):
    feature = _clean(itf_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_007'] = {'inputs': ['itf_replacement_d2_007'], 'func': itf_replacement_d3_007}


def itf_replacement_d3_008(itf_replacement_d2_008):
    feature = _clean(itf_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_008'] = {'inputs': ['itf_replacement_d2_008'], 'func': itf_replacement_d3_008}


def itf_replacement_d3_009(itf_replacement_d2_009):
    feature = _clean(itf_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_009'] = {'inputs': ['itf_replacement_d2_009'], 'func': itf_replacement_d3_009}


def itf_replacement_d3_010(itf_replacement_d2_010):
    feature = _clean(itf_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_010'] = {'inputs': ['itf_replacement_d2_010'], 'func': itf_replacement_d3_010}


def itf_replacement_d3_011(itf_replacement_d2_011):
    feature = _clean(itf_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_011'] = {'inputs': ['itf_replacement_d2_011'], 'func': itf_replacement_d3_011}


def itf_replacement_d3_012(itf_replacement_d2_012):
    feature = _clean(itf_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_012'] = {'inputs': ['itf_replacement_d2_012'], 'func': itf_replacement_d3_012}


def itf_replacement_d3_013(itf_replacement_d2_013):
    feature = _clean(itf_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_013'] = {'inputs': ['itf_replacement_d2_013'], 'func': itf_replacement_d3_013}


def itf_replacement_d3_014(itf_replacement_d2_014):
    feature = _clean(itf_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_014'] = {'inputs': ['itf_replacement_d2_014'], 'func': itf_replacement_d3_014}


def itf_replacement_d3_015(itf_replacement_d2_015):
    feature = _clean(itf_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_015'] = {'inputs': ['itf_replacement_d2_015'], 'func': itf_replacement_d3_015}


def itf_replacement_d3_016(itf_replacement_d2_016):
    feature = _clean(itf_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_016'] = {'inputs': ['itf_replacement_d2_016'], 'func': itf_replacement_d3_016}


def itf_replacement_d3_017(itf_replacement_d2_017):
    feature = _clean(itf_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_017'] = {'inputs': ['itf_replacement_d2_017'], 'func': itf_replacement_d3_017}


def itf_replacement_d3_018(itf_replacement_d2_018):
    feature = _clean(itf_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_018'] = {'inputs': ['itf_replacement_d2_018'], 'func': itf_replacement_d3_018}


def itf_replacement_d3_019(itf_replacement_d2_019):
    feature = _clean(itf_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_019'] = {'inputs': ['itf_replacement_d2_019'], 'func': itf_replacement_d3_019}


def itf_replacement_d3_020(itf_replacement_d2_020):
    feature = _clean(itf_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_020'] = {'inputs': ['itf_replacement_d2_020'], 'func': itf_replacement_d3_020}


def itf_replacement_d3_021(itf_replacement_d2_021):
    feature = _clean(itf_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_021'] = {'inputs': ['itf_replacement_d2_021'], 'func': itf_replacement_d3_021}


def itf_replacement_d3_022(itf_replacement_d2_022):
    feature = _clean(itf_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_022'] = {'inputs': ['itf_replacement_d2_022'], 'func': itf_replacement_d3_022}


def itf_replacement_d3_023(itf_replacement_d2_023):
    feature = _clean(itf_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_023'] = {'inputs': ['itf_replacement_d2_023'], 'func': itf_replacement_d3_023}


def itf_replacement_d3_024(itf_replacement_d2_024):
    feature = _clean(itf_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_024'] = {'inputs': ['itf_replacement_d2_024'], 'func': itf_replacement_d3_024}


def itf_replacement_d3_025(itf_replacement_d2_025):
    feature = _clean(itf_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_025'] = {'inputs': ['itf_replacement_d2_025'], 'func': itf_replacement_d3_025}


def itf_replacement_d3_026(itf_replacement_d2_026):
    feature = _clean(itf_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_026'] = {'inputs': ['itf_replacement_d2_026'], 'func': itf_replacement_d3_026}


def itf_replacement_d3_027(itf_replacement_d2_027):
    feature = _clean(itf_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_027'] = {'inputs': ['itf_replacement_d2_027'], 'func': itf_replacement_d3_027}


def itf_replacement_d3_028(itf_replacement_d2_028):
    feature = _clean(itf_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_028'] = {'inputs': ['itf_replacement_d2_028'], 'func': itf_replacement_d3_028}


def itf_replacement_d3_029(itf_replacement_d2_029):
    feature = _clean(itf_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_029'] = {'inputs': ['itf_replacement_d2_029'], 'func': itf_replacement_d3_029}


def itf_replacement_d3_030(itf_replacement_d2_030):
    feature = _clean(itf_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_030'] = {'inputs': ['itf_replacement_d2_030'], 'func': itf_replacement_d3_030}


def itf_replacement_d3_031(itf_replacement_d2_031):
    feature = _clean(itf_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_031'] = {'inputs': ['itf_replacement_d2_031'], 'func': itf_replacement_d3_031}


def itf_replacement_d3_032(itf_replacement_d2_032):
    feature = _clean(itf_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_032'] = {'inputs': ['itf_replacement_d2_032'], 'func': itf_replacement_d3_032}


def itf_replacement_d3_033(itf_replacement_d2_033):
    feature = _clean(itf_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_033'] = {'inputs': ['itf_replacement_d2_033'], 'func': itf_replacement_d3_033}


def itf_replacement_d3_034(itf_replacement_d2_034):
    feature = _clean(itf_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_034'] = {'inputs': ['itf_replacement_d2_034'], 'func': itf_replacement_d3_034}


def itf_replacement_d3_035(itf_replacement_d2_035):
    feature = _clean(itf_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_035'] = {'inputs': ['itf_replacement_d2_035'], 'func': itf_replacement_d3_035}


def itf_replacement_d3_036(itf_replacement_d2_036):
    feature = _clean(itf_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_036'] = {'inputs': ['itf_replacement_d2_036'], 'func': itf_replacement_d3_036}


def itf_replacement_d3_037(itf_replacement_d2_037):
    feature = _clean(itf_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_037'] = {'inputs': ['itf_replacement_d2_037'], 'func': itf_replacement_d3_037}


def itf_replacement_d3_038(itf_replacement_d2_038):
    feature = _clean(itf_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_038'] = {'inputs': ['itf_replacement_d2_038'], 'func': itf_replacement_d3_038}


def itf_replacement_d3_039(itf_replacement_d2_039):
    feature = _clean(itf_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_039'] = {'inputs': ['itf_replacement_d2_039'], 'func': itf_replacement_d3_039}


def itf_replacement_d3_040(itf_replacement_d2_040):
    feature = _clean(itf_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_040'] = {'inputs': ['itf_replacement_d2_040'], 'func': itf_replacement_d3_040}


def itf_replacement_d3_041(itf_replacement_d2_041):
    feature = _clean(itf_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_041'] = {'inputs': ['itf_replacement_d2_041'], 'func': itf_replacement_d3_041}


def itf_replacement_d3_042(itf_replacement_d2_042):
    feature = _clean(itf_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_042'] = {'inputs': ['itf_replacement_d2_042'], 'func': itf_replacement_d3_042}


def itf_replacement_d3_043(itf_replacement_d2_043):
    feature = _clean(itf_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_043'] = {'inputs': ['itf_replacement_d2_043'], 'func': itf_replacement_d3_043}


def itf_replacement_d3_044(itf_replacement_d2_044):
    feature = _clean(itf_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_044'] = {'inputs': ['itf_replacement_d2_044'], 'func': itf_replacement_d3_044}


def itf_replacement_d3_045(itf_replacement_d2_045):
    feature = _clean(itf_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_045'] = {'inputs': ['itf_replacement_d2_045'], 'func': itf_replacement_d3_045}


def itf_replacement_d3_046(itf_replacement_d2_046):
    feature = _clean(itf_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_046'] = {'inputs': ['itf_replacement_d2_046'], 'func': itf_replacement_d3_046}


def itf_replacement_d3_047(itf_replacement_d2_047):
    feature = _clean(itf_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_047'] = {'inputs': ['itf_replacement_d2_047'], 'func': itf_replacement_d3_047}


def itf_replacement_d3_048(itf_replacement_d2_048):
    feature = _clean(itf_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_048'] = {'inputs': ['itf_replacement_d2_048'], 'func': itf_replacement_d3_048}


def itf_replacement_d3_049(itf_replacement_d2_049):
    feature = _clean(itf_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_049'] = {'inputs': ['itf_replacement_d2_049'], 'func': itf_replacement_d3_049}


def itf_replacement_d3_050(itf_replacement_d2_050):
    feature = _clean(itf_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_050'] = {'inputs': ['itf_replacement_d2_050'], 'func': itf_replacement_d3_050}


def itf_replacement_d3_051(itf_replacement_d2_051):
    feature = _clean(itf_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_051'] = {'inputs': ['itf_replacement_d2_051'], 'func': itf_replacement_d3_051}


def itf_replacement_d3_052(itf_replacement_d2_052):
    feature = _clean(itf_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_052'] = {'inputs': ['itf_replacement_d2_052'], 'func': itf_replacement_d3_052}


def itf_replacement_d3_053(itf_replacement_d2_053):
    feature = _clean(itf_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_053'] = {'inputs': ['itf_replacement_d2_053'], 'func': itf_replacement_d3_053}


def itf_replacement_d3_054(itf_replacement_d2_054):
    feature = _clean(itf_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_054'] = {'inputs': ['itf_replacement_d2_054'], 'func': itf_replacement_d3_054}


def itf_replacement_d3_055(itf_replacement_d2_055):
    feature = _clean(itf_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_055'] = {'inputs': ['itf_replacement_d2_055'], 'func': itf_replacement_d3_055}


def itf_replacement_d3_056(itf_replacement_d2_056):
    feature = _clean(itf_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_056'] = {'inputs': ['itf_replacement_d2_056'], 'func': itf_replacement_d3_056}


def itf_replacement_d3_057(itf_replacement_d2_057):
    feature = _clean(itf_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_057'] = {'inputs': ['itf_replacement_d2_057'], 'func': itf_replacement_d3_057}


def itf_replacement_d3_058(itf_replacement_d2_058):
    feature = _clean(itf_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_058'] = {'inputs': ['itf_replacement_d2_058'], 'func': itf_replacement_d3_058}


def itf_replacement_d3_059(itf_replacement_d2_059):
    feature = _clean(itf_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_059'] = {'inputs': ['itf_replacement_d2_059'], 'func': itf_replacement_d3_059}


def itf_replacement_d3_060(itf_replacement_d2_060):
    feature = _clean(itf_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_060'] = {'inputs': ['itf_replacement_d2_060'], 'func': itf_replacement_d3_060}


def itf_replacement_d3_061(itf_replacement_d2_061):
    feature = _clean(itf_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_061'] = {'inputs': ['itf_replacement_d2_061'], 'func': itf_replacement_d3_061}


def itf_replacement_d3_062(itf_replacement_d2_062):
    feature = _clean(itf_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_062'] = {'inputs': ['itf_replacement_d2_062'], 'func': itf_replacement_d3_062}


def itf_replacement_d3_063(itf_replacement_d2_063):
    feature = _clean(itf_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_063'] = {'inputs': ['itf_replacement_d2_063'], 'func': itf_replacement_d3_063}


def itf_replacement_d3_064(itf_replacement_d2_064):
    feature = _clean(itf_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_064'] = {'inputs': ['itf_replacement_d2_064'], 'func': itf_replacement_d3_064}


def itf_replacement_d3_065(itf_replacement_d2_065):
    feature = _clean(itf_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_065'] = {'inputs': ['itf_replacement_d2_065'], 'func': itf_replacement_d3_065}


def itf_replacement_d3_066(itf_replacement_d2_066):
    feature = _clean(itf_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_066'] = {'inputs': ['itf_replacement_d2_066'], 'func': itf_replacement_d3_066}


def itf_replacement_d3_067(itf_replacement_d2_067):
    feature = _clean(itf_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_067'] = {'inputs': ['itf_replacement_d2_067'], 'func': itf_replacement_d3_067}


def itf_replacement_d3_068(itf_replacement_d2_068):
    feature = _clean(itf_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_068'] = {'inputs': ['itf_replacement_d2_068'], 'func': itf_replacement_d3_068}


def itf_replacement_d3_069(itf_replacement_d2_069):
    feature = _clean(itf_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_069'] = {'inputs': ['itf_replacement_d2_069'], 'func': itf_replacement_d3_069}


def itf_replacement_d3_070(itf_replacement_d2_070):
    feature = _clean(itf_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_070'] = {'inputs': ['itf_replacement_d2_070'], 'func': itf_replacement_d3_070}


def itf_replacement_d3_071(itf_replacement_d2_071):
    feature = _clean(itf_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_071'] = {'inputs': ['itf_replacement_d2_071'], 'func': itf_replacement_d3_071}


def itf_replacement_d3_072(itf_replacement_d2_072):
    feature = _clean(itf_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_072'] = {'inputs': ['itf_replacement_d2_072'], 'func': itf_replacement_d3_072}


def itf_replacement_d3_073(itf_replacement_d2_073):
    feature = _clean(itf_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_073'] = {'inputs': ['itf_replacement_d2_073'], 'func': itf_replacement_d3_073}


def itf_replacement_d3_074(itf_replacement_d2_074):
    feature = _clean(itf_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_074'] = {'inputs': ['itf_replacement_d2_074'], 'func': itf_replacement_d3_074}


def itf_replacement_d3_075(itf_replacement_d2_075):
    feature = _clean(itf_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_075'] = {'inputs': ['itf_replacement_d2_075'], 'func': itf_replacement_d3_075}


def itf_replacement_d3_076(itf_replacement_d2_076):
    feature = _clean(itf_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_076'] = {'inputs': ['itf_replacement_d2_076'], 'func': itf_replacement_d3_076}


def itf_replacement_d3_077(itf_replacement_d2_077):
    feature = _clean(itf_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_077'] = {'inputs': ['itf_replacement_d2_077'], 'func': itf_replacement_d3_077}


def itf_replacement_d3_078(itf_replacement_d2_078):
    feature = _clean(itf_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_078'] = {'inputs': ['itf_replacement_d2_078'], 'func': itf_replacement_d3_078}


def itf_replacement_d3_079(itf_replacement_d2_079):
    feature = _clean(itf_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_079'] = {'inputs': ['itf_replacement_d2_079'], 'func': itf_replacement_d3_079}


def itf_replacement_d3_080(itf_replacement_d2_080):
    feature = _clean(itf_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_080'] = {'inputs': ['itf_replacement_d2_080'], 'func': itf_replacement_d3_080}


def itf_replacement_d3_081(itf_replacement_d2_081):
    feature = _clean(itf_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_081'] = {'inputs': ['itf_replacement_d2_081'], 'func': itf_replacement_d3_081}


def itf_replacement_d3_082(itf_replacement_d2_082):
    feature = _clean(itf_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_082'] = {'inputs': ['itf_replacement_d2_082'], 'func': itf_replacement_d3_082}


def itf_replacement_d3_083(itf_replacement_d2_083):
    feature = _clean(itf_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_083'] = {'inputs': ['itf_replacement_d2_083'], 'func': itf_replacement_d3_083}


def itf_replacement_d3_084(itf_replacement_d2_084):
    feature = _clean(itf_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_084'] = {'inputs': ['itf_replacement_d2_084'], 'func': itf_replacement_d3_084}


def itf_replacement_d3_085(itf_replacement_d2_085):
    feature = _clean(itf_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_085'] = {'inputs': ['itf_replacement_d2_085'], 'func': itf_replacement_d3_085}


def itf_replacement_d3_086(itf_replacement_d2_086):
    feature = _clean(itf_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_086'] = {'inputs': ['itf_replacement_d2_086'], 'func': itf_replacement_d3_086}


def itf_replacement_d3_087(itf_replacement_d2_087):
    feature = _clean(itf_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_087'] = {'inputs': ['itf_replacement_d2_087'], 'func': itf_replacement_d3_087}


def itf_replacement_d3_088(itf_replacement_d2_088):
    feature = _clean(itf_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_088'] = {'inputs': ['itf_replacement_d2_088'], 'func': itf_replacement_d3_088}


def itf_replacement_d3_089(itf_replacement_d2_089):
    feature = _clean(itf_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_089'] = {'inputs': ['itf_replacement_d2_089'], 'func': itf_replacement_d3_089}


def itf_replacement_d3_090(itf_replacement_d2_090):
    feature = _clean(itf_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_090'] = {'inputs': ['itf_replacement_d2_090'], 'func': itf_replacement_d3_090}


def itf_replacement_d3_091(itf_replacement_d2_091):
    feature = _clean(itf_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_091'] = {'inputs': ['itf_replacement_d2_091'], 'func': itf_replacement_d3_091}


def itf_replacement_d3_092(itf_replacement_d2_092):
    feature = _clean(itf_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_092'] = {'inputs': ['itf_replacement_d2_092'], 'func': itf_replacement_d3_092}


def itf_replacement_d3_093(itf_replacement_d2_093):
    feature = _clean(itf_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_093'] = {'inputs': ['itf_replacement_d2_093'], 'func': itf_replacement_d3_093}


def itf_replacement_d3_094(itf_replacement_d2_094):
    feature = _clean(itf_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_094'] = {'inputs': ['itf_replacement_d2_094'], 'func': itf_replacement_d3_094}


def itf_replacement_d3_095(itf_replacement_d2_095):
    feature = _clean(itf_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_095'] = {'inputs': ['itf_replacement_d2_095'], 'func': itf_replacement_d3_095}


def itf_replacement_d3_096(itf_replacement_d2_096):
    feature = _clean(itf_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_096'] = {'inputs': ['itf_replacement_d2_096'], 'func': itf_replacement_d3_096}


def itf_replacement_d3_097(itf_replacement_d2_097):
    feature = _clean(itf_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_097'] = {'inputs': ['itf_replacement_d2_097'], 'func': itf_replacement_d3_097}


def itf_replacement_d3_098(itf_replacement_d2_098):
    feature = _clean(itf_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_098'] = {'inputs': ['itf_replacement_d2_098'], 'func': itf_replacement_d3_098}


def itf_replacement_d3_099(itf_replacement_d2_099):
    feature = _clean(itf_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_099'] = {'inputs': ['itf_replacement_d2_099'], 'func': itf_replacement_d3_099}


def itf_replacement_d3_100(itf_replacement_d2_100):
    feature = _clean(itf_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_100'] = {'inputs': ['itf_replacement_d2_100'], 'func': itf_replacement_d3_100}


def itf_replacement_d3_101(itf_replacement_d2_101):
    feature = _clean(itf_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_101'] = {'inputs': ['itf_replacement_d2_101'], 'func': itf_replacement_d3_101}


def itf_replacement_d3_102(itf_replacement_d2_102):
    feature = _clean(itf_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_102'] = {'inputs': ['itf_replacement_d2_102'], 'func': itf_replacement_d3_102}


def itf_replacement_d3_103(itf_replacement_d2_103):
    feature = _clean(itf_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_103'] = {'inputs': ['itf_replacement_d2_103'], 'func': itf_replacement_d3_103}


def itf_replacement_d3_104(itf_replacement_d2_104):
    feature = _clean(itf_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_104'] = {'inputs': ['itf_replacement_d2_104'], 'func': itf_replacement_d3_104}


def itf_replacement_d3_105(itf_replacement_d2_105):
    feature = _clean(itf_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_105'] = {'inputs': ['itf_replacement_d2_105'], 'func': itf_replacement_d3_105}


def itf_replacement_d3_106(itf_replacement_d2_106):
    feature = _clean(itf_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_106'] = {'inputs': ['itf_replacement_d2_106'], 'func': itf_replacement_d3_106}


def itf_replacement_d3_107(itf_replacement_d2_107):
    feature = _clean(itf_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_107'] = {'inputs': ['itf_replacement_d2_107'], 'func': itf_replacement_d3_107}


def itf_replacement_d3_108(itf_replacement_d2_108):
    feature = _clean(itf_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_108'] = {'inputs': ['itf_replacement_d2_108'], 'func': itf_replacement_d3_108}


def itf_replacement_d3_109(itf_replacement_d2_109):
    feature = _clean(itf_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_109'] = {'inputs': ['itf_replacement_d2_109'], 'func': itf_replacement_d3_109}


def itf_replacement_d3_110(itf_replacement_d2_110):
    feature = _clean(itf_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_110'] = {'inputs': ['itf_replacement_d2_110'], 'func': itf_replacement_d3_110}


def itf_replacement_d3_111(itf_replacement_d2_111):
    feature = _clean(itf_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_111'] = {'inputs': ['itf_replacement_d2_111'], 'func': itf_replacement_d3_111}


def itf_replacement_d3_112(itf_replacement_d2_112):
    feature = _clean(itf_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
ITF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['itf_replacement_d3_112'] = {'inputs': ['itf_replacement_d2_112'], 'func': itf_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def itf_base_universe_d3_001_itf_002_insider_net_buy_ratio_42(itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42):
    return _base_universe_d3(itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42, 1)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_001_itf_002_insider_net_buy_ratio_42'] = {'inputs': ['itf_base_universe_d2_001_itf_002_insider_net_buy_ratio_42'], 'func': itf_base_universe_d3_001_itf_002_insider_net_buy_ratio_42}


def itf_base_universe_d3_002_itf_003_insider_value_ratio_63(itf_base_universe_d2_002_itf_003_insider_value_ratio_63):
    return _base_universe_d3(itf_base_universe_d2_002_itf_003_insider_value_ratio_63, 2)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_002_itf_003_insider_value_ratio_63'] = {'inputs': ['itf_base_universe_d2_002_itf_003_insider_value_ratio_63'], 'func': itf_base_universe_d3_002_itf_003_insider_value_ratio_63}


def itf_base_universe_d3_003_itf_004_ceo_cfo_buy_weight_84(itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84, 3)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_003_itf_004_ceo_cfo_buy_weight_84'] = {'inputs': ['itf_base_universe_d2_003_itf_004_ceo_cfo_buy_weight_84'], 'func': itf_base_universe_d3_003_itf_004_ceo_cfo_buy_weight_84}


def itf_base_universe_d3_004_itf_006_insider_conviction_189(itf_base_universe_d2_004_itf_006_insider_conviction_189):
    return _base_universe_d3(itf_base_universe_d2_004_itf_006_insider_conviction_189, 4)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_004_itf_006_insider_conviction_189'] = {'inputs': ['itf_base_universe_d2_004_itf_006_insider_conviction_189'], 'func': itf_base_universe_d3_004_itf_006_insider_conviction_189}


def itf_base_universe_d3_005_itf_008_insider_buy_cluster_378(itf_base_universe_d2_005_itf_008_insider_buy_cluster_378):
    return _base_universe_d3(itf_base_universe_d2_005_itf_008_insider_buy_cluster_378, 5)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_005_itf_008_insider_buy_cluster_378'] = {'inputs': ['itf_base_universe_d2_005_itf_008_insider_buy_cluster_378'], 'func': itf_base_universe_d3_005_itf_008_insider_buy_cluster_378}


def itf_base_universe_d3_006_itf_009_insider_net_buy_ratio_504(itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504):
    return _base_universe_d3(itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504, 6)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_006_itf_009_insider_net_buy_ratio_504'] = {'inputs': ['itf_base_universe_d2_006_itf_009_insider_net_buy_ratio_504'], 'func': itf_base_universe_d3_006_itf_009_insider_net_buy_ratio_504}


def itf_base_universe_d3_007_itf_010_insider_value_ratio_756(itf_base_universe_d2_007_itf_010_insider_value_ratio_756):
    return _base_universe_d3(itf_base_universe_d2_007_itf_010_insider_value_ratio_756, 7)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_007_itf_010_insider_value_ratio_756'] = {'inputs': ['itf_base_universe_d2_007_itf_010_insider_value_ratio_756'], 'func': itf_base_universe_d3_007_itf_010_insider_value_ratio_756}


def itf_base_universe_d3_008_itf_011_ceo_cfo_buy_weight_1008(itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008, 8)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_008_itf_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['itf_base_universe_d2_008_itf_011_ceo_cfo_buy_weight_1008'], 'func': itf_base_universe_d3_008_itf_011_ceo_cfo_buy_weight_1008}


def itf_base_universe_d3_009_itf_014_insider_silence_63(itf_base_universe_d2_009_itf_014_insider_silence_63):
    return _base_universe_d3(itf_base_universe_d2_009_itf_014_insider_silence_63, 9)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_009_itf_014_insider_silence_63'] = {'inputs': ['itf_base_universe_d2_009_itf_014_insider_silence_63'], 'func': itf_base_universe_d3_009_itf_014_insider_silence_63}


def itf_base_universe_d3_010_itf_015_insider_buy_cluster_252(itf_base_universe_d2_010_itf_015_insider_buy_cluster_252):
    return _base_universe_d3(itf_base_universe_d2_010_itf_015_insider_buy_cluster_252, 10)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_010_itf_015_insider_buy_cluster_252'] = {'inputs': ['itf_base_universe_d2_010_itf_015_insider_buy_cluster_252'], 'func': itf_base_universe_d3_010_itf_015_insider_buy_cluster_252}


def itf_base_universe_d3_011_itf_016_insider_net_buy_ratio_21(itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21):
    return _base_universe_d3(itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21, 11)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_011_itf_016_insider_net_buy_ratio_21'] = {'inputs': ['itf_base_universe_d2_011_itf_016_insider_net_buy_ratio_21'], 'func': itf_base_universe_d3_011_itf_016_insider_net_buy_ratio_21}


def itf_base_universe_d3_012_itf_017_insider_value_ratio_42(itf_base_universe_d2_012_itf_017_insider_value_ratio_42):
    return _base_universe_d3(itf_base_universe_d2_012_itf_017_insider_value_ratio_42, 12)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_012_itf_017_insider_value_ratio_42'] = {'inputs': ['itf_base_universe_d2_012_itf_017_insider_value_ratio_42'], 'func': itf_base_universe_d3_012_itf_017_insider_value_ratio_42}


def itf_base_universe_d3_013_itf_018_ceo_cfo_buy_weight_63(itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63, 13)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_013_itf_018_ceo_cfo_buy_weight_63'] = {'inputs': ['itf_base_universe_d2_013_itf_018_ceo_cfo_buy_weight_63'], 'func': itf_base_universe_d3_013_itf_018_ceo_cfo_buy_weight_63}


def itf_base_universe_d3_014_itf_020_insider_conviction_126(itf_base_universe_d2_014_itf_020_insider_conviction_126):
    return _base_universe_d3(itf_base_universe_d2_014_itf_020_insider_conviction_126, 14)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_014_itf_020_insider_conviction_126'] = {'inputs': ['itf_base_universe_d2_014_itf_020_insider_conviction_126'], 'func': itf_base_universe_d3_014_itf_020_insider_conviction_126}


def itf_base_universe_d3_015_itf_021_insider_silence_189(itf_base_universe_d2_015_itf_021_insider_silence_189):
    return _base_universe_d3(itf_base_universe_d2_015_itf_021_insider_silence_189, 15)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_015_itf_021_insider_silence_189'] = {'inputs': ['itf_base_universe_d2_015_itf_021_insider_silence_189'], 'func': itf_base_universe_d3_015_itf_021_insider_silence_189}


def itf_base_universe_d3_016_itf_023_insider_net_buy_ratio_378(itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378):
    return _base_universe_d3(itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378, 16)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_016_itf_023_insider_net_buy_ratio_378'] = {'inputs': ['itf_base_universe_d2_016_itf_023_insider_net_buy_ratio_378'], 'func': itf_base_universe_d3_016_itf_023_insider_net_buy_ratio_378}


def itf_base_universe_d3_017_itf_024_insider_value_ratio_504(itf_base_universe_d2_017_itf_024_insider_value_ratio_504):
    return _base_universe_d3(itf_base_universe_d2_017_itf_024_insider_value_ratio_504, 17)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_017_itf_024_insider_value_ratio_504'] = {'inputs': ['itf_base_universe_d2_017_itf_024_insider_value_ratio_504'], 'func': itf_base_universe_d3_017_itf_024_insider_value_ratio_504}


def itf_base_universe_d3_018_itf_027_insider_conviction_1260(itf_base_universe_d2_018_itf_027_insider_conviction_1260):
    return _base_universe_d3(itf_base_universe_d2_018_itf_027_insider_conviction_1260, 18)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_018_itf_027_insider_conviction_1260'] = {'inputs': ['itf_base_universe_d2_018_itf_027_insider_conviction_1260'], 'func': itf_base_universe_d3_018_itf_027_insider_conviction_1260}


def itf_base_universe_d3_019_itf_028_insider_silence_1512(itf_base_universe_d2_019_itf_028_insider_silence_1512):
    return _base_universe_d3(itf_base_universe_d2_019_itf_028_insider_silence_1512, 19)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_019_itf_028_insider_silence_1512'] = {'inputs': ['itf_base_universe_d2_019_itf_028_insider_silence_1512'], 'func': itf_base_universe_d3_019_itf_028_insider_silence_1512}


def itf_base_universe_d3_020_itf_029_insider_buy_cluster_63(itf_base_universe_d2_020_itf_029_insider_buy_cluster_63):
    return _base_universe_d3(itf_base_universe_d2_020_itf_029_insider_buy_cluster_63, 20)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_020_itf_029_insider_buy_cluster_63'] = {'inputs': ['itf_base_universe_d2_020_itf_029_insider_buy_cluster_63'], 'func': itf_base_universe_d3_020_itf_029_insider_buy_cluster_63}


def itf_base_universe_d3_021_itf_030_insider_net_buy_ratio_252(itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252):
    return _base_universe_d3(itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252, 21)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_021_itf_030_insider_net_buy_ratio_252'] = {'inputs': ['itf_base_universe_d2_021_itf_030_insider_net_buy_ratio_252'], 'func': itf_base_universe_d3_021_itf_030_insider_net_buy_ratio_252}


def itf_base_universe_d3_022_itf_031_insider_value_ratio_21(itf_base_universe_d2_022_itf_031_insider_value_ratio_21):
    return _base_universe_d3(itf_base_universe_d2_022_itf_031_insider_value_ratio_21, 22)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_022_itf_031_insider_value_ratio_21'] = {'inputs': ['itf_base_universe_d2_022_itf_031_insider_value_ratio_21'], 'func': itf_base_universe_d3_022_itf_031_insider_value_ratio_21}


def itf_base_universe_d3_023_itf_032_ceo_cfo_buy_weight_42(itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42, 23)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_023_itf_032_ceo_cfo_buy_weight_42'] = {'inputs': ['itf_base_universe_d2_023_itf_032_ceo_cfo_buy_weight_42'], 'func': itf_base_universe_d3_023_itf_032_ceo_cfo_buy_weight_42}


def itf_base_universe_d3_024_itf_034_insider_conviction_84(itf_base_universe_d2_024_itf_034_insider_conviction_84):
    return _base_universe_d3(itf_base_universe_d2_024_itf_034_insider_conviction_84, 24)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_024_itf_034_insider_conviction_84'] = {'inputs': ['itf_base_universe_d2_024_itf_034_insider_conviction_84'], 'func': itf_base_universe_d3_024_itf_034_insider_conviction_84}


def itf_base_universe_d3_025_itf_035_insider_silence_126(itf_base_universe_d2_025_itf_035_insider_silence_126):
    return _base_universe_d3(itf_base_universe_d2_025_itf_035_insider_silence_126, 25)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_025_itf_035_insider_silence_126'] = {'inputs': ['itf_base_universe_d2_025_itf_035_insider_silence_126'], 'func': itf_base_universe_d3_025_itf_035_insider_silence_126}


def itf_base_universe_d3_026_itf_036_insider_buy_cluster_189(itf_base_universe_d2_026_itf_036_insider_buy_cluster_189):
    return _base_universe_d3(itf_base_universe_d2_026_itf_036_insider_buy_cluster_189, 26)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_026_itf_036_insider_buy_cluster_189'] = {'inputs': ['itf_base_universe_d2_026_itf_036_insider_buy_cluster_189'], 'func': itf_base_universe_d3_026_itf_036_insider_buy_cluster_189}


def itf_base_universe_d3_027_itf_038_insider_value_ratio_378(itf_base_universe_d2_027_itf_038_insider_value_ratio_378):
    return _base_universe_d3(itf_base_universe_d2_027_itf_038_insider_value_ratio_378, 27)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_027_itf_038_insider_value_ratio_378'] = {'inputs': ['itf_base_universe_d2_027_itf_038_insider_value_ratio_378'], 'func': itf_base_universe_d3_027_itf_038_insider_value_ratio_378}


def itf_base_universe_d3_028_itf_039_ceo_cfo_buy_weight_504(itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504, 28)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_028_itf_039_ceo_cfo_buy_weight_504'] = {'inputs': ['itf_base_universe_d2_028_itf_039_ceo_cfo_buy_weight_504'], 'func': itf_base_universe_d3_028_itf_039_ceo_cfo_buy_weight_504}


def itf_base_universe_d3_029_itf_041_insider_conviction_1008(itf_base_universe_d2_029_itf_041_insider_conviction_1008):
    return _base_universe_d3(itf_base_universe_d2_029_itf_041_insider_conviction_1008, 29)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_029_itf_041_insider_conviction_1008'] = {'inputs': ['itf_base_universe_d2_029_itf_041_insider_conviction_1008'], 'func': itf_base_universe_d3_029_itf_041_insider_conviction_1008}


def itf_base_universe_d3_030_itf_042_insider_silence_1260(itf_base_universe_d2_030_itf_042_insider_silence_1260):
    return _base_universe_d3(itf_base_universe_d2_030_itf_042_insider_silence_1260, 30)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_030_itf_042_insider_silence_1260'] = {'inputs': ['itf_base_universe_d2_030_itf_042_insider_silence_1260'], 'func': itf_base_universe_d3_030_itf_042_insider_silence_1260}


def itf_base_universe_d3_031_itf_043_insider_buy_cluster_1512(itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512):
    return _base_universe_d3(itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512, 31)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_031_itf_043_insider_buy_cluster_1512'] = {'inputs': ['itf_base_universe_d2_031_itf_043_insider_buy_cluster_1512'], 'func': itf_base_universe_d3_031_itf_043_insider_buy_cluster_1512}


def itf_base_universe_d3_032_itf_044_insider_net_buy_ratio_63(itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63):
    return _base_universe_d3(itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63, 32)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_032_itf_044_insider_net_buy_ratio_63'] = {'inputs': ['itf_base_universe_d2_032_itf_044_insider_net_buy_ratio_63'], 'func': itf_base_universe_d3_032_itf_044_insider_net_buy_ratio_63}


def itf_base_universe_d3_033_itf_045_insider_value_ratio_252(itf_base_universe_d2_033_itf_045_insider_value_ratio_252):
    return _base_universe_d3(itf_base_universe_d2_033_itf_045_insider_value_ratio_252, 33)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_033_itf_045_insider_value_ratio_252'] = {'inputs': ['itf_base_universe_d2_033_itf_045_insider_value_ratio_252'], 'func': itf_base_universe_d3_033_itf_045_insider_value_ratio_252}


def itf_base_universe_d3_034_itf_046_ceo_cfo_buy_weight_21(itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21, 34)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_034_itf_046_ceo_cfo_buy_weight_21'] = {'inputs': ['itf_base_universe_d2_034_itf_046_ceo_cfo_buy_weight_21'], 'func': itf_base_universe_d3_034_itf_046_ceo_cfo_buy_weight_21}


def itf_base_universe_d3_035_itf_048_insider_conviction_63(itf_base_universe_d2_035_itf_048_insider_conviction_63):
    return _base_universe_d3(itf_base_universe_d2_035_itf_048_insider_conviction_63, 35)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_035_itf_048_insider_conviction_63'] = {'inputs': ['itf_base_universe_d2_035_itf_048_insider_conviction_63'], 'func': itf_base_universe_d3_035_itf_048_insider_conviction_63}


def itf_base_universe_d3_036_itf_049_insider_silence_84(itf_base_universe_d2_036_itf_049_insider_silence_84):
    return _base_universe_d3(itf_base_universe_d2_036_itf_049_insider_silence_84, 36)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_036_itf_049_insider_silence_84'] = {'inputs': ['itf_base_universe_d2_036_itf_049_insider_silence_84'], 'func': itf_base_universe_d3_036_itf_049_insider_silence_84}


def itf_base_universe_d3_037_itf_050_insider_buy_cluster_126(itf_base_universe_d2_037_itf_050_insider_buy_cluster_126):
    return _base_universe_d3(itf_base_universe_d2_037_itf_050_insider_buy_cluster_126, 37)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_037_itf_050_insider_buy_cluster_126'] = {'inputs': ['itf_base_universe_d2_037_itf_050_insider_buy_cluster_126'], 'func': itf_base_universe_d3_037_itf_050_insider_buy_cluster_126}


def itf_base_universe_d3_038_itf_051_insider_net_buy_ratio_189(itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189):
    return _base_universe_d3(itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189, 38)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_038_itf_051_insider_net_buy_ratio_189'] = {'inputs': ['itf_base_universe_d2_038_itf_051_insider_net_buy_ratio_189'], 'func': itf_base_universe_d3_038_itf_051_insider_net_buy_ratio_189}


def itf_base_universe_d3_039_itf_053_ceo_cfo_buy_weight_378(itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378, 39)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_039_itf_053_ceo_cfo_buy_weight_378'] = {'inputs': ['itf_base_universe_d2_039_itf_053_ceo_cfo_buy_weight_378'], 'func': itf_base_universe_d3_039_itf_053_ceo_cfo_buy_weight_378}


def itf_base_universe_d3_040_itf_055_insider_conviction_756(itf_base_universe_d2_040_itf_055_insider_conviction_756):
    return _base_universe_d3(itf_base_universe_d2_040_itf_055_insider_conviction_756, 40)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_040_itf_055_insider_conviction_756'] = {'inputs': ['itf_base_universe_d2_040_itf_055_insider_conviction_756'], 'func': itf_base_universe_d3_040_itf_055_insider_conviction_756}


def itf_base_universe_d3_041_itf_056_insider_silence_1008(itf_base_universe_d2_041_itf_056_insider_silence_1008):
    return _base_universe_d3(itf_base_universe_d2_041_itf_056_insider_silence_1008, 41)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_041_itf_056_insider_silence_1008'] = {'inputs': ['itf_base_universe_d2_041_itf_056_insider_silence_1008'], 'func': itf_base_universe_d3_041_itf_056_insider_silence_1008}


def itf_base_universe_d3_042_itf_057_insider_buy_cluster_1260(itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260):
    return _base_universe_d3(itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260, 42)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_042_itf_057_insider_buy_cluster_1260'] = {'inputs': ['itf_base_universe_d2_042_itf_057_insider_buy_cluster_1260'], 'func': itf_base_universe_d3_042_itf_057_insider_buy_cluster_1260}


def itf_base_universe_d3_043_itf_058_insider_net_buy_ratio_1512(itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512, 43)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_043_itf_058_insider_net_buy_ratio_1512'] = {'inputs': ['itf_base_universe_d2_043_itf_058_insider_net_buy_ratio_1512'], 'func': itf_base_universe_d3_043_itf_058_insider_net_buy_ratio_1512}


def itf_base_universe_d3_044_itf_060_ceo_cfo_buy_weight_252(itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252, 44)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_044_itf_060_ceo_cfo_buy_weight_252'] = {'inputs': ['itf_base_universe_d2_044_itf_060_ceo_cfo_buy_weight_252'], 'func': itf_base_universe_d3_044_itf_060_ceo_cfo_buy_weight_252}


def itf_base_universe_d3_045_itf_062_insider_conviction_42(itf_base_universe_d2_045_itf_062_insider_conviction_42):
    return _base_universe_d3(itf_base_universe_d2_045_itf_062_insider_conviction_42, 45)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_045_itf_062_insider_conviction_42'] = {'inputs': ['itf_base_universe_d2_045_itf_062_insider_conviction_42'], 'func': itf_base_universe_d3_045_itf_062_insider_conviction_42}


def itf_base_universe_d3_046_itf_064_insider_buy_cluster_84(itf_base_universe_d2_046_itf_064_insider_buy_cluster_84):
    return _base_universe_d3(itf_base_universe_d2_046_itf_064_insider_buy_cluster_84, 46)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_046_itf_064_insider_buy_cluster_84'] = {'inputs': ['itf_base_universe_d2_046_itf_064_insider_buy_cluster_84'], 'func': itf_base_universe_d3_046_itf_064_insider_buy_cluster_84}


def itf_base_universe_d3_047_itf_065_insider_net_buy_ratio_126(itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126):
    return _base_universe_d3(itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126, 47)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_047_itf_065_insider_net_buy_ratio_126'] = {'inputs': ['itf_base_universe_d2_047_itf_065_insider_net_buy_ratio_126'], 'func': itf_base_universe_d3_047_itf_065_insider_net_buy_ratio_126}


def itf_base_universe_d3_048_itf_066_insider_value_ratio_189(itf_base_universe_d2_048_itf_066_insider_value_ratio_189):
    return _base_universe_d3(itf_base_universe_d2_048_itf_066_insider_value_ratio_189, 48)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_048_itf_066_insider_value_ratio_189'] = {'inputs': ['itf_base_universe_d2_048_itf_066_insider_value_ratio_189'], 'func': itf_base_universe_d3_048_itf_066_insider_value_ratio_189}


def itf_base_universe_d3_049_itf_069_insider_conviction_504(itf_base_universe_d2_049_itf_069_insider_conviction_504):
    return _base_universe_d3(itf_base_universe_d2_049_itf_069_insider_conviction_504, 49)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_049_itf_069_insider_conviction_504'] = {'inputs': ['itf_base_universe_d2_049_itf_069_insider_conviction_504'], 'func': itf_base_universe_d3_049_itf_069_insider_conviction_504}


def itf_base_universe_d3_050_itf_070_insider_silence_756(itf_base_universe_d2_050_itf_070_insider_silence_756):
    return _base_universe_d3(itf_base_universe_d2_050_itf_070_insider_silence_756, 50)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_050_itf_070_insider_silence_756'] = {'inputs': ['itf_base_universe_d2_050_itf_070_insider_silence_756'], 'func': itf_base_universe_d3_050_itf_070_insider_silence_756}


def itf_base_universe_d3_051_itf_071_insider_buy_cluster_1008(itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008):
    return _base_universe_d3(itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008, 51)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_051_itf_071_insider_buy_cluster_1008'] = {'inputs': ['itf_base_universe_d2_051_itf_071_insider_buy_cluster_1008'], 'func': itf_base_universe_d3_051_itf_071_insider_buy_cluster_1008}


def itf_base_universe_d3_052_itf_072_insider_net_buy_ratio_1260(itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260, 52)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_052_itf_072_insider_net_buy_ratio_1260'] = {'inputs': ['itf_base_universe_d2_052_itf_072_insider_net_buy_ratio_1260'], 'func': itf_base_universe_d3_052_itf_072_insider_net_buy_ratio_1260}


def itf_base_universe_d3_053_itf_073_insider_value_ratio_1512(itf_base_universe_d2_053_itf_073_insider_value_ratio_1512):
    return _base_universe_d3(itf_base_universe_d2_053_itf_073_insider_value_ratio_1512, 53)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_053_itf_073_insider_value_ratio_1512'] = {'inputs': ['itf_base_universe_d2_053_itf_073_insider_value_ratio_1512'], 'func': itf_base_universe_d3_053_itf_073_insider_value_ratio_1512}


def itf_base_universe_d3_054_itf_basefill_005(itf_base_universe_d2_054_itf_basefill_005):
    return _base_universe_d3(itf_base_universe_d2_054_itf_basefill_005, 54)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_054_itf_basefill_005'] = {'inputs': ['itf_base_universe_d2_054_itf_basefill_005'], 'func': itf_base_universe_d3_054_itf_basefill_005}


def itf_base_universe_d3_055_itf_basefill_012(itf_base_universe_d2_055_itf_basefill_012):
    return _base_universe_d3(itf_base_universe_d2_055_itf_basefill_012, 55)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_055_itf_basefill_012'] = {'inputs': ['itf_base_universe_d2_055_itf_basefill_012'], 'func': itf_base_universe_d3_055_itf_basefill_012}


def itf_base_universe_d3_056_itf_basefill_019(itf_base_universe_d2_056_itf_basefill_019):
    return _base_universe_d3(itf_base_universe_d2_056_itf_basefill_019, 56)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_056_itf_basefill_019'] = {'inputs': ['itf_base_universe_d2_056_itf_basefill_019'], 'func': itf_base_universe_d3_056_itf_basefill_019}


def itf_base_universe_d3_057_itf_basefill_022(itf_base_universe_d2_057_itf_basefill_022):
    return _base_universe_d3(itf_base_universe_d2_057_itf_basefill_022, 57)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_057_itf_basefill_022'] = {'inputs': ['itf_base_universe_d2_057_itf_basefill_022'], 'func': itf_base_universe_d3_057_itf_basefill_022}


def itf_base_universe_d3_058_itf_basefill_026(itf_base_universe_d2_058_itf_basefill_026):
    return _base_universe_d3(itf_base_universe_d2_058_itf_basefill_026, 58)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_058_itf_basefill_026'] = {'inputs': ['itf_base_universe_d2_058_itf_basefill_026'], 'func': itf_base_universe_d3_058_itf_basefill_026}


def itf_base_universe_d3_059_itf_basefill_033(itf_base_universe_d2_059_itf_basefill_033):
    return _base_universe_d3(itf_base_universe_d2_059_itf_basefill_033, 59)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_059_itf_basefill_033'] = {'inputs': ['itf_base_universe_d2_059_itf_basefill_033'], 'func': itf_base_universe_d3_059_itf_basefill_033}


def itf_base_universe_d3_060_itf_basefill_037(itf_base_universe_d2_060_itf_basefill_037):
    return _base_universe_d3(itf_base_universe_d2_060_itf_basefill_037, 60)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_060_itf_basefill_037'] = {'inputs': ['itf_base_universe_d2_060_itf_basefill_037'], 'func': itf_base_universe_d3_060_itf_basefill_037}


def itf_base_universe_d3_061_itf_basefill_040(itf_base_universe_d2_061_itf_basefill_040):
    return _base_universe_d3(itf_base_universe_d2_061_itf_basefill_040, 61)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_061_itf_basefill_040'] = {'inputs': ['itf_base_universe_d2_061_itf_basefill_040'], 'func': itf_base_universe_d3_061_itf_basefill_040}


def itf_base_universe_d3_062_itf_basefill_047(itf_base_universe_d2_062_itf_basefill_047):
    return _base_universe_d3(itf_base_universe_d2_062_itf_basefill_047, 62)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_062_itf_basefill_047'] = {'inputs': ['itf_base_universe_d2_062_itf_basefill_047'], 'func': itf_base_universe_d3_062_itf_basefill_047}


def itf_base_universe_d3_063_itf_basefill_052(itf_base_universe_d2_063_itf_basefill_052):
    return _base_universe_d3(itf_base_universe_d2_063_itf_basefill_052, 63)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_063_itf_basefill_052'] = {'inputs': ['itf_base_universe_d2_063_itf_basefill_052'], 'func': itf_base_universe_d3_063_itf_basefill_052}


def itf_base_universe_d3_064_itf_basefill_054(itf_base_universe_d2_064_itf_basefill_054):
    return _base_universe_d3(itf_base_universe_d2_064_itf_basefill_054, 64)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_064_itf_basefill_054'] = {'inputs': ['itf_base_universe_d2_064_itf_basefill_054'], 'func': itf_base_universe_d3_064_itf_basefill_054}


def itf_base_universe_d3_065_itf_basefill_059(itf_base_universe_d2_065_itf_basefill_059):
    return _base_universe_d3(itf_base_universe_d2_065_itf_basefill_059, 65)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_065_itf_basefill_059'] = {'inputs': ['itf_base_universe_d2_065_itf_basefill_059'], 'func': itf_base_universe_d3_065_itf_basefill_059}


def itf_base_universe_d3_066_itf_basefill_061(itf_base_universe_d2_066_itf_basefill_061):
    return _base_universe_d3(itf_base_universe_d2_066_itf_basefill_061, 66)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_066_itf_basefill_061'] = {'inputs': ['itf_base_universe_d2_066_itf_basefill_061'], 'func': itf_base_universe_d3_066_itf_basefill_061}


def itf_base_universe_d3_067_itf_basefill_063(itf_base_universe_d2_067_itf_basefill_063):
    return _base_universe_d3(itf_base_universe_d2_067_itf_basefill_063, 67)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_067_itf_basefill_063'] = {'inputs': ['itf_base_universe_d2_067_itf_basefill_063'], 'func': itf_base_universe_d3_067_itf_basefill_063}


def itf_base_universe_d3_068_itf_basefill_067(itf_base_universe_d2_068_itf_basefill_067):
    return _base_universe_d3(itf_base_universe_d2_068_itf_basefill_067, 68)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_068_itf_basefill_067'] = {'inputs': ['itf_base_universe_d2_068_itf_basefill_067'], 'func': itf_base_universe_d3_068_itf_basefill_067}


def itf_base_universe_d3_069_itf_basefill_068(itf_base_universe_d2_069_itf_basefill_068):
    return _base_universe_d3(itf_base_universe_d2_069_itf_basefill_068, 69)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_069_itf_basefill_068'] = {'inputs': ['itf_base_universe_d2_069_itf_basefill_068'], 'func': itf_base_universe_d3_069_itf_basefill_068}


def itf_base_universe_d3_070_itf_basefill_074(itf_base_universe_d2_070_itf_basefill_074):
    return _base_universe_d3(itf_base_universe_d2_070_itf_basefill_074, 70)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_070_itf_basefill_074'] = {'inputs': ['itf_base_universe_d2_070_itf_basefill_074'], 'func': itf_base_universe_d3_070_itf_basefill_074}


def itf_base_universe_d3_071_itf_basefill_075(itf_base_universe_d2_071_itf_basefill_075):
    return _base_universe_d3(itf_base_universe_d2_071_itf_basefill_075, 71)
ITF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itf_base_universe_d3_071_itf_basefill_075'] = {'inputs': ['itf_base_universe_d2_071_itf_basefill_075'], 'func': itf_base_universe_d3_071_itf_basefill_075}
