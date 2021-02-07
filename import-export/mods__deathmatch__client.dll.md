# client.dll

## Imports

<details><summary><b>bass.dll</b> (34)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 13 | BASS_ChannelGetPosition |
| 38 | BASS_ErrorGetCode |
| 59 | BASS_MusicLoad |
| 94 | BASS_StreamCreate |
| 95 | BASS_StreamCreateFile |
| 97 | BASS_StreamCreateURL |
| 98 | BASS_StreamFree |
| 99 | BASS_StreamGetFilePosition |
| 100 | BASS_StreamPutData |
| 1 | BASS_ChannelBytes2Seconds |
| 24 | BASS_ChannelSeconds2Bytes |
| 9 | BASS_ChannelGetInfo |
| 64 | BASS_PluginLoad |
| 93 | BASS_Stop |
| 14 | BASS_ChannelGetTags |
| 56 | BASS_Init |
| 88 | BASS_SetConfigPtr |
| 47 | BASS_GetConfig |
| 87 | BASS_SetConfig |
| 21 | BASS_ChannelRemoveFX |
| 31 | BASS_ChannelSetFX |
| 23 | BASS_ChannelRemoveSync |
| 34 | BASS_ChannelSetSync |
| 7 | BASS_ChannelGetData |
| 11 | BASS_ChannelGetLevel |
| 43 | BASS_Free |
| 33 | BASS_ChannelSetPosition |
| 10 | BASS_ChannelGetLength |
| 5 | BASS_ChannelGetAttribute |
| 27 | BASS_ChannelSetAttribute |
| 18 | BASS_ChannelPause |
| 36 | BASS_ChannelStop |
| 19 | BASS_ChannelPlay |
| 2 | BASS_ChannelFlags |

</p></details>
<details><summary><b>BASS_FX.dll</b> (8)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 1 | BASS_FX_BPM_BeatCallbackSet |
| 9 | BASS_FX_BPM_Free |
| 7 | BASS_FX_BPM_CallbackSet |
| 8 | BASS_FX_BPM_DecodeGet |
| 12 | BASS_FX_ReverseCreate |
| 16 | BASS_FX_TempoGetSource |
| 14 | BASS_FX_TempoCreate |
| 3 | BASS_FX_BPM_BeatFree |

</p></details>
<details><summary><b>bassmix.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 20 | BASS_Mixer_StreamCreate |
| 18 | BASS_Mixer_StreamAddChannel |

</p></details>
<details><summary><b>tags.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 2 | TAGS_Read |

</p></details>
<details><summary><b>KERNEL32.dll</b> (162)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 844 | HeapReAlloc |
| 782 | GetTimeZoneInformation |
| 340 | EnumSystemLocalesW |
| 786 | GetUserDefaultLCID |
| 909 | IsValidLocale |
| 780 | GetTimeFormatW |
| 545 | GetDateFormatW |
| 415 | FlushFileBuffers |
| 1315 | SetFilePointerEx |
| 837 | HeapAlloc |
| 841 | HeapFree |
| 490 | GetConsoleCP |
| 1554 | WriteFile |
| 1136 | ReadConsoleW |
| 508 | GetConsoleMode |
| 229 | CreateProcessW |
| 572 | GetExitCodeProcess |
| 221 | CreatePipe |
| 1354 | SetStdHandle |
| 1296 | SetEndOfFile |
| 846 | HeapSize |
| 379 | FindFirstFileExW |
| 588 | GetFileSizeEx |
| 907 | IsValidCodePage |
| 350 | ExitProcess |
| 1553 | WriteConsoleW |
| 590 | GetFileType |
| 722 | GetStdHandle |
| 631 | GetModuleHandleExW |
| 203 | CreateFileW |
| 373 | FindClose |
| 384 | FindFirstFileW |
| 396 | FindNextFileW |
| 576 | GetFileAttributesA |
| 578 | GetFileAttributesExW |
| 601 | GetFullPathNameW |
| 622 | GetLongPathNameW |
| 1139 | ReadFile |
| 1306 | SetFileAttributesA |
| 758 | GetTempPathW |
| 134 | CloseHandle |
| 434 | GetACP |
| 1101 | QueryPerformanceCounter |
| 1102 | QueryPerformanceFrequency |
| 862 | InitializeCriticalSection |
| 305 | EnterCriticalSection |
| 957 | LeaveCriticalSection |
| 272 | DeleteCriticalSection |
| 1495 | WaitForSingleObject |
| 535 | GetCurrentProcess |
| 536 | GetCurrentProcessId |
| 1420 | TerminateProcess |
| 539 | GetCurrentThread |
| 540 | GetCurrentThreadId |
| 1044 | OpenThread |
| 773 | GetThreadTimes |
| 1037 | OpenProcess |
| 743 | GetSystemTime |
| 610 | GetLocalTime |
| 628 | GetModuleFileNameW |
| 629 | GetModuleHandleA |
| 686 | GetProcAddress |
| 961 | LoadLibraryA |
| 813 | GlobalAlloc |
| 831 | GlobalUnlock |
| 824 | GlobalLock |
| 975 | LocalFree |
| 1000 | MoveFileExW |
| 252 | CreateToolhelp32Snapshot |
| 1068 | Process32FirstW |
| 1070 | Process32NextW |
| 1436 | Thread32First |
| 1437 | Thread32Next |
| 931 | K32GetModuleFileNameExW |
| 932 | K32GetModuleInformation |
| 243 | CreateThread |
| 427 | FreeLibrary |
| 251 | CreateTimerQueueTimer |
| 282 | DeleteTimerQueueTimer |
| 1405 | Sleep |
| 573 | GetExitCodeThread |
| 1374 | SetThreadPriority |
| 1229 | ResumeThread |
| 612 | GetLocaleInfoEx |
| 627 | GetModuleFileNameA |
| 422 | FormatMessageA |
| 617 | GetLogicalProcessorInformation |
| 351 | ExitThread |
| 186 | CreateDirectoryW |
| 1300 | SetEnvironmentVariableW |
| 277 | DeleteFileW |
| 1235 | RtlUnwind |
| 1122 | RaiseException |
| 964 | LoadLibraryW |
| 1463 | UnregisterWaitEx |
| 1091 | QueryDepthSList |
| 876 | InterlockedFlushSList |
| 663 | GetOEMCP |
| 470 | GetCommandLineA |
| 471 | GetCommandLineW |
| 567 | GetEnvironmentStringsW |
| 426 | FreeEnvironmentStringsW |
| 692 | GetProcessHeap |
| 609 | GetLastError |
| 769 | GetThreadPriority |
| 1403 | SignalObjectAndWait |
| 250 | CreateTimerQueue |
| 720 | GetStartupInfoW |
| 879 | InterlockedPushEntrySList |
| 878 | InterlockedPopEntrySList |
| 1204 | ReleaseSemaphore |
| 299 | DuplicateHandle |
| 1481 | VirtualFree |
| 1484 | VirtualProtect |
| 1478 | VirtualAlloc |
| 795 | GetVersionExW |
| 963 | LoadLibraryExW |
| 428 | FreeLibraryAndExitThread |
| 1049 | OutputDebugStringW |
| 1462 | UnregisterWait |
| 1193 | RegisterWaitForSingleObject |
| 1363 | SetThreadAffinityMask |
| 687 | GetProcessAffinityMask |
| 649 | GetNumaHighestNodeNumber |
| 793 | GetVersion |
| 820 | GlobalFree |
| 568 | GetEnvironmentVariableA |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 188 | CreateEventA |
| 794 | GetVersionExA |
| 970 | LocalAlloc |
| 1330 | SetLastError |
| 1496 | WaitForSingleObjectEx |
| 1415 | SwitchToThread |
| 1447 | TryEnterCriticalSection |
| 1202 | ReleaseSRWLockExclusive |
| 1445 | TryAcquireSRWLockExclusive |
| 1534 | WideCharToMultiByte |
| 863 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1438 | TlsAlloc |
| 1440 | TlsGetValue |
| 1441 | TlsSetValue |
| 1439 | TlsFree |
| 745 | GetSystemTimeAsFileTime |
| 775 | GetTickCount |
| 632 | GetModuleHandleW |
| 301 | EncodePointer |
| 265 | DecodePointer |
| 1007 | MultiByteToWideChar |
| 155 | CompareStringW |
| 945 | LCMapStringW |
| 613 | GetLocaleInfoW |
| 727 | GetStringTypeW |
| 449 | GetCPInfo |
| 1453 | UnhandledExceptionFilter |
| 1389 | SetUnhandledExceptionFilter |
| 902 | IsProcessorFeaturePresent |
| 867 | InitializeSListHead |
| 895 | IsDebuggerPresent |
| 120 | ChangeTimerQueueTimer |

</p></details>
<details><summary><b>USER32.dll</b> (12)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 319 | GetCursorPos |
| 278 | FlashWindowEx |
| 289 | GetAsyncKeyState |
| 323 | GetDesktopWindow |
| 77 | ClientToScreen |
| 663 | OpenClipboard |
| 79 | CloseClipboard |
| 788 | SetActiveWindow |
| 232 | EmptyClipboard |
| 646 | MessageBoxW |
| 814 | SetFocus |
| 795 | SetClipboardData |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (9)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 681 | RegSetValueExW |
| 210 | CryptGenRandom |
| 220 | CryptReleaseContext |
| 193 | CryptAcquireContextA |
| 665 | RegQueryValueExW |
| 652 | RegOpenKeyExW |
| 638 | RegFlushKey |
| 612 | RegCreateKeyExW |
| 603 | RegCloseKey |

</p></details>
<details><summary><b>SHELL32.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 321 | SHFileOperationW |
| 344 | SHGetFolderPathW |

</p></details>
<details><summary><b>pcre3.dll</b> (8)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 76 | ?FindAndConsume@RE@pcrecpp@@QBE_NPAVStringPiece@2@ABVArg@2@111111111111111@Z |
| 87 | ?PartialMatch@RE@pcrecpp@@QBE_NABVStringPiece@2@ABVArg@2@111111111111111@Z |
| 110 | ?no_arg@RE@pcrecpp@@2VArg@2@A |
| 80 | ?GlobalReplace@RE@pcrecpp@@QBEHABVStringPiece@2@PAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z |
| 47 | ??1RE@pcrecpp@@QAE@XZ |
| 32 | ??0RE@pcrecpp@@QAE@ABV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@ABVRE_Options@1@@Z |
| 42 | ??0StringPiece@pcrecpp@@QAE@ABV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z |
| 136 | ?parse_string@Arg@pcrecpp@@CA_NPBDHPAX@Z |

</p></details>
<details><summary><b>WINMM.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 148 | timeGetTime |
| 150 | timeSetEvent |
| 149 | timeKillEvent |

</p></details>
<details><summary><b>ole32.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 93 | CoInitialize |
| 141 | CoUninitialize |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | GetLibMtaVersion |
| 2 | InitClient |
| 3 | _json_c_strerror |
| 4 | json_c_object_sizeof |
| 5 | json_c_set_serialization_double_format |
| 6 | json_c_shallow_copy_default |
| 7 | json_object_array_add |
| 8 | json_object_array_bsearch |
| 9 | json_object_array_del_idx |
| 10 | json_object_array_get_idx |
| 11 | json_object_array_length |
| 12 | json_object_array_put_idx |
| 13 | json_object_array_shrink |
| 14 | json_object_array_sort |
| 15 | json_object_deep_copy |
| 16 | json_object_double_to_json_string |
| 17 | json_object_equal |
| 18 | json_object_free_userdata |
| 19 | json_object_from_fd |
| 20 | json_object_from_fd_ex |
| 21 | json_object_from_file |
| 22 | json_object_get |
| 23 | json_object_get_array |
| 24 | json_object_get_boolean |
| 25 | json_object_get_double |
| 26 | json_object_get_int |
| 27 | json_object_get_int64 |
| 28 | json_object_get_object |
| 29 | json_object_get_string |
| 30 | json_object_get_string_len |
| 31 | json_object_get_type |
| 32 | json_object_get_uint64 |
| 33 | json_object_get_userdata |
| 34 | json_object_int_inc |
| 35 | json_object_is_type |
| 36 | json_object_new_array |
| 37 | json_object_new_array_ext |
| 38 | json_object_new_boolean |
| 39 | json_object_new_double |
| 40 | json_object_new_double_s |
| 41 | json_object_new_int |
| 42 | json_object_new_int64 |
| 43 | json_object_new_null |
| 44 | json_object_new_object |
| 45 | json_object_new_string |
| 46 | json_object_new_string_len |
| 47 | json_object_new_uint64 |
| 48 | json_object_object_add |
| 49 | json_object_object_add_ex |
| 50 | json_object_object_del |
| 51 | json_object_object_get |
| 52 | json_object_object_get_ex |
| 53 | json_object_object_length |
| 54 | json_object_put |
| 55 | json_object_set_boolean |
| 56 | json_object_set_double |
| 57 | json_object_set_int |
| 58 | json_object_set_int64 |
| 59 | json_object_set_serializer |
| 60 | json_object_set_string |
| 61 | json_object_set_string_len |
| 62 | json_object_set_uint64 |
| 63 | json_object_set_userdata |
| 64 | json_object_to_fd |
| 65 | json_object_to_file |
| 66 | json_object_to_file_ext |
| 67 | json_object_to_json_string |
| 68 | json_object_to_json_string_ext |
| 69 | json_object_to_json_string_length |
| 70 | json_object_userdata_to_json_string |
| 71 | json_parse_double |
| 72 | json_parse_int64 |
| 73 | json_parse_uint64 |
| 74 | json_tokener_error_desc |
| 75 | json_tokener_free |
| 76 | json_tokener_get_error |
| 77 | json_tokener_get_parse_end |
| 78 | json_tokener_new |
| 79 | json_tokener_new_ex |
| 80 | json_tokener_parse |
| 81 | json_tokener_parse_ex |
| 82 | json_tokener_parse_verbose |
| 83 | json_tokener_reset |
| 84 | json_tokener_set_flags |
| 85 | json_type_to_name |
| 86 | json_util_get_last_err |
| 87 | printbuf_free |
| 88 | printbuf_memappend |
| 89 | printbuf_memset |
| 90 | printbuf_new |
| 91 | printbuf_reset |
| 92 | sprintbuf |

</p></details>
