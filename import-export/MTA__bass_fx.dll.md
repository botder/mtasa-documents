# bass_fx.dll

## Imports

<details><summary><b>bass.dll</b> (22)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 97 | BASS_StreamGetFilePosition |
| 34 | BASS_ChannelSetSync |
| 5 | BASS_ChannelGetAttribute |
| 15 | BASS_ChannelIsActive |
| 2 | BASS_ChannelFlags |
| 23 | BASS_ChannelRemoveSync |
| 14 | BASS_ChannelGetTags |
| 10 | BASS_ChannelGetLength |
| 38 | BASS_ErrorGetCode |
| 20 | BASS_ChannelRemoveDSP |
| 9 | BASS_ChannelGetInfo |
| 29 | BASS_ChannelSetDSP |
| 47 | BASS_GetConfig |
| 7 | BASS_ChannelGetData |
| 33 | BASS_ChannelSetPosition |
| 1 | BASS_ChannelBytes2Seconds |
| 24 | BASS_ChannelSeconds2Bytes |
| 96 | BASS_StreamFree |
| 57 | BASS_MusicFree |
| 54 | BASS_GetVersion |
| 13 | BASS_ChannelGetPosition |
| 101 | _ |

</p></details>
<details><summary><b>KERNEL32.dll</b> (19)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 633 | GetSystemTimeAsFileTime |
| 1048 | RtlUnwind |
| 748 | InterlockedExchange |
| 745 | InterlockedCompareExchange |
| 1216 | TerminateProcess |
| 448 | GetCurrentProcess |
| 1235 | UnhandledExceptionFilter |
| 1189 | SetUnhandledExceptionFilter |
| 674 | GetVersion |
| 935 | QueryPerformanceCounter |
| 659 | GetTickCount |
| 453 | GetCurrentThreadId |
| 449 | GetCurrentProcessId |
| 238 | EnterCriticalSection |
| 825 | LeaveCriticalSection |
| 1202 | Sleep |
| 209 | DeleteCriticalSection |
| 222 | DisableThreadLibraryCalls |
| 738 | InitializeCriticalSection |

</p></details>
<details><summary><b>USER32.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 764 | TranslateMessage |
| 562 | PeekMessageA |
| 174 | DispatchMessageA |
| 526 | MessageBoxA |

</p></details>
<details><summary><b>msvcrt.dll</b> (17)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 1246 | malloc |
| 1279 | realloc |
| 20 | ??3@YAXPAX@Z |
| 1190 | free |
| 1157 | calloc |
| 764 | _purecall |
| 1262 | memset |
| 1258 | memcpy |
| 106 | _XcptFilter |
| 469 | _initterm |
| 257 | _amsg_exit |
| 245 | _adjust_fdiv |
| 1260 | memmove |
| 18 | ??2@YAPAXI@Z |
| 68 | _CIpow |
| 64 | _CIexp |
| 70 | _CIsinh |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | BASS_FX_BPM_BeatCallbackReset |
| 2 | BASS_FX_BPM_BeatCallbackSet |
| 3 | BASS_FX_BPM_BeatDecodeGet |
| 4 | BASS_FX_BPM_BeatFree |
| 5 | BASS_FX_BPM_BeatGetParameters |
| 6 | BASS_FX_BPM_BeatSetParameters |
| 7 | BASS_FX_BPM_CallbackReset |
| 8 | BASS_FX_BPM_CallbackSet |
| 9 | BASS_FX_BPM_DecodeGet |
| 10 | BASS_FX_BPM_Free |
| 11 | BASS_FX_BPM_Translate |
| 12 | BASS_FX_GetVersion |
| 13 | BASS_FX_ReverseCreate |
| 14 | BASS_FX_ReverseGetSource |
| 15 | BASS_FX_TempoCreate |
| 16 | BASS_FX_TempoGetRateRatio |
| 17 | BASS_FX_TempoGetSource |

</p></details>
