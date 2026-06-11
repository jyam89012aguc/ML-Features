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



def evd_176_evd_001_pe_compression_z_21_accel_1(evd_151_evd_001_pe_compression_z_21_roc_1):
    feature = _s(evd_151_evd_001_pe_compression_z_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def evd_177_evd_007_earnings_yield_spike_252_accel_42(evd_152_evd_007_earnings_yield_spike_252_roc_42):
    feature = _s(evd_152_evd_007_earnings_yield_spike_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def evd_178_evd_013_ev_marketcap_gap_1512_accel_126(evd_153_evd_013_ev_marketcap_gap_1512_roc_126):
    feature = _s(evd_153_evd_013_ev_marketcap_gap_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def evd_179_evd_019_ps_compression_z_84_accel_378(evd_154_evd_019_ps_compression_z_84_roc_378):
    feature = _s(evd_154_evd_019_ps_compression_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def evd_180_evd_025_pe_compression_z_756_accel_4(evd_155_evd_025_pe_compression_z_756_roc_4):
    feature = _s(evd_155_evd_025_pe_compression_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















EV_DISTORTION_REGISTRY_3RD_DERIVATIVES = {
    'evd_176_evd_001_pe_compression_z_21_accel_1': {'inputs': ['evd_151_evd_001_pe_compression_z_21_roc_1'], 'func': evd_176_evd_001_pe_compression_z_21_accel_1},
    'evd_177_evd_007_earnings_yield_spike_252_accel_42': {'inputs': ['evd_152_evd_007_earnings_yield_spike_252_roc_42'], 'func': evd_177_evd_007_earnings_yield_spike_252_accel_42},
    'evd_178_evd_013_ev_marketcap_gap_1512_accel_126': {'inputs': ['evd_153_evd_013_ev_marketcap_gap_1512_roc_126'], 'func': evd_178_evd_013_ev_marketcap_gap_1512_accel_126},
    'evd_179_evd_019_ps_compression_z_84_accel_378': {'inputs': ['evd_154_evd_019_ps_compression_z_84_roc_378'], 'func': evd_179_evd_019_ps_compression_z_84_accel_378},
    'evd_180_evd_025_pe_compression_z_756_accel_4': {'inputs': ['evd_155_evd_025_pe_compression_z_756_roc_4'], 'func': evd_180_evd_025_pe_compression_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ed_replacement_d3_001(ed_replacement_d2_001):
    feature = _clean(ed_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_001'] = {'inputs': ['ed_replacement_d2_001'], 'func': ed_replacement_d3_001}


def ed_replacement_d3_002(ed_replacement_d2_002):
    feature = _clean(ed_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_002'] = {'inputs': ['ed_replacement_d2_002'], 'func': ed_replacement_d3_002}


def ed_replacement_d3_003(ed_replacement_d2_003):
    feature = _clean(ed_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_003'] = {'inputs': ['ed_replacement_d2_003'], 'func': ed_replacement_d3_003}


def ed_replacement_d3_004(ed_replacement_d2_004):
    feature = _clean(ed_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_004'] = {'inputs': ['ed_replacement_d2_004'], 'func': ed_replacement_d3_004}


def ed_replacement_d3_005(ed_replacement_d2_005):
    feature = _clean(ed_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_005'] = {'inputs': ['ed_replacement_d2_005'], 'func': ed_replacement_d3_005}


def ed_replacement_d3_006(ed_replacement_d2_006):
    feature = _clean(ed_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_006'] = {'inputs': ['ed_replacement_d2_006'], 'func': ed_replacement_d3_006}


def ed_replacement_d3_007(ed_replacement_d2_007):
    feature = _clean(ed_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_007'] = {'inputs': ['ed_replacement_d2_007'], 'func': ed_replacement_d3_007}


def ed_replacement_d3_008(ed_replacement_d2_008):
    feature = _clean(ed_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_008'] = {'inputs': ['ed_replacement_d2_008'], 'func': ed_replacement_d3_008}


def ed_replacement_d3_009(ed_replacement_d2_009):
    feature = _clean(ed_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_009'] = {'inputs': ['ed_replacement_d2_009'], 'func': ed_replacement_d3_009}


def ed_replacement_d3_010(ed_replacement_d2_010):
    feature = _clean(ed_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_010'] = {'inputs': ['ed_replacement_d2_010'], 'func': ed_replacement_d3_010}


def ed_replacement_d3_011(ed_replacement_d2_011):
    feature = _clean(ed_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_011'] = {'inputs': ['ed_replacement_d2_011'], 'func': ed_replacement_d3_011}


def ed_replacement_d3_012(ed_replacement_d2_012):
    feature = _clean(ed_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_012'] = {'inputs': ['ed_replacement_d2_012'], 'func': ed_replacement_d3_012}


def ed_replacement_d3_013(ed_replacement_d2_013):
    feature = _clean(ed_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_013'] = {'inputs': ['ed_replacement_d2_013'], 'func': ed_replacement_d3_013}


def ed_replacement_d3_014(ed_replacement_d2_014):
    feature = _clean(ed_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_014'] = {'inputs': ['ed_replacement_d2_014'], 'func': ed_replacement_d3_014}


def ed_replacement_d3_015(ed_replacement_d2_015):
    feature = _clean(ed_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_015'] = {'inputs': ['ed_replacement_d2_015'], 'func': ed_replacement_d3_015}


def ed_replacement_d3_016(ed_replacement_d2_016):
    feature = _clean(ed_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_016'] = {'inputs': ['ed_replacement_d2_016'], 'func': ed_replacement_d3_016}


def ed_replacement_d3_017(ed_replacement_d2_017):
    feature = _clean(ed_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_017'] = {'inputs': ['ed_replacement_d2_017'], 'func': ed_replacement_d3_017}


def ed_replacement_d3_018(ed_replacement_d2_018):
    feature = _clean(ed_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_018'] = {'inputs': ['ed_replacement_d2_018'], 'func': ed_replacement_d3_018}


def ed_replacement_d3_019(ed_replacement_d2_019):
    feature = _clean(ed_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_019'] = {'inputs': ['ed_replacement_d2_019'], 'func': ed_replacement_d3_019}


def ed_replacement_d3_020(ed_replacement_d2_020):
    feature = _clean(ed_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_020'] = {'inputs': ['ed_replacement_d2_020'], 'func': ed_replacement_d3_020}


def ed_replacement_d3_021(ed_replacement_d2_021):
    feature = _clean(ed_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_021'] = {'inputs': ['ed_replacement_d2_021'], 'func': ed_replacement_d3_021}


def ed_replacement_d3_022(ed_replacement_d2_022):
    feature = _clean(ed_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_022'] = {'inputs': ['ed_replacement_d2_022'], 'func': ed_replacement_d3_022}


def ed_replacement_d3_023(ed_replacement_d2_023):
    feature = _clean(ed_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_023'] = {'inputs': ['ed_replacement_d2_023'], 'func': ed_replacement_d3_023}


def ed_replacement_d3_024(ed_replacement_d2_024):
    feature = _clean(ed_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_024'] = {'inputs': ['ed_replacement_d2_024'], 'func': ed_replacement_d3_024}


def ed_replacement_d3_025(ed_replacement_d2_025):
    feature = _clean(ed_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_025'] = {'inputs': ['ed_replacement_d2_025'], 'func': ed_replacement_d3_025}


def ed_replacement_d3_026(ed_replacement_d2_026):
    feature = _clean(ed_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_026'] = {'inputs': ['ed_replacement_d2_026'], 'func': ed_replacement_d3_026}


def ed_replacement_d3_027(ed_replacement_d2_027):
    feature = _clean(ed_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_027'] = {'inputs': ['ed_replacement_d2_027'], 'func': ed_replacement_d3_027}


def ed_replacement_d3_028(ed_replacement_d2_028):
    feature = _clean(ed_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_028'] = {'inputs': ['ed_replacement_d2_028'], 'func': ed_replacement_d3_028}


def ed_replacement_d3_029(ed_replacement_d2_029):
    feature = _clean(ed_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_029'] = {'inputs': ['ed_replacement_d2_029'], 'func': ed_replacement_d3_029}


def ed_replacement_d3_030(ed_replacement_d2_030):
    feature = _clean(ed_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_030'] = {'inputs': ['ed_replacement_d2_030'], 'func': ed_replacement_d3_030}


def ed_replacement_d3_031(ed_replacement_d2_031):
    feature = _clean(ed_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_031'] = {'inputs': ['ed_replacement_d2_031'], 'func': ed_replacement_d3_031}


def ed_replacement_d3_032(ed_replacement_d2_032):
    feature = _clean(ed_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_032'] = {'inputs': ['ed_replacement_d2_032'], 'func': ed_replacement_d3_032}


def ed_replacement_d3_033(ed_replacement_d2_033):
    feature = _clean(ed_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_033'] = {'inputs': ['ed_replacement_d2_033'], 'func': ed_replacement_d3_033}


def ed_replacement_d3_034(ed_replacement_d2_034):
    feature = _clean(ed_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_034'] = {'inputs': ['ed_replacement_d2_034'], 'func': ed_replacement_d3_034}


def ed_replacement_d3_035(ed_replacement_d2_035):
    feature = _clean(ed_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_035'] = {'inputs': ['ed_replacement_d2_035'], 'func': ed_replacement_d3_035}


def ed_replacement_d3_036(ed_replacement_d2_036):
    feature = _clean(ed_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_036'] = {'inputs': ['ed_replacement_d2_036'], 'func': ed_replacement_d3_036}


def ed_replacement_d3_037(ed_replacement_d2_037):
    feature = _clean(ed_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_037'] = {'inputs': ['ed_replacement_d2_037'], 'func': ed_replacement_d3_037}


def ed_replacement_d3_038(ed_replacement_d2_038):
    feature = _clean(ed_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_038'] = {'inputs': ['ed_replacement_d2_038'], 'func': ed_replacement_d3_038}


def ed_replacement_d3_039(ed_replacement_d2_039):
    feature = _clean(ed_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_039'] = {'inputs': ['ed_replacement_d2_039'], 'func': ed_replacement_d3_039}


def ed_replacement_d3_040(ed_replacement_d2_040):
    feature = _clean(ed_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_040'] = {'inputs': ['ed_replacement_d2_040'], 'func': ed_replacement_d3_040}


def ed_replacement_d3_041(ed_replacement_d2_041):
    feature = _clean(ed_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_041'] = {'inputs': ['ed_replacement_d2_041'], 'func': ed_replacement_d3_041}


def ed_replacement_d3_042(ed_replacement_d2_042):
    feature = _clean(ed_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_042'] = {'inputs': ['ed_replacement_d2_042'], 'func': ed_replacement_d3_042}


def ed_replacement_d3_043(ed_replacement_d2_043):
    feature = _clean(ed_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_043'] = {'inputs': ['ed_replacement_d2_043'], 'func': ed_replacement_d3_043}


def ed_replacement_d3_044(ed_replacement_d2_044):
    feature = _clean(ed_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_044'] = {'inputs': ['ed_replacement_d2_044'], 'func': ed_replacement_d3_044}


def ed_replacement_d3_045(ed_replacement_d2_045):
    feature = _clean(ed_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_045'] = {'inputs': ['ed_replacement_d2_045'], 'func': ed_replacement_d3_045}


def ed_replacement_d3_046(ed_replacement_d2_046):
    feature = _clean(ed_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_046'] = {'inputs': ['ed_replacement_d2_046'], 'func': ed_replacement_d3_046}


def ed_replacement_d3_047(ed_replacement_d2_047):
    feature = _clean(ed_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_047'] = {'inputs': ['ed_replacement_d2_047'], 'func': ed_replacement_d3_047}


def ed_replacement_d3_048(ed_replacement_d2_048):
    feature = _clean(ed_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_048'] = {'inputs': ['ed_replacement_d2_048'], 'func': ed_replacement_d3_048}


def ed_replacement_d3_049(ed_replacement_d2_049):
    feature = _clean(ed_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_049'] = {'inputs': ['ed_replacement_d2_049'], 'func': ed_replacement_d3_049}


def ed_replacement_d3_050(ed_replacement_d2_050):
    feature = _clean(ed_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_050'] = {'inputs': ['ed_replacement_d2_050'], 'func': ed_replacement_d3_050}


def ed_replacement_d3_051(ed_replacement_d2_051):
    feature = _clean(ed_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_051'] = {'inputs': ['ed_replacement_d2_051'], 'func': ed_replacement_d3_051}


def ed_replacement_d3_052(ed_replacement_d2_052):
    feature = _clean(ed_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_052'] = {'inputs': ['ed_replacement_d2_052'], 'func': ed_replacement_d3_052}


def ed_replacement_d3_053(ed_replacement_d2_053):
    feature = _clean(ed_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_053'] = {'inputs': ['ed_replacement_d2_053'], 'func': ed_replacement_d3_053}


def ed_replacement_d3_054(ed_replacement_d2_054):
    feature = _clean(ed_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_054'] = {'inputs': ['ed_replacement_d2_054'], 'func': ed_replacement_d3_054}


def ed_replacement_d3_055(ed_replacement_d2_055):
    feature = _clean(ed_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_055'] = {'inputs': ['ed_replacement_d2_055'], 'func': ed_replacement_d3_055}


def ed_replacement_d3_056(ed_replacement_d2_056):
    feature = _clean(ed_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_056'] = {'inputs': ['ed_replacement_d2_056'], 'func': ed_replacement_d3_056}


def ed_replacement_d3_057(ed_replacement_d2_057):
    feature = _clean(ed_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_057'] = {'inputs': ['ed_replacement_d2_057'], 'func': ed_replacement_d3_057}


def ed_replacement_d3_058(ed_replacement_d2_058):
    feature = _clean(ed_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_058'] = {'inputs': ['ed_replacement_d2_058'], 'func': ed_replacement_d3_058}


def ed_replacement_d3_059(ed_replacement_d2_059):
    feature = _clean(ed_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_059'] = {'inputs': ['ed_replacement_d2_059'], 'func': ed_replacement_d3_059}


def ed_replacement_d3_060(ed_replacement_d2_060):
    feature = _clean(ed_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_060'] = {'inputs': ['ed_replacement_d2_060'], 'func': ed_replacement_d3_060}


def ed_replacement_d3_061(ed_replacement_d2_061):
    feature = _clean(ed_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_061'] = {'inputs': ['ed_replacement_d2_061'], 'func': ed_replacement_d3_061}


def ed_replacement_d3_062(ed_replacement_d2_062):
    feature = _clean(ed_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_062'] = {'inputs': ['ed_replacement_d2_062'], 'func': ed_replacement_d3_062}


def ed_replacement_d3_063(ed_replacement_d2_063):
    feature = _clean(ed_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_063'] = {'inputs': ['ed_replacement_d2_063'], 'func': ed_replacement_d3_063}


def ed_replacement_d3_064(ed_replacement_d2_064):
    feature = _clean(ed_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_064'] = {'inputs': ['ed_replacement_d2_064'], 'func': ed_replacement_d3_064}


def ed_replacement_d3_065(ed_replacement_d2_065):
    feature = _clean(ed_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_065'] = {'inputs': ['ed_replacement_d2_065'], 'func': ed_replacement_d3_065}


def ed_replacement_d3_066(ed_replacement_d2_066):
    feature = _clean(ed_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_066'] = {'inputs': ['ed_replacement_d2_066'], 'func': ed_replacement_d3_066}


def ed_replacement_d3_067(ed_replacement_d2_067):
    feature = _clean(ed_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_067'] = {'inputs': ['ed_replacement_d2_067'], 'func': ed_replacement_d3_067}


def ed_replacement_d3_068(ed_replacement_d2_068):
    feature = _clean(ed_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_068'] = {'inputs': ['ed_replacement_d2_068'], 'func': ed_replacement_d3_068}


def ed_replacement_d3_069(ed_replacement_d2_069):
    feature = _clean(ed_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_069'] = {'inputs': ['ed_replacement_d2_069'], 'func': ed_replacement_d3_069}


def ed_replacement_d3_070(ed_replacement_d2_070):
    feature = _clean(ed_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_070'] = {'inputs': ['ed_replacement_d2_070'], 'func': ed_replacement_d3_070}


def ed_replacement_d3_071(ed_replacement_d2_071):
    feature = _clean(ed_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_071'] = {'inputs': ['ed_replacement_d2_071'], 'func': ed_replacement_d3_071}


def ed_replacement_d3_072(ed_replacement_d2_072):
    feature = _clean(ed_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_072'] = {'inputs': ['ed_replacement_d2_072'], 'func': ed_replacement_d3_072}


def ed_replacement_d3_073(ed_replacement_d2_073):
    feature = _clean(ed_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_073'] = {'inputs': ['ed_replacement_d2_073'], 'func': ed_replacement_d3_073}


def ed_replacement_d3_074(ed_replacement_d2_074):
    feature = _clean(ed_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_074'] = {'inputs': ['ed_replacement_d2_074'], 'func': ed_replacement_d3_074}


def ed_replacement_d3_075(ed_replacement_d2_075):
    feature = _clean(ed_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_075'] = {'inputs': ['ed_replacement_d2_075'], 'func': ed_replacement_d3_075}


def ed_replacement_d3_076(ed_replacement_d2_076):
    feature = _clean(ed_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_076'] = {'inputs': ['ed_replacement_d2_076'], 'func': ed_replacement_d3_076}


def ed_replacement_d3_077(ed_replacement_d2_077):
    feature = _clean(ed_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_077'] = {'inputs': ['ed_replacement_d2_077'], 'func': ed_replacement_d3_077}


def ed_replacement_d3_078(ed_replacement_d2_078):
    feature = _clean(ed_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_078'] = {'inputs': ['ed_replacement_d2_078'], 'func': ed_replacement_d3_078}


def ed_replacement_d3_079(ed_replacement_d2_079):
    feature = _clean(ed_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_079'] = {'inputs': ['ed_replacement_d2_079'], 'func': ed_replacement_d3_079}


def ed_replacement_d3_080(ed_replacement_d2_080):
    feature = _clean(ed_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_080'] = {'inputs': ['ed_replacement_d2_080'], 'func': ed_replacement_d3_080}


def ed_replacement_d3_081(ed_replacement_d2_081):
    feature = _clean(ed_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_081'] = {'inputs': ['ed_replacement_d2_081'], 'func': ed_replacement_d3_081}


def ed_replacement_d3_082(ed_replacement_d2_082):
    feature = _clean(ed_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_082'] = {'inputs': ['ed_replacement_d2_082'], 'func': ed_replacement_d3_082}


def ed_replacement_d3_083(ed_replacement_d2_083):
    feature = _clean(ed_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_083'] = {'inputs': ['ed_replacement_d2_083'], 'func': ed_replacement_d3_083}


def ed_replacement_d3_084(ed_replacement_d2_084):
    feature = _clean(ed_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_084'] = {'inputs': ['ed_replacement_d2_084'], 'func': ed_replacement_d3_084}


def ed_replacement_d3_085(ed_replacement_d2_085):
    feature = _clean(ed_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_085'] = {'inputs': ['ed_replacement_d2_085'], 'func': ed_replacement_d3_085}


def ed_replacement_d3_086(ed_replacement_d2_086):
    feature = _clean(ed_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_086'] = {'inputs': ['ed_replacement_d2_086'], 'func': ed_replacement_d3_086}


def ed_replacement_d3_087(ed_replacement_d2_087):
    feature = _clean(ed_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_087'] = {'inputs': ['ed_replacement_d2_087'], 'func': ed_replacement_d3_087}


def ed_replacement_d3_088(ed_replacement_d2_088):
    feature = _clean(ed_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_088'] = {'inputs': ['ed_replacement_d2_088'], 'func': ed_replacement_d3_088}


def ed_replacement_d3_089(ed_replacement_d2_089):
    feature = _clean(ed_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_089'] = {'inputs': ['ed_replacement_d2_089'], 'func': ed_replacement_d3_089}


def ed_replacement_d3_090(ed_replacement_d2_090):
    feature = _clean(ed_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_090'] = {'inputs': ['ed_replacement_d2_090'], 'func': ed_replacement_d3_090}


def ed_replacement_d3_091(ed_replacement_d2_091):
    feature = _clean(ed_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_091'] = {'inputs': ['ed_replacement_d2_091'], 'func': ed_replacement_d3_091}


def ed_replacement_d3_092(ed_replacement_d2_092):
    feature = _clean(ed_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_092'] = {'inputs': ['ed_replacement_d2_092'], 'func': ed_replacement_d3_092}


def ed_replacement_d3_093(ed_replacement_d2_093):
    feature = _clean(ed_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_093'] = {'inputs': ['ed_replacement_d2_093'], 'func': ed_replacement_d3_093}


def ed_replacement_d3_094(ed_replacement_d2_094):
    feature = _clean(ed_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_094'] = {'inputs': ['ed_replacement_d2_094'], 'func': ed_replacement_d3_094}


def ed_replacement_d3_095(ed_replacement_d2_095):
    feature = _clean(ed_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_095'] = {'inputs': ['ed_replacement_d2_095'], 'func': ed_replacement_d3_095}


def ed_replacement_d3_096(ed_replacement_d2_096):
    feature = _clean(ed_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_096'] = {'inputs': ['ed_replacement_d2_096'], 'func': ed_replacement_d3_096}


def ed_replacement_d3_097(ed_replacement_d2_097):
    feature = _clean(ed_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_097'] = {'inputs': ['ed_replacement_d2_097'], 'func': ed_replacement_d3_097}


def ed_replacement_d3_098(ed_replacement_d2_098):
    feature = _clean(ed_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_098'] = {'inputs': ['ed_replacement_d2_098'], 'func': ed_replacement_d3_098}


def ed_replacement_d3_099(ed_replacement_d2_099):
    feature = _clean(ed_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_099'] = {'inputs': ['ed_replacement_d2_099'], 'func': ed_replacement_d3_099}


def ed_replacement_d3_100(ed_replacement_d2_100):
    feature = _clean(ed_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_100'] = {'inputs': ['ed_replacement_d2_100'], 'func': ed_replacement_d3_100}


def ed_replacement_d3_101(ed_replacement_d2_101):
    feature = _clean(ed_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_101'] = {'inputs': ['ed_replacement_d2_101'], 'func': ed_replacement_d3_101}


def ed_replacement_d3_102(ed_replacement_d2_102):
    feature = _clean(ed_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_102'] = {'inputs': ['ed_replacement_d2_102'], 'func': ed_replacement_d3_102}


def ed_replacement_d3_103(ed_replacement_d2_103):
    feature = _clean(ed_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_103'] = {'inputs': ['ed_replacement_d2_103'], 'func': ed_replacement_d3_103}


def ed_replacement_d3_104(ed_replacement_d2_104):
    feature = _clean(ed_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_104'] = {'inputs': ['ed_replacement_d2_104'], 'func': ed_replacement_d3_104}


def ed_replacement_d3_105(ed_replacement_d2_105):
    feature = _clean(ed_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_105'] = {'inputs': ['ed_replacement_d2_105'], 'func': ed_replacement_d3_105}


def ed_replacement_d3_106(ed_replacement_d2_106):
    feature = _clean(ed_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_106'] = {'inputs': ['ed_replacement_d2_106'], 'func': ed_replacement_d3_106}


def ed_replacement_d3_107(ed_replacement_d2_107):
    feature = _clean(ed_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_107'] = {'inputs': ['ed_replacement_d2_107'], 'func': ed_replacement_d3_107}


def ed_replacement_d3_108(ed_replacement_d2_108):
    feature = _clean(ed_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_108'] = {'inputs': ['ed_replacement_d2_108'], 'func': ed_replacement_d3_108}


def ed_replacement_d3_109(ed_replacement_d2_109):
    feature = _clean(ed_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_109'] = {'inputs': ['ed_replacement_d2_109'], 'func': ed_replacement_d3_109}


def ed_replacement_d3_110(ed_replacement_d2_110):
    feature = _clean(ed_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_110'] = {'inputs': ['ed_replacement_d2_110'], 'func': ed_replacement_d3_110}


def ed_replacement_d3_111(ed_replacement_d2_111):
    feature = _clean(ed_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_111'] = {'inputs': ['ed_replacement_d2_111'], 'func': ed_replacement_d3_111}


def ed_replacement_d3_112(ed_replacement_d2_112):
    feature = _clean(ed_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_112'] = {'inputs': ['ed_replacement_d2_112'], 'func': ed_replacement_d3_112}


def ed_replacement_d3_113(ed_replacement_d2_113):
    feature = _clean(ed_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_113'] = {'inputs': ['ed_replacement_d2_113'], 'func': ed_replacement_d3_113}


def ed_replacement_d3_114(ed_replacement_d2_114):
    feature = _clean(ed_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_114'] = {'inputs': ['ed_replacement_d2_114'], 'func': ed_replacement_d3_114}


def ed_replacement_d3_115(ed_replacement_d2_115):
    feature = _clean(ed_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_115'] = {'inputs': ['ed_replacement_d2_115'], 'func': ed_replacement_d3_115}


def ed_replacement_d3_116(ed_replacement_d2_116):
    feature = _clean(ed_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_116'] = {'inputs': ['ed_replacement_d2_116'], 'func': ed_replacement_d3_116}


def ed_replacement_d3_117(ed_replacement_d2_117):
    feature = _clean(ed_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_117'] = {'inputs': ['ed_replacement_d2_117'], 'func': ed_replacement_d3_117}


def ed_replacement_d3_118(ed_replacement_d2_118):
    feature = _clean(ed_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_118'] = {'inputs': ['ed_replacement_d2_118'], 'func': ed_replacement_d3_118}


def ed_replacement_d3_119(ed_replacement_d2_119):
    feature = _clean(ed_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_119'] = {'inputs': ['ed_replacement_d2_119'], 'func': ed_replacement_d3_119}


def ed_replacement_d3_120(ed_replacement_d2_120):
    feature = _clean(ed_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_120'] = {'inputs': ['ed_replacement_d2_120'], 'func': ed_replacement_d3_120}


def ed_replacement_d3_121(ed_replacement_d2_121):
    feature = _clean(ed_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_121'] = {'inputs': ['ed_replacement_d2_121'], 'func': ed_replacement_d3_121}


def ed_replacement_d3_122(ed_replacement_d2_122):
    feature = _clean(ed_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_122'] = {'inputs': ['ed_replacement_d2_122'], 'func': ed_replacement_d3_122}


def ed_replacement_d3_123(ed_replacement_d2_123):
    feature = _clean(ed_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_123'] = {'inputs': ['ed_replacement_d2_123'], 'func': ed_replacement_d3_123}


def ed_replacement_d3_124(ed_replacement_d2_124):
    feature = _clean(ed_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_124'] = {'inputs': ['ed_replacement_d2_124'], 'func': ed_replacement_d3_124}


def ed_replacement_d3_125(ed_replacement_d2_125):
    feature = _clean(ed_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_125'] = {'inputs': ['ed_replacement_d2_125'], 'func': ed_replacement_d3_125}


def ed_replacement_d3_126(ed_replacement_d2_126):
    feature = _clean(ed_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_126'] = {'inputs': ['ed_replacement_d2_126'], 'func': ed_replacement_d3_126}


def ed_replacement_d3_127(ed_replacement_d2_127):
    feature = _clean(ed_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_127'] = {'inputs': ['ed_replacement_d2_127'], 'func': ed_replacement_d3_127}


def ed_replacement_d3_128(ed_replacement_d2_128):
    feature = _clean(ed_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_128'] = {'inputs': ['ed_replacement_d2_128'], 'func': ed_replacement_d3_128}


def ed_replacement_d3_129(ed_replacement_d2_129):
    feature = _clean(ed_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_129'] = {'inputs': ['ed_replacement_d2_129'], 'func': ed_replacement_d3_129}


def ed_replacement_d3_130(ed_replacement_d2_130):
    feature = _clean(ed_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_130'] = {'inputs': ['ed_replacement_d2_130'], 'func': ed_replacement_d3_130}


def ed_replacement_d3_131(ed_replacement_d2_131):
    feature = _clean(ed_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_131'] = {'inputs': ['ed_replacement_d2_131'], 'func': ed_replacement_d3_131}


def ed_replacement_d3_132(ed_replacement_d2_132):
    feature = _clean(ed_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_132'] = {'inputs': ['ed_replacement_d2_132'], 'func': ed_replacement_d3_132}


def ed_replacement_d3_133(ed_replacement_d2_133):
    feature = _clean(ed_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_133'] = {'inputs': ['ed_replacement_d2_133'], 'func': ed_replacement_d3_133}


def ed_replacement_d3_134(ed_replacement_d2_134):
    feature = _clean(ed_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_134'] = {'inputs': ['ed_replacement_d2_134'], 'func': ed_replacement_d3_134}


def ed_replacement_d3_135(ed_replacement_d2_135):
    feature = _clean(ed_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_135'] = {'inputs': ['ed_replacement_d2_135'], 'func': ed_replacement_d3_135}


def ed_replacement_d3_136(ed_replacement_d2_136):
    feature = _clean(ed_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_136'] = {'inputs': ['ed_replacement_d2_136'], 'func': ed_replacement_d3_136}


def ed_replacement_d3_137(ed_replacement_d2_137):
    feature = _clean(ed_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_137'] = {'inputs': ['ed_replacement_d2_137'], 'func': ed_replacement_d3_137}


def ed_replacement_d3_138(ed_replacement_d2_138):
    feature = _clean(ed_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
ED_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ed_replacement_d3_138'] = {'inputs': ['ed_replacement_d2_138'], 'func': ed_replacement_d3_138}


# Third-derivative extensions for repaired first-base features.
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def evd_base_universe_d3_001_evd_002_pb_compression_z_42(evd_base_universe_d2_001_evd_002_pb_compression_z_42):
    return _base_universe_d3(evd_base_universe_d2_001_evd_002_pb_compression_z_42, 1)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_001_evd_002_pb_compression_z_42'] = {'inputs': ['evd_base_universe_d2_001_evd_002_pb_compression_z_42'], 'func': evd_base_universe_d3_001_evd_002_pb_compression_z_42}


def evd_base_universe_d3_002_evd_003_ps_compression_z_63(evd_base_universe_d2_002_evd_003_ps_compression_z_63):
    return _base_universe_d3(evd_base_universe_d2_002_evd_003_ps_compression_z_63, 2)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_002_evd_003_ps_compression_z_63'] = {'inputs': ['evd_base_universe_d2_002_evd_003_ps_compression_z_63'], 'func': evd_base_universe_d3_002_evd_003_ps_compression_z_63}


def evd_base_universe_d3_003_evd_005_ev_marketcap_gap_126(evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126):
    return _base_universe_d3(evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126, 3)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_003_evd_005_ev_marketcap_gap_126'] = {'inputs': ['evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126'], 'func': evd_base_universe_d3_003_evd_005_ev_marketcap_gap_126}


def evd_base_universe_d3_004_evd_006_dividend_yield_spike_189(evd_base_universe_d2_004_evd_006_dividend_yield_spike_189):
    return _base_universe_d3(evd_base_universe_d2_004_evd_006_dividend_yield_spike_189, 4)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_004_evd_006_dividend_yield_spike_189'] = {'inputs': ['evd_base_universe_d2_004_evd_006_dividend_yield_spike_189'], 'func': evd_base_universe_d3_004_evd_006_dividend_yield_spike_189}


def evd_base_universe_d3_005_evd_008_valuation_history_depth_378(evd_base_universe_d2_005_evd_008_valuation_history_depth_378):
    return _base_universe_d3(evd_base_universe_d2_005_evd_008_valuation_history_depth_378, 5)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_005_evd_008_valuation_history_depth_378'] = {'inputs': ['evd_base_universe_d2_005_evd_008_valuation_history_depth_378'], 'func': evd_base_universe_d3_005_evd_008_valuation_history_depth_378}


def evd_base_universe_d3_006_evd_009_pe_compression_z_504(evd_base_universe_d2_006_evd_009_pe_compression_z_504):
    return _base_universe_d3(evd_base_universe_d2_006_evd_009_pe_compression_z_504, 6)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_006_evd_009_pe_compression_z_504'] = {'inputs': ['evd_base_universe_d2_006_evd_009_pe_compression_z_504'], 'func': evd_base_universe_d3_006_evd_009_pe_compression_z_504}


def evd_base_universe_d3_007_evd_010_pb_compression_z_756(evd_base_universe_d2_007_evd_010_pb_compression_z_756):
    return _base_universe_d3(evd_base_universe_d2_007_evd_010_pb_compression_z_756, 7)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_007_evd_010_pb_compression_z_756'] = {'inputs': ['evd_base_universe_d2_007_evd_010_pb_compression_z_756'], 'func': evd_base_universe_d3_007_evd_010_pb_compression_z_756}


def evd_base_universe_d3_008_evd_011_ps_compression_z_1008(evd_base_universe_d2_008_evd_011_ps_compression_z_1008):
    return _base_universe_d3(evd_base_universe_d2_008_evd_011_ps_compression_z_1008, 8)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_008_evd_011_ps_compression_z_1008'] = {'inputs': ['evd_base_universe_d2_008_evd_011_ps_compression_z_1008'], 'func': evd_base_universe_d3_008_evd_011_ps_compression_z_1008}


def evd_base_universe_d3_009_evd_014_dividend_yield_spike_63(evd_base_universe_d2_009_evd_014_dividend_yield_spike_63):
    return _base_universe_d3(evd_base_universe_d2_009_evd_014_dividend_yield_spike_63, 9)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_009_evd_014_dividend_yield_spike_63'] = {'inputs': ['evd_base_universe_d2_009_evd_014_dividend_yield_spike_63'], 'func': evd_base_universe_d3_009_evd_014_dividend_yield_spike_63}


def evd_base_universe_d3_010_evd_016_valuation_history_depth_21(evd_base_universe_d2_010_evd_016_valuation_history_depth_21):
    return _base_universe_d3(evd_base_universe_d2_010_evd_016_valuation_history_depth_21, 10)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_010_evd_016_valuation_history_depth_21'] = {'inputs': ['evd_base_universe_d2_010_evd_016_valuation_history_depth_21'], 'func': evd_base_universe_d3_010_evd_016_valuation_history_depth_21}


def evd_base_universe_d3_011_evd_021_ev_marketcap_gap_189(evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189):
    return _base_universe_d3(evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189, 11)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_011_evd_021_ev_marketcap_gap_189'] = {'inputs': ['evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189'], 'func': evd_base_universe_d3_011_evd_021_ev_marketcap_gap_189}


def evd_base_universe_d3_012_evd_023_earnings_yield_spike_378(evd_base_universe_d2_012_evd_023_earnings_yield_spike_378):
    return _base_universe_d3(evd_base_universe_d2_012_evd_023_earnings_yield_spike_378, 12)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_012_evd_023_earnings_yield_spike_378'] = {'inputs': ['evd_base_universe_d2_012_evd_023_earnings_yield_spike_378'], 'func': evd_base_universe_d3_012_evd_023_earnings_yield_spike_378}


def evd_base_universe_d3_013_evd_024_valuation_history_depth_504(evd_base_universe_d2_013_evd_024_valuation_history_depth_504):
    return _base_universe_d3(evd_base_universe_d2_013_evd_024_valuation_history_depth_504, 13)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_013_evd_024_valuation_history_depth_504'] = {'inputs': ['evd_base_universe_d2_013_evd_024_valuation_history_depth_504'], 'func': evd_base_universe_d3_013_evd_024_valuation_history_depth_504}


def evd_base_universe_d3_014_evd_027_ps_compression_z_1260(evd_base_universe_d2_014_evd_027_ps_compression_z_1260):
    return _base_universe_d3(evd_base_universe_d2_014_evd_027_ps_compression_z_1260, 14)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_014_evd_027_ps_compression_z_1260'] = {'inputs': ['evd_base_universe_d2_014_evd_027_ps_compression_z_1260'], 'func': evd_base_universe_d3_014_evd_027_ps_compression_z_1260}


def evd_base_universe_d3_015_evd_029_ev_marketcap_gap_63(evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63):
    return _base_universe_d3(evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63, 15)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_015_evd_029_ev_marketcap_gap_63'] = {'inputs': ['evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63'], 'func': evd_base_universe_d3_015_evd_029_ev_marketcap_gap_63}


def evd_base_universe_d3_016_evd_031_earnings_yield_spike_21(evd_base_universe_d2_016_evd_031_earnings_yield_spike_21):
    return _base_universe_d3(evd_base_universe_d2_016_evd_031_earnings_yield_spike_21, 16)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_016_evd_031_earnings_yield_spike_21'] = {'inputs': ['evd_base_universe_d2_016_evd_031_earnings_yield_spike_21'], 'func': evd_base_universe_d3_016_evd_031_earnings_yield_spike_21}


def evd_base_universe_d3_017_evd_032_valuation_history_depth_42(evd_base_universe_d2_017_evd_032_valuation_history_depth_42):
    return _base_universe_d3(evd_base_universe_d2_017_evd_032_valuation_history_depth_42, 17)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_017_evd_032_valuation_history_depth_42'] = {'inputs': ['evd_base_universe_d2_017_evd_032_valuation_history_depth_42'], 'func': evd_base_universe_d3_017_evd_032_valuation_history_depth_42}


def evd_base_universe_d3_018_evd_035_ps_compression_z_126(evd_base_universe_d2_018_evd_035_ps_compression_z_126):
    return _base_universe_d3(evd_base_universe_d2_018_evd_035_ps_compression_z_126, 18)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_018_evd_035_ps_compression_z_126'] = {'inputs': ['evd_base_universe_d2_018_evd_035_ps_compression_z_126'], 'func': evd_base_universe_d3_018_evd_035_ps_compression_z_126}


def evd_base_universe_d3_019_evd_037_ev_marketcap_gap_252(evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252):
    return _base_universe_d3(evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252, 19)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_019_evd_037_ev_marketcap_gap_252'] = {'inputs': ['evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252'], 'func': evd_base_universe_d3_019_evd_037_ev_marketcap_gap_252}


def evd_base_universe_d3_020_evd_039_earnings_yield_spike_504(evd_base_universe_d2_020_evd_039_earnings_yield_spike_504):
    return _base_universe_d3(evd_base_universe_d2_020_evd_039_earnings_yield_spike_504, 20)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_020_evd_039_earnings_yield_spike_504'] = {'inputs': ['evd_base_universe_d2_020_evd_039_earnings_yield_spike_504'], 'func': evd_base_universe_d3_020_evd_039_earnings_yield_spike_504}


def evd_base_universe_d3_021_evd_040_valuation_history_depth_756(evd_base_universe_d2_021_evd_040_valuation_history_depth_756):
    return _base_universe_d3(evd_base_universe_d2_021_evd_040_valuation_history_depth_756, 21)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_021_evd_040_valuation_history_depth_756'] = {'inputs': ['evd_base_universe_d2_021_evd_040_valuation_history_depth_756'], 'func': evd_base_universe_d3_021_evd_040_valuation_history_depth_756}


def evd_base_universe_d3_022_evd_043_ps_compression_z_1512(evd_base_universe_d2_022_evd_043_ps_compression_z_1512):
    return _base_universe_d3(evd_base_universe_d2_022_evd_043_ps_compression_z_1512, 22)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_022_evd_043_ps_compression_z_1512'] = {'inputs': ['evd_base_universe_d2_022_evd_043_ps_compression_z_1512'], 'func': evd_base_universe_d3_022_evd_043_ps_compression_z_1512}


def evd_base_universe_d3_023_evd_047_earnings_yield_spike_42(evd_base_universe_d2_023_evd_047_earnings_yield_spike_42):
    return _base_universe_d3(evd_base_universe_d2_023_evd_047_earnings_yield_spike_42, 23)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_023_evd_047_earnings_yield_spike_42'] = {'inputs': ['evd_base_universe_d2_023_evd_047_earnings_yield_spike_42'], 'func': evd_base_universe_d3_023_evd_047_earnings_yield_spike_42}


def evd_base_universe_d3_024_evd_048_valuation_history_depth_63(evd_base_universe_d2_024_evd_048_valuation_history_depth_63):
    return _base_universe_d3(evd_base_universe_d2_024_evd_048_valuation_history_depth_63, 24)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_024_evd_048_valuation_history_depth_63'] = {'inputs': ['evd_base_universe_d2_024_evd_048_valuation_history_depth_63'], 'func': evd_base_universe_d3_024_evd_048_valuation_history_depth_63}


def evd_base_universe_d3_025_evd_051_ps_compression_z_189(evd_base_universe_d2_025_evd_051_ps_compression_z_189):
    return _base_universe_d3(evd_base_universe_d2_025_evd_051_ps_compression_z_189, 25)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_025_evd_051_ps_compression_z_189'] = {'inputs': ['evd_base_universe_d2_025_evd_051_ps_compression_z_189'], 'func': evd_base_universe_d3_025_evd_051_ps_compression_z_189}


def evd_base_universe_d3_026_evd_053_ev_marketcap_gap_378(evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378):
    return _base_universe_d3(evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378, 26)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_026_evd_053_ev_marketcap_gap_378'] = {'inputs': ['evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378'], 'func': evd_base_universe_d3_026_evd_053_ev_marketcap_gap_378}


def evd_base_universe_d3_027_evd_055_earnings_yield_spike_756(evd_base_universe_d2_027_evd_055_earnings_yield_spike_756):
    return _base_universe_d3(evd_base_universe_d2_027_evd_055_earnings_yield_spike_756, 27)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_027_evd_055_earnings_yield_spike_756'] = {'inputs': ['evd_base_universe_d2_027_evd_055_earnings_yield_spike_756'], 'func': evd_base_universe_d3_027_evd_055_earnings_yield_spike_756}


def evd_base_universe_d3_028_evd_056_valuation_history_depth_1008(evd_base_universe_d2_028_evd_056_valuation_history_depth_1008):
    return _base_universe_d3(evd_base_universe_d2_028_evd_056_valuation_history_depth_1008, 28)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_028_evd_056_valuation_history_depth_1008'] = {'inputs': ['evd_base_universe_d2_028_evd_056_valuation_history_depth_1008'], 'func': evd_base_universe_d3_028_evd_056_valuation_history_depth_1008}


def evd_base_universe_d3_029_evd_061_ev_marketcap_gap_21(evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21):
    return _base_universe_d3(evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21, 29)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_029_evd_061_ev_marketcap_gap_21'] = {'inputs': ['evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21'], 'func': evd_base_universe_d3_029_evd_061_ev_marketcap_gap_21}


def evd_base_universe_d3_030_evd_064_valuation_history_depth_84(evd_base_universe_d2_030_evd_064_valuation_history_depth_84):
    return _base_universe_d3(evd_base_universe_d2_030_evd_064_valuation_history_depth_84, 30)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_030_evd_064_valuation_history_depth_84'] = {'inputs': ['evd_base_universe_d2_030_evd_064_valuation_history_depth_84'], 'func': evd_base_universe_d3_030_evd_064_valuation_history_depth_84}


def evd_base_universe_d3_031_evd_067_ps_compression_z_252(evd_base_universe_d2_031_evd_067_ps_compression_z_252):
    return _base_universe_d3(evd_base_universe_d2_031_evd_067_ps_compression_z_252, 31)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_031_evd_067_ps_compression_z_252'] = {'inputs': ['evd_base_universe_d2_031_evd_067_ps_compression_z_252'], 'func': evd_base_universe_d3_031_evd_067_ps_compression_z_252}


def evd_base_universe_d3_032_evd_069_ev_marketcap_gap_504(evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504):
    return _base_universe_d3(evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504, 32)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_032_evd_069_ev_marketcap_gap_504'] = {'inputs': ['evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504'], 'func': evd_base_universe_d3_032_evd_069_ev_marketcap_gap_504}


def evd_base_universe_d3_033_evd_071_earnings_yield_spike_1008(evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008):
    return _base_universe_d3(evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008, 33)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_033_evd_071_earnings_yield_spike_1008'] = {'inputs': ['evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008'], 'func': evd_base_universe_d3_033_evd_071_earnings_yield_spike_1008}


def evd_base_universe_d3_034_evd_072_valuation_history_depth_1260(evd_base_universe_d2_034_evd_072_valuation_history_depth_1260):
    return _base_universe_d3(evd_base_universe_d2_034_evd_072_valuation_history_depth_1260, 34)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_034_evd_072_valuation_history_depth_1260'] = {'inputs': ['evd_base_universe_d2_034_evd_072_valuation_history_depth_1260'], 'func': evd_base_universe_d3_034_evd_072_valuation_history_depth_1260}


def evd_base_universe_d3_035_evd_basefill_004(evd_base_universe_d2_035_evd_basefill_004):
    return _base_universe_d3(evd_base_universe_d2_035_evd_basefill_004, 35)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_035_evd_basefill_004'] = {'inputs': ['evd_base_universe_d2_035_evd_basefill_004'], 'func': evd_base_universe_d3_035_evd_basefill_004}


def evd_base_universe_d3_036_evd_basefill_012(evd_base_universe_d2_036_evd_basefill_012):
    return _base_universe_d3(evd_base_universe_d2_036_evd_basefill_012, 36)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_036_evd_basefill_012'] = {'inputs': ['evd_base_universe_d2_036_evd_basefill_012'], 'func': evd_base_universe_d3_036_evd_basefill_012}


def evd_base_universe_d3_037_evd_basefill_015(evd_base_universe_d2_037_evd_basefill_015):
    return _base_universe_d3(evd_base_universe_d2_037_evd_basefill_015, 37)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_037_evd_basefill_015'] = {'inputs': ['evd_base_universe_d2_037_evd_basefill_015'], 'func': evd_base_universe_d3_037_evd_basefill_015}


def evd_base_universe_d3_038_evd_basefill_017(evd_base_universe_d2_038_evd_basefill_017):
    return _base_universe_d3(evd_base_universe_d2_038_evd_basefill_017, 38)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_038_evd_basefill_017'] = {'inputs': ['evd_base_universe_d2_038_evd_basefill_017'], 'func': evd_base_universe_d3_038_evd_basefill_017}


def evd_base_universe_d3_039_evd_basefill_018(evd_base_universe_d2_039_evd_basefill_018):
    return _base_universe_d3(evd_base_universe_d2_039_evd_basefill_018, 39)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_039_evd_basefill_018'] = {'inputs': ['evd_base_universe_d2_039_evd_basefill_018'], 'func': evd_base_universe_d3_039_evd_basefill_018}


def evd_base_universe_d3_040_evd_basefill_020(evd_base_universe_d2_040_evd_basefill_020):
    return _base_universe_d3(evd_base_universe_d2_040_evd_basefill_020, 40)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_040_evd_basefill_020'] = {'inputs': ['evd_base_universe_d2_040_evd_basefill_020'], 'func': evd_base_universe_d3_040_evd_basefill_020}


def evd_base_universe_d3_041_evd_basefill_022(evd_base_universe_d2_041_evd_basefill_022):
    return _base_universe_d3(evd_base_universe_d2_041_evd_basefill_022, 41)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_041_evd_basefill_022'] = {'inputs': ['evd_base_universe_d2_041_evd_basefill_022'], 'func': evd_base_universe_d3_041_evd_basefill_022}


def evd_base_universe_d3_042_evd_basefill_025(evd_base_universe_d2_042_evd_basefill_025):
    return _base_universe_d3(evd_base_universe_d2_042_evd_basefill_025, 42)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_042_evd_basefill_025'] = {'inputs': ['evd_base_universe_d2_042_evd_basefill_025'], 'func': evd_base_universe_d3_042_evd_basefill_025}


def evd_base_universe_d3_043_evd_basefill_026(evd_base_universe_d2_043_evd_basefill_026):
    return _base_universe_d3(evd_base_universe_d2_043_evd_basefill_026, 43)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_043_evd_basefill_026'] = {'inputs': ['evd_base_universe_d2_043_evd_basefill_026'], 'func': evd_base_universe_d3_043_evd_basefill_026}


def evd_base_universe_d3_044_evd_basefill_028(evd_base_universe_d2_044_evd_basefill_028):
    return _base_universe_d3(evd_base_universe_d2_044_evd_basefill_028, 44)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_044_evd_basefill_028'] = {'inputs': ['evd_base_universe_d2_044_evd_basefill_028'], 'func': evd_base_universe_d3_044_evd_basefill_028}


def evd_base_universe_d3_045_evd_basefill_030(evd_base_universe_d2_045_evd_basefill_030):
    return _base_universe_d3(evd_base_universe_d2_045_evd_basefill_030, 45)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_045_evd_basefill_030'] = {'inputs': ['evd_base_universe_d2_045_evd_basefill_030'], 'func': evd_base_universe_d3_045_evd_basefill_030}


def evd_base_universe_d3_046_evd_basefill_033(evd_base_universe_d2_046_evd_basefill_033):
    return _base_universe_d3(evd_base_universe_d2_046_evd_basefill_033, 46)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_046_evd_basefill_033'] = {'inputs': ['evd_base_universe_d2_046_evd_basefill_033'], 'func': evd_base_universe_d3_046_evd_basefill_033}


def evd_base_universe_d3_047_evd_basefill_034(evd_base_universe_d2_047_evd_basefill_034):
    return _base_universe_d3(evd_base_universe_d2_047_evd_basefill_034, 47)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_047_evd_basefill_034'] = {'inputs': ['evd_base_universe_d2_047_evd_basefill_034'], 'func': evd_base_universe_d3_047_evd_basefill_034}


def evd_base_universe_d3_048_evd_basefill_036(evd_base_universe_d2_048_evd_basefill_036):
    return _base_universe_d3(evd_base_universe_d2_048_evd_basefill_036, 48)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_048_evd_basefill_036'] = {'inputs': ['evd_base_universe_d2_048_evd_basefill_036'], 'func': evd_base_universe_d3_048_evd_basefill_036}


def evd_base_universe_d3_049_evd_basefill_038(evd_base_universe_d2_049_evd_basefill_038):
    return _base_universe_d3(evd_base_universe_d2_049_evd_basefill_038, 49)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_049_evd_basefill_038'] = {'inputs': ['evd_base_universe_d2_049_evd_basefill_038'], 'func': evd_base_universe_d3_049_evd_basefill_038}


def evd_base_universe_d3_050_evd_basefill_041(evd_base_universe_d2_050_evd_basefill_041):
    return _base_universe_d3(evd_base_universe_d2_050_evd_basefill_041, 50)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_050_evd_basefill_041'] = {'inputs': ['evd_base_universe_d2_050_evd_basefill_041'], 'func': evd_base_universe_d3_050_evd_basefill_041}


def evd_base_universe_d3_051_evd_basefill_042(evd_base_universe_d2_051_evd_basefill_042):
    return _base_universe_d3(evd_base_universe_d2_051_evd_basefill_042, 51)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_051_evd_basefill_042'] = {'inputs': ['evd_base_universe_d2_051_evd_basefill_042'], 'func': evd_base_universe_d3_051_evd_basefill_042}


def evd_base_universe_d3_052_evd_basefill_044(evd_base_universe_d2_052_evd_basefill_044):
    return _base_universe_d3(evd_base_universe_d2_052_evd_basefill_044, 52)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_052_evd_basefill_044'] = {'inputs': ['evd_base_universe_d2_052_evd_basefill_044'], 'func': evd_base_universe_d3_052_evd_basefill_044}


def evd_base_universe_d3_053_evd_basefill_045(evd_base_universe_d2_053_evd_basefill_045):
    return _base_universe_d3(evd_base_universe_d2_053_evd_basefill_045, 53)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_053_evd_basefill_045'] = {'inputs': ['evd_base_universe_d2_053_evd_basefill_045'], 'func': evd_base_universe_d3_053_evd_basefill_045}


def evd_base_universe_d3_054_evd_basefill_046(evd_base_universe_d2_054_evd_basefill_046):
    return _base_universe_d3(evd_base_universe_d2_054_evd_basefill_046, 54)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_054_evd_basefill_046'] = {'inputs': ['evd_base_universe_d2_054_evd_basefill_046'], 'func': evd_base_universe_d3_054_evd_basefill_046}


def evd_base_universe_d3_055_evd_basefill_049(evd_base_universe_d2_055_evd_basefill_049):
    return _base_universe_d3(evd_base_universe_d2_055_evd_basefill_049, 55)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_055_evd_basefill_049'] = {'inputs': ['evd_base_universe_d2_055_evd_basefill_049'], 'func': evd_base_universe_d3_055_evd_basefill_049}


def evd_base_universe_d3_056_evd_basefill_050(evd_base_universe_d2_056_evd_basefill_050):
    return _base_universe_d3(evd_base_universe_d2_056_evd_basefill_050, 56)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_056_evd_basefill_050'] = {'inputs': ['evd_base_universe_d2_056_evd_basefill_050'], 'func': evd_base_universe_d3_056_evd_basefill_050}


def evd_base_universe_d3_057_evd_basefill_052(evd_base_universe_d2_057_evd_basefill_052):
    return _base_universe_d3(evd_base_universe_d2_057_evd_basefill_052, 57)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_057_evd_basefill_052'] = {'inputs': ['evd_base_universe_d2_057_evd_basefill_052'], 'func': evd_base_universe_d3_057_evd_basefill_052}


def evd_base_universe_d3_058_evd_basefill_054(evd_base_universe_d2_058_evd_basefill_054):
    return _base_universe_d3(evd_base_universe_d2_058_evd_basefill_054, 58)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_058_evd_basefill_054'] = {'inputs': ['evd_base_universe_d2_058_evd_basefill_054'], 'func': evd_base_universe_d3_058_evd_basefill_054}


def evd_base_universe_d3_059_evd_basefill_057(evd_base_universe_d2_059_evd_basefill_057):
    return _base_universe_d3(evd_base_universe_d2_059_evd_basefill_057, 59)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_059_evd_basefill_057'] = {'inputs': ['evd_base_universe_d2_059_evd_basefill_057'], 'func': evd_base_universe_d3_059_evd_basefill_057}


def evd_base_universe_d3_060_evd_basefill_058(evd_base_universe_d2_060_evd_basefill_058):
    return _base_universe_d3(evd_base_universe_d2_060_evd_basefill_058, 60)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_060_evd_basefill_058'] = {'inputs': ['evd_base_universe_d2_060_evd_basefill_058'], 'func': evd_base_universe_d3_060_evd_basefill_058}


def evd_base_universe_d3_061_evd_basefill_059(evd_base_universe_d2_061_evd_basefill_059):
    return _base_universe_d3(evd_base_universe_d2_061_evd_basefill_059, 61)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_061_evd_basefill_059'] = {'inputs': ['evd_base_universe_d2_061_evd_basefill_059'], 'func': evd_base_universe_d3_061_evd_basefill_059}


def evd_base_universe_d3_062_evd_basefill_060(evd_base_universe_d2_062_evd_basefill_060):
    return _base_universe_d3(evd_base_universe_d2_062_evd_basefill_060, 62)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_062_evd_basefill_060'] = {'inputs': ['evd_base_universe_d2_062_evd_basefill_060'], 'func': evd_base_universe_d3_062_evd_basefill_060}


def evd_base_universe_d3_063_evd_basefill_062(evd_base_universe_d2_063_evd_basefill_062):
    return _base_universe_d3(evd_base_universe_d2_063_evd_basefill_062, 63)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_063_evd_basefill_062'] = {'inputs': ['evd_base_universe_d2_063_evd_basefill_062'], 'func': evd_base_universe_d3_063_evd_basefill_062}


def evd_base_universe_d3_064_evd_basefill_063(evd_base_universe_d2_064_evd_basefill_063):
    return _base_universe_d3(evd_base_universe_d2_064_evd_basefill_063, 64)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_064_evd_basefill_063'] = {'inputs': ['evd_base_universe_d2_064_evd_basefill_063'], 'func': evd_base_universe_d3_064_evd_basefill_063}


def evd_base_universe_d3_065_evd_basefill_065(evd_base_universe_d2_065_evd_basefill_065):
    return _base_universe_d3(evd_base_universe_d2_065_evd_basefill_065, 65)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_065_evd_basefill_065'] = {'inputs': ['evd_base_universe_d2_065_evd_basefill_065'], 'func': evd_base_universe_d3_065_evd_basefill_065}


def evd_base_universe_d3_066_evd_basefill_066(evd_base_universe_d2_066_evd_basefill_066):
    return _base_universe_d3(evd_base_universe_d2_066_evd_basefill_066, 66)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_066_evd_basefill_066'] = {'inputs': ['evd_base_universe_d2_066_evd_basefill_066'], 'func': evd_base_universe_d3_066_evd_basefill_066}


def evd_base_universe_d3_067_evd_basefill_068(evd_base_universe_d2_067_evd_basefill_068):
    return _base_universe_d3(evd_base_universe_d2_067_evd_basefill_068, 67)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_067_evd_basefill_068'] = {'inputs': ['evd_base_universe_d2_067_evd_basefill_068'], 'func': evd_base_universe_d3_067_evd_basefill_068}


def evd_base_universe_d3_068_evd_basefill_070(evd_base_universe_d2_068_evd_basefill_070):
    return _base_universe_d3(evd_base_universe_d2_068_evd_basefill_070, 68)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_068_evd_basefill_070'] = {'inputs': ['evd_base_universe_d2_068_evd_basefill_070'], 'func': evd_base_universe_d3_068_evd_basefill_070}


def evd_base_universe_d3_069_evd_basefill_073(evd_base_universe_d2_069_evd_basefill_073):
    return _base_universe_d3(evd_base_universe_d2_069_evd_basefill_073, 69)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_069_evd_basefill_073'] = {'inputs': ['evd_base_universe_d2_069_evd_basefill_073'], 'func': evd_base_universe_d3_069_evd_basefill_073}


def evd_base_universe_d3_070_evd_basefill_074(evd_base_universe_d2_070_evd_basefill_074):
    return _base_universe_d3(evd_base_universe_d2_070_evd_basefill_074, 70)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_070_evd_basefill_074'] = {'inputs': ['evd_base_universe_d2_070_evd_basefill_074'], 'func': evd_base_universe_d3_070_evd_basefill_074}


def evd_base_universe_d3_071_evd_basefill_075(evd_base_universe_d2_071_evd_basefill_075):
    return _base_universe_d3(evd_base_universe_d2_071_evd_basefill_075, 71)
EVD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evd_base_universe_d3_071_evd_basefill_075'] = {'inputs': ['evd_base_universe_d2_071_evd_basefill_075'], 'func': evd_base_universe_d3_071_evd_basefill_075}
