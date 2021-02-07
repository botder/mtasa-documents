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
| 150 | getaddrinfo |
| 9 |  |
| 149 | freeaddrinfo |
| 12 |  |

</p></details>
<details><summary><b>KERNEL32.dll</b> (143)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 272 | DeleteCriticalSection |
| 535 | GetCurrentProcess |
| 536 | GetCurrentProcessId |
| 539 | GetCurrentThread |
| 540 | GetCurrentThreadId |
| 773 | GetThreadTimes |
| 957 | LeaveCriticalSection |
| 610 | GetLocalTime |
| 629 | GetModuleHandleA |
| 686 | GetProcAddress |
| 961 | LoadLibraryA |
| 305 | EnterCriticalSection |
| 862 | InitializeCriticalSection |
| 1102 | QueryPerformanceFrequency |
| 1101 | QueryPerformanceCounter |
| 609 | GetLastError |
| 134 | CloseHandle |
| 1306 | SetFileAttributesA |
| 1139 | ReadFile |
| 578 | GetFileAttributesExW |
| 576 | GetFileAttributesA |
| 396 | FindNextFileW |
| 373 | FindClose |
| 203 | CreateFileW |
| 529 | GetCurrentDirectoryW |
| 1473 | VerSetConditionMask |
| 1405 | Sleep |
| 743 | GetSystemTime |
| 1007 | MultiByteToWideChar |
| 1296 | SetEndOfFile |
| 1553 | WriteConsoleW |
| 846 | HeapSize |
| 727 | GetStringTypeW |
| 692 | GetProcessHeap |
| 426 | FreeEnvironmentStringsW |
| 567 | GetEnvironmentStringsW |
| 471 | GetCommandLineW |
| 470 | GetCommandLineA |
| 449 | GetCPInfo |
| 663 | GetOEMCP |
| 434 | GetACP |
| 907 | IsValidCodePage |
| 379 | FindFirstFileExW |
| 1354 | SetStdHandle |
| 601 | GetFullPathNameW |
| 945 | LCMapStringW |
| 155 | CompareStringW |
| 780 | GetTimeFormatW |
| 545 | GetDateFormatW |
| 844 | HeapReAlloc |
| 722 | GetStdHandle |
| 1315 | SetFilePointerEx |
| 415 | FlushFileBuffers |
| 265 | DecodePointer |
| 837 | HeapAlloc |
| 841 | HeapFree |
| 490 | GetConsoleCP |
| 1554 | WriteFile |
| 1136 | ReadConsoleW |
| 508 | GetConsoleMode |
| 350 | ExitProcess |
| 362 | FileTimeToSystemTime |
| 1417 | SystemTimeToTzSpecificLocalTime |
| 1058 | PeekNamedPipe |
| 590 | GetFileType |
| 583 | GetFileInformationByHandle |
| 559 | GetDriveTypeW |
| 631 | GetModuleHandleExW |
| 351 | ExitThread |
| 1363 | SetThreadAffinityMask |
| 188 | CreateEventA |
| 1398 | SetWaitableTimer |
| 253 | CreateWaitableTimerA |
| 975 | LocalFree |
| 422 | FormatMessageA |
| 1330 | SetLastError |
| 423 | FormatMessageW |
| 864 | InitializeCriticalSectionEx |
| 1408 | SleepEx |
| 735 | GetSystemDirectoryA |
| 427 | FreeLibrary |
| 775 | GetTickCount |
| 1534 | WideCharToMultiByte |
| 999 | MoveFileExA |
| 1496 | WaitForSingleObjectEx |
| 568 | GetEnvironmentVariableA |
| 1476 | VerifyVersionInfoA |
| 195 | CreateFileA |
| 588 | GetFileSizeEx |
| 1415 | SwitchToThread |
| 1447 | TryEnterCriticalSection |
| 863 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1438 | TlsAlloc |
| 1440 | TlsGetValue |
| 1441 | TlsSetValue |
| 1439 | TlsFree |
| 745 | GetSystemTimeAsFileTime |
| 632 | GetModuleHandleW |
| 1453 | UnhandledExceptionFilter |
| 1389 | SetUnhandledExceptionFilter |
| 1420 | TerminateProcess |
| 902 | IsProcessorFeaturePresent |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 895 | IsDebuggerPresent |
| 720 | GetStartupInfoW |
| 867 | InitializeSListHead |
| 250 | CreateTimerQueue |
| 1403 | SignalObjectAndWait |
| 243 | CreateThread |
| 1374 | SetThreadPriority |
| 769 | GetThreadPriority |
| 617 | GetLogicalProcessorInformation |
| 251 | CreateTimerQueueTimer |
| 120 | ChangeTimerQueueTimer |
| 282 | DeleteTimerQueueTimer |
| 649 | GetNumaHighestNodeNumber |
| 687 | GetProcessAffinityMask |
| 1193 | RegisterWaitForSingleObject |
| 1462 | UnregisterWait |
| 301 | EncodePointer |
| 428 | FreeLibraryAndExitThread |
| 628 | GetModuleFileNameW |
| 963 | LoadLibraryExW |
| 795 | GetVersionExW |
| 1478 | VirtualAlloc |
| 1484 | VirtualProtect |
| 1481 | VirtualFree |
| 299 | DuplicateHandle |
| 1204 | ReleaseSemaphore |
| 878 | InterlockedPopEntrySList |
| 879 | InterlockedPushEntrySList |
| 876 | InterlockedFlushSList |
| 1091 | QueryDepthSList |
| 1463 | UnregisterWaitEx |
| 964 | LoadLibraryW |
| 1122 | RaiseException |
| 1235 | RtlUnwind |
| 782 | GetTimeZoneInformation |
| 277 | DeleteFileW |
| 1300 | SetEnvironmentVariableW |
| 186 | CreateDirectoryW |

</p></details>
<details><summary><b>CRYPT32.dll</b> (16)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 74 | CertGetNameStringA |
| 55 | CertFindExtension |
| 4 | CertAddCertificateContextToStore |
| 133 | CryptDecodeObjectEx |
| 27 | CertCreateCertificateChainEngine |
| 62 | CertFreeCertificateChainEngine |
| 298 | PFXImportCertStore |
| 227 | CryptStringToBinaryA |
| 64 | CertFreeCertificateContext |
| 53 | CertFindCertificateInStore |
| 44 | CertEnumCertificatesInStore |
| 18 | CertCloseStore |
| 89 | CertOpenStore |
| 69 | CertGetCertificateChain |
| 200 | CryptQueryObject |
| 61 | CertFreeCertificateChain |

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
| 148 | timeGetTime |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (7)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 193 | CryptAcquireContextA |
| 210 | CryptGenRandom |
| 199 | CryptDestroyHash |
| 217 | CryptHashData |
| 213 | CryptGetHashParam |
| 220 | CryptReleaseContext |
| 196 | CryptCreateHash |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | CheckCompatibility |
| 2 | GetLibMtaVersion |
| 3 | InitNetServerInterface |
| 4 | ReleaseNetServerInterface |

</p></details>
