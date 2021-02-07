# net.dll

## Imports

<details><summary><b>WS2_32.dll</b> (33)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 16 |  |
| 116 |  |
| 115 |  |
| 111 |  |
| 57 |  |
| 23 |  |
| 21 |  |
| 20 |  |
| 19 |  |
| 17 |  |
| 5 |  |
| 13 |  |
| 58 | WSAIoctl |
| 6 |  |
| 10 |  |
| 4 |  |
| 2 |  |
| 93 | WSAWaitForMultipleEvents |
| 46 | WSAEventSelect |
| 3 |  |
| 11 |  |
| 8 |  |
| 15 |  |
| 112 |  |
| 18 |  |
| 52 |  |
| 151 |  |
| 7 |  |
| 1 |  |
| 165 | getaddrinfo |
| 9 |  |
| 164 | freeaddrinfo |
| 12 |  |

</p></details>
<details><summary><b>KERNEL32.dll</b> (147)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 273 | DeleteCriticalSection |
| 541 | GetCurrentProcess |
| 542 | GetCurrentProcessId |
| 545 | GetCurrentThread |
| 546 | GetCurrentThreadId |
| 780 | GetThreadTimes |
| 960 | LeaveCriticalSection |
| 616 | GetLocalTime |
| 635 | GetModuleHandleA |
| 693 | GetProcAddress |
| 964 | LoadLibraryA |
| 309 | EnterCriticalSection |
| 871 | InitializeCriticalSection |
| 1105 | QueryPerformanceFrequency |
| 1104 | QueryPerformanceCounter |
| 615 | GetLastError |
| 134 | CloseHandle |
| 1320 | SetFileAttributesA |
| 1143 | ReadFile |
| 585 | GetFileAttributesExW |
| 583 | GetFileAttributesA |
| 402 | FindNextFileW |
| 379 | FindClose |
| 203 | CreateFileW |
| 535 | GetCurrentDirectoryW |
| 1488 | VerSetConditionMask |
| 1419 | Sleep |
| 750 | GetSystemTime |
| 1002 | MoveFileExA |
| 1310 | SetEndOfFile |
| 1568 | WriteConsoleW |
| 855 | HeapSize |
| 734 | GetStringTypeW |
| 699 | GetProcessHeap |
| 432 | FreeEnvironmentStringsW |
| 574 | GetEnvironmentStringsW |
| 477 | GetCommandLineW |
| 476 | GetCommandLineA |
| 455 | GetCPInfo |
| 670 | GetOEMCP |
| 440 | GetACP |
| 910 | IsValidCodePage |
| 385 | FindFirstFileExW |
| 1367 | SetStdHandle |
| 608 | GetFullPathNameW |
| 948 | LCMapStringW |
| 155 | CompareStringW |
| 787 | GetTimeFormatW |
| 552 | GetDateFormatW |
| 853 | HeapReAlloc |
| 729 | GetStdHandle |
| 1329 | SetFilePointerEx |
| 421 | FlushFileBuffers |
| 846 | HeapAlloc |
| 850 | HeapFree |
| 496 | GetConsoleCP |
| 1569 | WriteFile |
| 1140 | ReadConsoleW |
| 514 | GetConsoleMode |
| 356 | ExitProcess |
| 368 | FileTimeToSystemTime |
| 1431 | SystemTimeToTzSpecificLocalTime |
| 1061 | PeekNamedPipe |
| 597 | GetFileType |
| 590 | GetFileInformationByHandle |
| 566 | GetDriveTypeW |
| 637 | GetModuleHandleExW |
| 357 | ExitThread |
| 1376 | SetThreadAffinityMask |
| 188 | CreateEventA |
| 1412 | SetWaitableTimer |
| 254 | CreateWaitableTimerA |
| 978 | LocalFree |
| 428 | FormatMessageA |
| 1343 | SetLastError |
| 429 | FormatMessageW |
| 873 | InitializeCriticalSectionEx |
| 1422 | SleepEx |
| 742 | GetSystemDirectoryA |
| 433 | FreeLibrary |
| 782 | GetTickCount |
| 1010 | MultiByteToWideChar |
| 1549 | WideCharToMultiByte |
| 1247 | RtlUnwind |
| 1511 | WaitForSingleObjectEx |
| 575 | GetEnvironmentVariableA |
| 1491 | VerifyVersionInfoA |
| 195 | CreateFileA |
| 595 | GetFileSizeEx |
| 1429 | SwitchToThread |
| 1461 | TryEnterCriticalSection |
| 872 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1452 | TlsAlloc |
| 1454 | TlsGetValue |
| 1455 | TlsSetValue |
| 1453 | TlsFree |
| 752 | GetSystemTimeAsFileTime |
| 638 | GetModuleHandleW |
| 1235 | RtlCaptureContext |
| 1242 | RtlLookupFunctionEntry |
| 1249 | RtlVirtualUnwind |
| 1468 | UnhandledExceptionFilter |
| 1403 | SetUnhandledExceptionFilter |
| 1434 | TerminateProcess |
| 905 | IsProcessorFeaturePresent |
| 1316 | SetEvent |
| 1226 | ResetEvent |
| 898 | IsDebuggerPresent |
| 727 | GetStartupInfoW |
| 876 | InitializeSListHead |
| 249 | CreateTimerQueue |
| 1417 | SignalObjectAndWait |
| 242 | CreateThread |
| 1387 | SetThreadPriority |
| 776 | GetThreadPriority |
| 623 | GetLogicalProcessorInformation |
| 250 | CreateTimerQueueTimer |
| 120 | ChangeTimerQueueTimer |
| 283 | DeleteTimerQueueTimer |
| 656 | GetNumaHighestNodeNumber |
| 694 | GetProcessAffinityMask |
| 1197 | RegisterWaitForSingleObject |
| 1477 | UnregisterWait |
| 305 | EncodePointer |
| 434 | FreeLibraryAndExitThread |
| 634 | GetModuleFileNameW |
| 966 | LoadLibraryExW |
| 804 | GetVersionExW |
| 1493 | VirtualAlloc |
| 1499 | VirtualProtect |
| 1496 | VirtualFree |
| 303 | DuplicateHandle |
| 1208 | ReleaseSemaphore |
| 881 | InterlockedPopEntrySList |
| 882 | InterlockedPushEntrySList |
| 880 | InterlockedFlushSList |
| 1094 | QueryDepthSList |
| 1478 | UnregisterWaitEx |
| 967 | LoadLibraryW |
| 1244 | RtlPcToFileHeader |
| 1126 | RaiseException |
| 1248 | RtlUnwindEx |
| 789 | GetTimeZoneInformation |
| 278 | DeleteFileW |
| 1314 | SetEnvironmentVariableW |
| 186 | CreateDirectoryW |

</p></details>
<details><summary><b>CRYPT32.dll</b> (16)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 74 | CertGetNameStringA |
| 55 | CertFindExtension |
| 4 | CertAddCertificateContextToStore |
| 131 | CryptDecodeObjectEx |
| 62 | CertFreeCertificateChainEngine |
| 69 | CertGetCertificateChain |
| 197 | CryptQueryObject |
| 222 | CryptStringToBinaryA |
| 64 | CertFreeCertificateContext |
| 53 | CertFindCertificateInStore |
| 44 | CertEnumCertificatesInStore |
| 18 | CertCloseStore |
| 89 | CertOpenStore |
| 292 | PFXImportCertStore |
| 61 | CertFreeCertificateChain |
| 27 | CertCreateCertificateChainEngine |

</p></details>
<details><summary><b>Normaliz.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 0 | IdnToAscii |

</p></details>
<details><summary><b>pthread.dll</b> (13)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 84 | pthread_setcancelstate |
| 25 | pthread_cancel |
| 36 | pthread_create |
| 94 | pthread_testcancel |
| 53 | pthread_mutex_init |
| 57 | pthread_mutex_unlock |
| 28 | pthread_cond_init |
| 27 | pthread_cond_destroy |
| 31 | pthread_cond_wait |
| 30 | pthread_cond_timedwait |
| 54 | pthread_mutex_lock |
| 29 | pthread_cond_signal |
| 52 | pthread_mutex_destroy |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 138 | timeGetTime |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (7)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 193 | CryptAcquireContextA |
| 196 | CryptCreateHash |
| 210 | CryptGenRandom |
| 199 | CryptDestroyHash |
| 213 | CryptGetHashParam |
| 220 | CryptReleaseContext |
| 217 | CryptHashData |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | CheckCompatibility |
| 2 | GetLibMtaVersion |
| 3 | InitNetServerInterface |
| 4 | ReleaseNetServerInterface |

</p></details>
