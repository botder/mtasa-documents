# game_sa.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (104)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 601 | GetFullPathNameW |
| 622 | GetLongPathNameW |
| 1139 | ReadFile |
| 1306 | SetFileAttributesA |
| 1048 | OutputDebugStringA |
| 134 | CloseHandle |
| 609 | GetLastError |
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
| 743 | GetSystemTime |
| 610 | GetLocalTime |
| 576 | GetFileAttributesA |
| 628 | GetModuleFileNameW |
| 629 | GetModuleHandleA |
| 686 | GetProcAddress |
| 961 | LoadLibraryA |
| 813 | GlobalAlloc |
| 831 | GlobalUnlock |
| 824 | GlobalLock |
| 252 | CreateToolhelp32Snapshot |
| 1068 | Process32FirstW |
| 1070 | Process32NextW |
| 1436 | Thread32First |
| 1437 | Thread32Next |
| 932 | K32GetModuleInformation |
| 1007 | MultiByteToWideChar |
| 1296 | SetEndOfFile |
| 846 | HeapSize |
| 1354 | SetStdHandle |
| 692 | GetProcessHeap |
| 426 | FreeEnvironmentStringsW |
| 567 | GetEnvironmentStringsW |
| 471 | GetCommandLineW |
| 470 | GetCommandLineA |
| 396 | FindNextFileW |
| 373 | FindClose |
| 203 | CreateFileW |
| 1484 | VirtualProtect |
| 663 | GetOEMCP |
| 434 | GetACP |
| 907 | IsValidCodePage |
| 379 | FindFirstFileExW |
| 844 | HeapReAlloc |
| 1136 | ReadConsoleW |
| 1315 | SetFilePointerEx |
| 588 | GetFileSizeEx |
| 1496 | WaitForSingleObjectEx |
| 301 | EncodePointer |
| 265 | DecodePointer |
| 1534 | WideCharToMultiByte |
| 1330 | SetLastError |
| 863 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1438 | TlsAlloc |
| 1440 | TlsGetValue |
| 1441 | TlsSetValue |
| 1439 | TlsFree |
| 745 | GetSystemTimeAsFileTime |
| 632 | GetModuleHandleW |
| 945 | LCMapStringW |
| 613 | GetLocaleInfoW |
| 727 | GetStringTypeW |
| 449 | GetCPInfo |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 1453 | UnhandledExceptionFilter |
| 1389 | SetUnhandledExceptionFilter |
| 902 | IsProcessorFeaturePresent |
| 895 | IsDebuggerPresent |
| 720 | GetStartupInfoW |
| 867 | InitializeSListHead |
| 1049 | OutputDebugStringW |
| 427 | FreeLibrary |
| 963 | LoadLibraryExW |
| 876 | InterlockedFlushSList |
| 1235 | RtlUnwind |
| 1122 | RaiseException |
| 350 | ExitProcess |
| 631 | GetModuleHandleExW |
| 722 | GetStdHandle |
| 590 | GetFileType |
| 1553 | WriteConsoleW |
| 186 | CreateDirectoryW |
| 841 | HeapFree |
| 837 | HeapAlloc |
| 909 | IsValidLocale |
| 786 | GetUserDefaultLCID |
| 340 | EnumSystemLocalesW |
| 415 | FlushFileBuffers |
| 1554 | WriteFile |
| 490 | GetConsoleCP |
| 508 | GetConsoleMode |

</p></details>
<details><summary><b>USER32.dll</b> (5)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 663 | OpenClipboard |
| 646 | MessageBoxW |
| 232 | EmptyClipboard |
| 795 | SetClipboardData |
| 79 | CloseClipboard |

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
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 148 | timeGetTime |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | GetGameInterface |
| 2 | GetLibMtaVersion |

</p></details>
