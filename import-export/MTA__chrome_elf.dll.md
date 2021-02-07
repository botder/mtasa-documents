# chrome_elf.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (155)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 0 | AcquireSRWLockExclusive |
| 136 | CloseHandle |
| 157 | CompareStringW |
| 188 | CreateDirectoryW |
| 193 | CreateEventW |
| 205 | CreateFileW |
| 220 | CreateMutexW |
| 222 | CreateNamedPipeW |
| 231 | CreateProcessW |
| 233 | CreateRemoteThread |
| 245 | CreateThread |
| 267 | DecodePointer |
| 274 | DeleteCriticalSection |
| 279 | DeleteFileW |
| 301 | DuplicateHandle |
| 303 | EncodePointer |
| 307 | EnterCriticalSection |
| 342 | EnumSystemLocalesW |
| 352 | ExitProcess |
| 356 | ExpandEnvironmentStringsW |
| 364 | FileTimeToSystemTime |
| 375 | FindClose |
| 381 | FindFirstFileExW |
| 398 | FindNextFileW |
| 417 | FlushFileBuffers |
| 424 | FormatMessageA |
| 428 | FreeEnvironmentStringsW |
| 429 | FreeLibrary |
| 436 | GetACP |
| 451 | GetCPInfo |
| 472 | GetCommandLineA |
| 473 | GetCommandLineW |
| 480 | GetComputerNameExW |
| 510 | GetConsoleMode |
| 514 | GetConsoleOutputCP |
| 531 | GetCurrentDirectoryW |
| 537 | GetCurrentProcess |
| 538 | GetCurrentProcessId |
| 541 | GetCurrentThread |
| 542 | GetCurrentThreadId |
| 547 | GetDateFormatW |
| 561 | GetDriveTypeW |
| 569 | GetEnvironmentStringsW |
| 571 | GetEnvironmentVariableW |
| 583 | GetFileAttributesW |
| 585 | GetFileInformationByHandle |
| 590 | GetFileSizeEx |
| 591 | GetFileTime |
| 592 | GetFileType |
| 603 | GetFullPathNameW |
| 611 | GetLastError |
| 612 | GetLocalTime |
| 615 | GetLocaleInfoW |
| 624 | GetLongPathNameW |
| 630 | GetModuleFileNameW |
| 631 | GetModuleHandleA |
| 633 | GetModuleHandleExW |
| 634 | GetModuleHandleW |
| 647 | GetNativeSystemInfo |
| 665 | GetOEMCP |
| 688 | GetProcAddress |
| 694 | GetProcessHeap |
| 696 | GetProcessId |
| 704 | GetProcessTimes |
| 709 | GetProductInfo |
| 722 | GetStartupInfoW |
| 724 | GetStdHandle |
| 729 | GetStringTypeW |
| 741 | GetSystemInfo |
| 747 | GetSystemTimeAsFileTime |
| 760 | GetTempPathW |
| 766 | GetThreadId |
| 771 | GetThreadPriority |
| 777 | GetTickCount |
| 782 | GetTimeFormatW |
| 784 | GetTimeZoneInformation |
| 788 | GetUserDefaultLCID |
| 795 | GetVersion |
| 797 | GetVersionExW |
| 839 | HeapAlloc |
| 843 | HeapFree |
| 846 | HeapReAlloc |
| 848 | HeapSize |
| 859 | InitOnceExecuteOnce |
| 864 | InitializeCriticalSection |
| 865 | InitializeCriticalSectionAndSpinCount |
| 869 | InitializeSListHead |
| 878 | InterlockedFlushSList |
| 897 | IsDebuggerPresent |
| 904 | IsProcessorFeaturePresent |
| 910 | IsValidCodePage |
| 912 | IsValidLocale |
| 916 | IsWow64Process |
| 948 | LCMapStringW |
| 960 | LeaveCriticalSection |
| 965 | LoadLibraryExA |
| 966 | LoadLibraryExW |
| 967 | LoadLibraryW |
| 978 | LocalFree |
| 989 | LockFileEx |
| 1010 | MultiByteToWideChar |
| 1038 | OpenProcess |
| 1049 | OutputDebugStringA |
| 1050 | OutputDebugStringW |
| 1059 | PeekNamedPipe |
| 1102 | QueryPerformanceCounter |
| 1103 | QueryPerformanceFrequency |
| 1107 | QueryThreadCycleTime |
| 1123 | RaiseException |
| 1137 | ReadConsoleW |
| 1140 | ReadFile |
| 1143 | ReadProcessMemory |
| 1201 | ReleaseMutex |
| 1203 | ReleaseSRWLockExclusive |
| 1210 | RemoveDirectoryW |
| 1223 | ResetEvent |
| 1232 | RtlCaptureStackBackTrace |
| 1236 | RtlUnwind |
| 1258 | SetConsoleCtrlHandler |
| 1297 | SetEndOfFile |
| 1301 | SetEnvironmentVariableW |
| 1303 | SetEvent |
| 1316 | SetFilePointerEx |
| 1331 | SetLastError |
| 1340 | SetNamedPipeHandleState |
| 1356 | SetStdHandle |
| 1376 | SetThreadPriority |
| 1391 | SetUnhandledExceptionFilter |
| 1407 | Sleep |
| 1409 | SleepConditionVariableSRW |
| 1410 | SleepEx |
| 1419 | SystemTimeToTzSpecificLocalTime |
| 1422 | TerminateProcess |
| 1440 | TlsAlloc |
| 1441 | TlsFree |
| 1442 | TlsGetValue |
| 1443 | TlsSetValue |
| 1445 | TransactNamedPipe |
| 1447 | TryAcquireSRWLockExclusive |
| 1455 | UnhandledExceptionFilter |
| 1457 | UnlockFileEx |
| 1475 | VerSetConditionMask |
| 1479 | VerifyVersionInfoW |
| 1486 | VirtualProtect |
| 1487 | VirtualProtectEx |
| 1488 | VirtualQuery |
| 1497 | WaitForSingleObject |
| 1498 | WaitForSingleObjectEx |
| 1504 | WaitNamedPipeW |
| 1505 | WakeAllConditionVariable |
| 1536 | WideCharToMultiByte |
| 1555 | WriteConsoleW |
| 1556 | WriteFile |
| 1565 | WriteProcessMemory |
| 1588 | lstrcmpiA |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (10)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 0 | BuildExplicitAccessWithNameW |
| 0 | BuildSecurityDescriptorW |
| 0 | ConvertStringSecurityDescriptorToSecurityDescriptorW |
| 0 | EventRegister |
| 0 | EventUnregister |
| 0 | EventWrite |
| 0 | RegCloseKey |
| 0 | RegOpenKeyExW |
| 0 | RegQueryValueExW |
| 0 | SystemFunction036 |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 0 | timeGetTime |

</p></details>
<details><summary><b>dbghelp.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 0 | MiniDumpWriteDump |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 0 |  |
| 1 | ClearReportsBetween_ExportThunk |
| 2 | CrashForException_ExportThunk |
| 3 | DisableHook |
| 4 | DrainLog |
| 5 | DumpHungProcessWithPtype_ExportThunk |
| 6 | DumpProcessWithoutCrash |
| 7 | GetApplyHookResult |
| 8 | GetBlockedModulesCount |
| 9 | GetCrashReports_ExportThunk |
| 10 | GetCrashpadDatabasePath_ExportThunk |
| 11 | GetHandleVerifier |
| 12 | GetInstallDetailsPayload |
| 13 | GetUniqueBlockedModulesCount |
| 14 | GetUserDataDirectoryThunk |
| 15 | InjectDumpForHungInput_ExportThunk |
| 16 | IsCrashReportingEnabledImpl |
| 17 | IsThirdPartyInitialized |
| 18 | RegisterLogNotification |
| 19 | RequestSingleCrashUpload_ExportThunk |
| 20 | SetCrashKeyValueImpl |
| 21 | SetMetricsClientId |
| 22 | SetUploadConsent_ExportThunk |
| 23 | SignalChromeElf |
| 24 | SignalInitializeCrashReporting |

</p></details>
