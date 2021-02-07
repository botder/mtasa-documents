# multiplayer_sa.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (100)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 576 | GetFileAttributesA |
| 601 | GetFullPathNameW |
| 622 | GetLongPathNameW |
| 1139 | ReadFile |
| 1306 | SetFileAttributesA |
| 134 | CloseHandle |
| 609 | GetLastError |
| 1330 | SetLastError |
| 1101 | QueryPerformanceCounter |
| 862 | InitializeCriticalSection |
| 305 | EnterCriticalSection |
| 957 | LeaveCriticalSection |
| 272 | DeleteCriticalSection |
| 535 | GetCurrentProcess |
| 536 | GetCurrentProcessId |
| 1420 | TerminateProcess |
| 539 | GetCurrentThread |
| 540 | GetCurrentThreadId |
| 1044 | OpenThread |
| 773 | GetThreadTimes |
| 743 | GetSystemTime |
| 610 | GetLocalTime |
| 1484 | VirtualProtect |
| 396 | FindNextFileW |
| 629 | GetModuleHandleA |
| 686 | GetProcAddress |
| 961 | LoadLibraryA |
| 813 | GlobalAlloc |
| 831 | GlobalUnlock |
| 824 | GlobalLock |
| 975 | LocalFree |
| 252 | CreateToolhelp32Snapshot |
| 1068 | Process32FirstW |
| 1070 | Process32NextW |
| 1436 | Thread32First |
| 1437 | Thread32Next |
| 932 | K32GetModuleInformation |
| 1296 | SetEndOfFile |
| 846 | HeapSize |
| 727 | GetStringTypeW |
| 1354 | SetStdHandle |
| 415 | FlushFileBuffers |
| 692 | GetProcessHeap |
| 426 | FreeEnvironmentStringsW |
| 567 | GetEnvironmentStringsW |
| 471 | GetCommandLineW |
| 470 | GetCommandLineA |
| 449 | GetCPInfo |
| 663 | GetOEMCP |
| 373 | FindClose |
| 203 | CreateFileW |
| 1405 | Sleep |
| 628 | GetModuleFileNameW |
| 1495 | WaitForSingleObject |
| 434 | GetACP |
| 907 | IsValidCodePage |
| 379 | FindFirstFileExW |
| 588 | GetFileSizeEx |
| 490 | GetConsoleCP |
| 1315 | SetFilePointerEx |
| 1136 | ReadConsoleW |
| 508 | GetConsoleMode |
| 945 | LCMapStringW |
| 1554 | WriteFile |
| 844 | HeapReAlloc |
| 265 | DecodePointer |
| 837 | HeapAlloc |
| 841 | HeapFree |
| 1496 | WaitForSingleObjectEx |
| 863 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1438 | TlsAlloc |
| 1440 | TlsGetValue |
| 1441 | TlsSetValue |
| 1439 | TlsFree |
| 745 | GetSystemTimeAsFileTime |
| 632 | GetModuleHandleW |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 902 | IsProcessorFeaturePresent |
| 895 | IsDebuggerPresent |
| 1453 | UnhandledExceptionFilter |
| 1389 | SetUnhandledExceptionFilter |
| 720 | GetStartupInfoW |
| 867 | InitializeSListHead |
| 1007 | MultiByteToWideChar |
| 1534 | WideCharToMultiByte |
| 1049 | OutputDebugStringW |
| 301 | EncodePointer |
| 427 | FreeLibrary |
| 963 | LoadLibraryExW |
| 876 | InterlockedFlushSList |
| 1122 | RaiseException |
| 1235 | RtlUnwind |
| 350 | ExitProcess |
| 631 | GetModuleHandleExW |
| 722 | GetStdHandle |
| 590 | GetFileType |
| 1553 | WriteConsoleW |
| 186 | CreateDirectoryW |

</p></details>
<details><summary><b>USER32.dll</b> (9)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 305 | GetClientRect |
| 663 | OpenClipboard |
| 323 | GetDesktopWindow |
| 77 | ClientToScreen |
| 795 | SetClipboardData |
| 79 | CloseClipboard |
| 646 | MessageBoxW |
| 232 | EmptyClipboard |
| 491 | GetWindowRect |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (6)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 665 | RegQueryValueExW |
| 652 | RegOpenKeyExW |
| 638 | RegFlushKey |
| 612 | RegCreateKeyExW |
| 603 | RegCloseKey |
| 681 | RegSetValueExW |

</p></details>
<details><summary><b>SHELL32.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 435 | ShellExecuteA |
| 438 | ShellExecuteExW |
| 344 | SHGetFolderPathW |

</p></details>
<details><summary><b>ole32.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 40 | CoCreateInstance |
| 94 | CoInitializeEx |
| 95 | CoInitializeSecurity |
| 132 | CoSetProxyBlanket |

</p></details>
<details><summary><b>OLEAUT32.dll</b> (6)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 6 |  |
| 7 |  |
| 2 |  |
| 150 |  |
| 12 |  |
| 9 |  |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 148 | timeGetTime |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | GetLibMtaVersion |
| 2 | InitMultiplayerInterface |

</p></details>
